# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: introspection.pyc (Python 3.11)

'''High-level introspection utilities, used to inspect type annotations.'''
from __future__ import annotations
import sys
import types
from collections.abc import Generator
from dataclasses import InitVar
from enum import Enum, IntEnum, auto
from typing import Any, Literal, NamedTuple, cast
from typing_extensions import TypeAlias, assert_never, get_args, get_origin
from  import typing_objects
__all__ = ('AnnotationSource', 'ForbiddenQualifier', 'InspectedAnnotation', 'Qualifier', 'get_literal_values', 'inspect_annotation', 'is_union_origin')
if sys.version_info >= (3, 14) or sys.version_info < (3, 10):
    
    def is_union_origin(obj = None):
        '''Return whether the provided origin is the union form.

        ```pycon
        >>> is_union_origin(typing.Union)
        True
        >>> is_union_origin(get_origin(int | str))
        True
        >>> is_union_origin(types.UnionType)
        True
        ```

        !!! note
            Since Python 3.14, both `Union[<t1>, <t2>, ...]` and `<t1> | <t2> | ...` forms create instances
            of the same [`typing.Union`][] class. As such, it is recommended to not use this function
            anymore (provided that you only support Python 3.14 or greater), and instead use the
            [`typing_objects.is_union()`][typing_inspection.typing_objects.is_union] function directly:

            ```python
            from typing import Union, get_origin

            from typing_inspection import typing_objects

            typ = int | str  # Or Union[int, str]
            origin = get_origin(typ)
            if typing_objects.is_union(origin):
                ...
            ```
        '''
        return typing_objects.is_union(obj)

else:
    
    def is_union_origin(obj = None):
