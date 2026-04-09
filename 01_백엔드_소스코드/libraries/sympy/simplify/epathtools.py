# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: epathtools.pyc (Python 3.11)

'''Tools for manipulation of expressions using paths. '''
from sympy.core import Basic

class EPath:
    '''
    Manipulate expressions using paths.

    EPath grammar in EBNF notation::

        literal   ::= /[A-Za-z_][A-Za-z_0-9]*/
        number    ::= /-?\\d+/
        type      ::= literal
        attribute ::= literal "?"
        all       ::= "*"
        slice     ::= "[" number? (":" number? (":" number?)?)? "]"
        range     ::= all | slice
        query     ::= (type | attribute) ("|" (type | attribute))*
        selector  ::= range | query range?
        path      ::= "/" selector ("/" selector)*

    See the docstring of the epath() function.

    '''
    __slots__ = ('_path', '_epath')
    
    def __new__(cls, path):
        '''Construct new EPath. '''
        if isinstance(path, EPath):
            return path
        if not None:
            raise ValueError('empty EPath')
        _path = path
        if path[0] == '/':
            path = path[1:]
        else:
            raise NotImplementedError('non-root EPath')
        epath = []
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return f'''{self.__class__.__name__!s}({self._path!r})'''

    
    def _get_ordered_args(self, expr):
        '''Sort ``expr.args`` using printing order. '''
        if expr.is_Add:
            return expr.as_ordered_terms()
        if None.is_Mul:
            return expr.as_ordered_factors()
        return None.args

    
    def _hasattrs(self, expr, attrs):
        '''Check if ``expr`` has any of ``attrs``. '''
        for attr in attrs:
            if not hasattr(expr, attr):
                return False
            return True

    
    def _hastypes(self, expr, types):
        '''Check if ``expr`` is any of ``types``. '''
        _types = expr.__class__.mro()()
        return bool(set(_types).intersection(types))

    
    def _has(self, expr, attrs, types):
        '''Apply ``_hasattrs`` and ``_hastypes`` to ``expr``. '''
        if not attrs and types:
            return True
        if None and self._hasattrs(expr, attrs):
            return True
        if None and self._hastypes(expr, types):
            return True

    
    def apply(self, expr, func, args, kwargs = (None, None)):
        '''
        Modify parts of an expression selected by a path.

        Examples
        ========

        >>> from sympy.simplify.epathtools import EPath
        >>> from sympy import sin, cos, E
        >>> from sympy.abc import x, y, z, t

        >>> path = EPath("/*/[0]/Symbol")
        >>> expr = [((x, 1), 2), ((3, y), z)]

        >>> path.apply(expr, lambda expr: expr**2)
        [((x**2, 1), 2), ((3, y**2), z)]

        >>> path = EPath("/*/*/Symbol")
        >>> expr = t + sin(x + 1) + cos(x + y + E)

        >>> path.apply(expr, lambda expr: 2*expr)
        t + sin(2*x + 1) + cos(2*x + 2*y + E)

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def select(self, expr):
        '''
        Retrieve parts of an expression selected by a path.

        Examples
        ========

        >>> from sympy.simplify.epathtools import EPath
        >>> from sympy import sin, cos, E
        >>> from sympy.abc import x, y, z, t

        >>> path = EPath("/*/[0]/Symbol")
        >>> expr = [((x, 1), 2), ((3, y), z)]

        >>> path.select(expr)
        [x, y]

        >>> path = EPath("/*/*/Symbol")
        >>> expr = t + sin(x + 1) + cos(x + y + E)

        >>> path.select(expr)
        [x, x, y]

        '''
        pass
    # WARNING: Decompyle incomplete



def epath(path, expr, func, args, kwargs = (None, None, None, None)):
    '''
    Manipulate parts of an expression selected by a path.

    Explanation
    ===========

    This function allows to manipulate large nested expressions in single
    line of code, utilizing techniques to those applied in XML processing
    standards (e.g. XPath).

    If ``func`` is ``None``, :func:`epath` retrieves elements selected by
    the ``path``. Otherwise it applies ``func`` to each matching element.

    Note that it is more efficient to create an EPath object and use the select
    and apply methods of that object, since this will compile the path string
    only once.  This function should only be used as a convenient shortcut for
    interactive use.

    This is the supported syntax:

    * select all: ``/*``
          Equivalent of ``for arg in args:``.
    * select slice: ``/[0]`` or ``/[1:5]`` or ``/[1:5:2]``
          Supports standard Python\'s slice syntax.
    * select by type: ``/list`` or ``/list|tuple``
          Emulates ``isinstance()``.
    * select by attribute: ``/__iter__?``
          Emulates ``hasattr()``.

    Parameters
    ==========

    path : str | EPath
        A path as a string or a compiled EPath.
    expr : Basic | iterable
        An expression or a container of expressions.
    func : callable (optional)
        A callable that will be applied to matching parts.
    args : tuple (optional)
        Additional positional arguments to ``func``.
    kwargs : dict (optional)
        Additional keyword arguments to ``func``.

    Examples
    ========

    >>> from sympy.simplify.epathtools import epath
    >>> from sympy import sin, cos, E
    >>> from sympy.abc import x, y, z, t

    >>> path = "/*/[0]/Symbol"
    >>> expr = [((x, 1), 2), ((3, y), z)]

    >>> epath(path, expr)
    [x, y]
    >>> epath(path, expr, lambda expr: expr**2)
    [((x**2, 1), 2), ((3, y**2), z)]

    >>> path = "/*/*/Symbol"
    >>> expr = t + sin(x + 1) + cos(x + y + E)

    >>> epath(path, expr)
    [x, x, y]
    >>> epath(path, expr, lambda expr: 2*expr)
    t + sin(2*x + 1) + cos(2*x + 2*y + E)

    '''
    _epath = EPath(path)
# WARNING: Decompyle incomplete
