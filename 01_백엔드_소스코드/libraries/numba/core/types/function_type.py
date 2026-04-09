# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: function_type.pyc (Python 3.11)

__all__ = [
    'FunctionType',
    'UndefinedFunctionType',
    'FunctionPrototype',
    'WrapperAddressProtocol',
    'CompileResultWAP']
from abc import ABC, abstractmethod
from abstract import Type
from  import types, errors

class FunctionType(Type):
    '''
    First-class function type.
    '''
    cconv = None
    
    def __init__(self, signature):
        sig = types.unliteral(signature)
        self.nargs = len(sig.args)
        self.signature = sig
        self.ftype = FunctionPrototype(sig.return_type, sig.args)
        self._key = self.ftype.key

    key = (lambda self: self._key)()
    name = (lambda self: f'''{type(self).__name__}[{self.key}]''')()
    
    def is_precise(self):
        return self.signature.is_precise()

    
    def get_precise(self):
        return self

    
    def dump(self, tab = ('',)):
        print(f'''{tab}DUMP {type(self).__name__}[code={self._code}]''')
        self.signature.dump(tab = tab + '  ')
        print(f'''{tab}END DUMP {type(self).__name__}''')

    
    def get_call_type(self, context, args, kws):
        typing = typing
        import numba.core
        if kws:
            raise errors.UnsupportedError('first-class function call cannot use keyword arguments')
        if len(args) != self.nargs:
            raise ValueError(f'''mismatch of arguments number: {len(args)} vs {self.nargs}''')
        sig = self.signature
    # WARNING: Decompyle incomplete

    
    def check_signature(self, other_sig):
