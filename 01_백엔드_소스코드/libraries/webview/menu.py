# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: menu.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Callable
from typing import Any, Union

class Menu:
    
    def __init__(self = None, title = None, items = None):
        '''
        Args:
            title: the menu or submenu title
            items: the contents of the menu (can consist of Menu, MenuAction, or MenuSeparator instances)
        '''
        self.title = title
        self.items = items



class MenuAction:
    
    def __init__(self = None, title = None, function = None):
        self.title = title
        self.function = function



class MenuSeparator:
    pass
