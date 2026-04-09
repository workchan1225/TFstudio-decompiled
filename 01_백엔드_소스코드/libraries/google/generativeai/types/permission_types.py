# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: permission_types.pyc (Python 3.11)

from __future__ import annotations
import dataclasses
from typing import Optional, Union, Any, Iterable, AsyncIterable
import re

generativelanguage
from google.generativeai import protos
import google.ai.generativelanguage, ai
from google.protobuf import field_mask_pb2
from google.generativeai.client import get_default_permission_client
from google.generativeai.client import get_default_permission_async_client
from google.generativeai.utils import flatten_update_paths
from google.generativeai import string_utils
__all__ = [
    'Permission',
    'Permissions']
GranteeType = protos.Permission.GranteeType
Role = protos.Permission.Role
GranteeTypeOptions = Union[(str, int, GranteeType)]
RoleOptions = Union[(str, int, Role)]
_GRANTEE_TYPE: 'dict[GranteeTypeOptions, GranteeType]' = {
    'everyone': GranteeType.EVERYONE,
    3: GranteeType.EVERYONE,
    GranteeType.EVERYONE: GranteeType.EVERYONE,
    'group': GranteeType.GROUP,
    2: GranteeType.GROUP,
    GranteeType.GROUP: GranteeType.GROUP,
    'user': GranteeType.USER,
    1: GranteeType.USER,
    GranteeType.USER: GranteeType.USER,
    'unspecified': GranteeType.GRANTEE_TYPE_UNSPECIFIED,
    'grantee_type_unspecified': GranteeType.GRANTEE_TYPE_UNSPECIFIED,
    0: GranteeType.GRANTEE_TYPE_UNSPECIFIED,
    GranteeType.GRANTEE_TYPE_UNSPECIFIED: GranteeType.GRANTEE_TYPE_UNSPECIFIED }
_ROLE: 'dict[RoleOptions, Role]' = {
    'reader': Role.READER,
    3: Role.READER,
    Role.READER: Role.READER,
    'writer': Role.WRITER,
    2: Role.WRITER,
    Role.WRITER: Role.WRITER,
    'owner': Role.OWNER,
    1: Role.OWNER,
    Role.OWNER: Role.OWNER,
    'unspecified': Role.ROLE_UNSPECIFIED,
    'role_unspecified': Role.ROLE_UNSPECIFIED,
    0: Role.ROLE_UNSPECIFIED,
    Role.ROLE_UNSPECIFIED: Role.ROLE_UNSPECIFIED }
_VALID_PERMISSION_ID = 'permissions/([a-z0-9]+)$'
INVALID_PERMISSION_ID_MSG = '`permission_id` must follow the pattern: `permissions/<id>` and must consist of only alphanumeric characters. Got: `{permission_id}` instead.'

def to_grantee_type(x = None):
    if isinstance(x, str):
        x = x.lower()
    return _GRANTEE_TYPE[x]


def to_role(x = None):
    if isinstance(x, str):
        x = x.lower()
    return _ROLE[x]


def valid_id(name = None):
    return re.match(_VALID_PERMISSION_ID, name) is not None

Permission = <NODE:12>()()

class Permissions:
    
    def __init__(self, parent):
        if isinstance(parent, str):
            self._parent = parent
            return None
        self._parent = None.name

    parent = (lambda self: self._parent)()
    
    def _make_create_permission_request(self = None, role = None, grantee_type = property, email_address = (None, None)):
        role = to_role(role)
        if grantee_type:
            grantee_type = to_grantee_type(grantee_type)
        if email_address and grantee_type == GranteeType.EVERYONE:
            raise ValueError(f'''Invalid operation: Access cannot be limited for a specific email address (\'{email_address}\') when \'grantee_type\' is set to \'EVERYONE\'.''')
        if email_address and grantee_type != GranteeType.EVERYONE:
            raise ValueError(f'''Invalid operation: An \'email_address\' must be provided when \'grantee_type\' is not set to \'EVERYONE\'. Currently, \'grantee_type\' is set to \'{grantee_type}\' and \'email_address\' is \'{email_address if email_address else 'not provided'}\'.''')
    # WARNING: Decompyle incomplete

    
    def create(self = None, role = None, grantee_type = None, email_address = (None, None, None), client = ('role', 'RoleOptions', 'grantee_type', 'Optional[GranteeTypeOptions]', 'email_address', 'Optional[str]', 'client', 'glm.PermissionServiceClient | None', 'return', 'Permission')):
        '''
        Create a new permission on a resource (self).

        Args:
            parent: The resource name of the parent resource in which the permission will be listed.
            role: role that will be granted by the permission.
            grantee_type: The type of the grantee for the permission.
            email_address: The email address of the grantee.

        Returns:
            `Permission` object with specified parent, role, grantee type, and email address.

        Raises:
            ValueError: When email_address is specified and grantee_type is set to EVERYONE.
            ValueError: When email_address is not specified and grantee_type is not set to EVERYONE.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def create_async(self = None, role = None, grantee_type = None, email_address = (None, None, None), client = ('role', 'RoleOptions', 'grantee_type', 'Optional[GranteeTypeOptions]', 'email_address', 'Optional[str]', 'client', 'glm.PermissionServiceAsyncClient | None', 'return', 'Permission')):
        '''
        This is the async version of `PermissionAdapter.create_permission`.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def list(self = None, page_size = None, client = None):
        '''
        List `Permission`s enforced on a resource (self).

        Args:
            parent: The resource name of the parent resource in which the permission will be listed.
            page_size: The maximum number of permissions to return (per page). The service may return fewer permissions.

        Returns:
            Paginated list of `Permission` objects.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __iter__(self):
        return self.list()

    
    def list_async(self = None, page_size = None, client = None):
        '''
        This is the async version of `PermissionAdapter.list_permissions`.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def __aiter__(self):
        pass
    # WARNING: Decompyle incomplete

    get = (lambda cls = None, name = None: Permission.get(name))()
    get_async = (lambda cls = None, name = None: pass# WARNING: Decompyle incomplete
)()
    
    def transfer_ownership(self = None, email_address = None, client = None):
        '''
        Transfer ownership of a resource (self) to a new owner.

        Args:
            name: Name of the resource to transfer ownership.
            email_address: Email address of the new owner.
        '''
        if self.parent.startswith('corpora'):
            raise NotImplementedError("Can'/t transfer_ownership for a Corpus")
    # WARNING: Decompyle incomplete

    
    async def transfer_ownership_async(self = None, email_address = None, client = None):
        '''This is the async version of `PermissionAdapter.transfer_ownership`.'''
        pass
    # WARNING: Decompyle incomplete
