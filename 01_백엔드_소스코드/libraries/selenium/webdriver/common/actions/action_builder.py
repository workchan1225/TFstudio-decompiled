# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: action_builder.pyc (Python 3.11)

from typing import Any, Union
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.key_actions import KeyActions
from selenium.webdriver.common.actions.key_input import KeyInput
from selenium.webdriver.common.actions.pointer_actions import PointerActions
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.wheel_actions import WheelActions
from selenium.webdriver.common.actions.wheel_input import WheelInput
from selenium.webdriver.remote.command import Command

class ActionBuilder:
    
    def __init__(self, driver = None, mouse = None, wheel = None, keyboard = (None, None, None, 250), duration = ('mouse', PointerInput | None, 'wheel', WheelInput | None, 'keyboard', KeyInput | None, 'duration', int, 'return', None)):
