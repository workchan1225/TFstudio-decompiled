# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: plot_mode.pyc (Python 3.11)

from plot_interval import PlotInterval
from plot_object import PlotObject
from util import parse_option_string
from sympy.core.symbol import Symbol
from sympy.core.sympify import sympify
from sympy.geometry.entity import GeometryEntity
from sympy.utilities.iterables import is_sequence

class PlotMode(PlotObject):
    '''
    Grandparent class for plotting
    modes. Serves as interface for
    registration, lookup, and init
    of modes.

    To create a new plot mode,
    inherit from PlotModeBase
    or one of its children, such
    as PlotSurface or PlotCurve.
    '''
    (i_vars, d_vars) = ('', '')
    intervals = []
    aliases = []
    is_default = False
    
    def draw(self):
        raise NotImplementedError()

    _mode_alias_list = []
    _mode_map = {
        1: {
            1: { },
            2: { } },
        2: {
            1: { },
            2: { } },
        3: {
            1: { },
            2: { } } }
    _mode_default_map = {
        1: { },
        2: { },
        3: { } }
    (_i_var_max, _d_var_max) = (2, 3)
    
    def __new__(cls, *args, **kwargs):
        '''
        This is the function which interprets
        arguments given to Plot.__init__ and
        Plot.__setattr__. Returns an initialized
        instance of the appropriate child class.
        '''
        (newargs, newkwargs) = PlotMode._extract_options(args, kwargs)
        mode_arg = newkwargs.get('mode', '')
        (d_vars, intervals) = PlotMode._interpret_args(newargs)
        i_vars = PlotMode._find_i_vars(d_vars, intervals)
        d = len(d_vars)
        i = max([
            len(i_vars),
            len(intervals)])
        subcls = PlotMode._get_mode(mode_arg, i, d)
        o = object.__new__(subcls)
        o.d_vars = d_vars
        o._fill_i_vars(i_vars)
        o._fill_intervals(intervals)
        o.options = newkwargs
        return o

    _get_mode = (lambda mode_arg, i_var_count, d_var_count: try:
m = Noneif issubclass(mode_arg, PlotMode):
m = mode_argelse:
except TypeError:
passif m:
if not m._was_initialized:
raise ValueError(f'''To use unregistered plot mode {m.__name__!s} you must first call {m.__name__!s}._init_mode().''')if d_var_count != m.d_var_count:
raise ValueError('%s can only plot functions with %i dependent variables.' % (m.__name__, m.d_var_count))if i_var_count > m.i_var_count:
raise ValueError('%s cannot plot functions with more than %i independent variables.' % (m.__name__, m.i_var_count))mif None(mode_arg, str):
d = d_var_counti = i_var_countif i > PlotMode._i_var_max:
raise ValueError(var_count_error(True, True))if d > PlotMode._d_var_max:
raise ValueError(var_count_error(False, True))if not mode_arg:
PlotMode._get_default_mode(i, d)None._get_aliased_mode(mode_arg, i, d)raise None('PlotMode argument must be a class or a string'))()
    _get_default_mode = (lambda i, d, i_vars = (-1,): if i_vars == -1:
i_vars = itry:
PlotMode._mode_default_map[d][i]except KeyError:
if i < PlotMode._i_var_max:
raise None("Couldn't find a default mode for %i independent and %i dependent variables." % (i_vars, d)))()
    _get_aliased_mode = (lambda alias, i, d, i_vars = (-1,): if i_vars == -1:
i_vars = iif alias not in PlotMode._mode_alias_list:
raise ValueError(f'''Couldn\'t find a mode called {alias!s}. Known modes: {', '.join(PlotMode._mode_alias_list)!s}.''')try:
PlotMode._mode_map[d][i][alias]except TypeError:
if i < PlotMode._i_var_max:
raise None("Couldn't find a %s mode for %i independent and %i dependent variables." % (alias, i_vars, d)))()
    _register = (lambda cls: name = cls.__name__cls._init_mode()try:
d = cls.d_var_counti = cls.i_var_countfor a in cls.aliases:
if a not in PlotMode._mode_alias_list:
PlotMode._mode_alias_list.append(a)PlotMode._mode_map[d][i][a] = clsif cls.is_default:
PlotMode._mode_default_map[d][i] = clsNoneNoneexcept Exception:
e = Noneraise RuntimeError(f'''Failed to register plot mode {name!s}. Reason: {str(e)!s}''')e = Nonedel e)()
    _init_mode = (lambda cls: 
def symbols_list(symbol_str):
symbol_str()cls.i_vars = symbols_list(cls.i_vars)cls.d_vars = symbols_list(cls.d_vars)cls.i_var_count = len(cls.i_vars)cls.d_var_count = len(cls.d_vars)if cls.i_var_count > PlotMode._i_var_max:
raise ValueError(var_count_error(True, False))if cls.d_var_count > PlotMode._d_var_max:
raise ValueError(var_count_error(False, False))if len(cls.aliases) > 0:
cls.primary_alias = cls.aliases[0]else:
cls.primary_alias = cls.__name__di = cls.intervalsif len(di) != cls.i_var_count:
raise ValueError('Plot mode must provide a default interval for each i_var.')# WARNING: Decompyle incomplete
)()
    _was_initialized = False
    _find_i_vars = (lambda functions, intervals: i_vars = []# WARNING: Decompyle incomplete
)()
    
    def _fill_i_vars(self, i_vars):
        self.i_vars = self.i_vars()
        for i in range(len(i_vars)):
            self.i_vars[i] = i_vars[i]
            return None

    
    def _fill_intervals(self, intervals):
        pass
    # WARNING: Decompyle incomplete

    _interpret_args = (lambda args: interval_wrong_order = 'PlotInterval %s was given before any function(s).'interpret_error = 'Could not interpret %s as a function or interval.'intervals = []functions = []if isinstance(args[0], GeometryEntity):
for coords in list(args[0].arbitrary_point()):
functions.append(coords)intervals.append(PlotInterval.try_parse(args[0].plot_interval()))# WARNING: Decompyle incomplete
)()
    _extract_options = (lambda args, kwargs: newargs = []newkwargs = { }# WARNING: Decompyle incomplete
)()


def var_count_error(is_independent, is_plotting):
    '''
    Used to format an error message which differs
    slightly in 4 places.
    '''
    if is_plotting:
        v = 'Plotting'
    else:
        v = 'Registering plot modes'
    if is_independent:
        s = 'independent'
        n = PlotMode._i_var_max
    else:
        s = 'dependent'
        n = PlotMode._d_var_max
    return '%s with more than %i %s variables is not supported.' % (v, n, s)
