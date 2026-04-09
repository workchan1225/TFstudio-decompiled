# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ImageMath.pyc (Python 3.11)

from __future__ import annotations
import builtins
from  import Image, _imagingmath
TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Callable
    from types import CodeType
    from typing import Any

class _Operand:
    '''Wraps an image operand, providing standard operators'''
    
    def __init__(self = None, im = None):
        self.im = im

    
    def _Operand__fixup(self = None, im1 = None):
        if isinstance(im1, _Operand):
            if im1.im.mode in ('1', 'L'):
                return im1.im.convert('I')
            if None.im.mode in ('I', 'F'):
                return im1.im
            msg = f'''{im1.im.mode}'''
            raise ValueError(msg)
        if isinstance(im1, (int, float)) and self.im.mode in ('1', 'L', 'I'):
            return Image.new('I', self.im.size, im1)
        return None.new('F', self.im.size, im1)

    
    def apply(self = None, op = None, im1 = None, im2 = (None, None), mode = ('op', 'str', 'im1', '_Operand | float', 'im2', '_Operand | float | None', 'mode', 'str | None', 'return', '_Operand')):
        im_1 = self._Operand__fixup(im1)
    # WARNING: Decompyle incomplete

    
    def __bool__(self = None):
        return self.im.getbbox() is not None

    
    def __abs__(self = None):
        return self.apply('abs', self)

    
    def __pos__(self = None):
        return self

    
    def __neg__(self = None):
        return self.apply('neg', self)

    
    def __add__(self = None, other = None):
        return self.apply('add', self, other)

    
    def __radd__(self = None, other = None):
        return self.apply('add', other, self)

    
    def __sub__(self = None, other = None):
        return self.apply('sub', self, other)

    
    def __rsub__(self = None, other = None):
        return self.apply('sub', other, self)

    
    def __mul__(self = None, other = None):
        return self.apply('mul', self, other)

    
    def __rmul__(self = None, other = None):
        return self.apply('mul', other, self)

    
    def __truediv__(self = None, other = None):
        return self.apply('div', self, other)

    
    def __rtruediv__(self = None, other = None):
        return self.apply('div', other, self)

    
    def __mod__(self = None, other = None):
        return self.apply('mod', self, other)

    
    def __rmod__(self = None, other = None):
        return self.apply('mod', other, self)

    
    def __pow__(self = None, other = None):
        return self.apply('pow', self, other)

    
    def __rpow__(self = None, other = None):
        return self.apply('pow', other, self)

    
    def __invert__(self = None):
        return self.apply('invert', self)

    
    def __and__(self = None, other = None):
        return self.apply('and', self, other)

    
    def __rand__(self = None, other = None):
        return self.apply('and', other, self)

    
    def __or__(self = None, other = None):
        return self.apply('or', self, other)

    
    def __ror__(self = None, other = None):
        return self.apply('or', other, self)

    
    def __xor__(self = None, other = None):
        return self.apply('xor', self, other)

    
    def __rxor__(self = None, other = None):
        return self.apply('xor', other, self)

    
    def __lshift__(self = None, other = None):
        return self.apply('lshift', self, other)

    
    def __rshift__(self = None, other = None):
        return self.apply('rshift', self, other)

    
    def __eq__(self = None, other = None):
        return self.apply('eq', self, other)

    
    def __ne__(self = None, other = None):
        return self.apply('ne', self, other)

    
    def __lt__(self = None, other = None):
        return self.apply('lt', self, other)

    
    def __le__(self = None, other = None):
        return self.apply('le', self, other)

    
    def __gt__(self = None, other = None):
        return self.apply('gt', self, other)

    
    def __ge__(self = None, other = None):
        return self.apply('ge', self, other)



def imagemath_int(self = None):
    return _Operand(self.im.convert('I'))


def imagemath_float(self = None):
    return _Operand(self.im.convert('F'))


def imagemath_equal(self = None, other = None):
    return self.apply('eq', self, other, mode = 'I')


def imagemath_notequal(self = None, other = None):
    return self.apply('ne', self, other, mode = 'I')


def imagemath_min(self = None, other = None):
    return self.apply('min', self, other)


def imagemath_max(self = None, other = None):
    return self.apply('max', self, other)


def imagemath_convert(self = None, mode = None):
    return _Operand(self.im.convert(mode))

ops = {
    'int': imagemath_int,
    'float': imagemath_float,
    'equal': imagemath_equal,
    'notequal': imagemath_notequal,
    'min': imagemath_min,
    'max': imagemath_max,
    'convert': imagemath_convert }

def lambda_eval(expression = None, **kw):
    """
    Returns the result of an image function.

    :py:mod:`~PIL.ImageMath` only supports single-layer images. To process multi-band
    images, use the :py:meth:`~PIL.Image.Image.split` method or
    :py:func:`~PIL.Image.merge` function.

    :param expression: A function that receives a dictionary.
    :param **kw: Values to add to the function's dictionary.
    :return: The expression result. This is usually an image object, but can
             also be an integer, a floating point value, or a pixel tuple,
             depending on the expression.
    """
    args = ops.copy()
    args.update(kw)
    for k, v in args.items():
        if isinstance(v, Image.Image):
            args[k] = _Operand(v)
        out = expression(args)
        
        try:
            return out.im
        except AttributeError:
            return 



def unsafe_eval(expression = None, **kw):
    """
    Evaluates an image expression. This uses Python's ``eval()`` function to process
    the expression string, and carries the security risks of doing so. It is not
    recommended to process expressions without considering this.
    :py:meth:`~lambda_eval` is a more secure alternative.

    :py:mod:`~PIL.ImageMath` only supports single-layer images. To process multi-band
    images, use the :py:meth:`~PIL.Image.Image.split` method or
    :py:func:`~PIL.Image.merge` function.

    :param expression: A string containing a Python-style expression.
    :param **kw: Values to add to the evaluation context.
    :return: The evaluated expression. This is usually an image object, but can
             also be an integer, a floating point value, or a pixel tuple,
             depending on the expression.
    """
    pass
# WARNING: Decompyle incomplete
