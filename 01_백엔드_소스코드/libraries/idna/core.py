# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: core.pyc (Python 3.11)

import bisect
import re
import unicodedata
from typing import Optional, Union
from  import idnadata
from intranges import intranges_contain
_virama_combining_class = 9
_alabel_prefix = b'xn--'
_unicode_dots_re = re.compile('[.。．｡]')

class IDNAError(UnicodeError):
    '''Base exception for all IDNA-encoding related problems'''
    pass


class IDNABidiError(IDNAError):
    '''Exception when bidirectional requirements are not satisfied'''
    pass


class InvalidCodepoint(IDNAError):
    '''Exception when a disallowed or unallocated codepoint is used'''
    pass


class InvalidCodepointContext(IDNAError):
    '''Exception when the codepoint is not valid in the context it is used'''
    pass


def _combining_class(cp = None):
    v = unicodedata.combining(chr(cp))
    if not v == 0 and unicodedata.name(chr(cp)):
        raise ValueError('Unknown character in unicodedata')
    return v


def _is_script(cp = None, script = None):
    return intranges_contain(ord(cp), idnadata.scripts[script])


def _punycode(s = None):
    return s.encode('punycode')


def _unot(s = None):
    return 'U+{:04X}'.format(s)


def valid_label_length(label = None):
    if len(label) > 63:
        return False


def valid_string_length(label = None, trailing_dot = None):
    if len(label) > 254 if trailing_dot else 253:
        return False


def check_bidi(label = None, check_ltr = None):
    bidi_label = False
    for idx, cp in enumerate(label, 1):
        direction = unicodedata.bidirectional(cp)
        if direction == '':
            raise IDNABidiError('Unknown directionality in label {} at position {}'.format(repr(label), idx))
        if direction in ('R', 'AL', 'AN'):
            bidi_label = True
        if not bidi_label and check_ltr:
            return True
        direction = None.bidirectional(label[0])
        if direction in ('R', 'AL'):
            rtl = True
        elif direction == 'L':
            rtl = False
        else:
            raise IDNABidiError('First codepoint in label {} must be directionality L, R or AL'.format(repr(label)))
        valid_ending = False
        number_type = None
        for idx, cp in enumerate(label, 1):
            direction = unicodedata.bidirectional(cp)
            if rtl:
                if direction not in ('R', 'AL', 'AN', 'EN', 'ES', 'CS', 'ET', 'ON', 'BN', 'NSM'):
                    raise IDNABidiError('Invalid direction for codepoint at position {} in a right-to-left label'.format(idx))
                if direction in ('R', 'AL', 'EN', 'AN'):
                    valid_ending = True
                elif direction != 'NSM':
                    valid_ending = False
                if direction in ('AN', 'EN'):
                    if not number_type:
                        number_type = direction
                        continue
                    if number_type != direction:
                        raise IDNABidiError('Can not mix numeral types in a right-to-left label')
                continue
            if direction not in ('L', 'EN', 'ES', 'CS', 'ET', 'ON', 'BN', 'NSM'):
                raise IDNABidiError('Invalid direction for codepoint at position {} in a left-to-right label'.format(idx))
            if direction in ('L', 'EN'):
                valid_ending = True
                continue
            if direction != 'NSM':
                valid_ending = False
            if not valid_ending:
                raise IDNABidiError('Label ends with illegal codepoint directionality')
            return True


def check_initial_combiner(label = None):
    if unicodedata.category(label[0])[0] == 'M':
        raise IDNAError('Label begins with an illegal combining character')
    return True


def check_hyphen_ok(label = None):
    if label[2:4] == '--':
        raise IDNAError('Label has disallowed hyphens in 3rd and 4th position')
    if label[0] == '-' or label[-1] == '-':
        raise IDNAError('Label must not start or end with a hyphen')
    return True


def check_nfc(label = None):
    if unicodedata.normalize('NFC', label) != label:
        raise IDNAError('Label must be in Normalization Form C')


def valid_contextj(label = None, pos = None):
    cp_value = ord(label[pos])
    if cp_value == 8204:
        if pos > 0 and _combining_class(ord(label[pos - 1])) == _virama_combining_class:
            return True
        ok = None
        for i in range(pos - 1, -1, -1):
            joining_type = idnadata.joining_types.get(ord(label[i]))
            if joining_type == ord('T'):
                continue
            if joining_type in (ord('L'), ord('D')):
                ok = True
            
        if not ok:
            return False
        ok = None
        for i in range(pos + 1, len(label)):
            joining_type = idnadata.joining_types.get(ord(label[i]))
            if joining_type == ord('T'):
                continue
            if joining_type in (ord('R'), ord('D')):
                ok = True
            
        return ok
    if cp_value == 8205:
        if pos > 0 and _combining_class(ord(label[pos - 1])) == _virama_combining_class:
            return True
        return None


def valid_contexto(label = None, pos = None, exception = None):
    cp_value = ord(label[pos])
    if cp_value == 183:
        if  < 0, pos or 0, pos < len(label) - 1:
            pass
        
    elif ord(label[pos - 1]) == 108 and ord(label[pos + 1]) == 108:
        return True
    return False
    if cp_value == 885:
        if pos < len(label) - 1 and len(label) > 1:
            return _is_script(label[pos + 1], 'Greek')
        return None
    if None == 1523 or cp_value == 1524:
        if pos > 0:
            return _is_script(label[pos - 1], 'Hebrew')
        return None
    if None == 12539:
        for None in label:
            if cp == '・':
                continue
            if _is_script(cp, 'Hiragana') and _is_script(cp, 'Katakana') or _is_script(cp, 'Han'):
                return True
            return False
            if  <= 1632, cp_value or 1632, cp_value <= 1641:
                pass
            
        for None in label:
            if  <= 1776, ord(cp) or 1776, ord(cp) <= 1785:
                pass
            
            return False
            return True
            if  <= 1776, cp_value or 1776, cp_value <= 1785:
                pass
            
        for None in label:
            if  <= 1632, ord(cp) or 1632, ord(cp) <= 1641:
                pass
            
            return False
            return True
            return False


def check_label(label = None):
    if isinstance(label, (bytes, bytearray)):
        label = label.decode('utf-8')
    if len(label) == 0:
        raise IDNAError('Empty Label')
    check_nfc(label)
    check_hyphen_ok(label)
    check_initial_combiner(label)
    for pos, cp in enumerate(label):
        cp_value = ord(cp)
        if intranges_contain(cp_value, idnadata.codepoint_classes['PVALID']):
            continue
        if intranges_contain(cp_value, idnadata.codepoint_classes['CONTEXTJ']):
            if not valid_contextj(label, pos):
                raise InvalidCodepointContext('Joiner {} not allowed at position {} in {}'.format(_unot(cp_value), pos + 1, repr(label)))
            continue
            except ValueError:
                raise IDNAError('Unknown codepoint adjacent to joiner {} at position {} in {}'.format(_unot(cp_value), pos + 1, repr(label)))
        if intranges_contain(cp_value, idnadata.codepoint_classes['CONTEXTO']):
            if not valid_contexto(label, pos):
                raise InvalidCodepointContext('Codepoint {} not allowed at position {} in {}'.format(_unot(cp_value), pos + 1, repr(label)))
            continue
        raise InvalidCodepoint('Codepoint {} at position {} of {} not allowed'.format(_unot(cp_value), pos + 1, repr(label)))
        check_bidi(label)
        return None


def alabel(label = None):
    
    try:
        label_bytes = label.encode('ascii')
        ulabel(label_bytes)
        if not valid_label_length(label_bytes):
            raise IDNAError('Label too long')
        return label_bytes
    except UnicodeEncodeError:
        pass

    check_label(label)
    label_bytes = _alabel_prefix + _punycode(label)
    if not valid_label_length(label_bytes):
        raise IDNAError('Label too long')
    return label_bytes


def ulabel(label = None):
    if not isinstance(label, (bytes, bytearray)):
        
        try:
            label_bytes = label.encode('ascii')
        except UnicodeEncodeError:
            check_label(label)
            return 

        label_bytes.lower() = None
        if label_bytes.startswith(_alabel_prefix):
            label_bytes = label_bytes[len(_alabel_prefix):]
            if not label_bytes:
                raise IDNAError('Malformed A-label, no Punycode eligible content found')
            if label_bytes.decode('ascii')[-1] == '-':
                raise IDNAError('A-label must not end with a hyphen')
        else:
            check_label(label_bytes)
            return label_bytes.decode('ascii')
        
        try:
            label = label_bytes.decode('punycode')
        except UnicodeError:
            raise IDNAError('Invalid A-label')

        check_label(label)
        return label


def uts46_remap(domain = None, std3_rules = None, transitional = None):
    '''Re-map the characters in the string according to UTS46 processing.'''
    uts46data = uts46data
    import uts46data
    output = ''
# WARNING: Decompyle incomplete


def encode(s = None, strict = None, uts46 = None, std3_rules = (False, False, False, False), transitional = ('s', Union[(str, bytes, bytearray)], 'strict', bool, 'uts46', bool, 'std3_rules', bool, 'transitional', bool, 'return', bytes)):
    if not isinstance(s, str):
        
        try:
            s = str(s, 'ascii')
        except UnicodeDecodeError:
            raise IDNAError('should pass a unicode string to the function rather than a byte string.')

        if uts46:
            s = uts46_remap(s, std3_rules, transitional)
    trailing_dot = False
    result = []
    if strict:
        labels = s.split('.')
    else:
        labels = _unicode_dots_re.split(s)
    if labels or labels == [
        '']:
        raise IDNAError('Empty domain')
    if labels[-1] == '':
        del labels[-1]
        trailing_dot = True
    for label in labels:
        s = alabel(label)
        if s:
            result.append(s)
            continue
        raise IDNAError('Empty label')
        if trailing_dot:
            result.append(b'')
    s = b'.'.join(result)
    if not valid_string_length(s, trailing_dot):
        raise IDNAError('Domain too long')
    return s


def decode(s = None, strict = None, uts46 = None, std3_rules = (False, False, False)):
    
    try:
        pass

    if uts46:
        s = uts46_remap(s, std3_rules, False)
    trailing_dot = False
    result = []
    if labels or labels == [
        '']:
        raise IDNAError('Empty domain')
    if not labels[-1]:
        del labels[-1]
        trailing_dot = True
    for label in labels:
        s = ulabel(label)
        if s:
            result.append(s)
            continue
        raise IDNAError('Empty label')
        if trailing_dot:
            result.append('')
    return '.'.join(result)
