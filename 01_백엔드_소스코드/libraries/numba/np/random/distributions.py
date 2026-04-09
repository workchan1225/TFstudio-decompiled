# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: distributions.pyc (Python 3.11)

'''
Algorithmic implementations for generating different types
of random distributions.
'''
import numpy as np
from numba.core.extending import register_jitable
from numba.np.random._constants import wi_double, ki_double, ziggurat_nor_r, fi_double, wi_float, ki_float, ziggurat_nor_inv_r_f, ziggurat_nor_r_f, fi_float, we_double, ke_double, ziggurat_exp_r, fe_double, we_float, ke_float, ziggurat_exp_r_f, fe_float, INT64_MAX, ziggurat_nor_inv_r
from numba.np.random.generator_core import next_double, next_float, next_uint32, next_uint64
from numba import float32, int64
from numba.np.numpy_support import numpy_version
np_log1p = (lambda x: np.log1p(x))()
np_log1pf = (lambda x: np.log1p(float32(x)))()
random_rayleigh = (lambda bitgen, mode: mode * np.sqrt(2 * random_standard_exponential(bitgen)))()
np_expm1 = (lambda x: np.expm1(x))()
random_standard_normal = (lambda bitgen: r = next_uint64(bitgen)idx = r & 255r >>= 8sign = r & 1rabs = r >> 1 & 0xFFFFFFFFFFFFFx = rabs * wi_double[idx]if sign & 1:
x = -xif rabs < ki_double[idx]:
xif None == 0:
xx = -ziggurat_nor_inv_r * np.log1p(-next_double(bitgen))yy = -np.log1p(-next_double(bitgen))if yy + yy > xx * xx:
if rabs >> 8 & 1:
-(ziggurat_nor_r + xx)None + xxif (fi_double[idx - 1] - fi_double[idx]) * next_double(bitgen) + fi_double[idx] < np.exp(-0.5 * x * x):
x)()
random_standard_normal_f = (lambda bitgen: r = next_uint32(bitgen)idx = r & 255sign = r >> 8 & 1rabs = r >> 9 & 8388607x = float32(float32(rabs) * wi_float[idx])if sign & 1:
x = -xif rabs < ki_float[idx]:
xif None == 0:
xx = float32(-ziggurat_nor_inv_r_f * np_log1pf(-next_float(bitgen)))yy = float32(-np_log1pf(-next_float(bitgen)))if float32(yy + yy) > float32(xx * xx):
if rabs >> 8 & 1:
-float32(ziggurat_nor_r_f + xx)None(ziggurat_nor_r_f + xx)if (fi_float[idx - 1] - fi_float[idx]) * next_float(bitgen) + fi_float[idx] < float32(np.exp(-float32(0.5) * x * x)):
x)()
random_standard_exponential = (lambda bitgen: ri = next_uint64(bitgen)ri >>= 3idx = ri & 255ri >>= 8x = ri * we_double[idx]if ri < ke_double[idx]:
xif None == 0:
ziggurat_exp_r - np_log1p(-next_double(bitgen))if (None[idx - 1] - fe_double[idx]) * next_double(bitgen) + fe_double[idx] < np.exp(-x):
x)()
random_standard_exponential_f = (lambda bitgen: ri = next_uint32(bitgen)ri >>= 1idx = ri & 255ri >>= 8x = float32(float32(ri) * we_float[idx])if ri < ke_float[idx]:
xif None == 0:
float32(ziggurat_exp_r_f - float32(np_log1pf(-next_float(bitgen))))if (None[idx - 1] - fe_float[idx]) * next_float(bitgen) + fe_float[idx] < float32(np.exp(float32(-x))):
x)()
random_standard_exponential_inv = (lambda bitgen: -np_log1p(-next_double(bitgen)))()
random_standard_exponential_inv_f = (lambda bitgen: -np.log(float32(1) - next_float(bitgen)))()
random_standard_gamma = (lambda bitgen, shape: if shape == 1:
random_standard_exponential(bitgen)if None == 0:
0if None < 1:
U = next_double(bitgen)V = random_standard_exponential(bitgen)if U <= 1 - shape:
X = pow(U, 1 / shape)if X <= V:
XY = -np.log((1 - U) / shape)X = pow((1 - shape) + shape * Y, 1 / shape)if X <= V + Y:
Xb = shape - 0.333333c = 1 / np.sqrt(9 * b)X = random_standard_normal(bitgen)V = 1 + c * Xif V > 0:
passV = V * V * VU = next_double(bitgen)if U < 1 - 0.0331 * X * X * X * X:
b * Vif None.log(U) < 0.5 * X * X + b * ((1 - V) + np.log(V)):
b * V)()
random_standard_gamma_f = (lambda bitgen, shape: f32_one = float32(1)shape = float32(shape)if shape == f32_one:
random_standard_exponential_f(bitgen)if None == float32(0):
float32(0)if None < f32_one:
U = next_float(bitgen)V = random_standard_exponential_f(bitgen)if U <= f32_one - shape:
X = float32(pow(U, float32(f32_one / shape)))if X <= V:
XY = float32(-np.log(float32((f32_one - U) / shape)))X = float32(pow((f32_one - shape) + float32(shape * Y), float32(f32_one / shape)))if X <= V + Y:
Xb = shape - f32_one / float32(3)c = float32(f32_one / float32(np.sqrt(float32(9) * b)))X = float32(random_standard_normal_f(bitgen))V = float32(f32_one + c * X)if V > float32(0):
passV = float32(V * V * V)U = next_float(bitgen)if U < f32_one - float32(0.0331) * X * X * X * X:
float32(b * V)if None.log(U) < float32(0.5) * X * X + b * ((f32_one - V) + np.log(V)):
float32(b * V))()
random_normal = (lambda bitgen, loc, scale: scaled_normal = scale * random_standard_normal(bitgen)loc + scaled_normal)()
random_normal_f = (lambda bitgen, loc, scale: scaled_normal = float32(scale * random_standard_normal_f(bitgen))float32(loc + scaled_normal))()
random_exponential = (lambda bitgen, scale: scale * random_standard_exponential(bitgen))()
random_uniform = (lambda bitgen, lower, range: scaled_uniform = range * next_double(bitgen)lower + scaled_uniform)()
random_gamma = (lambda bitgen, shape, scale: scale * random_standard_gamma(bitgen, shape))()
random_gamma_f = (lambda bitgen, shape, scale: float32(scale * random_standard_gamma_f(bitgen, shape)))()
random_beta = (lambda bitgen, a, b: if a <= 1 and b <= 1:
U = next_double(bitgen)V = next_double(bitgen)X = pow(U, 1 / a)Y = pow(V, 1 / b)XpY = X + Yif XpY <= 1 and XpY > 0:
if X + Y > 0:
X / XpYlogX = None.log(U) / alogY = np.log(V) / blogM = min(logX, logY)logX -= logMlogY -= logMnp.exp(logX - np.log(np.exp(logX) + np.exp(logY)))Ga = random_standard_gamma(bitgen, a)Gb = random_standard_gamma(bitgen, b)Ga / (Ga + Gb))()
random_chisquare = (lambda bitgen, df: 2 * random_standard_gamma(bitgen, df / 2))()
random_f = (lambda bitgen, dfnum, dfden: random_chisquare(bitgen, dfnum) * dfden / (random_chisquare(bitgen, dfden) * dfnum))()
random_standard_cauchy = (lambda bitgen: random_standard_normal(bitgen) / random_standard_normal(bitgen))()
random_pareto = (lambda bitgen, a: np_expm1(random_standard_exponential(bitgen) / a))()
random_weibull = (lambda bitgen, a: if a == 0:
0None(random_standard_exponential(bitgen), 1 / a))()
random_power = (lambda bitgen, a: pow(-np_expm1(-random_standard_exponential(bitgen)), 1 / a))()
random_laplace = (lambda bitgen, loc, scale: U = next_double(bitgen)# WARNING: Decompyle incomplete
)()
random_logistic = (lambda bitgen, loc, scale: U = next_double(bitgen)# WARNING: Decompyle incomplete
)()
random_lognormal = (lambda bitgen, mean, sigma: np.exp(random_normal(bitgen, mean, sigma)))()
random_standard_t = (lambda bitgen, df: num = random_standard_normal(bitgen)denom = random_standard_gamma(bitgen, df / 2)np.sqrt(df / 2) * num / np.sqrt(denom))()
random_wald = (lambda bitgen, mean, scale: mu_2l = mean / (2 * scale)Y = random_standard_normal(bitgen)Y = mean * Y * YX = mean + mu_2l * (Y - np.sqrt(4 * scale * Y + Y * Y))U = next_double(bitgen)if U <= mean / (mean + X):
XNone * mean / X)()
random_geometric_search = (lambda bitgen, p: X = 1sum = pprod = pq = 1 - pU = next_double(bitgen)# WARNING: Decompyle incomplete
)()
random_geometric_inversion = (lambda bitgen, p: np.ceil(-random_standard_exponential(bitgen) / np.log1p(-p)))()
random_geometric = (lambda bitgen, p: if p >= 0.333333:
random_geometric_search(bitgen, p)None(bitgen, p))()
random_triangular = (lambda bitgen, left, mode, right: base = right - leftleftbase = mode - leftratio = leftbase / baseleftprod = leftbase * baserightprod = (right - mode) * baseU = next_double(bitgen)if U <= ratio:
left + np.sqrt(U * leftprod)None - np.sqrt((1 - U) * rightprod))()
random_loggam = (lambda x: a = [
0.0833333,
-0.00277778,
0.000793651,
-0.000595238,
0.000841751,
-0.00191753,
0.00641026,
-0.0295507,
0.179644,
-1.39243]if x == 1 or x == 2:
0if None < 7:
n = int(7 - x)else:
n = 0x0 = x + nx2 = (1 / x0) * (1 / x0)lg2pi = 1.83788gl0 = a[9]for k in range(0, 9):
gl0 *= x2gl0 += a[8 - k]gl = gl0 / x0 + 0.5 * lg2pi + (x0 - 0.5) * np.log(x0) - x0if x < 7:
for k in range(1, n + 1):
gl = gl - np.log(x0 - 1)x0 = x0 - 1gl)()
random_poisson_mult = (lambda bitgen, lam: enlam = np.exp(-lam)X = 0prod = 1U = next_double(bitgen)prod *= Uif prod > enlam:
X += 1else:
X)()
random_poisson_ptrs = (lambda bitgen, lam: slam = np.sqrt(lam)loglam = np.log(lam)b = 0.931 + 2.53 * slama = -0.059 + 0.02483 * binvalpha = 1.1239 + 1.1328 / (b - 3.4)vr = 0.9277 - 3.6224 / (b - 2)U = next_double(bitgen) - 0.5V = next_double(bitgen)us = 0.5 - np.fabs(U)k = int((2 * a / us + b) * U + lam + 0.43)if us >= 0.07 and V <= vr:
kif (None < 0 or us < 0.013) and V > us:
continueif np.log(V) + np.log(invalpha) - np.log(a / (us * us) + b) <= -lam + k * loglam - random_loggam(k + 1):
k)()
random_poisson = (lambda bitgen, lam: if lam >= 10:
random_poisson_ptrs(bitgen, lam)if None == 0:
0None(bitgen, lam))()
random_negative_binomial = (lambda bitgen, n, p: Y = random_gamma(bitgen, n, (1 - p) / p)random_poisson(bitgen, Y))()
random_noncentral_chisquare = (lambda bitgen, df, nonc: if np.isnan(nonc):
np.nanif None == 0:
random_chisquare(bitgen, df)if None < df:
Chi2 = random_chisquare(bitgen, df - 1)n = random_standard_normal(bitgen) + np.sqrt(nonc)Chi2 + n * ni = None(bitgen, nonc / 2)random_chisquare(bitgen, df + 2 * i))()
random_noncentral_f = (lambda bitgen, dfnum, dfden, nonc: t = random_noncentral_chisquare(bitgen, dfnum, nonc) * dfdent / (random_chisquare(bitgen, dfden) * dfnum))()
random_logseries = (lambda bitgen, p: r = np_log1p(-p)V = next_double(bitgen)if V >= p:
1U = None(bitgen)q = -np.expm1(r * U)if V <= q * q:
result = int64(np.floor(1 + np.log(V) / np.log(q)))if result < 1 or V == 0:
continueresultif None >= q:
1)()
random_binomial_btpe = (lambda bitgen, n, p: r = min(p, 1 - p)q = 1 - rfm = n * r + rm = int(np.floor(fm))p1 = np.floor(2.195 * np.sqrt(n * r * q) - 4.6 * q) + 0.5xm = m + 0.5xl = xm - p1xr = xm + p1c = 0.134 + 20.5 / (15.3 + m)a = (fm - xl) / (fm - xl * r)laml = a * (1 + a / 2)a = (xr - fm) / (xr * q)lamr = a * (1 + a / 2)p2 = p1 * (1 + 2 * c)p3 = p2 + c / lamlp4 = p3 + c / lamrcase = 10y = 0k = 0if case == 10:
nrq = n * r * qu = next_double(bitgen) * p4v = next_double(bitgen)if u > p1:
case = 20continuey = int(np.floor((xm - p1 * v) + u))case = 60continueif case == 20:
if u > p2:
case = 30continuex = xl + (u - p1) / cv = v * c + 1 - np.fabs((m - x) + 0.5) / p1if v > 1:
case = 10continuey = int(np.floor(x))case = 50continueif case == 30:
if u > p3:
case = 40continuey = int(np.floor(xl + np.log(v) / laml))if y < 0 or v == 0:
case = 10continuev = v * (u - p2) * lamlcase = 50continueif case == 40:
y = int(np.floor(xr - np.log(v) / lamr))if y > n or v == 0:
case = 10continuev = v * (u - p3) * lamrcase = 50continueif case == 50:
k = abs(y - m)if k > 20 and k < nrq / 2 - 1:
case = 52continues = r / qa = s * (n + 1)F = 1if m < y:
for i in range(m + 1, y + 1):
F = F * (a / i - s)if m > y:
for i in range(y + 1, m + 1):
F = F / (a / i - s)if v > F:
case = 10continuecase = 60continueif case == 52:
rho = (k / nrq) * ((k * (k / 3 + 0.625) + 0.166667) / nrq + 0.5)t = -k * k / (2 * nrq)A = np.log(v)if A < t - rho:
case = 60continueif A > t + rho:
case = 10continuex1 = y + 1f1 = m + 1z = n + 1 - mw = (n - y) + 1x2 = x1 * x1f2 = f1 * f1z2 = z * zw2 = w * wif A > xm * np.log(f1 / x1) + ((n - m) + 0.5) * np.log(z / w) + (y - m) * np.log(w * r / (x1 * q)) + (13680 - (462 - (132 - (99 - 140 / f2) / f2) / f2) / f2) / f1 / 166320 + (13680 - (462 - (132 - (99 - 140 / z2) / z2) / z2) / z2) / z / 166320 + (13680 - (462 - (132 - (99 - 140 / x2) / x2) / x2) / x2) / x1 / 166320 + (13680 - (462 - (132 - (99 - 140 / w2) / w2) / w2) / w2) / w / 66320:
case = 10continuecase = 60continueif case == 60:
if p > 0.5:
y = n - yy)()
random_binomial_inversion = (lambda bitgen, n, p: q = 1 - pqn = np.exp(n * np.log(q))_np = n * pbound = min(n, _np + 10 * np.sqrt(_np * q + 1))X = 0px = qnU = next_double(bitgen)# WARNING: Decompyle incomplete
)()
random_binomial = (lambda bitgen, n, p: if n == 0 or p == 0:
0if None <= 0.5:
if p * n <= 30:
random_binomial_inversion(bitgen, n, p)None(bitgen, n, p)q = None - pif q * n <= 30:
n - random_binomial_inversion(bitgen, n, q)None - random_binomial_btpe(bitgen, n, q))()
