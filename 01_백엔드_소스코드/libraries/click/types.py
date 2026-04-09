# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

import os
import stat
import sys
import typing as t
from datetime import datetime
from gettext import gettext as _
from gettext import ngettext
from _compat import _get_argv_encoding
from _compat import open_stream
from exceptions import BadParameter
from utils import format_filename
from utils import LazyFile
from utils import safecall
if t.TYPE_CHECKING:
    import typing_extensions as te
    from core import Context
    from core import Parameter
    from shell_completion import CompletionItem

class ParamType:
    '''Represents the type of a parameter. Validates and converts values
    from the command line or Python into the correct type.

    To implement a custom type, subclass and implement at least the
    following:

    -   The :attr:`name` class attribute must be set.
    -   Calling an instance of the type with ``None`` must return
        ``None``. This is already implemented by default.
    -   :meth:`convert` must convert string values to the correct type.
    -   :meth:`convert` must accept values that are already the correct
        type.
    -   It must be able to convert a value if the ``ctx`` and ``param``
        arguments are ``None``. This can occur when converting prompt
        input.
    '''
    is_composite: t.ClassVar[bool] = False
    name: str = 1
    envvar_list_splitter: t.ClassVar[t.Optional[str]] = None
    
    def to_info_dict(self = None):
        '''Gather information that could be useful for a tool generating
        user-facing documentation.

        Use :meth:`click.Context.to_info_dict` to traverse the entire
        CLI structure.

        .. versionadded:: 8.0
        '''
        param_type = type(self).__name__.partition('ParamType')[0]
        param_type = param_type.partition('ParameterType')[0]
        if hasattr(self, 'name'):
            name = self.name
        else:
            name = param_type
        return {
            'param_type': param_type,
            'name': name }

    
    def __call__(self = None, value = None, param = None, ctx = (None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def get_metavar(self = None, param = None):
        '''Returns the metavar default for this param if it provides one.'''
        pass

    
    def get_missing_message(self = None, param = None):
        '''Optionally might return extra information about a missing
        parameter.

        .. versionadded:: 2.0
        '''
        pass

    
    def convert(self = None, value = None, param = None, ctx = ('value', t.Any, 'param', t.Optional['Parameter'], 'ctx', t.Optional['Context'], 'return', t.Any)):
        '''Convert the value to the correct type. This is not called if
        the value is ``None`` (the missing value).

        This must accept string values from the command line, as well as
        values that are already the correct type. It may also convert
        other compatible types.

        The ``param`` and ``ctx`` arguments may be ``None`` in certain
        situations, such as when converting prompt input.

        If the value cannot be converted, call :meth:`fail` with a
        descriptive message.

        :param value: The value to convert.
        :param param: The parameter that is using this type to convert
            its value. May be ``None``.
        :param ctx: The current context that arrived at this value. May
            be ``None``.
        '''
        return value

    
    def split_envvar_value(self = None, rv = None):
