# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rlmain.pyc (Python 3.11)

import os
import re
import sys
import time
from glob import glob
import pyreadline3
from pyreadline3.clipboard import clipboard
from pyreadline3.console import console

history

lineobj
import pyreadline3.logger as logger
import pyreadline3.lineeditor.lineobj, lineeditor
from pyreadline3.keysyms.common import make_KeyPress_from_keydescr
from pyreadline3.py3k_compat import is_ironpython
from pyreadline3.unicode_helper import ensure_str, ensure_unicode
from error import GetSetError, ReadlineError
from logger import log
from modes import editingmodes
from py3k_compat import execfile, is_callable

class MockConsoleError(Exception):
    pass


class MockConsole(object):
    '''object used during refactoring. Should raise errors when someone tries
    to use it.
    '''
    
    def __setattr__(self, _name, _value):
        raise MockConsoleError('Should not try to get attributes from MockConsole')

    
    def cursor(self, size = (50,)):
        pass



class BaseReadline(object):
    
    def __init__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def parse_and_bind(self, string):
        '''Parse and execute single line of a readline init file.'''
        
        try:
            log('parse_and_bind("%s")' % string)
            if string.startswith('#'):
                return None
            if None.startswith('set'):
                m = re.compile('set\\s+([-a-zA-Z0-9]+)\\s+(.+)\\s*$').match(string)
                if m:
                    var_name = m.group(1)
                    val = m.group(2)
                    
                    try:
                        setattr(self.mode, var_name.replace('-', '_'), val)
                        
                        try:
                            pass
                        except AttributeError:
                            log(f'''unknown var="{var_name!s}" val="{val!s}"''')
                            
                            try:
                                pass
                            try:
                                log('bad set "%s"' % string)
                                return None
                                
                                try:
                                    m = re.compile('\\s*(\\S+)\\s*:\\s*([-a-zA-Z]+)\\s*$').match(string)
                                    if m:
                                        key = m.group(1)
                                        func_name = m.group(2)
                                        py_name = func_name.replace('-', '_')
                                        
                                        try:
                                            func = getattr(self.mode, py_name)
                                            
                                            try:
                                                pass
                                            except AttributeError:
                                                log(f'''unknown func key="{key!s}" func="{func_name!s}"''')
                                                if self.debug:
                                                    print('pyreadline3 parse_and_bind error, unknown function to bind: "%s"' % func_name)
                                                    
                                                    try:
                                                        return None
                                                        
                                                        try:
                                                            self.mode._bind_key(key, func)
                                                            return None
                                                            return None
                                                        except BaseException:
                                                            log('error')
                                                            raise 










    
    def _set_prompt(self, prompt):
        self.mode.prompt = prompt

    
    def _get_prompt(self):
        return self.mode.prompt

    prompt = property(_get_prompt, _set_prompt)
    
    def get_line_buffer(self):
        '''Return the current contents of the line buffer.'''
        return self.mode.l_buffer.get_line_text()

    
    def insert_text(self, string):
        '''Insert text into the command line.'''
        self.mode.insert_text(string)

    
    def read_init_file(self, filename = (None,)):
        '''Parse a readline initialization file. The default filename is the last filename used.'''
        log('read_init_file("%s")' % filename)

    
    def add_history(self, line):
        '''Append a line to the history buffer, as if it was the last line typed.'''
        self.mode._history.add_history(line)

    
    def get_current_history_length(self):
        '''Return the number of lines currently in the history.
        (This is different from get_history_length(), which returns
        the maximum number of lines that will be written to a history file.)'''
        return self.mode._history.get_current_history_length()

    
    def get_history_length(self):
        '''Return the desired length of the history file.

        Negative values imply unlimited history file size.'''
        return self.mode._history.get_history_length()

    
    def set_history_length(self, length):
        '''Set the number of lines to save in the history file.

        write_history_file() uses this value to truncate the history file
        when saving. Negative values imply unlimited history file size.
        '''
        self.mode._history.set_history_length(length)

    
    def get_history_item(self, index):
        '''Return the current contents of history item at index.'''
        return self.mode._history.get_history_item(index)

    
    def clear_history(self):
        '''Clear readline history'''
        self.mode._history.clear_history()

    
    def read_history_file(self, filename = (None,)):
        '''Load a readline history file. The default filename is ~/.history.'''
        pass
    # WARNING: Decompyle incomplete

    
    def write_history_file(self, filename = (None,)):
        '''Save a readline history file. The default filename is ~/.history.'''
        self.mode._history.write_history_file(filename)

    
    def set_completer(self, function = (None,)):
        '''Set or remove the completer function.

        If function is specified, it will be used as the new completer
        function; if omitted or None, any completer function already
        installed is removed. The completer function is called as
        function(text, state), for state in 0, 1, 2, ..., until it returns a
        non-string value. It should return the next possible completion
        starting with text.
        '''
        log('set_completer')
        self.mode.completer = function

    
    def get_completer(self):
        '''Get the completer function.'''
        log('get_completer')
        return self.mode.completer

    
    def get_begidx(self):
        '''Get the beginning index of the readline tab-completion scope.'''
        return self.mode.begidx

    
    def get_endidx(self):
        '''Get the ending index of the readline tab-completion scope.'''
        return self.mode.endidx

    
    def set_completer_delims(self, string):
        '''Set the readline word delimiters for tab-completion.'''
        self.mode.completer_delims = string

    
    def get_completer_delims(self):
        '''Get the readline word delimiters for tab-completion.'''
        return self.mode.completer_delims

    
    def set_startup_hook(self, function = (None,)):
        '''Set or remove the startup_hook function.

        If function is specified, it will be used as the new startup_hook
        function; if omitted or None, any hook function already installed is
        removed. The startup_hook function is called with no arguments just
        before readline prints the first prompt.

        '''
        self.mode.startup_hook = function

    
    def set_pre_input_hook(self, function = (None,)):
        '''Set or remove the pre_input_hook function.

        If function is specified, it will be used as the new pre_input_hook
        function; if omitted or None, any hook function already installed is
        removed. The pre_input_hook function is called with no arguments
        after the first prompt has been printed and just before readline
        starts reading input characters.

        '''
        self.mode.pre_input_hook = function

    
    def _bell(self):
        pass

    
    def readline(self, prompt = ('',)):
        raise NotImplementedError

    
    def process_keyevent(self, keyinfo):
        return self.mode.process_keyevent(keyinfo)

    
    def readline_setup(self, prompt = ('',)):
        return self.mode.readline_setup(prompt)

    
    def keyboard_poll(self):
        return self.mode._readline_from_keyboard_poll()

    
    def callback_handler_install(self, prompt, callback):
        '''bool readline_callback_handler_install ( string prompt, callback callback)
        Initializes the readline callback interface and terminal, prints the prompt and returns immediately
        '''
        self.callback = callback
        self.readline_setup(prompt)

    
    def callback_handler_remove(self):
        '''Removes a previously installed callback handler and restores terminal settings'''
        self.callback = None

    
    def callback_read_char(self):
        '''Reads a character and informs the readline callback interface when a line is received'''
        if self.keyboard_poll():
            line = self.get_line_buffer() + '\n'
            self.add_history(self.mode.l_buffer)
            self.callback(line)
            return None

    
    def read_inputrc(self, inputrcpath = (os.path.expanduser(ensure_str('~/pyreadlineconfig.ini')),)):
        pass
    # WARNING: Decompyle incomplete

    
    def redisplay(self):
        pass



class Readline(BaseReadline):
    pass
# WARNING: Decompyle incomplete
