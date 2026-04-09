# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: warnings.pyc (Python 3.11)

'''Pydantic-specific warnings.'''
from __future__ import annotations as _annotations
from version import version_short
__all__ = ('PydanticDeprecatedSince20', 'PydanticDeprecatedSince26', 'PydanticDeprecatedSince29', 'PydanticDeprecatedSince210', 'PydanticDeprecatedSince211', 'PydanticDeprecatedSince212', 'PydanticDeprecationWarning', 'PydanticExperimentalWarning', 'ArbitraryTypeWarning', 'UnsupportedFieldAttributeWarning', 'TypedDictExtraConfigWarning')

class PydanticDeprecationWarning(DeprecationWarning):
    pass
# WARNING: Decompyle incomplete


class PydanticDeprecatedSince20(PydanticDeprecationWarning):
    pass
# WARNING: Decompyle incomplete


class PydanticDeprecatedSince26(PydanticDeprecationWarning):
    pass
# WARNING: Decompyle incomplete


class PydanticDeprecatedSince29(PydanticDeprecationWarning):
    pass
# WARNING: Decompyle incomplete


class PydanticDeprecatedSince210(PydanticDeprecationWarning):
    pass
# WARNING: Decompyle incomplete


class PydanticDeprecatedSince211(PydanticDeprecationWarning):
    pass
# WARNING: Decompyle incomplete


class PydanticDeprecatedSince212(PydanticDeprecationWarning):
    pass
# WARNING: Decompyle incomplete


class GenericBeforeBaseModelWarning(Warning):
    pass


class PydanticExperimentalWarning(Warning):
    '''A Pydantic specific experimental functionality warning.

    It is raised to warn users that the functionality may change or be removed in future versions of Pydantic.
    '''
    pass


class CoreSchemaGenerationWarning(UserWarning):
    '''A warning raised during core schema generation.'''
    pass


class ArbitraryTypeWarning(CoreSchemaGenerationWarning):
    '''A warning raised when Pydantic fails to generate a core schema for an arbitrary type.'''
    pass


class UnsupportedFieldAttributeWarning(CoreSchemaGenerationWarning):
    """A warning raised when a `Field()` attribute isn't supported in the context it is used."""
    pass


class TypedDictExtraConfigWarning(CoreSchemaGenerationWarning):
    '''A warning raised when the [`extra`][pydantic.ConfigDict.extra] configuration is incompatible with the `closed` or `extra_items` specification.'''
    pass
