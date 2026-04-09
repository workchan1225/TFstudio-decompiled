# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import railroad
import pyparsing
import typing
from typing import List, NamedTuple, Generic, TypeVar, Dict, Callable, Set, Iterable
from jinja2 import Template
from io import StringIO
import inspect
jinja2_template_source = '<!DOCTYPE html>\n<html>\n<head>\n    {% if not head %}\n        <style type="text/css">\n            .railroad-heading {\n                font-family: monospace;\n            }\n        </style>\n    {% else %}\n        {{ head | safe }}\n    {% endif %}\n</head>\n<body>\n{{ body | safe }}\n{% for diagram in diagrams %}\n    <div class="railroad-group">\n        <h1 class="railroad-heading">{{ diagram.title }}</h1>\n        <div class="railroad-description">{{ diagram.text }}</div>\n        <div class="railroad-svg">\n            {{ diagram.svg }}\n        </div>\n    </div>\n{% endfor %}\n</body>\n</html>\n'
template = Template(jinja2_template_source)
NamedDiagram = NamedTuple('NamedDiagram', [
    ('name', str),
    ('diagram', typing.Optional[railroad.DiagramItem]),
    ('index', int)])
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
    
    def __init__(self = None, func = None, args = None, kwargs = ('func', Callable[(..., T)], 'args', list, 'kwargs', dict)):
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

def railroad_to_html(diagrams = None, **kwargs):
    '''
    Given a list of NamedDiagram, produce a single HTML string that visualises those diagrams
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


def to_railroad(element = None, diagram_kwargs = None, vertical = None, show_results_names = (None, 3, False, False), show_groups = ('element', pyparsing.ParserElement, 'diagram_kwargs', typing.Optional[dict], 'vertical', int, 'show_results_names', bool, 'show_groups', bool, 'return', List[NamedDiagram])):
    '''
    Convert a pyparsing element tree into a list of diagrams. This is the recommended entrypoint to diagram
    creation if you want to access the Railroad tree before it is converted to HTML
    :param element: base element of the parser being diagrammed
    :param diagram_kwargs: kwargs to pass to the Diagram() constructor
    :param vertical: (optional) - int - limit at which number of alternatives should be
       shown vertically instead of horizontally
    :param show_results_names - bool to indicate whether results name annotations should be
       included in the diagram
    :param show_groups - bool to indicate whether groups should be highlighted with an unlabeled
       surrounding box
    '''
    if not diagram_kwargs:
        lookup = ConverterState(diagram_kwargs = { })
        _to_diagram_element(element, lookup = lookup, parent = None, vertical = vertical, show_results_names = show_results_names, show_groups = show_groups)
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


class ElementState:
    '''
    State recorded for an individual pyparsing Element
    '''
    
    def __init__(self, element, converted = None, parent = None, number = None, name = (None, None), parent_index = ('element', pyparsing.ParserElement, 'converted', EditablePartial, 'parent', EditablePartial, 'number', int, 'name', str, 'parent_index', typing.Optional[int])):
        self.element = element
        self.name = name
        self.converted = converted
        self.parent = parent
        self.number = number
        self.parent_index = parent_index
        self.extract = False
        self.complete = False

    
    def mark_for_extraction(self = None, el_id = None, state = None, name = (None, False), force = ('el_id', int, 'state', 'ConverterState', 'name', str, 'force', bool)):
        """
        Called when this instance has been seen twice, and thus should eventually be extracted into a sub-diagram
        :param el_id: id of the element
        :param state: element/diagram state tracker
        :param name: name to use for this element's text
        :param force: If true, force extraction now, regardless of the state of this. Only useful for extracting the
        root element when we know we're finished
        """
        self.extract = True
        if not self.name:
            if name:
                self.name = name
            elif self.element.customName:
                self.name = self.element.customName
            else:
                self.name = ''
        if force or self.complete or _worth_extracting(self.element):
            state.extract_into_diagram(el_id)
            return None
        return None



class ConverterState:
    '''
    Stores some state that persists between recursions into the element tree
    '''
    
    def __init__(self = None, diagram_kwargs = None):
