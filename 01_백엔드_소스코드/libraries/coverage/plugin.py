# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: plugin.pyc (Python 3.11)

"""
.. versionadded:: 4.0

Plug-in interfaces for coverage.py.

Coverage.py supports a few different kinds of plug-ins that change its
behavior:

* File tracers implement tracing of non-Python file types.

* Configurers add custom configuration, using Python code to change the
  configuration.

* Dynamic context switchers decide when the dynamic context has changed, for
  example, to record what test function produced the coverage.

To write a coverage.py plug-in, create a module with a subclass of
:class:`~coverage.CoveragePlugin`.  You will override methods in your class to
participate in various aspects of coverage.py's processing.
Different types of plug-ins have to override different methods.

Any plug-in can optionally implement :meth:`~coverage.CoveragePlugin.sys_info`
to provide debugging information about their operation.

Your module must also contain a ``coverage_init`` function that registers an
instance of your plug-in class::

    import coverage

    class MyPlugin(coverage.CoveragePlugin):
        ...

    def coverage_init(reg, options):
        reg.add_file_tracer(MyPlugin())

You use the `reg` parameter passed to your ``coverage_init`` function to
register your plug-in object.  The registration method you call depends on
what kind of plug-in it is.

If your plug-in takes options, the `options` parameter is a dictionary of your
plug-in's options from the coverage.py configuration file.  Use them however
you want to configure your object before registering it.

Coverage.py will store its own information on your plug-in object, using
attributes whose names start with ``_coverage_``.  Don't be startled.

.. warning::
    Plug-ins are imported by coverage.py before it begins measuring code.
    If you write a plugin in your own project, it might import your product
    code before coverage.py can start measuring.  This can result in your
    own code being reported as missing.

    One solution is to put your plugins in your project tree, but not in
    your importable Python package.


.. _file_tracer_plugins:

File Tracers
============

File tracers implement measurement support for non-Python files.  File tracers
implement the :meth:`~coverage.CoveragePlugin.file_tracer` method to claim
files and the :meth:`~coverage.CoveragePlugin.file_reporter` method to report
on those files.

In your ``coverage_init`` function, use the ``add_file_tracer`` method to
register your file tracer.


.. _configurer_plugins:

Configurers
===========

.. versionadded:: 4.5

Configurers modify the configuration of coverage.py during start-up.
Configurers implement the :meth:`~coverage.CoveragePlugin.configure` method to
change the configuration.

In your ``coverage_init`` function, use the ``add_configurer`` method to
register your configurer.


.. _dynamic_context_plugins:

Dynamic Context Switchers
=========================

.. versionadded:: 5.0

Dynamic context switcher plugins implement the
:meth:`~coverage.CoveragePlugin.dynamic_context` method to dynamically compute
the context label for each measured frame.

Computed context labels are useful when you want to group measured data without
modifying the source code.

For example, you could write a plugin that checks `frame.f_code` to inspect
the currently executed method, and set the context label to a fully qualified
method name if it's an instance method of `unittest.TestCase` and the method
name starts with 'test'.  Such a plugin would provide basic coverage grouping
by test and could be used with test runners that have no built-in coveragepy
support.

In your ``coverage_init`` function, use the ``add_dynamic_context`` method to
register your dynamic context switcher.

"""
from __future__ import annotations
import dataclasses
import functools
from collections.abc import Iterable
from types import FrameType
from typing import Any
from coverage import files
from coverage.misc import _needs_to_implement
from coverage.types import TArc, TConfigurable, TLineNo, TSourceTokenLines

class CoveragePlugin:
    _coverage_enabled: 'bool' = 'Base class for coverage.py plug-ins.'
    
    def file_tracer(self = None, filename = None):
        '''Get a :class:`FileTracer` object for a file.

        Plug-in type: file tracer.

        Every Python source file is offered to your plug-in to give it a chance
        to take responsibility for tracing the file.  If your plug-in can
        handle the file, it should return a :class:`FileTracer` object.
        Otherwise return None.

        There is no way to register your plug-in for particular files.
        Instead, this method is invoked for all  files as they are executed,
        and the plug-in decides whether it can trace the file or not.
        Be prepared for `filename` to refer to all kinds of files that have
        nothing to do with your plug-in.

        The file name will be a Python file being executed.  There are two
        broad categories of behavior for a plug-in, depending on the kind of
        files your plug-in supports:

        * Static file names: each of your original source files has been
          converted into a distinct Python file.  Your plug-in is invoked with
          the Python file name, and it maps it back to its original source
          file.

        * Dynamic file names: all of your source files are executed by the same
          Python file.  In this case, your plug-in implements
          :meth:`FileTracer.dynamic_source_filename` to provide the actual
          source file for each execution frame.

        `filename` is a string, the path to the file being considered.  This is
        the absolute real path to the file.  If you are comparing to other
        paths, be sure to take this into account.

        Returns a :class:`FileTracer` object to use to trace `filename`, or
        None if this plug-in cannot trace this file.

        '''
        pass

    
    def file_reporter(self = None, filename = None):
        '''Get the :class:`FileReporter` class to use for a file.

        Plug-in type: file tracer.

        This will only be invoked if `filename` returns non-None from
        :meth:`file_tracer`.  It\'s an error to return None from this method.

        Returns a :class:`FileReporter` object to use to report on `filename`,
        or the string `"python"` to have coverage.py treat the file as Python.

        '''
        _needs_to_implement(self, 'file_reporter')

    
    def dynamic_context(self = None, frame = None):
        '''Get the dynamically computed context label for `frame`.

        Plug-in type: dynamic context.

        This method is invoked for each frame when outside of a dynamic
        context, to see if a new dynamic context should be started.  If it
        returns a string, a new context label is set for this and deeper
        frames.  The dynamic context ends when this frame returns.

        Returns a string to start a new dynamic context, or None if no new
        context should be started.

        '''
        pass

    
    def find_executable_files(self = None, src_dir = None):
        '''Yield all of the executable files in `src_dir`, recursively.

        Plug-in type: file tracer.

        Executability is a plug-in-specific property, but generally means files
        which would have been considered for coverage analysis, had they been
        included automatically.

        Returns or yields a sequence of strings, the paths to files that could
        have been executed, including files that had been executed.

        '''
        return []

    
    def configure(self = None, config = None):
        '''Modify the configuration of coverage.py.

        Plug-in type: configurer.

        This method is called during coverage.py start-up, to give your plug-in
        a chance to change the configuration.  The `config` parameter is an
        object with :meth:`~coverage.Coverage.get_option` and
        :meth:`~coverage.Coverage.set_option` methods.  Do not call any other
        methods on the `config` object.

        '''
        pass

    
    def sys_info(self = None):
        '''Get a list of information useful for debugging.

        Plug-in type: any.

        This method will be invoked for ``--debug=sys``.  Your
        plug-in can return any information it wants to be displayed.

        Returns a list of pairs: `[(name, value), ...]`.

        '''
        return []



class CoveragePluginBase:
    _coverage_plugin: 'CoveragePlugin' = 'Plugins produce specialized objects, which point back to the original plugin.'


class FileTracer(CoveragePluginBase):
    '''Support needed for files during the execution phase.

    File tracer plug-ins implement subclasses of FileTracer to return from
    their :meth:`~CoveragePlugin.file_tracer` method.

    You may construct this object from :meth:`CoveragePlugin.file_tracer` any
    way you like.  A natural choice would be to pass the file name given to
    `file_tracer`.

    `FileTracer` objects should only be created in the
    :meth:`CoveragePlugin.file_tracer` method.

    See :ref:`howitworks` for details of the different coverage.py phases.

    '''
    
    def source_filename(self = None):
        '''The source file name for this file.

        This may be any file name you like.  A key responsibility of a plug-in
        is to own the mapping from Python execution back to whatever source
        file name was originally the source of the code.

        See :meth:`CoveragePlugin.file_tracer` for details about static and
        dynamic file names.

        Returns the file name to credit with this execution.

        '''
        _needs_to_implement(self, 'source_filename')

    
    def has_dynamic_source_filename(self = None):
        '''Does this FileTracer have dynamic source file names?

        FileTracers can provide dynamically determined file names by
        implementing :meth:`dynamic_source_filename`.  Invoking that function
        is expensive. To determine whether to invoke it, coverage.py uses the
        result of this function to know if it needs to bother invoking
        :meth:`dynamic_source_filename`.

        See :meth:`CoveragePlugin.file_tracer` for details about static and
        dynamic file names.

        Returns True if :meth:`dynamic_source_filename` should be called to get
        dynamic source file names.

        '''
        return False

    
    def dynamic_source_filename(self = None, filename = None, frame = None):
        """Get a dynamically computed source file name.

        Some plug-ins need to compute the source file name dynamically for each
        frame.

        This function will not be invoked if
        :meth:`has_dynamic_source_filename` returns False.

        Returns the source file name for this frame, or None if this frame
        shouldn't be measured.

        """
        pass

    
    def line_number_range(self = None, frame = None):
        """Get the range of source line numbers for a given a call frame.

        The call frame is examined, and the source line number in the original
        file is returned.  The return value is a pair of numbers, the starting
        line number and the ending line number, both inclusive.  For example,
        returning (5, 7) means that lines 5, 6, and 7 should be considered
        executed.

        This function might decide that the frame doesn't indicate any lines
        from the source file were executed.  Return (-1, -1) in this case to
        tell coverage.py that no lines should be recorded for this frame.

        """
        lineno = frame.f_lineno
        return (lineno, lineno)


CodeRegion = <NODE:12>()
FileReporter = <NODE:12>()
