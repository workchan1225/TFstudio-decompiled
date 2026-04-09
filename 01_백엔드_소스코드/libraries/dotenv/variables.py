# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: variables.pyc (Python 3.11)

import re
from abc import ABCMeta, abstractmethod
from typing import Iterator, Mapping, Optional, Pattern
_posix_variable: Pattern[str] = re.compile('\n    \\$\\{\n        (?P<name>[^\\}:]*)\n        (?::-\n            (?P<default>[^\\}]*)\n        )?\n    \\}\n    ', re.VERBOSE)

def Atom():
    '''Atom'''
    
    def __ne__(self = None, other = None):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        return not None

    resolve = (lambda self = None, env = None: pass)()

Atom = <NODE:27>(Atom, 'Atom', metaclass = ABCMeta)

class Literal(Atom):
    
    def __init__(self = None, value = None):
        self.value = value

    
    def __repr__(self = None):
        return f'''Literal(value={self.value})'''

    
    def __eq__(self = None, other = None):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return None.value == other.value

    
    def __hash__(self = None):
        return hash((self.__class__, self.value))

    
    def resolve(self = None, env = None):
        return self.value



class Variable(Atom):
    
    def __init__(self = None, name = None, default = None):
        self.name = name
        self.default = default

    
    def __repr__(self = None):
        return f'''Variable(name={self.name}, default={self.default})'''

    
    def __eq__(self = None, other = None):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (None.name, self.default) == (other.name, other.default)

    
    def __hash__(self = None):
        return hash((self.__class__, self.name, self.default))

    
    def resolve(self = None, env = None):
        pass
    # WARNING: Decompyle incomplete



def parse_variables(value = None):
    pass
# WARNING: Decompyle incomplete
