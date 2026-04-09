# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _parser.pyc (Python 3.11)

'''Internal support module for sre'''
from _constants import *
SPECIAL_CHARS = '.\\[{()*+?^$|'
REPEAT_CHARS = '*+?{'
DIGITS = frozenset('0123456789')
OCTDIGITS = frozenset('01234567')
HEXDIGITS = frozenset('0123456789abcdefABCDEF')
ASCIILETTERS = frozenset('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
WHITESPACE = frozenset(' \t\n\r\x0b\x0c')
_REPEATCODES = frozenset({
    MIN_REPEAT,
    MAX_REPEAT,
    POSSESSIVE_REPEAT})
_UNITCODES = frozenset({
    ANY,
    RANGE,
    IN,
    LITERAL,
    NOT_LITERAL,
    CATEGORY})
ESCAPES = {
    '\\a': (LITERAL, ord('\x07')),
    '\\b': (LITERAL, ord('\x08')),
    '\\f': (LITERAL, ord('\x0c')),
    '\\n': (LITERAL, ord('\n')),
    '\\r': (LITERAL, ord('\r')),
    '\\t': (LITERAL, ord('\t')),
    '\\v': (LITERAL, ord('\x0b')),
    '\\\\': (LITERAL, ord('\\')) }
CATEGORIES = {
    '\\A': (AT, AT_BEGINNING_STRING),
    '\\b': (AT, AT_BOUNDARY),
    '\\B': (AT, AT_NON_BOUNDARY),
    '\\d': (IN, [
        (CATEGORY, CATEGORY_DIGIT)]),
    '\\D': (IN, [
        (CATEGORY, CATEGORY_NOT_DIGIT)]),
    '\\s': (IN, [
        (CATEGORY, CATEGORY_SPACE)]),
    '\\S': (IN, [
        (CATEGORY, CATEGORY_NOT_SPACE)]),
    '\\w': (IN, [
        (CATEGORY, CATEGORY_WORD)]),
    '\\W': (IN, [
        (CATEGORY, CATEGORY_NOT_WORD)]),
    '\\Z': (AT, AT_END_STRING) }
FLAGS = {
    'i': SRE_FLAG_IGNORECASE,
    'L': SRE_FLAG_LOCALE,
    'm': SRE_FLAG_MULTILINE,
    's': SRE_FLAG_DOTALL,
    'x': SRE_FLAG_VERBOSE,
    'a': SRE_FLAG_ASCII,
    't': SRE_FLAG_TEMPLATE,
    'u': SRE_FLAG_UNICODE }
TYPE_FLAGS = SRE_FLAG_ASCII | SRE_FLAG_LOCALE | SRE_FLAG_UNICODE
GLOBAL_FLAGS = SRE_FLAG_DEBUG | SRE_FLAG_TEMPLATE
MAXWIDTH = 0x10000000000000000

class State:
    
    def __init__(self):
        self.flags = 0
        self.groupdict = { }
        self.groupwidths = [
            None]
        self.lookbehindgroups = None
        self.grouprefpos = { }

    groups = (lambda self: len(self.groupwidths))()
    
    def opengroup(self, name = (None,)):
        gid = self.groups
        self.groupwidths.append(None)
        if self.groups > MAXGROUPS:
            raise error('too many groups')
    # WARNING: Decompyle incomplete

    
    def closegroup(self, gid, p):
        self.groupwidths[gid] = p.getwidth()

    
    def checkgroup(self, gid):
        if gid < self.groups:
            pass
        return self.groupwidths[gid] is not None

    
    def checklookbehindgroup(self, gid, source):
        pass
    # WARNING: Decompyle incomplete



class SubPattern:
    
    def __init__(self, state, data = (None,)):
        self.state = state
    # WARNING: Decompyle incomplete

    
    def dump(self, level = (0,)):
        seqtypes = (tuple, list)
        for op, av in self.data:
            print(level * '  ' + str(op), end = '')
            if op is IN:
                print()
                for op, a in av:
                    print((level + 1) * '  ' + str(op), a)
                    if op is BRANCH:
                        print()
                        for i, a in enumerate(av[1]):
                            if i:
                                print(level * '  ' + 'OR')
                            a.dump(level + 1)
                            if op is GROUPREF_EXISTS:
                                (condgroup, item_yes, item_no) = av
                                print('', condgroup)
                                item_yes.dump(level + 1)
                                if item_no:
                                    print(level * '  ' + 'ELSE')
                                    item_no.dump(level + 1)
                                continue
            if isinstance(av, SubPattern):
                print()
                av.dump(level + 1)
                continue
            if isinstance(av, seqtypes):
                nl = False
                for a in av:
                    if isinstance(a, SubPattern):
                        if not nl:
                            print()
                        a.dump(level + 1)
                        nl = True
                        continue
                    if not nl:
                        print(' ', end = '')
                    print(a, end = '')
                    nl = False
                    if not nl:
                        print()
                continue
            print('', av)
            return None

    
    def __repr__(self):
        return repr(self.data)

    
    def __len__(self):
        return len(self.data)

    
    def __delitem__(self, index):
        del self.data[index]

    
    def __getitem__(self, index):
        if isinstance(index, slice):
            return SubPattern(self.state, self.data[index])
        return None.data[index]

    
    def __setitem__(self, index, code):
        self.data[index] = code

    
    def insert(self, index, code):
        self.data.insert(index, code)

    
    def append(self, code):
        self.data.append(code)

    
    def getwidth(self):
        pass
    # WARNING: Decompyle incomplete



class Tokenizer:
    
    def __init__(self, string):
        self.istext = isinstance(string, str)
        self.string = string
        if not self.istext:
            string = str(string, 'latin1')
        self.decoded_string = string
        self.index = 0
        self.next = None
        self.__next()

    
    def __next(self):
        index = self.index
        
        try:
            char = self.decoded_string[index]
        except IndexError:
            self.next = None
            return None

        if char == '\\':
            index += 1
            
            try:
                char += self.decoded_string[index]
            except IndexError:
                raise error('bad escape (end of pattern)', self.string, len(self.string) - 1), None

            self.index = index + 1
            self.next = char
            return None

    
    def match(self, char):
        if char == self.next:
            self.__next()
            return True

    
    def get(self):
        this = self.next
        self.__next()
        return this

    
    def getwhile(self, n, charset):
        result = ''
        for _ in range(n):
            c = self.next
            if c not in charset:
                pass
            else:
                result += c
                self.__next()
            return result

    
    def getuntil(self, terminator, name):
        result = ''
        c = self.next
        self.__next()
    # WARNING: Decompyle incomplete

    pos = (lambda self:
