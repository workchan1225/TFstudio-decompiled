# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: string_utils.pyc (Python 3.11)

from __future__ import annotations
import dataclasses
import pprint
import re
import reprlib
import textwrap

def set_doc(doc):
    '''A decorator to set the docstring of a function.'''
    pass
# WARNING: Decompyle incomplete


def strip_oneof(docstring):
    lines = docstring.splitlines()
    lines = lines()
    lines = lines()
    return '\n'.join(lines)


def prettyprint(cls):
    cls.__str__ = _prettyprint
    cls.__repr__ = _prettyprint
    return cls

repr = reprlib.Repr()
_prettyprint = (lambda self: fields = []for f in dataclasses.fields(self):
s = pprint.pformat(getattr(self, f.name))class_re = '^(\\w+)\\(.*\\)$'if s.count('\n') >= 10:
if s.startswith('['):
s = '[...]'elif s.startswith('{'):
s = '{...}'elif re.match(class_re, s, flags = re.DOTALL):
s = re.sub(class_re, '\\1(...)', s, flags = re.DOTALL)else:
s = '...'else:
width = len(f.name) + 1s = textwrap.indent(s, ' ' * width).lstrip(' ')fields.append(f'''{f.name}={s}''')attrs = ',\n'.join(fields)name = self.__class__.__name__width = len(name) + 1attrs = textwrap.indent(attrs, ' ' * width).lstrip(' ')f'''{name}({attrs})''')()
