# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
Code coverage measurement for Python.

Ned Batchelder
https://coverage.readthedocs.io

'''
from __future__ import annotations
from coverage.version import __version__, version_info
from coverage.control import Coverage, process_startup
from coverage.data import CoverageData
from coverage.exceptions import CoverageException
from coverage.plugin import CodeRegion, CoveragePlugin, FileReporter, FileTracer
coverage = Coverage
