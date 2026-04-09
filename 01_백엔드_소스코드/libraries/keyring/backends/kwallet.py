# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: kwallet.pyc (Python 3.11)

import contextlib
import os
import sys
from backend import KeyringBackend
from compat import properties
from credentials import SimpleCredential
from errors import InitError, KeyringLocked, PasswordDeleteError, PasswordSetError

try:
    import dbus
    from dbus.mainloop.glib import DBusGMainLoop
except ImportError:
    pass
except AttributeError:
    pass


def _id_from_argv():
    '''
    Safely infer an app id from sys.argv.
    '''
    allowed = (AttributeError, IndexError, TypeError)
    contextlib.suppress(allowed)
    None(None, None)
    return 
    with None:
        if not None, sys.argv[0]:
            pass


class DBusKeyring(KeyringBackend):
    pass
# WARNING: Decompyle incomplete


class DBusKeyringKWallet4(DBusKeyring):
    pass
# WARNING: Decompyle incomplete
