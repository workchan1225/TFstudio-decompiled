# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: abc.pyc (Python 3.11)

__doc__ = '\nThis module exports all latin and greek letters as Symbols, so you can\nconveniently do\n\n    >>> from sympy.abc import x, y\n\ninstead of the slightly more clunky-looking\n\n    >>> from sympy import symbols\n    >>> x, y = symbols(\'x y\')\n\nCaveats\n=======\n\n1. As of the time of writing this, the names ``O``, ``S``, ``I``, ``N``,\n``E``, and ``Q`` are colliding with names defined in SymPy. If you import them\nfrom both ``sympy.abc`` and ``sympy``, the second import will "win".\nThis is an issue only for * imports, which should only be used for short-lived\ncode such as interactive sessions and throwaway scripts that do not survive\nuntil the next SymPy upgrade, where ``sympy`` may contain a different set of\nnames.\n\n2. This module does not define symbol names on demand, i.e.\n``from sympy.abc import foo`` will be reported as an error because\n``sympy.abc`` does not contain the name ``foo``. To get a symbol named ``foo``,\nyou still need to use ``Symbol(\'foo\')`` or ``symbols(\'foo\')``.\nYou can freely mix usage of ``sympy.abc`` and ``Symbol``/``symbols``, though\nsticking with one and only one way to get the symbols does tend to make the code\nmore readable.\n\nThe module also defines some special names to help detect which names clash\nwith the default SymPy namespace.\n\n``_clash1`` defines all the single letter variables that clash with\nSymPy objects; ``_clash2`` defines the multi-letter clashing symbols;\nand ``_clash`` is the union of both. These can be passed for ``locals``\nduring sympification if one desires Symbols rather than the non-Symbol\nobjects for those names.\n\nExamples\n========\n\n>>> from sympy import S\n>>> from sympy.abc import _clash1, _clash2, _clash\n>>> S("Q & C", locals=_clash1)\nC & Q\n>>> S(\'pi(x)\', locals=_clash2)\npi(x)\n>>> S(\'pi(C, Q)\', locals=_clash)\npi(C, Q)\n\n'
from typing import Any, Dict as tDict
import string
from core import Symbol, symbols
from core.alphabets import greeks
from sympy.parsing.sympy_parser import null
(a, b, c, d, e, f, g, h, i, j) = symbols('a, b, c, d, e, f, g, h, i, j')
(k, l, m, n, o, p, q, r, s, t) = symbols('k, l, m, n, o, p, q, r, s, t')
(u, v, w, x, y, z) = symbols('u, v, w, x, y, z')
(A, B, C, D, E, F, G, H, I, J) = symbols('A, B, C, D, E, F, G, H, I, J')
(K, L, M, N, O, P, Q, R, S, T) = symbols('K, L, M, N, O, P, Q, R, S, T')
(U, V, W, X, Y, Z) = symbols('U, V, W, X, Y, Z')
(alpha, beta, gamma, delta) = symbols('alpha, beta, gamma, delta')
(epsilon, zeta, eta, theta) = symbols('epsilon, zeta, eta, theta')
(iota, kappa, lamda, mu) = symbols('iota, kappa, lamda, mu')
(nu, xi, omicron, pi) = symbols('nu, xi, omicron, pi')
(rho, sigma, tau, upsilon) = symbols('rho, sigma, tau, upsilon')
(phi, chi, psi, omega) = symbols('phi, chi, psi, omega')
_latin = list(string.ascii_letters)
_greek = list(greeks)
_greek.remove('lambda')
_greek.append('lamda')
ns: tDict[(str, Any)] = { }
exec('from sympy import *', ns)
_clash1: tDict[(str, Any)] = { }
_clash2: tDict[(str, Any)] = { }
# WARNING: Decompyle incomplete
