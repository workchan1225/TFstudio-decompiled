# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: plot_axes.pyc (Python 3.11)

from pyglet.gl import gl as pgl
from pyglet import font
from sympy.core import S
from sympy.plotting.pygletplot.plot_object import PlotObject
from sympy.plotting.pygletplot.util import billboard_matrix, dot_product, get_direction_vectors, strided_range, vec_mag, vec_sub
from sympy.utilities.iterables import is_sequence

class PlotAxes(PlotObject):
    
    def __init__(self = None, *, style, none, frame, box, ordinate, stride, visible, overlay, colored, label_axes, label_ticks, tick_length, font_face, font_size, *args, **kwargs):
        style = style.lower()
    # WARNING: Decompyle incomplete

    
    def reset_resources(self):
        self.label_font = None

    
    def reset_bounding_box(self):
        self._bounding_box = [
            [
                None,
                None],
            [
                None,
                None],
            [
                None,
                None]]
        self._axis_ticks = [
            [],
            [],
            []]

    
    def draw(self):
        if self._render_object:
            pgl.glPushAttrib(pgl.GL_ENABLE_BIT | pgl.GL_POLYGON_BIT | pgl.GL_DEPTH_BUFFER_BIT)
            if self._overlay:
                pgl.glDisable(pgl.GL_DEPTH_TEST)
            self._render_object.draw()
            pgl.glPopAttrib()
            return None

    
    def adjust_bounds(self, child_bounds):
        b = self._bounding_box
        c = child_bounds
    # WARNING: Decompyle incomplete

    
    def _recalculate_axis_ticks(self, axis):
        b = self._bounding_box
    # WARNING: Decompyle incomplete

    
    def toggle_visible(self):
        self.visible = not (self.visible)

    
    def toggle_colors(self):
        self._colored = not (self._colored)



class PlotAxesBase(PlotObject):
    
    def __init__(self, parent_axes):
        self._p = parent_axes

    
    def draw(self):
        color = [
            ([
                0.2,
                0.1,
                0.3], [
                0.2,
                0.1,
                0.3], [
                0.2,
                0.1,
                0.3]),
            ([
                0.9,
                0.3,
                0.5], [
                0.5,
                1,
                0.5], [
                0.3,
                0.3,
                0.9])][self._p._colored]
        self.draw_background(color)
        self.draw_axis(2, color[2])
        self.draw_axis(1, color[1])
        self.draw_axis(0, color[0])

    
    def draw_background(self, color):
        pass

    
    def draw_axis(self, axis, color):
        raise NotImplementedError()

    
    def draw_text(self, text, position, color, scale = (1,)):
        if len(color) == 3:
            color = (color[0], color[1], color[2], 1)
    # WARNING: Decompyle incomplete

    
    def draw_line(self, v, color):
        o = self._p._origin
        pgl.glBegin(pgl.GL_LINES)
    # WARNING: Decompyle incomplete



class PlotAxesOrdinate(PlotAxesBase):
    pass
# WARNING: Decompyle incomplete


class PlotAxesFrame(PlotAxesBase):
    pass
# WARNING: Decompyle incomplete
