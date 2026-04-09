# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: variable.pyc (Python 3.11)

'''

uritemplate.variable
====================

This module contains the URIVariable class which powers the URITemplate class.

What treasures await you:

- URIVariable class

You see a hammer in front of you.
What do you do?
>

'''
import collections.abc as collections
import enum
import string
import typing as t
import urllib.parse as urllib
ScalarVariableValue = t.Union[(int, float, complex, str, None)]
VariableValue = t.Union[(t.Sequence[ScalarVariableValue], t.List[ScalarVariableValue], t.Mapping[(str, ScalarVariableValue)], t.Tuple[(str, ScalarVariableValue)], ScalarVariableValue)]
VariableValueDict = t.Dict[(str, VariableValue)]
_UNRESERVED_CHARACTERS: t.Final[str] = f'''{string.ascii_letters}{string.digits}~-_.'''
_GEN_DELIMS: t.Final[str] = ':/?#[]@'
_SUB_DELIMS: t.Final[str] = "!$&'()*+,;="
_RESERVED_CHARACTERS: t.Final[str] = f'''{_GEN_DELIMS}{_SUB_DELIMS}'''

class Operator(enum.Enum):
    default = ''
    reserved = '+'
    fragment = '#'
    label_with_dot_prefix = '.'
    path_segment = '/'
    path_style_parameter = ';'
    form_style_query = '?'
    form_style_query_continuation = '&'
    reserved_eq = '='
    reserved_comma = ','
    reserved_bang = '!'
    reserved_at = '@'
    reserved_pipe = '|'
    
    def reserved_characters(self = None):
        if self == Operator.reserved:
            return _RESERVED_CHARACTERS + '%'
        if None == Operator.fragment:
            return _RESERVED_CHARACTERS

    
    def expansion_separator(self = None):
        '''Identify the separator used during expansion.

        Per `Section 3.2.1. Variable Expansion`_:

        ======  ===========    =========
        Type    Separator
        ======  ===========    =========
                ``","``        (default)
        ``+``   ``","``
        ``#``   ``","``
        ``.``   ``"."``
        ``/``   ``"/"``
        ``;``   ``";"``
        ``?``   ``"&"``
        ``&``   ``"&"``
        ======  ===========    =========

        .. _`Section 3.2.1. Variable Expansion`:
            https://www.rfc-editor.org/rfc/rfc6570#section-3.2.1
        '''
        if self == Operator.label_with_dot_prefix:
            return '.'
        if None == Operator.path_segment:
            return '/'
        if None == Operator.path_style_parameter:
            return ';'
        if None == Operator.form_style_query or self == Operator.form_style_query_continuation:
            return '&'

    
    def variable_prefix(self = None):
        if self == Operator.reserved:
            return ''
        return None.cast(str, self.value)

    
    def _always_quote(self = None, value = None):
        return quote(value, '')

    
    def _only_quote_unquoted_characters(self = None, value = None):
        if urllib.parse.unquote(value) == value:
            return quote(value, _RESERVED_CHARACTERS)

    
    def quote(self = None, value = None):
        if not isinstance(value, (str, bytes)):
            value = str(value)
        if isinstance(value, bytes):
            value = value.decode()
        if self == Operator.reserved or self == Operator.fragment:
            return self._only_quote_unquoted_characters(value)
        return None._always_quote(value)

    from_string = (lambda s = None: _operators.get(s, Operator.default))()

_operators: t.Final[t.Dict[(str, Operator)]] = {
    '+': Operator.reserved,
    '#': Operator.fragment,
    '.': Operator.label_with_dot_prefix,
    '/': Operator.path_segment,
    ';': Operator.path_style_parameter,
    '?': Operator.form_style_query,
    '&': Operator.form_style_query_continuation,
    '!': Operator.reserved_bang,
    '|': Operator.reserved_pipe,
    '@': Operator.reserved_at,
    '=': Operator.reserved_eq,
    ',': Operator.reserved_comma }

class URIVariable:
    """This object validates everything inside the URITemplate object.

    It validates template expansions and will truncate length as decided by
    the template.

    Please note that just like the :class:`URITemplate <URITemplate>`, this
    object's ``__str__`` and ``__repr__`` methods do not return the same
    information. Calling ``str(var)`` will return the original variable.

    This object does the majority of the heavy lifting. The ``URITemplate``
    object finds the variables in the URI and then creates ``URIVariable``
    objects.  Expansions of the URI are handled by each ``URIVariable``
    object. ``URIVariable.expand()`` returns a dictionary of the original
    variable and the expanded value. Check that method's documentation for
    more information.

    """
    
    def __init__(self = None, var = None):
        self.original = var
        self.operator = Operator.default
        self.variables = []
        self.variable_names = []
        self.defaults = { }
        self.parse()

    
    def __repr__(self = None):
        return 'URIVariable(%s)' % self

    
    def __str__(self = None):
        return self.original

    
    def parse(self = None):
        '''Parse the variable.

        This finds the:
            - operator,
            - set of safe characters,
            - variables, and
            - defaults.

        '''
        var_list_str = self.original
        operator_str = self.original[0]
        if self.original[0] in _operators:
            self.operator = Operator.from_string(operator_str)
            var_list_str = self.original[1:]
        var_list = var_list_str.split(',')
        for var in var_list:
            default_val = None
            name = var
            if '=' in var:
                (name, default_val) = tuple(var.split('=', 1))
            explode = name.endswith('*')
            name = name.rstrip('*')
            prefix = None
            if ':' in name:
                (name, prefix_str) = tuple(name.split(':', 1))
                prefix = int(prefix_str, 10)
            if default_val:
                self.defaults[name] = default_val
            self.variables.append((name, {
                'explode': explode,
                'prefix': prefix }))
            self.variable_names = self.variables()
            return None

    
    def _query_expansion(self, name = None, value = None, explode = None, prefix = ('name', str, 'value', VariableValue, 'explode', bool, 'prefix', t.Optional[int], 'return', t.Optional[str])):
        """Expansion method for the '?' and '&' operators."""
        pass
    # WARNING: Decompyle incomplete

    
    def _label_path_expansion(self, name = None, value = None, explode = None, prefix = ('name', str, 'value', VariableValue, 'explode', bool, 'prefix', t.Optional[int], 'return', t.Optional[str])):
        """Label and path expansion method.

        Expands for operators: '/', '.'

        """
        pass
    # WARNING: Decompyle incomplete

    
    def _semi_path_expansion(self, name = None, value = None, explode = None, prefix = ('name', str, 'value', VariableValue, 'explode', bool, 'prefix', t.Optional[int], 'return', t.Optional[str])):
        """Expansion method for ';' operator."""
        pass
    # WARNING: Decompyle incomplete

    
    def _string_expansion(self, name = None, value = None, explode = None, prefix = ('name', str, 'value', VariableValue, 'explode', bool, 'prefix', t.Optional[int], 'return', t.Optional[str])):
        pass
    # WARNING: Decompyle incomplete

    
    def expand(self = None, var_dict = None):
        """Expand the variable in question.

        Using ``var_dict`` and the previously parsed defaults, expand this
        variable and subvariables.

        :param dict var_dict: dictionary of key-value pairs to be used during
            expansion
        :returns: dict(variable=value)

        Examples::

            # (1)
            v = URIVariable('/var')
            expansion = v.expand({'var': 'value'})
            print(expansion)
            # => {'/var': '/value'}

            # (2)
            v = URIVariable('?var,hello,x,y')
            expansion = v.expand({'var': 'value', 'hello': 'Hello World!',
                                  'x': '1024', 'y': '768'})
            print(expansion)
            # => {'?var,hello,x,y':
            #     '?var=value&hello=Hello%20World%21&x=1024&y=768'}

        """
        return_values = []
    # WARNING: Decompyle incomplete



def is_list_of_tuples(value = None):
    if not value and isinstance(value, (list, tuple)) or (lambda .0: pass# WARNING: Decompyle incomplete
)(value()):
        return (False, None)
    return (all, value)


def list_test(value = None):
    return isinstance(value, (list, tuple))


def dict_test(value = None):
    return isinstance(value, (dict, collections.abc.MutableMapping))


def _encode(value = None, encoding = None):
    if isinstance(value, str):
        return value.encode(encoding)


def quote(value = None, safe = None):
    if not isinstance(value, (str, bytes)):
        value = str(value)
    return urllib.parse.quote(_encode(value), safe)
