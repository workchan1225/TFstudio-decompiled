# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: univ.pyc (Python 3.11)

import math
import sys
from pyasn1 import error
from pyasn1.codec.ber import eoo
from pyasn1.compat import integer
from pyasn1.type import base
from pyasn1.type import constraint
from pyasn1.type import namedtype
from pyasn1.type import namedval
from pyasn1.type import tag
from pyasn1.type import tagmap
NoValue = base.NoValue
noValue = NoValue()
__all__ = [
    'Integer',
    'Boolean',
    'BitString',
    'OctetString',
    'Null',
    'ObjectIdentifier',
    'Real',
    'Enumerated',
    'SequenceOfAndSetOfBase',
    'SequenceOf',
    'SetOf',
    'SequenceAndSetBase',
    'Sequence',
    'Set',
    'Choice',
    'Any',
    'NoValue',
    'noValue']

class Integer(base.SimpleAsn1Type):
    """Create |ASN.1| schema or value object.

    |ASN.1| class is based on :class:`~pyasn1.type.base.SimpleAsn1Type`, its
    objects are immutable and duck-type Python :class:`int` objects.

    Keyword Args
    ------------
    value: :class:`int`, :class:`str` or |ASN.1| object
        Python :class:`int` or :class:`str` literal or |ASN.1| class
        instance. If `value` is not given, schema object will be created.

    tagSet: :py:class:`~pyasn1.type.tag.TagSet`
        Object representing non-default ASN.1 tag(s)

    subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
        Object representing non-default ASN.1 subtype constraint(s). Constraints
        verification for |ASN.1| type occurs automatically on object
        instantiation.

    namedValues: :py:class:`~pyasn1.type.namedval.NamedValues`
        Object representing non-default symbolic aliases for numbers

    Raises
    ------
    ~pyasn1.error.ValueConstraintError, ~pyasn1.error.PyAsn1Error
        On constraint violation or bad initializer.

    Examples
    --------

    .. code-block:: python

        class ErrorCode(Integer):
            '''
            ASN.1 specification:

            ErrorCode ::=
                INTEGER { disk-full(1), no-disk(-1),
                          disk-not-formatted(2) }

            error ErrorCode ::= disk-full
            '''
            namedValues = NamedValues(
                ('disk-full', 1), ('no-disk', -1),
                ('disk-not-formatted', 2)
            )

        error = ErrorCode('disk-full')
    """
    tagSet = tag.initTagSet(tag.Tag(tag.tagClassUniversal, tag.tagFormatSimple, 2))
    subtypeSpec = constraint.ConstraintsIntersection()
    namedValues = namedval.NamedValues()
    typeId = base.SimpleAsn1Type.getTypeId()
    
    def __init__(self, value = (noValue,), **kwargs):
        if 'namedValues' not in kwargs:
            kwargs['namedValues'] = self.namedValues
    # WARNING: Decompyle incomplete

    
    def __and__(self, value):
        return self.clone(self._value & value)

    
    def __rand__(self, value):
        return self.clone(value & self._value)

    
    def __or__(self, value):
        return self.clone(self._value | value)

    
    def __ror__(self, value):
        return self.clone(value | self._value)

    
    def __xor__(self, value):
        return self.clone(self._value ^ value)

    
    def __rxor__(self, value):
        return self.clone(value ^ self._value)

    
    def __lshift__(self, value):
        return self.clone(self._value << value)

    
    def __rshift__(self, value):
        return self.clone(self._value >> value)

    
    def __add__(self, value):
        return self.clone(self._value + value)

    
    def __radd__(self, value):
        return self.clone(value + self._value)

    
    def __sub__(self, value):
        return self.clone(self._value - value)

    
    def __rsub__(self, value):
        return self.clone(value - self._value)

    
    def __mul__(self, value):
        return self.clone(self._value * value)

    
    def __rmul__(self, value):
        return self.clone(value * self._value)

    
    def __mod__(self, value):
        return self.clone(self._value % value)

    
    def __rmod__(self, value):
        return self.clone(value % self._value)

    
    def __pow__(self, value, modulo = (None,)):
        return self.clone(pow(self._value, value, modulo))

    
    def __rpow__(self, value):
        return self.clone(pow(value, self._value))

    
    def __floordiv__(self, value):
        return self.clone(self._value // value)

    
    def __rfloordiv__(self, value):
        return self.clone(value // self._value)

    
    def __truediv__(self, value):
        return Real(self._value / value)

    
    def __rtruediv__(self, value):
        return Real(value / self._value)

    
    def __divmod__(self, value):
        return self.clone(divmod(self._value, value))

    
    def __rdivmod__(self, value):
        return self.clone(divmod(value, self._value))

    __hash__ = base.SimpleAsn1Type.__hash__
    
    def __int__(self):
        return int(self._value)

    
    def __float__(self):
        return float(self._value)

    
    def __abs__(self):
        return self.clone(abs(self._value))

    
    def __index__(self):
        return int(self._value)

    
    def __pos__(self):
        return self.clone(+(self._value))

    
    def __neg__(self):
        return self.clone(-(self._value))

    
    def __invert__(self):
        return self.clone(~(self._value))

    
    def __round__(self, n = (0,)):
        r = round(self._value, n)
        if n:
            return self.clone(r)

    
    def __floor__(self):
        return math.floor(self._value)

    
    def __ceil__(self):
        return math.ceil(self._value)

    
    def __trunc__(self):
        return self.clone(math.trunc(self._value))

    
    def __lt__(self, value):
        return self._value < value

    
    def __le__(self, value):
        return self._value <= value

    
    def __eq__(self, value):
        return self._value == value

    
    def __ne__(self, value):
        return self._value != value

    
    def __gt__(self, value):
        return self._value > value

    
    def __ge__(self, value):
        return self._value >= value

    
    def prettyIn(self, value):
        
        try:
            return int(value)
        except ValueError:
            return 
            except KeyError:
                raise error.PyAsn1Error(f'''Can\'t coerce {value!r} into integer: {exc!s}''')
                None = None
                del exc


    
    def prettyOut(self, value):
        
        try:
            return str(self.namedValues[value])
        except KeyError:
            return 


    
    def getNamedValues(self):
        return self.namedValues



class Boolean(Integer):
    """Create |ASN.1| schema or value object.

    |ASN.1| class is based on :class:`~pyasn1.type.base.SimpleAsn1Type`, its
    objects are immutable and duck-type Python :class:`int` objects.

    Keyword Args
    ------------
    value: :class:`int`, :class:`str` or |ASN.1| object
        Python :class:`int` or :class:`str` literal or |ASN.1| class
        instance. If `value` is not given, schema object will be created.

    tagSet: :py:class:`~pyasn1.type.tag.TagSet`
        Object representing non-default ASN.1 tag(s)

    subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
        Object representing non-default ASN.1 subtype constraint(s).Constraints
        verification for |ASN.1| type occurs automatically on object
        instantiation.

    namedValues: :py:class:`~pyasn1.type.namedval.NamedValues`
        Object representing non-default symbolic aliases for numbers

    Raises
    ------
    ~pyasn1.error.ValueConstraintError, ~pyasn1.error.PyAsn1Error
        On constraint violation or bad initializer.

    Examples
    --------
    .. code-block:: python

        class RoundResult(Boolean):
            '''
            ASN.1 specification:

            RoundResult ::= BOOLEAN

            ok RoundResult ::= TRUE
            ko RoundResult ::= FALSE
            '''
        ok = RoundResult(True)
        ko = RoundResult(False)
    """
    tagSet = tag.initTagSet(tag.Tag(tag.tagClassUniversal, tag.tagFormatSimple, 1))
    subtypeSpec = Integer.subtypeSpec + constraint.SingleValueConstraint(0, 1)
    namedValues = namedval.NamedValues(('False', 0), ('True', 1))
    typeId = Integer.getTypeId()


class SizedInteger(int):
    bitLength = None
    leadingZeroBits = None
    
    def setBitLength(self, bitLength):
        self.bitLength = bitLength
        self.leadingZeroBits = max(bitLength - self.bit_length(), 0)
        return self

    
    def __len__(self):
        pass
    # WARNING: Decompyle incomplete



class BitString(base.SimpleAsn1Type):
    """Create |ASN.1| schema or value object.

    |ASN.1| class is based on :class:`~pyasn1.type.base.SimpleAsn1Type`, its
    objects are immutable and duck-type both Python :class:`tuple` (as a tuple
    of bits) and :class:`int` objects.

    Keyword Args
    ------------
    value: :class:`int`, :class:`str` or |ASN.1| object
        Python :class:`int` or :class:`str` literal representing binary
        or hexadecimal number or sequence of integer bits or |ASN.1| object.
        If `value` is not given, schema object will be created.

    tagSet: :py:class:`~pyasn1.type.tag.TagSet`
        Object representing non-default ASN.1 tag(s)

    subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
        Object representing non-default ASN.1 subtype constraint(s). Constraints
        verification for |ASN.1| type occurs automatically on object
        instantiation.

    namedValues: :py:class:`~pyasn1.type.namedval.NamedValues`
        Object representing non-default symbolic aliases for numbers

    binValue: :py:class:`str`
        Binary string initializer to use instead of the *value*.
        Example: '10110011'.

    hexValue: :py:class:`str`
        Hexadecimal string initializer to use instead of the *value*.
        Example: 'DEADBEEF'.

    Raises
    ------
    ~pyasn1.error.ValueConstraintError, ~pyasn1.error.PyAsn1Error
        On constraint violation or bad initializer.

    Examples
    --------
    .. code-block:: python

        class Rights(BitString):
            '''
            ASN.1 specification:

            Rights ::= BIT STRING { user-read(0), user-write(1),
                                    group-read(2), group-write(3),
                                    other-read(4), other-write(5) }

            group1 Rights ::= { group-read, group-write }
            group2 Rights ::= '0011'B
            group3 Rights ::= '3'H
            '''
            namedValues = NamedValues(
                ('user-read', 0), ('user-write', 1),
                ('group-read', 2), ('group-write', 3),
                ('other-read', 4), ('other-write', 5)
            )

        group1 = Rights(('group-read', 'group-write'))
        group2 = Rights('0011')
        group3 = Rights(0x3)
    """
    tagSet = tag.initTagSet(tag.Tag(tag.tagClassUniversal, tag.tagFormatSimple, 3))
    subtypeSpec = constraint.ConstraintsIntersection()
    namedValues = namedval.NamedValues()
    typeId = base.SimpleAsn1Type.getTypeId()
    defaultBinValue = noValue
    defaultHexValue = noValue
    
    def __init__(self, value = (noValue,), **kwargs):
        if value is noValue and kwargs:
            
            try:
                value = self.fromBinaryString(kwargs.pop('binValue'), internalFormat = True)
            except KeyError:
                pass

            
            try:
                value = self.fromHexString(kwargs.pop('hexValue'), internalFormat = True)
            except KeyError:
                pass

            if value is noValue:
                if self.defaultBinValue is not noValue:
                    value = self.fromBinaryString(self.defaultBinValue, internalFormat = True)
                elif self.defaultHexValue is not noValue:
                    value = self.fromHexString(self.defaultHexValue, internalFormat = True)
        if 'namedValues' not in kwargs:
            kwargs['namedValues'] = self.namedValues
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        return self.asBinary()

    
    def __eq__(self, other):
