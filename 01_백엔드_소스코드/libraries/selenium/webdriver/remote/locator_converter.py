# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: locator_converter.pyc (Python 3.11)

from selenium.common.exceptions import InvalidSelectorException
from selenium.webdriver.common.by import By

class LocatorConverter:
    
    def convert(self, by, value):
        if by == By.ID:
            return (By.CSS_SELECTOR, f'''[id="{value}"]''')
        if None == By.CLASS_NAME:
            if value and (lambda .0: pass# WARNING: Decompyle incomplete
)(value.strip()()):
                raise InvalidSelectorException('Compound class names are not allowed.')
            return (By.CSS_SELECTOR, f'''.{value}''')
        if None == By.NAME:
            return (By.CSS_SELECTOR, f'''[name="{value}"]''')
        return (None, value)
