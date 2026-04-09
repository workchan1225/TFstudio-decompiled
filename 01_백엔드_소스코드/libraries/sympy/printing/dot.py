# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dot.pyc (Python 3.11)

from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.symbol import Symbol
from sympy.core.numbers import Integer, Rational, Float
from sympy.printing.repr import srepr
__all__ = [
    'dotprint']
default_styles = ((Basic, {
    'color': 'blue',
    'shape': 'ellipse' }), (Expr, {
    'color': 'black' }))
slotClasses = (Symbol, Integer, Rational, Float)

def purestr(x, with_args = (False,)):
    '''A string that follows ```obj = type(obj)(*obj.args)``` exactly.

    Parameters
    ==========

    with_args : boolean, optional
        If ``True``, there will be a second argument for the return
        value, which is a tuple containing ``purestr`` applied to each
        of the subnodes.

        If ``False``, there will not be a second argument for the
        return.

        Default is ``False``

    Examples
    ========

    >>> from sympy import Float, Symbol, MatrixSymbol
    >>> from sympy import Integer # noqa: F401
    >>> from sympy.core.symbol import Str # noqa: F401
    >>> from sympy.printing.dot import purestr

    Applying ``purestr`` for basic symbolic object:
    >>> code = purestr(Symbol(\'x\'))
    >>> code
    "Symbol(\'x\')"
    >>> eval(code) == Symbol(\'x\')
    True

    For basic numeric object:
    >>> purestr(Float(2))
    "Float(\'2.0\', precision=53)"

    For matrix symbol:
    >>> code = purestr(MatrixSymbol(\'x\', 2, 2))
    >>> code
    "MatrixSymbol(Str(\'x\'), Integer(2), Integer(2))"
    >>> eval(code) == MatrixSymbol(\'x\', 2, 2)
    True

    With ``with_args=True``:
    >>> purestr(Float(2), with_args=True)
    ("Float(\'2.0\', precision=53)", ())
    >>> purestr(MatrixSymbol(\'x\', 2, 2), with_args=True)
    ("MatrixSymbol(Str(\'x\'), Integer(2), Integer(2))",
     ("Str(\'x\')", \'Integer(2)\', \'Integer(2)\'))
    '''
    sargs = ()
    if not isinstance(x, Basic):
        rv = str(x)
    elif not x.args:
        rv = srepr(x)
    else:
        args = x.args
        sargs = tuple(map(purestr, args))
        rv = f'''{type(x).__name__!s}({', '.join(sargs)!s})'''
    if with_args:
        rv = (rv, sargs)
    return rv


def styleof(expr, styles = (default_styles,)):
    """ Merge style dictionaries in order

    Examples
    ========

    >>> from sympy import Symbol, Basic, Expr, S
    >>> from sympy.printing.dot import styleof
    >>> styles = [(Basic, {'color': 'blue', 'shape': 'ellipse'}),
    ...           (Expr,  {'color': 'black'})]

    >>> styleof(Basic(S(1)), styles)
    {'color': 'blue', 'shape': 'ellipse'}

    >>> x = Symbol('x')
    >>> styleof(x + 1, styles)  # this is an Expr
    {'color': 'black', 'shape': 'ellipse'}
    """
    style = { }
    for typ, sty in styles:
        if isinstance(expr, typ):
            style.update(sty)
        return style


def attrprint(d, delimiter = (', ',)):
    ''' Print a dictionary of attributes

    Examples
    ========

    >>> from sympy.printing.dot import attrprint
    >>> print(attrprint({\'color\': \'blue\', \'shape\': \'ellipse\'}))
    "color"="blue", "shape"="ellipse"
    '''
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(sorted(d.items())())


def dotnode(expr, styles, labelfunc, pos, repeat = (default_styles, str, (), True)):
    ''' String defining a node

    Examples
    ========

    >>> from sympy.printing.dot import dotnode
    >>> from sympy.abc import x
    >>> print(dotnode(x))
    "Symbol(\'x\')_()" ["color"="black", "label"="x", "shape"="ellipse"];
    '''
    style = styleof(expr, styles)
    if not isinstance(expr, Basic) and expr.is_Atom:
        label = str(expr.__class__.__name__)
    else:
        label = labelfunc(expr)
    style['label'] = label
    expr_str = purestr(expr)
    if repeat:
        expr_str += '_%s' % str(pos)
    return f'''"{expr_str!s}" [{attrprint(style)!s}];'''


def dotedges(expr, atom, pos, repeat = ((lambda x: not isinstance(x, Basic)), (), True)):
    ''' List of strings for all expr->expr.arg pairs

    See the docstring of dotprint for explanations of the options.

    Examples
    ========

    >>> from sympy.printing.dot import dotedges
    >>> from sympy.abc import x
    >>> for e in dotedges(x+2):
    ...     print(e)
    "Add(Integer(2), Symbol(\'x\'))_()" -> "Integer(2)_(0,)";
    "Add(Integer(2), Symbol(\'x\'))_()" -> "Symbol(\'x\')_(1,)";
    '''
    pass
# WARNING: Decompyle incomplete

template = 'digraph{\n\n# Graph style\n%(graphstyle)s\n\n#########\n# Nodes #\n#########\n\n%(nodes)s\n\n#########\n# Edges #\n#########\n\n%(edges)s\n}'
_graphstyle = {
    'rankdir': 'TD',
    'ordering': 'out' }

def dotprint(expr, styles, atom, maxdepth, repeat, labelfunc = (default_styles, (lambda x: not isinstance(x, Basic)), None, True, str), **kwargs):
    '''DOT description of a SymPy expression tree

    Parameters
    ==========

    styles : list of lists composed of (Class, mapping), optional
        Styles for different classes.

        The default is

        .. code-block:: python

            (
                (Basic, {\'color\': \'blue\', \'shape\': \'ellipse\'}),
                (Expr,  {\'color\': \'black\'})
            )

    atom : function, optional
        Function used to determine if an arg is an atom.

        A good choice is ``lambda x: not x.args``.

        The default is ``lambda x: not isinstance(x, Basic)``.

    maxdepth : integer, optional
        The maximum depth.

        The default is ``None``, meaning no limit.

    repeat : boolean, optional
        Whether to use different nodes for common subexpressions.

        The default is ``True``.

        For example, for ``x + x*y`` with ``repeat=True``, it will have
        two nodes for ``x``; with ``repeat=False``, it will have one
        node.

        .. warning::
            Even if a node appears twice in the same object like ``x`` in
            ``Pow(x, x)``, it will still only appear once.
            Hence, with ``repeat=False``, the number of arrows out of an
            object might not equal the number of args it has.

    labelfunc : function, optional
        A function to create a label for a given leaf node.

        The default is ``str``.

        Another good option is ``srepr``.

        For example with ``str``, the leaf nodes of ``x + 1`` are labeled,
        ``x`` and ``1``.  With ``srepr``, they are labeled ``Symbol(\'x\')``
        and ``Integer(1)``.

    **kwargs : optional
        Additional keyword arguments are included as styles for the graph.

    Examples
    ========

    >>> from sympy import dotprint
    >>> from sympy.abc import x
    >>> print(dotprint(x+2)) # doctest: +NORMALIZE_WHITESPACE
    digraph{
    <BLANKLINE>
    # Graph style
    "ordering"="out"
    "rankdir"="TD"
    <BLANKLINE>
    #########
    # Nodes #
    #########
    <BLANKLINE>
    "Add(Integer(2), Symbol(\'x\'))_()" ["color"="black", "label"="Add", "shape"="ellipse"];
    "Integer(2)_(0,)" ["color"="black", "label"="2", "shape"="ellipse"];
    "Symbol(\'x\')_(1,)" ["color"="black", "label"="x", "shape"="ellipse"];
    <BLANKLINE>
    #########
    # Edges #
    #########
    <BLANKLINE>
    "Add(Integer(2), Symbol(\'x\'))_()" -> "Integer(2)_(0,)";
    "Add(Integer(2), Symbol(\'x\'))_()" -> "Symbol(\'x\')_(1,)";
    }

    '''
    pass
# WARNING: Decompyle incomplete
