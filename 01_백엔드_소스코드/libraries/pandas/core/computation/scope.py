# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scope.pyc (Python 3.11)

'''
Module for scope operations
'''
from __future__ import annotations
from collections import ChainMap
import datetime
import inspect
from io import StringIO
import itertools
import pprint
import struct
import sys
from typing import TypeVar
import numpy as np
from pandas._libs.tslibs import Timestamp
from pandas.errors import UndefinedVariableError
_KT = TypeVar('_KT')
_VT = TypeVar('_VT')

def DeepChainMap():
    '''DeepChainMap'''
    __doc__ = '\n    Variant of ChainMap that allows direct updates to inner scopes.\n\n    Only works when all passed mapping are mutable.\n    '
    
    def __setitem__(self = None, key = None, value = None):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = value
                return None
            self.maps[0][key] = value
            return None

    
    def __delitem__(self = None, key = None):
        """
        Raises
        ------
        KeyError
            If `key` doesn't exist.
        """
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return None
            raise KeyError(key)


DeepChainMap = <NODE:27>(DeepChainMap, 'DeepChainMap', ChainMap[(_KT, _VT)])

def ensure_scope(level = None, global_dict = None, local_dict = None, resolvers = (None, None, (), None), target = ('level', 'int', 'return', 'Scope')):
    '''Ensure that we are grabbing the correct scope.'''
    return Scope(level + 1, global_dict = global_dict, local_dict = local_dict, resolvers = resolvers, target = target)


def _replacer(x = None):
    """
    Replace a number with its hexadecimal representation. Used to tag
    temporary variables with their calling scope's id.
    """
    
    try:
        hexin = ord(x)
    except TypeError:
        hexin = x

    return hex(hexin)


def _raw_hex_id(obj = None):
    '''Return the padded hexadecimal id of ``obj``.'''
    packed = struct.pack('@P', id(obj))
    return (lambda .0: [ _replacer(x) for x in .0 ])(packed())

DEFAULT_GLOBALS = {
    'Timestamp': Timestamp,
    'datetime': datetime.datetime,
    'True': True,
    'False': False,
    'list': list,
    'tuple': tuple,
    'inf': np.inf,
    'Inf': np.inf }

def _get_pretty_string(obj = None):
    '''
    Return a prettier version of obj.

    Parameters
    ----------
    obj : object
        Object to pretty print

    Returns
    -------
    str
        Pretty print object repr
    '''
    sio = StringIO()
    pprint.pprint(obj, stream = sio)
    return sio.getvalue()


class Scope:
    '''
    Object to hold scope, with a few bells to deal with some custom syntax
    and contexts added by pandas.

    Parameters
    ----------
    level : int
    global_dict : dict or None, optional, default None
    local_dict : dict or Scope or None, optional, default None
    resolvers : list-like or None, optional, default None
    target : object

    Attributes
    ----------
    level : int
    scope : DeepChainMap
    target : object
    temps : dict
    '''
    temps: 'dict' = [
        'level',
        'resolvers',
        'scope',
        'target',
        'temps']
    
    def __init__(self, level = None, global_dict = None, local_dict = None, resolvers = (None, None, (), None), target = ('level', 'int', 'return', 'None')):
        self.level = level + 1
        self.scope = DeepChainMap(DEFAULT_GLOBALS.copy())
        self.target = target
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        scope_keys = _get_pretty_string(list(self.scope.keys()))
        res_keys = _get_pretty_string(list(self.resolvers.keys()))
        return f'''{type(self).__name__}(scope={scope_keys}, resolvers={res_keys})'''

    has_resolvers = (lambda self = None: bool(len(self.resolvers)))()
    
    def resolve(self = None, key = None, is_local = None):
        """
        Resolve a variable name in a possibly local context.

        Parameters
        ----------
        key : str
            A variable name
        is_local : bool
            Flag indicating whether the variable is local or not (prefixed with
            the '@' symbol)

        Returns
        -------
        value : object
            The value of a particular variable
        """
        pass
    # WARNING: Decompyle incomplete

    
    def swapkey(self = None, old_key = None, new_key = None, new_value = (None,)):
        '''
        Replace a variable name, with a potentially new value.

        Parameters
        ----------
        old_key : str
            Current variable name to replace
        new_key : str
            New variable name to replace `old_key` with
        new_value : object
            Value to be replaced along with the possible renaming
        '''
        if self.has_resolvers:
            maps = self.resolvers.maps + self.scope.maps
        else:
            maps = self.scope.maps
        maps.append(self.temps)
        for mapping in maps:
            if old_key in mapping:
                mapping[new_key] = new_value
                return None
            return None

    
    def _get_vars(self = None, stack = None, scopes = None):
        """
        Get specifically scoped variables from a list of stack frames.

        Parameters
        ----------
        stack : list
            A list of stack frames as returned by ``inspect.stack()``
        scopes : sequence of strings
            A sequence containing valid stack frame attribute names that
            evaluate to a dictionary. For example, ('locals', 'globals')
        """
        variables = itertools.product(scopes, stack)
        for frame, _, _, _, _, _ in variables:
            d = getattr(frame, f'''f_{scope}''')
            self.scope = DeepChainMap(self.scope.new_child(d))
            del frame
            del frame
            return None

    
    def _update(self = None, level = None):
        '''
        Update the current scope by going back `level` levels.

        Parameters
        ----------
        level : int
        '''
        sl = level + 1
        stack = inspect.stack()
        
        try:
            self._get_vars(stack[:sl], scopes = [
                'locals'])
            del stack[:]
            del stack
            return None
        except:
            del stack[:]
            del stack


    
    def add_tmp(self = None, value = None):
        '''
        Add a temporary variable to the scope.

        Parameters
        ----------
        value : object
            An arbitrary object to be assigned to a temporary variable.

        Returns
        -------
        str
            The name of the temporary variable created.
        '''
        name = f'''{type(value).__name__}_{self.ntemps}_{_raw_hex_id(self)}'''
    # WARNING: Decompyle incomplete

    ntemps = (lambda self = None: len(self.temps))()
    full_scope = (lambda self = None:
