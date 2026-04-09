# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
    pygments.styles
    ~~~~~~~~~~~~~~~

    Contains built-in styles.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.plugin import find_plugin_styles
from pygments.util import ClassNotFound
from pygments.styles._mapping import STYLES
STYLE_MAP = STYLES.items()()
_STYLE_NAME_TO_MODULE_MAP = STYLES.items()()

def get_style_by_name(name):
    '''
    Return a style class by its short name. The names of the builtin styles
    are listed in :data:`pygments.styles.STYLE_MAP`.

    Will raise :exc:`pygments.util.ClassNotFound` if no style of that name is
    found.
    '''
    if name in _STYLE_NAME_TO_MODULE_MAP:
        (mod, cls) = _STYLE_NAME_TO_MODULE_MAP[name]
        builtin = 'yes'
    else:
        for found_name, style in find_plugin_styles():
            if name == found_name:
                
                return None, style
            'pygments.styles.' + name = ''
            cls = name.title() + 'Style'
            
            try:
                mod = __import__(mod, None, None, [
                    cls])
            except ImportError:
                if builtin:
                    raise ClassNotFound(f'''Could not find style module {mod!r}''' + ', though it should be builtin' + '.')

            
            try:
                return getattr(mod, cls)
            except AttributeError:
                raise ClassNotFound(f'''Could not find style class {cls!r} in style module.''')



def get_all_styles():
    '''Return a generator for all styles by name, both builtin and plugin.'''
    pass
# WARNING: Decompyle incomplete
