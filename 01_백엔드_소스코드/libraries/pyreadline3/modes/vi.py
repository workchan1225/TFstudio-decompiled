# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vi.pyc (Python 3.11)

import os

lineobj
from pyreadline3.logger import log
import pyreadline3.lineeditor.lineobj, lineeditor
from  import basemode

class ViMode(basemode.BaseMode):
    pass
# WARNING: Decompyle incomplete

_VI_BEGIN = 'vi_begin'
_VI_MULTI1 = 'vi_multi1'
_VI_ACTION = 'vi_action'
_VI_MULTI2 = 'vi_multi2'
_VI_MOTION = 'vi_motion'
_VI_MOTION_ARGUMENT = 'vi_motion_argument'
_VI_REPLACE_ONE = 'vi_replace_one'
_VI_TEXT = 'vi_text'
_VI_SEARCH = 'vi_search'
_VI_END = 'vi_end'

class ViCommand:
    
    def __init__(self, readline):
        self.readline = readline
        self.lst_char = []
        self.state = _VI_BEGIN
        self.action = self.movement
        self.motion = None
        self.motion_argument = None
        self.text = None
        self.pos_motion = None
        self.is_edit = False
        self.is_overwrite = False
        self.is_error = False
        self.is_star = False
        self.delete_left = 0
        self.delete_right = 0
        self.readline._vi_multiplier1 = ''
        self.readline._vi_multiplier2 = ''
        self.set_override_multiplier(0)
        self.skip_multipler = False
        self.tabstop = 4
        self.dct_fcn = {
            8: self.key_backspace,
            ord('~'): self.key_tilde,
            ord('|'): self.key_bar,
            ord('*'): self.key_star,
            ord('/'): self.key_slash,
            ord('.'): self.key_dot,
            ord('%'): self.key_percent,
            ord(','): self.key_comma,
            ord(';'): self.key_semicolon,
            ord('^'): self.key_hat,
            ord('$'): self.key_dollar }

    
    def add_char(self, char):
        self.lst_char.append(char)
        if self.state == _VI_BEGIN and self.readline.vi_is_insert_mode:
            self.readline.vi_save_line()
            self.state = _VI_TEXT
        if self.state == _VI_SEARCH:
            if char == '\x08':
                self.key_backspace(char)
            else:
                self.set_text(char)
            return None
        if None.state == _VI_TEXT:
            if char == '\x1b':
                self.escape(char)
            elif char == '\t':
                ts = self.tabstop
                ws = ' ' * (ts - self.readline.l_buffer.point % ts)
                self.set_text(ws)
            elif char == '\x08':
                self.key_backspace(char)
            else:
                self.set_text(char)
            return None
        if None.state == _VI_MOTION_ARGUMENT:
            self.set_motion_argument(char)
            return None
        if None.state == _VI_REPLACE_ONE:
            self.replace_one(char)
            return None
        
        try:
            fcn_instance = self.dct_fcn[ord(char)]
        except BaseException:
            fcn_instance = getattr(self, 'key_%s' % char, None)

        if fcn_instance:
            fcn_instance(char)
            return None
        if None.isdigit():
            self.key_digit(char)
            return None
        None.error()

    
    def set_text(self, text):
        pass
    # WARNING: Decompyle incomplete

    
    def set_buffer(self, text):
        for char in text:
            if not self.char_isprint(char):
                continue
            if self.is_overwrite:
                if self.readline.l_buffer.point < len(self.readline.l_buffer.line_buffer):
                    self.readline.l_buffer.line_buffer[self.readline.l_buffer.point] = char
                else:
                    self.readline.l_buffer.line_buffer.append(char)
            else:
                self.readline.l_buffer.line_buffer.insert(self.readline.l_buffer.point, char)
            return None

    
    def replace_one(self, char):
        if char == '\x1b':
            self.end()
            return None
        self.is_edit = None
        self.readline.vi_save_line()
        times = self.get_multiplier()
        cursor = self.readline.l_buffer.point
        self.readline.l_buffer.line_buffer[cursor:cursor + times] = char * times
        if times > 1:
            pass
        self.end()

    
    def char_isprint(self, char):
