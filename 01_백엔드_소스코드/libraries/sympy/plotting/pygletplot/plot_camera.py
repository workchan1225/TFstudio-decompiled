# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: plot_camera.pyc (Python 3.11)

from pyglet.gl import gl as pgl
from sympy.plotting.pygletplot.plot_rotation import get_spherical_rotatation
from sympy.plotting.pygletplot.util import get_model_matrix, model_to_screen, screen_to_model, vec_subs

class PlotCamera:
    min_dist = 0.05
    max_dist = 500
    min_ortho_dist = 100
    max_ortho_dist = 10000
    _default_dist = 6
    _default_ortho_dist = 600
    rot_presets = {
        'xy': (0, 0, 0),
        'xz': (-90, 0, 0),
        'yz': (0, 90, 0),
        'perspective': (-45, 0, -45) }
    
    def __init__(self, window, ortho = (False,)):
        self.window = window
        self.axes = self.window.plot.axes
        self.ortho = ortho
        self.reset()

    
    def init_rot_matrix(self):
        pgl.glPushMatrix()
        pgl.glLoadIdentity()
        self._rot = get_model_matrix()
        pgl.glPopMatrix()

    
    def set_rot_preset(self, preset_name):
        self.init_rot_matrix()
        if preset_name not in self.rot_presets:
            raise ValueError('%s is not a valid rotation preset.' % preset_name)
        r = self.rot_presets[preset_name]
        self.euler_rotate(r[0], 1, 0, 0)
        self.euler_rotate(r[1], 0, 1, 0)
        self.euler_rotate(r[2], 0, 0, 1)

    
    def reset(self):
        self._dist = 0
        (self._x, self._y) = (0, 0)
        self._rot = None
        if self.ortho:
            self._dist = self._default_ortho_dist
        else:
            self._dist = self._default_dist
        self.init_rot_matrix()

    
    def mult_rot_matrix(self, rot):
        pgl.glPushMatrix()
        pgl.glLoadMatrixf(rot)
        pgl.glMultMatrixf(self._rot)
        self._rot = get_model_matrix()
        pgl.glPopMatrix()

    
    def setup_projection(self):
        pgl.glMatrixMode(pgl.GL_PROJECTION)
        pgl.glLoadIdentity()
        if self.ortho:
            pgl.gluPerspective(0.3, float(self.window.width) / float(self.window.height), self.min_ortho_dist - 0.01, self.max_ortho_dist + 0.01)
        else:
            pgl.gluPerspective(30, float(self.window.width) / float(self.window.height), self.min_dist - 0.01, self.max_dist + 0.01)
        pgl.glMatrixMode(pgl.GL_MODELVIEW)

    
    def _get_scale(self):
        return (1, 1, 1)

    
    def apply_transformation(self):
        pgl.glLoadIdentity()
        pgl.glTranslatef(self._x, self._y, -(self._dist))
    # WARNING: Decompyle incomplete

    
    def spherical_rotate(self, p1, p2, sensitivity = (1,)):
        mat = get_spherical_rotatation(p1, p2, self.window.width, self.window.height, sensitivity)
    # WARNING: Decompyle incomplete

    
    def euler_rotate(self, angle, x, y, z):
        pgl.glPushMatrix()
        pgl.glLoadMatrixf(self._rot)
        pgl.glRotatef(angle, x, y, z)
        self._rot = get_model_matrix()
        pgl.glPopMatrix()

    
    def zoom_relative(self, clicks, sensitivity):
        if self.ortho:
            dist_d = clicks * sensitivity * 50
            min_dist = self.min_ortho_dist
            max_dist = self.max_ortho_dist
        else:
            dist_d = clicks * sensitivity
            min_dist = self.min_dist
            max_dist = self.max_dist
        new_dist = self._dist - dist_d
        if clicks < 0 or new_dist < max_dist or new_dist > min_dist:
            self._dist = new_dist
            return None

    
    def mouse_translate(self, x, y, dx, dy):
        pgl.glPushMatrix()
        pgl.glLoadIdentity()
        pgl.glTranslatef(0, 0, -(self._dist))
        z = model_to_screen(0, 0, 0)[2]
        d = vec_subs(screen_to_model(x, y, z), screen_to_model(x - dx, y - dy, z))
        pgl.glPopMatrix()
