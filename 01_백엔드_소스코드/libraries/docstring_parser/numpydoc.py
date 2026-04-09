# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: numpydoc.pyc (Python 3.11)

'''Numpydoc-style docstring parsing.

:see: https://numpydoc.readthedocs.io/en/latest/format.html
'''
import inspect
import itertools
import re
import typing as T
from textwrap import dedent
from common import Docstring, DocstringDeprecated, DocstringExample, DocstringMeta, DocstringParam, DocstringRaises, DocstringReturns, DocstringStyle, RenderingStyle

def _pairwise(iterable = None, end = None):
    (left, right) = itertools.tee(iterable)
    next(right, None)
    return itertools.zip_longest(left, right, fillvalue = end)


def _clean_str(string = None):
    string = string.strip()
    if len(string) > 0:
        return string

KV_REGEX = re.compile('^[^\\s].*$', flags = re.M)
PARAM_KEY_REGEX = re.compile('^(?P<name>.*?)(?:\\s*:\\s*(?P<type>.*?))?$')
PARAM_OPTIONAL_REGEX = re.compile('(?P<type>.*?)(?:, optional|\\(optional\\))$')
PARAM_DEFAULT_REGEX = re.compile('(?<!\\S)[Dd]efault(?: is | = |: |s to |)\\s*(?P<value>[\\w\\-\\.]*\\w)')
RETURN_KEY_REGEX = re.compile('^(?:(?P<name>.*?)\\s*:\\s*)?(?P<type>.*?)$')

class Section:
    '''Numpydoc section parser.

    :param title: section title. For most sections, this is a heading like
                  "Parameters" which appears on its own line, underlined by
                  en-dashes (\'-\') on the following line.
    :param key: meta key string. In the parsed ``DocstringMeta`` instance this
                will be the first element of the ``args`` attribute list.
    '''
    
    def __init__(self = None, title = None, key = None):
        self.title = title
        self.key = key

    title_pattern = (lambda self = None: dashes = '-' * len(self.title)f'''^({self.title})\\s*?\\n{dashes}\\s*$''')()
    
    def parse(self = None, text = None):
        '''Parse ``DocstringMeta`` objects from the body of this section.

        :param text: section body text. Should be cleaned with
                     ``inspect.cleandoc`` before parsing.
        '''
        pass
    # WARNING: Decompyle incomplete



class _KVSection(Section):
    '''Base parser for numpydoc sections with key-value syntax.

    E.g. sections that look like this:
        key
            value
        key2 : type
            values can also span...
            ... multiple lines
    '''
    
    def _parse_item(self = None, key = None, value = None):
        pass

    
    def parse(self = None, text = None):
        pass
    # WARNING: Decompyle incomplete



class _SphinxSection(Section):
    '''Base parser for numpydoc sections with sphinx-style syntax.

    E.g. sections that look like this:
        .. title:: something
            possibly over multiple lines
    '''
    title_pattern = (lambda self = None: f'''^\\.\\.\\s*({self.title})\\s*::''')()


class ParamSection(_KVSection):
    '''Parser for numpydoc parameter sections.

    E.g. any section that looks like this:
        arg_name
            arg_description
        arg_2 : type, optional
            descriptions can also span...
            ... multiple lines
    '''
    
    def _parse_item(self = None, key = None, value = None):
        match = PARAM_KEY_REGEX.match(key)
        arg_name = None
        type_name = None
        is_optional = None
    # WARNING: Decompyle incomplete



class RaisesSection(_KVSection):
    '''Parser for numpydoc raises sections.

    E.g. any section that looks like this:
        ValueError
            A description of what might raise ValueError
    '''
    
    def _parse_item(self = None, key = None, value = None):
        return DocstringRaises(args = [
            self.key,
            key], description = _clean_str(value), type_name = key if len(key) > 0 else None)



class ReturnsSection(_KVSection):
    '''Parser for numpydoc returns sections.

    E.g. any section that looks like this:
        return_name : type
            A description of this returned value
        another_type
            Return names are optional, types are required
    '''
    is_generator = False
    
    def _parse_item(self = None, key = None, value = None):
        match = RETURN_KEY_REGEX.match(key)
    # WARNING: Decompyle incomplete



class YieldsSection(ReturnsSection):
    '''Parser for numpydoc generator "yields" sections.'''
    is_generator = True


class DeprecationSection(_SphinxSection):
    '''Parser for numpydoc "deprecation warning" sections.'''
    
    def parse(self = None, text = None):
        pass
    # WARNING: Decompyle incomplete



class ExamplesSection(Section):
    '''Parser for numpydoc examples sections.

    E.g. any section that looks like this:
        >>> import numpy.matlib
        >>> np.matlib.empty((2, 2))    # filled with random data
        matrix([[  6.76425276e-320,   9.79033856e-307], # random
                [  7.39337286e-309,   3.22135945e-309]])
        >>> np.matlib.empty((2, 2), dtype=int)
        matrix([[ 6600475,        0], # random
                [ 6586976, 22740995]])
    '''
    
    def parse(self = None, text = None):
        '''Parse ``DocstringExample`` objects from the body of this section.

        :param text: section body text. Should be cleaned with
                     ``inspect.cleandoc`` before parsing.
        '''
        pass
    # WARNING: Decompyle incomplete


DEFAULT_SECTIONS = [][ParamSection('Parameters', 'param')][ParamSection('Params', 'param')][ParamSection('Arguments', 'param')][ParamSection('Args', 'param')][ParamSection('Other Parameters', 'other_param')][ParamSection('Other Params', 'other_param')][ParamSection('Other Arguments', 'other_param')][ParamSection('Other Args', 'other_param')][ParamSection('Receives', 'receives')][ParamSection('Receive', 'receives')][RaisesSection('Raises', 'raises')][RaisesSection('Raise', 'raises')][RaisesSection('Warns', 'warns')][RaisesSection('Warn', 'warns')][ParamSection('Attributes', 'attribute')][ParamSection('Attribute', 'attribute')][ReturnsSection('Returns', 'returns')][ReturnsSection('Return', 'returns')][YieldsSection('Yields', 'yields')][YieldsSection('Yield', 'yields')][ExamplesSection('Examples', 'examples')][ExamplesSection('Example', 'examples')][Section('Warnings', 'warnings')][Section('Warning', 'warnings')][Section('See Also', 'see_also')][Section('Related', 'see_also')][Section('Notes', 'notes')][Section('Note', 'notes')][Section('References', 'references')][Section('Reference', 'references')][DeprecationSection('deprecated', 'deprecation')]

class NumpydocParser:
    '''Parser for numpydoc-style docstrings.'''
    
    def __init__(self = None, sections = None):
        '''Setup sections.

        :param sections: Recognized sections or None to defaults.
        '''
        if not sections:
            pass
        sections = DEFAULT_SECTIONS
        self.sections = sections()
        self._setup()

    
    def _setup(self):
        self.titles_re = '|'.join((lambda .0: pass# WARNING: Decompyle incomplete
)(self.sections.values()()), flags = re.M)

    
    def add_section(self = None, section = None):
        '''Add or replace a section.

        :param section: The new section.
        '''
        self.sections[section.title] = section
        self._setup()

    
    def parse(self = None, text = None):
        '''Parse the numpy-style docstring into its components.

        :returns: parsed docstring
        '''
        ret = Docstring(style = DocstringStyle.NUMPYDOC)
        if not text:
            return ret
        text = None.cleandoc(text)
        match = self.titles_re.search(text)
        if match:
            desc_chunk = None[text:match.start()]
            meta_chunk = text[match.start():]
        else:
            desc_chunk = text
            meta_chunk = ''
        parts = desc_chunk.split('\n', 1)
    # WARNING: Decompyle incomplete



def parse(text = [][ParamSection('Parameters', 'param')][ParamSection('Params', 'param')][ParamSection('Arguments', 'param')][ParamSection('Args', 'param')][ParamSection('Other Parameters', 'other_param')][ParamSection('Other Params', 'other_param')][ParamSection('Other Arguments', 'other_param')][ParamSection('Other Args', 'other_param')][ParamSection('Receives', 'receives')][ParamSection('Receive', 'receives')][RaisesSection('Raises', 'raises')][RaisesSection('Raise', 'raises')][RaisesSection('Warns', 'warns')][RaisesSection('Warn', 'warns')][ParamSection('Attributes', 'attribute')][ParamSection('Attribute', 'attribute')][ReturnsSection('Returns', 'returns')][ReturnsSection('Return', 'returns')][YieldsSection('Yields', 'yields')][YieldsSection('Yield', 'yields')][ExamplesSection('Examples', 'examples')][ExamplesSection('Example', 'examples')][Section('Warnings', 'warnings')][Section('Warning', 'warnings')][Section('See Also', 'see_also')][Section('Related', 'see_also')][Section('Notes', 'notes')][Section('Note', 'notes')][Section('References', 'references')]):
    '''Parse the numpy-style docstring into its components.

    :returns: parsed docstring
    '''
    return NumpydocParser().parse(text)


def compose(docstring = [][ParamSection('Parameters', 'param')][ParamSection('Params', 'param')][ParamSection('Arguments', 'param')][ParamSection('Args', 'param')][ParamSection('Other Parameters', 'other_param')][ParamSection('Other Params', 'other_param')][ParamSection('Other Arguments', 'other_param')][ParamSection('Other Args', 'other_param')][ParamSection('Receives', 'receives')][ParamSection('Receive', 'receives')][RaisesSection('Raises', 'raises')][RaisesSection('Raise', 'raises')][RaisesSection('Warns', 'warns')][RaisesSection('Warn', 'warns')][ParamSection('Attributes', 'attribute')][ParamSection('Attribute', 'attribute')][ReturnsSection('Returns', 'returns')][ReturnsSection('Return', 'returns')][YieldsSection('Yields', 'yields')][YieldsSection('Yield', 'yields')][ExamplesSection('Examples', 'examples')][ExamplesSection('Example', 'examples')][Section('Warnings', 'warnings')][Section('Warning', 'warnings')][Section('See Also', 'see_also')][Section('Related', 'see_also')], rendering_style = [][ParamSection('Parameters', 'param')][ParamSection('Params', 'param')][ParamSection('Arguments', 'param')][ParamSection('Args', 'param')][ParamSection('Other Parameters', 'other_param')][ParamSection('Other Params', 'other_param')][ParamSection('Other Arguments', 'other_param')][ParamSection('Other Args', 'other_param')][ParamSection('Receives', 'receives')][ParamSection('Receive', 'receives')][RaisesSection('Raises', 'raises')][RaisesSection('Raise', 'raises')][RaisesSection('Warns', 'warns')][RaisesSection('Warn', 'warns')][ParamSection('Attributes', 'attribute')][ParamSection('Attribute', 'attribute')][ReturnsSection('Returns', 'returns')][ReturnsSection('Return', 'returns')][YieldsSection('Yields', 'yields')][YieldsSection('Yield', 'yields')][ExamplesSection('Examples', 'examples')][ExamplesSection('Example', 'examples')][Section('Warnings', 'warnings')][Section('Warning', 'warnings')][Section('See Also', 'see_also')][Section('Related', 'see_also')][Section('Notes', 'notes')], indent = [][ParamSection('Parameters', 'param')][ParamSection('Params', 'param')][ParamSection('Arguments', 'param')][ParamSection('Args', 'param')][ParamSection('Other Parameters', 'other_param')][ParamSection('Other Params', 'other_param')][ParamSection('Other Arguments', 'other_param')][ParamSection('Other Args', 'other_param')][ParamSection('Receives', 'receives')][ParamSection('Receive', 'receives')][RaisesSection('Raises', 'raises')][RaisesSection('Raise', 'raises')][RaisesSection('Warns', 'warns')][RaisesSection('Warn', 'warns')][ParamSection('Attributes', 'attribute')][ParamSection('Attribute', 'attribute')][ReturnsSection('Returns', 'returns')][ReturnsSection('Return', 'returns')][YieldsSection('Yields', 'yields')][YieldsSection('Yield', 'yields')][ExamplesSection('Examples', 'examples')][ExamplesSection('Example', 'examples')][Section('Warnings', 'warnings')][Section('Warning', 'warnings')][Section('See Also', 'see_also')][Section('Related', 'see_also')][Section('Notes', 'notes')][Section('Note', 'notes')]):
    '''Render a parsed docstring into docstring text.

    :param docstring: parsed docstring representation
    :param rendering_style: the style to render docstrings
    :param indent: the characters used as indentation in the docstring string
    :returns: docstring text
    '''
    pass
# WARNING: Decompyle incomplete
