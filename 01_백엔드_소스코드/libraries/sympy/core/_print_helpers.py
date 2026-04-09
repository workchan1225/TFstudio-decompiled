# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _print_helpers.pyc (Python 3.11)

'''
Base class to provide str and repr hooks that `init_printing` can overwrite.

This is exposed publicly in the `printing.defaults` module,
but cannot be defined there without causing circular imports.
'''

class Printable:
    '''
    The default implementation of printing for SymPy classes.

    This implements a hack that allows us to print elements of built-in
    Python containers in a readable way. Natively Python uses ``repr()``
    even if ``str()`` was explicitly requested. Mix in this trait into
    a class to get proper default printing.

    This also adds support for LaTeX printing in jupyter notebooks.
    '''
    __slots__ = ()
    
    def __str__(self):
        sstr = sstr
        import sympy.printing.str
        return sstr(self, order = None)

    __repr__ = __str__
    
    def _repr_disabled(self):
        '''
        No-op repr function used to disable jupyter display hooks.

        When :func:`sympy.init_printing` is used to disable certain display
        formats, this function is copied into the appropriate ``_repr_*_``
        attributes.

        While we could just set the attributes to `None``, doing it this way
        allows derived classes to call `super()`.
        '''
        pass

    _repr_png_ = _repr_disabled
    _repr_svg_ = _repr_disabled
    
    def _repr_latex_(self):
        '''
        IPython/Jupyter LaTeX printing

        To change the behavior of this (e.g., pass in some settings to LaTeX),
        use init_printing(). init_printing() will also enable LaTeX printing
        for built in numeric types like ints and container types that contain
        SymPy objects, like lists and dictionaries of expressions.
        '''
        latex = latex
        import sympy.printing.latex
        s = latex(self, mode = 'plain')
        return '$\\displaystyle %s$' % s
