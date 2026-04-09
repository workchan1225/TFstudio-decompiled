# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: useful.pyc (Python 3.11)

import datetime
from pyasn1 import error
from pyasn1.type import char
from pyasn1.type import tag
from pyasn1.type import univ
__all__ = [
    'ObjectDescriptor',
    'GeneralizedTime',
    'UTCTime']
NoValue = univ.NoValue
noValue = univ.noValue

class ObjectDescriptor(char.GraphicString):
    __doc__ = char.GraphicString.__doc__
    tagSet = char.GraphicString.tagSet.tagImplicitly(tag.Tag(tag.tagClassUniversal, tag.tagFormatSimple, 7))
    typeId = char.GraphicString.getTypeId()


class TimeMixIn(object):
    _yearsDigits = 4
    _hasSubsecond = False
    _optionalMinutes = False
    _shortTZ = False
    
    class FixedOffset(datetime.tzinfo):
        '''Fixed offset in minutes east from UTC.'''
        
        def __init__(self, offset, name = (0, 'UTC')):
            self._FixedOffset__offset = datetime.timedelta(minutes = offset)
            self._FixedOffset__name = name

        
        def utcoffset(self, dt):
            return self._FixedOffset__offset

        
        def tzname(self, dt):
            return self._FixedOffset__name

        
        def dst(self, dt):
            return datetime.timedelta(0)


    UTC = FixedOffset()
    asDateTime = (lambda self: text = str(self)if text.endswith('Z'):
tzinfo = TimeMixIn.UTCtext = text[:-1]elif '-' in text or '+' in text:
if '+' in text:
(text, plusminus, tz) = text.partition('+')else:
(text, plusminus, tz) = text.partition('-')if self._shortTZ and len(tz) == 2:
tz += '00'if len(tz) != 4:
raise error.PyAsn1Error('malformed time zone offset %s' % tz)try:
minutes = int(tz[:2]) * 60 + int(tz[2:])tzinfo = TimeMixIn.FixedOffset(minutes, '?')else:
tzinfo = Noneif '.' in text or ',' in text:
try:
ms = int(ms) * 1000except ValueError:
raise error.PyAsn1Error('bad sub-second time specification %s' % self)ms = 0if self._optionalMinutes and len(text) - self._yearsDigits == 6:
text += '0000'elif len(text) - self._yearsDigits == 8:
text += '00'try:
if self._yearsDigits == 4:
passdt.replace(microsecond = ms, tzinfo = tzinfo))()
    fromDateTime = (lambda cls, dt: if cls._yearsDigits == 4:
if not '%Y%m%d%H%M%S':
text = dt.strftime('%y%m%d%H%M%S')if cls._hasSubsecond:
text += '.%d' % dt.microsecond // 1000if dt.utcoffset():
seconds = dt.utcoffset().secondsif seconds < 0:
text += '-'else:
text += '+'text += '%.2d%.2d' % (seconds // 3600, seconds % 3600)else:
text += 'Z'cls(text))()


class GeneralizedTime(TimeMixIn, char.VisibleString):
    __doc__ = char.VisibleString.__doc__
    tagSet = char.VisibleString.tagSet.tagImplicitly(tag.Tag(tag.tagClassUniversal, tag.tagFormatSimple, 24))
    typeId = char.VideotexString.getTypeId()
    _yearsDigits = 4
    _hasSubsecond = True
    _optionalMinutes = True
    _shortTZ = True


class UTCTime(TimeMixIn, char.VisibleString):
    __doc__ = char.VisibleString.__doc__
    tagSet = char.VisibleString.tagSet.tagImplicitly(tag.Tag(tag.tagClassUniversal, tag.tagFormatSimple, 23))
    typeId = char.VideotexString.getTypeId()
    _yearsDigits = 2
    _hasSubsecond = False
    _optionalMinutes = False
    _shortTZ = False
