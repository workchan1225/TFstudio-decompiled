# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: session.pyc (Python 3.11)

from selenium.webdriver.common.bidi.common import command_builder

class UserPromptHandlerType:
    '''Represents the behavior of the user prompt handler.'''
    ACCEPT = 'accept'
    DISMISS = 'dismiss'
    IGNORE = 'ignore'
    VALID_TYPES = {
        ACCEPT,
        DISMISS,
        IGNORE}


class UserPromptHandler:
    '''Represents the configuration of the user prompt handler.'''
    
    def __init__(self, alert, before_unload = None, confirm = None, default = None, file = (None, None, None, None, None, None), prompt = ('alert', str | None, 'before_unload', str | None, 'confirm', str | None, 'default', str | None, 'file', str | None, 'prompt', str | None)):
        '''Initialize UserPromptHandler.

        Args:
            alert: Handler type for alert prompts.
            before_unload: Handler type for beforeUnload prompts.
            confirm: Handler type for confirm prompts.
            default: Default handler type for all prompts.
            file: Handler type for file picker prompts.
            prompt: Handler type for prompt dialogs.

        Raises:
            ValueError: If any handler type is not valid.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def to_dict(self = None):
        '''Convert the UserPromptHandler to a dictionary for BiDi protocol.

        Returns:
            Dictionary representation suitable for BiDi protocol.
        '''
        field_mapping = {
            'alert': 'alert',
            'before_unload': 'beforeUnload',
            'confirm': 'confirm',
            'default': 'default',
            'file': 'file',
            'prompt': 'prompt' }
        result = { }
    # WARNING: Decompyle incomplete



class Session:
    
    def __init__(self, conn):
        self.conn = conn

    
    def subscribe(self = None, *, browsing_contexts, *events):
        params = {
            'events': events }
    # WARNING: Decompyle incomplete

    
    def unsubscribe(self = None, *, browsing_contexts, *events):
        params = {
            'events': events }
    # WARNING: Decompyle incomplete

    
    def status(self):
        """The session.status command returns information about the remote end's readiness.

        Returns information about the remote end's readiness to create new sessions
        and may include implementation-specific metadata.

        Returns:
            Dictionary containing the ready state (bool), message (str) and metadata.
        """
        cmd = command_builder('session.status', { })
        return self.conn.execute(cmd)
