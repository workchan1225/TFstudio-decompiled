# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: interaction.pyc (Python 3.11)

from selenium.webdriver.common.actions.input_device import InputDevice
KEY = 'key'
POINTER = 'pointer'
NONE = 'none'
WHEEL = 'wheel'
SOURCE_TYPES = {
    KEY,
    POINTER,
    WHEEL,
    NONE}
POINTER_MOUSE = 'mouse'
POINTER_TOUCH = 'touch'
POINTER_PEN = 'pen'
POINTER_KINDS = {
    POINTER_MOUSE,
    POINTER_TOUCH,
    POINTER_PEN}

class Interaction:
    PAUSE = 'pause'
    
    def __init__(self = None, source = None):
        self.source = source



class Pause(Interaction):
    pass
# WARNING: Decompyle incomplete
