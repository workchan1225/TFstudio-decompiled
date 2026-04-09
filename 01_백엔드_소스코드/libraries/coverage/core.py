# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: core.pyc (Python 3.11)

'''Management of core choices.'''
from __future__ import annotations
import os
import sys
from typing import Any
from coverage import env
from coverage.config import CoverageConfig
from coverage.disposition import FileDisposition
from coverage.exceptions import ConfigError
from coverage.misc import isolate_module
from coverage.pytracer import PyTracer
from coverage.sysmon import SysMonitor
from coverage.types import TDebugCtl, TFileDisposition, Tracer, TWarnFn
os = isolate_module(os)
IMPORT_ERROR: 'str' = ''

try:
    import coverage.tracer as coverage
    CTRACER_FILE: 'str | None' = getattr(coverage.tracer, '__file__', 'unknown')
except ImportError:
    imp_err = None
    if os.getenv('COVERAGE_CORE') == 'ctrace':
        sys.stderr.write("*** COVERAGE_CORE is 'ctrace' but can't import CTracer!\n")
        sys.exit(1)
    IMPORT_ERROR = str(imp_err)
    CTRACER_FILE = None
    imp_err = None
    del imp_err
except:
    imp_err = None
    del imp_err


class Core:
    systrace: 'bool' = 'Information about the central technology enabling execution measurement.'
    
    def __init__(self = None, *, warn, debug, config, dynamic_contexts, metacov):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''<Core tracer_class={self.tracer_class.__name__}>'''
