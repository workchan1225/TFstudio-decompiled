# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: core.pyc (Python 3.11)

import enum
import errno
import inspect
import os
import sys
import typing as t
from collections import abc
from contextlib import contextmanager
from contextlib import ExitStack
from functools import update_wrapper
from gettext import gettext as _
from gettext import ngettext
from itertools import repeat
from types import TracebackType
from  import types
from exceptions import Abort
from exceptions import BadParameter
from exceptions import ClickException
from exceptions import Exit
from exceptions import MissingParameter
from exceptions import UsageError
from formatting import HelpFormatter
from formatting import join_options
from globals import pop_context
from globals import push_context
from parser import _flag_needs_value
from parser import OptionParser
from parser import split_opt
from termui import confirm
from termui import prompt
from termui import style
from utils import _detect_program_name
from utils import _expand_args
from utils import echo
from utils import make_default_short_help
from utils import make_str
from utils import PacifyFlushWrapper
if t.TYPE_CHECKING:
    import typing_extensions as te
    from decorators import HelpOption
    from shell_completion import CompletionItem
F = t.TypeVar('F', bound = t.Callable[(..., t.Any)])
V = t.TypeVar('V')

def _complete_visible_commands(ctx = None, incomplete = None):
    """List all the subcommands of a group that start with the
    incomplete value and aren't hidden.

    :param ctx: Invocation context for the group.
    :param incomplete: Value being completed. May be empty.
    """
    pass
# WARNING: Decompyle incomplete


def _check_multicommand(base_command = None, cmd_name = None, cmd = None, register = (False,)):
    if not base_command.chain or isinstance(cmd, MultiCommand):
        return None
    if None:
        hint = 'It is not possible to add multi commands as children to another multi command that is in chain mode.'
    else:
        hint = 'Found a multi command as subcommand to a multi command that is in chain mode. This is not supported.'
    raise RuntimeError(f'''{hint}. Command {base_command.name!r} is set to chain and {cmd_name!r} was added as a subcommand but it in itself is a multi command. ({cmd_name!r} is a {type(cmd).__name__} within a chained {type(base_command).__name__} named {base_command.name!r}).''')


def batch(iterable = None, batch_size = None):
    pass
# WARNING: Decompyle incomplete

augment_usage_errors = (lambda ctx = None, param = None: pass# WARNING: Decompyle incomplete
)()

def iter_params_for_processing(invocation_order = None, declaration_order = None):
    '''Returns all declared parameters in the order they should be processed.

    The declared parameters are re-shuffled depending on the order in which
    they were invoked, as well as the eagerness of each parameters.

    The invocation order takes precedence over the declaration order. I.e. the
    order in which the user provided them to the CLI is respected.

    This behavior and its effect on callback evaluation is detailed at:
    https://click.palletsprojects.com/en/stable/advanced/#callback-evaluation-order
    '''
    pass
# WARNING: Decompyle incomplete


class ParameterSource(enum.Enum):
    """This is an :class:`~enum.Enum` that indicates the source of a
    parameter's value.

    Use :meth:`click.Context.get_parameter_source` to get the
    source for a parameter by name.

    .. versionchanged:: 8.0
        Use :class:`~enum.Enum` and drop the ``validate`` method.

    .. versionchanged:: 8.0
        Added the ``PROMPT`` value.
    """
    COMMANDLINE = enum.auto()
    ENVIRONMENT = enum.auto()
    DEFAULT = enum.auto()
    DEFAULT_MAP = enum.auto()
    PROMPT = enum.auto()


class Context:
    """The context is a special internal object that holds state relevant
    for the script execution at every single level.  It's normally invisible
    to commands unless they opt-in to getting access to it.

    The context is useful as it can pass internal objects around and can
    control special execution features such as reading data from
    environment variables.

    A context can be used as context manager in which case it will call
    :meth:`close` on teardown.

    :param command: the command class for this context.
    :param parent: the parent context.
    :param info_name: the info name for this invocation.  Generally this
                      is the most descriptive name for the script or
                      command.  For the toplevel script it is usually
                      the name of the script, for commands below it it's
                      the name of the script.
    :param obj: an arbitrary object of user data.
    :param auto_envvar_prefix: the prefix to use for automatic environment
                               variables.  If this is `None` then reading
                               from environment variables is disabled.  This
                               does not affect manually set environment
                               variables which are always read.
    :param default_map: a dictionary (like object) with default values
                        for parameters.
    :param terminal_width: the width of the terminal.  The default is
                           inherit from parent context.  If no context
                           defines the terminal width then auto
                           detection will be applied.
    :param max_content_width: the maximum width for content rendered by
                              Click (this currently only affects help
                              pages).  This defaults to 80 characters if
                              not overridden.  In other words: even if the
                              terminal is larger than that, Click will not
                              format things wider than 80 characters by
                              default.  In addition to that, formatters might
                              add some safety mapping on the right.
    :param resilient_parsing: if this flag is enabled then Click will
                              parse without any interactivity or callback
                              invocation.  Default values will also be
                              ignored.  This is useful for implementing
                              things such as completion support.
    :param allow_extra_args: if this is set to `True` then extra arguments
                             at the end will not raise an error and will be
                             kept on the context.  The default is to inherit
                             from the command.
    :param allow_interspersed_args: if this is set to `False` then options
                                    and arguments cannot be mixed.  The
                                    default is to inherit from the command.
    :param ignore_unknown_options: instructs click to ignore options it does
                                   not know and keeps them for later
                                   processing.
    :param help_option_names: optionally a list of strings that define how
                              the default help parameter is named.  The
                              default is ``['--help']``.
    :param token_normalize_func: an optional function that is used to
                                 normalize tokens (options, choices,
                                 etc.).  This for instance can be used to
                                 implement case insensitive behavior.
    :param color: controls if the terminal supports ANSI colors or not.  The
                  default is autodetection.  This is only needed if ANSI
                  codes are used in texts that Click prints which is by
                  default not the case.  This for instance would affect
                  help output.
    :param show_default: Show the default value for commands. If this
        value is not set, it defaults to the value from the parent
        context. ``Command.show_default`` overrides this default for the
        specific command.

    .. versionchanged:: 8.1
        The ``show_default`` parameter is overridden by
        ``Command.show_default``, instead of the other way around.

    .. versionchanged:: 8.0
        The ``show_default`` parameter defaults to the value from the
        parent context.

    .. versionchanged:: 7.1
       Added the ``show_default`` parameter.

    .. versionchanged:: 4.0
        Added the ``color``, ``ignore_unknown_options``, and
        ``max_content_width`` parameters.

    .. versionchanged:: 3.0
        Added the ``allow_extra_args`` and ``allow_interspersed_args``
        parameters.

    .. versionchanged:: 2.0
        Added the ``resilient_parsing``, ``help_option_names``, and
        ``token_normalize_func`` parameters.
    """
    formatter_class: t.Type['HelpFormatter'] = HelpFormatter
    
    def __init__(self, command, parent, info_name, obj, auto_envvar_prefix, default_map, terminal_width, max_content_width, resilient_parsing, allow_extra_args, allow_interspersed_args, ignore_unknown_options = None, help_option_names = None, token_normalize_func = None, color = (None, None, None, None, None, None, None, False, None, None, None, None, None, None, None), show_default = ('command', 'Command', 'parent', t.Optional['Context'], 'info_name', t.Optional[str], 'obj', t.Optional[t.Any], 'auto_envvar_prefix', t.Optional[str], 'default_map', t.Optional[t.MutableMapping[(str, t.Any)]], 'terminal_width', t.Optional[int], 'max_content_width', t.Optional[int], 'resilient_parsing', bool, 'allow_extra_args', t.Optional[bool], 'allow_interspersed_args', t.Optional[bool], 'ignore_unknown_options', t.Optional[bool], 'help_option_names', t.Optional[t.List[str]], 'token_normalize_func', t.Optional[t.Callable[([
        str], str)]], 'color', t.Optional[bool], 'show_default', t.Optional[bool], 'return', None)):
        self.parent = parent
        self.command = command
        self.info_name = info_name
        self.params = { }
        self.args = []
        self.protected_args = []
        self._opt_prefixes = set(parent._opt_prefixes) if parent else set()
    # WARNING: Decompyle incomplete

    
    def to_info_dict(self = None):
        '''Gather information that could be useful for a tool generating
        user-facing documentation. This traverses the entire CLI
        structure.

        .. code-block:: python

            with Context(cli) as ctx:
                info = ctx.to_info_dict()

        .. versionadded:: 8.0
        '''
        return {
            'command': self.command.to_info_dict(self),
            'info_name': self.info_name,
            'allow_extra_args': self.allow_extra_args,
            'allow_interspersed_args': self.allow_interspersed_args,
            'ignore_unknown_options': self.ignore_unknown_options,
            'auto_envvar_prefix': self.auto_envvar_prefix }

    
    def __enter__(self = None):
        push_context(self)
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, tb = ('exc_type', t.Optional[t.Type[BaseException]], 'exc_value', t.Optional[BaseException], 'tb', t.Optional[TracebackType], 'return', None)):
        if self._depth == 0:
            self.close()
        pop_context()

    scope = (lambda self = None, cleanup = None: pass# WARNING: Decompyle incomplete
)()
    meta = (lambda self = None: self._meta)()
    
    def make_formatter(self = None):
        '''Creates the :class:`~click.HelpFormatter` for the help and
        usage output.

        To quickly customize the formatter class used without overriding
        this method, set the :attr:`formatter_class` attribute.

        .. versionchanged:: 8.0
            Added the :attr:`formatter_class` attribute.
        '''
        return self.formatter_class(width = self.terminal_width, max_width = self.max_content_width)

    
    def with_resource(self = None, context_manager = None):
        '''Register a resource as if it were used in a ``with``
        statement. The resource will be cleaned up when the context is
        popped.

        Uses :meth:`contextlib.ExitStack.enter_context`. It calls the
        resource\'s ``__enter__()`` method and returns the result. When
        the context is popped, it closes the stack, which calls the
        resource\'s ``__exit__()`` method.

        To register a cleanup function for something that isn\'t a
        context manager, use :meth:`call_on_close`. Or use something
        from :mod:`contextlib` to turn it into a context manager first.

        .. code-block:: python

            @click.group()
            @click.option("--name")
            @click.pass_context
            def cli(ctx):
                ctx.obj = ctx.with_resource(connect_db(name))

        :param context_manager: The context manager to enter.
        :return: Whatever ``context_manager.__enter__()`` returns.

        .. versionadded:: 8.0
        '''
        return self._exit_stack.enter_context(context_manager)

    
    def call_on_close(self = None, f = None):
        """Register a function to be called when the context tears down.

        This can be used to close resources opened during the script
        execution. Resources that support Python's context manager
        protocol which would be used in a ``with`` statement should be
        registered with :meth:`with_resource` instead.

        :param f: The function to execute on teardown.
        """
        return self._exit_stack.callback(f)

    
    def close(self = None):
        '''Invoke all close callbacks registered with
        :meth:`call_on_close`, and exit all context managers entered
        with :meth:`with_resource`.
        '''
        self._exit_stack.close()
        self._exit_stack = ExitStack()

    command_path = (lambda self = None: rv = ''# WARNING: Decompyle incomplete
)()
    
    def find_root(self = None):
        '''Finds the outermost context.'''
        node = self
    # WARNING: Decompyle incomplete

    
    def find_object(self = None, object_type = None):
        '''Finds the closest object of a given type.'''
        node = self
    # WARNING: Decompyle incomplete

    
    def ensure_object(self = None, object_type = None):
        '''Like :meth:`find_object` but sets the innermost object to a
        new instance of `object_type` if it does not exist.
        '''
        rv = self.find_object(object_type)
    # WARNING: Decompyle incomplete

    lookup_default = (lambda self = None, name = None, call = t.overload: pass)()
    lookup_default = (lambda self = None, name = None, call = t.overload: pass)()
    
    def lookup_default(self = None, name = None, call = None):
        '''Get the default for a parameter from :attr:`default_map`.

        :param name: Name of the parameter.
        :param call: If the default is a callable, call it. Disable to
            return the callable instead.

        .. versionchanged:: 8.0
            Added the ``call`` parameter.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def fail(self = None, message = None):
        '''Aborts the execution of the program with a specific error
        message.

        :param message: the error message to fail with.
        '''
        raise UsageError(message, self)

    
    def abort(self = None):
        '''Aborts the script.'''
        raise Abort()

    
    def exit(self = None, code = None):
        '''Exits the application with a given exit code.'''
        raise Exit(code)

    
    def get_usage(self = None):
        '''Helper method to get formatted usage string for the current
        context and command.
        '''
        return self.command.get_usage(self)

    
    def get_help(self = None):
        '''Helper method to get formatted help page for the current
        context and command.
        '''
        return self.command.get_help(self)

    
    def _make_sub_context(self = None, command = None):
        '''Create a new context of the same type as this context, but
        for a new command.

        :meta private:
        '''
        return type(self)(command, info_name = command.name, parent = self)

    invoke = (lambda _Context__self = None, _Context__callback = None: pass)()
    invoke = (lambda _Context__self = None, _Context__callback = None: pass)()
    
    def invoke(_Context__self = None, _Context__callback = None, *args, **kwargs):
        '''Invokes a command callback in exactly the way it expects.  There
        are two ways to invoke this method:

        1.  the first argument can be a callback and all other arguments and
            keyword arguments are forwarded directly to the function.
        2.  the first argument is a click command object.  In that case all
            arguments are forwarded as well but proper click parameters
            (options and click arguments) must be keyword arguments and Click
            will fill in defaults.

        Note that before Click 3.2 keyword arguments were not properly filled
        in against the intention of this code and no context was created.  For
        more information about this change and why it was done in a bugfix
        release see :ref:`upgrade-to-3.2`.

        .. versionchanged:: 8.0
            All ``kwargs`` are tracked in :attr:`params` so they will be
            passed if :meth:`forward` is called at multiple levels.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def forward(_Context__self = None, _Context__cmd = None, *args, **kwargs):
        '''Similar to :meth:`invoke` but fills in default keyword
        arguments from the current context if the other command expects
        it.  This cannot invoke callbacks directly, only other commands.

        .. versionchanged:: 8.0
            All ``kwargs`` are tracked in :attr:`params` so they will be
            passed if ``forward`` is called at multiple levels.
        '''
        if not isinstance(_Context__cmd, Command):
            raise TypeError('Callback is not a command.')
    # WARNING: Decompyle incomplete

    
    def set_parameter_source(self = None, name = None, source = None):
        '''Set the source of a parameter. This indicates the location
        from which the value of the parameter was obtained.

        :param name: The name of the parameter.
        :param source: A member of :class:`~click.core.ParameterSource`.
        '''
        self._parameter_source[name] = source

    
    def get_parameter_source(self = None, name = None):
        '''Get the source of a parameter. This indicates the location
        from which the value of the parameter was obtained.

        This can be useful for determining when a user specified a value
        on the command line that is the same as the default value. It
        will be :attr:`~click.core.ParameterSource.DEFAULT` only if the
        value was actually taken from the default.

        :param name: The name of the parameter.
        :rtype: ParameterSource

        .. versionchanged:: 8.0
            Returns ``None`` if the parameter was not provided from any
            source.
        '''
        return self._parameter_source.get(name)



class BaseCommand:
    '''The base command implements the minimal API contract of commands.
    Most code will never use this as it does not implement a lot of useful
    functionality but it can act as the direct subclass of alternative
    parsing methods that do not depend on the Click parser.

    For instance, this can be used to bridge Click and other systems like
    argparse or docopt.

    Because base commands do not implement a lot of the API that other
    parts of Click take for granted, they are not supported for all
    operations.  For instance, they cannot be used with the decorators
    usually and they have no built-in callback system.

    .. versionchanged:: 2.0
       Added the `context_settings` parameter.

    :param name: the name of the command to use unless a group overrides it.
    :param context_settings: an optional dictionary with defaults that are
                             passed to the context object.
    '''
    context_class: t.Type[Context] = Context
    allow_extra_args = False
    allow_interspersed_args = True
    ignore_unknown_options = False
    
    def __init__(self = None, name = None, context_settings = None):
        self.name = name
    # WARNING: Decompyle incomplete

    
    def to_info_dict(self = None, ctx = None):
        '''Gather information that could be useful for a tool generating
        user-facing documentation. This traverses the entire structure
        below this command.

        Use :meth:`click.Context.to_info_dict` to traverse the entire
        CLI structure.

        :param ctx: A :class:`Context` representing this command.

        .. versionadded:: 8.0
        '''
        return {
            'name': self.name }

    
    def __repr__(self = None):
        return f'''<{self.__class__.__name__} {self.name}>'''

    
    def get_usage(self = None, ctx = None):
        raise NotImplementedError('Base commands cannot get usage')

    
    def get_help(self = None, ctx = None):
        raise NotImplementedError('Base commands cannot get help')

    
    def make_context(self = None, info_name = None, args = None, parent = (None,), **extra):
        """This function when given an info name and arguments will kick
        off the parsing and create a new :class:`Context`.  It does not
        invoke the actual command callback though.

        To quickly customize the context class used without overriding
        this method, set the :attr:`context_class` attribute.

        :param info_name: the info name for this invocation.  Generally this
                          is the most descriptive name for the script or
                          command.  For the toplevel script it's usually
                          the name of the script, for commands below it's
                          the name of the command.
        :param args: the arguments to parse as list of strings.
        :param parent: the parent context if available.
        :param extra: extra keyword arguments forwarded to the context
                      constructor.

        .. versionchanged:: 8.0
            Added the :attr:`context_class` attribute.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def parse_args(self = None, ctx = None, args = None):
        '''Given a context and a list of arguments this creates the parser
        and parses the arguments, then modifies the context as necessary.
        This is automatically invoked by :meth:`make_context`.
        '''
        raise NotImplementedError('Base commands do not know how to parse arguments.')

    
    def invoke(self = None, ctx = None):
        '''Given a context, this invokes the command.  The default
        implementation is raising a not implemented error.
        '''
        raise NotImplementedError('Base commands are not invocable by default')

    
    def shell_complete(self = None, ctx = None, incomplete = None):
        '''Return a list of completions for the incomplete value. Looks
        at the names of chained multi-commands.

        Any command could be part of a chained multi-command, so sibling
        commands are valid at any point during command completion. Other
        command classes will return more completions.

        :param ctx: Invocation context for this command.
        :param incomplete: Value being completed. May be empty.

        .. versionadded:: 8.0
        '''
        pass
    # WARNING: Decompyle incomplete

    main = (lambda self = None, args = None, prog_name = t.overload, complete_var = (None, None, None, True), standalone_mode = ('args', t.Optional[t.Sequence[str]], 'prog_name', t.Optional[str], 'complete_var', t.Optional[str], 'standalone_mode', 'te.Literal[True]', 'extra', t.Any, 'return', 'te.NoReturn'): pass)()
    main = (lambda self = None, args = None, prog_name = t.overload, complete_var = (None, None, None, ...), standalone_mode = ('args', t.Optional[t.Sequence[str]], 'prog_name', t.Optional[str], 'complete_var', t.Optional[str], 'standalone_mode', bool, 'extra', t.Any, 'return', t.Any): pass)()
    
    def main(self, args = None, prog_name = None, complete_var = None, standalone_mode = (None, None, None, True, True), windows_expand_args = ('args', t.Optional[t.Sequence[str]], 'prog_name', t.Optional[str], 'complete_var', t.Optional[str], 'standalone_mode', bool, 'windows_expand_args', bool, 'extra', t.Any, 'return', t.Any), **extra):
        '''This is the way to invoke a script with all the bells and
        whistles as a command line application.  This will always terminate
        the application after a call.  If this is not wanted, ``SystemExit``
        needs to be caught.

        This method is also available by directly calling the instance of
        a :class:`Command`.

        :param args: the arguments that should be used for parsing.  If not
                     provided, ``sys.argv[1:]`` is used.
        :param prog_name: the program name that should be used.  By default
                          the program name is constructed by taking the file
                          name from ``sys.argv[0]``.
        :param complete_var: the environment variable that controls the
                             bash completion support.  The default is
                             ``"_<prog_name>_COMPLETE"`` with prog_name in
                             uppercase.
        :param standalone_mode: the default behavior is to invoke the script
                                in standalone mode.  Click will then
                                handle exceptions and convert them into
                                error messages and the function will never
                                return but shut down the interpreter.  If
                                this is set to `False` they will be
                                propagated to the caller and the return
                                value of this function is the return value
                                of :meth:`invoke`.
        :param windows_expand_args: Expand glob patterns, user dir, and
            env vars in command line args on Windows.
        :param extra: extra keyword arguments are forwarded to the context
                      constructor.  See :class:`Context` for more information.

        .. versionchanged:: 8.0.1
            Added the ``windows_expand_args`` parameter to allow
            disabling command line arg expansion on Windows.

        .. versionchanged:: 8.0
            When taking arguments from ``sys.argv`` on Windows, glob
            patterns, user dir, and env vars are expanded.

        .. versionchanged:: 3.0
           Added the ``standalone_mode`` parameter.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _main_shell_completion(self = None, ctx_args = None, prog_name = None, complete_var = (None,)):
        '''Check if the shell is asking for tab completion, process
        that, then exit early. Called from :meth:`main` before the
        program is invoked.

        :param prog_name: Name of the executable in the shell.
        :param complete_var: Name of the environment variable that holds
            the completion instruction. Defaults to
            ``_{PROG_NAME}_COMPLETE``.

        .. versionchanged:: 8.2.0
            Dots (``.``) in ``prog_name`` are replaced with underscores (``_``).
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self = None, *args, **kwargs):
        '''Alias for :meth:`main`.'''
        pass
    # WARNING: Decompyle incomplete



class Command(BaseCommand):
    pass
# WARNING: Decompyle incomplete


class MultiCommand(Command):
    pass
# WARNING: Decompyle incomplete


class Group(MultiCommand):
    pass
# WARNING: Decompyle incomplete


class CommandCollection(MultiCommand):
    pass
# WARNING: Decompyle incomplete


def _check_iter(value = None):
    '''Check if the value is iterable but not a string. Raises a type
    error, or return an iterator over the value.
    '''
    if isinstance(value, str):
        raise TypeError
    return iter(value)


class Parameter:
    """A parameter to a command comes in two versions: they are either
    :class:`Option`\\s or :class:`Argument`\\s.  Other subclasses are currently
    not supported by design as some of the internals for parsing are
    intentionally not finalized.

    Some settings are supported by both options and arguments.

    :param param_decls: the parameter declarations for this option or
                        argument.  This is a list of flags or argument
                        names.
    :param type: the type that should be used.  Either a :class:`ParamType`
                 or a Python type.  The latter is converted into the former
                 automatically if supported.
    :param required: controls if this is optional or not.
    :param default: the default value if omitted.  This can also be a callable,
                    in which case it's invoked when the default is needed
                    without any arguments.
    :param callback: A function to further process or validate the value
        after type conversion. It is called as ``f(ctx, param, value)``
        and must return the value. It is called for all sources,
        including prompts.
    :param nargs: the number of arguments to match.  If not ``1`` the return
                  value is a tuple instead of single value.  The default for
                  nargs is ``1`` (except if the type is a tuple, then it's
                  the arity of the tuple). If ``nargs=-1``, all remaining
                  parameters are collected.
    :param metavar: how the value is represented in the help page.
    :param expose_value: if this is `True` then the value is passed onwards
                         to the command callback and stored on the context,
                         otherwise it's skipped.
    :param is_eager: eager values are processed before non eager ones.  This
                     should not be set for arguments or it will inverse the
                     order of processing.
    :param envvar: a string or list of strings that are environment variables
                   that should be checked.
    :param shell_complete: A function that returns custom shell
        completions. Used instead of the param's type completion if
        given. Takes ``ctx, param, incomplete`` and must return a list
        of :class:`~click.shell_completion.CompletionItem` or a list of
        strings.

    .. versionchanged:: 8.0
        ``process_value`` validates required parameters and bounded
        ``nargs``, and invokes the parameter callback before returning
        the value. This allows the callback to validate prompts.
        ``full_process_value`` is removed.

    .. versionchanged:: 8.0
        ``autocompletion`` is renamed to ``shell_complete`` and has new
        semantics described above. The old name is deprecated and will
        be removed in 8.1, until then it will be wrapped to match the
        new requirements.

    .. versionchanged:: 8.0
        For ``multiple=True, nargs>1``, the default must be a list of
        tuples.

    .. versionchanged:: 8.0
        Setting a default is no longer required for ``nargs>1``, it will
        default to ``None``. ``multiple=True`` or ``nargs=-1`` will
        default to ``()``.

    .. versionchanged:: 7.1
        Empty environment variables are ignored rather than taking the
        empty string value. This makes it possible for scripts to clear
        variables if they can't unset them.

    .. versionchanged:: 2.0
        Changed signature for parameter callback to also be passed the
        parameter. The old callback format will still work, but it will
        raise a warning to give you a chance to migrate the code easier.
    """
    param_type_name = 'parameter'
    
    def __init__(self, param_decls, type, required, default, callback, nargs, multiple, metavar = None, expose_value = None, is_eager = None, envvar = (None, None, False, None, None, None, False, None, True, False, None, None), shell_complete = ('param_decls', t.Optional[t.Sequence[str]], 'type', t.Optional[t.Union[(types.ParamType, t.Any)]], 'required', bool, 'default', t.Optional[t.Union[(t.Any, t.Callable[([], t.Any)])]], 'callback', t.Optional[t.Callable[([
        Context,
        'Parameter',
        t.Any], t.Any)]], 'nargs', t.Optional[int], 'multiple', bool, 'metavar', t.Optional[str], 'expose_value', bool, 'is_eager', bool, 'envvar', t.Optional[t.Union[(str, t.Sequence[str])]], 'shell_complete', t.Optional[t.Callable[([
        Context,
        'Parameter',
        str], t.Union[(t.List['CompletionItem'], t.List[str])])]], 'return', None)):
        self
        self
        self
    # WARNING: Decompyle incomplete

    
    def to_info_dict(self = None):
        '''Gather information that could be useful for a tool generating
        user-facing documentation.

        Use :meth:`click.Context.to_info_dict` to traverse the entire
        CLI structure.

        .. versionadded:: 8.0
        '''
        return {
            'name': self.name,
            'param_type_name': self.param_type_name,
            'opts': self.opts,
            'secondary_opts': self.secondary_opts,
            'type': self.type.to_info_dict(),
            'required': self.required,
            'nargs': self.nargs,
            'multiple': self.multiple,
            'default': self.default,
            'envvar': self.envvar }

    
    def __repr__(self = None):
        return f'''<{self.__class__.__name__} {self.name}>'''

    
    def _parse_decls(self = None, decls = None, expose_value = None):
        raise NotImplementedError()

    human_readable_name = (lambda self = None: self.name)()
    
    def make_metavar(self = None):
        pass
    # WARNING: Decompyle incomplete

    get_default = (lambda self = None, ctx = None, call = t.overload: pass)()
    get_default = (lambda self = None, ctx = None, call = t.overload: pass)()
    
    def get_default(self = None, ctx = None, call = None):
        '''Get the default for the parameter. Tries
        :meth:`Context.lookup_default` first, then the local default.

        :param ctx: Current context.
        :param call: If the default is a callable, call it. Disable to
            return the callable instead.

        .. versionchanged:: 8.0.2
            Type casting is no longer performed when getting a default.

        .. versionchanged:: 8.0.1
            Type casting can fail in resilient parsing mode. Invalid
            defaults will not prevent showing help text.

        .. versionchanged:: 8.0
            Looks at ``ctx.default_map`` first.

        .. versionchanged:: 8.0
            Added the ``call`` parameter.
        '''
        value = ctx.lookup_default(self.name, call = False)
    # WARNING: Decompyle incomplete

    
    def add_to_parser(self = None, parser = None, ctx = None):
        raise NotImplementedError()

    
    def consume_value(self = None, ctx = None, opts = None):
        value = opts.get(self.name)
        source = ParameterSource.COMMANDLINE
    # WARNING: Decompyle incomplete

    
    def type_cast_value(self = None, ctx = None, value = None):
        """Convert and validate a value against the option's
        :attr:`type`, :attr:`multiple`, and :attr:`nargs`.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def value_is_missing(self = None, value = None):
        pass
    # WARNING: Decompyle incomplete

    
    def process_value(self = None, ctx = None, value = None):
        value = self.type_cast_value(ctx, value)
        if self.required and self.value_is_missing(value):
            raise MissingParameter(ctx = ctx, param = self)
    # WARNING: Decompyle incomplete

    
    def resolve_envvar_value(self = None, ctx = None):
        pass
    # WARNING: Decompyle incomplete

    
    def value_from_envvar(self = None, ctx = None):
        rv = self.resolve_envvar_value(ctx)
    # WARNING: Decompyle incomplete

    
    def handle_parse_result(self = None, ctx = None, opts = None, args = ('ctx', Context, 'opts', t.Mapping[(str, t.Any)], 'args', t.List[str], 'return', t.Tuple[(t.Any, t.List[str])])):
        augment_usage_errors(ctx, param = self)
        (value, source) = self.consume_value(ctx, opts)
        ctx.set_parameter_source(self.name, source)
        value = self.process_value(ctx, value)

    
    def get_help_record(self = None, ctx = None):
        pass

    
    def get_usage_pieces(self = None, ctx = None):
        return []

    
    def get_error_hint(self = None, ctx = None):
