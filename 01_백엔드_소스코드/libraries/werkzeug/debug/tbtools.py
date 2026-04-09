# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tbtools.pyc (Python 3.11)

from __future__ import annotations
import itertools
import linecache
import os
import re
import sys
import sysconfig
import traceback
import typing as t
from markupsafe import escape
from utils import cached_property
from console import Console
HEADER = '<!doctype html>\n<html lang=en>\n  <head>\n    <title>%(title)s // Werkzeug Debugger</title>\n    <link rel="stylesheet" href="?__debugger__=yes&amp;cmd=resource&amp;f=style.css">\n    <link rel="shortcut icon"\n        href="?__debugger__=yes&amp;cmd=resource&amp;f=console.png">\n    <script src="?__debugger__=yes&amp;cmd=resource&amp;f=debugger.js"></script>\n    <script>\n      var CONSOLE_MODE = %(console)s,\n          EVALEX = %(evalex)s,\n          EVALEX_TRUSTED = %(evalex_trusted)s,\n          SECRET = "%(secret)s";\n    </script>\n  </head>\n  <body style="background-color: #fff">\n    <div class="debugger">\n'
FOOTER = '      <div class="footer">\n        Brought to you by <strong class="arthur">DON\'T PANIC</strong>, your\n        friendly Werkzeug powered traceback interpreter.\n      </div>\n    </div>\n\n    <div class="pin-prompt">\n      <div class="inner">\n        <h3>Console Locked</h3>\n        <p>\n          The console is locked and needs to be unlocked by entering the PIN.\n          You can find the PIN printed out on the standard output of your\n          shell that runs the server.\n        <form>\n          <p>PIN:\n            <input type=text name=pin size=14>\n            <input type=submit name=btn value="Confirm Pin">\n        </form>\n      </div>\n    </div>\n  </body>\n</html>\n'
PAGE_HTML = HEADER + '<h1>%(exception_type)s</h1>\n<div class="detail">\n  <p class="errormsg">%(exception)s</p>\n</div>\n<h2 class="traceback">Traceback <em>(most recent call last)</em></h2>\n%(summary)s\n<div class="plain">\n    <p>\n      This is the Copy/Paste friendly version of the traceback.\n    </p>\n    <textarea cols="50" rows="10" name="code" readonly>%(plaintext)s</textarea>\n</div>\n<div class="explanation">\n  The debugger caught an exception in your WSGI application.  You can now\n  look at the traceback which led to the error.  <span class="nojavascript">\n  If you enable JavaScript you can also use additional features such as code\n  execution (if the evalex feature is enabled), automatic pasting of the\n  exceptions and much more.</span>\n</div>\n' + FOOTER + '\n<!--\n\n%(plaintext_cs)s\n\n-->\n'
CONSOLE_HTML = HEADER + '<h1>Interactive Console</h1>\n<div class="explanation">\nIn this console you can execute Python expressions in the context of the\napplication.  The initial namespace was created by the debugger automatically.\n</div>\n<div class="console"><div class="inner">The Console requires JavaScript.</div></div>\n' + FOOTER
SUMMARY_HTML = '<div class="%(classes)s">\n  %(title)s\n  <ul>%(frames)s</ul>\n  %(description)s\n</div>\n'
FRAME_HTML = '<div class="frame" id="frame-%(id)d">\n  <h4>File <cite class="filename">"%(filename)s"</cite>,\n      line <em class="line">%(lineno)s</em>,\n      in <code class="function">%(function_name)s</code></h4>\n  <div class="source %(library)s">%(lines)s</div>\n</div>\n'

def _process_traceback(exc = None, te = None, *, skip, hide):
    pass
# WARNING: Decompyle incomplete


class DebugTraceback:
    __slots__ = ('_te', '_cache_all_tracebacks', '_cache_all_frames')
    
    def __init__(self = None, exc = None, te = None, *, skip, hide):
        self._te = _process_traceback(exc, te, skip = skip, hide = hide)

    
    def __str__(self = None):
        return f'''<{type(self).__name__} {self._te}>'''

    all_tracebacks = (lambda self = None: out = []current = self._te# WARNING: Decompyle incomplete
)()
    all_frames = (lambda self = None: self.all_tracebacks())()
    
    def render_traceback_text(self = None):
        return ''.join(self._te.format())

    
    def render_traceback_html(self = None, include_title = None):
        library_frames = self.all_frames()
        [] = None if  < 0, sum(library_frames) else (lambda .0: [ f.is_library for f in .0 ]), 0, sum(library_frames) < len(library_frames)
        if not library_frames:
            classes = 'traceback noframe-traceback'
    # WARNING: Decompyle incomplete

    
    def render_debugger_html(self = None, evalex = None, secret = None, evalex_trusted = ('evalex', 'bool', 'secret', 'str', 'evalex_trusted', 'bool', 'return', 'str')):
        exc_lines = list(self._te.format_exception_only())
        plaintext = ''.join(self._te.format())
        if sys.version_info < (3, 13):
            exc_type_str = self._te.exc_type.__name__
        else:
            exc_type_str = self._te.exc_type_str
        return PAGE_HTML % {
            'evalex': 'true' if evalex else 'false',
            'evalex_trusted': 'true' if evalex_trusted else 'false',
            'console': 'false',
            'title': escape(exc_lines[0]),
            'exception': escape(''.join(exc_lines)),
            'exception_type': escape(exc_type_str),
            'summary': self.render_traceback_html(include_title = False),
            'plaintext': escape(plaintext),
            'plaintext_cs': re.sub('-{2,}', '-', plaintext),
            'secret': secret }



class DebugFrameSummary(traceback.FrameSummary):
    pass
# WARNING: Decompyle incomplete


def render_console_html(secret = None, evalex_trusted = None):
    return CONSOLE_HTML % {
        'evalex': 'true',
        'evalex_trusted': 'true' if evalex_trusted else 'false',
        'console': 'true',
        'title': 'Console',
        'secret': secret }
