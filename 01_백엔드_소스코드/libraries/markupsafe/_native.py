# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _native.pyc (Python 3.11)


def _escape_inner(s = None):
    return s.replace('&', '&amp;').replace('>', '&gt;').replace('<', '&lt;').replace("'", '&#39;').replace('"', '&#34;')
