# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: script.pyc (Python 3.11)

import datetime
import math
from dataclasses import dataclass
from typing import Any
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.bidi.common import command_builder
from selenium.webdriver.common.bidi.log import LogEntryAdded
from selenium.webdriver.common.bidi.session import Session

class ResultOwnership:
    '''Represents the possible result ownership types.'''
    NONE = 'none'
    ROOT = 'root'


class RealmType:
    '''Represents the possible realm types.'''
    WINDOW = 'window'
    DEDICATED_WORKER = 'dedicated-worker'
    SHARED_WORKER = 'shared-worker'
    SERVICE_WORKER = 'service-worker'
    WORKER = 'worker'
    PAINT_WORKLET = 'paint-worklet'
    AUDIO_WORKLET = 'audio-worklet'
    WORKLET = 'worklet'

RealmInfo = <NODE:12>()
Source = <NODE:12>()
EvaluateResult = <NODE:12>()

class ScriptMessage:
    '''Represents a script message event.'''
    event_class = 'script.message'
    
    def __init__(self = None, channel = None, data = None, source = ('channel', str, 'data', dict, 'source', Source)):
        self.channel = channel
        self.data = data
        self.source = source

    from_json = (lambda cls = None, json = None: if 'channel' not in json:
raise ValueError("Missing required field 'channel' in ScriptMessage")if 'data' not in json:
raise ValueError("Missing required field 'data' in ScriptMessage")if 'source' not in json:
raise ValueError("Missing required field 'source' in ScriptMessage")cls(channel = json['channel'], data = json['data'], source = Source.from_json(json['source'])))()


class RealmCreated:
    '''Represents a realm created event.'''
    event_class = 'script.realmCreated'
    
    def __init__(self = None, realm_info = None):
        self.realm_info = realm_info

    from_json = (lambda cls = None, json = None: cls(realm_info = RealmInfo.from_json(json)))()


class RealmDestroyed:
    '''Represents a realm destroyed event.'''
    event_class = 'script.realmDestroyed'
    
    def __init__(self = None, realm = None):
        self.realm = realm

    from_json = (lambda cls = None, json = None: if 'realm' not in json:
raise ValueError("Missing required field 'realm' in RealmDestroyed")cls(realm = json['realm']))()


class Script:
    '''BiDi implementation of the script module.'''
    EVENTS = {
        'message': 'script.message',
        'realm_created': 'script.realmCreated',
        'realm_destroyed': 'script.realmDestroyed' }
    
    def __init__(self, conn, driver = (None,)):
        self.conn = conn
        self.driver = driver
        self.log_entry_subscribed = False
        self.subscriptions = { }
        self.callbacks = { }

    
    def add_console_message_handler(self, handler):
        self._subscribe_to_log_entries()
        return self.conn.add_callback(LogEntryAdded, self._handle_log_entry('console', handler))

    
    def add_javascript_error_handler(self, handler):
        self._subscribe_to_log_entries()
        return self.conn.add_callback(LogEntryAdded, self._handle_log_entry('javascript', handler))

    
    def remove_console_message_handler(self, id):
        self.conn.remove_callback(LogEntryAdded, id)
        self._unsubscribe_from_log_entries()

    remove_javascript_error_handler = remove_console_message_handler
    
    def pin(self = None, script = None):
        '''Pins a script to the current browsing context.

        Args:
            script: The script to pin.

        Returns:
            str: The ID of the pinned script.
        '''
        return self._add_preload_script(script)

    
    def unpin(self = None, script_id = None):
        '''Unpins a script from the current browsing context.

        Args:
            script_id: The ID of the pinned script to unpin.
        '''
        self._remove_preload_script(script_id)

    
    def execute(self = None, script = None, *args):
        '''Executes a script in the current browsing context.

        Args:
            script: The script function to execute.
            *args: Arguments to pass to the script function.

        Returns:
            dict: The result value from the script execution.

        Raises:
            WebDriverException: If the script execution fails.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __convert_to_local_value(self = None, value = None):
        '''Converts a Python value to BiDi LocalValue format.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _add_preload_script(self, function_declaration = None, arguments = None, contexts = None, user_contexts = (None, None, None, None), sandbox = ('function_declaration', str, 'arguments', list[dict[(str, Any)]] | None, 'contexts', list[str] | None, 'user_contexts', list[str] | None, 'sandbox', str | None, 'return', str)):
        '''Adds a preload script.

        Args:
            function_declaration: The function declaration to preload.
            arguments: The arguments to pass to the function.
            contexts: The browsing context IDs to apply the script to.
            user_contexts: The user context IDs to apply the script to.
            sandbox: The sandbox name to apply the script to.

        Returns:
            str: The preload script ID.

        Raises:
            ValueError: If both contexts and user_contexts are provided.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _remove_preload_script(self = None, script_id = None):
        '''Removes a preload script.

        Args:
            script_id: The preload script ID to remove.
        '''
        params = {
            'script': script_id }
        self.conn.execute(command_builder('script.removePreloadScript', params))

    
    def _disown(self = None, handles = None, target = None):
        '''Disowns the given handles.

        Args:
            handles: The handles to disown.
            target: The target realm or context.
        '''
        params = {
            'handles': handles,
            'target': target }
        self.conn.execute(command_builder('script.disown', params))

    
    def _call_function(self, function_declaration, await_promise, target, arguments = None, result_ownership = None, serialization_options = None, this = (None, None, None, None, False), user_activation = ('function_declaration', str, 'await_promise', bool, 'target', dict, 'arguments', list[dict] | None, 'result_ownership', str | None, 'serialization_options', dict | None, 'this', dict | None, 'user_activation', bool, 'return', EvaluateResult)):
        """Calls a provided function with given arguments in a given realm.

        Args:
            function_declaration: The function declaration to call.
            await_promise: Whether to await promise resolution.
            target: The target realm or context.
            arguments: The arguments to pass to the function.
            result_ownership: The result ownership type.
            serialization_options: The serialization options.
            this: The 'this' value for the function call.
            user_activation: Whether to trigger user activation.

        Returns:
            EvaluateResult: The result of the function call.
        """
        params = {
            'functionDeclaration': function_declaration,
            'awaitPromise': await_promise,
            'target': target,
            'userActivation': user_activation }
    # WARNING: Decompyle incomplete

    
    def _evaluate(self, expression, target = None, await_promise = None, result_ownership = None, serialization_options = (None, None, False), user_activation = ('expression', str, 'target', dict, 'await_promise', bool, 'result_ownership', str | None, 'serialization_options', dict | None, 'user_activation', bool, 'return', EvaluateResult)):
        '''Evaluates a provided script in a given realm.

        Args:
            expression: The script expression to evaluate.
            target: The target realm or context.
            await_promise: Whether to await promise resolution.
            result_ownership: The result ownership type.
            serialization_options: The serialization options.
            user_activation: Whether to trigger user activation.

        Returns:
            EvaluateResult: The result of the script evaluation.
        '''
        params = {
            'expression': expression,
            'target': target,
            'awaitPromise': await_promise,
            'userActivation': user_activation }
    # WARNING: Decompyle incomplete

    
    def _get_realms(self = None, context = None, type = None):
        '''Returns a list of all realms, optionally filtered.

        Args:
            context: The browsing context ID to filter by.
            type: The realm type to filter by.

        Returns:
            List[RealmInfo]: A list of realm information.
        '''
        params = { }
    # WARNING: Decompyle incomplete

    
    def _subscribe_to_log_entries(self):
        if not self.log_entry_subscribed:
            session = Session(self.conn)
            self.conn.execute(session.subscribe(LogEntryAdded.event_class))
            self.log_entry_subscribed = True
            return None

    
    def _unsubscribe_from_log_entries(self):
        if self.log_entry_subscribed or LogEntryAdded.event_class not in self.conn.callbacks:
            session = Session(self.conn)
            self.conn.execute(session.unsubscribe(LogEntryAdded.event_class))
            self.log_entry_subscribed = False
            return None
        return None

    
    def _handle_log_entry(self, type, handler):
        pass
    # WARNING: Decompyle incomplete
