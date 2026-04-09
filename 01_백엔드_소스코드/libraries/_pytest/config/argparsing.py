# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: argparsing.pyc (Python 3.11)

from __future__ import annotations
import argparse
from collections.abc import Callable
from collections.abc import Mapping
from collections.abc import Sequence
import os
import sys
from typing import Any
from typing import final
from typing import Literal
from typing import NoReturn
from exceptions import UsageError
import _pytest._io as _pytest
from _pytest.deprecated import check_ispytest
FILE_OR_DIR = 'file_or_dir'

class NotSet:
    
    def __repr__(self = None):
        return '<notset>'


NOT_SET = NotSet()
Parser = <NODE:12>()

def get_ini_default_for_type(type = None):
    '''
    Used by addini to get the default value for a given config option type, when
    default is not supplied.
    '''
    if type in ('paths', 'pathlist', 'args', 'linelist'):
        return []
    if None == 'bool':
        return False
    if None == 'int':
        return 0
    if None == 'float':
        return 0


class ArgumentError(Exception):
    '''Raised if an Argument instance is created with invalid or
    inconsistent arguments.'''
    
    def __init__(self = None, msg = None, option = None):
        self.msg = msg
        self.option_id = str(option)

    
    def __str__(self = None):
        if self.option_id:
            return f'''option {self.option_id}: {self.msg}'''
        return None.msg



class Argument:
    """Class that mimics the necessary behaviour of optparse.Option.

    It's currently a least effort implementation and ignoring choices
    and integer prefixes.

    https://docs.python.org/3/library/optparse.html#optparse-standard-option-types
    """
    
    def __init__(self = None, *names, **attrs):
        '''Store params in private vars for use in add_argument.'''
        self._attrs = attrs
        self._short_opts = []
        self._long_opts = []
        
        try:
            self.type = attrs['type']
        except KeyError:
            pass

        
        try:
            self.default = attrs['default']
        except KeyError:
            pass

        self._set_opt_strings(names)
        dest = attrs.get('dest')
        if dest:
            self.dest = dest
            return None
        if None._long_opts:
            self.dest = self._long_opts[0][2:].replace('-', '_')
            return None
        
        try:
            self.dest = self._short_opts[0][1:]
            return None
        except IndexError:
            e = None
            self.dest = '???'
            raise ArgumentError('need a long or short option', self), e
            e = None
            del e


    
    def names(self = None):
        return self._short_opts + self._long_opts

    
    def attrs(self = None):
        for attr in ('default', 'dest', 'help', self.dest):
            self._attrs[attr] = getattr(self, attr)
            except AttributeError:
                continue
            return self._attrs

    
    def _set_opt_strings(self = None, opts = None):
        '''Directly from optparse.

        Might not be necessary as this is passed to argparse later on.
        '''
        for opt in opts:
            if len(opt) < 2:
                raise ArgumentError(f'''invalid option string {opt!r}: must be at least two characters long''', self)
            if len(opt) == 2:
                if not opt[0] == '-' or opt[1] != '-':
                    raise ArgumentError(f'''invalid short option string {opt!r}: must be of the form -x, (x any non-dash char)''', self)
                self._short_opts.append(opt)
                continue
            if not opt[0:2] == '--' or opt[2] != '-':
                raise ArgumentError(f'''invalid long option string {opt!r}: must start with --, followed by non-dash''', self)
            self._long_opts.append(opt)
            return None

    
    def __repr__(self = None):
        args = []
        if self._short_opts:
            args += [
                '_short_opts: ' + repr(self._short_opts)]
        if self._long_opts:
            args += [
                '_long_opts: ' + repr(self._long_opts)]
        args += [
            'dest: ' + repr(self.dest)]
        if hasattr(self, 'type'):
            args += [
                'type: ' + repr(self.type)]
        if hasattr(self, 'default'):
            args += [
                'default: ' + repr(self.default)]
        return 'Argument({})'.format(', '.join(args))



class OptionGroup:
    '''A group of options shown in its own section.'''
    
    def __init__(self = None, arggroup = None, name = None, parser = (False,), _ispytest = ('arggroup', 'argparse._ArgumentGroup', 'name', 'str', 'parser', 'Parser | None', '_ispytest', 'bool', 'return', 'None')):
        check_ispytest(_ispytest)
        self._arggroup = arggroup
        self.name = name
        self.options = []
        self.parser = parser

    
    def addoption(self = None, *opts, **attrs):
        """Add an option to this group.

        If a shortened version of a long option is specified, it will
        be suppressed in the help. ``addoption('--twowords', '--two-words')``
        results in help showing ``--two-words`` only, but ``--twowords`` gets
        accepted **and** the automatic destination is in ``args.twowords``.

        :param opts:
            Option names, can be short or long options.
        :param attrs:
            Same attributes as the argparse library's :meth:`add_argument()
            <argparse.ArgumentParser.add_argument>` function accepts.
        """
        conflict = (lambda .0: pass# WARNING: Decompyle incomplete
)(self.options())
        if conflict:
            raise ValueError(f'''option names {conflict} already added''')
    # WARNING: Decompyle incomplete

    
    def _addoption(self = None, *opts, **attrs):
        pass
    # WARNING: Decompyle incomplete

    
    def _addoption_instance(self = None, option = None, shortupper = None):
        if not shortupper:
            for opt in option._short_opts:
                if opt[0] == '-' and opt[1].islower():
                    raise ValueError('lowercase shortoptions reserved')
                if self.parser:
                    self.parser.processoption(option)
    # WARNING: Decompyle incomplete



class PytestArgumentParser(argparse.ArgumentParser):
    pass
# WARNING: Decompyle incomplete


class DropShorterLongHelpFormatter(argparse.HelpFormatter):
    pass
# WARNING: Decompyle incomplete


class OverrideIniAction(argparse.Action):
    pass
# WARNING: Decompyle incomplete
