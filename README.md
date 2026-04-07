# wosclient

[![Tests](https://github.com/iplweb/wosclient/actions/workflows/test.yml/badge.svg)](https://github.com/iplweb/wosclient/actions/workflows/test.yml)
[![PyPI Version](https://img.shields.io/pypi/v/wosclient.svg)](https://pypi.org/project/wosclient/)
[![License](https://img.shields.io/pypi/l/wosclient.svg)](LICENSE)

Web of Science Article Match Retrieval Client for Python by IPLweb.

This product is not endorsed or connected with Clarivate Analytics in any way.

<p align="center">
  <b>Support graciously provided by</b><br><br>
  <a href="https://www.iplweb.pl"><img src="https://www.iplweb.pl/images/ipl-logo-large.png" width="150" alt="IPL Web"></a>
</p>

## Features

- Query the Article Match Retrieval API of Web of Science Core Collection
- CLI commands `wosclient` and `lookup_ids` for batch lookups from CSV files
- Credentials via command-line prompts or environment variables (`WOS_USER`, `WOS_PASSWORD`)
- Uses [Requests](https://docs.python-requests.org/) for HTTP and generators for memory efficiency

## Supported Python versions

| Python | 3.9 | 3.10 | 3.11 | 3.12 | 3.13 |
|--------|-----|------|------|------|------|
|        | ✓   | ✓    | ✓    | ✓    | ✓    |

## Installation

### Using uv (recommended)

```bash
uv add wosclient
```

### Using pip

```bash
pip install wosclient
```

## Usage

The `lookup_ids` command looks up articles from a CSV file against the Web of Science API:

```shell
$ lookup_ids --help
Usage: lookup_ids [OPTIONS] INFILE

Options:
  --outfile PATH
  --password TEXT  API password
  --user TEXT      API username
  --help           Show this message and exit.
```

You can set credentials via environment variables instead of being prompted:

```shell
export WOS_USER=username
export WOS_PASSWORD=password
```

Then run a lookup:

```shell
$ lookup_ids tests/example.csv
id,ut,doi,pmid,times cited,source
0,WOS:000276621200002,10.1016/j.bbr.2009.10.030,19883697,123,...
1,WOS:000299789100009,10.1080/09602011.2011.621275,22011016,40,...
```

## License

MIT — see [LICENSE](LICENSE) for details.
