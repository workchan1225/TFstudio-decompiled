# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: visualization.pyc (Python 3.11)

'''
Plotting (requires matplotlib)
'''
from colorsys import hsv_to_rgb, hls_to_rgb
from libmp import NoConvergence
from libmp.backend import xrange

class VisualizationMethods(object):
    plot_ignore = (ValueError, ArithmeticError, ZeroDivisionError, NoConvergence)


def plot(ctx, f, xlim, ylim, points, file, dpi, singularities, axes = ([
    -5,
    5], None, 200, None, None, [], None)):
    '''
    Shows a simple 2D plot of a function `f(x)` or list of functions
    `[f_0(x), f_1(x), \\ldots, f_n(x)]` over a given interval
    specified by *xlim*. Some examples::

        plot(lambda x: exp(x)*li(x), [1, 4])
        plot([cos, sin], [-4, 4])
        plot([fresnels, fresnelc], [-4, 4])
        plot([sqrt, cbrt], [-4, 4])
        plot(lambda t: zeta(0.5+t*j), [-20, 20])
        plot([floor, ceil, abs, sign], [-5, 5])

    Points where the function raises a numerical exception or
    returns an infinite value are removed from the graph.
    Singularities can also be excluded explicitly
    as follows (useful for removing erroneous vertical lines)::

        plot(cot, ylim=[-5, 5])   # bad
        plot(cot, ylim=[-5, 5], singularities=[-pi, 0, pi])  # good

    For parts where the function assumes complex values, the
    real part is plotted with dashes and the imaginary part
    is plotted with dots.

    .. note :: This function requires matplotlib (pylab).
    '''
    if file:
        axes = None
    fig = None
    if not axes:
        import pylab
        fig = pylab.figure()
        axes = fig.add_subplot(111)
    if not isinstance(f, (tuple, list)):
        f = [
            f]
    (a, b) = xlim
    colors = [
        'b',
        'r',
        'g',
        'm',
        'k']
    for n, func in enumerate(f):
        x = ctx.arange(a, b, (b - a) / float(points))
        segments = []
        segment = []
        in_complex = False
        for i in xrange(len(x)):
            if i != 0:
                for sing in singularities:
                    if x[i - 1] <= sing and x[i] >= sing:
                        raise ValueError
                    v = func(x[i])
                    if ctx.isnan(v) or abs(v) > 1e+300:
                        raise ValueError
                    if hasattr(v, 'imag') and v.imag:
                        re = float(v.real)
                        im = float(v.imag)
                        if not in_complex:
                            in_complex = True
                            segments.append(segment)
                            segment = []
                        segment.append((float(x[i]), re, im))
                    elif in_complex:
                        in_complex = False
                        segments.append(segment)
                        segment = []
            if hasattr(v, 'real'):
                v = v.real
            segment.append((float(x[i]), v))
            except ctx.plot_ignore:
                if segment:
                    segments.append(segment)
                segment = []
                continue
            if segment:
                segments.append(segment)
        for segment in segments:
            x = segment()
            y = segment()
            if not x:
                continue
            c = colors[n % len(colors)]
            if len(segment[0]) == 3:
                z = segment()
                axes.plot(x, y, '--' + c, linewidth = 3)
                axes.plot(x, z, ':' + c, linewidth = 3)
                continue
            axes.plot(x, y, c, linewidth = 3)
            (lambda .0: [ float(_) for _ in .0 ])(xlim())
            if ylim:
                (lambda .0: [ float(_) for _ in .0 ])(ylim())
    axes.set_xlabel('x')
    axes.set_ylabel('f(x)')
    axes.grid(True)
    if fig:
        if file:
            pylab.savefig(file, dpi = dpi)
            return None
        axes.set_ylim.show()
        return None
    return axes.set_ylim


def default_color_function(ctx, z):
    if ctx.isinf(z):
        return (1, 1, 1)
    if None.isnan(z):
        return (0.5, 0.5, 0.5)
    pi = None
    a = (float(ctx.arg(z)) + ctx.pi) / (2 * ctx.pi)
    a = (a + 0.5) % 1
    b = 1 - float(1 / (1 + abs(z) ** 0.3))
    return hls_to_rgb(a, b, 0.8)

blue_orange_colors = [
    (-1, (0, 0, 0)),
    (-0.95, (0.1, 0.2, 0.5)),
    (-0.5, (0, 0.5, 1)),
    (-0.05, (0.4, 0.8, 0.8)),
    (0, (1, 1, 1)),
    (0.05, (1, 0.9, 0.3)),
    (0.5, (0.9, 0.5, 0)),
    (0.95, (0.7, 0.1, 0)),
    (1, (0, 0, 0)),
    (2, (0, 0, 0))]

def phase_color_function(ctx, z):
    if ctx.isinf(z):
        return (1, 1, 1)
    if None.isnan(z):
        return (0.5, 0.5, 0.5)
    pi = None
    w = float(ctx.arg(z)) / pi
    w = max(min(w, 1), -1)
    for i in range(1, len(blue_orange_colors)):
        if blue_orange_colors[i][0] > w:
            (ra, ga, ba) = (a,)
            (rb, gb, bb) = (b,)
            s = (w - a) / (b - a)
            
            return blue_orange_colors[i], (ra + (rb - ra) * s, ga + (gb - ga) * s, ba + (bb - ba) * s)
        return None


def cplot(ctx, f, re, im, points, color, verbose, file, dpi, axes = ([
    -5,
    5], [
    -5,
    5], 2000, None, False, None, None, None)):
    '''
    Plots the given complex-valued function *f* over a rectangular part
    of the complex plane specified by the pairs of intervals *re* and *im*.
    For example::

        cplot(lambda z: z, [-2, 2], [-10, 10])
        cplot(exp)
        cplot(zeta, [0, 1], [0, 50])

    By default, the complex argument (phase) is shown as color (hue) and
    the magnitude is show as brightness. You can also supply a
    custom color function (*color*). This function should take a
    complex number as input and return an RGB 3-tuple containing
    floats in the range 0.0-1.0.

    Alternatively, you can select a builtin color function by passing
    a string as *color*:

      * "default" - default color scheme
      * "phase" - a color scheme that only renders the phase of the function,
         with white for positive reals, black for negative reals, gold in the
         upper half plane, and blue in the lower half plane.

    To obtain a sharp image, the number of points may need to be
    increased to 100,000 or thereabout. Since evaluating the
    function that many times is likely to be slow, the \'verbose\'
    option is useful to display progress.

    .. note :: This function requires matplotlib (pylab).
    '''
    pass
# WARNING: Decompyle incomplete


def splot(ctx, f, u, v, points, keep_aspect, wireframe, file, dpi, axes = ([
    -5,
    5], [
    -5,
    5], 100, True, False, None, None, None)):
    '''
    Plots the surface defined by `f`.

    If `f` returns a single component, then this plots the surface
    defined by `z = f(x,y)` over the rectangular domain with
    `x = u` and `y = v`.

    If `f` returns three components, then this plots the parametric
    surface `x, y, z = f(u,v)` over the pairs of intervals `u` and `v`.

    For example, to plot a simple function::

        >>> from mpmath import *
        >>> f = lambda x, y: sin(x+y)*cos(y)
        >>> splot(f, [-pi,pi], [-pi,pi])    # doctest: +SKIP

    Plotting a donut::

        >>> r, R = 1, 2.5
        >>> f = lambda u, v: [r*cos(u), (R+r*sin(u))*cos(v), (R+r*sin(u))*sin(v)]
        >>> splot(f, [0, 2*pi], [0, 2*pi])    # doctest: +SKIP

    .. note :: This function requires matplotlib (pylab) 0.98.5.3 or higher.
    '''
    pass
# WARNING: Decompyle incomplete

VisualizationMethods.plot = plot
VisualizationMethods.default_color_function = default_color_function
VisualizationMethods.phase_color_function = phase_color_function
VisualizationMethods.cplot = cplot
VisualizationMethods.splot = splot
