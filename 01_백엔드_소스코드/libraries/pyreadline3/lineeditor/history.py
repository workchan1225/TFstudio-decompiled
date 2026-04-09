# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: history.pyc (Python 3.11)

import re
import operator
import string
import sys
import os
import io
from pyreadline3.logger import log
from pyreadline3.unicode_helper import ensure_str, ensure_unicode
from  import lineobj

class EscapeHistory(Exception):
    pass


class LineHistory(object):
    
    def __init__(self):
        self.history = []
        self._history_length = 100
        self._history_cursor = 0
        self.history_filename = os.path.expanduser(ensure_str('~/.history'))
        self.lastcommand = None
        self.query = ''
        self.last_search_for = ''

    
    def get_current_history_length(self):
        '''Return the number of lines currently in the history.
        (This is different from get_history_length(), which returns
        the maximum number of lines that will be written to a history file.)'''
        value = len(self.history)
        log('get_current_history_length:%d' % value)
        return value

    
    def get_history_length(self):
        '''Return the desired length of the history file. Negative values imply
        unlimited history file size.'''
        value = self._history_length
        log('get_history_length:%d' % value)
        return value

    
    def get_history_item(self, index):
        '''Return the current contents of history item at index (starts with index 1).'''
        item = self.history[index - 1]
        log('get_history_item: index:%d item:%r' % (index, item))
        return item.get_line_text()

    
    def set_history_length(self, value):
        log('set_history_length: old:%d new:%d' % (self._history_length, value))
        self._history_length = value

    
    def get_history_cursor(self):
        value = self._history_cursor
        log('get_history_cursor:%d' % value)
        return value

    
    def set_history_cursor(self, value):
        log('set_history_cursor: old:%d new:%d' % (self._history_cursor, value))
        self._history_cursor = value

    history_length = property(get_history_length, set_history_length)
    history_cursor = property(get_history_cursor, set_history_cursor)
    
    def clear_history(self):
        '''Clear readline history.'''
        self.history[:] = []
        self.history_cursor = 0

    
    def read_history_file(self, filename = (None,)):
        '''Load a readline history file.'''
        pass
    # WARNING: Decompyle incomplete

    
    def write_history_file(self, filename = (None,)):
        '''Save a readline history file.'''
        pass
    # WARNING: Decompyle incomplete

    
    def add_history(self, line):
        '''Append a line to the history buffer, as if it was the last line typed.'''
        line = ensure_unicode(line)
        if not hasattr(line, 'get_line_text'):
            line = lineobj.ReadLineTextBuffer(line)
        if not line.get_line_text():
            pass
        elif len(self.history) > 0 and self.history[-1].get_line_text() == line.get_line_text():
            pass
        else:
            self.history.append(line)
        self.history_cursor = len(self.history)

    
    def previous_history(self, current):
        '''Move back through the history list, fetching the previous command.'''
        if self.history_cursor == len(self.history):
            self.history.append(current.copy())
        if self.history_cursor > 0:
            current.set_line(self.history[self.history_cursor].get_line_text())
            lineobj.EndOfLine = self, self.history_cursor -= 1, .history_cursor
            return None

    
    def next_history(self, current):
        '''Move forward through the history list, fetching the next command.'''
        if self.history_cursor < len(self.history) - 1:
            current.set_line(self.history[self.history_cursor].get_line_text())
            return None

    
    def beginning_of_history(self):
        '''Move to the first line in the history.'''
        self.history_cursor = 0
        if len(self.history) > 0:
            self.l_buffer = self.history[0]
            return None

    
    def end_of_history(self, current):
        '''Move to the end of the input history, i.e., the line currently
        being entered.'''
        self.history_cursor = len(self.history)
        current.set_line(self.history[-1].get_line_text())

    
    def reverse_search_history(self, searchfor, startpos = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def forward_search_history(self, searchfor, startpos = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _search(self, direction, partial):
        pass
    # WARNING: Decompyle incomplete

    
    def history_search_forward(self, partial):
        '''Search forward through the history for the string of characters
        between the start of the current line and the point. This is a
        non-incremental search. By default, this command is unbound.'''
        return self._search(1, partial)

    
    def history_search_backward(self, partial):
        '''Search backward through the history for the string of characters
        between the start of the current line and the point. This is a
        non-incremental search. By default, this command is unbound.'''
        return self._search(-1, partial)


if __name__ == '__main__':
    q = LineHistory()
    r = LineHistory()
    s = LineHistory()
    RL = lineobj.ReadLineTextBuffer
    q.add_history(RL('aaaa'))
    q.add_history(RL('aaba'))
    q.add_history(RL('aaca'))
    q.add_history(RL('akca'))
    q.add_history(RL('bbb'))
    q.add_history(RL('ako'))
    r.add_history(RL('ako'))
    return None
