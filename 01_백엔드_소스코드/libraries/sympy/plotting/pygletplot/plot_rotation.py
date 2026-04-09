# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: plot_rotation.pyc (Python 3.11)


try:
    from ctypes import c_float
except ImportError:
    pass

from pyglet.gl import gl as pgl
from math import sqrt as _sqrt, acos as _acos

def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def mag(a):
    return _sqrt(a[0] ** 2 + a[1] ** 2 + a[2] ** 2)


def norm(a):
    m = mag(a)
    return (a[0] / m, a[1] / m, a[2] / m)


def get_sphere_mapping(x, y, width, height):
    x = min([
        max([
            x,
            0]),
        width])
    y = min([
        max([
            y,
            0]),
        height])
    sr = _sqrt((width / 2) ** 2 + (height / 2) ** 2)
    sx = (x - width / 2) / sr
    sy = (y - height / 2) / sr
    sz = 1 - sx ** 2 - sy ** 2
    if sz > 0:
        sz = _sqrt(sz)
        return (sx, sy, sz)
    sz = None
    return norm((sx, sy, sz))

rad2deg = 57.2958

def get_spherical_rotatation(p1, p2, width, height, theta_multiplier):
    v1 = get_sphere_mapping(p1[0], p1[1], width, height)
    v2 = get_sphere_mapping(p2[0], p2[1], width, height)
    d = min(max([
        dot(v1, v2),
        -1]), 1)
    if abs(d - 1) < 1e-06:
        return None
    raxis = None(cross(v1, v2))
    rtheta = theta_multiplier * rad2deg * _acos(d)
    pgl.glPushMatrix()
    pgl.glLoadIdentity()
# WARNING: Decompyle incomplete
