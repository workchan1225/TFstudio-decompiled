# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _tracing.pyc (Python 3.11)

'''
Tracing utils
'''
from __future__ import annotations
from collections.abc import Sequence
from typing import Any
from typing import Callable
_Writer = Callable[([
    str], object)]
_Processor = Callable[([
    tuple[(str, ...)],
    tuple[(Any, ...)]], object)]

class TagTracer:
    
    def __init__(self = None):
        self._tags2proc = { }
        self._writer = None
        self.indent = 0

    
    def get(self = None, name = None):
        return TagTracerSub(self, (name,))

    
    def _format_message(self = None, tags = None, args = None):
        if isinstance(args[-1], dict):
            extra = args[-1]
            args = args[:-1]
        else:
            extra = { }
        content = ' '.join(map(str, args))
        indent = '  ' * self.indent
        lines = [
            '{}{} [{}]\n'.format(indent, content, ':'.join(tags))]
        for name, value in extra.items():
            lines.append(f'''{indent}    {name}: {value}\n''')
            return ''.join(lines)

    
    def _processmessage(self = None, tags = None, args = None):
        pass
    # WARNING: Decompyle incomplete

    
    def setwriter(self = None, writer = None):
        self._writer = writer

    
    def setprocessor(self = None, tags = None, processor = None):
        if isinstance(tags, str):
            tags = tuple(tags.split(':'))
    # WARNING: Decompyle incomplete



class TagTracerSub:
    
    def __init__(self = None, root = None, tags = None):
        self.root = root
        self.tags = tags

    
    def __call__(self = None, *args):
        self.root._processmessage(self.tags, args)

    
    def get(self = None, name = None):
        return self.__class__(self.root, self.tags + (name,))
