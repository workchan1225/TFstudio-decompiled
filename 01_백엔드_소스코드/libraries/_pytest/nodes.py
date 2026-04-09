# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: nodes.pyc (Python 3.11)

from __future__ import annotations
import abc
from collections.abc import Callable
from collections.abc import Iterable
from collections.abc import Iterator
from collections.abc import MutableMapping
from functools import cached_property
from functools import lru_cache
import os
import pathlib
from pathlib import Path
from typing import Any
from typing import cast
from typing import NoReturn
from typing import overload
from typing import TYPE_CHECKING
from typing import TypeVar
import warnings
import pluggy
import _pytest._code as _pytest
from _pytest._code import getfslineno
from _pytest._code.code import ExceptionInfo
from _pytest._code.code import TerminalRepr
from _pytest._code.code import Traceback
from _pytest._code.code import TracebackStyle
from _pytest.compat import LEGACY_PATH
from _pytest.compat import signature
from _pytest.config import Config
from _pytest.config import ConftestImportFailure
from _pytest.config.compat import _check_path
from _pytest.deprecated import NODE_CTOR_FSPATH_ARG
from _pytest.mark.structures import Mark
from _pytest.mark.structures import MarkDecorator
from _pytest.mark.structures import NodeKeywords
from _pytest.outcomes import fail
from _pytest.pathlib import absolutepath
from _pytest.stash import Stash
from _pytest.warning_types import PytestWarning
if TYPE_CHECKING:
    from typing_extensions import Self
    from _pytest.main import Session
SEP = '/'
tracebackcutdir = Path(_pytest.__file__).parent
_T = TypeVar('_T')

def _imply_path(node_type = None, path = None, fspath = None):
    pass
# WARNING: Decompyle incomplete

_NodeType = TypeVar('_NodeType', bound = 'Node')

class NodeMeta(abc.ABCMeta):
    pass
# WARNING: Decompyle incomplete


def Node():
    '''Node'''
    fspath: 'LEGACY_PATH' = "Base class of :class:`Collector` and :class:`Item`, the components of\n    the test collection tree.\n\n    ``Collector``\\'s are the internal nodes of the tree, and ``Item``\\'s are the\n    leaf nodes.\n    "
    __slots__ = ('__dict__', '_nodeid', '_store', 'config', 'name', 'parent', 'path', 'session')
    
    def __init__(self, name, parent, config = None, session = None, fspath = None, path = (None, None, None, None, None, None), nodeid = ('name', 'str', 'parent', 'Node | None', 'config', 'Config | None', 'session', 'Session | None', 'fspath', 'LEGACY_PATH | None', 'path', 'Path | None', 'nodeid', 'str | None', 'return', 'None')):
        self.name = name
        self.parent = parent
        if config:
            self.config = config
        elif not parent:
            raise TypeError('config or parent must be provided')
        self.config = parent.config
        if session:
            self.session = session
        elif not parent:
            raise TypeError('session or parent must be provided')
        self.session = parent.session
    # WARNING: Decompyle incomplete

    from_parent = (lambda cls = None, parent = None: if 'config' in kw:
raise TypeError('config is not a valid argument for from_parent')if 'session' in kw:
raise TypeError('session is not a valid argument for from_parent')# WARNING: Decompyle incomplete
)()
    ihook = (lambda self = None: self.session.gethookproxy(self.path))()
    
    def __repr__(self = None):
        return '<{} {}>'.format(self.__class__.__name__, getattr(self, 'name', None))

    
    def warn(self = None, warning = None):
        '''Issue a warning for this Node.

        Warnings will be displayed after the test session, unless explicitly suppressed.

        :param Warning warning:
            The warning instance to issue.

        :raises ValueError: If ``warning`` instance is not a subclass of Warning.

        Example usage:

        .. code-block:: python

            node.warn(PytestWarning("some message"))
            node.warn(UserWarning("some message"))

        .. versionchanged:: 6.2
            Any subclass of :class:`Warning` is now accepted, rather than only
            :class:`PytestWarning <pytest.PytestWarning>` subclasses.
        '''
        if not isinstance(warning, Warning):
            raise ValueError(f'''warning must be an instance of Warning or subclass, got {warning!r}''')
        (path, lineno) = get_fslocation_from_item(self)
    # WARNING: Decompyle incomplete

    nodeid = (lambda self = None: self._nodeid)()
    
    def __hash__(self = None):
        return hash(self._nodeid)

    
    def setup(self = None):
        pass

    
    def teardown(self = None):
        pass

    
    def iter_parents(self = None):
        '''Iterate over all parent collectors starting from and including self
        up to the root of the collection tree.

        .. versionadded:: 8.1
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def listchain(self = None):
        '''Return a list of all parent collectors starting from the root of the
        collection tree down to and including self.'''
        chain = []
        item = self
    # WARNING: Decompyle incomplete

    
    def add_marker(self = None, marker = None, append = None):
        '''Dynamically add a marker object to the node.

        :param marker:
            The marker.
        :param append:
            Whether to append the marker, or prepend it.
        '''
        MARK_GEN = MARK_GEN
        import _pytest.mark
        if isinstance(marker, MarkDecorator):
            marker_ = marker
        elif isinstance(marker, str):
            marker_ = getattr(MARK_GEN, marker)
        else:
            raise ValueError('is not a string or pytest.mark.* Marker')
        self.keywords[marker_.name] = marker_
        if append:
            self.own_markers.append(marker_.mark)
            return None
        None.own_markers.insert(0, marker_.mark)

    
    def iter_markers(self = None, name = None):
        '''Iterate over all markers of the node.

        :param name: If given, filter the results by the name attribute.
        :returns: An iterator of the markers of the node.
        '''
        return self.iter_markers_with_node(name = name)()

    
    def iter_markers_with_node(self = None, name = None):
        '''Iterate over all markers of the node.

        :param name: If given, filter the results by the name attribute.
        :returns: An iterator of (node, mark) tuples.
        '''
        pass
    # WARNING: Decompyle incomplete

    get_closest_marker = (lambda self = None, name = None: pass)()
    get_closest_marker = (lambda self = None, name = None, default = overload: pass)()
    
    def get_closest_marker(self = None, name = None, default = None):
        '''Return the first marker matching the name, from closest (for
        example function) to farther level (for example module level).

        :param default: Fallback return value if no marker was found.
        :param name: Name to filter by.
        '''
        return next(self.iter_markers(name = name), default)

    
    def listextrakeywords(self = None):
        '''Return a set of all extra keywords in self and any parents.'''
        extra_keywords = set()
        for item in self.listchain():
            extra_keywords.update(item.extra_keyword_matches)
            return extra_keywords

    
    def listnames(self = None):
        return self.listchain()()

    
    def addfinalizer(self = None, fin = None):
        '''Register a function to be called without arguments when this node is
        finalized.

        This method can only be called when this node is active
        in a setup chain, for example during self.setup().
        '''
        self.session._setupstate.addfinalizer(fin, self)

    
    def getparent(self = None, cls = None):
        '''Get the closest parent node (including self) which is an instance of
        the given class.

        :param cls: The node class to search for.
        :returns: The node, if found.
        '''
        for node in self.iter_parents():
            if isinstance(node, cls):
                
                return None, node
            return None

    
    def _traceback_filter(self = None, excinfo = None):
        return excinfo.traceback

    
    def _repr_failure_py(self = None, excinfo = None, style = None):
        FixtureLookupError = FixtureLookupError
        import _pytest.fixtures
        if isinstance(excinfo.value, ConftestImportFailure):
            excinfo = ExceptionInfo.from_exception(excinfo.value.cause)
        if not isinstance(excinfo.value, fail.Exception) and excinfo.value.pytrace:
            style = 'value'
        if isinstance(excinfo.value, FixtureLookupError):
            return excinfo.value.formatrepr()
        if None.config.getoption('fulltrace', False):
            style = 'long'
            tbfilter = False
        else:
            tbfilter = self._traceback_filter
            if style == 'auto':
                style = 'long'
    # WARNING: Decompyle incomplete

    
    def repr_failure(self = None, excinfo = None, style = None):
        '''Return a representation of a collection or test failure.

        .. seealso:: :ref:`non-python tests`

        :param excinfo: Exception information for the failure.
        '''
        return self._repr_failure_py(excinfo, style)


Node = <NODE:27>(Node, 'Node', abc.ABC, metaclass = NodeMeta)

def get_fslocation_from_item(node = None):
    '''Try to extract the actual location from a node, depending on available attributes:

    * "location": a pair (path, lineno)
    * "obj": a Python object that the node wraps.
    * "path": just a path

    :rtype: A tuple of (str|Path, int) with filename and 0-based line number.
    '''
    location = getattr(node, 'location', None)
# WARNING: Decompyle incomplete


class Collector(abc.ABC, Node):
    '''Base class of all collectors.

    Collector create children through `collect()` and thus iteratively build
    the collection tree.
    '''
    
    class CollectError(Exception):
        '''An error during collection, contains a custom message.'''
        pass

    collect = (lambda self = None: raise NotImplementedError('abstract'))()
    
    def repr_failure(self = None, excinfo = None):
        '''Return a representation of a collection failure.

        :param excinfo: Exception information for the failure.
        '''
        if not isinstance(excinfo.value, self.CollectError) and self.config.getoption('fulltrace', False):
            exc = excinfo.value
            return str(exc.args[0])
        tbstyle = None.config.getoption('tbstyle', 'auto')
        if tbstyle == 'auto':
            tbstyle = 'short'
        return self._repr_failure_py(excinfo, style = tbstyle)

    
    def _traceback_filter(self = None, excinfo = None):
        if hasattr(self, 'path'):
            traceback = excinfo.traceback
            ntraceback = traceback.cut(path = self.path)
            if ntraceback == traceback:
                ntraceback = ntraceback.cut(excludepath = tracebackcutdir)
            return ntraceback.filter(excinfo)
        return None.traceback


_check_initialpaths_for_relpath = (lambda initial_paths = None, path = None: if path in initial_paths:
''for parent in None.parents:
if parent in initial_paths:
None, str(path.relative_to(parent))None)()

class FSCollector(abc.ABC, Collector):
    pass
# WARNING: Decompyle incomplete


class File(abc.ABC, FSCollector):
    '''Base class for collecting tests from a file.

    :ref:`non-python tests`.
    '''
    pass


class Directory(abc.ABC, FSCollector):
    '''Base class for collecting files from a directory.

    A basic directory collector does the following: goes over the files and
    sub-directories in the directory and creates collectors for them by calling
    the hooks :hook:`pytest_collect_directory` and :hook:`pytest_collect_file`,
    after checking that they are not ignored using
    :hook:`pytest_ignore_collect`.

    The default directory collectors are :class:`~pytest.Dir` and
    :class:`~pytest.Package`.

    .. versionadded:: 8.0

    :ref:`custom directory collectors`.
    '''
    pass


class Item(abc.ABC, Node):
    pass
# WARNING: Decompyle incomplete
