# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: testing.pyc (Python 3.11)

from __future__ import annotations
import importlib.metadata as importlib
import typing as t
from contextlib import contextmanager
from contextlib import ExitStack
from copy import copy
from types import TracebackType
from urllib.parse import urlsplit
import werkzeug.test as werkzeug
from click.testing import CliRunner
from werkzeug.test import Client
from werkzeug.wrappers import Request as BaseRequest
from cli import ScriptInfo
from sessions import SessionMixin
if t.TYPE_CHECKING:
    from werkzeug.test import TestResponse
    from app import Flask

class EnvironBuilder(werkzeug.test.EnvironBuilder):
    pass
# WARNING: Decompyle incomplete

_werkzeug_version = ''

def _get_werkzeug_version():
    global _werkzeug_version
    if not _werkzeug_version:
        _werkzeug_version = importlib.metadata.version('werkzeug')
    return _werkzeug_version


class FlaskClient(Client):
    pass
# WARNING: Decompyle incomplete


class FlaskCliRunner(CliRunner):
    pass
# WARNING: Decompyle incomplete
