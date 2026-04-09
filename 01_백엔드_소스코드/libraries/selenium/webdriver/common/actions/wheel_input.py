# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: wheel_input.pyc (Python 3.11)

from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.input_device import InputDevice
from selenium.webdriver.remote.webelement import WebElement

class ScrollOrigin:
    
    def __init__(self = None, origin = None, x_offset = None, y_offset = ('origin', str | WebElement, 'x_offset', int, 'y_offset', int, 'return', None)):
        self._origin = origin
        self._x_offset = x_offset
        self._y_offset = y_offset

    from_element = (lambda cls = None, element = None, x_offset = classmethod, y_offset = (0, 0): cls(element, x_offset, y_offset))()
    from_viewport = (lambda cls = None, x_offset = None, y_offset = classmethod: cls('viewport', x_offset, y_offset))()
    origin = (lambda self = None: self._origin)()
    x_offset = (lambda self = None: self._x_offset)()
    y_offset = (lambda self = None: self._y_offset)()


class WheelInput(InputDevice):
    pass
# WARNING: Decompyle incomplete
