# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: shell_completion.pyc (Python 3.11)

import os
import re
import typing as t
from gettext import gettext as _
from core import Argument
from core import BaseCommand
from core import Context
from core import MultiCommand
from core import Option
from core import Parameter
from core import ParameterSource
from parser import split_arg_string
from utils import echo

def shell_complete(cli, ctx_args = None, prog_name = None, complete_var = None, instruction = ('cli', BaseCommand, 'ctx_args', t.MutableMapping[(str, t.Any)], 'prog_name', str, 'complete_var', str, 'instruction', str, 'return', int)):
    '''Perform shell completion for the given CLI program.

    :param cli: Command being called.
    :param ctx_args: Extra arguments to pass to
        ``cli.make_context``.
    :param prog_name: Name of the executable in the shell.
    :param complete_var: Name of the environment variable that holds
        the completion instruction.
    :param instruction: Value of ``complete_var`` with the completion
        instruction and shell, in the form ``instruction_shell``.
    :return: Status code to exit with.
    '''
    (shell, _, instruction) = instruction.partition('_')
    comp_cls = get_completion_class(shell)
# WARNING: Decompyle incomplete


class CompletionItem:
    '''Represents a completion value and metadata about the value. The
    default metadata is ``type`` to indicate special shell handling,
    and ``help`` if a shell supports showing a help string next to the
    value.

    Arbitrary parameters can be passed when creating the object, and
    accessed using ``item.attr``. If an attribute wasn\'t passed,
    accessing it returns ``None``.

    :param value: The completion suggestion.
    :param type: Tells the shell script to provide special completion
        support for the type. Click uses ``"dir"`` and ``"file"``.
    :param help: String shown next to the value if supported.
    :param kwargs: Arbitrary metadata. The built-in implementations
        don\'t use this, but custom type completions paired with custom
        shell support could use it.
    '''
    __slots__ = ('value', 'type', 'help', '_info')
    
    def __init__(self = None, value = None, type = None, help = ('plain', None), **kwargs):
        self.value = value
        self.type = type
        self.help = help
        self._info = kwargs

    
    def __getattr__(self = None, name = None):
        return self._info.get(name)


_SOURCE_BASH = '%(complete_func)s() {\n    local IFS=$\'\\n\'\n    local response\n\n    response=$(env COMP_WORDS="${COMP_WORDS[*]}" COMP_CWORD=$COMP_CWORD %(complete_var)s=bash_complete $1)\n\n    for completion in $response; do\n        IFS=\',\' read type value <<< "$completion"\n\n        if [[ $type == \'dir\' ]]; then\n            COMPREPLY=()\n            compopt -o dirnames\n        elif [[ $type == \'file\' ]]; then\n            COMPREPLY=()\n            compopt -o default\n        elif [[ $type == \'plain\' ]]; then\n            COMPREPLY+=($value)\n        fi\n    done\n\n    return 0\n}\n\n%(complete_func)s_setup() {\n    complete -o nosort -F %(complete_func)s %(prog_name)s\n}\n\n%(complete_func)s_setup;\n'
_SOURCE_ZSH = '#compdef %(prog_name)s\n\n%(complete_func)s() {\n    local -a completions\n    local -a completions_with_descriptions\n    local -a response\n    (( ! $+commands[%(prog_name)s] )) && return 1\n\n    response=("${(@f)$(env COMP_WORDS="${words[*]}" COMP_CWORD=$((CURRENT-1)) %(complete_var)s=zsh_complete %(prog_name)s)}")\n\n    for type key descr in ${response}; do\n        if [[ "$type" == "plain" ]]; then\n            if [[ "$descr" == "_" ]]; then\n                completions+=("$key")\n            else\n                completions_with_descriptions+=("$key":"$descr")\n            fi\n        elif [[ "$type" == "dir" ]]; then\n            _path_files -/\n        elif [[ "$type" == "file" ]]; then\n            _path_files -f\n        fi\n    done\n\n    if [ -n "$completions_with_descriptions" ]; then\n        _describe -V unsorted completions_with_descriptions -U\n    fi\n\n    if [ -n "$completions" ]; then\n        compadd -U -V unsorted -a completions\n    fi\n}\n\nif [[ $zsh_eval_context[-1] == loadautofunc ]]; then\n    # autoload from fpath, call function directly\n    %(complete_func)s "$@"\nelse\n    # eval/source/. command, register function for later\n    compdef %(complete_func)s %(prog_name)s\nfi\n'
_SOURCE_FISH = 'function %(complete_func)s;\n    set -l response (env %(complete_var)s=fish_complete COMP_WORDS=(commandline -cp) COMP_CWORD=(commandline -t) %(prog_name)s);\n\n    for completion in $response;\n        set -l metadata (string split "," $completion);\n\n        if test $metadata[1] = "dir";\n            __fish_complete_directories $metadata[2];\n        else if test $metadata[1] = "file";\n            __fish_complete_path $metadata[2];\n        else if test $metadata[1] = "plain";\n            echo $metadata[2];\n        end;\n    end;\nend;\n\ncomplete --no-files --command %(prog_name)s --arguments "(%(complete_func)s)";\n'

class ShellComplete:
    source_template: t.ClassVar[str] = 'Base class for providing shell completion support. A subclass for\n    a given shell will override attributes and methods to implement the\n    completion instructions (``source`` and ``complete``).\n\n    :param cli: Command being called.\n    :param prog_name: Name of the executable in the shell.\n    :param complete_var: Name of the environment variable that holds\n        the completion instruction.\n\n    .. versionadded:: 8.0\n    '
    
    def __init__(self, cli = None, ctx_args = None, prog_name = None, complete_var = ('cli', BaseCommand, 'ctx_args', t.MutableMapping[(str, t.Any)], 'prog_name', str, 'complete_var', str, 'return', None)):
        self.cli = cli
        self.ctx_args = ctx_args
        self.prog_name = prog_name
        self.complete_var = complete_var

    func_name = (lambda self = None: safe_name = re.sub('\\W*', '', self.prog_name.replace('-', '_'), flags = re.ASCII)f'''_{safe_name}_completion''')()
    
    def source_vars(self = None):
        '''Vars for formatting :attr:`source_template`.

        By default this provides ``complete_func``, ``complete_var``,
        and ``prog_name``.
        '''
        return {
            'complete_func': self.func_name,
            'complete_var': self.complete_var,
            'prog_name': self.prog_name }

    
    def source(self = None):
        '''Produce the shell script that defines the completion
        function. By default this ``%``-style formats
        :attr:`source_template` with the dict returned by
        :meth:`source_vars`.
        '''
        return self.source_template % self.source_vars()

    
    def get_completion_args(self = None):
        '''Use the env vars defined by the shell script to return a
        tuple of ``args, incomplete``. This must be implemented by
        subclasses.
        '''
        raise NotImplementedError

    
    def get_completions(self = None, args = None, incomplete = None):
        """Determine the context and last complete command or parameter
        from the complete args. Call that object's ``shell_complete``
        method to get the completions for the incomplete value.

        :param args: List of complete args before the incomplete value.
        :param incomplete: Value being completed. May be empty.
        """
        ctx = _resolve_context(self.cli, self.ctx_args, self.prog_name, args)
        (obj, incomplete) = _resolve_incomplete(ctx, args, incomplete)
        return obj.shell_complete(ctx, incomplete)

    
    def format_completion(self = None, item = None):
        '''Format a completion item into the form recognized by the
        shell script. This must be implemented by subclasses.

        :param item: Completion item to format.
        '''
        raise NotImplementedError

    
    def complete(self = None):
        '''Produce the completion data to send back to the shell.

        By default this calls :meth:`get_completion_args`, gets the
        completions, then calls :meth:`format_completion` for each
        completion.
        '''
        pass
    # WARNING: Decompyle incomplete



class BashComplete(ShellComplete):
    pass
# WARNING: Decompyle incomplete


class ZshComplete(ShellComplete):
    '''Shell completion for Zsh.'''
    name = 'zsh'
    source_template = _SOURCE_ZSH
    
    def get_completion_args(self = None):
        cwords = split_arg_string(os.environ['COMP_WORDS'])
        cword = int(os.environ['COMP_CWORD'])
        args = cwords[1:cword]
        
        try:
            incomplete = cwords[cword]
        except IndexError:
            incomplete = ''

        return (args, incomplete)

    
    def format_completion(self = None, item = None):
        return f'''{item.type}\n{item.value}\n{item.help if item.help else '_'}'''



class FishComplete(ShellComplete):
    '''Shell completion for Fish.'''
    name = 'fish'
    source_template = _SOURCE_FISH
    
    def get_completion_args(self = None):
        cwords = split_arg_string(os.environ['COMP_WORDS'])
        incomplete = os.environ['COMP_CWORD']
        args = cwords[1:]
        if incomplete and args and args[-1] == incomplete:
            args.pop()
        return (args, incomplete)

    
    def format_completion(self = None, item = None):
        if item.help:
            return f'''{item.type},{item.value}\t{item.help}'''
        return f'''{None.type},{item.value}'''


ShellCompleteType = t.TypeVar('ShellCompleteType', bound = t.Type[ShellComplete])
_available_shells: t.Dict[(str, t.Type[ShellComplete])] = {
    'bash': BashComplete,
    'fish': FishComplete,
    'zsh': ZshComplete }

def add_completion_class(cls = None, name = None):
    """Register a :class:`ShellComplete` subclass under the given name.
    The name will be provided by the completion instruction environment
    variable during completion.

    :param cls: The completion class that will handle completion for the
        shell.
    :param name: Name to register the class under. Defaults to the
        class's ``name`` attribute.
    """
    pass
# WARNING: Decompyle incomplete


def get_completion_class(shell = None):
    """Look up a registered :class:`ShellComplete` subclass by the name
    provided by the completion instruction environment variable. If the
    name isn't registered, returns ``None``.

    :param shell: Name the class is registered under.
    """
    return _available_shells.get(shell)


def _is_incomplete_argument(ctx = None, param = None):
    '''Determine if the given parameter is an argument that can still
    accept values.

    :param ctx: Invocation context for the command represented by the
        parsed complete args.
    :param param: Argument object being checked.
    '''
    if not isinstance(param, Argument):
        return False
# WARNING: Decompyle incomplete


def _start_of_option(ctx = None, value = None):
    '''Check if the value looks like the start of an option.'''
    if not value:
        return False
    c = None[0]
    return c in ctx._opt_prefixes


def _is_incomplete_option(ctx = None, args = None, param = None):
