#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import pytest
import requests
from click.testing import CliRunner
from mock import Mock

from wosclient import cli, util, wosclient
from wosclient.wosclient import WoSClient


@pytest.fixture(scope="session")
def example_csv_path():
    return os.path.join(os.path.dirname(__file__), "example.csv")


@pytest.fixture(scope="session")
def example_reply_path():
    return os.path.join(os.path.dirname(__file__), "example_reply.xml")


@pytest.fixture(scope="session")
def example_reply(example_reply_path):
    return open(example_reply_path, "rb").read()


@pytest.fixture(scope="session")
def example_single_reply_path():
    return os.path.join(os.path.dirname(__file__), "example_single_reply.xml")


@pytest.fixture(scope="session")
def example_single_reply(example_single_reply_path):
    return open(example_single_reply_path, "rb").read()


def test_grouper():
    i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    r = util.grouper(i, 3)
    assert len(list(r)) == 4


def test_parse_reply(example_reply):
    res = wosclient.parse_reply(example_reply)
    assert res["0"]["timesCited"] == "123"


def test_prepare_request():
    res = wosclient.prepare_request(
        [
            {"id": "31337", "pmid": "123456", "doi": "7890"},
        ],
        "user",
        "pass",
    )

    assert "b'" not in res
    assert "wosclient" in res


def test_get(mocker):
    mocker.patch("requests.post")
    mocker.patch("wosclient.wosclient.parse_reply")

    wosclient.get("")

    requests.post.assert_called_once()
    wosclient.parse_reply.assert_called_once()


def test_get_with_reply(mocker, example_reply):
    m = Mock()
    m.text = example_reply
    mocker.patch("requests.post", return_value=m)

    res = wosclient.get("")
    assert res["1"]["timesCited"] == "40"


def test_query_single(mocker, example_single_reply):
    m = Mock()
    m.text = example_single_reply
    mocker.patch("requests.post", return_value=m)

    res = wosclient.query_single("31337", None, None, None)
    assert res["timesCited"] == "123"


def test_query_multiple(mocker, example_reply):
    m = Mock()
    m.text = example_reply
    mocker.patch("requests.post", return_value=m)

    res = wosclient.query_multiple(
        [
            {"id": "1", "pmid": "foo"},
            {"id": "2", "pmid": "foo"},
            {"id": "3", "pmid": "foo"},
        ],
        None,
        None,
    )
    res = list(res)

    assert len(list(res)) == 1


def test_WoSClient(mocker, example_single_reply):
    m = Mock()
    m.text = example_single_reply
    mocker.patch("requests.post", return_value=m)

    WoSClient("foo", "bar").query_single("pmid")
    list(
        WoSClient("foo", "bar").query_multiple(
            [
                {"pmid": "foo"},
            ]
        )
    )


def test_cli_main(mocker, example_single_reply):
    m = Mock()
    m.text = example_single_reply
    mocker.patch("requests.post", return_value=m)

    runner = CliRunner()

    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "Please specify DOI or PubMedID" in result.output

    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0

    result = runner.invoke(
        cli.main,
        args=[
            "--doi=test",
        ],
    )
    assert result.exit_code == 0
    assert "timesCited" in result.output


def test_cli_lookup_ids(mocker, example_reply, example_csv_path):
    m = Mock()
    m.text = example_reply
    mocker.patch("requests.post", return_value=m)

    runner = CliRunner()

    result = runner.invoke(cli.lookup_ids)
    assert result.exit_code == 2
    assert "Error: Missing argument 'INFILE'" in result.output

    result = runner.invoke(
        cli.lookup_ids,
        [
            example_csv_path,
        ],
    )
    assert result.exit_code == 0
    assert "times cited" in result.output
