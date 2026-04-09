# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: multidimensional.pyc (Python 3.11)

'''
Provides functionality for multidimensional usage of scalar-functions.

Read the vectorize docstring for more details.
'''
from functools import wraps

def apply_on_element(f, args, kwargs, n):
    '''
    Returns a structure with the same dimension as the specified argument,
    where each basic element is replaced by the function f applied on it. All
    other arguments stay the same.
    '''
    pass
# WARNING: Decompyle incomplete


def iter_copy(structure):
    '''
    Returns a copy of an iterable object (also copying all embedded iterables).
    '''
    return structure()


def structure_copy(structure):
    '''
    Returns a copy of the given structure (numpy-array, list, iterable, ..).
    '''
    if hasattr(structure, 'copy'):
        return structure.copy()
    return None(structure)


class vectorize:
    """
    Generalizes a function taking scalars to accept multidimensional arguments.

    Examples
    ========

    >>> from sympy import vectorize, diff, sin, symbols, Function
    >>> x, y, z = symbols('x y z')
    >>> f, g, h = list(map(Function, 'fgh'))

    >>> @vectorize(0)
    ... def vsin(x):
    ...     return sin(x)

    >>> vsin([1, x, y])
    [sin(1), sin(x), sin(y)]

    >>> @vectorize(0, 1)
    ... def vdiff(f, y):
    ...     return diff(f, y)

    >>> vdiff([f(x, y, z), g(x, y, z), h(x, y, z)], [x, y, z])
    [[Derivative(f(x, y, z), x), Derivative(f(x, y, z), y), Derivative(f(x, y, z), z)], [Derivative(g(x, y, z), x), Derivative(g(x, y, z), y), Derivative(g(x, y, z), z)], [Derivative(h(x, y, z), x), Derivative(h(x, y, z), y), Derivative(h(x, y, z), z)]]
    """
    
    def __init__(self, *mdargs):
        '''
        The given numbers and strings characterize the arguments that will be
        treated as data structures, where the decorated function will be applied
        to every single element.
        If no argument is given, everything is treated multidimensional.
        '''
        for a in mdargs:
            if not isinstance(a, (int, str)):
                raise TypeError('a is of invalid type')
            self.mdargs = mdargs
            return None

    
    def __call__(self, f):
        '''
        Returns a wrapper for the one-dimensional function that can handle
        multidimensional arguments.
        '''
        pass
    # WARNING: Decompyle incomplete
