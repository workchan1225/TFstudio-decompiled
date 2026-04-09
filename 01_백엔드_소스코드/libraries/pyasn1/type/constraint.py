# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: constraint.pyc (Python 3.11)

import sys
from pyasn1.type import error
__all__ = [
    'SingleValueConstraint',
    'ContainedSubtypeConstraint',
    'ValueRangeConstraint',
    'ValueSizeConstraint',
    'PermittedAlphabetConstraint',
    'InnerTypeConstraint',
    'ConstraintsExclusion',
    'ConstraintsIntersection',
    'ConstraintsUnion']

class AbstractConstraint(object):
    
    def __init__(self, *values):
        self._valueMap = set()
        self._setValues(values)
        self._AbstractConstraint__hash = hash((self.__class__.__name__, self._values))

    
    def __call__(self, value, idx = (None,)):
        if not self._values:
            return None
        
        try:
            self._testValue(value, idx)
            return None
        except error.ValueConstraintError:
            exc = None
            raise error.ValueConstraintError(f'''{self!s} failed at: {exc!r}''')
            exc = None
            del exc


    
    def __repr__(self):
        representation = '%s object' % self.__class__.__name__
        if self._values:
            ', consts %s' += ', '.join % (lambda .0: [ repr(x) for x in .0 ])(self._values())
        return '<%s>' % representation

    
    def __eq__(self, other):
        if self is other:
            return True
        return None._values == other

    
    def __ne__(self, other):
        return self._values != other

    
    def __lt__(self, other):
        return self._values < other

    
    def __le__(self, other):
        return self._values <= other

    
    def __gt__(self, other):
        return self._values > other

    
    def __ge__(self, other):
        return self._values >= other

    
    def __bool__(self):
        return bool(self._values)

    
    def __hash__(self):
        return self._AbstractConstraint__hash

    
    def _setValues(self, values):
        self._values = values

    
    def _testValue(self, value, idx):
        raise error.ValueConstraintError(value)

    
    def getValueMap(self):
        return self._valueMap

    
    def isSuperTypeOf(self, otherConstraint):
        if not otherConstraint is self:
            if not not (self._values):
                if not otherConstraint == self:
                    pass
        return self in otherConstraint.getValueMap()

    
    def isSubTypeOf(self, otherConstraint):
