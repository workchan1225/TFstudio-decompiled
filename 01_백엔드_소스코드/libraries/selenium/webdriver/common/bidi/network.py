# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: network.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Callable
from typing import Any
from selenium.webdriver.common.bidi.common import command_builder
from selenium.webdriver.remote.websocket_connection import WebSocketConnection

class NetworkEvent:
    '''Represents a network event.'''
    
    def __init__(self = None, event_class = None, **kwargs):
        self.event_class = event_class
        self.params = kwargs

    from_json = (lambda cls = None, json = None: pass# WARNING: Decompyle incomplete
)()


class Network:
    EVENTS = {
        'before_request': 'network.beforeRequestSent',
        'response_started': 'network.responseStarted',
        'response_completed': 'network.responseCompleted',
        'auth_required': 'network.authRequired',
        'fetch_error': 'network.fetchError',
        'continue_request': 'network.continueRequest',
        'continue_auth': 'network.continueWithAuth' }
    PHASES = {
        'before_request': 'beforeRequestSent',
        'response_started': 'responseStarted',
        'auth_required': 'authRequired' }
    
    def __init__(self = None, conn = None):
        self.conn = conn
        self.intercepts = []
        self.callbacks = { }
        self.subscriptions = { }

    
    def _add_intercept(self = None, phases = None, contexts = None, url_patterns = (None, None, None)):
        '''Add an intercept to the network.

        Args:
            phases: A list of phases to intercept. Default is None (empty list).
            contexts: A list of contexts to intercept. Default is None.
            url_patterns: A list of URL patterns to intercept. Default is None.

        Returns:
            str: intercept id
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _remove_intercept(self = None, intercept = None):
        '''Remove a specific intercept, or all intercepts.

        Args:
            intercept: The intercept to remove. Default is None.

        Raises:
            ValueError: If intercept is not found.

        Note:
            If intercept is None, all intercepts will be removed.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _on_request(self = None, event_name = None, callback = None):
        '''Set a callback function to subscribe to a network event.

        Args:
            event_name: The event to subscribe to.
            callback: The callback function to execute on event.
                Takes Request object as argument.

        Returns:
            int: callback id
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def add_request_handler(self = None, event = None, callback = None, url_patterns = (None, None), contexts = ('event', 'str', 'callback', 'Callable[[Request], Any]', 'url_patterns', 'list[Any] | None', 'contexts', 'list[str] | None', 'return', 'int')):
        '''Add a request handler to the network.

        Args:
            event: The event to subscribe to.
            callback: The callback function to execute on request interception.
                Takes Request object as argument.
            url_patterns: A list of URL patterns to intercept. Default is None.
            contexts: A list of contexts to intercept. Default is None.

        Returns:
            int: callback id
        '''
        
        try:
            event_name = self.EVENTS[event]
            phase_name = self.PHASES[event]
        except KeyError:
            raise Exception(f'''Event {event} not found''')

        result = self._add_intercept(phases = [
            phase_name], url_patterns = url_patterns, contexts = contexts)
        callback_id = self._on_request(event_name, callback)
        if event_name in self.subscriptions:
            self.subscriptions[event_name].append(callback_id)
        else:
            params = { }
            params['events'] = [
                event_name]
            self.conn.execute(command_builder('session.subscribe', params))
            self.subscriptions[event_name] = [
                callback_id]
        self.callbacks[callback_id] = result['intercept']
        return callback_id

    
    def remove_request_handler(self = None, event = None, callback_id = None):
        '''Remove a request handler from the network.

        Args:
            event: The event to unsubscribe from.
            callback_id: The callback id to remove.
        '''
        
        try:
            event_name = self.EVENTS[event]
        except KeyError:
            raise Exception(f'''Event {event} not found''')

        net_event = NetworkEvent(event_name)
        self.conn.remove_callback(net_event, callback_id)
        self._remove_intercept(self.callbacks[callback_id])
        del self.callbacks[callback_id]
        self.subscriptions[event_name].remove(callback_id)
        if len(self.subscriptions[event_name]) == 0:
            params = { }
            params['events'] = [
                event_name]
            self.conn.execute(command_builder('session.unsubscribe', params))
            del self.subscriptions[event_name]
            return None

    
    def clear_request_handlers(self = None):
        '''Clear all request handlers from the network.'''
        for event_name in self.subscriptions:
            net_event = NetworkEvent(event_name)
            for callback_id in self.subscriptions[event_name]:
                self.conn.remove_callback(net_event, callback_id)
                self._remove_intercept(self.callbacks[callback_id])
                del self.callbacks[callback_id]
                params = { }
                params['events'] = [
                    event_name]
                self.conn.execute(command_builder('session.unsubscribe', params))
                self.subscriptions = { }
                return None

    
    def add_auth_handler(self = None, username = None, password = None):
        '''Add an authentication handler to the network.

        Args:
            username: The username to authenticate with.
            password: The password to authenticate with.

        Returns:
            int: callback id
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def remove_auth_handler(self = None, callback_id = None):
        '''Remove an authentication handler from the network.

        Args:
            callback_id: The callback id to remove.
        '''
        event = 'auth_required'
        self.remove_request_handler(event, callback_id)



class Request:
    '''Represents an intercepted network request.'''
    
    def __init__(self, network, request_id, body_size, cookies, resource_type, headers = None, headers_size = None, method = None, timings = (None, None, None, None, None, None, None, None), url = ('network', 'Network', 'request_id', 'Any', 'body_size', 'int | None', 'cookies', 'Any', 'resource_type', 'str | None', 'headers', 'Any', 'headers_size', 'int | None', 'method', 'str | None', 'timings', 'Any', 'url', 'str | None', 'return', 'None')):
        self.network = network
        self.request_id = request_id
        self.body_size = body_size
        self.cookies = cookies
        self.resource_type = resource_type
        self.headers = headers
        self.headers_size = headers_size
        self.method = method
        self.timings = timings
        self.url = url

    
    def fail_request(self = None):
        '''Fail this request.'''
        if not self.request_id:
            raise ValueError('Request not found.')
        params = {
            'request': self.request_id }
        self.network.conn.execute(command_builder('network.failRequest', params))

    
    def continue_request(self, body = None, method = None, headers = None, cookies = (None, None, None, None, None), url = ('body', 'Any', 'method', 'str | None', 'headers', 'Any', 'cookies', 'Any', 'url', 'str | None', 'return', 'None')):
        '''Continue after intercepting this request.'''
        if not self.request_id:
            raise ValueError('Request not found.')
        params = {
            'request': self.request_id }
    # WARNING: Decompyle incomplete

    
    def _continue_with_auth(self = None, username = None, password = None):
        '''Continue with authentication.

        Args:
            username: The username to authenticate with.
            password: The password to authenticate with.

        Note:
            If username or password is None, it attempts auth with no credentials.
        '''
        params = { }
        params['request'] = self.request_id
        if not username or password:
            params['action'] = 'default'
        else:
            params['action'] = 'provideCredentials'
            params['credentials'] = {
                'type': 'password',
                'username': username,
                'password': password }
        self.network.conn.execute(command_builder('network.continueWithAuth', params))
