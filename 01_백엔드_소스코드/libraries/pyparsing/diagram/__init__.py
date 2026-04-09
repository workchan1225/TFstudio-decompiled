# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import annotations
import itertools
import railroad
import pyparsing
import dataclasses
import typing
from typing import Generic, TypeVar, Callable, Iterable
from jinja2 import Template
from io import StringIO
import inspect
import re
jinja2_template_source = '{% if not embed %}\n<!DOCTYPE html>\n<html>\n<head>\n{% endif %}\n    {% if not head %}\n        <style>\n            .railroad-heading {\n                font-family: monospace;\n            }\n        </style>\n    {% else %}\n        {{ head | safe }}\n    {% endif %}\n{% if not embed %}\n</head>\n<body>\n{% endif %}\n<meta charset="UTF-8"/>\n{{ body | safe }}\n{% for diagram in diagrams %}\n    <div class="railroad-group">\n        <h1 class="railroad-heading" id="{{ diagram.bookmark }}">{{ diagram.title }}</h1>\n        <div class="railroad-description">{{ diagram.text }}</div>\n        <div class="railroad-svg">\n            {{ diagram.svg }}\n        </div>\n    </div>\n{% endfor %}\n{% if not embed %}\n</body>\n</html>\n{% endif %}\n'
template = Template(jinja2_template_source)
_bookmark_lookup = { }
_bookmark_ids = itertools.count(start = 1)

def _make_bookmark(s = None):
    '''
    Converts a string into a valid HTML bookmark (ID or anchor name).
    '''
    if s in _bookmark_lookup:
        return _bookmark_lookup[s]
    bookmark = None.sub('[^a-zA-Z0-9-]+', '-', s)
    if not bookmark[:1].isalpha():
        bookmark = f'''z{bookmark}'''
    bookmark = bookmark.lower().strip('-')
    _bookmark_lookup[s] = f'''{bookmark}-{next(_bookmark_ids):04d}'''
    bookmark = f'''{bookmark}-{next(_bookmark_ids):04d}'''
    return bookmark


def _collapse_verbose_regex(regex_str = None):
    if '\n' not in regex_str:
        return regex_str
    collapsed = None.Regex('#.*$').suppress().transform_string(regex_str)
    collapsed = re.sub('\\s*\\n\\s*', '', collapsed)
    return collapsed

NamedDiagram = <NODE:12>()
T = TypeVar('T')

class EachItem(railroad.Group):
    pass
# WARNING: Decompyle incomplete


class AnnotatedItem(railroad.Group):
    pass
# WARNING: Decompyle incomplete


def EditablePartial():
    '''EditablePartial'''
    __doc__ = "\n    Acts like a functools.partial, but can be edited. In other words, it represents a type that hasn't yet been\n    constructed.\n    "
    
    def __init__(self = None, func = None, args = None, kwargs = ('func', 'Callable[..., T]', 'args', 'list', 'kwargs', 'dict', 'return', 'None')):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    from_call = (lambda cls = None, func = None: EditablePartial(func = func, args = list(args), kwargs = kwargs))()
    name = (lambda self: self.kwargs['name'])()
    
    def __call__(self = None):
        '''
        Evaluate the partial and return the result
        '''
        args = self.args.copy()
        kwargs = self.kwargs.copy()
        arg_spec = inspect.getfullargspec(self.func)
        if arg_spec.varargs in self.kwargs:
            args += kwargs.pop(arg_spec.varargs)
    # WARNING: Decompyle incomplete


EditablePartial = <NODE:27>(EditablePartial, 'EditablePartial', Generic[T])

def railroad_to_html(diagrams = dataclasses.dataclass, embed = None, **kwargs):
    '''
    Given a list of :class:`NamedDiagram`, produce a single HTML string
    that visualises those diagrams.

    :params kwargs: kwargs to be passed in to the template
    '''
    data = []
# WARNING: Decompyle incomplete


def resolve_partial(partial = None):
    '''
    Recursively resolves a collection of Partials into whatever type they are
    '''
    if isinstance(partial, EditablePartial):
        partial.args = resolve_partial(partial.args)
        partial.kwargs = resolve_partial(partial.kwargs)
        return partial()
    if None(partial, list):
        return partial()
    if None(partial, dict):
        return partial.items()()


def to_railroad(element, diagram_kwargs = None, vertical = None, show_results_names = None, show_groups = (None, 3, False, False, False), show_hidden = ('element', 'pyparsing.ParserElement', 'diagram_kwargs', 'typing.Optional[dict]', 'vertical', 'int', 'show_results_names', 'bool', 'show_groups', 'bool', 'show_hidden', 'bool', 'return', 'list[NamedDiagram]')):
    '''
    Convert a pyparsing element tree into a list of diagrams. This is the recommended entrypoint to diagram
    creation if you want to access the Railroad tree before it is converted to HTML

    :param element: base element of the parser being diagrammed

    :param diagram_kwargs: kwargs to pass to the :meth:`Diagram` constructor

    :param vertical: (optional) int - limit at which number of alternatives
        should be shown vertically instead of horizontally

    :param show_results_names: bool to indicate whether results name
        annotations should be included in the diagram

    :param show_groups: bool to indicate whether groups should be highlighted
        with an unlabeled surrounding box

    :param show_hidden: bool to indicate whether internal elements that are
        typically hidden should be shown
    '''
    if not diagram_kwargs:
        lookup = ConverterState(diagram_kwargs = { })
        _to_diagram_element(element, lookup = lookup, parent = None, vertical = vertical, show_results_names = show_results_names, show_groups = show_groups, show_hidden = show_hidden)
        root_id = id(element)
        if root_id in lookup:
            if not element.customName:
                lookup[root_id].name = ''
            lookup[root_id].mark_for_extraction(root_id, lookup, force = True)
    diags = list(lookup.diagrams.values())
# WARNING: Decompyle incomplete


def _should_vertical(specification = None, exprs = None):
    '''
    Returns true if we should return a vertical list of elements
    '''
    pass
# WARNING: Decompyle incomplete

ElementState = <NODE:12>()

class ConverterState:
    '''
    Stores some state that persists between recursions into the element tree
    '''
    
    def __init__(self = None, diagram_kwargs = None):
