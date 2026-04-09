# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: nest_asyncio.pyc (Python 3.11)

'''Patch asyncio to allow nested event loops.'''
import asyncio
from asyncio.events import events
import os
import sys
import threading
from contextlib import contextmanager, suppress
from heapq import heappop

def apply(loop = (None,)):
