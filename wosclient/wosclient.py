import xml.etree.ElementTree as ET

import logging
import requests

from wosclient import const
from wosclient.exceptions import ParameterException, MultipleObjectsReturned
from wosclient.util import grouper


def parse_reply(raw):
    ns = {'isi': 'http://www.isinet.com/xrpc41'}
    raw = ET.fromstring(raw)
    out = {}
    for cite in raw.findall('isi:fn/isi:map/isi:map', ns):
        cite_key = cite.attrib['name']
        meta = {}
        for val in cite.findall('isi:map/isi:val', ns):
            meta[val.attrib['name']] = val.text
        out[cite_key] = meta
    return out


def get(request_xml):
    res = requests.post(
        const.AMR_URL,
        request_xml,
        headers={
            "content-type": "application/xml"
        })
    return parse_reply(res.text)


def prepare_request(items, username, password, local_id="id",
                    appId="wosclient", allowed_keys=None):
    """
    Process the incoming items into an AMR request.

    <map name="cite_1">
        <val name="{id_type}">{value}</val>
    </map>
    """
    allowed_keys = allowed_keys or const.ALLOWED_KEYS
    map_items = ET.Element("map")
    for idx, pub in enumerate(items):
        if pub is None:
            continue
        local_id_value = pub.get(local_id) or pub.get(local_id.upper())
        if local_id_value is None:
            local_id_value = str(idx)
        this_item = ET.Element("map", name=str(local_id_value))
        for k, v in pub.items():
            if v is None or k not in const.ALLOWED_KEYS:
                msg = "Unknown key %r for prepare_request, ignored" % k
                logging.warning(msg)
                continue
            de = ET.Element("val", name=str(k).lower())
            de.text = v.strip()
            this_item.append(de)
        map_items.append(this_item)

    request_items = ET.tostring(map_items, encoding="unicode")
    xml = const.id_request_template.format(
        user=username,
        password=password,
        items=request_items,
        appId=appId)
    return xml


def query_single(pmid, doi, username, password):
    if pmid is None and doi is None:
        raise ParameterException("Please specify PubMedID or DOI or both")

    qdict = {}
    if pmid:
        qdict['pmid'] = pmid
    if doi:
        qdict['doi'] = doi

    res = prepare_request([qdict, ], username, password)

    ret = get(res)

    if len(ret) > 1:
        raise MultipleObjectsReturned("More than one object returned")

    return ret['0']


def query_multiple(iterable, username, password, batch_size=None):
    for group in grouper(iterable, batch_size or const.BATCH_SIZE):
        res = prepare_request(group, username, password)
        yield get(res)


class WoSClient(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def query_single(self, pmid=None, doi=None):
        return query_single(pmid, doi, self.username, self.password)

    def query_multiple(self, iterable):
        return query_multiple(iterable, self.username, self.password)
