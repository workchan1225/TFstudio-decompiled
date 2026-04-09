# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _local.pyc (Python 3.11)

from __future__ import annotations
from typing import Generic, TypeVar, cast
import attrs
from _util import NoPublicConstructor, final
from  import _run
T = TypeVar('T')
_NoValue = <NODE:12>()

def RunVarToken():
    '''RunVarToken'''
    _var: 'RunVar[T]' = 'RunVarToken'
    previous_value: 'T | type[_NoValue]' = _NoValue
    redeemed: 'bool' = attrs.field(default = False, init = False)
    _empty = (lambda cls = None, var = None: cls._create(var))()

RunVarToken = <NODE:27>(RunVarToken, 'RunVarToken', Generic[T], metaclass = NoPublicConstructor)()()

def RunVar():
    '''RunVar'''
    __doc__ = 'The run-local variant of a context variable.\n\n    :class:`RunVar` objects are similar to context variable objects,\n    except that they are shared across a single call to :func:`trio.run`\n    rather than a single task.\n\n    '
    _name: 'str' = attrs.field(alias = 'name')
    _default: 'T | type[_NoValue]' = attrs.field(default = _NoValue, alias = 'default')
    
    def get(self = None, default = None):
        '''Gets the value of this :class:`RunVar` for the current run call.'''
        
        try:
            return cast('T', _run.GLOBAL_RUN_CONTEXT.runner._locals[self])
        except AttributeError:
            raise RuntimeError('Cannot be used outside of a run context'), None
            except KeyError:
                if default is not _NoValue:
                    return 
                if None._default is not _NoValue:
                    return 
                raise None(self), None


    
    def set(self = None, value = None):
        '''Sets the value of this :class:`RunVar` for this current run
        call.

        '''
        
        try:
            old_value = self.get()
            token = RunVarToken[T]._create(self, old_value)
        except LookupError:
            token = RunVarToken._empty(self)

        _run.GLOBAL_RUN_CONTEXT.runner._locals[self] = value
        return token

    
    def reset(self = None, token = None):
        '''Resets the value of this :class:`RunVar` to what it was
        previously specified by the token.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''<RunVar name={self._name!r}>'''


RunVar = <NODE:27>(RunVar, 'RunVar', Generic[T])()()
