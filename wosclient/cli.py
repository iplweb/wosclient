# -*- coding: utf-8 -*-

"""Console script for wosclient."""
import csv
import os
import sys

import click

from wosclient import wosclient


@click.option('--password',
              help='API password',
              prompt=True,
              hide_input=True,
              default=lambda: os.environ.get('WOS_PASSWORD', ''))
@click.option('--user',
              help='API username',
              hide_input=True,
              prompt=True,
              default=lambda: os.environ.get('WOS_USER', ''))
@click.argument('infile', type=click.File('r'))
@click.option(
    '--outfile',
    default="-",
    type=click.Path(
        dir_okay=False,
        writable=True,
        readable=False,
        allow_dash=True
    ))
@click.command()
def lookup_ids(infile, outfile, user, password, args=None):
    if outfile == "-":
        outfile = sys.stdout
    else:
        outfile = open(outfile, "wb")

    def _reader():
        for row in csv.DictReader(infile):
            d = {}
            for k, v in row.items():
                d[k.lower()] = v.strip()
            yield d

    client = wosclient.WoSClient(user, password)

    writer = csv.writer(outfile)
    writer.writerow(('id', 'ut', 'doi', 'pmid', 'times cited', 'source'))
    for grp in client.query_multiple(_reader()):
        for k, item in grp.items():
            ut = item.get('ut')
            if ut is not None:
                ut = "WOS:" + ut
            writer.writerow([k, ut, item.get('doi', ""), item.get('pmid', ""),
                             item.get('timesCited', '0'),
                             item.get('sourceURL', 'N/A')])

    return 0


@click.option('--pmid', help='PubMedID (for example, 19883697)')
@click.option('--doi', help='DOI (for example, 10.1016/j.bbr.2009.10.030)')
@click.option('--password',
              help='API password',
              prompt=True,
              hide_input=True,
              default=lambda: os.environ.get('WOS_PASSWORD', ''))
@click.option('--user',
              help='API username',
              prompt=True,
              default=lambda: os.environ.get('WOS_USER', ''))
@click.command()
def main(pmid, doi, user, password, args=None):
    if pmid is None and doi is None:
        click.echo("Please specify DOI or PubMedID")
        return 1

    client = wosclient.WoSClient(user, password)
    result = client.query_single(pmid, doi)

    click.echo(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
