# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

'''Base implementation classes.

The public-facing ``Events`` serves as the base class for an event interface;
its public attributes represent different kinds of events.   These attributes
are mirrored onto a ``_Dispatch`` class, which serves as a container for
collections of listener functions.   These collections are represented both
at the class level of a particular ``_Dispatch`` class as well as within
instances of ``_Dispatch``.

'''
from __future__ import annotations
import typing
from typing import Any
from typing import cast
from typing import Dict
from typing import Generic
from typing import Iterator
from typing import List
from typing import Mapping
from typing import MutableMapping
from typing import Optional
from typing import overload
from typing import Tuple
from typing import Type
from typing import Union
import weakref
from attr import _ClsLevelDispatch
from attr import _EmptyListener
from attr import _InstanceLevelDispatch
from attr import _JoinedListener
from registry import _ET
from registry import _EventKey
from  import util
from util.typing import Literal
_registrars: 'MutableMapping[str, List[Type[_HasEventsDispatch[Any]]]]' = util.defaultdict(list)

def _is_event_name(name = None):
