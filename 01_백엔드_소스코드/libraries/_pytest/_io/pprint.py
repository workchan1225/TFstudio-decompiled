# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pprint.pyc (Python 3.11)

from __future__ import annotations
import collections as _collections
from collections.abc import Callable
from collections.abc import Iterator
import dataclasses as _dataclasses
from io import StringIO as _StringIO
import re
import types as _types
from typing import Any
from typing import IO

class _safe_key:
    '''Helper function for key functions when sorting unorderable objects.

    The wrapped-object will fallback to a Py2.x style comparison for
    unorderable types (sorting first comparing the type name and then by
    the obj ids).  Does not work recursively, so dict.items() must have
    _safe_key applied to both the key and the value.

    '''
    __slots__ = [
        'obj']
    
    def __init__(self, obj):
        self.obj = obj

    
    def __lt__(self, other):
        
        try:
            return self.obj < other.obj
        except TypeError:
            return 




def _safe_tuple(t):
    '''Helper function for comparing 2-tuples'''
    return (_safe_key(t[0]), _safe_key(t[1]))


class PrettyPrinter:
    
    def __init__(self = None, indent = None, width = None, depth = (4, 80, None)):
        '''Handle pretty printing operations onto a stream using a set of
        configured parameters.

        indent
            Number of spaces to indent for each level of nesting.

        width
            Attempted maximum number of columns in the output.

        depth
            The maximum depth to print out nested structures.

        '''
        if indent < 0:
            raise ValueError('indent must be >= 0')
    # WARNING: Decompyle incomplete

    
    def pformat(self = None, object = None):
        sio = _StringIO()
        self._format(object, sio, 0, 0, set(), 0)
        return sio.getvalue()

    
    def _format(self, object, stream, indent = None, allowance = None, context = None, level = ('object', 'Any', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        objid = id(object)
        if objid in context:
            stream.write(_recursion(object))
            return None
        p = None._dispatch.get(type(object).__repr__, None)
    # WARNING: Decompyle incomplete

    
    def _pprint_dataclass(self, object, stream, indent = None, allowance = None, context = None, level = ('object', 'Any', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    _dispatch: 'dict[Callable[..., str], Callable[[PrettyPrinter, Any, IO[str], int, int, set[int], int], None]]' = { }
    
    def _pprint_dict(self, object, stream, indent = None, allowance = None, context = None, level = ('object', 'Any', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        write = stream.write
        write('{')
        items = sorted(object.items(), key = _safe_tuple)
        self._format_dict_items(items, stream, indent, allowance, context, level)
        write('}')

    _dispatch[dict.__repr__] = _pprint_dict
    
    def _pprint_ordered_dict(self, object, stream, indent = None, allowance = None, context = None, level = ('object', 'Any', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        if not len(object):
            stream.write(repr(object))
            return None
        cls = None.__class__
        stream.write(cls.__name__ + '(')
        self._pprint_dict(object, stream, indent, allowance, context, level)
        stream.write(')')

    _dispatch[_collections.OrderedDict.__repr__] = _pprint_ordered_dict
    
    def _pprint_list(self, object, stream, indent = None, allowance = None, context = None, level = ('object', 'Any', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        stream.write('[')
        self._format_items(object, stream, indent, allowance, context, level)
        stream.write(']')

    _dispatch[list.__repr__] = _pprint_list
    
    def _pprint_tuple(self, object, stream, indent = None, allowance = None, context = None, level = ('object', 'Any', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        stream.write('(')
        self._format_items(object, stream, indent, allowance, context, level)
        stream.write(')')

    _dispatch[tuple.__repr__] = _pprint_tuple
    
    def _pprint_set(self, object, stream, indent = None, allowance = None, context = None, level = ('object', 'Any', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        if not len(object):
            stream.write(repr(object))
            return None
        typ = None.__class__
        if typ is set:
            stream.write('{')
            endchar = '}'
        else:
            stream.write(typ.__name__ + '({')
            endchar = '})'
        object = sorted(object, key = _safe_key)
        self._format_items(object, stream, indent, allowance, context, level)
        stream.write(endchar)

    _dispatch[set.__repr__] = _pprint_set
    _dispatch[frozenset.__repr__] = _pprint_set
    
    def _pprint_str(self, object, stream, indent = None, allowance = None, context = None, level = ('object', 'Any', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        write = stream.write
        if not len(object):
            write(repr(object))
            return None
        chunks = None
        lines = object.splitlines(True)
        if level == 1:
            indent += 1
            allowance += 1
        max_width1 = self._width - indent
        max_width = self._width - indent
    # WARNING: Decompyle incomplete

    _dispatch[str.__repr__] = _pprint_str
    
    def _pprint_bytes(self, object, stream, indent = None, allowance = None, context = None, level = ('object', 'Any', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        write = stream.write
        if len(object) <= 4:
            write(repr(object))
            return None
        parens = None == 1
        if parens:
            indent += 1
            allowance += 1
            write('(')
        delim = ''
        for rep in _wrap_bytes_repr(object, self._width - indent, allowance):
            write(delim)
            write(rep)
            if not delim:
                delim = '\n' + ' ' * indent
            if parens:
                write(')')
                return None
            return None

    _dispatch[bytes.__repr__] = _pprint_bytes
    
    def _pprint_bytearray(self, object, stream, indent = None, allowance = None, context = None, level = ('object', 'Any', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        write = stream.write
        write('bytearray(')
        self._pprint_bytes(bytes(object), stream, indent + 10, allowance + 1, context, level + 1)
        write(')')

    _dispatch[bytearray.__repr__] = _pprint_bytearray
    
    def _pprint_mappingproxy(self, object, stream, indent = None, allowance = None, context = None, level = ('object', 'Any', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        stream.write('mappingproxy(')
        self._format(object.copy(), stream, indent, allowance, context, level)
        stream.write(')')

    _dispatch[_types.MappingProxyType.__repr__] = _pprint_mappingproxy
    
    def _pprint_simplenamespace(self, object, stream, indent = None, allowance = None, context = None, level = ('object', 'Any', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        if type(object) is _types.SimpleNamespace:
            cls_name = 'namespace'
        else:
            cls_name = object.__class__.__name__
        items = object.__dict__.items()
        stream.write(cls_name + '(')
        self._format_namespace_items(items, stream, indent, allowance, context, level)
        stream.write(')')

    _dispatch[_types.SimpleNamespace.__repr__] = _pprint_simplenamespace
    
    def _format_dict_items(self, items, stream, indent = None, allowance = None, context = None, level = ('items', 'list[tuple[Any, Any]]', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        if not items:
            return None
        write = None.write
        item_indent = indent + self._indent_per_level
        delimnl = '\n' + ' ' * item_indent
        for key, ent in items:
            write(delimnl)
            write(self._repr(key, context, level))
            write(': ')
            self._format(ent, stream, item_indent, 1, context, level)
            write(',')
            write('\n' + ' ' * indent)
            return None

    
    def _format_namespace_items(self, items, stream, indent = None, allowance = None, context = None, level = ('items', 'list[tuple[Any, Any]]', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        if not items:
            return None
        write = None.write
        item_indent = indent + self._indent_per_level
        delimnl = '\n' + ' ' * item_indent
        for key, ent in items:
            write(delimnl)
            write(key)
            write('=')
            if id(ent) in context:
                write('...')
            else:
                self._format(ent, stream, item_indent + len(key) + 1, 1, context, level)
            write(',')
            write('\n' + ' ' * indent)
            return None

    
    def _format_items(self, items, stream, indent = None, allowance = None, context = None, level = ('items', 'list[Any]', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        if not items:
            return None
        write = None.write
        item_indent = indent + self._indent_per_level
        delimnl = '\n' + ' ' * item_indent
        for item in items:
            write(delimnl)
            self._format(item, stream, item_indent, 1, context, level)
            write(',')
            write('\n' + ' ' * indent)
            return None

    
    def _repr(self = None, object = None, context = None, level = ('object', 'Any', 'context', 'set[int]', 'level', 'int', 'return', 'str')):
        return self._safe_repr(object, context.copy(), self._depth, level)

    
    def _pprint_default_dict(self, object, stream, indent = None, allowance = None, context = None, level = ('object', 'Any', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        rdf = self._repr(object.default_factory, context, level)
        stream.write(f'''{object.__class__.__name__}({rdf}, ''')
        self._pprint_dict(object, stream, indent, allowance, context, level)
        stream.write(')')

    _dispatch[_collections.defaultdict.__repr__] = _pprint_default_dict
    
    def _pprint_counter(self, object, stream, indent = None, allowance = None, context = None, level = ('object', 'Any', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        stream.write(object.__class__.__name__ + '(')
        if object:
            stream.write('{')
            items = object.most_common()
            self._format_dict_items(items, stream, indent, allowance, context, level)
            stream.write('}')
        stream.write(')')

    _dispatch[_collections.Counter.__repr__] = _pprint_counter
    
    def _pprint_chain_map(self, object, stream, indent = None, allowance = None, context = None, level = ('object', 'Any', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        if not (len(object.maps) or len(object.maps) == 1) and len(object.maps[0]):
            stream.write(repr(object))
            return None
        None.write(object.__class__.__name__ + '(')
        self._format_items(object.maps, stream, indent, allowance, context, level)
        stream.write(')')

    _dispatch[_collections.ChainMap.__repr__] = _pprint_chain_map
    
    def _pprint_deque(self, object, stream, indent = None, allowance = None, context = None, level = ('object', 'Any', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        stream.write(object.__class__.__name__ + '(')
    # WARNING: Decompyle incomplete

    _dispatch[_collections.deque.__repr__] = _pprint_deque
    
    def _pprint_user_dict(self, object, stream, indent = None, allowance = None, context = None, level = ('object', 'Any', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        self._format(object.data, stream, indent, allowance, context, level - 1)

    _dispatch[_collections.UserDict.__repr__] = _pprint_user_dict
    
    def _pprint_user_list(self, object, stream, indent = None, allowance = None, context = None, level = ('object', 'Any', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        self._format(object.data, stream, indent, allowance, context, level - 1)

    _dispatch[_collections.UserList.__repr__] = _pprint_user_list
    
    def _pprint_user_string(self, object, stream, indent = None, allowance = None, context = None, level = ('object', 'Any', 'stream', 'IO[str]', 'indent', 'int', 'allowance', 'int', 'context', 'set[int]', 'level', 'int', 'return', 'None')):
        self._format(object.data, stream, indent, allowance, context, level - 1)

    _dispatch[_collections.UserString.__repr__] = _pprint_user_string
    
    def _safe_repr(self, object = None, context = None, maxlevels = None, level = ('object', 'Any', 'context', 'set[int]', 'maxlevels', 'int | None', 'level', 'int', 'return', 'str')):
        typ = type(object)
        if typ in _builtin_scalars:
            return repr(object)
        r = None(typ, '__repr__', None)
        if issubclass(typ, dict) and r is dict.__repr__:
            if not object:
                return '{}'
            objid = None(object)
            if maxlevels and level >= maxlevels:
                return '{...}'
            if None in context:
                return _recursion(object)
            None.add(objid)
            components = []
            append = components.append
            level += 1
            for k, v in sorted(object.items(), key = _safe_tuple):
                krepr = self._safe_repr(k, context, maxlevels, level)
                vrepr = self._safe_repr(v, context, maxlevels, level)
                append(f'''{krepr}: {vrepr}''')
                context.remove(objid)
                return '{{{}}}'.format(', '.join(components))
                if (issubclass(typ, list) or r is list.__repr__ or issubclass(typ, tuple)) and r is tuple.__repr__:
                    if issubclass(typ, list):
                        if not object:
                            return '[]'
                        format = None
                    elif len(object) == 1:
                        format = '(%s,)'
                    elif not object:
                        return '()'
                    format = '(%s)'
                    objid = id(object)
                    if maxlevels and level >= maxlevels:
                        return format % '...'
                    if None in context:
                        return _recursion(object)
                    None.add(objid)
                    components = []
                    append = components.append
                    level += 1
                    for o in object:
                        orepr = self._safe_repr(o, context, maxlevels, level)
                        append(orepr)
                        context.remove(objid)
                        return format % ', '.join(components)
                        return repr(object)


_builtin_scalars = frozenset({
    str,
    bytes,
    bytearray,
    float,
    complex,
    bool,
    type(None),
    int})

def _recursion(object = None):
    return f'''<Recursion on {type(object).__name__} with id={id(object)}>'''


def _wrap_bytes_repr(object = None, width = None, allowance = None):
    pass
# WARNING: Decompyle incomplete
