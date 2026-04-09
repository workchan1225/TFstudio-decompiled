# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reprlib.pyc (Python 3.11)

'''Redo the builtin repr() (representation) but with limits on most sizes.'''
__all__ = [
    'Repr',
    'repr',
    'recursive_repr']
import builtins
from itertools import islice
from _thread import get_ident

def recursive_repr(fillvalue = ('...',)):
    '''Decorator to make a repr function return fillvalue for a recursive call'''
    pass
# WARNING: Decompyle incomplete


class Repr:
    
    def __init__(self):
        self.fillvalue = '...'
        self.maxlevel = 6
        self.maxtuple = 6
        self.maxlist = 6
        self.maxarray = 5
        self.maxdict = 4
        self.maxset = 6
        self.maxfrozenset = 6
        self.maxdeque = 6
        self.maxstring = 30
        self.maxlong = 40
        self.maxother = 30

    
    def repr(self, x):
        return self.repr1(x, self.maxlevel)

    
    def repr1(self, x, level):
        typename = type(x).__name__
        if ' ' in typename:
            parts = typename.split()
            typename = '_'.join(parts)
        if hasattr(self, 'repr_' + typename):
            return getattr(self, 'repr_' + typename)(x, level)
        return None.repr_instance(x, level)

    
    def _repr_iterable(self, x, level, left, right, maxiter, trail = ('',)):
        pass
    # WARNING: Decompyle incomplete

    
    def repr_tuple(self, x, level):
        return self._repr_iterable(x, level, '(', ')', self.maxtuple, ',')

    
    def repr_list(self, x, level):
        return self._repr_iterable(x, level, '[', ']', self.maxlist)

    
    def repr_array(self, x, level):
        if not x:
            return "array('%s')" % x.typecode
        header = None % x.typecode
        return self._repr_iterable(x, level, header, '])', self.maxarray)

    
    def repr_set(self, x, level):
        if not x:
            return 'set()'
        x = None(x)
        return self._repr_iterable(x, level, '{', '}', self.maxset)

    
    def repr_frozenset(self, x, level):
        if not x:
            return 'frozenset()'
        x = None(x)
        return self._repr_iterable(x, level, 'frozenset({', '})', self.maxfrozenset)

    
    def repr_deque(self, x, level):
        return self._repr_iterable(x, level, 'deque([', '])', self.maxdeque)

    
    def repr_dict(self, x, level):
        n = len(x)
        if n == 0:
            return '{}'
        if None <= 0:
            return '{' + self.fillvalue + '}'
        newlevel = None - 1
        repr1 = self.repr1
        pieces = []
        for key in islice(_possibly_sorted(x), self.maxdict):
            keyrepr = repr1(key, newlevel)
            valrepr = repr1(x[key], newlevel)
            pieces.append(f'''{keyrepr!s}: {valrepr!s}''')
            if n > self.maxdict:
                pieces.append(self.fillvalue)
        s = ', '.join(pieces)
        return f'''{{{s!s}}}'''

    
    def repr_str(self, x, level):
        s = builtins.repr(x[:self.maxstring])
        if len(s) > self.maxstring:
            i = max(0, (self.maxstring - 3) // 2)
            j = max(0, self.maxstring - 3 - i)
            s = builtins.repr(x[:i] + x[len(x) - j:])
            s = s[:i] + self.fillvalue + s[len(s) - j:]
        return s

    
    def repr_int(self, x, level):
        s = builtins.repr(x)
        if len(s) > self.maxlong:
            i = max(0, (self.maxlong - 3) // 2)
            j = max(0, self.maxlong - 3 - i)
            s = s[:i] + self.fillvalue + s[len(s) - j:]
        return s

    
    def repr_instance(self, x, level):
        
        try:
            s = builtins.repr(x)
        except Exception:
            return 

        if len(s) > self.maxother:
            max(0, self.maxother - 3 - i) = max(0, (self.maxother - 3) // 2)
            s = s[:i] + self.fillvalue + s[len(s) - j:]
        return s



def _possibly_sorted(x):
    
    try:
        return sorted(x)
    except Exception:
        return 


aRepr = Repr()
repr = aRepr.repr
