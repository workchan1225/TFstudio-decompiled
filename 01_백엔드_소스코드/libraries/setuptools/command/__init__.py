# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from distutils.command.bdist import bdist
import sys
if 'egg' not in bdist.format_commands:
    
    try:
        bdist.format_commands['egg'] = ('bdist_egg', 'Python .egg file')
    except TypeError:
        bdist.format_command['egg'] = ('bdist_egg', 'Python .egg file')
        bdist.format_commands.append('egg')

    del bdist
    del sys
    return None
