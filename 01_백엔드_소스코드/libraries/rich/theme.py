# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: theme.pyc (Python 3.11)

import configparser
from typing import IO, Dict, List, Mapping, Optional
from default_styles import DEFAULT_STYLES
from style import Style, StyleType

class Theme:
    styles: Dict[(str, Style)] = 'A container for style information, used by :class:`~rich.console.Console`.\n\n    Args:\n        styles (Dict[str, Style], optional): A mapping of style names on to styles. Defaults to None for a theme with no styles.\n        inherit (bool, optional): Inherit default styles. Defaults to True.\n    '
    
    def __init__(self = None, styles = None, inherit = None):
        self.styles = DEFAULT_STYLES.copy() if inherit else { }
    # WARNING: Decompyle incomplete

    config = (lambda self = None: config = '\n'.join + (lambda .0: pass# WARNING: Decompyle incomplete
)(sorted(self.styles.items())())
        return config
)()
    from_file = (lambda cls = None, config_file = None, source = classmethod, inherit = (None, True): config = configparser.ConfigParser()config.read_file(config_file, source = source)styles = config.items('styles')()theme = Theme(styles, inherit = inherit)theme)()
    read = (lambda cls = None, path = None, inherit = classmethod, encoding = (True, None): config_file = open(path, encoding = encoding)None(None, None)with None:
if not None, cls.from_file(config_file, source = path, inherit = inherit):
pass)()


class ThemeStackError(Exception):
    '''Base exception for errors related to the theme stack.'''
    pass


class ThemeStack:
    '''A stack of themes.

    Args:
        theme (Theme): A theme instance
    '''
    
    def __init__(self = None, theme = None):
        self._entries = [
            theme.styles]
        self.get = self._entries[-1].get

    
    def push_theme(self = None, theme = None, inherit = None):
        '''Push a theme on the top of the stack.

        Args:
            theme (Theme): A Theme instance.
            inherit (boolean, optional): Inherit styles from current top of stack.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def pop_theme(self = None):
        '''Pop (and discard) the top-most theme.'''
        if len(self._entries) == 1:
            raise ThemeStackError('Unable to pop base theme')
        self._entries.pop()
        self.get = self._entries[-1].get


if __name__ == '__main__':
    theme = Theme()
    print(theme.config)
    return None
