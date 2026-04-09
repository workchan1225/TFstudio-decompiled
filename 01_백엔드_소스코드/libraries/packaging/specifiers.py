# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: specifiers.pyc (Python 3.11)

'''
.. testsetup::

    from packaging.specifiers import Specifier, SpecifierSet, InvalidSpecifier
    from packaging.version import Version
'''
from __future__ import annotations
import abc
import itertools
import re
from typing import Callable, Iterable, Iterator, TypeVar, Union
from utils import canonicalize_version
from version import Version
UnparsedVersion = Union[(Version, str)]
UnparsedVersionVar = TypeVar('UnparsedVersionVar', bound = UnparsedVersion)
CallableOperator = Callable[([
    Version,
    str], bool)]

def _coerce_version(version = None):
    if not isinstance(version, Version):
        version = Version(version)
    return version


class InvalidSpecifier(ValueError):
    '''
    Raised when attempting to create a :class:`Specifier` with a specifier
    string that is invalid.

    >>> Specifier("lolwat")
    Traceback (most recent call last):
        ...
    packaging.specifiers.InvalidSpecifier: Invalid specifier: \'lolwat\'
    '''
    pass


def BaseSpecifier():
    '''BaseSpecifier'''
    __str__ = (lambda self = None: pass)()
    __hash__ = (lambda self = None: pass)()
    __eq__ = (lambda self = None, other = None: pass)()
    prereleases = (lambda self = None: pass)()()
    prereleases = (lambda self = None, value = None: pass)()
    contains = (lambda self = None, item = None, prereleases = abc.abstractmethod: pass)()
    filter = (lambda self = None, iterable = None, prereleases = abc.abstractmethod: pass)()

BaseSpecifier = <NODE:27>(BaseSpecifier, 'BaseSpecifier', metaclass = abc.ABCMeta)

class Specifier(BaseSpecifier):
    '''This class abstracts handling of version specifiers.

    .. tip::

        It is generally not required to instantiate this manually. You should instead
        prefer to work with :class:`SpecifierSet` instead, which can parse
        comma-separated version specifiers (which is what package metadata contains).
    '''
    _operator_regex_str = '\n        (?P<operator>(~=|==|!=|<=|>=|<|>|===))\n        '
    _version_regex_str = "\n        (?P<version>\n            (?:\n                # The identity operators allow for an escape hatch that will\n                # do an exact string match of the version you wish to install.\n                # This will not be parsed by PEP 440 and we cannot determine\n                # any semantic meaning from it. This operator is discouraged\n                # but included entirely as an escape hatch.\n                (?<====)  # Only match for the identity operator\n                \\s*\n                [^\\s;)]*  # The arbitrary version can be just about anything,\n                          # we match everything except for whitespace, a\n                          # semi-colon for marker support, and a closing paren\n                          # since versions can be enclosed in them.\n            )\n            |\n            (?:\n                # The (non)equality operators allow for wild card and local\n                # versions to be specified so we have to define these two\n                # operators separately to enable that.\n                (?<===|!=)            # Only match for equals and not equals\n\n                \\s*\n                v?\n                (?:[0-9]+!)?          # epoch\n                [0-9]+(?:\\.[0-9]+)*   # release\n\n                # You cannot use a wild card and a pre-release, post-release, a dev or\n                # local version together so group them with a | and make them optional.\n                (?:\n                    \\.\\*  # Wild card syntax of .*\n                    |\n                    (?:                                  # pre release\n                        [-_\\.]?\n                        (alpha|beta|preview|pre|a|b|c|rc)\n                        [-_\\.]?\n                        [0-9]*\n                    )?\n                    (?:                                  # post release\n                        (?:-[0-9]+)|(?:[-_\\.]?(post|rev|r)[-_\\.]?[0-9]*)\n                    )?\n                    (?:[-_\\.]?dev[-_\\.]?[0-9]*)?         # dev release\n                    (?:\\+[a-z0-9]+(?:[-_\\.][a-z0-9]+)*)? # local\n                )?\n            )\n            |\n            (?:\n                # The compatible operator requires at least two digits in the\n                # release segment.\n                (?<=~=)               # Only match for the compatible operator\n\n                \\s*\n                v?\n                (?:[0-9]+!)?          # epoch\n                [0-9]+(?:\\.[0-9]+)+   # release  (We have a + instead of a *)\n                (?:                   # pre release\n                    [-_\\.]?\n                    (alpha|beta|preview|pre|a|b|c|rc)\n                    [-_\\.]?\n                    [0-9]*\n                )?\n                (?:                                   # post release\n                    (?:-[0-9]+)|(?:[-_\\.]?(post|rev|r)[-_\\.]?[0-9]*)\n                )?\n                (?:[-_\\.]?dev[-_\\.]?[0-9]*)?          # dev release\n            )\n            |\n            (?:\n                # All other operators only allow a sub set of what the\n                # (non)equality operators do. Specifically they do not allow\n                # local versions to be specified nor do they allow the prefix\n                # matching wild cards.\n                (?<!==|!=|~=)         # We have special cases for these\n                                      # operators so we want to make sure they\n                                      # don't match here.\n\n                \\s*\n                v?\n                (?:[0-9]+!)?          # epoch\n                [0-9]+(?:\\.[0-9]+)*   # release\n                (?:                   # pre release\n                    [-_\\.]?\n                    (alpha|beta|preview|pre|a|b|c|rc)\n                    [-_\\.]?\n                    [0-9]*\n                )?\n                (?:                                   # post release\n                    (?:-[0-9]+)|(?:[-_\\.]?(post|rev|r)[-_\\.]?[0-9]*)\n                )?\n                (?:[-_\\.]?dev[-_\\.]?[0-9]*)?          # dev release\n            )\n        )\n        "
    _regex = re.compile('^\\s*' + _operator_regex_str + _version_regex_str + '\\s*$', re.VERBOSE | re.IGNORECASE)
    _operators = {
        '~=': 'compatible',
        '==': 'equal',
        '!=': 'not_equal',
        '<=': 'less_than_equal',
        '>=': 'greater_than_equal',
        '<': 'less_than',
        '>': 'greater_than',
        '===': 'arbitrary' }
    
    def __init__(self = None, spec = None, prereleases = None):
        '''Initialize a Specifier instance.

        :param spec:
            The string representation of a specifier which will be parsed and
            normalized before use.
        :param prereleases:
            This tells the specifier if it should accept prerelease versions if
            applicable or not. The default of ``None`` will autodetect it from the
            given specifiers.
        :raises InvalidSpecifier:
            If the given specifier is invalid (i.e. bad syntax).
        '''
        match = self._regex.search(spec)
        if not match:
            raise InvalidSpecifier(f'''Invalid specifier: {spec!r}''')
        self._spec = (match.group('operator').strip(), match.group('version').strip())
        self._prereleases = prereleases

    prereleases = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    prereleases = (lambda self = None, value = None: self._prereleases = value)()
    operator = (lambda self = None: self._spec[0])()
    version = (lambda self = None: self._spec[1])()
    
    def __repr__(self = None):
        """A representation of the Specifier that shows all internal state.

        >>> Specifier('>=1.0.0')
        <Specifier('>=1.0.0')>
        >>> Specifier('>=1.0.0', prereleases=False)
        <Specifier('>=1.0.0', prereleases=False)>
        >>> Specifier('>=1.0.0', prereleases=True)
        <Specifier('>=1.0.0', prereleases=True)>
        """
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self = None):
        """A string representation of the Specifier that can be round-tripped.

        >>> str(Specifier('>=1.0.0'))
        '>=1.0.0'
        >>> str(Specifier('>=1.0.0', prereleases=False))
        '>=1.0.0'
        """
        pass
    # WARNING: Decompyle incomplete

    _canonical_spec = (lambda self = None: canonical_version = canonicalize_version(self._spec[1], strip_trailing_zero = self._spec[0] != '~=')(self._spec[0], canonical_version))()
    
    def __hash__(self = None):
        return hash(self._canonical_spec)

    
    def __eq__(self = None, other = None):
        '''Whether or not the two Specifier-like objects are equal.

        :param other: The other object to check against.

        The value of :attr:`prereleases` is ignored.

        >>> Specifier("==1.2.3") == Specifier("== 1.2.3.0")
        True
        >>> (Specifier("==1.2.3", prereleases=False) ==
        ...  Specifier("==1.2.3", prereleases=True))
        True
        >>> Specifier("==1.2.3") == "==1.2.3"
        True
        >>> Specifier("==1.2.3") == Specifier("==1.2.4")
        False
        >>> Specifier("==1.2.3") == Specifier("~=1.2.3")
        False
        '''
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

    
    def _compare_compatible(self = None, prospective = None, spec = None):
