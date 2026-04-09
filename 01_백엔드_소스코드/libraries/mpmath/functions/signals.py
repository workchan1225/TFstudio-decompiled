# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: signals.pyc (Python 3.11)

from functions import defun_wrapped
squarew = (lambda ctx, t, amplitude, period = (1, 1): P = periodA = amplitudeA * -1 ** ctx.floor(2 * t / P))()
trianglew = (lambda ctx, t, amplitude, period = (1, 1): A = amplitudeP = period2 * A * (0.5 - ctx.fabs(1 - 2 * ctx.frac(t / P + 0.25))))()
sawtoothw = (lambda ctx, t, amplitude, period = (1, 1): A = amplitudeP = periodA * ctx.frac(t / P))()
unit_triangle = (lambda ctx, t, amplitude = (1,): A = amplitudeif t <= -1 or t >= 1:
ctx.zeroNone * (-ctx.fabs(t) + 1))()
sigmoid = (lambda ctx, t, amplitude = (1,): A = amplitudeA / (1 + ctx.exp(-t)))()
