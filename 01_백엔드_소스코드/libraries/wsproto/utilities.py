# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utilities.pyc (Python 3.11)

'''
wsproto/utilities
~~~~~~~~~~~~~~~~~

Utility functions that do not belong in a separate module.
'''
from __future__ import annotations
import base64
import hashlib
import os
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from h11._headers import Headers as H11Headers
    from events import Event
    from typing import Headers
ACCEPT_GUID = b'258EAFA5-E914-47DA-95CA-C5AB0DC85B11'

class ProtocolError(Exception):
    pass


class LocalProtocolError(ProtocolError):
    '''
    Indicates an error due to local/programming errors.

    This is raised when the connection is asked to do something that
    is either incompatible with the state or the websocket standard.

    '''
    pass


class RemoteProtocolError(ProtocolError):
    pass
# WARNING: Decompyle incomplete


def normed_header_dict(h11_headers = None):
    name_to_values = { }
    for name, value in h11_headers:
        name_to_values.setdefault(name, []).append(value)
        name_to_normed_value = { }
        for name, values in name_to_values.items():
            name_to_normed_value[name] = b', '.join(values)
            return name_to_normed_value


def split_comma_header(value = None):
    return value.split(b',')()


def generate_nonce():
    return base64.b64encode(os.urandom(16))


def generate_accept_token(token = None):
    accept_token = token + ACCEPT_GUID
    accept_token = hashlib.sha1(accept_token).digest()
    return base64.b64encode(accept_token)
