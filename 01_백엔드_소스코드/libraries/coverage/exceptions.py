# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

'''Exceptions coverage.py can raise.'''
from __future__ import annotations
from typing import Any

class CoverageException(Exception):
    pass
# WARNING: Decompyle incomplete


class ConfigError(CoverageException):
    '''A problem with a config file, or a value in one.'''
    pass


class DataError(CoverageException):
    '''An error in using a data file.'''
    pass


class NoDataError(CoverageException):
    """We didn't have data to work with."""
    pass


class NoSource(CoverageException):
    """We couldn't find the source for a module."""
    pass


class NoCode(NoSource):
    """We couldn't find any code at all."""
    pass


class NotPython(CoverageException):
    '''A source file turned out not to be parsable Python.'''
    pass


class PluginError(CoverageException):
    '''A plugin misbehaved.'''
    pass


class _ExceptionDuringRun(CoverageException):
    '''An exception happened while running customer code.

    Construct it with three arguments, the values from `sys.exc_info`.

    '''
    pass


class CoverageWarning(Warning):
    '''A warning from Coverage.py.'''
    pass
