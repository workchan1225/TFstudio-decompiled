# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sqldata.pyc (Python 3.11)

'''SQLite coverage data.'''
from __future__ import annotations
import collections
import datetime
import functools
import glob
import itertools
import os
import random
import socket
import sqlite3
import string
import sys
import textwrap
import threading
import uuid
import zlib
from collections.abc import Collection, Mapping, Sequence
from typing import Any, Callable, cast
from coverage.debug import NoDebugging, auto_repr, file_summary
from coverage.exceptions import CoverageException, DataError
from coverage.misc import file_be_gone, isolate_module
from coverage.numbits import numbits_to_nums, numbits_union, nums_to_numbits
from coverage.sqlitedb import SqliteDb
from coverage.types import AnyCallable, FilePath, TArc, TDebugCtl, TLineNo, TWarnFn
from coverage.version import __version__
os = isolate_module(os)
SCHEMA_VERSION = 7
SCHEMA = "CREATE TABLE coverage_schema (\n    -- One row, to record the version of the schema in this db.\n    version integer\n);\n\nCREATE TABLE meta (\n    -- Key-value pairs, to record metadata about the data\n    key text,\n    value text,\n    unique (key)\n    -- Possible keys:\n    --  'has_arcs' boolean      -- Is this data recording branches?\n    --  'sys_argv' text         -- The coverage command line that recorded the data.\n    --  'version' text          -- The version of coverage.py that made the file.\n    --  'when' text             -- Datetime when the file was created.\n);\n\nCREATE TABLE file (\n    -- A row per file measured.\n    id integer primary key,\n    path text,\n    unique (path)\n);\n\nCREATE TABLE context (\n    -- A row per context measured.\n    id integer primary key,\n    context text,\n    unique (context)\n);\n\nCREATE TABLE line_bits (\n    -- If recording lines, a row per context per file executed.\n    -- All of the line numbers for that file/context are in one numbits.\n    file_id integer,            -- foreign key to `file`.\n    context_id integer,         -- foreign key to `context`.\n    numbits blob,               -- see the numbits functions in coverage.numbits\n    foreign key (file_id) references file (id),\n    foreign key (context_id) references context (id),\n    unique (file_id, context_id)\n);\n\nCREATE TABLE arc (\n    -- If recording branches, a row per context per from/to line transition executed.\n    file_id integer,            -- foreign key to `file`.\n    context_id integer,         -- foreign key to `context`.\n    fromno integer,             -- line number jumped from.\n    tono integer,               -- line number jumped to.\n    foreign key (file_id) references file (id),\n    foreign key (context_id) references context (id),\n    unique (file_id, context_id, fromno, tono)\n);\n\nCREATE TABLE tracer (\n    -- A row per file indicating the tracer used for that file.\n    file_id integer primary key,\n    tracer text,\n    foreign key (file_id) references file (id)\n);\n"

def _locked(method = None):
    '''A decorator for methods that should hold self._lock.'''
    pass
# WARNING: Decompyle incomplete


class NumbitsUnionAgg:
    '''SQLite aggregate function for computing union of numbits.'''
    
    def __init__(self = None):
        self.result = b''

    
    def step(self = None, value = None):
        '''Process one value in the aggregation.'''
        self.result = numbits_union(self.result, value)

    
    def finalize(self = None):
        '''Return the final aggregated result.'''
        return self.result



class CoverageData:
    '''Manages collected coverage data, including file storage.

    This class is the public supported API to the data that coverage.py
    collects during program execution.  It includes information about what code
    was executed. It does not include information from the analysis phase, to
    determine what lines could have been executed, or what lines were not
    executed.

    .. note::

        The data file is currently a SQLite database file, with a
        :ref:`documented schema <dbschema>`. The schema is subject to change
        though, so be careful about querying it directly. Use this API if you
        can to isolate yourself from changes.

    There are a number of kinds of data that can be collected:

    * **lines**: the line numbers of source lines that were executed.
      These are always available.

    * **arcs**: pairs of source and destination line numbers for transitions
      between source lines.  These are only available if branch coverage was
      used.

    * **file tracer names**: the module names of the file tracer plugins that
      handled each file in the data.

    Lines, arcs, and file tracer names are stored for each source file. File
    names in this API are case-sensitive, even on platforms with
    case-insensitive file systems.

    A data file either stores lines, or arcs, but not both.

    A data file is associated with the data when the :class:`CoverageData`
    is created, using the parameters `basename`, `suffix`, and `no_disk`. The
    base name can be queried with :meth:`base_filename`, and the actual file
    name being used is available from :meth:`data_filename`.

    To read an existing coverage.py data file, use :meth:`read`.  You can then
    access the line, arc, or file tracer data with :meth:`lines`, :meth:`arcs`,
    or :meth:`file_tracer`.

    The :meth:`has_arcs` method indicates whether arc data is available.  You
    can get a set of the files in the data with :meth:`measured_files`.  As
    with most Python containers, you can determine if there is any data at all
    by using this object as a boolean value.

    The contexts for each line in a file can be read with
    :meth:`contexts_by_lineno`.

    To limit querying to certain contexts, use :meth:`set_query_context` or
    :meth:`set_query_contexts`. These will narrow the focus of subsequent
    :meth:`lines`, :meth:`arcs`, and :meth:`contexts_by_lineno` calls. The set
    of all measured context names can be retrieved with
    :meth:`measured_contexts`.

    Most data files will be created by coverage.py itself, but you can use
    methods here to create data files if you like.  The :meth:`add_lines`,
    :meth:`add_arcs`, and :meth:`add_file_tracers` methods add data, in ways
    that are convenient for coverage.py.

    To record data for contexts, use :meth:`set_context` to set a context to
    be used for subsequent :meth:`add_lines` and :meth:`add_arcs` calls.

    To add a source file without any measured data, use :meth:`touch_file`,
    or :meth:`touch_files` for a list of such files.

    Write the data to its file with :meth:`write`.

    You can clear the data in memory with :meth:`erase`.  Data for specific
    files can be removed from the database with :meth:`purge_files`.

    Two data collections can be combined by using :meth:`update` on one
    :class:`CoverageData`, passing it the other.

    Data in a :class:`CoverageData` can be serialized and deserialized with
    :meth:`dumps` and :meth:`loads`.

    The methods used during the coverage.py collection phase
    (:meth:`add_lines`, :meth:`add_arcs`, :meth:`set_context`, and
    :meth:`add_file_tracers`) are thread-safe.  Other methods may not be.

    '''
    
    def __init__(self, basename = None, suffix = None, no_disk = None, warn = (None, None, False, None, None), debug = ('basename', 'FilePath | None', 'suffix', 'str | bool | None', 'no_disk', 'bool', 'warn', 'TWarnFn | None', 'debug', 'TDebugCtl | None', 'return', 'None')):
