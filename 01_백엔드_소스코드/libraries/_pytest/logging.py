# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: logging.pyc (Python 3.11)

'''Access and control log capturing.'''
from __future__ import annotations
from collections.abc import Generator
from collections.abc import Mapping
from collections.abc import Set as AbstractSet
from contextlib import contextmanager
from contextlib import nullcontext
from datetime import datetime
from datetime import timedelta
from datetime import timezone
import io
from io import StringIO
import logging
from logging import LogRecord
import os
from pathlib import Path
import re
from types import TracebackType
from typing import final
from typing import Generic
from typing import Literal
from typing import TYPE_CHECKING
from typing import TypeVar
from _pytest import nodes
from _pytest._io import TerminalWriter
from _pytest.capture import CaptureManager
from _pytest.config import _strtobool
from _pytest.config import Config
from _pytest.config import create_terminal_writer
from _pytest.config import hookimpl
from _pytest.config import UsageError
from _pytest.config.argparsing import Parser
from _pytest.deprecated import check_ispytest
from _pytest.fixtures import fixture
from _pytest.fixtures import FixtureRequest
from _pytest.main import Session
from _pytest.stash import StashKey
from _pytest.terminal import TerminalReporter
if TYPE_CHECKING:
    logging_StreamHandler = logging.StreamHandler[StringIO]
else:
    logging_StreamHandler = logging.StreamHandler
DEFAULT_LOG_FORMAT = '%(levelname)-8s %(name)s:%(filename)s:%(lineno)d %(message)s'
DEFAULT_LOG_DATE_FORMAT = '%H:%M:%S'
_ANSI_ESCAPE_SEQ = re.compile('\\x1b\\[[\\d;]+m')
caplog_handler_key = StashKey['LogCaptureHandler']()
caplog_records_key = StashKey[dict[(str, list[logging.LogRecord])]]()

def _remove_ansi_escape_sequences(text = None):
    return _ANSI_ESCAPE_SEQ.sub('', text)


class DatetimeFormatter(logging.Formatter):
    pass
# WARNING: Decompyle incomplete


class ColoredLevelFormatter(DatetimeFormatter):
    pass
# WARNING: Decompyle incomplete


class PercentStyleMultiline(logging.PercentStyle):
    pass
# WARNING: Decompyle incomplete


def get_option_ini(config = None, *names):
    pass
# WARNING: Decompyle incomplete


def pytest_addoption(parser = None):
    '''Add options to control log capturing.'''
    pass
# WARNING: Decompyle incomplete

_HandlerType = TypeVar('_HandlerType', bound = logging.Handler)

def catching_logs():
    '''catching_logs'''
    __doc__ = 'Context manager that prepares the whole logging machinery properly.'
    __slots__ = ('handler', 'level', 'orig_level')
    
    def __init__(self = None, handler = None, level = None):
        self.handler = handler
        self.level = level

    
    def __enter__(self = None):
        root_logger = logging.getLogger()
    # WARNING: Decompyle incomplete

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        root_logger = logging.getLogger()
    # WARNING: Decompyle incomplete


catching_logs = <NODE:27>(catching_logs, 'catching_logs', Generic[_HandlerType])

class LogCaptureHandler(logging_StreamHandler):
    pass
# WARNING: Decompyle incomplete

LogCaptureFixture = <NODE:12>()
caplog = (lambda request = None: pass# WARNING: Decompyle incomplete
)()

def get_log_level_for_setting(config = None, *setting_names):
    pass
# WARNING: Decompyle incomplete

pytest_configure = (lambda config = None: config.pluginmanager.register(LoggingPlugin(config), 'logging-plugin'))()

class LoggingPlugin:
    '''Attaches to the logging module and captures log messages for each test.'''
    
    def __init__(self = None, config = None):
        '''Create a new plugin to capture log messages.

        The formatter can be safely shared across all handlers so
        create a single one for the entire test session here.
        '''
        self._config = config
        self.formatter = self._create_formatter(get_option_ini(config, 'log_format'), get_option_ini(config, 'log_date_format'), get_option_ini(config, 'log_auto_indent'))
        self.log_level = get_log_level_for_setting(config, 'log_level')
        self.caplog_handler = LogCaptureHandler()
        self.caplog_handler.setFormatter(self.formatter)
        self.report_handler = LogCaptureHandler()
        self.report_handler.setFormatter(self.formatter)
        self.log_file_level = get_log_level_for_setting(config, 'log_file_level', 'log_level')
        if not get_option_ini(config, 'log_file'):
            log_file = os.devnull
            if log_file != os.devnull:
                directory = os.path.dirname(os.path.abspath(log_file))
                if not os.path.isdir(directory):
                    os.makedirs(directory)
    # WARNING: Decompyle incomplete

    
    def _disable_loggers(self = None, loggers_to_disable = None):
        if not loggers_to_disable:
            return None
        for name in None:
            logger = logging.getLogger(name)
            logger.disabled = True
            return None

    
    def _create_formatter(self, log_format, log_date_format, auto_indent):
        color = getattr(self._config.option, 'color', 'no')
        if color != 'no' and ColoredLevelFormatter.LEVELNAME_FMT_REGEX.search(log_format):
            formatter = ColoredLevelFormatter(create_terminal_writer(self._config), log_format, log_date_format)
        else:
            formatter = DatetimeFormatter(log_format, log_date_format)
        formatter._style = PercentStyleMultiline(formatter._style._fmt, auto_indent = auto_indent)
        return formatter

    
    def set_log_path(self = None, fname = None):
        '''Set the filename parameter for Logging.FileHandler().

        Creates parent directory if it does not exist.

        .. warning::
            This is an experimental API.
        '''
        fpath = Path(fname)
        if not fpath.is_absolute():
            fpath = self._config.rootpath / fpath
        if not fpath.parent.exists():
            fpath.parent.mkdir(exist_ok = True, parents = True)
        stream = fpath.open(mode = self.log_file_mode, encoding = 'UTF-8')
        old_stream = self.log_file_handler.setStream(stream)
        if old_stream:
            old_stream.close()
            return None

    
    def _log_cli_enabled(self = None):
        '''Return whether live logging is enabled.'''
        pass
    # WARNING: Decompyle incomplete

    pytest_sessionstart = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    pytest_collection = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    pytest_runtestloop = (lambda self = None, session = None: pass# WARNING: Decompyle incomplete
)()
    pytest_runtest_logstart = (lambda self = None: self.log_cli_handler.reset()self.log_cli_handler.set_when('start'))()
    pytest_runtest_logreport = (lambda self = None: self.log_cli_handler.set_when('logreport'))()
    _runtest_for = (lambda self = None, item = None, when = contextmanager: pass# WARNING: Decompyle incomplete
)()
    pytest_runtest_setup = (lambda self = None, item = None: pass# WARNING: Decompyle incomplete
)()
    pytest_runtest_call = (lambda self = None, item = None: pass# WARNING: Decompyle incomplete
)()
    pytest_runtest_teardown = (lambda self = None, item = None: pass# WARNING: Decompyle incomplete
)()
    pytest_runtest_logfinish = (lambda self = None: self.log_cli_handler.set_when('finish'))()
    pytest_sessionfinish = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    pytest_unconfigure = (lambda self = None: self.log_file_handler.close())()


class _FileHandler(logging.FileHandler):
    '''A logging FileHandler with pytest tweaks.'''
    
    def handleError(self = None, record = None):
        pass



class _LiveLoggingStreamHandler(logging_StreamHandler):
    pass
# WARNING: Decompyle incomplete


class _LiveLoggingNullHandler(logging.NullHandler):
    '''A logging handler used when live logging is disabled.'''
    
    def reset(self = None):
        pass

    
    def set_when(self = None, when = None):
        pass

    
    def handleError(self = None, record = None):
        pass
