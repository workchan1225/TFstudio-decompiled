# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: matrices.pyc (Python 3.11)

from libmp.backend import xrange
import warnings
rowsep = '\n'
colsep = '  '

class _matrix(object):
    '''
    Numerical matrix.

    Specify the dimensions or the data as a nested list.
    Elements default to zero.
    Use a flat list to create a column vector easily.

    The datatype of the context (mpf for mp, mpi for iv, and float for fp) is used to store the data.

    Creating matrices
    -----------------

    Matrices in mpmath are implemented using dictionaries. Only non-zero values
    are stored, so it is cheap to represent sparse matrices.

    The most basic way to create one is to use the ``matrix`` class directly.
    You can create an empty matrix specifying the dimensions:

        >>> from mpmath import *
        >>> mp.dps = 15
        >>> matrix(2)
        matrix(
        [[\'0.0\', \'0.0\'],
         [\'0.0\', \'0.0\']])
        >>> matrix(2, 3)
        matrix(
        [[\'0.0\', \'0.0\', \'0.0\'],
         [\'0.0\', \'0.0\', \'0.0\']])

    Calling ``matrix`` with one dimension will create a square matrix.

    To access the dimensions of a matrix, use the ``rows`` or ``cols`` keyword:

        >>> A = matrix(3, 2)
        >>> A
        matrix(
        [[\'0.0\', \'0.0\'],
         [\'0.0\', \'0.0\'],
         [\'0.0\', \'0.0\']])
        >>> A.rows
        3
        >>> A.cols
        2

    You can also change the dimension of an existing matrix. This will set the
    new elements to 0. If the new dimension is smaller than before, the
    concerning elements are discarded:

        >>> A.rows = 2
        >>> A
        matrix(
        [[\'0.0\', \'0.0\'],
         [\'0.0\', \'0.0\']])

    Internally ``mpmathify`` is used every time an element is set. This
    is done using the syntax A[row,column], counting from 0:

        >>> A = matrix(2)
        >>> A[1,1] = 1 + 1j
        >>> A
        matrix(
        [[\'0.0\', \'0.0\'],
         [\'0.0\', mpc(real=\'1.0\', imag=\'1.0\')]])

    A more comfortable way to create a matrix lets you use nested lists:

        >>> matrix([[1, 2], [3, 4]])
        matrix(
        [[\'1.0\', \'2.0\'],
         [\'3.0\', \'4.0\']])

    Convenient advanced functions are available for creating various standard
    matrices, see ``zeros``, ``ones``, ``diag``, ``eye``, ``randmatrix`` and
    ``hilbert``.

    Vectors
    .......

    Vectors may also be represented by the ``matrix`` class (with rows = 1 or cols = 1).
    For vectors there are some things which make life easier. A column vector can
    be created using a flat list, a row vectors using an almost flat nested list::

        >>> matrix([1, 2, 3])
        matrix(
        [[\'1.0\'],
         [\'2.0\'],
         [\'3.0\']])
        >>> matrix([[1, 2, 3]])
        matrix(
        [[\'1.0\', \'2.0\', \'3.0\']])

    Optionally vectors can be accessed like lists, using only a single index::

        >>> x = matrix([1, 2, 3])
        >>> x[1]
        mpf(\'2.0\')
        >>> x[1,0]
        mpf(\'2.0\')

    Other
    .....

    Like you probably expected, matrices can be printed::

        >>> print randmatrix(3) # doctest:+SKIP
        [ 0.782963853573023  0.802057689719883  0.427895717335467]
        [0.0541876859348597  0.708243266653103  0.615134039977379]
        [ 0.856151514955773  0.544759264818486  0.686210904770947]

    Use ``nstr`` or ``nprint`` to specify the number of digits to print::

        >>> nprint(randmatrix(5), 3) # doctest:+SKIP
        [2.07e-1  1.66e-1  5.06e-1  1.89e-1  8.29e-1]
        [6.62e-1  6.55e-1  4.47e-1  4.82e-1  2.06e-2]
        [4.33e-1  7.75e-1  6.93e-2  2.86e-1  5.71e-1]
        [1.01e-1  2.53e-1  6.13e-1  3.32e-1  2.59e-1]
        [1.56e-1  7.27e-2  6.05e-1  6.67e-2  2.79e-1]

    As matrices are mutable, you will need to copy them sometimes::

        >>> A = matrix(2)
        >>> A
        matrix(
        [[\'0.0\', \'0.0\'],
         [\'0.0\', \'0.0\']])
        >>> B = A.copy()
        >>> B[0,0] = 1
        >>> B
        matrix(
        [[\'1.0\', \'0.0\'],
         [\'0.0\', \'0.0\']])
        >>> A
        matrix(
        [[\'0.0\', \'0.0\'],
         [\'0.0\', \'0.0\']])

    Finally, it is possible to convert a matrix to a nested list. This is very useful,
    as most Python libraries involving matrices or arrays (namely NumPy or SymPy)
    support this format::

        >>> B.tolist()
        [[mpf(\'1.0\'), mpf(\'0.0\')], [mpf(\'0.0\'), mpf(\'0.0\')]]


    Matrix operations
    -----------------

    You can add and subtract matrices of compatible dimensions::

        >>> A = matrix([[1, 2], [3, 4]])
        >>> B = matrix([[-2, 4], [5, 9]])
        >>> A + B
        matrix(
        [[\'-1.0\', \'6.0\'],
         [\'8.0\', \'13.0\']])
        >>> A - B
        matrix(
        [[\'3.0\', \'-2.0\'],
         [\'-2.0\', \'-5.0\']])
        >>> A + ones(3) # doctest:+ELLIPSIS
        Traceback (most recent call last):
          ...
        ValueError: incompatible dimensions for addition

    It is possible to multiply or add matrices and scalars. In the latter case the
    operation will be done element-wise::

        >>> A * 2
        matrix(
        [[\'2.0\', \'4.0\'],
         [\'6.0\', \'8.0\']])
        >>> A / 4
        matrix(
        [[\'0.25\', \'0.5\'],
         [\'0.75\', \'1.0\']])
        >>> A - 1
        matrix(
        [[\'0.0\', \'1.0\'],
         [\'2.0\', \'3.0\']])

    Of course you can perform matrix multiplication, if the dimensions are
    compatible, using ``@`` (for Python >= 3.5) or ``*``. For clarity, ``@`` is
    recommended (`PEP 465 <https://www.python.org/dev/peps/pep-0465/>`), because
    the meaning of ``*`` is different in many other Python libraries such as NumPy.

        >>> A @ B # doctest:+SKIP
        matrix(
        [[\'8.0\', \'22.0\'],
         [\'14.0\', \'48.0\']])
        >>> A * B # same as A @ B
        matrix(
        [[\'8.0\', \'22.0\'],
         [\'14.0\', \'48.0\']])
        >>> matrix([[1, 2, 3]]) * matrix([[-6], [7], [-2]])
        matrix(
        [[\'2.0\']])

    ..
        COMMENT: TODO: the above "doctest:+SKIP" may be removed as soon as we
        have dropped support for Python 3.5 and below.

    You can raise powers of square matrices::

        >>> A**2
        matrix(
        [[\'7.0\', \'10.0\'],
         [\'15.0\', \'22.0\']])

    Negative powers will calculate the inverse::

        >>> A**-1
        matrix(
        [[\'-2.0\', \'1.0\'],
         [\'1.5\', \'-0.5\']])
        >>> A * A**-1
        matrix(
        [[\'1.0\', \'1.0842021724855e-19\'],
         [\'-2.16840434497101e-19\', \'1.0\']])



    Matrix transposition is straightforward::

        >>> A = ones(2, 3)
        >>> A
        matrix(
        [[\'1.0\', \'1.0\', \'1.0\'],
         [\'1.0\', \'1.0\', \'1.0\']])
        >>> A.T
        matrix(
        [[\'1.0\', \'1.0\'],
         [\'1.0\', \'1.0\'],
         [\'1.0\', \'1.0\']])

    Norms
    .....

    Sometimes you need to know how "large" a matrix or vector is. Due to their
    multidimensional nature it\'s not possible to compare them, but there are
    several functions to map a matrix or a vector to a positive real number, the
    so called norms.

    For vectors the p-norm is intended, usually the 1-, the 2- and the oo-norm are
    used.

        >>> x = matrix([-10, 2, 100])
        >>> norm(x, 1)
        mpf(\'112.0\')
        >>> norm(x, 2)
        mpf(\'100.5186549850325\')
        >>> norm(x, inf)
        mpf(\'100.0\')

    Please note that the 2-norm is the most used one, though it is more expensive
    to calculate than the 1- or oo-norm.

    It is possible to generalize some vector norms to matrix norm::

        >>> A = matrix([[1, -1000], [100, 50]])
        >>> mnorm(A, 1)
        mpf(\'1050.0\')
        >>> mnorm(A, inf)
        mpf(\'1001.0\')
        >>> mnorm(A, \'F\')
        mpf(\'1006.2310867787777\')

    The last norm (the "Frobenius-norm") is an approximation for the 2-norm, which
    is hard to calculate and not available. The Frobenius-norm lacks some
    mathematical properties you might expect from a norm.
    '''
    
    def __init__(self, *args, **kwargs):
        self._matrix__data = { }
        self._LU = None
        if 'force_type' in kwargs:
            warnings.warn('The force_type argument was removed, it did not work properly anyway. If you want to force floating-point or interval computations, use the respective methods from `fp` or `mp` instead, e.g., `fp.matrix()` or `iv.matrix()`. If you want to truncate values to integer, use .apply(int) instead.')
        if isinstance(args[0], (list, tuple)):
            if isinstance(args[0][0], (list, tuple)):
                A = args[0]
                self._matrix__rows = len(A)
                self._matrix__cols = len(A[0])
                for i, row in enumerate(A):
                    for j, a in enumerate(row):
                        self[(i, j)] = a
                        return None
                        v = args[0]
                        self._matrix__rows = len(v)
                        self._matrix__cols = 1
                        for i, e in enumerate(v):
                            self[(i, 0)] = e
                            return None
                            if isinstance(args[0], int):
                                if len(args) == 1:
                                    self._matrix__rows = args[0]
                                    self._matrix__cols = args[0]
                                    return None
                                if not None(args[1], int):
                                    raise TypeError('expected int')
                                self._matrix__rows = args[0]
                                self._matrix__cols = args[1]
                                return None
                            if None(args[0], _matrix):
                                A = args[0]
                                self._matrix__rows = A._matrix__rows
                                self._matrix__cols = A._matrix__cols
                                for i in xrange(A._matrix__rows):
                                    for j in xrange(A._matrix__cols):
                                        self[(i, j)] = A[(i, j)]
                                        return None
                                        if hasattr(args[0], 'tolist'):
                                            A = self.ctx.matrix(args[0].tolist())
                                            self._matrix__data = A._matrix__data
                                            self._matrix__rows = A._matrix__rows
                                            self._matrix__cols = A._matrix__cols
                                            return None
                                        raise None('could not interpret given arguments')

    
    def apply(self, f):
        '''
        Return a copy of self with the function `f` applied elementwise.
        '''
        new = self.ctx.matrix(self._matrix__rows, self._matrix__cols)
        for i in xrange(self._matrix__rows):
            for j in xrange(self._matrix__cols):
                new[(i, j)] = f(self[(i, j)])
                return new

    
    def __nstr__(self, n = (None,), **kwargs):
        res = []
        maxlen = [
            0] * self.cols
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        return self.__nstr__()

    
    def _toliststr(self, avoid_type = (False,)):
        """
        Create a list string from a matrix.

        If avoid_type: avoid multiple 'mpf's.
        """
        typ = self.ctx.mpf
        s = '['
        for i in xrange(self._matrix__rows):
            s += '['
            for j in xrange(self._matrix__cols):
                if not avoid_type or isinstance(self[(i, j)], typ):
                    a = repr(self[(i, j)])
                else:
                    a = "'" + str(self[(i, j)]) + "'"
                s += a + ', '
                s = s[:-2]
                s += '],\n '
                s = s[:-3]
                s += ']'
                return s

    
    def tolist(self):
        '''
        Convert the matrix to a nested list.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        if self.ctx.pretty:
            return self.__str__()
        s = None
        s += self._toliststr(avoid_type = True) + ')'
        return s

    
    def _matrix__get_element(self, key):
        '''
        Fast extraction of the i,j element from the matrix
            This function is for private use only because is unsafe:
                1. Does not check on the value of key it expects key to be a integer tuple (i,j)
                2. Does not check bounds
        '''
        if key in self._matrix__data:
            return self._matrix__data[key]
        return None.ctx.zero

    
    def _matrix__set_element(self, key, value):
        '''
        Fast assignment of the i,j element in the matrix
            This function is unsafe:
                1. Does not check on the value of key it expects key to be a integer tuple (i,j)
                2. Does not check bounds
                3. Does not check the value type
                4. Does not reset the LU cache
        '''
        if value:
            self._matrix__data[key] = value
            return None
        if None in self._matrix__data:
            del self._matrix__data[key]
            return None

    
    def __getitem__(self, key):
        '''
            Getitem function for mp matrix class with slice index enabled
            it allows the following assingments
            scalar to a slice of the matrix
         B = A[:,2:6]
        '''
        if isinstance(key, int) or isinstance(key, slice):
            if self._matrix__rows == 1:
                key = (0, key)
            elif self._matrix__cols == 1:
                key = (key, 0)
            else:
                raise IndexError('insufficient indices for matrix')
    # WARNING: Decompyle incomplete

    
    def __setitem__(self, key, value):
        if isinstance(key, int) or isinstance(key, slice):
            if self._matrix__rows == 1:
                key = (0, key)
            elif self._matrix__cols == 1:
                key = (key, 0)
            else:
                raise IndexError('insufficient indices for matrix')
    # WARNING: Decompyle incomplete

    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __mul__(self, other):
        pass
    # WARNING: Decompyle incomplete

    
    def __matmul__(self, other):
        return self.__mul__(other)

    
    def __rmul__(self, other):
        if isinstance(other, self.ctx.matrix):
            raise TypeError('other should not be type of ctx.matrix')
        return self.__mul__(other)

    
    def __pow__(self, other):
        if not isinstance(other, int):
            raise ValueError('only integer exponents are supported')
        if not self._matrix__rows == self._matrix__cols:
            raise ValueError('only powers of square matrices are defined')
        n = other
        if n == 0:
            return self.ctx.eye(self._matrix__rows)
        if None < 0:
            n = -n
            neg = True
        else:
            neg = False
        i = n
        y = 1
        z = self.copy()
    # WARNING: Decompyle incomplete

    
    def __div__(self, other):
        pass
    # WARNING: Decompyle incomplete

    __truediv__ = __div__
    
    def __add__(self, other):
        if isinstance(other, self.ctx.matrix):
            if not self._matrix__rows == other._matrix__rows or self._matrix__cols == other._matrix__cols:
                raise ValueError('incompatible dimensions for addition')
            new = self.ctx.matrix(self._matrix__rows, self._matrix__cols)
            for i in xrange(self._matrix__rows):
                for j in xrange(self._matrix__cols):
                    new[(i, j)] = self[(i, j)] + other[(i, j)]
                    return new
                    new = self.ctx.matrix(self._matrix__rows, self._matrix__cols)
                    for i in xrange(self._matrix__rows):
                        for j in xrange(self._matrix__cols):
                            return new

    
    def __radd__(self, other):
        return self.__add__(other)

    
    def __sub__(self, other):
        if isinstance(other, self.ctx.matrix):
            if not self._matrix__rows == other._matrix__rows or self._matrix__cols == other._matrix__cols:
                raise ValueError('incompatible dimensions for subtraction')
        return self.__add__(other * -1)

    
    def __pos__(self):
        '''
        +M returns a copy of M, rounded to current working precision.
        '''
        return 1 * self

    
    def __neg__(self):
        return -1 * self

    
    def __rsub__(self, other):
        return -self + other

    
    def __eq__(self, other):
