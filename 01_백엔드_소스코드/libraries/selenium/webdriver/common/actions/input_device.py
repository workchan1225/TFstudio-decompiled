# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: input_device.pyc (Python 3.11)

import uuid
from typing import Any

class InputDevice:
    '''Describes the input device being used for the action.'''
    
    def __init__(self = None, name = None):
        if not name:
            pass
        self.name = uuid.uuid4()
        self.actions = []

    
    def add_action(self = None, action = None):
        self.actions.append(action)

    
    def clear_actions(self = None):
        self.actions = []

    
    def create_pause(self = None, duration = None):
        pass
