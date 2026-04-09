# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: iam.pyc (Python 3.11)

'''Non-API-specific IAM policy definitions

For allowed roles / permissions, see:
https://cloud.google.com/iam/docs/understanding-roles

Example usage:

.. code-block:: python

   # ``get_iam_policy`` returns a :class:\'~google.api_core.iam.Policy`.
   policy = resource.get_iam_policy(requested_policy_version=3)

   phred = "user:phred@example.com"
   admin_group = "group:admins@groups.example.com"
   account = "serviceAccount:account-1234@accounts.example.com"

   policy.version = 3
   policy.bindings = [
       {
           "role": "roles/owner",
           "members": {phred, admin_group, account}
       },
       {
           "role": "roles/editor",
           "members": {"allAuthenticatedUsers"}
       },
       {
           "role": "roles/viewer",
           "members": {"allUsers"}
           "condition": {
               "title": "request_time",
               "description": "Requests made before 2021-01-01T00:00:00Z",
               "expression": "request.time < timestamp("2021-01-01T00:00:00Z")"
           }
       }
   ]

   resource.set_iam_policy(policy)
'''
import collections
import collections.abc as collections
import operator
import warnings
OWNER_ROLE = 'roles/owner'
EDITOR_ROLE = 'roles/editor'
VIEWER_ROLE = 'roles/viewer'
_ASSIGNMENT_DEPRECATED_MSG = "Assigning to '{}' is deprecated. Use the `policy.bindings` property to modify bindings instead."
_DICT_ACCESS_MSG = 'Dict access is not supported on policies with version > 1 or with conditional bindings.'

class InvalidOperationException(Exception):
    '''Raised when trying to use Policy class as a dict.'''
    pass


class Policy(collections.abc.MutableMapping):
    """IAM Policy

    Args:
        etag (Optional[str]): ETag used to identify a unique of the policy
        version (Optional[int]): The syntax schema version of the policy.

    Note:
        Using conditions in bindings requires the policy's version to be set
        to `3` or greater, depending on the versions that are currently supported.

        Accessing the policy using dict operations will raise InvalidOperationException
        when the policy's version is set to 3.

        Use the policy.bindings getter/setter to retrieve and modify the policy's bindings.

    See:
        IAM Policy https://cloud.google.com/iam/reference/rest/v1/Policy
        Policy versions https://cloud.google.com/iam/docs/policies#versions
        Conditions overview https://cloud.google.com/iam/docs/conditions-overview.
    """
    _OWNER_ROLES = (OWNER_ROLE,)
    _EDITOR_ROLES = (EDITOR_ROLE,)
    _VIEWER_ROLES = (VIEWER_ROLE,)
    
    def __init__(self, etag, version = (None, None)):
        self.etag = etag
        self.version = version
        self._bindings = []

    
    def __iter__(self):
        self.__check_version__()
        return self._bindings()

    
    def __len__(self):
        self.__check_version__()
        return len(list(self.__iter__()))

    
    def __getitem__(self, key):
        self.__check_version__()
        for b in self._bindings:
            if b['role'] == key:
                
                return None, b['members']
            self._bindings.append(new_binding)
            return new_binding['members']

    
    def __setitem__(self, key, value):
        self.__check_version__()
        value = set(value)
        for binding in self._bindings:
            if binding['role'] == key:
                binding['members'] = value
                return None
            self._bindings.append({
                'role': key,
                'members': value })
            return None

    
    def __delitem__(self, key):
        self.__check_version__()
        for b in self._bindings:
            if b['role'] == key:
                self._bindings.remove(b)
                return None
            raise KeyError(key)

    
    def __check_version__(self):
        '''Raise InvalidOperationException if version is greater than 1 or policy contains conditions.'''
        if self.version is not None:
            pass
        raise_version = self.version > 1
        if raise_version or self._contains_conditions():
            raise InvalidOperationException(_DICT_ACCESS_MSG)

    
    def _contains_conditions(self):
        pass
    # WARNING: Decompyle incomplete

    bindings = (lambda self: self._bindings)()
    bindings = (lambda self, bindings: self._bindings = bindings)()
    owners = (lambda self: result = set()for role in self._OWNER_ROLES:
for member in self.get(role, ()):
result.add(member)frozenset(result))()
    owners = (lambda self, value: warnings.warn(_ASSIGNMENT_DEPRECATED_MSG.format('owners', OWNER_ROLE), DeprecationWarning)self[OWNER_ROLE] = value)()
    editors = (lambda self: result = set()for role in self._EDITOR_ROLES:
for member in self.get(role, ()):
result.add(member)frozenset(result))()
    editors = (lambda self, value: warnings.warn(_ASSIGNMENT_DEPRECATED_MSG.format('editors', EDITOR_ROLE), DeprecationWarning)self[EDITOR_ROLE] = value)()
    viewers = (lambda self: result = set()for role in self._VIEWER_ROLES:
for member in self.get(role, ()):
result.add(member)frozenset(result))()
    viewers = (lambda self, value: warnings.warn(_ASSIGNMENT_DEPRECATED_MSG.format('viewers', VIEWER_ROLE), DeprecationWarning)self[VIEWER_ROLE] = value)()
    user = (lambda email: f'''user:{email!s}''')()
    service_account = (lambda email: f'''serviceAccount:{email!s}''')()
    group = (lambda email: f'''group:{email!s}''')()
    domain = (lambda domain: f'''domain:{domain!s}''')()
    all_users = (lambda : 'allUsers')()
    authenticated_users = (lambda : 'allAuthenticatedUsers')()
    from_api_repr = (lambda cls, resource: version = resource.get('version')etag = resource.get('etag')policy = cls(etag, version)policy.bindings = resource.get('bindings', [])for binding in policy.bindings:
binding['members'] = set(binding.get('members', ()))policy)()
    
    def to_api_repr(self):
        '''Render a JSON policy resource.

        Returns:
            dict: a resource to be passed to the ``setIamPolicy`` API.
        '''
        resource = { }
    # WARNING: Decompyle incomplete
