# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: plot_curve.pyc (Python 3.11)

from pyglet.gl import gl as pgl
from sympy.core import S
from sympy.plotting.pygletplot.plot_mode_base import PlotModeBase

class PlotCurve(PlotModeBase):
    style_override = 'wireframe'
    
    def _on_calculate_verts(self):
        self.t_interval = self.intervals[0]
        self.t_set = list(self.t_interval.frange())
        self.bounds = [
            [
                S.Infinity,
                S.NegativeInfinity,
                0],
            [
                S.Infinity,
                S.NegativeInfinity,
                0],
            [
                S.Infinity,
                S.NegativeInfinity,
                0]]
        evaluate = self._get_evaluator()
        self._calculating_verts_pos = 0
        self._calculating_verts_len = float(self.t_interval.v_len)
        self.verts = []
        b = self.bounds
        for t in self.t_set:
            _e = evaluate(t)
        except (NameError, ZeroDivisionError):
            _e = None
    # WARNING: Decompyle incomplete

    
    def _on_calculate_cverts(self):
        pass
    # WARNING: Decompyle incomplete

    
    def calculate_one_cvert(self, t):
        vert = self.verts[t]
        return self.color(vert[0], vert[1], vert[2], self.t_set[t], None)

    
    def draw_verts(self, use_cverts):
        pass
    # WARNING: Decompyle incomplete
