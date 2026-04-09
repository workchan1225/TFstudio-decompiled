# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: color_scheme.pyc (Python 3.11)

from sympy.core.basic import Basic
from sympy.core.symbol import Symbol, symbols
from sympy.utilities.lambdify import lambdify
from util import interpolate, rinterpolate, create_bounds, update_bounds
from sympy.utilities.iterables import sift

class ColorGradient:
    colors = ([
        0.4,
        0.4,
        0.4], [
        0.9,
        0.9,
        0.9])
    intervals = (0, 1)
    
    def __init__(self, *args):
        pass
    # WARNING: Decompyle incomplete

    
    def copy(self):
        c = ColorGradient()
        c.colors = self.colors()
        c.intervals = self.intervals[:]
        return c

    
    def _find_interval(self, v):
        m = len(self.intervals)
        i = 0
    # WARNING: Decompyle incomplete

    
    def _interpolate_axis(self, axis, v):
        i = self._find_interval(v)
        v = rinterpolate(self.intervals[i - 1], self.intervals[i], v)
        return interpolate(self.colors[i - 1][axis], self.colors[i][axis], v)

    
    def __call__(self, r, g, b):
        c = self._interpolate_axis
        return (c(0, r), c(1, g), c(2, b))


default_color_schemes = { }

class ColorScheme:
    
    def __init__(self, *args, **kwargs):
        self.args = args
        self.f, self.gradient = None, ColorGradient()
        if len(args) == 1 and isinstance(args[0], Basic) and callable(args[0]):
            self.f = args[0]
        elif len(args) == 1 and isinstance(args[0], str):
            if args[0] in default_color_schemes:
                cs = default_color_schemes[args[0]]
                self.f, self.gradient = cs.f, cs.gradient.copy()
            else:
                self.f = lambdify('x,y,z,u,v', args[0])
        else:
            (self.f, self.gradient) = self._interpret_args(args)
        self._test_color_function()
        if not isinstance(self.gradient, ColorGradient):
            raise ValueError('Color gradient not properly initialized. (Not a ColorGradient instance.)')

    
    def _interpret_args(self, args):
        gradient = self.gradient
        f = None
        (atoms, lists) = self._sort_args(args)
        s = self._pop_symbol_list(lists)
        s = self._fill_in_vars(s)
        f_str = (lambda .0: pass# WARNING: Decompyle incomplete
)(atoms())
        s_str = s()
        s_str = (lambda .0: pass# WARNING: Decompyle incomplete
)(s_str())
        f_error = ValueError(f'''Could not interpret arguments {f_str!s} as functions of {s_str!s}.''')
    # WARNING: Decompyle incomplete

    
    def _pop_symbol_list(self, lists):
        symbol_lists = []
    # WARNING: Decompyle incomplete

    
    def _fill_in_vars(self, args):
        defaults = symbols('x,y,z,u,v')
        v_error = ValueError('Could not find what to plot.')
        if len(args) == 0:
            return defaults
        if not None(args, (tuple, list)):
            raise v_error
        if len(args) == 0:
            return defaults
    # WARNING: Decompyle incomplete

    
    def _sort_args(self, args):
        (lists, atoms) = sift(args, (lambda a: isinstance(a, (tuple, list))), binary = True)
        return (atoms, lists)

    
    def _test_color_function(self):
        if not callable(self.f):
            raise ValueError('Color function is not callable.')
        
        try:
            result = self.f(0, 0, 0, 0, 0)
            if len(result) != 3:
                raise ValueError('length should be equal to 3')
            return None
        except TypeError:
            raise ValueError("Color function needs to accept x,y,z,u,v, as arguments even if it doesn't use all of them.")
            except AssertionError:
                raise ValueError('Color function needs to return 3-tuple r,g,b.')
            except Exception:
                return None


    
    def __call__(self, x, y, z, u, v):
        
        try:
            return self.f(x, y, z, u, v)
        except Exception:
            return None


    
    def apply_to_curve(self, verts, u_set, set_len, inc_pos = (None, None)):
        '''
        Apply this color scheme to a
        set of vertices over a single
        independent variable u.
        '''
        bounds = create_bounds()
        cverts = []
        if callable(set_len):
            set_len(len(u_set) * 2)
    # WARNING: Decompyle incomplete

    
    def apply_to_surface(self, verts, u_set, v_set, set_len, inc_pos = (None, None)):
        '''
        Apply this color scheme to a
        set of vertices over two
        independent variables u and v.
        '''
        bounds = create_bounds()
        cverts = []
        if callable(set_len):
            set_len(len(u_set) * len(v_set) * 2)
    # WARNING: Decompyle incomplete

    
    def str_base(self):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args())

    
    def __repr__(self):
        return '%s' % self.str_base()


(x, y, z, t, u, v) = symbols('x,y,z,t,u,v')
default_color_schemes['rainbow'] = ColorScheme(z, y, x)
default_color_schemes['zfade'] = ColorScheme(z, (0.4, 0.4, 0.97), (0.97, 0.4, 0.4), (None, None, z))
default_color_schemes['zfade3'] = ColorScheme(z, (None, None, z), [
    0,
    (0.2, 0.2, 1),
    0.35,
    (0.2, 0.8, 0.4),
    0.5,
    (0.3, 0.9, 0.3),
    0.65,
    (0.4, 0.8, 0.2),
    1,
    (1, 0.2, 0.2)])
default_color_schemes['zfade4'] = ColorScheme(z, (None, None, z), [
    0,
    (0.3, 0.3, 1),
    0.3,
    (0.3, 1, 0.3),
    0.55,
    (0.95, 1, 0.2),
    0.65,
    (1, 0.95, 0.2),
    0.85,
    (1, 0.7, 0.2),
    1,
    (1, 0.3, 0.2)])
