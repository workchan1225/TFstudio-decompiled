# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: typing_objects.pyc (Python 3.11)

__doc__ = 'Low-level introspection utilities for [`typing`][] members.\n\nThe provided functions in this module check against both the [`typing`][] and [`typing_extensions`][]\nvariants, if they exists and are different.\n'
import collections.abc as collections
import contextlib
import re
import sys
import typing
import warnings
from textwrap import dedent
from types import FunctionType, GenericAlias
from typing import Any, Final
import typing_extensions
from typing_extensions import LiteralString, TypeAliasType, TypeIs, deprecated
__all__ = ('DEPRECATED_ALIASES', 'NoneType', 'is_annotated', 'is_any', 'is_classvar', 'is_concatenate', 'is_deprecated', 'is_final', 'is_forwardref', 'is_generic', 'is_literal', 'is_literalstring', 'is_namedtuple', 'is_never', 'is_newtype', 'is_nodefault', 'is_noextraitems', 'is_noreturn', 'is_notrequired', 'is_paramspec', 'is_paramspecargs', 'is_paramspeckwargs', 'is_readonly', 'is_required', 'is_self', 'is_typealias', 'is_typealiastype', 'is_typeguard', 'is_typeis', 'is_typevar', 'is_typevartuple', 'is_union', 'is_unpack')
_IS_PY310 = sys.version_info[:2] == (3, 10)

def _compile_identity_check_function(member = None, function_name = None):
    '''Create a function checking that the function argument is the (unparameterized) typing `member`.

    The function will make sure to check against both the `typing` and `typing_extensions`
    variants as depending on the Python version, the `typing_extensions` variant might be different.
    For instance, on Python 3.9:

    ```pycon
    >>> from typing import Literal as t_Literal
    >>> from typing_extensions import Literal as te_Literal, get_origin

    >>> t_Literal is te_Literal
    False
    >>> get_origin(t_Literal[1])
    typing.Literal
    >>> get_origin(te_Literal[1])
    typing_extensions.Literal
    ```
    '''
    in_typing = hasattr(typing, member)
    in_typing_extensions = hasattr(typing_extensions, member)
    if in_typing and in_typing_extensions:
        if getattr(typing, member) is getattr(typing_extensions, member):
            check_code = f'''obj is typing.{member}'''
        else:
            check_code = f'''obj is typing.{member} or obj is typing_extensions.{member}'''
    elif not in_typing and in_typing_extensions:
        check_code = f'''obj is typing.{member}'''
    elif in_typing and in_typing_extensions:
        check_code = f'''obj is typing_extensions.{member}'''
    else:
        check_code = 'False'
    func_code = dedent(f'''\n    def {function_name}(obj: Any, /) -> bool:\n        return {check_code}\n    ''')
    locals_ = { }
    globals_ = {
        'Any': Any,
        'typing': typing,
        'typing_extensions': typing_extensions }
    exec(func_code, globals_, locals_)
    return locals_[function_name]


def _compile_isinstance_check_function(member = None, function_name = None):
    '''Create a function checking that the function is an instance of the typing `member`.

    The function will make sure to check against both the `typing` and `typing_extensions`
    variants as depending on the Python version, the `typing_extensions` variant might be different.
    '''
    in_typing = hasattr(typing, member)
    in_typing_extensions = hasattr(typing_extensions, member)
    if in_typing and in_typing_extensions:
        if getattr(typing, member) is getattr(typing_extensions, member):
            check_code = f'''isinstance(obj, typing.{member})'''
        else:
            check_code = f'''isinstance(obj, (typing.{member}, typing_extensions.{member}))'''
    elif not in_typing and in_typing_extensions:
        check_code = f'''isinstance(obj, typing.{member})'''
    elif in_typing and in_typing_extensions:
        check_code = f'''isinstance(obj, typing_extensions.{member})'''
    else:
        check_code = 'False'
    func_code = dedent(f'''\n    def {function_name}(obj: Any, /) -> \'TypeIs[{member}]\':\n        return {check_code}\n    ''')
    locals_ = { }
    globals_ = {
        'Any': Any,
        'typing': typing,
        'typing_extensions': typing_extensions }
    exec(func_code, globals_, locals_)
    return locals_[function_name]

if sys.version_info >= (3, 10):
    from types import NoneType
else:
    NoneType = type(None)
is_annotated = _compile_identity_check_function('Annotated', 'is_annotated')
is_annotated.__doc__ = '\nReturn whether the argument is the [`Annotated`][typing.Annotated] [special form][].\n\n```pycon\n>>> is_annotated(Annotated)\nTrue\n>>> is_annotated(Annotated[int, ...])\nFalse\n```\n'
is_any = _compile_identity_check_function('Any', 'is_any')
is_any.__doc__ = '\nReturn whether the argument is the [`Any`][typing.Any] [special form][].\n\n```pycon\n>>> is_any(Any)\nTrue\n```\n'
is_classvar = _compile_identity_check_function('ClassVar', 'is_classvar')
is_classvar.__doc__ = '\nReturn whether the argument is the [`ClassVar`][typing.ClassVar] [type qualifier][].\n\n```pycon\n>>> is_classvar(ClassVar)\nTrue\n>>> is_classvar(ClassVar[int])\n>>> False\n```\n'
is_concatenate = _compile_identity_check_function('Concatenate', 'is_concatenate')
is_concatenate.__doc__ = '\nReturn whether the argument is the [`Concatenate`][typing.Concatenate] [special form][].\n\n```pycon\n>>> is_concatenate(Concatenate)\nTrue\n>>> is_concatenate(Concatenate[int, P])\nFalse\n```\n'
is_final = _compile_identity_check_function('Final', 'is_final')
is_final.__doc__ = '\nReturn whether the argument is the [`Final`][typing.Final] [type qualifier][].\n\n```pycon\n>>> is_final(Final)\nTrue\n>>> is_final(Final[int])\nFalse\n```\n'
is_forwardref = _compile_isinstance_check_function('ForwardRef', 'is_forwardref')
is_forwardref.__doc__ = "\nReturn whether the argument is an instance of [`ForwardRef`][typing.ForwardRef].\n\n```pycon\n>>> is_forwardref(ForwardRef('T'))\nTrue\n```\n"
is_generic = _compile_identity_check_function('Generic', 'is_generic')
is_generic.__doc__ = '\nReturn whether the argument is the [`Generic`][typing.Generic] [special form][].\n\n```pycon\n>>> is_generic(Generic)\nTrue\n>>> is_generic(Generic[T])\nFalse\n```\n'
is_literal = _compile_identity_check_function('Literal', 'is_literal')
is_literal.__doc__ = '\nReturn whether the argument is the [`Literal`][typing.Literal] [special form][].\n\n```pycon\n>>> is_literal(Literal)\nTrue\n>>> is_literal(Literal["a"])\nFalse\n```\n'
is_paramspec = _compile_isinstance_check_function('ParamSpec', 'is_paramspec')
is_paramspec.__doc__ = "\nReturn whether the argument is an instance of [`ParamSpec`][typing.ParamSpec].\n\n```pycon\n>>> P = ParamSpec('P')\n>>> is_paramspec(P)\nTrue\n```\n"
is_typevar = _compile_isinstance_check_function('TypeVar', 'is_typevar')
is_typevar.__doc__ = "\nReturn whether the argument is an instance of [`TypeVar`][typing.TypeVar].\n\n```pycon\n>>> T = TypeVar('T')\n>>> is_typevar(T)\nTrue\n```\n"
is_typevartuple = _compile_isinstance_check_function('TypeVarTuple', 'is_typevartuple')
is_typevartuple.__doc__ = "\nReturn whether the argument is an instance of [`TypeVarTuple`][typing.TypeVarTuple].\n\n```pycon\n>>> Ts = TypeVarTuple('Ts')\n>>> is_typevartuple(Ts)\nTrue\n```\n"
is_union = _compile_identity_check_function('Union', 'is_union')
is_union.__doc__ = '\nReturn whether the argument is the [`Union`][typing.Union] [special form][].\n\nThis function can also be used to check for the [`Optional`][typing.Optional] [special form][],\nas at runtime, `Optional[int]` is equivalent to `Union[int, None]`.\n\n```pycon\n>>> is_union(Union)\nTrue\n>>> is_union(Union[int, str])\nFalse\n```\n\n!!! warning\n    This does not check for unions using the [new syntax][types-union] (e.g. `int | str`).\n'

def is_namedtuple(obj = None):
