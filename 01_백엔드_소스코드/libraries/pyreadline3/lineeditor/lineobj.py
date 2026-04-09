# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lineobj.pyc (Python 3.11)

from pyreadline3.clipboard import clipboard
from pyreadline3.unicode_helper import biter, ensure_unicode
from  import wordmatcher
kill_ring_to_clipboard = False

class NotAWordError(IndexError):
    pass


def quote_char(c):
    if ord(c) > 0:
        return c


class LinePositioner(object):
    
    def __call__(self, line):
        NotImplementedError('Base class !!!')



class NextChar(LinePositioner):
    
    def __call__(self, line):
        if line.point < len(line.line_buffer):
            return line.point + 1
        return None.point


NextChar = NextChar()

class PrevChar(LinePositioner):
    
    def __call__(self, line):
        if line.point > 0:
            return line.point - 1
        return None.point


PrevChar = PrevChar()

class NextWordStart(LinePositioner):
    
    def __call__(self, line):
        return line.next_start_segment(line.line_buffer, line.is_word_token)[line.point]


NextWordStart = NextWordStart()

class NextWordEnd(LinePositioner):
    
    def __call__(self, line):
        return line.next_end_segment(line.line_buffer, line.is_word_token)[line.point]


NextWordEnd = NextWordEnd()

class PrevWordStart(LinePositioner):
    
    def __call__(self, line):
        return line.prev_start_segment(line.line_buffer, line.is_word_token)[line.point]


PrevWordStart = PrevWordStart()

class WordStart(LinePositioner):
    
    def __call__(self, line):
        if line.is_word_token(line.get_line_text()[Point(line):Point(line) + 1]):
            if Point(line) > 0 and line.is_word_token(line.get_line_text()[Point(line) - 1:Point(line)]):
                return PrevWordStart(line)
            return None.point
        raise None('Point is not in a word')


WordStart = WordStart()

class WordEnd(LinePositioner):
    
    def __call__(self, line):
        if line.is_word_token(line.get_line_text()[Point(line):Point(line) + 1]):
            if line.is_word_token(line.get_line_text()[Point(line) + 1:Point(line) + 2]):
                return NextWordEnd(line)
            return None.point
        raise None('Point is not in a word')


WordEnd = WordEnd()

class PrevWordEnd(LinePositioner):
    
    def __call__(self, line):
        return line.prev_end_segment(line.line_buffer, line.is_word_token)[line.point]


PrevWordEnd = PrevWordEnd()

class PrevSpace(LinePositioner):
    
    def __call__(self, line):
        point = line.point
    # WARNING: Decompyle incomplete


PrevSpace = PrevSpace()

class StartOfLine(LinePositioner):
    
    def __call__(self, line):
        return 0


StartOfLine = StartOfLine()

class EndOfLine(LinePositioner):
    
    def __call__(self, line):
        return len(line.line_buffer)


EndOfLine = EndOfLine()

class Point(LinePositioner):
    
    def __call__(self, line):
        return line.point


Point = Point()

class Mark(LinePositioner):
    
    def __call__(self, line):
        return line.mark


k = Mark()
all_positioners = (lambda .0: pass# WARNING: Decompyle incomplete
)(globals().items()())

class LineSlice(object):
    
    def __call__(self, line):
        NotImplementedError('Base class !!!')



class CurrentWord(LineSlice):
    
    def __call__(self, line):
        return slice(WordStart(line), WordEnd(line), None)


CurrentWord = CurrentWord()

class NextWord(LineSlice):
    
    def __call__(self, line):
        work = TextLine(line)
        work.point = NextWordStart
        start = work.point
        stop = NextWordEnd(work)
        return slice(start, stop)


NextWord = NextWord()

class PrevWord(LineSlice):
    
    def __call__(self, line):
        work = TextLine(line)
        work.point = PrevWordEnd
        stop = work.point
        start = PrevWordStart(work)
        return slice(start, stop)


PrevWord = PrevWord()

class PointSlice(LineSlice):
    
    def __call__(self, line):
        return slice(Point(line), Point(line) + 1, None)


PointSlice = PointSlice()

class TextLine(object):
    
    def __init__(self, txtstr, point, mark = (None, None)):
        self.line_buffer = []
        self._point = 0
        self.mark = -1
        self.undo_stack = []
        self.overwrite = False
    # WARNING: Decompyle incomplete

    
    def push_undo(self):
        l_text = self.get_line_text()
        if self.undo_stack and l_text == self.undo_stack[-1].get_line_text():
            self.undo_stack[-1].point = self.point
            return None
        None.undo_stack.append(self.copy())

    
    def pop_undo(self):
        if len(self.undo_stack) >= 2:
            self.undo_stack.pop()
            self.set_top_undo()
            self.undo_stack.pop()
            return None
        None.reset_line()
        self.undo_stack = []

    
    def set_top_undo(self):
        if self.undo_stack:
            undo = self.undo_stack[-1]
            self.line_buffer = undo.line_buffer
            self.point = undo.point
            self.mark = undo.mark
            return None

    
    def __repr__(self):
        return f'''TextLine("{self.line_buffer!s}",point={self.point!s},mark={self.mark!s})'''

    
    def copy(self):
        return self.__class__(self)

    
    def set_point(self, value):
        if isinstance(value, LinePositioner):
            value = value(self)
    # WARNING: Decompyle incomplete

    
    def get_point(self):
        return self._point

    point = property(get_point, set_point)
    
    def visible_line_width(self, position = (Point,)):
        '''Return the visible width of the text up to position.'''
        extra_char_width = (lambda .0: pass# WARNING: Decompyle incomplete
)(self[:position].line_buffer())
        return len(self[:position].quoted_text()) + self[:position].line_buffer.count('\t') * 7 + extra_char_width

    
    def quoted_text(self):
        quoted = self.line_buffer()
        return ''.join(map(ensure_unicode, quoted))

    
    def get_line_text(self):
        buf = self.line_buffer
        buf = list(map(ensure_unicode, buf))
        return ''.join(buf)

    
    def set_line(self, text, cursor = (None,)):
        self.line_buffer = str(text)()
    # WARNING: Decompyle incomplete

    
    def reset_line(self):
        self.line_buffer = []
        self.point = 0

    
    def end_of_line(self):
        self.point = len(self.line_buffer)

    
    def _insert_text(self, text, argument = (1,)):
        text = text * argument
        if self.overwrite:
            for c in biter(text):
                self.line_buffer[self.point] = c
                return None
                for None in biter(text):
                    self.line_buffer.insert(self.point, c)
                    return None

    
    def __getitem__(self, key):
        if isinstance(key, LineSlice):
            key = key(self)
    # WARNING: Decompyle incomplete

    
    def __delitem__(self, key):
        point = self.point
        if isinstance(key, LineSlice):
            key = key(self)
    # WARNING: Decompyle incomplete

    
    def __setitem__(self, key, value):
        if isinstance(key, LineSlice):
            key = key(self)
        if isinstance(key, slice):
            start = key.start
            stop = key.stop
        elif isinstance(key, LinePositioner):
            start = key(self)
            stop = start + 1
        else:
            start = key
            stop = key + 1
        prev = self.line_buffer[:start]
        value = self.__class__(value).line_buffer
        rest = self.line_buffer[stop:]
        out = prev + value + rest
        if len(out) >= len(self):
            self.point = len(self)
        self.line_buffer = out

    
    def __len__(self):
        return len(self.line_buffer)

    
    def upper(self):
        self.line_buffer = self.line_buffer()
        return self

    
    def lower(self):
        self.line_buffer = self.line_buffer()
        return self

    
    def capitalize(self):
        self.set_line(self.get_line_text().capitalize(), self.point)
        return self

    
    def startswith(self, txt):
        return self.get_line_text().startswith(txt)

    
    def endswith(self, txt):
        return self.get_line_text().endswith(txt)

    
    def __contains__(self, txt):
        return txt in self.get_line_text()



class ReadLineTextBuffer(TextLine):
    pass
# WARNING: Decompyle incomplete

q = ReadLineTextBuffer('asff asFArw  ewrWErhg', point = 8)
q = TextLine('asff asFArw  ewrWErhg', point = 8)

def show_pos(buff, pos, chr = ('.',)):
    pass
# WARNING: Decompyle incomplete


def test_positioner(buff, points, positioner):
    print((' %s ' % positioner.__class__.__name__).center(40, '-'))
    buffstr = buff.line_buffer
    print('"%s"' % buffstr)
    for point in points:
        b = TextLine(buff, point = point)
        out = [
            ' '] * (len(buffstr) + 1)
        pos = positioner(b)
        if pos == point:
            out[pos] = '&'
        else:
            out[point] = '.'
            out[pos] = '^'
        print('"%s"' % ''.join(out))
        return None

if __name__ == '__main__':
    print(f'''{'Position'!s:15} "{q.get_line_text()!s}"''')
    print(f'''{'Point'!s:15} "{show_pos(q, q.point)!s}"''')
    for name, positioner_q in all_positioners:
        pos_q = positioner_q(q)
        print(f'''{name!s:15} "{show_pos(q, pos_q, '^')!s}"''')
        l_t = ReadLineTextBuffer('kjjk asads   asad')
        l_t.point = EndOfLine
        return None
        return None
