
sofficehelpers
==============

This is a small, highly opinionated, and not generally useful package developed
to deal with soffice/LibreOffice files in the Tendril framework.

Various other packages may exist to perform the same tasks and much more, and you
should consider using them instead.

At present, the only script this file contains is the ``ssconverter`` script, which
converts a Spreadsheet into csv files.

The need for this package exists because the LibreOffice API requires you to use
the same Python version as is built into LibreOffice, which in the case of Ubuntu
14.04 is Python 3.4.

Installation
------------

This package has been tested only with python 3.4 and the LibreOffice installed
from standard Ubuntu 14.04 repositories.

This package can be installed from pypi using pip::

    $ pip install sofficehelpers

Or by using setup.py::

    $ python3 setup.py install

Usage
-----

TODO

Downloads and Documentation
---------------------------

The simplest way to obtain the source for this package is to clone the git repository::

    git clone https://github.com/chintal/tendril-sofficehelpers.git sofficehelpers

The latest version of the documentation can be found at
`ReadTheDocs <http://sofficehelpers.readthedocs.org/en/latest/index.html>`_.

License
-------

sofficehelpers is distributed under the LGPLv2.1+ license.



