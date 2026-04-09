# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: series_class.pyc (Python 3.11)

'''
Contains the base class for series
Made using sequences in mind
'''
from sympy.core.expr import Expr
from sympy.core.singleton import S
from sympy.core.cache import cacheit

class SeriesBase(Expr):
    '''Base Class for series'''
    interval = (lambda self: raise NotImplementedError('(%s).interval' % self))()
    start = (lambda self: raise NotImplementedError('(%s).start' % self))()
    stop = (lambda self: raise NotImplementedError('(%s).stop' % self))()
    length = (lambda self: raise NotImplementedError('(%s).length' % self))()
    variables = (lambda self: ())()
    free_symbols = (lambda self: self.args().difference(self.variables))()
    term = (lambda self, pt: if pt < self.start or pt > self.stop:
raise IndexError(f'''Index {pt!s} out of bounds {self.interval!s}''')self._eval_term(pt))()
    
    def _eval_term(self, pt):
        raise NotImplementedError("The _eval_term method should be added to%s to return series term so it is availablewhen 'term' calls it." % self.func)

    
    def _ith_point(self, i):
        """
        Returns the i'th point of a series
        If start point is negative infinity, point is returned from the end.
        Assumes the first point to be indexed zero.

        Examples
        ========

        TODO
        """
        if self.start is S.NegativeInfinity:
            initial = self.stop
            step = -1
        else:
            initial = self.start
            step = 1
        return initial + i * step

    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __getitem__(self, index):
        pass
    # WARNING: Decompyle incomplete
