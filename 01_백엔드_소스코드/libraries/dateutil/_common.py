# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _common.pyc (Python 3.11)

'''
Common code used in multiple modules.
'''

class weekday(object):
    __slots__ = [
        'weekday',
        'n']
    
    def __init__(self, weekday, n = (None,)):
        self.weekday = weekday
        self.n = n

    
    def __call__(self, n):
        if n == self.n:
            return self
        return None.__class__(self.weekday, n)

    
    def __eq__(self, other):
        
        try:
            if self.weekday != other.weekday or self.n != other.n:
                return False
        except AttributeError:
            return False
            return True


    
    def __hash__(self):
        return hash((self.weekday, self.n))

    
    def __ne__(self, other):
        return not (self == other)

    
    def __repr__(self):
        s = ('MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU')[self.weekday]
        if not self.n:
            return s
        return None % (s, self.n)
