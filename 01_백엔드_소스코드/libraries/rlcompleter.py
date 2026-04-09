# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rlcompleter.pyc (Python 3.11)

'''Word completion for GNU readline.

The completer completes keywords, built-ins and globals in a selectable
namespace (which defaults to __main__); when completing NAME.NAME..., it
evaluates (!) the expression up to the last dot and completes its attributes.

It\'s very cool to do "import sys" type "sys.", hit the completion key (twice),
and see the list of names defined by the sys module!

Tip: to use the tab key as the completion key, call

    readline.parse_and_bind("tab: complete")

Notes:

- Exceptions raised by the completer function are *ignored* (and generally cause
  the completion to fail).  This is a feature -- since readline sets the tty
  device in raw (or cbreak) mode, printing a traceback wouldn\'t work well
  without some complicated hoopla to save, reset and restore the tty state.

- The evaluation of the NAME.NAME... form may cause arbitrary application
  defined code to be executed if an object with a __getattr__ hook is found.
  Since it is the responsibility of the application (or the user) to enable this
  feature, I consider this an acceptable risk.  More complicated expressions
  (e.g. function calls or indexing operations) are *not* evaluated.

- When the original stdin is not a tty device, GNU readline is never
  used, and this module (and the readline module) are silently inactive.

'''
import atexit
import builtins
import inspect
import keyword
import re
import __main__
__all__ = [
    'Completer']

class Completer:
    
    def __init__(self, namespace = (None,)):
        '''Create a new completer for the command line.

        Completer([namespace]) -> completer instance.

        If unspecified, the default namespace where completions are performed
        is __main__ (technically, __main__.__dict__). Namespaces should be
        given as dictionaries.

        Completer instances should be used as the completion mechanism of
        readline via the set_completer() call:

        readline.set_completer(Completer(my_namespace).complete)
        '''
        if not namespace and isinstance(namespace, dict):
            raise TypeError('namespace must be a dictionary')
    # WARNING: Decompyle incomplete

    
    def complete(self, text, state):
        """Return the next possible completion for 'text'.

        This is called successively with state == 0, 1, 2, ... until it
        returns None.  The completion should begin with 'text'.

        """
        if self.use_main_ns:
            self.namespace = __main__.__dict__
        if not text.strip():
            if state == 0:
                if _readline_available:
                    readline.insert_text('\t')
                    readline.redisplay()
                    return ''
                return None
            return None
        if None == 0:
            if '.' in text:
                self.matches = self.attr_matches(text)
            else:
                self.matches = self.global_matches(text)
        
        try:
            return self.matches[state]
        except IndexError:
            return None


    
    def _callable_postfix(self, val, word):
