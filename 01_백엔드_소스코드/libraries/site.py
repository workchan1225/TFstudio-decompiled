# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: site.pyc (Python 3.11)

'''Append module search paths for third-party packages to sys.path.

****************************************************************
* This module is automatically imported during initialization. *
****************************************************************

This will append site-specific paths to the module search path.  On
Unix (including Mac OSX), it starts with sys.prefix and
sys.exec_prefix (if different) and appends
lib/python<version>/site-packages.
On other platforms (such as Windows), it tries each of the
prefixes directly, as well as with lib/site-packages appended.  The
resulting directories, if they exist, are appended to sys.path, and
also inspected for path configuration files.

If a file named "pyvenv.cfg" exists one directory above sys.executable,
sys.prefix and sys.exec_prefix are set to that directory and
it is also checked for site-packages (sys.base_prefix and
sys.base_exec_prefix will always be the "real" prefixes of the Python
installation). If "pyvenv.cfg" (a bootstrap configuration file) contains
the key "include-system-site-packages" set to anything other than "false"
(case-insensitive), the system-level prefixes will still also be
searched for site-packages; otherwise they won\'t.

All of the resulting site-specific directories, if they exist, are
appended to sys.path, and also inspected for path configuration
files.

A path configuration file is a file whose name has the form
<package>.pth; its contents are additional directories (one per line)
to be added to sys.path.  Non-existing directories (or
non-directories) are never added to sys.path; no directory is added to
sys.path more than once.  Blank lines and lines beginning with
\'#\' are skipped. Lines starting with \'import\' are executed.

For example, suppose sys.prefix and sys.exec_prefix are set to
/usr/local and there is a directory /usr/local/lib/python2.5/site-packages
with three subdirectories, foo, bar and spam, and two path
configuration files, foo.pth and bar.pth.  Assume foo.pth contains the
following:

  # foo package configuration
  foo
  bar
  bletch

and bar.pth contains:

  # bar package configuration
  bar

Then the following directories are added to sys.path, in this order:

  /usr/local/lib/python2.5/site-packages/bar
  /usr/local/lib/python2.5/site-packages/foo

Note that bletch is omitted because it doesn\'t exist; bar precedes foo
because bar.pth comes alphabetically before foo.pth; and spam is
omitted because it is not mentioned in either path configuration file.

The readline module is also automatically configured to enable
completion for systems that support it.  This can be overridden in
sitecustomize, usercustomize or PYTHONSTARTUP.  Starting Python in
isolated mode (-I) disables automatic readline configuration.

After these operations, an attempt is made to import a module
named sitecustomize, which can perform arbitrary additional
site-specific customizations.  If this import fails with an
ImportError exception, it is silently ignored.
'''
import sys
import os
import builtins
import _sitebuiltins
import io
import stat
PREFIXES = [
    sys.prefix,
    sys.exec_prefix]
ENABLE_USER_SITE = None
USER_SITE = None
USER_BASE = None

def _trace(message):
    if sys.flags.verbose:
        print(message, file = sys.stderr)
        return None


def makepath(*paths):
    pass
# WARNING: Decompyle incomplete


def abs_paths():
