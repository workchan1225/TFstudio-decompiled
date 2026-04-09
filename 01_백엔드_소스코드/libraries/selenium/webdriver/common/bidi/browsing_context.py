# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: browsing_context.pyc (Python 3.11)

import threading
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
from typing_extensions import Sentinel
from selenium.webdriver.common.bidi.common import command_builder
from selenium.webdriver.common.bidi.session import Session
UNDEFINED = Sentinel('UNDEFINED')

class ReadinessState:
    '''Represents the stage of document loading at which a navigation command will return.'''
    NONE = 'none'
    INTERACTIVE = 'interactive'
    COMPLETE = 'complete'


class UserPromptType:
    '''Represents the possible user prompt types.'''
    ALERT = 'alert'
    BEFORE_UNLOAD = 'beforeunload'
    CONFIRM = 'confirm'
    PROMPT = 'prompt'


class NavigationInfo:
    '''Provides details of an ongoing navigation.'''
    
    def __init__(self, context = None, navigation = None, timestamp = None, url = ('context', str, 'navigation', str | None, 'timestamp', int, 'url', str)):
        self.context = context
        self.navigation = navigation
        self.timestamp = timestamp
        self.url = url

    from_json = (lambda cls = None, json = None: context = json.get('context')# WARNING: Decompyle incomplete
)()


class BrowsingContextInfo:
    '''Represents the properties of a navigable.'''
    
    def __init__(self, context, url, children = None, client_window = None, user_context = None, parent = (None, None), original_opener = ('context', str, 'url', str, 'children', list['BrowsingContextInfo'] | None, 'client_window', str, 'user_context', str, 'parent', str | None, 'original_opener', str | None)):
        self.context = context
        self.url = url
        self.children = children
        self.parent = parent
        self.user_context = user_context
        self.original_opener = original_opener
        self.client_window = client_window

    from_json = (lambda cls = None, json = None: children = Noneraw_children = json.get('children')# WARNING: Decompyle incomplete
)()


class DownloadWillBeginParams(NavigationInfo):
    pass
# WARNING: Decompyle incomplete


class UserPromptOpenedParams:
    '''Parameters for the userPromptOpened event.'''
    
    def __init__(self, context = None, handler = None, message = None, type = (None,), default_value = ('context', str, 'handler', str, 'message', str, 'type', str, 'default_value', str | None)):
        self.context = context
        self.handler = handler
        self.message = message
        self.type = type
        self.default_value = default_value

    from_json = (lambda cls = None, json = None: context = json.get('context')# WARNING: Decompyle incomplete
)()


class UserPromptClosedParams:
    '''Parameters for the userPromptClosed event.'''
    
    def __init__(self = None, context = None, accepted = None, type = (None,), user_text = ('context', str, 'accepted', bool, 'type', str, 'user_text', str | None)):
        self.context = context
        self.accepted = accepted
        self.type = type
        self.user_text = user_text

    from_json = (lambda cls = None, json = None: context = json.get('context')# WARNING: Decompyle incomplete
)()


class HistoryUpdatedParams:
    '''Parameters for the historyUpdated event.'''
    
    def __init__(self = None, context = None, timestamp = None, url = ('context', str, 'timestamp', int, 'url', str)):
        self.context = context
        self.timestamp = timestamp
        self.url = url

    from_json = (lambda cls = None, json = None: context = json.get('context')# WARNING: Decompyle incomplete
)()


class DownloadCanceledParams(NavigationInfo):
    pass
# WARNING: Decompyle incomplete


class DownloadCompleteParams(NavigationInfo):
    pass
# WARNING: Decompyle incomplete


class DownloadEndParams:
    '''Parameters for the downloadEnd event.'''
    
    def __init__(self = None, download_params = None):
        self.download_params = download_params

    from_json = (lambda cls = None, json = None: status = json.get('status')if status == 'canceled':
cls(DownloadCanceledParams.from_json(json))if None == 'complete':
cls(DownloadCompleteParams.from_json(json))raise None("status must be either 'canceled' or 'complete'"))()


class ContextCreated:
    '''Event class for browsingContext.contextCreated event.'''
    event_class = 'browsingContext.contextCreated'
    from_json = (lambda cls = None, json = None: if isinstance(json, BrowsingContextInfo):
jsonNone.from_json(json))()


class ContextDestroyed:
    '''Event class for browsingContext.contextDestroyed event.'''
    event_class = 'browsingContext.contextDestroyed'
    from_json = (lambda cls = None, json = None: if isinstance(json, BrowsingContextInfo):
jsonNone.from_json(json))()


class NavigationStarted:
    '''Event class for browsingContext.navigationStarted event.'''
    event_class = 'browsingContext.navigationStarted'
    from_json = (lambda cls = None, json = None: if isinstance(json, NavigationInfo):
jsonNone.from_json(json))()


class NavigationCommitted:
    '''Event class for browsingContext.navigationCommitted event.'''
    event_class = 'browsingContext.navigationCommitted'
    from_json = (lambda cls = None, json = None: if isinstance(json, NavigationInfo):
jsonNone.from_json(json))()


class NavigationFailed:
    '''Event class for browsingContext.navigationFailed event.'''
    event_class = 'browsingContext.navigationFailed'
    from_json = (lambda cls = None, json = None: if isinstance(json, NavigationInfo):
jsonNone.from_json(json))()


class NavigationAborted:
    '''Event class for browsingContext.navigationAborted event.'''
    event_class = 'browsingContext.navigationAborted'
    from_json = (lambda cls = None, json = None: if isinstance(json, NavigationInfo):
jsonNone.from_json(json))()


class DomContentLoaded:
    '''Event class for browsingContext.domContentLoaded event.'''
    event_class = 'browsingContext.domContentLoaded'
    from_json = (lambda cls = None, json = None: if isinstance(json, NavigationInfo):
jsonNone.from_json(json))()


class Load:
    '''Event class for browsingContext.load event.'''
    event_class = 'browsingContext.load'
    from_json = (lambda cls = None, json = None: if isinstance(json, NavigationInfo):
jsonNone.from_json(json))()


class FragmentNavigated:
    '''Event class for browsingContext.fragmentNavigated event.'''
    event_class = 'browsingContext.fragmentNavigated'
    from_json = (lambda cls = None, json = None: if isinstance(json, NavigationInfo):
jsonNone.from_json(json))()


class DownloadWillBegin:
    '''Event class for browsingContext.downloadWillBegin event.'''
    event_class = 'browsingContext.downloadWillBegin'
    from_json = (lambda cls = None, json = None: DownloadWillBeginParams.from_json(json))()


class UserPromptOpened:
    '''Event class for browsingContext.userPromptOpened event.'''
    event_class = 'browsingContext.userPromptOpened'
    from_json = (lambda cls = None, json = None: UserPromptOpenedParams.from_json(json))()


class UserPromptClosed:
    '''Event class for browsingContext.userPromptClosed event.'''
    event_class = 'browsingContext.userPromptClosed'
    from_json = (lambda cls = None, json = None: UserPromptClosedParams.from_json(json))()


class HistoryUpdated:
    '''Event class for browsingContext.historyUpdated event.'''
    event_class = 'browsingContext.historyUpdated'
    from_json = (lambda cls = None, json = None: HistoryUpdatedParams.from_json(json))()


class DownloadEnd:
    '''Event class for browsingContext.downloadEnd event.'''
    event_class = 'browsingContext.downloadEnd'
    from_json = (lambda cls = None, json = None: DownloadEndParams.from_json(json))()

EventConfig = <NODE:12>()

class _EventManager:
    '''Class to manage event subscriptions and callbacks for BrowsingContext.'''
    
    def __init__(self = None, conn = None, event_configs = None):
        self.conn = conn
        self.event_configs = event_configs
        self.subscriptions = { }
        self._bidi_to_class = event_configs.values()()
        self._available_events = ', '.join(sorted(event_configs.keys()))
        self._subscription_lock = threading.Lock()

    
    def validate_event(self = None, event = None):
        event_config = self.event_configs.get(event)
        if not event_config:
            raise ValueError(f'''Event \'{event}\' not found. Available events: {self._available_events}''')
        return event_config

    
    def subscribe_to_event(self = None, bidi_event = None, contexts = None):
        '''Subscribe to a BiDi event if not already subscribed.

        Args:
            bidi_event: The BiDi event name.
            contexts: Optional browsing context IDs to subscribe to.
        '''
        self._subscription_lock
        if bidi_event not in self.subscriptions:
            session = Session(self.conn)
            self.conn.execute(session.subscribe(bidi_event, browsing_contexts = contexts))
            self.subscriptions[bidi_event] = []
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def unsubscribe_from_event(self = None, bidi_event = None):
        '''Unsubscribe from a BiDi event if no more callbacks exist.

        Args:
            bidi_event: The BiDi event name.
        '''
        self._subscription_lock
        callback_list = self.subscriptions.get(bidi_event)
    # WARNING: Decompyle incomplete

    
    def add_callback_to_tracking(self = None, bidi_event = None, callback_id = None):
        self._subscription_lock
        self.subscriptions[bidi_event].append(callback_id)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def remove_callback_from_tracking(self = None, bidi_event = None, callback_id = None):
        self._subscription_lock
        callback_list = self.subscriptions.get(bidi_event)
        if callback_list and callback_id in callback_list:
            callback_list.remove(callback_id)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def add_event_handler(self = None, event = None, callback = None, contexts = (None,)):
        event_config = self.validate_event(event)
        callback_id = self.conn.add_callback(event_config.event_class, callback)
        self.subscribe_to_event(event_config.bidi_event, contexts)
        self.add_callback_to_tracking(event_config.bidi_event, callback_id)
        return callback_id

    
    def remove_event_handler(self = None, event = None, callback_id = None):
        event_config = self.validate_event(event)
        self.conn.remove_callback(event_config.event_class, callback_id)
        self.remove_callback_from_tracking(event_config.bidi_event, callback_id)
        self.unsubscribe_from_event(event_config.bidi_event)

    
    def clear_event_handlers(self = None):
        '''Clear all event handlers from the browsing context.'''
        self._subscription_lock
        if not self.subscriptions:
            None(None, None)
            return None
        session = None(self.conn)
        for bidi_event, callback_ids in list(self.subscriptions.items()):
            event_class = self._bidi_to_class.get(bidi_event)
            if event_class:
                for callback_id in callback_ids:
                    self.conn.remove_callback(event_class, callback_id)
                    self.conn.execute(session.unsubscribe(bidi_event))
                    self.subscriptions.clear()
                    None(None, None)
                    return None
                    with None:
                        if not None:
                            pass



class BrowsingContext:
    '''BiDi implementation of the browsingContext module.'''
    EVENT_CONFIGS = {
        'context_created': EventConfig('context_created', 'browsingContext.contextCreated', ContextCreated),
        'context_destroyed': EventConfig('context_destroyed', 'browsingContext.contextDestroyed', ContextDestroyed),
        'dom_content_loaded': EventConfig('dom_content_loaded', 'browsingContext.domContentLoaded', DomContentLoaded),
        'download_end': EventConfig('download_end', 'browsingContext.downloadEnd', DownloadEnd),
        'download_will_begin': EventConfig('download_will_begin', 'browsingContext.downloadWillBegin', DownloadWillBegin),
        'fragment_navigated': EventConfig('fragment_navigated', 'browsingContext.fragmentNavigated', FragmentNavigated),
        'history_updated': EventConfig('history_updated', 'browsingContext.historyUpdated', HistoryUpdated),
        'load': EventConfig('load', 'browsingContext.load', Load),
        'navigation_aborted': EventConfig('navigation_aborted', 'browsingContext.navigationAborted', NavigationAborted),
        'navigation_committed': EventConfig('navigation_committed', 'browsingContext.navigationCommitted', NavigationCommitted),
        'navigation_failed': EventConfig('navigation_failed', 'browsingContext.navigationFailed', NavigationFailed),
        'navigation_started': EventConfig('navigation_started', 'browsingContext.navigationStarted', NavigationStarted),
        'user_prompt_closed': EventConfig('user_prompt_closed', 'browsingContext.userPromptClosed', UserPromptClosed),
        'user_prompt_opened': EventConfig('user_prompt_opened', 'browsingContext.userPromptOpened', UserPromptOpened) }
    
    def __init__(self, conn):
        self.conn = conn
        self._event_manager = _EventManager(conn, self.EVENT_CONFIGS)

    get_event_names = (lambda cls = None: list(cls.EVENT_CONFIGS.keys()))()
    
    def activate(self = None, context = None):
        '''Activates and focuses the given top-level traversable.

        Args:
            context: The browsing context ID to activate.

        Raises:
            Exception: If the browsing context is not a top-level traversable.
        '''
        params = {
            'context': context }
        self.conn.execute(command_builder('browsingContext.activate', params))

    
    def capture_screenshot(self = None, context = None, origin = None, format = ('viewport', None, None), clip = ('context', str, 'origin', str, 'format', dict | None, 'clip', dict | None, 'return', str)):
        '''Captures an image of the given navigable, and returns it as a Base64-encoded string.

        Args:
            context: The browsing context ID to capture.
            origin: The origin of the screenshot, either "viewport" or "document".
            format: The format of the screenshot.
            clip: The clip rectangle of the screenshot.

        Returns:
            The Base64-encoded screenshot.
        '''
        params = {
            'context': context,
            'origin': origin }
    # WARNING: Decompyle incomplete

    
    def close(self = None, context = None, prompt_unload = None):
        '''Closes a top-level traversable.

        Args:
            context: The browsing context ID to close.
            prompt_unload: Whether to prompt to unload.

        Raises:
            Exception: If the browsing context is not a top-level traversable.
        '''
        params = {
            'context': context,
            'promptUnload': prompt_unload }
        self.conn.execute(command_builder('browsingContext.close', params))

    
    def create(self = None, type = None, reference_context = None, background = (None, False, None), user_context = ('type', str, 'reference_context', str | None, 'background', bool, 'user_context', str | None, 'return', str)):
        '''Creates a new navigable, either in a new tab or in a new window, and returns its navigable id.

        Args:
            type: The type of the new navigable, either "tab" or "window".
            reference_context: The reference browsing context ID.
            background: Whether to create the new navigable in the background.
            user_context: The user context ID.

        Returns:
            The browsing context ID of the created navigable.
        '''
        params = {
            'type': type }
    # WARNING: Decompyle incomplete

    
    def get_tree(self = None, max_depth = None, root = None):
        '''Get a tree of all descendent navigables including the given parent itself.

        Returns a tree of all descendent navigables including the given parent itself, or all top-level contexts
        when no parent is provided.

        Args:
            max_depth: The maximum depth of the tree.
            root: The root browsing context ID.

        Returns:
            A list of browsing context information.
        '''
        params = { }
    # WARNING: Decompyle incomplete

    
    def handle_user_prompt(self = None, context = None, accept = None, user_text = (None, None)):
        '''Allows closing an open prompt.

        Args:
            context: The browsing context ID.
            accept: Whether to accept the prompt.
            user_text: The text to enter in the prompt.
        '''
        params = {
            'context': context }
    # WARNING: Decompyle incomplete

    
    def locate_nodes(self, context = None, locator = None, max_node_count = None, serialization_options = (None, None, None), start_nodes = ('context', str, 'locator', dict, 'max_node_count', int | None, 'serialization_options', dict | None, 'start_nodes', list[dict] | None, 'return', list[dict])):
        '''Returns a list of all nodes matching the specified locator.

        Args:
            context: The browsing context ID.
            locator: The locator to use.
            max_node_count: The maximum number of nodes to return.
            serialization_options: The serialization options.
            start_nodes: The start nodes.

        Returns:
            A list of nodes.
        '''
        params = {
            'context': context,
            'locator': locator }
    # WARNING: Decompyle incomplete

    
    def navigate(self = None, context = None, url = None, wait = (None,)):
        '''Navigates a navigable to the given URL.

        Args:
            context: The browsing context ID.
            url: The URL to navigate to.
            wait: The readiness state to wait for.

        Returns:
            A dictionary containing the navigation result.
        '''
        params = {
            'context': context,
            'url': url }
    # WARNING: Decompyle incomplete

    
    def print(self, context, background, margin, orientation = None, page = None, page_ranges = None, scale = (False, None, 'portrait', None, None, 1, True), shrink_to_fit = ('context', str, 'background', bool, 'margin', dict | None, 'orientation', str, 'page', dict | None, 'page_ranges', list[int | str] | None, 'scale', float, 'shrink_to_fit', bool, 'return', str)):
        '''Create a paginated PDF representation of the document as a Base64-encoded string.

        Args:
            context: The browsing context ID.
            background: Whether to include the background.
            margin: The margin parameters.
            orientation: The orientation, either "portrait" or "landscape".
            page: The page parameters.
            page_ranges: The page ranges.
            scale: The scale.
            shrink_to_fit: Whether to shrink to fit.

        Returns:
            The Base64-encoded PDF document.
        '''
        params = {
            'context': context,
            'background': background,
            'orientation': orientation,
            'scale': scale,
            'shrinkToFit': shrink_to_fit }
    # WARNING: Decompyle incomplete

    
    def reload(self = None, context = None, ignore_cache = None, wait = (None, None)):
        '''Reloads a navigable.

        Args:
            context: The browsing context ID.
            ignore_cache: Whether to ignore the cache.
            wait: The readiness state to wait for.

        Returns:
            A dictionary containing the navigation result.
        '''
        params = {
            'context': context }
    # WARNING: Decompyle incomplete

    
    def set_viewport(self = None, context = None, viewport = None, device_pixel_ratio = (None, UNDEFINED, UNDEFINED, None), user_contexts = ('context', str | None, 'viewport', dict | None | Sentinel, 'device_pixel_ratio', float | None | Sentinel, 'user_contexts', list[str] | None, 'return', None)):
        '''Modifies specific viewport characteristics on the given top-level traversable.

        Args:
            context: The browsing context ID.
            viewport: The viewport parameters - {"width": <int>, "height": <int>} (`None` resets to default).
            device_pixel_ratio: The device pixel ratio (`None` resets to default).
            user_contexts: The user context IDs.

        Raises:
            Exception: If the browsing context is not a top-level traversable
            ValueError: If neither `context` nor `user_contexts` is provided
            ValueError: If both `context` and `user_contexts` are provided
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def traverse_history(self = None, context = None, delta = None):
        '''Traverses the history of a given navigable by a delta.

        Args:
            context: The browsing context ID.
            delta: The delta to traverse by.

        Returns:
            A dictionary containing the traverse history result.
        '''
        params = {
            'context': context,
            'delta': delta }
        result = self.conn.execute(command_builder('browsingContext.traverseHistory', params))
        return result

    
    def add_event_handler(self = None, event = None, callback = None, contexts = (None,)):
        '''Add an event handler to the browsing context.

        Args:
            event: The event to subscribe to.
            callback: The callback function to execute on event.
            contexts: The browsing context IDs to subscribe to.

        Returns:
            Callback id.
        '''
        return self._event_manager.add_event_handler(event, callback, contexts)

    
    def remove_event_handler(self = None, event = None, callback_id = None):
        '''Remove an event handler from the browsing context.

        Args:
            event: The event to unsubscribe from.
            callback_id: The callback id to remove.
        '''
        self._event_manager.remove_event_handler(event, callback_id)

    
    def clear_event_handlers(self = None):
        '''Clear all event handlers from the browsing context.'''
        self._event_manager.clear_event_handlers()
