# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: json_context.pyc (Python 3.11)

from enum import Enum, auto

class ContextValues(Enum):
    OBJECT_KEY = auto()
    OBJECT_VALUE = auto()
    ARRAY = auto()


class JsonContext:
    
    def __init__(self = None):
        self.context = []
        self.current = None
        self.empty = True

    
    def set(self = None, value = None):
        '''
        Set a new context value.

        Args:
            value (ContextValues): The context value to be added.

        Returns:
            None
        '''
        self.context.append(value)
        self.current = value
        self.empty = False

    
    def reset(self = None):
        '''
        Remove the most recent context value.

        Returns:
            None
        '''
        
        try:
            self.context.pop()
            self.current = self.context[-1]
            return None
        except IndexError:
            self.current = None
            self.empty = True
            return None
