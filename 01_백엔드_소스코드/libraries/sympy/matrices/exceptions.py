# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

'''
Exceptions raised by the matrix module.
'''

class MatrixError(Exception):
    pass


class ShapeError(MatrixError, ValueError):
    '''Wrong matrix shape'''
    pass


class NonSquareMatrixError(ShapeError):
    pass


class NonInvertibleMatrixError(MatrixError, ValueError):
    '''The matrix in not invertible (division by multidimensional zero error).'''
    pass


class NonPositiveDefiniteMatrixError(MatrixError, ValueError):
    '''The matrix is not a positive-definite matrix.'''
    pass
