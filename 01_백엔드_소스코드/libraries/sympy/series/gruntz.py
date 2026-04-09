# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: gruntz.pyc (Python 3.11)

'''
Limits
======

Implemented according to the PhD thesis
https://www.cybertester.com/data/gruntz.pdf, which contains very thorough
descriptions of the algorithm including many examples.  We summarize here
the gist of it.

All functions are sorted according to how rapidly varying they are at
infinity using the following rules. Any two functions f and g can be
compared using the properties of L:

L=lim  log|f(x)| / log|g(x)|           (for x -> oo)

We define >, < ~ according to::

    1. f > g .... L=+-oo

        we say that:
        - f is greater than any power of g
        - f is more rapidly varying than g
        - f goes to infinity/zero faster than g

    2. f < g .... L=0

        we say that:
        - f is lower than any power of g

    3. f ~ g .... L!=0, +-oo

        we say that:
        - both f and g are bounded from above and below by suitable integral
          powers of the other

Examples
========
::
    2 < x < exp(x) < exp(x**2) < exp(exp(x))
    2 ~ 3 ~ -5
    x ~ x**2 ~ x**3 ~ 1/x ~ x**m ~ -x
    exp(x) ~ exp(-x) ~ exp(2x) ~ exp(x)**2 ~ exp(x+exp(-x))
    f ~ 1/f

So we can divide all the functions into comparability classes (x and x^2
belong to one class, exp(x) and exp(-x) belong to some other class). In
principle, we could compare any two functions, but in our algorithm, we
do not compare anything below the class 2~3~-5 (for example log(x) is
below this), so we set 2~3~-5 as the lowest comparability class.

Given the function f, we find the list of most rapidly varying (mrv set)
subexpressions of it. This list belongs to the same comparability class.
Let\'s say it is {exp(x), exp(2x)}. Using the rule f ~ 1/f we find an
element "w" (either from the list or a new one) from the same
comparability class which goes to zero at infinity. In our example we
set w=exp(-x) (but we could also set w=exp(-2x) or w=exp(-3x) ...). We
rewrite the mrv set using w, in our case {1/w, 1/w^2}, and substitute it
into f. Then we expand f into a series in w::

    f = c0*w^e0 + c1*w^e1 + ... + O(w^en),       where e0<e1<...<en, c0!=0

but for x->oo, lim f = lim c0*w^e0, because all the other terms go to zero,
because w goes to zero faster than the ci and ei. So::

    for e0>0, lim f = 0
    for e0<0, lim f = +-oo   (the sign depends on the sign of c0)
    for e0=0, lim f = lim c0

We need to recursively compute limits at several places of the algorithm, but
as is shown in the PhD thesis, it always finishes.

Important functions from the implementation:

compare(a, b, x) compares "a" and "b" by computing the limit L.
mrv(e, x) returns list of most rapidly varying (mrv) subexpressions of "e"
rewrite(e, Omega, x, wsym) rewrites "e" in terms of w
leadterm(f, x) returns the lowest power term in the series of f
mrv_leadterm(e, x) returns the lead term (c0, e0) for e
limitinf(e, x) computes lim e  (for x->oo)
limit(e, z, z0) computes any limit by converting it to the case x->oo

All the functions are really simple and straightforward except
rewrite(), which is the most difficult/complex part of the algorithm.
When the algorithm fails, the bugs are usually in the series expansion
(i.e. in SymPy) or in rewrite.

This code is almost exact rewrite of the Maple code inside the Gruntz
thesis.

Debugging
---------

Because the gruntz algorithm is highly recursive, it\'s difficult to
figure out what went wrong inside a debugger. Instead, turn on nice
debug prints by defining the environment variable SYMPY_DEBUG. For
example:

[user@localhost]: SYMPY_DEBUG=True ./bin/isympy

In [1]: limit(sin(x)/x, x, 0)
limitinf(_x*sin(1/_x), _x) = 1
+-mrv_leadterm(_x*sin(1/_x), _x) = (1, 0)
| +-mrv(_x*sin(1/_x), _x) = set([_x])
| | +-mrv(_x, _x) = set([_x])
| | +-mrv(sin(1/_x), _x) = set([_x])
| |   +-mrv(1/_x, _x) = set([_x])
| |     +-mrv(_x, _x) = set([_x])
| +-mrv_leadterm(exp(_x)*sin(exp(-_x)), _x, set([exp(_x)])) = (1, 0)
|   +-rewrite(exp(_x)*sin(exp(-_x)), set([exp(_x)]), _x, _w) = (1/_w*sin(_w), -_x)
|     +-sign(_x, _x) = 1
|     +-mrv_leadterm(1, _x) = (1, 0)
+-sign(0, _x) = 0
+-limitinf(1, _x) = 1

And check manually which line is wrong. Then go to the source code and
debug this function to figure out the exact problem.

'''
from functools import reduce
from sympy.core import Basic, S, Mul, PoleError, expand_mul
from sympy.core.cache import cacheit
from sympy.core.intfunc import ilcm
from sympy.core.numbers import I, oo
from sympy.core.symbol import Dummy, Wild
from sympy.core.traversal import bottom_up
from sympy.functions import log, exp, sign as _sign
from sympy.series.order import Order
from sympy.utilities.exceptions import SymPyDeprecationWarning
from sympy.utilities.misc import debug_decorator as debug
from sympy.utilities.timeutils import timethis
timeit = timethis('gruntz')

def compare(a, b, x):
    '''Returns "<" if a<b, "=" for a == b, ">" for a>b'''
    lb = log(b)
    la = log(a)
    if isinstance(a, Basic):
        if (isinstance(a, exp) or a.is_Pow) and a.base == S.Exp1:
            la = a.exp
    if isinstance(b, Basic):
        if (isinstance(b, exp) or b.is_Pow) and b.base == S.Exp1:
            lb = b.exp
    c = limitinf(la / lb, x)
    if c == 0:
        return '<'
    if None.is_infinite:
        return '>'


class SubsSet(dict):
    pass
# WARNING: Decompyle incomplete

mrv = (lambda e, x: pass# WARNING: Decompyle incomplete
)()

def mrv_max3(f, expsf, g, expsg, union, expsboth, x):
    '''
    Computes the maximum of two sets of expressions f and g, which
    are in the same comparability class, i.e. max() compares (two elements of)
    f and g and returns either (f, expsf) [if f is larger], (g, expsg)
    [if g is larger] or (union, expsboth) [if f, g are of the same class].
    '''
    if not isinstance(f, SubsSet):
        raise TypeError('f should be an instance of SubsSet')
    if not isinstance(g, SubsSet):
        raise TypeError('g should be an instance of SubsSet')
    if f == SubsSet():
        return (g, expsg)
    if None == SubsSet():
        return (f, expsf)
    if None.meets(g):
        return (union, expsboth)
    c = None(list(f.keys())[0], list(g.keys())[0], x)
    if c == '>':
        return (f, expsf)
    if None == '<':
        return (g, expsg)
    if None != '=':
        raise ValueError('c should be =')
    return (union, expsboth)


def mrv_max1(f, g, exps, x):
    '''Computes the maximum of two sets of expressions f and g, which
    are in the same comparability class, i.e. mrv_max1() compares (two elements of)
    f and g and returns the set, which is in the higher comparability class
    of the union of both, if they have the same order of variation.
    Also returns exps, with the appropriate substitutions made.
    '''
    (u, b) = f.union(g, exps)
    return mrv_max3(f, g.do_subs(exps), g, f.do_subs(exps), u, b, x)

sign = (lambda e, x: if not isinstance(e, Basic):
raise TypeError('e should be an instance of Basic')if e.is_positive:
1if None.is_negative:
-1if None.is_zero:
0if not None.has(x):
logcombine = logcombineimport sympy.simplifye = logcombine(e)_sign(e)if None == x:
1if None.is_Mul:
(a, b) = e.as_two_terms()sa = sign(a, x)if not sa:
0None * sign(b, x)if None(e, exp):
1if None.is_Pow:
if e.base == S.Exp1:
1s = None(e.base, x)if s == 1:
1if None.exp.is_Integer:
s ** e.expif isinstance(e, log):
sign(e.args[0] - 1, x)(c0, e0) = None(e, x)sign(c0, x))()()()
limitinf = (lambda e, x: old = eif not e.has(x):
epowdenest = powdenestimport sympy.simplify.powsimpAccumBounds = AccumBoundsimport sympy.calculus.utilif e.has(Order):
e = e.expand().removeO()if x.is_positive or x.is_integer:
p = Dummy('p', positive = True)e = e.subs(x, p)x = pe = e.rewrite('tractable', deep = True, limitvar = x)e = powdenest(e)if isinstance(e, AccumBounds):
if mrv_leadterm(e.min, x) != mrv_leadterm(e.max, x):
raise NotImplementedError(c0, e0) = mrv_leadterm(e.min, x)else:
(c0, e0) = mrv_leadterm(e, x)sig = sign(e0, x)if sig == 1:
S.Zeroif None == -1:
if c0.match(I * Wild('a', exclude = [
I])):
c0 * oos = None(c0, x)if s == 0:
raise ValueError('Leading term should not be 0')s * ooif None == 0:
if c0 == old:
c0 = c0.cancel()limitinf(c0, x)raise None('{} could not be evaluated'.format(sig)))()()()

def moveup2(s, x):
    r = SubsSet()
    for expr, var in s.items():
        r[expr.xreplace({
            x: exp(x) })] = var
        for var, expr in s.rewrites.items():
            r.rewrites[var] = s.rewrites[var].xreplace({
                x: exp(x) })
            return r


def moveup(l, x):
    pass
# WARNING: Decompyle incomplete

calculate_series = (lambda e, x, logx = (None,): SymPyDeprecationWarning(feature = 'calculate_series', useinstead = 'series() with suitable n, or as_leading_term', issue = 21838, deprecated_since_version = '1.12').warn()powdenest = powdenestimport sympy.simplify.powsimpfor t in e.lseries(x, logx = logx):
t = bottom_up(t, (lambda w: pass# WARNING: Decompyle incomplete
))
        t = t.factor()
        if t.has(exp) and t.has(log):
            t = powdenest(t)
        if not t.is_zero:
            pass
        
        return t
)()()
mrv_leadterm = (lambda e, x: Omega = SubsSet()if not e.has(x):
(e, S.Zero)if None == SubsSet():
(Omega, exps) = mrv(e, x)if not Omega:
(exps, S.Zero)if None in Omega:
Omega_up = moveup2(Omega, x)exps_up = moveup([
exps], x)[0]Omega = Omega_upexps = exps_upw = Dummy('w', positive = True)(f, logw) = rewrite(exps, Omega, x, w)# WARNING: Decompyle incomplete
)()()()

def build_expression_tree(Omega, rewrites):
    ''' Helper function for rewrite.

    We need to sort Omega (mrv set) so that we replace an expression before
    we replace any expression in terms of which it has to be rewritten::

        e1 ---> e2 ---> e3
                 \\
                  -> e4

    Here we can do e1, e2, e3, e4 or e1, e2, e4, e3.
    To do this we assemble the nodes into a tree, and sort them by height.

    This function builds the tree, rewrites then sorts the nodes.
    '''
    
    class Node:
        
        def __init__(self):
            self.before = []
            self.expr = None
            self.var = None

        
        def ht(self):
            
            def <listcomp>(.0):
                return [ x.ht() for x in .0 ]

            return (lambda x, y: x + y)(<listcomp>, self.before(), 1)


    nodes = { }
    for expr, v in Omega:
        n = Node()
        n.var = v
        n.expr = expr
        nodes[v] = n
        for _, v in Omega:
            if v in rewrites:
                n = nodes[v]
                r = rewrites[v]
                for _, v2 in Omega:
                    if r.has(v2):
                        n.before.append(nodes[v2])
                    return nodes

rewrite = (lambda e, Omega, x, wsym: pass# WARNING: Decompyle incomplete
)()()

def gruntz(e, z, z0, dir = ('+',)):
    '''
    Compute the limit of e(z) at the point z0 using the Gruntz algorithm.

    Explanation
    ===========

    ``z0`` can be any expression, including oo and -oo.

    For ``dir="+"`` (default) it calculates the limit from the right
    (z->z0+) and for ``dir="-"`` the limit from the left (z->z0-). For infinite z0
    (oo or -oo), the dir argument does not matter.

    This algorithm is fully described in the module docstring in the gruntz.py
    file. It relies heavily on the series expansion. Most frequently, gruntz()
    is only used if the faster limit() function (which uses heuristics) fails.
    '''
    if not z.is_symbol:
        raise NotImplementedError('Second argument must be a Symbol')
    r = None
    if z0 in (oo, I * oo):
        e0 = e
    elif z0 in (-oo, -I * oo):
        e0 = e.subs(z, -z)
    elif str(dir) == '-':
        e0 = e.subs(z, z0 - 1 / z)
    elif str(dir) == '+':
        e0 = e.subs(z, z0 + 1 / z)
    else:
        raise NotImplementedError("dir must be '+' or '-'")
    r = limitinf(e0, z)
    return r.rewrite('intractable', deep = True)
