# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: browser.pyc (Python 3.11)

import os
from typing import Any
from selenium.webdriver.common.bidi.common import command_builder
from selenium.webdriver.common.bidi.session import UserPromptHandler
from selenium.webdriver.common.proxy import Proxy

class ClientWindowState:
    '''Represents a window state.'''
    FULLSCREEN = 'fullscreen'
    MAXIMIZED = 'maximized'
    MINIMIZED = 'minimized'
    NORMAL = 'normal'
    VALID_STATES = {
        FULLSCREEN,
        MAXIMIZED,
        MINIMIZED,
        NORMAL}


class ClientWindowInfo:
    '''Represents a client window information.'''
    
    def __init__(self, client_window, state, width, height = None, x = None, y = None, active = ('client_window', str, 'state', str, 'width', int, 'height', int, 'x', int, 'y', int, 'active', bool)):
        self.client_window = client_window
        self.state = state
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.active = active

    
    def get_state(self = None):
        '''Gets the state of the client window.

        Returns:
            str: The state of the client window (one of the ClientWindowState constants).
        '''
        return self.state

    
    def get_client_window(self = None):
        '''Gets the client window identifier.

        Returns:
            str: The client window identifier.
        '''
        return self.client_window

    
    def get_width(self = None):
        '''Gets the width of the client window.

        Returns:
            int: The width of the client window.
        '''
        return self.width

    
    def get_height(self = None):
        '''Gets the height of the client window.

        Returns:
            int: The height of the client window.
        '''
        return self.height

    
    def get_x(self = None):
        '''Gets the x coordinate of the client window.

        Returns:
            int: The x coordinate of the client window.
        '''
        return self.x

    
    def get_y(self = None):
        '''Gets the y coordinate of the client window.

        Returns:
            int: The y coordinate of the client window.
        '''
        return self.y

    
    def is_active(self = None):
        '''Checks if the client window is active.

        Returns:
            bool: True if the client window is active, False otherwise.
        '''
        return self.active

    from_dict = (lambda cls = None, data = None: try:
client_window = data['clientWindow']if not isinstance(client_window, str):
raise ValueError('clientWindow must be a string')state = data['state']if not isinstance(state, str):
raise ValueError('state must be a string')if state not in ClientWindowState.VALID_STATES:
raise ValueError(f'''Invalid state: {state}. Must be one of {ClientWindowState.VALID_STATES}''')width = data['width']if isinstance(width, int) or width < 0:
raise ValueError(f'''width must be a non-negative integer, got {width}''')height = data['height']if isinstance(height, int) or height < 0:
raise ValueError(f'''height must be a non-negative integer, got {height}''')x = data['x']if not isinstance(x, int):
raise ValueError(f'''x must be an integer, got {type(x).__name__}''')y = data['y']if not isinstance(y, int):
raise ValueError(f'''y must be an integer, got {type(y).__name__}''')active = data['active']if not isinstance(active, bool):
raise ValueError('active must be a boolean')cls(client_window = client_window, state = state, width = width, height = height, x = x, y = y, active = active)except (KeyError, TypeError):
e = Noneraise ValueError(f'''Invalid data format for ClientWindowInfo: {e}'''), ee = Nonedel e)()


class Browser:
    '''BiDi implementation of the browser module.'''
    
    def __init__(self, conn):
        self.conn = conn

    
    def create_user_context(self = None, accept_insecure_certs = None, proxy = None, unhandled_prompt_behavior = (None, None, None)):
        '''Creates a new user context.

        Args:
            accept_insecure_certs: Optional flag to accept insecure TLS certificates.
            proxy: Optional proxy configuration for the user context.
            unhandled_prompt_behavior: Optional configuration for handling user prompts.

        Returns:
            str: The ID of the created user context.
        '''
        params = { }
    # WARNING: Decompyle incomplete

    
    def get_user_contexts(self = None):
        '''Gets all user contexts.

        Returns:
            List[str]: A list of user context IDs.
        '''
        result = self.conn.execute(command_builder('browser.getUserContexts', { }))
        return result['userContexts']()

    
    def remove_user_context(self = None, user_context_id = None):
        '''Removes a user context.

        Args:
            user_context_id: The ID of the user context to remove.

        Raises:
            ValueError: If the user context ID is "default" or does not exist.
        '''
        if user_context_id == 'default':
            raise ValueError('Cannot remove the default user context')
        params = {
            'userContext': user_context_id }
        self.conn.execute(command_builder('browser.removeUserContext', params))

    
    def get_client_windows(self = None):
        '''Gets all client windows.

        Returns:
            List[ClientWindowInfo]: A list of client window information.
        '''
        result = self.conn.execute(command_builder('browser.getClientWindows', { }))
        return result['clientWindows']()

    
    def set_download_behavior(self = None, *, allowed, destination_folder, user_contexts):
        '''Set the download behavior for the browser or specific user contexts.

        Args:
            allowed: True to allow downloads, False to deny downloads, or None to
                clear download behavior (revert to default).
            destination_folder: Required when allowed is True. Specifies the folder
                to store downloads in.
            user_contexts: Optional list of user context IDs to apply this
                behavior to. If omitted, updates the default behavior.

        Raises:
            ValueError: If allowed=True and destination_folder is missing, or if
                allowed=False and destination_folder is provided.
        '''
        params = { }
    # WARNING: Decompyle incomplete
