# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)


try:
    from ctypes import c_float, c_int, c_double
except ImportError:
    pass

from pyglet.gl import gl as pgl
from sympy.core import S

def get_model_matrix(array_type, glGetMethod = (c_float, pgl.glGetFloatv)):
    '''
    Returns the current modelview matrix.
    '''
    m = array_type * 16()
    glGetMethod(pgl.GL_MODELVIEW_MATRIX, m)
    return m


def get_projection_matrix(array_type, glGetMethod = (c_float, pgl.glGetFloatv)):
    '''
    Returns the current modelview matrix.
    '''
    m = array_type * 16()
    glGetMethod(pgl.GL_PROJECTION_MATRIX, m)
    return m


def get_viewport():
    '''
    Returns the current viewport.
    '''
    m = c_int * 4()
    pgl.glGetIntegerv(pgl.GL_VIEWPORT, m)
    return m


def get_direction_vectors():
    m = get_model_matrix()
    return ((m[0], m[4], m[8]), (m[1], m[5], m[9]), (m[2], m[6], m[10]))


def get_view_direction_vectors():
    m = get_model_matrix()
    return ((m[0], m[1], m[2]), (m[4], m[5], m[6]), (m[8], m[9], m[10]))


def get_basis_vectors():
    return ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def screen_to_model(x, y, z):
    m = get_model_matrix(c_double, pgl.glGetDoublev)
    p = get_projection_matrix(c_double, pgl.glGetDoublev)
    w = get_viewport()
    mz = c_double()
    my = c_double()
    mx = c_double()
    pgl.gluUnProject(x, y, z, m, p, w, mx, my, mz)
    return (float(mx.value), float(my.value), float(mz.value))


def model_to_screen(x, y, z):
    m = get_model_matrix(c_double, pgl.glGetDoublev)
    p = get_projection_matrix(c_double, pgl.glGetDoublev)
    w = get_viewport()
    mz = c_double()
    my = c_double()
    mx = c_double()
    pgl.gluProject(x, y, z, m, p, w, mx, my, mz)
    return (float(mx.value), float(my.value), float(mz.value))


def vec_subs(a, b):
    pass
# WARNING: Decompyle incomplete


def billboard_matrix():
    '''
    Removes rotational components of
    current matrix so that primitives
    are always drawn facing the viewer.

    |1|0|0|x|
    |0|1|0|x|
    |0|0|1|x| (x means left unchanged)
    |x|x|x|x|
    '''
    m = get_model_matrix()
    m[0] = 1
    m[1] = 0
    m[2] = 0
    m[4] = 0
    m[5] = 1
    m[6] = 0
    m[8] = 0
    m[9] = 0
    m[10] = 1
    pgl.glLoadMatrixf(m)


def create_bounds():
    return [
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


def update_bounds(b, v):
    pass
# WARNING: Decompyle incomplete


def interpolate(a_min, a_max, a_ratio):
    return a_min + a_ratio * (a_max - a_min)


def rinterpolate(a_min, a_max, a_value):
    a_range = a_max - a_min
    if a_max == a_min:
        a_range = 1
    return (a_value - a_min) / float(a_range)


def interpolate_color(color1, color2, ratio):
    pass
# WARNING: Decompyle incomplete


def scale_value(v, v_min, v_len):
    return (v - v_min) / v_len


def scale_value_list(flist):
    pass
# WARNING: Decompyle incomplete


def strided_range(r_min, r_max, stride, max_steps = (50,)):
    pass
# WARNING: Decompyle incomplete


def parse_option_string(s):
    if not isinstance(s, str):
        return None
    options = None
    for token in s.split(';'):
        pieces = token.split('=')
        if len(pieces) == 1:
            value = ''
            option = pieces[0]
        elif len(pieces) == 2:
            (option, value) = pieces
        else:
            raise ValueError("Plot option string '%s' is malformed." % s)
        options[option.strip()] = value.strip()
        return options


def dot_product(v1, v2):
    pass
# WARNING: Decompyle incomplete


def vec_sub(v1, v2):
    pass
# WARNING: Decompyle incomplete


def vec_mag(v):
    pass
# WARNING: Decompyle incomplete
