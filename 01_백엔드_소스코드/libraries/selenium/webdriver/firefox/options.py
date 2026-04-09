# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: options.pyc (Python 3.11)

from typing import Any
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.options import ArgOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

class Log:
    
    def __init__(self = None):
        self.level = None

    
    def to_capabilities(self = None):
        if self.level:
            return {
                'log': {
                    'level': self.level } }



class Options(ArgOptions):
    pass
# WARNING: Decompyle incomplete
