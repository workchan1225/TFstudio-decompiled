# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: python.pyc (Python 3.11)

'''Python source expertise for coverage.py'''
from __future__ import annotations
import os.path as os
import types
import zipimport
from collections.abc import Iterable
from typing import TYPE_CHECKING
from coverage import env
from coverage.exceptions import CoverageException, NoSource
from coverage.files import canonical_filename, relative_filename, zip_location
from coverage.misc import isolate_module, join_regex
from coverage.parser import PythonParser
from coverage.phystokens import source_encoding, source_token_lines
from coverage.plugin import CodeRegion, FileReporter
from coverage.regions import code_regions
from coverage.types import TArc, TLineNo, TMorf, TSourceTokenLines
if TYPE_CHECKING:
    from coverage import Coverage
os = isolate_module(os)
open = open

def read_python_source(filename = None):
    '''Read the Python source text from `filename`.

    Returns bytes.

    '''
    f = open(filename, 'rb')
    source = f.read()
    None(None, None)


def get_python_source(filename = None):
    '''Return the source code, as unicode.'''
    (base, ext) = os.path.splitext(filename)
    if ext == '.py' and env.WINDOWS:
        exts = [
            '.py',
            '.pyw']
    else:
        exts = [
            ext]
# WARNING: Decompyle incomplete


def get_zip_bytes(filename = None):
    """Get data from `filename` if it is a zip file path.

    Returns the bytestring data read from the zip file, or None if no zip file
    could be found or `filename` isn't in it.  The data returned will be
    an empty string if the file is empty.

    """
    zipfile_inner = zip_location(filename)
# WARNING: Decompyle incomplete


def source_for_file(filename = None):
