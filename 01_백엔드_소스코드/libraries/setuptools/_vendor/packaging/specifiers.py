# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: specifiers.pyc (Python 3.11)

import abc
import functools
import itertools
import re
import warnings
from typing import Callable, Dict, Iterable, Iterator, List, Optional, Pattern, Set, Tuple, TypeVar, Union
from utils import canonicalize_version
from version import LegacyVersion, Version, parse
ParsedVersion = Union[(Version, LegacyVersion)]
UnparsedVersion = Union[(Version, LegacyVersion, str)]
VersionTypeVar = TypeVar('VersionTypeVar', bound = UnparsedVersion)
CallableOperator = Callable[([
    ParsedVersion,
    str], bool)]

class InvalidSpecifier(ValueError):
    '''
    An invalid specifier was found, users should refer to PEP 440.
    '''
    pass


def BaseSpecifier():
    '''BaseSpecifier'''
    __str__ = (lambda self = None: pass)()
    __hash__ = (lambda self = None: pass)()
    __eq__ = (lambda self = None, other = None: pass)()
    prereleases = (lambda self = None: pass)()
    prereleases = (lambda self = None, value = None: pass)()
    contains = (lambda self = None, item = None, prereleases = abc.abstractmethod: pass)()
    filter = (lambda self = None, iterable = None, prereleases = abc.abstractmethod: pass)()

BaseSpecifier = <NODE:27>(BaseSpecifier, 'BaseSpecifier', metaclass = abc.ABCMeta)

class _IndividualSpecifier(BaseSpecifier):
    _regex: Pattern[str] = { }
    
    def __init__(self = None, spec = None, prereleases = None):
        match = self._regex.search(spec)
        if not match:
            raise InvalidSpecifier(f'''Invalid specifier: \'{spec}\'''')
        self._spec = (match.group('operator').strip(), match.group('version').strip())
        self._prereleases = prereleases

    
    def __repr__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self = None):
        pass
    # WARNING: Decompyle incomplete

    _canonical_spec = (lambda self = None: (self._spec[0], canonicalize_version(self._spec[1])))()
    
    def __hash__(self = None):
        return hash(self._canonical_spec)

    
    def __eq__(self = None, other = None):
        if isinstance(other, str):
            
            try:
                other = self.__class__(str(other))
            except InvalidSpecifier:
                return 
                if not isinstance(other, self.__class__):
                    return NotImplemented
                return None._canonical_spec == other._canonical_spec


    
    def _get_operator(self = None, op = None):
        operator_callable = getattr(self, f'''_compare_{self._operators[op]}''')
        return operator_callable

    
    def _coerce_version(self = None, version = None):
        if not isinstance(version, (LegacyVersion, Version)):
            version = parse(version)
        return version

    operator = (lambda self = None: self._spec[0])()
    version = (lambda self = None: self._spec[1])()
    prereleases = (lambda self = None: self._prereleases)()
    prereleases = (lambda self = None, value = None: self._prereleases = value)()
    
    def __contains__(self = None, item = None):
        return self.contains(item)

    
    def contains(self = None, item = None, prereleases = None):
        pass
    # WARNING: Decompyle incomplete

    
    def filter(self = None, iterable = None, prereleases = None):
        pass
    # WARNING: Decompyle incomplete



class LegacySpecifier(_IndividualSpecifier):
    pass
# WARNING: Decompyle incomplete


def _require_version_compare(fn = None):
    pass
# WARNING: Decompyle incomplete


class Specifier(_IndividualSpecifier):
    _regex_str = "\n        (?P<operator>(~=|==|!=|<=|>=|<|>|===))\n        (?P<version>\n            (?:\n                # The identity operators allow for an escape hatch that will\n                # do an exact string match of the version you wish to install.\n                # This will not be parsed by PEP 440 and we cannot determine\n                # any semantic meaning from it. This operator is discouraged\n                # but included entirely as an escape hatch.\n                (?<====)  # Only match for the identity operator\n                \\s*\n                [^\\s]*    # We just match everything, except for whitespace\n                          # since we are only testing for strict identity.\n            )\n            |\n            (?:\n                # The (non)equality operators allow for wild card and local\n                # versions to be specified so we have to define these two\n                # operators separately to enable that.\n                (?<===|!=)            # Only match for equals and not equals\n\n                \\s*\n                v?\n                (?:[0-9]+!)?          # epoch\n                [0-9]+(?:\\.[0-9]+)*   # release\n                (?:                   # pre release\n                    [-_\\.]?\n                    (a|b|c|rc|alpha|beta|pre|preview)\n                    [-_\\.]?\n                    [0-9]*\n                )?\n                (?:                   # post release\n                    (?:-[0-9]+)|(?:[-_\\.]?(post|rev|r)[-_\\.]?[0-9]*)\n                )?\n\n                # You cannot use a wild card and a dev or local version\n                # together so group them with a | and make them optional.\n                (?:\n                    (?:[-_\\.]?dev[-_\\.]?[0-9]*)?         # dev release\n                    (?:\\+[a-z0-9]+(?:[-_\\.][a-z0-9]+)*)? # local\n                    |\n                    \\.\\*  # Wild card syntax of .*\n                )?\n            )\n            |\n            (?:\n                # The compatible operator requires at least two digits in the\n                # release segment.\n                (?<=~=)               # Only match for the compatible operator\n\n                \\s*\n                v?\n                (?:[0-9]+!)?          # epoch\n                [0-9]+(?:\\.[0-9]+)+   # release  (We have a + instead of a *)\n                (?:                   # pre release\n                    [-_\\.]?\n                    (a|b|c|rc|alpha|beta|pre|preview)\n                    [-_\\.]?\n                    [0-9]*\n                )?\n                (?:                                   # post release\n                    (?:-[0-9]+)|(?:[-_\\.]?(post|rev|r)[-_\\.]?[0-9]*)\n                )?\n                (?:[-_\\.]?dev[-_\\.]?[0-9]*)?          # dev release\n            )\n            |\n            (?:\n                # All other operators only allow a sub set of what the\n                # (non)equality operators do. Specifically they do not allow\n                # local versions to be specified nor do they allow the prefix\n                # matching wild cards.\n                (?<!==|!=|~=)         # We have special cases for these\n                                      # operators so we want to make sure they\n                                      # don't match here.\n\n                \\s*\n                v?\n                (?:[0-9]+!)?          # epoch\n                [0-9]+(?:\\.[0-9]+)*   # release\n                (?:                   # pre release\n                    [-_\\.]?\n                    (a|b|c|rc|alpha|beta|pre|preview)\n                    [-_\\.]?\n                    [0-9]*\n                )?\n                (?:                                   # post release\n                    (?:-[0-9]+)|(?:[-_\\.]?(post|rev|r)[-_\\.]?[0-9]*)\n                )?\n                (?:[-_\\.]?dev[-_\\.]?[0-9]*)?          # dev release\n            )\n        )\n        "
    _regex = re.compile('^\\s*' + _regex_str + '\\s*$', re.VERBOSE | re.IGNORECASE)
    _operators = {
        '~=': 'compatible',
        '==': 'equal',
        '!=': 'not_equal',
        '<=': 'less_than_equal',
        '>=': 'greater_than_equal',
        '<': 'less_than',
        '>': 'greater_than',
        '===': 'arbitrary' }
    _compare_compatible = (lambda self = None, prospective = None, spec = _require_version_compare:
