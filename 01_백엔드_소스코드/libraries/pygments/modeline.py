# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: modeline.pyc (Python 3.11)

'''
    pygments.modeline
    ~~~~~~~~~~~~~~~~~

    A simple modeline parser (based on pymodeline).

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
__all__ = [
    'get_filetype_from_buffer']
modeline_re = re.compile('\n    (?: vi | vim | ex ) (?: [<=>]? \\d* )? :\n    .* (?: ft | filetype | syn | syntax ) = ( [^:\\s]+ )\n', re.VERBOSE)

def get_filetype_from_line(l):
    m = modeline_re.search(l)
    if m:
        return m.group(1)


def get_filetype_from_buffer(buf, max_lines = (5,)):
