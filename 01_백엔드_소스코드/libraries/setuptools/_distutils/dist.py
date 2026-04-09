# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dist.pyc (Python 3.11)

'''distutils.dist

Provides the Distribution class, which represents the module distribution
being built/installed/distributed.
'''
import sys
import os
import re
import pathlib
import contextlib
from email import message_from_file

try:
    import warnings
except ImportError:
    warnings = None

from distutils.errors import DistutilsOptionError, DistutilsModuleError, DistutilsArgError, DistutilsClassError
from distutils.fancy_getopt import FancyGetopt, translate_longopt
from distutils.util import check_environ, strtobool, rfc822_escape
from distutils import log
from distutils.debug import DEBUG
command_re = re.compile('^[a-zA-Z]([a-zA-Z0-9_]*)$')

def _ensure_list(value, fieldname):
    if isinstance(value, str):
        pass
# WARNING: Decompyle incomplete


class Distribution:
    """The core of the Distutils.  Most of the work hiding behind 'setup'
    is really done within a Distribution instance, which farms the work out
    to the Distutils commands specified on the command line.

    Setup scripts will almost never instantiate Distribution directly,
    unless the 'setup()' function is totally inadequate to their needs.
    However, it is conceivable that a setup script might wish to subclass
    Distribution for some specialized purpose, and then pass the subclass
    to 'setup()' as the 'distclass' keyword argument.  If so, it is
    necessary to respect the expectations that 'setup' has of Distribution.
    See the code for 'setup()', in core.py, for details.
    """
    global_options = [
        ('verbose', 'v', 'run verbosely (default)', 1),
        ('quiet', 'q', 'run quietly (turns verbosity off)'),
        ('dry-run', 'n', "don't actually do anything"),
        ('help', 'h', 'show detailed help message'),
        ('no-user-cfg', None, 'ignore pydistutils.cfg in your home directory')]
    common_usage = "Common commands: (see '--help-commands' for more)\n\n  setup.py build      will build the package underneath 'build/'\n  setup.py install    will install the package\n"
    display_options = [
        ('help-commands', None, 'list all available commands'),
        ('name', None, 'print package name'),
        ('version', 'V', 'print package version'),
        ('fullname', None, 'print <package name>-<version>'),
        ('author', None, "print the author's name"),
        ('author-email', None, "print the author's email address"),
        ('maintainer', None, "print the maintainer's name"),
        ('maintainer-email', None, "print the maintainer's email address"),
        ('contact', None, "print the maintainer's name if known, else the author's"),
        ('contact-email', None, "print the maintainer's email address if known, else the author's"),
        ('url', None, 'print the URL for this package'),
        ('license', None, 'print the license of the package'),
        ('licence', None, 'alias for --license'),
        ('description', None, 'print the package description'),
        ('long-description', None, 'print the long package description'),
        ('platforms', None, 'print the list of platforms'),
        ('classifiers', None, 'print the list of classifiers'),
        ('keywords', None, 'print the list of keywords'),
        ('provides', None, 'print the list of packages/modules provided'),
        ('requires', None, 'print the list of packages/modules required'),
        ('obsoletes', None, 'print the list of packages/modules made obsolete')]
    display_option_names = display_options()
    negative_opt = {
        'quiet': 'verbose' }
    
    def __init__(self, attrs = (None,)):
        '''Construct a new Distribution instance: initialize all the
        attributes of a Distribution, and then use \'attrs\' (a dictionary
        mapping attribute names to values) to assign some of those
        attributes their "real" values.  (Any attributes not mentioned in
        \'attrs\' will be assigned to some null value: 0, None, an empty list
        or dictionary, etc.)  Most importantly, initialize the
        \'command_obj\' attribute to the empty dictionary; this will be
        filled in with real command objects by \'parse_command_line()\'.
        '''
        self.verbose = 1
        self.dry_run = 0
        self.help = 0
    # WARNING: Decompyle incomplete

    
    def get_option_dict(self, command):
        """Get the option dictionary for a given command.  If that
        command's option dictionary hasn't been created yet, then create it
        and return the new dictionary; otherwise, return the existing
        option dictionary.
        """
        dict = self.command_options.get(command)
    # WARNING: Decompyle incomplete

    
    def dump_option_dicts(self, header, commands, indent = (None, None, '')):
        pformat = pformat
        import pprint
    # WARNING: Decompyle incomplete

    
    def find_config_files(self):
        """Find as many configuration files as should be processed for this
        platform, and return a list of filenames in the order in which they
        should be parsed.  The filenames returned are guaranteed to exist
        (modulo nasty race conditions).

        There are multiple possible config files:
        - distutils.cfg in the Distutils installation directory (i.e.
          where the top-level Distutils __inst__.py file lives)
        - a file in the user's home directory named .pydistutils.cfg
          on Unix and pydistutils.cfg on Windows/Mac; may be disabled
          with the ``--no-user-cfg`` option
        - setup.cfg in the current directory
        - a file named by an environment variable
        """
        check_environ()
        files = self._gen_paths()()
        if DEBUG:
            self.announce('using config files: %s' % ', '.join(files))
        return files

    
    def _gen_paths(self):
        pass
    # WARNING: Decompyle incomplete

    
    def parse_config_files(self, filenames = (None,)):
        ConfigParser = ConfigParser
        import configparser
        if sys.prefix != sys.base_prefix:
            ignore_options = [
                'install-base',
                'install-platbase',
                'install-lib',
                'install-platlib',
                'install-purelib',
                'install-headers',
                'install-scripts',
                'install-data',
                'prefix',
                'exec-prefix',
                'home',
                'user',
                'root']
        else:
            ignore_options = []
        ignore_options = frozenset(ignore_options)
    # WARNING: Decompyle incomplete

    
    def parse_command_line(self):
        '''Parse the setup script\'s command line, taken from the
        \'script_args\' instance attribute (which defaults to \'sys.argv[1:]\'
        -- see \'setup()\' in core.py).  This list is first processed for
        "global options" -- options that set attributes of the Distribution
        instance.  Then, it is alternately scanned for Distutils commands
        and options for that command.  Each new command terminates the
        options for the previous command.  The allowed options for a
        command are determined by the \'user_options\' attribute of the
        command class -- thus, we have to be able to load command classes
        in order to parse the command line.  Any error in that \'options\'
        attribute raises DistutilsGetoptError; any error on the
        command-line raises DistutilsArgError.  If no Distutils commands
        were found on the command line, raises DistutilsArgError.  Return
        true if command-line was successfully parsed and we should carry
        on with executing commands; false if no errors but we shouldn\'t
        execute commands (currently, this only happens if user asks for
        help).
        '''
        toplevel_options = self._get_toplevel_options()
        self.commands = []
        parser = FancyGetopt(toplevel_options + self.display_options)
        parser.set_negative_aliases(self.negative_opt)
        parser.set_aliases({
            'licence': 'license' })
        args = parser.getopt(args = self.script_args, object = self)
        option_order = parser.get_option_order()
        log.set_verbosity(self.verbose)
        if self.handle_display_options(option_order):
            return None
    # WARNING: Decompyle incomplete

    
    def _get_toplevel_options(self):
        '''Return the non-display options recognized at the top level.

        This includes options that are recognized *only* at the top
        level as well as options recognized for commands.
        '''
        return self.global_options + [
            ('command-packages=', None, 'list of packages that provide distutils commands')]

    
    def _parse_command_opts(self, parser, args):
        """Parse the command-line options for a single command.
        'parser' must be a FancyGetopt instance; 'args' must be the list
        of arguments, starting with the current command (whose options
        we are about to parse).  Returns a new version of 'args' with
        the next command at the front of the list; will be the empty
        list if there are no more commands on the command line.  Returns
        None if the user asked for help on this command.
        """
        Command = Command
        import distutils.cmd
        command = args[0]
        if not command_re.match(command):
            raise SystemExit("invalid command name '%s'" % command)
        self.commands.append(command)
        
        try:
            cmd_class = self.get_command_class(command)
        except DistutilsModuleError:
            msg = None
            raise DistutilsArgError(msg)
            msg = None
            del msg

        if not issubclass(cmd_class, Command):
            raise DistutilsClassError('command class %s must subclass Command' % cmd_class)
        if not hasattr(cmd_class, 'user_options') or isinstance(cmd_class.user_options, list):
            msg = "command class %s must provide 'user_options' attribute (a list of tuples)"
            raise DistutilsClassError(msg % cmd_class)
        negative_opt = self.negative_opt
        if hasattr(cmd_class, 'negative_opt'):
            negative_opt = negative_opt.copy()
            negative_opt.update(cmd_class.negative_opt)
        if hasattr(cmd_class, 'help_options') and isinstance(cmd_class.help_options, list):
            help_options = fix_help_options(cmd_class.help_options)
        else:
            help_options = []
        parser.set_option_table(self.global_options + cmd_class.user_options + help_options)
        parser.set_negative_aliases(negative_opt)
        (args, opts) = parser.getopt(args[1:])
        if hasattr(opts, 'help') and opts.help:
            self._show_help(parser, display_options = 0, commands = [
                cmd_class])
            return None
        if None(cmd_class, 'help_options') and isinstance(cmd_class.help_options, list):
            help_option_found = 0
            for help_option, short, desc, func in cmd_class.help_options:
                if hasattr(opts, parser.get_attr_name(help_option)):
                    help_option_found = 1
                    if callable(func):
                        func()
                        continue
                    raise DistutilsClassError(f'''invalid help function {func!r} for help option \'{help_option!s}\': must be a callable object (function, etc.)''')
                if help_option_found:
                    return None
                opt_dict = None.get_option_dict(command)
                for name, value in vars(opts).items():
                    opt_dict[name] = ('command line', value)
                    return args

    
    def finalize_options(self):
        '''Set final values for all the options on the Distribution
        instance, analogous to the .finalize_options() method of Command
        objects.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _show_help(self, parser, global_options, display_options, commands = (1, 1, [])):
        '''Show help for the setup script command-line in the form of
        several lists of command-line options.  \'parser\' should be a
        FancyGetopt instance; do not expect it to be returned in the
        same state, as its option table will be reset to make it
        generate the correct help text.

        If \'global_options\' is true, lists the global options:
        --verbose, --dry-run, etc.  If \'display_options\' is true, lists
        the "display-only" options: --name, --version, etc.  Finally,
        lists per-command help for every command name or command class
        in \'commands\'.
        '''
        gen_usage = gen_usage
        import distutils.core
        Command = Command
        import distutils.cmd
        if global_options:
            if display_options:
                options = self._get_toplevel_options()
            else:
                options = self.global_options
            parser.set_option_table(options)
            parser.print_help(self.common_usage + '\nGlobal options:')
            print('')
        if display_options:
            parser.set_option_table(self.display_options)
            parser.print_help('Information display options (just display information, ignore any commands)')
            print('')
        for command in self.commands:
            if isinstance(command, type) and issubclass(command, Command):
                klass = command
            else:
                klass = self.get_command_class(command)
            if hasattr(klass, 'help_options') and isinstance(klass.help_options, list):
                parser.set_option_table(klass.user_options + fix_help_options(klass.help_options))
            else:
                parser.set_option_table(klass.user_options)
            parser.print_help("Options for '%s' command:" % klass.__name__)
            print('')
            print(gen_usage(self.script_name))
            return None

    
    def handle_display_options(self, option_order):
        '''If there were any non-global "display-only" options
        (--help-commands or the metadata display options) on the command
        line, display the requested info and return true; else return
        false.
        '''
        gen_usage = gen_usage
        import distutils.core
        if self.help_commands:
            self.print_commands()
            print('')
            print(gen_usage(self.script_name))
            return 1
        any_display_options = None
        is_display_option = { }
        for option in self.display_options:
            is_display_option[option[0]] = 1
            for opt, val in option_order:
                if val and is_display_option.get(opt):
                    opt = translate_longopt(opt)
                    value = getattr(self.metadata, 'get_' + opt)()
                    if opt in ('keywords', 'platforms'):
                        print(','.join(value))
                    elif opt in ('classifiers', 'provides', 'requires', 'obsoletes'):
                        print('\n'.join(value))
                    else:
                        print(value)
                    any_display_options = 1
                return any_display_options

    
    def print_command_list(self, commands, header, max_length):
        """Print a subset of the list of all commands -- used by
        'print_commands()'.
        """
        print(header + ':')
        for cmd in commands:
            klass = self.cmdclass.get(cmd)
            if not klass:
                klass = self.get_command_class(cmd)
            description = klass.description
        except AttributeError:
            description = '(no description available)'
        print('  %-*s  %s' % (max_length, cmd, description))
        continue

    
    def print_commands(self):
        '''Print out a help message listing all available commands with a
        description of each.  The list is divided into "standard commands"
        (listed in distutils.command.__all__) and "extra commands"
        (mentioned in self.cmdclass, but not a standard command).  The
        descriptions come from the command class attribute
        \'description\'.
        '''
        import distutils.command as distutils
        std_commands = distutils.command.__all__
        is_std = { }
        for cmd in std_commands:
            is_std[cmd] = 1
            extra_commands = []
            for cmd in self.cmdclass.keys():
                if not is_std.get(cmd):
                    extra_commands.append(cmd)
                max_length = 0
                for cmd in std_commands + extra_commands:
                    if len(cmd) > max_length:
                        max_length = len(cmd)
                    self.print_command_list(std_commands, 'Standard commands', max_length)
                    if extra_commands:
                        print()
                        self.print_command_list(extra_commands, 'Extra commands', max_length)
                        return None
                    return None

    
    def get_command_list(self):
        '''Get a list of (command, description) tuples.
        The list is divided into "standard commands" (listed in
        distutils.command.__all__) and "extra commands" (mentioned in
        self.cmdclass, but not a standard command).  The descriptions come
        from the command class attribute \'description\'.
        '''
        import distutils.command as distutils
        std_commands = distutils.command.__all__
        is_std = { }
        for cmd in std_commands:
            is_std[cmd] = 1
            extra_commands = []
            for cmd in self.cmdclass.keys():
                if not is_std.get(cmd):
                    extra_commands.append(cmd)
                rv = []
                for cmd in std_commands + extra_commands:
                    klass = self.cmdclass.get(cmd)
                    if not klass:
                        klass = self.get_command_class(cmd)
                    description = klass.description
                except AttributeError:
                    description = '(no description available)'
                rv.append((cmd, description))
                return rv

    
    def get_command_packages(self):
        '''Return a list of packages from which commands are loaded.'''
        pkgs = self.command_packages
    # WARNING: Decompyle incomplete

    
    def get_command_class(self, command):
        '''Return the class that implements the Distutils command named by
        \'command\'.  First we check the \'cmdclass\' dictionary; if the
        command is mentioned there, we fetch the class object from the
        dictionary and return it.  Otherwise we load the command module
        ("distutils.command." + command) and fetch the command class from
        the module.  The loaded class is also stored in \'cmdclass\'
        to speed future calls to \'get_command_class()\'.

        Raises DistutilsModuleError if the expected module could not be
        found, or if that module does not define the expected class.
        '''
        klass = self.cmdclass.get(command)
        if klass:
            return klass
        for pkgname in None.get_command_packages():
            module_name = '{}.{}'.format(pkgname, command)
            klass_name = command
            __import__(module_name)
            module = sys.modules[module_name]
        except ImportError:
            continue
        klass = getattr(module, klass_name)

    
    def get_command_obj(self, command, create = (1,)):
        """Return the command object for 'command'.  Normally this object
        is cached on a previous call to 'get_command_obj()'; if no command
        object for 'command' is in the cache, then we either create and
        return it (if 'create' is true) or return None.
        """
        cmd_obj = self.command_obj.get(command)
        if cmd_obj and create:
            if DEBUG:
                self.announce("Distribution.get_command_obj(): creating '%s' command object" % command)
            klass = self.get_command_class(command)
            cmd_obj = klass(self)
            self.command_obj[command] = klass(self)
            self.have_run[command] = 0
            options = self.command_options.get(command)
            if options:
                self._set_command_options(cmd_obj, options)
        return cmd_obj

    
    def _set_command_options(self, command_obj, option_dict = (None,)):
        """Set the options for 'command_obj' from 'option_dict'.  Basically
        this means copying elements of a dictionary ('option_dict') to
        attributes of an instance ('command').

        'command_obj' must be a Command instance.  If 'option_dict' is not
        supplied, uses the standard option dictionary for this command
        (from 'self.command_options').
        """
        command_name = command_obj.get_command_name()
    # WARNING: Decompyle incomplete

    
    def reinitialize_command(self, command, reinit_subcommands = (0,)):
        '''Reinitializes a command to the state it was in when first
        returned by \'get_command_obj()\': ie., initialized but not yet
        finalized.  This provides the opportunity to sneak option
        values in programmatically, overriding or supplementing
        user-supplied values from the config files and command line.
        You\'ll have to re-finalize the command object (by calling
        \'finalize_options()\' or \'ensure_finalized()\') before using it for
        real.

        \'command\' should be a command name (string) or command object.  If
        \'reinit_subcommands\' is true, also reinitializes the command\'s
        sub-commands, as declared by the \'sub_commands\' class attribute (if
        it has one).  See the "install" command for an example.  Only
        reinitializes the sub-commands that actually matter, ie. those
        whose test predicates return true.

        Returns the reinitialized command object.
        '''
        Command = Command
        import distutils.cmd
        if not isinstance(command, Command):
            command_name = command
            command = self.get_command_obj(command_name)
        else:
            command_name = command.get_command_name()
        if not command.finalized:
            return command
        None.initialize_options()
        command.finalized = 0
        self.have_run[command_name] = 0
        self._set_command_options(command)
        if reinit_subcommands:
            for sub in command.get_sub_commands():
                self.reinitialize_command(sub, reinit_subcommands)
                return command

    
    def announce(self, msg, level = (log.INFO,)):
        log.log(level, msg)

    
    def run_commands(self):
        """Run each command that was seen on the setup script command line.
        Uses the list of commands found and cache of command objects
        created by 'get_command_obj()'.
        """
        for cmd in self.commands:
            self.run_command(cmd)
            return None

    
    def run_command(self, command):
        """Do whatever it takes to run a command (including nothing at all,
        if the command has already been run).  Specifically: if we have
        already created and run the command named by 'command', return
        silently without doing anything.  If the command named by 'command'
        doesn't even have a command object yet, create one.  Then invoke
        'run()' on that command object (or an existing one).
        """
        if self.have_run.get(command):
            return None
        None.info('running %s', command)
        cmd_obj = self.get_command_obj(command)
        cmd_obj.ensure_finalized()
        cmd_obj.run()
        self.have_run[command] = 1

    
    def has_pure_modules(self):
