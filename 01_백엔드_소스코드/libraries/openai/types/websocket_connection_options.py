# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: websocket_connection_options.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING
from typing_extensions import Sequence, TypedDict
if TYPE_CHECKING:
    from websockets import Subprotocol
    from websockets.extensions import ClientExtensionFactory

def WebsocketConnectionOptions():
    '''WebsocketConnectionOptions'''
    write_limit: 'int | tuple[int, int | None]' = 'Websocket connection options copied from `websockets`.\n\n    For example: https://websockets.readthedocs.io/en/stable/reference/asyncio/client.html#websockets.asyncio.client.connect\n    '

WebsocketConnectionOptions = <NODE:27>(WebsocketConnectionOptions, 'WebsocketConnectionOptions', TypedDict, total = False)
