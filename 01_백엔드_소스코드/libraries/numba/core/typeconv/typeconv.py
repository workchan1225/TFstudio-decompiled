# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: typeconv.pyc (Python 3.11)


try:
    from numba.core.typeconv import _typeconv
except ImportError:
    e = None
    base_url = 'https://numba.readthedocs.io/en/stable'
    dev_url = f'''{base_url}/developer/contributing.html'''
    user_url = f'''{base_url}/user/faq.html#numba-could-not-be-imported'''
    dashes = '--------------------------------------------------------------------------------'
    msg = f'''Numba could not be imported.\n{dashes}\nIf you are seeing this message and are undertaking Numba development work, you may need to rebuild Numba.\nPlease see the development set up guide:\n\n{dev_url}.\n\n{dashes}\nIf you are not working on Numba development, the original error was: \'{str(e)}\'.\nFor help, please visit:\n\n{user_url}\n'''
    raise ImportError(msg)
    e = None
    del e

from numba.core.typeconv import castgraph, Conversion
from numba.core import types

class TypeManager(object):
    _conversion_codes = {
        Conversion.promote: ord('p'),
        Conversion.unsafe: ord('u'),
        Conversion.safe: ord('s') }
    
    def __init__(self):
        self._ptr = _typeconv.new_type_manager()
        self._types = set()

    
    def select_overload(self, sig, overloads, allow_unsafe, exact_match_required):
        sig = sig()
        overloads = overloads()
        return _typeconv.select_overload(self._ptr, sig, overloads, allow_unsafe, exact_match_required)

    
    def check_compatible(self, fromty, toty):
        if not isinstance(toty, types.Type):
            raise ValueError(f'''Specified type \'{toty!s}\' ({type(toty)!s}) is not a Numba type''')
        name = _typeconv.check_compatible(self._ptr, fromty._code, toty._code)
    # WARNING: Decompyle incomplete

    
    def set_compatible(self, fromty, toty, by):
        code = self._conversion_codes[by]
        _typeconv.set_compatible(self._ptr, fromty._code, toty._code, code)
        self._types.add(fromty)
        self._types.add(toty)

    
    def set_promote(self, fromty, toty):
        self.set_compatible(fromty, toty, Conversion.promote)

    
    def set_unsafe_convert(self, fromty, toty):
        self.set_compatible(fromty, toty, Conversion.unsafe)

    
    def set_safe_convert(self, fromty, toty):
        self.set_compatible(fromty, toty, Conversion.safe)

    
    def get_pointer(self):
        return _typeconv.get_pointer(self._ptr)



class TypeCastingRules(object):
    '''
    A helper for establishing type casting rules.
    '''
    
    def __init__(self, tm):
        self._tm = tm
        self._tg = castgraph.TypeGraph(self._cb_update)

    
    def promote(self, a, b):
        '''
        Set `a` can promote to `b`
        '''
        self._tg.promote(a, b)

    
    def unsafe(self, a, b):
        '''
        Set `a` can unsafe convert to `b`
        '''
        self._tg.unsafe(a, b)

    
    def safe(self, a, b):
        '''
        Set `a` can safe convert to `b`
        '''
        self._tg.safe(a, b)

    
    def promote_unsafe(self, a, b):
        '''
        Set `a` can promote to `b` and `b` can unsafe convert to `a`
        '''
        self.promote(a, b)
        self.unsafe(b, a)

    
    def safe_unsafe(self, a, b):
        '''
        Set `a` can safe convert to `b` and `b` can unsafe convert to `a`
        '''
        self._tg.safe(a, b)
        self._tg.unsafe(b, a)

    
    def unsafe_unsafe(self, a, b):
        '''
        Set `a` can unsafe convert to `b` and `b` can unsafe convert to `a`
        '''
        self._tg.unsafe(a, b)
        self._tg.unsafe(b, a)

    
    def _cb_update(self, a, b, rel):
        '''
        Callback for updating.
        '''
        if rel == Conversion.promote:
            self._tm.set_promote(a, b)
            return None
        if None == Conversion.safe:
            self._tm.set_safe_convert(a, b)
            return None
        if None == Conversion.unsafe:
            self._tm.set_unsafe_convert(a, b)
            return None
        raise None(rel)
