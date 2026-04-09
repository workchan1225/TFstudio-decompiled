# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: errors.pyc (Python 3.11)

'''Pydantic-specific errors.'''
from __future__ import annotations as _annotations
import re
from typing import Any, ClassVar, Literal
from typing_extensions import Self
from typing_inspection.introspection import Qualifier
from pydantic._internal import _repr
from _migration import getattr_migration
from version import version_short
__all__ = ('PydanticUserError', 'PydanticUndefinedAnnotation', 'PydanticImportError', 'PydanticSchemaGenerationError', 'PydanticInvalidForJsonSchema', 'PydanticForbiddenQualifier', 'PydanticErrorCodes')
DEV_ERROR_DOCS_URL = f'''https://errors.pydantic.dev/{version_short()}/u/'''
PydanticErrorCodes = Literal[('class-not-fully-defined', 'custom-json-schema', 'decorator-missing-field', 'discriminator-no-field', 'discriminator-alias-type', 'discriminator-needs-literal', 'discriminator-alias', 'discriminator-validator', 'callable-discriminator-no-tag', 'typed-dict-version', 'model-field-overridden', 'model-field-missing-annotation', 'config-both', 'removed-kwargs', 'circular-reference-schema', 'invalid-for-json-schema', 'json-schema-already-used', 'base-model-instantiated', 'undefined-annotation', 'schema-for-unknown-type', 'import-error', 'create-model-field-definitions', 'validator-no-fields', 'validator-invalid-fields', 'validator-instance-method', 'validator-input-type', 'root-validator-pre-skip', 'model-serializer-instance-method', 'validator-field-config-info', 'validator-v1-signature', 'validator-signature', 'field-serializer-signature', 'model-serializer-signature', 'multiple-field-serializers', 'invalid-annotated-type', 'type-adapter-config-unused', 'root-model-extra', 'unevaluable-type-annotation', 'dataclass-init-false-extra-allow', 'clashing-init-and-init-var', 'model-config-invalid-field-name', 'with-config-on-model', 'dataclass-on-model', 'validate-call-type', 'unpack-typed-dict', 'overlapping-unpack-typed-dict', 'invalid-self-type', 'validate-by-alias-and-name-false')]

class PydanticErrorMixin:
    '''A mixin class for common functionality shared by all Pydantic-specific errors.

    Attributes:
        message: A message describing the error.
        code: An optional error code from PydanticErrorCodes enum.
    '''
    
    def __init__(self = None, message = None, *, code):
        self.message = message
        self.code = code

    
    def __str__(self = None):
        pass
    # WARNING: Decompyle incomplete



class PydanticUserError(TypeError, PydanticErrorMixin):
    '''An error raised due to incorrect use of Pydantic.'''
    pass


class PydanticUndefinedAnnotation(NameError, PydanticErrorMixin):
    pass
# WARNING: Decompyle incomplete


class PydanticImportError(ImportError, PydanticErrorMixin):
    pass
# WARNING: Decompyle incomplete


class PydanticSchemaGenerationError(PydanticUserError):
    pass
# WARNING: Decompyle incomplete


class PydanticInvalidForJsonSchema(PydanticUserError):
    pass
# WARNING: Decompyle incomplete


class PydanticForbiddenQualifier(PydanticUserError):
    pass
# WARNING: Decompyle incomplete

__getattr__ = getattr_migration(__name__)
