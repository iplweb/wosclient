=========================
Web of Science API Client
=========================


.. image:: https://img.shields.io/pypi/v/wosclient.svg
        :target: https://pypi.python.org/pypi/wosclient

.. image:: https://img.shields.io/travis/iplweb/wosclient.svg
        :target: https://travis-ci.org/iplweb/wosclient

.. image:: https://readthedocs.org/projects/wosclient/badge/?version=latest
        :target: https://wosclient.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/iplweb/wosclient/shield.svg
     :target: https://pyup.io/repos/github/iplweb/wosclient/
     :alt: Updates



Web of Science Article Match Retrival Client for Python 3.6 by IPLweb.

This product is not endorsed or connected with Clarivate Analytics in any way.


* Free software: MIT license
* Documentation: https://wosclient.readthedocs.io.


Features
--------

* query the Article Match Retrival API of Web of Science Core Collection,
* internally uses requests_ to handle web traffic and generators_ to save
  memory, Click_ for handling of the command-line,
* supports Python 3.6.

.. _Requests: http://docs.python-requests.org/en/master/
.. _generators: https://wiki.python.org/moin/Generators
.. _Click: http://click.pocoo.org/5/

Example use
-----------

Please review the original README file at https://github.com/Clarivate-SAR/wos-amr .
``wosclient`` module, after installation, provides a command called ``lookup_ids``
which should behave in a similar way, as the ``lookup_ids.py`` example in original
module in Clarivate-SAR repo. There are some minor improvements, though,
like the outfile is stdout by default, you can pass username and password
in the command line, check it out:

.. code-block:: shell

  $ lookup_ids --help                                                                                                     (env: wosclient) 2 ↵
  Usage: lookup_ids [OPTIONS] INFILE

  Options:
  --outfile PATH
  --password TEXT  API password
  --user TEXT      API username
  --help           Show this message and exit.

  $ # These are completely optional, you will be prompted:
  # export WOS_USER=username
  # export WOS_PASSWORD=Password

  $ lookup_ids tests/example.csv
  User [username]:
  Password [password]:
  id,ut,doi,pmid,times cited,source
  # ... after a second
  0,WOS:000276621200002,10.1016/j.bbr.2009.10.030,19883697,123,http://gateway.webofknowledge.com/gateway/Gateway.cgi?GWVersion=2&SrcApp=PARTNER_APP&SrcAuth=LinksAMR&KeyUT=WOS:000276621200002&DestLinkType=FullRecord&DestApp=ALL_WOS&UsrCustomerID=536ab1eb96204d8944f0b2ff5513dbea
  1,WOS:000299789100009,10.1080/09602011.2011.621275,22011016,40,http://gateway.webofknowledge.com/gateway/Gateway.cgi?GWVersion=2&SrcApp=PARTNER_APP&SrcAuth=LinksAMR&KeyUT=WOS:000299789100009&DestLinkType=FullRecord&DestApp=ALL_WOS&UsrCustomerID=536ab1eb96204d8944f0b2ff5513dbea
  2,WOS:000300816600006,10.1016/j.neuropsychologia.2011.12.011,22223077,25,http://gateway.webofknowledge.com/gateway/Gateway.cgi?GWVersion=2&SrcApp=PARTNER_APP&SrcAuth=LinksAMR&KeyUT=WOS:000300816600006&DestLinkType=FullRecord&DestApp=ALL_WOS&UsrCustomerID=536ab1eb96204d8944f0b2ff5513dbea



Credits
-------


This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
