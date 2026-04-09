# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: plot_modes.pyc (Python 3.11)

from sympy.utilities.lambdify import lambdify
from sympy.core.numbers import pi
from sympy.functions import sin, cos
from sympy.plotting.pygletplot.plot_curve import PlotCurve
from sympy.plotting.pygletplot.plot_surface import PlotSurface
from math import sin as p_sin
from math import cos as p_cos

def float_vec3(f):
    pass
# WARNING: Decompyle incomplete


class Cartesian2D(PlotCurve):
    (i_vars, d_vars) = ('x', 'y')
    intervals = [
        [
            -5,
            5,
            100]]
    aliases = [
        'cartesian']
    is_default = True
    
    def _get_sympy_evaluator(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_lambda_evaluator(self):
        fy = self.d_vars[0]
        x = self.t_interval.v
        return lambdify([
            x], [
            x,
            fy,
            0])



class Cartesian3D(PlotSurface):
    (i_vars, d_vars) = ('xy', 'z')
    intervals = [
        [
            -1,
            1,
            40],
        [
            -1,
            1,
            40]]
    aliases = [
        'cartesian',
        'monge']
    is_default = True
    
    def _get_sympy_evaluator(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_lambda_evaluator(self):
        fz = self.d_vars[0]
        x = self.u_interval.v
        y = self.v_interval.v
        return lambdify([
            x,
            y], [
            x,
            y,
            fz])



class ParametricCurve2D(PlotCurve):
    (i_vars, d_vars) = ('t', 'xy')
    intervals = [
        [
            0,
            2 * pi,
            100]]
    aliases = [
        'parametric']
    is_default = True
    
    def _get_sympy_evaluator(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_lambda_evaluator(self):
        (fx, fy) = self.d_vars
        t = self.t_interval.v
        return lambdify([
            t], [
            fx,
            fy,
            0])



class ParametricCurve3D(PlotCurve):
    (i_vars, d_vars) = ('t', 'xyz')
    intervals = [
        [
            0,
            2 * pi,
            100]]
    aliases = [
        'parametric']
    is_default = True
    
    def _get_sympy_evaluator(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_lambda_evaluator(self):
        (fx, fy, fz) = self.d_vars
        t = self.t_interval.v
        return lambdify([
            t], [
            fx,
            fy,
            fz])



class ParametricSurface(PlotSurface):
    (i_vars, d_vars) = ('uv', 'xyz')
    intervals = [
        [
            -1,
            1,
            40],
        [
            -1,
            1,
            40]]
    aliases = [
        'parametric']
    is_default = True
    
    def _get_sympy_evaluator(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_lambda_evaluator(self):
        (fx, fy, fz) = self.d_vars
        u = self.u_interval.v
        v = self.v_interval.v
        return lambdify([
            u,
            v], [
            fx,
            fy,
            fz])



class Polar(PlotCurve):
    (i_vars, d_vars) = ('t', 'r')
    intervals = [
        [
            0,
            2 * pi,
            100]]
    aliases = [
        'polar']
    is_default = False
    
    def _get_sympy_evaluator(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_lambda_evaluator(self):
        fr = self.d_vars[0]
        t = self.t_interval.v
        fy = fr * sin(t)
        fx = fr * cos(t)
        return lambdify([
            t], [
            fx,
            fy,
            0])



class Cylindrical(PlotSurface):
    (i_vars, d_vars) = ('th', 'r')
    intervals = [
        [
            0,
            2 * pi,
            40],
        [
            -1,
            1,
            20]]
    aliases = [
        'cylindrical',
        'polar']
    is_default = False
    
    def _get_sympy_evaluator(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_lambda_evaluator(self):
        fr = self.d_vars[0]
        t = self.u_interval.v
        h = self.v_interval.v
        fy = fr * sin(t)
        fx = fr * cos(t)
        return lambdify([
            t,
            h], [
            fx,
            fy,
            h])



class Spherical(PlotSurface):
    (i_vars, d_vars) = ('tp', 'r')
    intervals = [
        [
            0,
            2 * pi,
            40],
        [
            0,
            pi,
            20]]
    aliases = [
        'spherical']
    is_default = False
    
    def _get_sympy_evaluator(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_lambda_evaluator(self):
        fr = self.d_vars[0]
        t = self.u_interval.v
        p = self.v_interval.v
        fx = fr * cos(t) * sin(p)
        fy = fr * sin(t) * sin(p)
        fz = fr * cos(p)
        return lambdify([
            t,
            p], [
            fx,
            fy,
            fz])


Cartesian2D._register()
Cartesian3D._register()
ParametricCurve2D._register()
ParametricCurve3D._register()
ParametricSurface._register()
Polar._register()
Cylindrical._register()
Spherical._register()
