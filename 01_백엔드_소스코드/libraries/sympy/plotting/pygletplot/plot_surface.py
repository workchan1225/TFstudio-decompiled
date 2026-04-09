# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: plot_surface.pyc (Python 3.11)

from pyglet.gl import gl as pgl
from sympy.core import S
from sympy.plotting.pygletplot.plot_mode_base import PlotModeBase

class PlotSurface(PlotModeBase):
    default_rot_preset = 'perspective'
    
    def _on_calculate_verts(self):
        self.u_interval = self.intervals[0]
        self.u_set = list(self.u_interval.frange())
        self.v_interval = self.intervals[1]
        self.v_set = list(self.v_interval.frange())
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
        self._calculating_verts_len = float(self.u_interval.v_len * self.v_interval.v_len)
        verts = []
        b = self.bounds
    # WARNING: Decompyle incomplete

    
    def _on_calculate_cverts(self):
        pass
    # WARNING: Decompyle incomplete

    
    def calculate_one_cvert(self, u, v):
        vert = self.verts[u][v]
        return self.color(vert[0], vert[1], vert[2], self.u_set[u], self.v_set[v])

    
    def draw_verts(self, use_cverts, use_solid_color):
        pass
    # WARNING: Decompyle incomplete
