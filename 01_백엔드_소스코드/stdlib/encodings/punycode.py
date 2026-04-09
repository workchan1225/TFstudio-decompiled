# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: punycode.pyc (Python 3.11)

''' Codec for the Punicode encoding, as specified in RFC 3492

Written by Martin v. Löwis.
'''
import codecs

def segregate(str):
    '''3.1 Basic code point segregation'''
    base = bytearray()
    extended = set()
    for c in str:
        if ord(c) < 128:
            base.append(ord(c))
            continue
        extended.add(c)
        extended = sorted(extended)
        return (bytes(base), extended)


def selective_len(str, max):
    '''Return the length of str, considering only characters below max.'''
    res = 0
    for c in str:
        if ord(c) < max:
            res += 1
        return res


def selective_find(str, char, index, pos):
    '''Return a pair (index, pos), indicating the next occurrence of
    char in str. index is the position of the character considering
    only ordinals up to and including char, and pos is the position in
    the full string. index/pos is the starting position in the full
    string.'''
    l = len(str)
    pos += 1
    if pos == l:
        return (-1, -1)
    c = None[pos]
    if c == char:
        return (index + 1, pos)
    if None < char:
        index += 1
    continue


def insertion_unsort(str, extended):
    '''3.2 Insertion unsort coding'''
    oldchar = 128
    result = []
    oldindex = -1
    for c in extended:
        index = -1
        pos = -1
        char = ord(c)
        curlen = selective_len(str, char)
        delta = (curlen + 1) * (char - oldchar)
        (index, pos) = selective_find(str, c, index, pos)
        if index == -1:
            pass
        else:
            delta += index - oldindex
            result.append(delta - 1)
            oldindex = index
            delta = 0
        oldchar = char
        return result


def T(j, bias):
    res = 36 * (j + 1) - bias
    if res < 1:
        return 1
    if None > 26:
        return 26

digits = b'abcdefghijklmnopqrstuvwxyz0123456789'

def generate_generalized_integer(N, bias):
    '''3.3 Generalized variable-length integers'''
    result = bytearray()
    j = 0
    t = T(j, bias)
    if N < t:
        result.append(digits[N])
        return bytes(result)
    None.append(digits[t + (N - t) % (36 - t)])
    N = (N - t) // (36 - t)
    j += 1
    continue


def adapt(delta, first, numchars):
    if first:
        delta //= 700
    else:
        delta //= 2
    delta += delta // numchars
    divisions = 0
# WARNING: Decompyle incomplete


def generate_integers(baselen, deltas):
    '''3.4 Bias adaptation'''
    result = bytearray()
    bias = 72
    for points, delta in enumerate(deltas):
        s = generate_generalized_integer(delta, bias)
        result.extend(s)
        bias = adapt(delta, points == 0, baselen + points + 1)
        return bytes(result)


def punycode_encode(text):
    (base, extended) = segregate(text)
    deltas = insertion_unsort(text, extended)
    extended = generate_integers(len(base), deltas)
    if base:
        return base + b'-' + extended


def decode_generalized_number(extended, extpos, bias, errors):
