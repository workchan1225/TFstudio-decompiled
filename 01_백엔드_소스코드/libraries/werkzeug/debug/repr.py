# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: repr.pyc (Python 3.11)

'''Object representations for debugging purposes. Unlike the default
repr, these expose more information and produce HTML instead of ASCII.

Together with the CSS and JavaScript of the debugger this gives a
colorful and more compact output.
'''
from __future__ import annotations
import codecs
import re
import sys
import typing as t
from collections import deque
from traceback import format_exception_only
from markupsafe import escape
missing = object()
_paragraph_re = re.compile('(?:\\r\\n|\\r|\\n){2,}')
RegexType = type(_paragraph_re)
HELP_HTML = '<div class=box>\n  <h3>%(title)s</h3>\n  <pre class=help>%(text)s</pre>\n</div>'
OBJECT_DUMP_HTML = '<div class=box>\n  <h3>%(title)s</h3>\n  %(repr)s\n  <table>%(items)s</table>\n</div>'

def debug_repr(obj = None):
    '''Creates a debug repr of an object as HTML string.'''
    return DebugReprGenerator().repr(obj)


def dump(obj = None):
    '''Print the object details to stdout._write (for the interactive
    console of the web debugger.
    '''
    gen = DebugReprGenerator()
    if obj is missing:
        rv = gen.dump_locals(sys._getframe(1).f_locals)
    else:
        rv = gen.dump_object(obj)
    sys.stdout._write(rv)


class _Helper:
    '''Displays an HTML version of the normal help, for the interactive
    debugger only because it requires a patched sys.stdout.
    '''
    
    def __repr__(self = None):
        return 'Type help(object) for help about object.'

    
    def __call__(self = None, topic = None):
        pass
    # WARNING: Decompyle incomplete


helper = _Helper()

def _add_subclass_info(inner = None, obj = None, base = None):
    if isinstance(base, tuple):
        for cls in base:
            if type(obj) is cls:
                
                return None, inner
    if type(obj) is base:
        return inner
    if obj.__class__.__module__ not in ('__builtin__', 'exceptions'):
        f'''<span class="module">{obj.__class__.__module__}.</span>''' = None
    return f'''{module}{type(obj).__name__}({inner})'''


def _sequence_repr_maker(left = None, right = None, base = None, limit = (8,)):
    pass
# WARNING: Decompyle incomplete


class DebugReprGenerator:
    
    def __init__(self = None):
        self._stack = []

    list_repr = _sequence_repr_maker('[', ']', list)
    tuple_repr = _sequence_repr_maker('(', ')', tuple)
    set_repr = _sequence_repr_maker('set([', '])', set)
    frozenset_repr = _sequence_repr_maker('frozenset([', '])', frozenset)
    deque_repr = _sequence_repr_maker('<span class="module">collections.</span>deque([', '])', deque)
    
    def regex_repr(self = None, obj = None):
        pattern = repr(obj.pattern)
        pattern = codecs.decode(pattern, 'unicode-escape', 'ignore')
        pattern = f'''r{pattern}'''
        return f'''re.compile(<span class="string regex">{pattern}</span>)'''

    
    def string_repr(self = None, obj = None, limit = None):
        buf = [
            '<span class="string">']
        r = repr(obj)
        if len(r) - limit > 2:
            buf.extend((escape(r[:limit]), '<span class="extended">', escape(r[limit:]), '</span>'))
        else:
            buf.append(escape(r))
        buf.append('</span>')
        out = ''.join(buf)
        if (r[0] in '\'"' or r[0] == 'b') and r[1] in '\'"':
            return _add_subclass_info(out, obj, (bytes, str))

    
    def dict_repr(self = None, d = None, recursive = None, limit = (5,)):
        if recursive:
            return _add_subclass_info('{...}', d, dict)
        buf = [
            None]
        have_extended_section = False
        for key, value in enumerate(d.items()):
            if idx:
                buf.append(', ')
            if idx == limit - 1:
                buf.append('<span class="extended">')
                have_extended_section = True
            buf.append(f'''<span class="pair"><span class="key">{self.repr(key)}</span>: <span class="value">{self.repr(value)}</span></span>''')
            if have_extended_section:
                buf.append('</span>')
        buf.append('}')
        return _add_subclass_info(''.join(buf), d, dict)

    
    def object_repr(self = None, obj = None):
        r = repr(obj)
        return f'''<span class="object">{escape(r)}</span>'''

    
    def dispatch_repr(self = None, obj = None, recursive = None):
        if obj is helper:
            return f'''<span class="help">{helper!r}</span>'''
        if None(obj, (int, float, complex)):
            return f'''<span class="number">{obj!r}</span>'''
        if None(obj, str) or isinstance(obj, bytes):
            return self.string_repr(obj)
        if None(obj, RegexType):
            return self.regex_repr(obj)
        if None(obj, list):
            return self.list_repr(obj, recursive)
        if None(obj, tuple):
            return self.tuple_repr(obj, recursive)
        if None(obj, set):
            return self.set_repr(obj, recursive)
        if None(obj, frozenset):
            return self.frozenset_repr(obj, recursive)
        if None(obj, dict):
            return self.dict_repr(obj, recursive)
        if None(obj, deque):
            return self.deque_repr(obj, recursive)
        return None.object_repr(obj)

    
    def fallback_repr(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def repr(self = None, obj = None):
        recursive = False
        for item in self._stack:
            if item is obj:
                recursive = True
            
            self._stack.append(obj)
            
            try:
                self._stack.pop()
                return self.dispatch_repr(obj, recursive)
            except Exception:
                
                try:
                    self._stack.pop()
                    return 
                    
                    try:
                        pass
                    except:
                        self._stack.pop()




    
    def dump_object(self = None, obj = None):
        repr = None
        items = None
    # WARNING: Decompyle incomplete

    
    def dump_locals(self = None, d = None):
        pass
    # WARNING: Decompyle incomplete

    
    def render_object_dump(self = None, items = None, title = None, repr = (None,)):
        html_items = []
        for key, value in items:
            html_items.append(f'''<tr><th>{escape(key)}<td><pre class=repr>{value}</pre>''')
            if not html_items:
                html_items.append('<tr><td><em>Nothing</em>')
        return OBJECT_DUMP_HTML % {
            'title': escape(title),
            'repr': f'''<pre class=repr>{repr if repr else ''}</pre>''',
            'items': '\n'.join(html_items) }
