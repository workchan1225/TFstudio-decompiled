# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bdist.pyc (Python 3.11)

"""distutils.command.bdist

Implements the Distutils 'bdist' command (create a built [binary]
distribution)."""
import os
from distutils.core import Command
from distutils.errors import *
from distutils.util import get_platform

def show_formats():
    '''Print list of available formats (arguments to "--format" option).
    '''
    FancyGetopt = FancyGetopt
    import distutils.fancy_getopt
    formats = []
    for format in bdist.format_commands:
        formats.append(('formats=' + format, None, bdist.format_command[format][1]))
        pretty_printer = FancyGetopt(formats)
        pretty_printer.print_help('List of available distribution formats:')
        return None


class bdist(Command):
    description = 'create a built (binary) distribution'
    user_options = [
        ('bdist-base=', 'b', 'temporary directory for creating built distributions'),
        ('plat-name=', 'p', 'platform name to embed in generated filenames (default: %s)' % get_platform()),
        ('formats=', None, 'formats for distribution (comma-separated list)'),
        ('dist-dir=', 'd', 'directory to put final built distributions in [default: dist]'),
        ('skip-build', None, 'skip rebuilding everything (for testing/debugging)'),
        ('owner=', 'u', 'Owner name used when creating a tar file [default: current user]'),
        ('group=', 'g', 'Group name used when creating a tar file [default: current group]')]
    boolean_options = [
        'skip-build']
    help_options = [
        ('help-formats', None, 'lists available distribution formats', show_formats)]
    no_format_option = ('bdist_rpm',)
    default_format = {
        'posix': 'gztar',
        'nt': 'zip' }
    format_commands = [
        'rpm',
        'gztar',
        'bztar',
        'xztar',
        'ztar',
        'tar',
        'zip']
    format_command = {
        'rpm': ('bdist_rpm', 'RPM distribution'),
        'gztar': ('bdist_dumb', "gzip'ed tar file"),
        'bztar': ('bdist_dumb', "bzip2'ed tar file"),
        'xztar': ('bdist_dumb', "xz'ed tar file"),
        'ztar': ('bdist_dumb', 'compressed tar file'),
        'tar': ('bdist_dumb', 'tar file'),
        'zip': ('bdist_dumb', 'ZIP file') }
    
    def initialize_options(self):
        self.bdist_base = None
        self.plat_name = None
        self.formats = None
        self.dist_dir = None
        self.skip_build = 0
        self.group = None
        self.owner = None

    
    def finalize_options(self):
        pass
    # WARNING: Decompyle incomplete

    
    def run(self):
        commands = []
        for format in self.formats:
            commands.append(self.format_command[format][0])
            except KeyError:
                raise DistutilsOptionError("invalid format '%s'" % format)
            for i in range(len(self.formats)):
                cmd_name = commands[i]
                sub_cmd = self.reinitialize_command(cmd_name)
                if cmd_name not in self.no_format_option:
                    sub_cmd.format = self.formats[i]
                if cmd_name == 'bdist_dumb':
                    sub_cmd.owner = self.owner
                    sub_cmd.group = self.group
                if cmd_name in commands[i + 1:]:
                    sub_cmd.keep_temp = 1
                self.run_command(cmd_name)
                return None
