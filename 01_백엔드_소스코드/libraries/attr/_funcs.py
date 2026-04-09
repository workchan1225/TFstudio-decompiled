# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _funcs.pyc (Python 3.11)

import copy
from _compat import get_generic_base
from _make import _OBJ_SETATTR, NOTHING, fields
from exceptions import AttrsAttributeNotFoundError
_ATOMIC_TYPES = frozenset({
    type(None),
    bool,
    int,
    float,
    str,
    complex,
    bytes,
    type(...),
    type,
    range,
    property})

def asdict(inst, recurse, filter, dict_factory, retain_collection_types, value_serializer = (True, None, dict, False, None)):
    '''
    Return the *attrs* attribute values of *inst* as a dict.

    Optionally recurse into other *attrs*-decorated classes.

    Args:
        inst: Instance of an *attrs*-decorated class.

        recurse (bool): Recurse into classes that are also *attrs*-decorated.

        filter (~typing.Callable):
            A callable whose return code determines whether an attribute or
            element is included (`True`) or dropped (`False`).  Is called with
            the `attrs.Attribute` as the first argument and the value as the
            second argument.

        dict_factory (~typing.Callable):
            A callable to produce dictionaries from.  For example, to produce
            ordered dictionaries instead of normal Python dictionaries, pass in
            ``collections.OrderedDict``.

        retain_collection_types (bool):
            Do not convert to `list` when encountering an attribute whose type
            is `tuple` or `set`.  Only meaningful if *recurse* is `True`.

        value_serializer (typing.Callable | None):
            A hook that is called for every attribute or dict key/value.  It
            receives the current instance, field and value and must return the
            (updated) value.  The hook is run *after* the optional *filter* has
            been applied.

    Returns:
        Return type of *dict_factory*.

    Raises:
        attrs.exceptions.NotAnAttrsClassError:
            If *cls* is not an *attrs* class.

    ..  versionadded:: 16.0.0 *dict_factory*
    ..  versionadded:: 16.1.0 *retain_collection_types*
    ..  versionadded:: 20.3.0 *value_serializer*
    ..  versionadded:: 21.3.0
        If a dict has a collection for a key, it is serialized as a tuple.
    '''
    pass
# WARNING: Decompyle incomplete


def _asdict_anything(val, is_key, filter, dict_factory, retain_collection_types, value_serializer):
    '''
    ``asdict`` only works on attrs instances, this works on anything.
    '''
    pass
# WARNING: Decompyle incomplete


def astuple(inst, recurse, filter, tuple_factory, retain_collection_types = (True, None, tuple, False)):
    '''
    Return the *attrs* attribute values of *inst* as a tuple.

    Optionally recurse into other *attrs*-decorated classes.

    Args:
        inst: Instance of an *attrs*-decorated class.

        recurse (bool):
            Recurse into classes that are also *attrs*-decorated.

        filter (~typing.Callable):
            A callable whose return code determines whether an attribute or
            element is included (`True`) or dropped (`False`).  Is called with
            the `attrs.Attribute` as the first argument and the value as the
            second argument.

        tuple_factory (~typing.Callable):
            A callable to produce tuples from. For example, to produce lists
            instead of tuples.

        retain_collection_types (bool):
            Do not convert to `list` or `dict` when encountering an attribute
            which type is `tuple`, `dict` or `set`. Only meaningful if
            *recurse* is `True`.

    Returns:
        Return type of *tuple_factory*

    Raises:
        attrs.exceptions.NotAnAttrsClassError:
            If *cls* is not an *attrs* class.

    ..  versionadded:: 16.2.0
    '''
    pass
# WARNING: Decompyle incomplete


def has(cls):
    '''
    Check whether *cls* is a class with *attrs* attributes.

    Args:
        cls (type): Class to introspect.

    Raises:
        TypeError: If *cls* is not a class.

    Returns:
        bool:
    '''
    attrs = getattr(cls, '__attrs_attrs__', None)
# WARNING: Decompyle incomplete


def assoc(inst, **changes):
    """
    Copy *inst* and apply *changes*.

    This is different from `evolve` that applies the changes to the arguments
    that create the new instance.

    `evolve`'s behavior is preferable, but there are `edge cases`_ where it
    doesn't work. Therefore `assoc` is deprecated, but will not be removed.

    .. _`edge cases`: https://github.com/python-attrs/attrs/issues/251

    Args:
        inst: Instance of a class with *attrs* attributes.

        changes: Keyword changes in the new copy.

    Returns:
        A copy of inst with *changes* incorporated.

    Raises:
        attrs.exceptions.AttrsAttributeNotFoundError:
            If *attr_name* couldn't be found on *cls*.

        attrs.exceptions.NotAnAttrsClassError:
            If *cls* is not an *attrs* class.

    ..  deprecated:: 17.1.0
        Use `attrs.evolve` instead if you can. This function will not be
        removed du to the slightly different approach compared to
        `attrs.evolve`, though.
    """
    new = copy.copy(inst)
    attrs = fields(inst.__class__)
    for k, v in changes.items():
        a = getattr(attrs, k, NOTHING)
        if a is NOTHING:
            msg = f'''{k} is not an attrs attribute on {new.__class__}.'''
            raise AttrsAttributeNotFoundError(msg)
        _OBJ_SETATTR(new, k, v)
        return new


def resolve_types(cls, globalns, localns, attribs, include_extras = (None, None, None, True)):
    """
    Resolve any strings and forward annotations in type annotations.

    This is only required if you need concrete types in :class:`Attribute`'s
    *type* field. In other words, you don't need to resolve your types if you
    only use them for static type checking.

    With no arguments, names will be looked up in the module in which the class
    was created. If this is not what you want, for example, if the name only
    exists inside a method, you may pass *globalns* or *localns* to specify
    other dictionaries in which to look up these names. See the docs of
    `typing.get_type_hints` for more details.

    Args:
        cls (type): Class to resolve.

        globalns (dict | None): Dictionary containing global variables.

        localns (dict | None): Dictionary containing local variables.

        attribs (list | None):
            List of attribs for the given class. This is necessary when calling
            from inside a ``field_transformer`` since *cls* is not an *attrs*
            class yet.

        include_extras (bool):
            Resolve more accurately, if possible. Pass ``include_extras`` to
            ``typing.get_hints``, if supported by the typing module. On
            supported Python versions (3.9+), this resolves the types more
            accurately.

    Raises:
        TypeError: If *cls* is not a class.

        attrs.exceptions.NotAnAttrsClassError:
            If *cls* is not an *attrs* class and you didn't pass any attribs.

        NameError: If types cannot be resolved because of missing variables.

    Returns:
        *cls* so you can use this function also as a class decorator. Please
        note that you have to apply it **after** `attrs.define`. That means the
        decorator has to come in the line **before** `attrs.define`.

    ..  versionadded:: 20.1.0
    ..  versionadded:: 21.1.0 *attribs*
    ..  versionadded:: 23.1.0 *include_extras*
    """
    pass
# WARNING: Decompyle incomplete
