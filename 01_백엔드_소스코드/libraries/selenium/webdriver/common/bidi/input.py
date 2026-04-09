# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: input.pyc (Python 3.11)

import math
from dataclasses import dataclass, field
from typing import Any
from selenium.webdriver.common.bidi.common import command_builder
from selenium.webdriver.common.bidi.session import Session

class PointerType:
    '''Represents the possible pointer types.'''
    MOUSE = 'mouse'
    PEN = 'pen'
    TOUCH = 'touch'
    VALID_TYPES = {
        MOUSE,
        PEN,
        TOUCH}


class Origin:
    '''Represents the possible origin types.'''
    VIEWPORT = 'viewport'
    POINTER = 'pointer'

ElementOrigin = <NODE:12>()
PointerParameters = <NODE:12>()
PointerCommonProperties = <NODE:12>()
PauseAction = <NODE:12>()
KeyDownAction = <NODE:12>()
KeyUpAction = <NODE:12>()
PointerDownAction = <NODE:12>()
PointerUpAction = <NODE:12>()
PointerMoveAction = <NODE:12>()
WheelScrollAction = <NODE:12>()
NoneSourceActions = <NODE:12>()
KeySourceActions = <NODE:12>()
PointerSourceActions = <NODE:12>()
WheelSourceActions = <NODE:12>()
FileDialogInfo = <NODE:12>()

class FileDialogOpened:
    '''Event class for input.fileDialogOpened event.'''
    event_class = 'input.fileDialogOpened'
    from_json = (lambda cls, json: FileDialogInfo.from_dict(json))()


class Input:
    '''BiDi implementation of the input module.'''
    
    def __init__(self, conn):
        self.conn = conn
        self.subscriptions = { }
        self.callbacks = { }

    
    def perform_actions(self = None, context = None, actions = None):
        '''Performs a sequence of user input actions.

        Args:
            context: The browsing context ID where actions should be performed.
            actions: A list of source actions to perform.
        '''
        params = {
            'context': (lambda .0: [ action.to_dict() for action in .0 ]),
            'actions': actions() }
        self.conn.execute(command_builder('input.performActions', params))

    
    def release_actions(self = None, context = None):
        '''Releases all input state for the given context.

        Args:
            context: The browsing context ID to release actions for.
        '''
        params = {
            'context': context }
        self.conn.execute(command_builder('input.releaseActions', params))

    
    def set_files(self = None, context = None, element = None, files = ('context', str, 'element', dict, 'files', list[str], 'return', None)):
        '''Sets files for a file input element.

        Args:
            context: The browsing context ID.
            element: The element reference (script.SharedReference).
            files: A list of file paths to set.
        '''
        params = {
            'context': context,
            'element': element,
            'files': files }
        self.conn.execute(command_builder('input.setFiles', params))

    
    def add_file_dialog_handler(self = None, handler = None):
        '''Add a handler for file dialog opened events.

        Args:
            handler: Callback function that takes a FileDialogInfo object.

        Returns:
            int: Callback ID for removing the handler later.
        '''
        if FileDialogOpened.event_class not in self.subscriptions:
            session = Session(self.conn)
            self.conn.execute(session.subscribe(FileDialogOpened.event_class))
            self.subscriptions[FileDialogOpened.event_class] = []
        callback_id = self.conn.add_callback(FileDialogOpened, handler)
        self.subscriptions[FileDialogOpened.event_class].append(callback_id)
        self.callbacks[callback_id] = handler
        return callback_id

    
    def remove_file_dialog_handler(self = None, callback_id = None):
        '''Remove a file dialog handler.

        Args:
            callback_id: The callback ID returned by add_file_dialog_handler.
        '''
        if callback_id in self.callbacks:
            del self.callbacks[callback_id]
        if FileDialogOpened.event_class in self.subscriptions:
            if callback_id in self.subscriptions[FileDialogOpened.event_class]:
                self.subscriptions[FileDialogOpened.event_class].remove(callback_id)
            if not self.subscriptions[FileDialogOpened.event_class]:
                session = Session(self.conn)
                self.conn.execute(session.unsubscribe(FileDialogOpened.event_class))
                del self.subscriptions[FileDialogOpened.event_class]
        self.conn.remove_callback(FileDialogOpened, callback_id)
