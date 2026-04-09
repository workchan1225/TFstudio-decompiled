# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: defmatrix.pyc (Python 3.11)

__all__ = [
    'matrix',
    'bmat',
    'mat',
    'asmatrix']
import sys
import warnings
import ast
from _utils import set_module

numeric
from numpy.core.numeric import concatenate, isscalar
isscalar = isscalar
import numpy.core.numeric, core
from numpy.linalg import matrix_power

def _convert_from_string(data):
    for char in '[]':
        data = data.replace(char, '')
        rows = data.split(';')
        newdata = []
        count = 0
        for row in rows:
            trow = row.split(',')
            newrow = []
            for col in trow:
                temp = col.split()
                newrow.extend(map(ast.literal_eval, temp))
                if count == 0:
                    Ncols = len(newrow)
                elif len(newrow) != Ncols:
                    raise ValueError('Rows not the same size.')
            count += 1
            newdata.append(newrow)
            return newdata

asmatrix = (lambda data, dtype = (None,): matrix(data, dtype = dtype, copy = False))()
matrix = <NODE:12>()

def _from_string(str, gdict, ldict):
    rows = str.split(';')
    rowtup = []
    for row in rows:
        trow = row.split(',')
        newrow = []
        for x in trow:
            newrow.extend(x.split())
            trow = newrow
            coltup = []
            for col in trow:
                col = col.strip()
                thismat = ldict[col]
            except KeyError:
                thismat = gdict[col]
            except KeyError:
                e = None
                raise NameError(f'''name {col!r} is not defined'''), None
                e = None
                del e
        coltup.append(thismat)
        rowtup.append(concatenate(coltup, axis = -1))
        return concatenate(rowtup, axis = 0)

bmat = (lambda obj, ldict, gdict = (None, None): pass# WARNING: Decompyle incomplete
)()
mat = asmatrix
