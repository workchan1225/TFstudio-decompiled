# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _textwrap.pyc (Python 3.11)

import textwrap
import typing as t
from contextlib import contextmanager

class TextWrapper(textwrap.TextWrapper):
    
    def _handle_long_word(self, reversed_chunks = None, cur_line = None, cur_len = None, width = ('reversed_chunks', t.List[str], 'cur_line', t.List[str], 'cur_len', int, 'width', int, 'return', None)):
        space_left = max(width - cur_len, 1)
        if self.break_long_words:
            last = reversed_chunks[-1]
            cut = last[:space_left]
            res = last[space_left:]
            cur_line.append(cut)
            reversed_chunks[-1] = res
            return None
        if not None:
            cur_line.append(reversed_chunks.pop())
            return None

    extra_indent = (lambda self = None, indent = None: pass# WARNING: Decompyle incomplete
)()
    
    def indent_only(self = None, text = None):
        rv = []
        for idx, line in enumerate(text.splitlines()):
            indent = self.initial_indent
            if idx > 0:
                indent = self.subsequent_indent
            rv.append(f'''{indent}{line}''')
            return '\n'.join(rv)
