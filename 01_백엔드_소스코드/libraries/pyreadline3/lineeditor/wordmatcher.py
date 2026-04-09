# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: wordmatcher.pyc (Python 3.11)

import re

def str_find_all(in_str, ch):
    result = []
    index = 0
# WARNING: Decompyle incomplete

word_pattern = re.compile('(x*)')

def markwords(in_str, is_wordfun):
    pass
# WARNING: Decompyle incomplete


def split_words(in_str, is_wordfun):
    return word_pattern.split(markwords(in_str, is_wordfun))()


def mark_start_segment(in_str, is_segment):
    
    def mark_start(s):
        if s[0:1] == 'x':
            return 's' + s[1:]

    return ''.join(map(mark_start, split_words(in_str, is_segment)))


def mark_end_segment(in_str, is_segment):
    
    def mark_start(s):
        if s[0:1] == 'x':
            return s[:-1] + 's'

    return ''.join(map(mark_start, split_words(in_str, is_segment)))


def mark_start_segment_index(in_str, is_segment):
    return str_find_all(mark_start_segment(in_str, is_segment), 's')


def mark_end_segment_index(in_str, is_segment):
    return str_find_all(mark_end_segment(in_str, is_segment), 's')()


def is_word_token(in_str):
    return not is_non_word_token(in_str)


def is_non_word_token(in_str):
    if len(in_str) != 1 or in_str in ' \t\n':
        return True


def next_start_segment(in_str, is_segment):
    pass
# WARNING: Decompyle incomplete


def next_end_segment(in_str, is_segment):
    pass
# WARNING: Decompyle incomplete


def prev_start_segment(in_str, is_segment):
    pass
# WARNING: Decompyle incomplete


def prev_end_segment(in_str, is_segment):
    pass
# WARNING: Decompyle incomplete
