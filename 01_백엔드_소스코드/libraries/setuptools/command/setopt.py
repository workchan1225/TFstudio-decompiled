# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: setopt.pyc (Python 3.11)

from distutils.util import convert_path
from distutils import log
from distutils.errors import DistutilsOptionError
import distutils
import os
import configparser
from setuptools import Command
__all__ = [
    'config_file',
    'edit_config',
    'option_base',
    'setopt']

def config_file(kind = ('local',)):
    '''Get the filename of the distutils, local, global, or per-user config

    `kind` must be one of "local", "global", or "user"
    '''
    if kind == 'local':
        return 'setup.cfg'
    if None == 'global':
        return os.path.join(os.path.dirname(distutils.__file__), 'distutils.cfg')
    if None == 'user':
        if os.name == 'posix':
            if not '.':
                dot = ''
                return os.path.expanduser(convert_path('~/%spydistutils.cfg' % dot))
            raise '.'("config_file() type must be 'local', 'global', or 'user'", kind)


def edit_config(filename, settings, dry_run = (False,)):
    '''Edit a configuration file to include `settings`

    `settings` is a dictionary of dictionaries or ``None`` values, keyed by
    command/section name.  A ``None`` value means to delete the entire section,
    while a dictionary lists settings to be changed or deleted in that section.
    A setting of ``None`` means to delete that setting.
    '''
    log.debug('Reading configuration from %s', filename)
    opts = configparser.RawConfigParser()
    
    opts.optionxform = lambda x: x
    opts.read([
        filename])
# WARNING: Decompyle incomplete


class option_base(Command):
    '''Abstract base class for commands that mess with config files'''
    user_options = [
        ('global-config', 'g', 'save options to the site-wide distutils.cfg file'),
        ('user-config', 'u', "save options to the current user's pydistutils.cfg file"),
        ('filename=', 'f', 'configuration file to use (default=setup.cfg)')]
    boolean_options = [
        'global-config',
        'user-config']
    
    def initialize_options(self):
        self.global_config = None
        self.user_config = None
        self.filename = None

    
    def finalize_options(self):
        filenames = []
        if self.global_config:
            filenames.append(config_file('global'))
        if self.user_config:
            filenames.append(config_file('user'))
    # WARNING: Decompyle incomplete



class setopt(option_base):
    '''Save command-line options to a file'''
    description = 'set an option in setup.cfg or another config file'
    user_options = [
        ('command=', 'c', 'command to set an option for'),
        ('option=', 'o', 'option to set'),
        ('set-value=', 's', 'value of the option'),
        ('remove', 'r', 'remove (unset) the value')] + option_base.user_options
    boolean_options = option_base.boolean_options + [
        'remove']
    
    def initialize_options(self):
        option_base.initialize_options(self)
        self.command = None
        self.option = None
        self.set_value = None
        self.remove = None

    
    def finalize_options(self):
        option_base.finalize_options(self)
    # WARNING: Decompyle incomplete

    
    def run(self):
        edit_config(self.filename, {
            self.command: {
                self.option.replace('-', '_'): self.set_value } }, self.dry_run)
