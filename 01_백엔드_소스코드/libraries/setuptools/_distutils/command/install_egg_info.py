# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: install_egg_info.pyc (Python 3.11)

"""
distutils.command.install_egg_info

Implements the Distutils 'install_egg_info' command, for installing
a package's PKG-INFO metadata.
"""
import os
import sys
import re
from distutils.cmd import Command
from distutils import log, dir_util

class install_egg_info(Command):
    '''Install an .egg-info file for the package'''
    description = "Install package's PKG-INFO metadata as an .egg-info file"
    user_options = [
        ('install-dir=', 'd', 'directory to install to')]
    
    def initialize_options(self):
        self.install_dir = None

    basename = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def finalize_options(self):
        self.set_undefined_options('install_lib', ('install_dir', 'install_dir'))
        self.target = os.path.join(self.install_dir, self.basename)
        self.outputs = [
            self.target]

    
    def run(self):
        target = self.target
        if not os.path.isdir(target) and os.path.islink(target):
            dir_util.remove_tree(target, dry_run = self.dry_run)
        elif os.path.exists(target):
            self.execute(os.unlink, (self.target,), 'Removing ' + target)
        elif not os.path.isdir(self.install_dir):
            self.execute(os.makedirs, (self.install_dir,), 'Creating ' + self.install_dir)
        log.info('Writing %s', target)
        if not self.dry_run:
            f = open(target, 'w', encoding = 'UTF-8')
            self.distribution.metadata.write_pkg_file(f)
            None(None, None)
            return None
        with None:
            if not None:
                pass
        return None

    
    def get_outputs(self):
        return self.outputs



def safe_name(name):
    """Convert an arbitrary string to a standard distribution name

    Any runs of non-alphanumeric/. characters are replaced with a single '-'.
    """
    return re.sub('[^A-Za-z0-9.]+', '-', name)


def safe_version(version):
    '''Convert an arbitrary string to a standard version string

    Spaces become dots, and all other non-alphanumeric characters become
    dashes, with runs of multiple dashes condensed to a single dash.
    '''
    version = version.replace(' ', '.')
    return re.sub('[^A-Za-z0-9.]+', '-', version)


def to_filename(name):
    """Convert a project or version name to its filename-escaped form

    Any '-' characters are currently replaced with '_'.
    """
    return name.replace('-', '_')
