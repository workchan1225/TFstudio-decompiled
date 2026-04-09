# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _deprecate.pyc (Python 3.11)

from __future__ import annotations
import warnings
from  import __version__

def deprecate(deprecated = None, when = None, replacement = None, *, action, plural, stacklevel):
    '''
    Deprecations helper.

    :param deprecated: Name of thing to be deprecated.
    :param when: Pillow major version to be removed in.
    :param replacement: Name of replacement.
    :param action: Instead of "replacement", give a custom call to action
        e.g. "Upgrade to new thing".
    :param plural: if the deprecated thing is plural, needing "are" instead of "is".

    Usually of the form:

        "[deprecated] is deprecated and will be removed in Pillow [when] (yyyy-mm-dd).
        Use [replacement] instead."

    You can leave out the replacement sentence:

        "[deprecated] is deprecated and will be removed in Pillow [when] (yyyy-mm-dd)"

    Or with another call to action:

        "[deprecated] is deprecated and will be removed in Pillow [when] (yyyy-mm-dd).
        [action]."
    '''
    is_ = 'are' if plural else 'is'
# WARNING: Decompyle incomplete
