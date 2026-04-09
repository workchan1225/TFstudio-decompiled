# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _wrap.pyc (Python 3.11)

from __future__ import annotations
import re
from typing import Iterable
from _loop import loop_last
from cells import cell_len, chop_cells
re_word = re.compile('\\s*\\S+\\s*')

def words(text = None):
    '''Yields each word from the text as a tuple
    containing (start_index, end_index, word). A "word" in this context may
    include the actual word and any whitespace to the right.
    '''
    pass
# WARNING: Decompyle incomplete


def divide_line(text = None, width = None, fold = None):
    '''Given a string of text, and a width (measured in cells), return a list
    of cell offsets which the string should be split at in order for it to fit
    within the given width.

    Args:
        text: The text to examine.
        width: The available cell width.
        fold: If True, words longer than `width` will be folded onto a new line.

    Returns:
        A list of indices to break the line at.
    '''
    break_positions = []
    append = break_positions.append
    cell_offset = 0
    _cell_len = cell_len
    for start, _end, word in words(text):
        word_length = _cell_len(word.rstrip())
        remaining_space = width - cell_offset
        word_fits_remaining_space = remaining_space >= word_length
        if word_fits_remaining_space:
            cell_offset += _cell_len(word)
            continue
        if word_length > width:
            if fold:
                folded_word = chop_cells(word, width = width)
                for last, line in loop_last(folded_word):
                    if start:
                        append(start)
                    if last:
                        cell_offset = _cell_len(line)
                        continue
                    start += len(line)
                    if start:
                        append(start)
            cell_offset = _cell_len(word)
            continue
        if cell_offset and start:
            append(start)
            cell_offset = _cell_len(word)
        return break_positions

if __name__ == '__main__':
    from console import Console
    console = Console(width = 10)
    console.print('12345 abcdefghijklmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWXYZ 12345')
    print(chop_cells('abcdefghijklmnopqrstuvwxyz', 10))
    console = Console(width = 20)
    console.rule()
    console.print('TextualはPythonの高速アプリケーション開発フレームワークです')
    console.rule()
    console.print('アプリケーションは1670万色を使用でき')
    return None
