# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cli.pyc (Python 3.11)

from __future__ import annotations
import argparse
import asyncio
import os
import sys
from typing import Generator
from asyncio.client import ClientConnection, connect
from asyncio.messages import SimpleQueue
from exceptions import ConnectionClosed
from frames import Close
from streams import StreamReader
from version import version as websockets_version
__all__ = [
    'main']

def print_during_input(string = None):
    sys.stdout.write(f'''\x1b7\n\x1b[A\x1b[L{string}\n\x1b8\x1b[B''')
    sys.stdout.flush()


def print_over_input(string = None):
    sys.stdout.write(f'''\r\x1b[K{string}\n''')
    sys.stdout.flush()


class ReadLines(asyncio.Protocol):
    
    def __init__(self = None):
        self.reader = StreamReader()
        self.messages = SimpleQueue()

    
    def parse(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def connection_made(self = None, transport = None):
        self.parser = self.parse()
        next(self.parser)

    
    def data_received(self = None, data = None):
        self.reader.feed_data(data)
        next(self.parser)

    
    def eof_received(self = None):
        self.reader.feed_eof()

    
    def connection_lost(self = None, exc = None):
        self.reader.discard()
        self.messages.abort()



async def print_incoming_messages(websocket = None):
    pass
# WARNING: Decompyle incomplete


async def send_outgoing_messages(websocket = None, messages = None):
    pass
# WARNING: Decompyle incomplete


async def interactive_client(uri = None):
    pass
# WARNING: Decompyle incomplete


def main(argv = None):
    parser = argparse.ArgumentParser(prog = 'websockets', description = 'Interactive WebSocket client.', add_help = False)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--version', action = 'store_true')
    group.add_argument('uri', metavar = '<uri>', nargs = '?')
    args = parser.parse_args(argv)
    if args.version:
        print(f'''websockets {websockets_version}''')
        return None
# WARNING: Decompyle incomplete
