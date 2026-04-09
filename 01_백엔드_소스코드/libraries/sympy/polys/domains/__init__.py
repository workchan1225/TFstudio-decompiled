# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Implementation of mathematical domains. '''
__all__ = [
    'Domain',
    'FiniteField',
    'IntegerRing',
    'RationalField',
    'RealField',
    'ComplexField',
    'AlgebraicField',
    'PolynomialRing',
    'FractionField',
    'ExpressionDomain',
    'PythonRational',
    'GF',
    'FF',
    'ZZ',
    'QQ',
    'ZZ_I',
    'QQ_I',
    'RR',
    'CC',
    'EX',
    'EXRAW']
from domain import Domain
from finitefield import FiniteField, FF, GF
from integerring import IntegerRing, ZZ
from rationalfield import RationalField, QQ
from algebraicfield import AlgebraicField
from gaussiandomains import ZZ_I, QQ_I
from realfield import RealField, RR
from complexfield import ComplexField, CC
from polynomialring import PolynomialRing
from fractionfield import FractionField
from expressiondomain import ExpressionDomain, EX
from expressionrawdomain import EXRAW
from pythonrational import PythonRational
from sympy.external.gmpy import GROUND_TYPES
from pythonfinitefield import PythonFiniteField
from gmpyfinitefield import GMPYFiniteField
from pythonintegerring import PythonIntegerRing
from gmpyintegerring import GMPYIntegerRing
from pythonrationalfield import PythonRationalField
from gmpyrationalfield import GMPYRationalField
FF_python = PythonFiniteField
FF_gmpy = GMPYFiniteField
ZZ_python = PythonIntegerRing
ZZ_gmpy = GMPYIntegerRing
QQ_python = PythonRationalField
QQ_gmpy = GMPYRationalField
__all__.extend(('PythonFiniteField', 'GMPYFiniteField', 'PythonIntegerRing', 'GMPYIntegerRing', 'PythonRational', 'GMPYRationalField', 'FF_python', 'FF_gmpy', 'ZZ_python', 'ZZ_gmpy', 'QQ_python', 'QQ_gmpy'))
