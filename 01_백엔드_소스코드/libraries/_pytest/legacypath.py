# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: legacypath.pyc (Python 3.11)

'''Add backward compatibility support for the legacy py path type.'''
from __future__ import annotations
import dataclasses
from pathlib import Path
import shlex
import subprocess
from typing import Final
from typing import final
from typing import TYPE_CHECKING
from iniconfig import SectionWrapper
from _pytest.cacheprovider import Cache
from _pytest.compat import LEGACY_PATH
from _pytest.compat import legacy_path
from _pytest.config import Config
from _pytest.config import hookimpl
from _pytest.config import PytestPluginManager
from _pytest.deprecated import check_ispytest
from _pytest.fixtures import fixture
from _pytest.fixtures import FixtureRequest
from _pytest.main import Session
from _pytest.monkeypatch import MonkeyPatch
from _pytest.nodes import Collector
from _pytest.nodes import Item
from _pytest.nodes import Node
from _pytest.pytester import HookRecorder
from _pytest.pytester import Pytester
from _pytest.pytester import RunResult
from _pytest.terminal import TerminalReporter
from _pytest.tmpdir import TempPathFactory
if TYPE_CHECKING:
    import pexpect
Testdir = <NODE:12>()

class LegacyTestdirPlugin:
    testdir = (lambda pytester = None: Testdir(pytester, _ispytest = True))()()

TempdirFactory = <NODE:12>()()

class LegacyTmpdirPlugin:
    tmpdir_factory = (lambda request = None: request.config._tmpdirhandler)()()
    tmpdir = (lambda tmp_path = None: legacy_path(tmp_path))()()


def Cache_makedir(self = final, name = dataclasses.dataclass):
    '''Return a directory path object with the given name.

    Same as :func:`mkdir`, but returns a legacy py path instance.
    '''
    return legacy_path(self.mkdir(name))


def FixtureRequest_fspath(self = None):
    '''(deprecated) The file system path of the test module which collected this test.'''
    return legacy_path(self.path)


def TerminalReporter_startdir(self = None):
    '''The directory from which pytest was invoked.

    Prefer to use ``startpath`` which is a :class:`pathlib.Path`.

    :type: LEGACY_PATH
    '''
    return legacy_path(self.startpath)


def Config_invocation_dir(self = None):
    '''The directory from which pytest was invoked.

    Prefer to use :attr:`invocation_params.dir <InvocationParams.dir>`,
    which is a :class:`pathlib.Path`.

    :type: LEGACY_PATH
    '''
    return legacy_path(str(self.invocation_params.dir))


def Config_rootdir(self = None):
    '''The path to the :ref:`rootdir <rootdir>`.

    Prefer to use :attr:`rootpath`, which is a :class:`pathlib.Path`.

    :type: LEGACY_PATH
    '''
    return legacy_path(str(self.rootpath))


def Config_inifile(self = None):
    '''The path to the :ref:`configfile <configfiles>`.

    Prefer to use :attr:`inipath`, which is a :class:`pathlib.Path`.

    :type: Optional[LEGACY_PATH]
    '''
    return legacy_path(str(self.inipath)) if self.inipath else None


def Session_startdir(self = None):
    '''The path from which pytest was invoked.

    Prefer to use ``startpath`` which is a :class:`pathlib.Path`.

    :type: LEGACY_PATH
    '''
    return legacy_path(self.startpath)


def Config__getini_unknown_type(self = None, name = None, type = None, value = ('name', 'str', 'type', 'str', 'value', 'str | list[str]')):
    pass
# WARNING: Decompyle incomplete


def Node_fspath(self = None):
    '''(deprecated) returns a legacy_path copy of self.path'''
    return legacy_path(self.path)


def Node_fspath_set(self = None, value = None):
    self.path = Path(value)

pytest_load_initial_conftests = (lambda early_config = None: mp = MonkeyPatch()early_config.add_cleanup(mp.undo)mp.setattr(Cache, 'makedir', Cache_makedir, raising = False)mp.setattr(FixtureRequest, 'fspath', property(FixtureRequest_fspath), raising = False)mp.setattr(TerminalReporter, 'startdir', property(TerminalReporter_startdir), raising = False)mp.setattr(Config, 'invocation_dir', property(Config_invocation_dir), raising = False)mp.setattr(Config, 'rootdir', property(Config_rootdir), raising = False)mp.setattr(Config, 'inifile', property(Config_inifile), raising = False)mp.setattr(Session, 'startdir', property(Session_startdir), raising = False)mp.setattr(Config, '_getini_unknown_type', Config__getini_unknown_type)mp.setattr(Node, 'fspath', property(Node_fspath, Node_fspath_set), raising = False))()
pytest_configure = (lambda config = None: if config.pluginmanager.has_plugin('tmpdir'):
mp = MonkeyPatch()config.add_cleanup(mp.undo)try:
tmp_path_factory = config._tmp_path_factory_tmpdirhandler = TempdirFactory(tmp_path_factory, _ispytest = True)mp.setattr(config, '_tmpdirhandler', _tmpdirhandler, raising = False)except AttributeError:
passconfig.pluginmanager.register(LegacyTmpdirPlugin, 'legacypath-tmpdir')None)()
pytest_plugin_registered = (lambda plugin = None, manager = None: is_pytester = plugin is manager.get_plugin('pytester')if not is_pytester or manager.is_registered(LegacyTestdirPlugin):
manager.register(LegacyTestdirPlugin, 'legacypath-pytester')NoneNone)()
