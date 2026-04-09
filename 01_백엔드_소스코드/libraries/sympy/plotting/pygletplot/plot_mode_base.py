# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: plot_mode_base.pyc (Python 3.11)

from pyglet.gl import gl as pgl
from sympy.core import S
from sympy.plotting.pygletplot.color_scheme import ColorScheme
from sympy.plotting.pygletplot.plot_mode import PlotMode
from sympy.utilities.iterables import is_sequence
from time import sleep
from threading import Thread, Event, RLock
import warnings

class PlotModeBase(PlotMode):
    '''
    Intended parent class for plotting
    modes. Provides base functionality
    in conjunction with its parent,
    PlotMode.
    '''
    (i_vars, d_vars) = ('', '')
    intervals = []
    aliases = []
    is_default = False
    styles = {
        'wireframe': 1,
        'solid': 2,
        'both': 3 }
    style_override = ''
    default_wireframe_color = (0.85, 0.85, 0.85)
    default_solid_color = (0.6, 0.6, 0.9)
    default_rot_preset = 'xy'
    
    def _get_evaluator(self):
