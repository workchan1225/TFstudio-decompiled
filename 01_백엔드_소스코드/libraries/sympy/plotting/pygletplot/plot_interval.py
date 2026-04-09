# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: plot_interval.pyc (Python 3.11)

from sympy.core.singleton import S
from sympy.core.symbol import Symbol
from sympy.core.sympify import sympify
from sympy.core.numbers import Integer

class PlotInterval:
    '''
    '''
    (_v, _v_min, _v_max, _v_steps) = (None, None, None, None)
    
    def require_all_args(f):
        pass
    # WARNING: Decompyle incomplete

    
    def __init__(self, *args):
        pass
    # WARNING: Decompyle incomplete

    
    def get_v(self):
        return self._v

    
    def set_v(self, v):
        pass
    # WARNING: Decompyle incomplete

    
    def get_v_min(self):
        return self._v_min

    
    def set_v_min(self, v_min):
        pass
    # WARNING: Decompyle incomplete

    
    def get_v_max(self):
        return self._v_max

    
    def set_v_max(self, v_max):
        pass
    # WARNING: Decompyle incomplete

    
    def get_v_steps(self):
        return self._v_steps

    
    def set_v_steps(self, v_steps):
        pass
    # WARNING: Decompyle incomplete

    get_v_len = (lambda self: self.v_steps + 1)()
    v = property(get_v, set_v)
    v_min = property(get_v_min, set_v_min)
    v_max = property(get_v_max, set_v_max)
    v_steps = property(get_v_steps, set_v_steps)
    v_len = property(get_v_len)
    
    def fill_from(self, b):
        pass
    # WARNING: Decompyle incomplete

    try_parse = (lambda : if len(args) == 1 and isinstance(args[0], PlotInterval):
args[0]# WARNING: Decompyle incomplete
)()
    
    def _str_base(self):
        return ','.join([
            str(self.v),
            str(self.v_min),
            str(self.v_max),
            str(self.v_steps)])

    
    def __repr__(self):
        '''
        A string representing the interval in class constructor form.
        '''
        return 'PlotInterval(%s)' % self._str_base()

    
    def __str__(self):
        '''
        A string representing the interval in list form.
        '''
        return '[%s]' % self._str_base()

    assert_complete = (lambda self: pass)()
    vrange = (lambda self: pass# WARNING: Decompyle incomplete
)()
    vrange2 = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def frange(self):
        pass
    # WARNING: Decompyle incomplete
