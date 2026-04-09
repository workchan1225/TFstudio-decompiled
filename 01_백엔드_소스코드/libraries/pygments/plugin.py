# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: plugin.pyc (Python 3.11)

'''
    pygments.plugin
    ~~~~~~~~~~~~~~~

    Pygments plugin interface.

    lexer plugins::

        [pygments.lexers]
        yourlexer = yourmodule:YourLexer

    formatter plugins::

        [pygments.formatters]
        yourformatter = yourformatter:YourFormatter
        /.ext = yourformatter:YourFormatter

    As you can see, you can define extensions for the formatter
    with a leading slash.

    syntax plugins::

        [pygments.styles]
        yourstyle = yourstyle:YourStyle

    filter plugin::

        [pygments.filter]
        yourfilter = yourfilter:YourFilter


    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from importlib.metadata import entry_points
LEXER_ENTRY_POINT = 'pygments.lexers'
FORMATTER_ENTRY_POINT = 'pygments.formatters'
STYLE_ENTRY_POINT = 'pygments.styles'
FILTER_ENTRY_POINT = 'pygments.filters'

def iter_entry_points(group_name):
    groups = entry_points()
    if hasattr(groups, 'select'):
        return groups.select(group = group_name)
    return None.get(group_name, [])


def find_plugin_lexers():
    pass
# WARNING: Decompyle incomplete


def find_plugin_formatters():
    pass
# WARNING: Decompyle incomplete


def find_plugin_styles():
    pass
# WARNING: Decompyle incomplete


def find_plugin_filters():
    pass
# WARNING: Decompyle incomplete
