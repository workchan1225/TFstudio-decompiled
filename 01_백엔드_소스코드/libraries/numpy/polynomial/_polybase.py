# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _polybase.pyc (Python 3.11)

'''
Abstract base class for the various polynomial Classes.

The ABCPolyBase class provides the methods needed to implement the common API
for the various polynomial classes. It operates as a mixin, but uses the
abc module from the stdlib, hence it is only available for Python >= 2.6.

'''
import os
import abc
import numbers
import numpy as np
from  import polyutils as pu
__all__ = [
    'ABCPolyBase']

class ABCPolyBase(abc.ABC):
    """An abstract base class for immutable series classes.

    ABCPolyBase provides the standard Python numerical methods
    '+', '-', '*', '//', '%', 'divmod', '**', and '()' along with the
    methods listed below.

    .. versionadded:: 1.9.0

    Parameters
    ----------
    coef : array_like
        Series coefficients in order of increasing degree, i.e.,
        ``(1, 2, 3)`` gives ``1*P_0(x) + 2*P_1(x) + 3*P_2(x)``, where
        ``P_i`` is the basis polynomials of degree ``i``.
    domain : (2,) array_like, optional
        Domain to use. The interval ``[domain[0], domain[1]]`` is mapped
        to the interval ``[window[0], window[1]]`` by shifting and scaling.
        The default value is the derived class domain.
    window : (2,) array_like, optional
        Window, see domain for its use. The default value is the
        derived class window.
    symbol : str, optional
        Symbol used to represent the independent variable in string 
        representations of the polynomial expression, e.g. for printing.
        The symbol must be a valid Python identifier. Default value is 'x'.

        .. versionadded:: 1.24

    Attributes
    ----------
    coef : (N,) ndarray
        Series coefficients in order of increasing degree.
    domain : (2,) ndarray
        Domain that is mapped to window.
    window : (2,) ndarray
        Window that domain is mapped to.
    symbol : str
        Symbol representing the independent variable.

    Class Attributes
    ----------------
    maxpower : int
        Maximum power allowed, i.e., the largest number ``n`` such that
        ``p(x)**n`` is allowed. This is to limit runaway polynomial size.
    domain : (2,) ndarray
        Default domain of the class.
    window : (2,) ndarray
        Default window of the class.

    """
    __hash__ = None
    __array_ufunc__ = None
    maxpower = 100
    _superscript_mapping = str.maketrans({
        '0': '⁰',
        '1': '¹',
        '2': '²',
        '3': '³',
        '4': '⁴',
        '5': '⁵',
        '6': '⁶',
        '7': '⁷',
        '8': '⁸',
        '9': '⁹' })
    _subscript_mapping = str.maketrans({
        '0': '₀',
        '1': '₁',
        '2': '₂',
        '3': '₃',
        '4': '₄',
        '5': '₅',
        '6': '₆',
        '7': '₇',
        '8': '₈',
        '9': '₉' })
    _use_unicode = not (os.name == 'nt')
    symbol = (lambda self: self._symbol)()
    domain = (lambda self: pass)()()
    window = (lambda self: pass)()()
    basis_name = (lambda self: pass)()()
    _add = (lambda c1, c2: pass)()()
    _sub = (lambda c1, c2: pass)()()
    _mul = (lambda c1, c2: pass)()()
    _div = (lambda c1, c2: pass)()()
    _pow = (lambda c, pow, maxpower = (None,): pass)()()
    _val = (lambda x, c: pass)()()
    _int = (lambda c, m, k, lbnd, scl: pass)()()
    _der = (lambda c, m, scl: pass)()()
    _fit = (lambda x, y, deg, rcond, full: pass)()()
    _line = (lambda off, scl: pass)()()
    _roots = (lambda c: pass)()()
    _fromroots = (lambda r: pass)()()
    
    def has_samecoef(self, other):
        '''Check if coefficients match.

        .. versionadded:: 1.6.0

        Parameters
        ----------
        other : class instance
            The other class must have the ``coef`` attribute.

        Returns
        -------
        bool : boolean
            True if the coefficients are the same, False otherwise.

        '''
        if len(self.coef) != len(other.coef):
            return False
        if not None.all(self.coef == other.coef):
            return False

    
    def has_samedomain(self, other):
        '''Check if domains match.

        .. versionadded:: 1.6.0

        Parameters
        ----------
        other : class instance
            The other class must have the ``domain`` attribute.

        Returns
        -------
        bool : boolean
            True if the domains are the same, False otherwise.

        '''
        return np.all(self.domain == other.domain)

    
    def has_samewindow(self, other):
        '''Check if windows match.

        .. versionadded:: 1.6.0

        Parameters
        ----------
        other : class instance
            The other class must have the ``window`` attribute.

        Returns
        -------
        bool : boolean
            True if the windows are the same, False otherwise.

        '''
        return np.all(self.window == other.window)

    
    def has_sametype(self, other):
        '''Check if types match.

        .. versionadded:: 1.7.0

        Parameters
        ----------
        other : object
            Class instance.

        Returns
        -------
        bool : boolean
            True if other is same class as self

        '''
        return isinstance(other, self.__class__)

    
    def _get_coefficients(self, other):
        '''Interpret other as polynomial coefficients.

        The `other` argument is checked to see if it is of the same
        class as self with identical domain and window. If so,
        return its coefficients, otherwise return `other`.

        .. versionadded:: 1.9.0

        Parameters
        ----------
        other : anything
            Object to be checked.

        Returns
        -------
        coef
            The coefficients of`other` if it is a compatible instance,
            of ABCPolyBase, otherwise `other`.

        Raises
        ------
        TypeError
            When `other` is an incompatible instance of ABCPolyBase.

        '''
        if isinstance(other, ABCPolyBase):
            if not isinstance(other, self.__class__):
                raise TypeError('Polynomial types differ')
            if not np.all(self.domain == other.domain):
                raise TypeError('Domains differ')
            if not np.all(self.window == other.window):
                raise TypeError('Windows differ')
            if self.symbol != other.symbol:
                raise ValueError('Polynomial symbols differ')
            return other.coef

    
    def __init__(self, coef, domain, window, symbol = (None, None, 'x')):
        (coef,) = pu.as_series([
            coef], trim = False)
        self.coef = coef
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        coef = repr(self.coef)[6:-1]
        domain = repr(self.domain)[6:-1]
        window = repr(self.window)[6:-1]
        name = self.__class__.__name__
        return f'''{name}({coef}, domain={domain}, window={window}, symbol=\'{self.symbol}\')'''

    
    def __format__(self, fmt_str):
        if fmt_str == '':
            return self.__str__()
        if None not in ('ascii', 'unicode'):
            raise ValueError(f'''Unsupported format string \'{fmt_str}\' passed to {self.__class__}.__format__. Valid options are \'ascii\' and \'unicode\'''')
        if fmt_str == 'ascii':
            return self._generate_string(self._str_term_ascii)
        return None._generate_string(self._str_term_unicode)

    
    def __str__(self):
        if self._use_unicode:
            return self._generate_string(self._str_term_unicode)
        return None._generate_string(self._str_term_ascii)

    
    def _generate_string(self, term_method):
        '''
        Generate the full string representation of the polynomial, using
        ``term_method`` to generate each polynomial term.
        '''
        linewidth = np.get_printoptions().get('linewidth', 75)
        if linewidth < 1:
            linewidth = 1
        out = pu.format_float(self.coef[0])
        for i, coef in enumerate(self.coef[1:]):
            out += ' '
            power = str(i + 1)
            if coef >= 0:
                next_term = '+ ' + pu.format_float(coef, parens = True)
            else:
                next_term = '- ' + pu.format_float(-coef, parens = True)
        except TypeError:
            next_term = f'''+ {coef}'''
        next_term += term_method(power, self.symbol)
        line_len = len(out.split('\n')[-1]) + len(next_term)
        if i < len(self.coef[1:]) - 1:
            line_len += 2
        if line_len >= linewidth:
            next_term = next_term.replace(' ', '\n', 1)
        out += next_term
        continue
        return out

    _str_term_unicode = (lambda cls, i, arg_str: pass# WARNING: Decompyle incomplete
)()
    _str_term_ascii = (lambda cls, i, arg_str: pass# WARNING: Decompyle incomplete
)()
    _repr_latex_term = (lambda cls, i, arg_str, needs_parens: pass# WARNING: Decompyle incomplete
)()
    _repr_latex_scalar = (lambda x, parens = (False,): '\\text{{{}}}'.format(pu.format_float(x, parens = parens)))()
    
    def _repr_latex_(self):
        (off, scale) = self.mapparms()
        if off == 0 and scale == 1:
            term = self.symbol
            needs_parens = False
        elif scale == 1:
            term = f'''{self._repr_latex_scalar(off)} + {self.symbol}'''
            needs_parens = True
        elif off == 0:
            term = f'''{self._repr_latex_scalar(scale)}{self.symbol}'''
            needs_parens = True
        else:
            term = f'''{self._repr_latex_scalar(off)} + {self._repr_latex_scalar(scale)}{self.symbol}'''
            needs_parens = True
        mute = '\\color{{LightGray}}{{{}}}'.format
        parts = []
        for i, c in enumerate(self.coef):
            if i == 0:
                coef_str = f'''{self._repr_latex_scalar(c)}'''
            elif not isinstance(c, numbers.Real):
                coef_str = f''' + ({self._repr_latex_scalar(c)})'''
            elif not np.signbit(c):
                coef_str = f''' + {self._repr_latex_scalar(c, parens = True)}'''
            else:
                coef_str = f''' - {self._repr_latex_scalar(-c, parens = True)}'''
            term_str = self._repr_latex_term(i, term, needs_parens)
            if term_str == '1':
                part = coef_str
            else:
                part = f'''{coef_str}\\,{term_str}'''
            if c == 0:
                part = mute(part)
            parts.append(part)
            if parts:
                body = ''.join(parts)
            else:
                body = '0'
        return f'''${self.symbol} \\mapsto {body}$'''

    
    def __getstate__(self):
        ret = self.__dict__.copy()
        ret['coef'] = self.coef.copy()
        ret['domain'] = self.domain.copy()
        ret['window'] = self.window.copy()
        ret['symbol'] = self.symbol
        return ret

    
    def __setstate__(self, dict):
        self.__dict__ = dict

    
    def __call__(self, arg):
        (off, scl) = pu.mapparms(self.domain, self.window)
        arg = off + scl * arg
        return self._val(arg, self.coef)

    
    def __iter__(self):
        return iter(self.coef)

    
    def __len__(self):
        return len(self.coef)

    
    def __neg__(self):
        return self.__class__(-(self.coef), self.domain, self.window, self.symbol)

    
    def __pos__(self):
        return self

    
    def __add__(self, other):
        othercoef = self._get_coefficients(other)
        
        try:
            coef = self._add(self.coef, othercoef)
        except Exception:
            return 

        return self.__class__(coef, self.domain, self.window, self.symbol)

    
    def __sub__(self, other):
        othercoef = self._get_coefficients(other)
        
        try:
            coef = self._sub(self.coef, othercoef)
        except Exception:
            return 

        return self.__class__(coef, self.domain, self.window, self.symbol)

    
    def __mul__(self, other):
        othercoef = self._get_coefficients(other)
        
        try:
            coef = self._mul(self.coef, othercoef)
        except Exception:
            return 

        return self.__class__(coef, self.domain, self.window, self.symbol)

    
    def __truediv__(self, other):
        if isinstance(other, numbers.Number) or isinstance(other, bool):
            raise TypeError(f'''unsupported types for true division: \'{type(self)}\', \'{type(other)}\'''')
        return self.__floordiv__(other)

    
    def __floordiv__(self, other):
        res = self.__divmod__(other)
        if res is NotImplemented:
            return res
        return None[0]

    
    def __mod__(self, other):
        res = self.__divmod__(other)
        if res is NotImplemented:
            return res
        return None[1]

    
    def __divmod__(self, other):
        othercoef = self._get_coefficients(other)
        
        try:
            (quo, rem) = self._div(self.coef, othercoef)
        except ZeroDivisionError:
            raise 
            except Exception:
                return 

        self.__class__(rem, self.domain, self.window, self.symbol) = self.__class__(quo, self.domain, self.window, self.symbol)
        return (quo, rem)

    
    def __pow__(self, other):
        coef = self._pow(self.coef, other, maxpower = self.maxpower)
        res = self.__class__(coef, self.domain, self.window, self.symbol)
        return res

    
    def __radd__(self, other):
        
        try:
            coef = self._add(other, self.coef)
        except Exception:
            return 

        return self.__class__(coef, self.domain, self.window, self.symbol)

    
    def __rsub__(self, other):
        
        try:
            coef = self._sub(other, self.coef)
        except Exception:
            return 

        return self.__class__(coef, self.domain, self.window, self.symbol)

    
    def __rmul__(self, other):
        
        try:
            coef = self._mul(other, self.coef)
        except Exception:
            return 

        return self.__class__(coef, self.domain, self.window, self.symbol)

    
    def __rdiv__(self, other):
        return self.__rfloordiv__(other)

    
    def __rtruediv__(self, other):
        return NotImplemented

    
    def __rfloordiv__(self, other):
        res = self.__rdivmod__(other)
        if res is NotImplemented:
            return res
        return None[0]

    
    def __rmod__(self, other):
        res = self.__rdivmod__(other)
        if res is NotImplemented:
            return res
        return None[1]

    
    def __rdivmod__(self, other):
        
        try:
            (quo, rem) = self._div(other, self.coef)
        except ZeroDivisionError:
            raise 
            except Exception:
                return 

        self.__class__(rem, self.domain, self.window, self.symbol) = self.__class__(quo, self.domain, self.window, self.symbol)
        return (quo, rem)

    
    def __eq__(self, other):
