# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: unicode.pyc (Python 3.11)

import sys
from itertools import filterfalse
from typing import Union

class _lazyclassproperty:
    
    def __init__(self, fn):
        self.fn = fn
        self.__doc__ = fn.__doc__
        self.__name__ = fn.__name__

    
    def __get__(self, obj, cls):
        pass
    # WARNING: Decompyle incomplete


UnicodeRangeList = list[Union[(tuple[(int, int)], tuple[int])]]

class unicode_set:
    '''
    A set of Unicode characters, for language-specific strings for
    ``alphas``, ``nums``, ``alphanums``, and ``printables``.
    A unicode_set is defined by a list of ranges in the Unicode character
    set, in a class attribute ``_ranges``. Ranges can be specified using
    2-tuples or a 1-tuple, such as::

        _ranges = [
            (0x0020, 0x007e),
            (0x00a0, 0x00ff),
            (0x0100,),
            ]

    Ranges are left- and right-inclusive. A 1-tuple of (x,) is treated as (x, x).

    A unicode set can also be defined using multiple inheritance of other unicode sets::

        class CJK(Chinese, Japanese, Korean):
            pass
    '''
    _ranges: UnicodeRangeList = []
    _chars_for_ranges = (lambda cls = None: ret = []for cc in cls.__mro__:
if cc is unicode_set:
passelse:
for rr in getattr(cc, '_ranges', ()):
ret.extend(range(rr[0], rr[-1] + 1))(lambda .0: pass# WARNING: Decompyle incomplete
)(set(ret)())
)()
    printables = (lambda cls = None: ''.join(filterfalse(str.isspace, cls._chars_for_ranges)))()
    alphas = (lambda cls = None: ''.join(filter(str.isalpha, cls._chars_for_ranges)))()
    nums = (lambda cls = None: ''.join(filter(str.isdigit, cls._chars_for_ranges)))()
    alphanums = (lambda cls = None: cls.alphas + cls.nums)()
    identchars = (lambda cls = None: ''.join(sorted(set(filter(str.isidentifier, cls._chars_for_ranges)) | set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzªµºÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ_'))))()
    identbodychars = (lambda cls = None: identifier_chars = (lambda .0: pass# WARNING: Decompyle incomplete
)(cls._chars_for_ranges())
        return ''.join(sorted(identifier_chars | set(cls.identchars) | set('0123456789·')))
)()
    identifier = (lambda cls: Word = Wordimport pyparsingWord(cls.identchars, cls.identbodychars))()


class pyparsing_unicode(unicode_set):
    '''
    A namespace class for defining common language unicode_sets.
    '''
    _ranges: UnicodeRangeList = [
        (32, sys.maxunicode)]
    
    class BasicMultilingualPlane(unicode_set):
        '''Unicode set for the Basic Multilingual Plane'''
        _ranges: UnicodeRangeList = [
            (32, 65535)]

    
    class Latin1(unicode_set):
        '''Unicode set for Latin-1 Unicode Character Range'''
        _ranges: UnicodeRangeList = [
            (32, 126),
            (160, 255)]

    
    class LatinA(unicode_set):
        '''Unicode set for Latin-A Unicode Character Range'''
        _ranges: UnicodeRangeList = [
            (256, 383)]

    
    class LatinB(unicode_set):
        '''Unicode set for Latin-B Unicode Character Range'''
        _ranges: UnicodeRangeList = [
            (384, 591)]

    
    class Greek(unicode_set):
        '''Unicode set for Greek Unicode Character Ranges'''
        _ranges: UnicodeRangeList = [
            (834, 837),
            (880, 887),
            (890, 895),
            (900, 906),
            (908,),
            (910, 929),
            (931, 993),
            (1008, 1023),
            (7462, 7466),
            (7518,),
            (7520,),
            (7526, 7530),
            (7936, 7957),
            (7960, 7965),
            (7968, 8005),
            (8008, 8013),
            (8016, 8023),
            (8025,),
            (8027,),
            (8029,),
            (8031, 8061),
            (8064, 8116),
            (8118, 8132),
            (8134, 8147),
            (8150, 8155),
            (8157, 8175),
            (8178, 8180),
            (8182, 8190),
            (8489,),
            (10009, 10010),
            (43877,),
            (65856, 65933),
            (65952,),
            (119296, 119365),
            (128929, 128935)]

    
    class Cyrillic(unicode_set):
        '''Unicode set for Cyrillic Unicode Character Range'''
        _ranges: UnicodeRangeList = [
            (1024, 1327),
            (7296, 7304),
            (7467,),
            (7544,),
            (11744, 11775),
            (42560, 42610),
            (42612, 42655),
            (65070, 65071)]

    
    class Chinese(unicode_set):
        '''Unicode set for Chinese Unicode Character Range'''
        _ranges: UnicodeRangeList = [
            (11904, 11929),
            (11931, 12019),
            (12736, 12771),
            (13312, 19893),
            (19968, 40943),
            (42752, 42759),
            (63744, 64109),
            (64112, 64217),
            (94178, 94179),
            (127504, 127506),
            (127508, 127547),
            (127552, 127560),
            (131072, 173782),
            (173824, 177972),
            (177984, 178205),
            (178208, 183969),
            (183984, 191456),
            (194560, 195101)]

    
    class Japanese(unicode_set):
        '''Unicode set for Japanese Unicode Character Range, combining Kanji, Hiragana, and Katakana ranges'''
        
        class Kanji(unicode_set):
            '''Unicode set for Kanji Unicode Character Range'''
            _ranges: UnicodeRangeList = [
                (19968, 40895),
                (12288, 12351)]

        
        class Hiragana(unicode_set):
            '''Unicode set for Hiragana Unicode Character Range'''
            _ranges: UnicodeRangeList = [
                (12353, 12438),
                (12441, 12448),
                (12540,),
                (65392,),
                (110593,),
                (110928, 110930),
                (127488,)]

        
        class Katakana(unicode_set):
            '''Unicode set for Katakana  Unicode Character Range'''
            _ranges: UnicodeRangeList = [
                (12441, 12444),
                (12448, 12543),
                (12784, 12799),
                (13008, 13054),
                (65381, 65439),
                (110592,),
                (110948, 110951),
                (127489, 127490),
                (127507,)]

        漢字 = Kanji
        カタカナ = Katakana
        ひらがな = Hiragana
        _ranges = Kanji._ranges + Hiragana._ranges + Katakana._ranges

    
    class Hangul(unicode_set):
        '''Unicode set for Hangul (Korean) Unicode Character Range'''
        _ranges: UnicodeRangeList = [
            (4352, 4607),
            (12334, 12335),
            (12593, 12686),
            (12800, 12828),
            (12896, 12923),
            (12926,),
            (43360, 43388),
            (44032, 55203),
            (55216, 55238),
            (55243, 55291),
            (65440, 65470),
            (65474, 65479),
            (65482, 65487),
            (65490, 65495),
            (65498, 65500)]

    Korean = Hangul
    
    class CJK(Hangul, Japanese, Chinese):
        '''Unicode set for combined Chinese, Japanese, and Korean (CJK) Unicode Character Range'''
        pass

    
    class Thai(unicode_set):
        '''Unicode set for Thai Unicode Character Range'''
        _ranges: UnicodeRangeList = [
            (3585, 3642),
            (3647, 3675)]

    
    class Arabic(unicode_set):
        '''Unicode set for Arabic Unicode Character Range'''
        _ranges: UnicodeRangeList = [
            (1536, 1563),
            (1566, 1791),
            (1792, 1919)]

    
    class Hebrew(unicode_set):
        '''Unicode set for Hebrew Unicode Character Range'''
        _ranges: UnicodeRangeList = [
            (1425, 1479),
            (1488, 1514),
            (1519, 1524),
            (64285, 64310),
            (64312, 64316),
            (64318,),
            (64320, 64321),
            (64323, 64324),
            (64326, 64335)]

    
    class Devanagari(unicode_set):
        '''Unicode set for Devanagari Unicode Character Range'''
        _ranges: UnicodeRangeList = [
            (2304, 2431),
            (43232, 43263)]

    BMP = BasicMultilingualPlane
    العربية = Arabic
    中文 = Chinese
    кириллица = Cyrillic
    Ελληνικά = Greek
    עִברִית = Hebrew
    日本語 = Japanese
    한국어 = Korean
    ไทย = Thai
    देवनागरी = Devanagari
