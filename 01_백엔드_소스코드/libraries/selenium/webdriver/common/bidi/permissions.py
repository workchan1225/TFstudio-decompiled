# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: permissions.pyc (Python 3.11)

from selenium.webdriver.common.bidi.common import command_builder

class PermissionState:
    '''Represents the possible permission states.'''
    GRANTED = 'granted'
    DENIED = 'denied'
    PROMPT = 'prompt'


class PermissionDescriptor:
    '''Represents a permission descriptor.'''
    
    def __init__(self = None, name = None):
        self.name = name

    
    def to_dict(self = None):
        return {
            'name': self.name }



class Permissions:
    '''BiDi implementation of the permissions module.'''
    
    def __init__(self, conn):
        self.conn = conn

    
    def set_permission(self = None, descriptor = None, state = None, origin = (None,), user_context = ('descriptor', str | PermissionDescriptor, 'state', str, 'origin', str, 'user_context', str | None, 'return', None)):
        '''Sets a permission state for a given permission descriptor.

        Args:
            descriptor: The permission name (str) or PermissionDescriptor object.
              Examples: "geolocation", "camera", "microphone".
            state: The permission state (granted, denied, prompt).
            origin: The origin for which the permission is set.
            user_context: The user context id (optional).

        Raises:
            ValueError: If the permission state is invalid.
        '''
        if state not in (PermissionState.GRANTED, PermissionState.DENIED, PermissionState.PROMPT):
            valid_states = f'''{PermissionState.GRANTED}, {PermissionState.DENIED}, {PermissionState.PROMPT}'''
            raise ValueError(f'''Invalid permission state. Must be one of: {valid_states}''')
        if isinstance(descriptor, str):
            permission_descriptor = PermissionDescriptor(descriptor)
        else:
            permission_descriptor = descriptor
        params = {
            'descriptor': permission_descriptor.to_dict(),
            'state': state,
            'origin': origin }
    # WARNING: Decompyle incomplete
