# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: token.pyc (Python 3.11)

__doc__ = '\n    pygments.token\n    ~~~~~~~~~~~~~~\n\n    Basic token types and the standard tokens.\n\n    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.\n    :license: BSD, see LICENSE for details.\n'

class _TokenType(tuple):
    parent = None
    
    def split(self):
        buf = []
        node = self
    # WARNING: Decompyle incomplete

    
    def __init__(self, *args):
        self.subtypes = set()

    
    def __contains__(self, val):
