# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: log.pyc (Python 3.11)

'''Logging control and utilities.

Control of logging for SA can be performed from the regular python logging
module.  The regular dotted module namespace is used, starting at
\'sqlalchemy\'.  For class-level logging, the class name is appended.

The "echo" keyword parameter, available on SQLA :class:`_engine.Engine`
and :class:`_pool.Pool` objects, corresponds to a logger specific to that
instance only.

'''
from __future__ import annotations
import logging
import sys
from typing import Any
from typing import Optional
from typing import overload
from typing import Set
from typing import Type
from typing import TypeVar
from typing import Union
from util import py311
from util import py38
from util.typing import Literal
if py38:
    STACKLEVEL = True
    STACKLEVEL_OFFSET = 2 if py311 else 1
else:
    STACKLEVEL = False
    STACKLEVEL_OFFSET = 0
_IT = TypeVar('_IT', bound = 'Identified')
_EchoFlagType = Union[(None, bool, Literal['debug'])]
rootlogger = logging.getLogger('sqlalchemy')
if rootlogger.level == logging.NOTSET:
    rootlogger.setLevel(logging.WARN)

def _add_default_handler(logger = None):
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s'))
    logger.addHandler(handler)

_logged_classes: 'Set[Type[Identified]]' = set()

def _qual_logger_name_for_cls(cls = None):
