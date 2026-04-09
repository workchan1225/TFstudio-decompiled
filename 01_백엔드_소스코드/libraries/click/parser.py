# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parser.pyc (Python 3.11)

"""
This module started out as largely a copy paste from the stdlib's
optparse module with the features removed that we do not need from
optparse because we implement them in Click on a higher level (for
instance type handling, help formatting and a lot more).

The plan is to remove more and more from here over time.

The reason this is a different module and not optparse from the stdlib
is that there are differences in 2.x and 3.x about the error messages
generated and optparse in the stdlib uses gettext for no good reason
and might cause us issues.

Click uses parts of optparse written by Gregory P. Ward and maintained
by the Python Software Foundation. This is limited to code in parser.py.

Copyright 2001-2006 Gregory P. Ward. All rights reserved.
Copyright 2002-2006 Python Software Foundation. All rights reserved.
"""
import typing as t
from collections import deque
from gettext import gettext as _
from gettext import ngettext
from exceptions import BadArgumentUsage
from exceptions import BadOptionUsage
from exceptions import NoSuchOption
from exceptions import UsageError
if t.TYPE_CHECKING:
    import typing_extensions as te
    from core import Argument as CoreArgument
    from core import Context
    from core import Option as CoreOption
    from core import Parameter as CoreParameter
V = t.TypeVar('V')
_flag_needs_value = object()

def _unpack_args(args = None, nargs_spec = None):
    '''Given an iterable of arguments and an iterable of nargs specifications,
    it returns a tuple with all the unpacked arguments at the first index
    and all remaining arguments as the second.

    The nargs specification is the number of arguments that should be consumed
    or `-1` to indicate that this position should eat up all the remainders.

    Missing items are filled with `None`.
    '''
    pass
# WARNING: Decompyle incomplete


def split_opt(opt = None):
    first = opt[:1]
    if first.isalnum():
        return ('', opt)
    if None[1:2] == first:
        return (opt[:2], opt[2:])
    return (None, opt[1:])


def normalize_opt(opt = None, ctx = None):
    pass
# WARNING: Decompyle incomplete


def split_arg_string(string = None):
    '''Split an argument string as with :func:`shlex.split`, but don\'t
    fail if the string is incomplete. Ignores a missing closing quote or
    incomplete escape sequence and uses the partial token as-is.

    .. code-block:: python

        split_arg_string("example \'my file")
        ["example", "my file"]

        split_arg_string("example my\\")
        ["example", "my"]

    :param string: String to split.
    '''
    import shlex
    lex = shlex.shlex(string, posix = True)
    lex.whitespace_split = True
    lex.commenters = ''
    out = []
    
    try:
        for token in lex:
            out.append(token)
    except ValueError:
        out.append(lex.token)

    return out


class Option:
    
    def __init__(self, obj, opts = None, dest = None, action = None, nargs = (None, 1, None), const = ('obj', 'CoreOption', 'opts', t.Sequence[str], 'dest', t.Optional[str], 'action', t.Optional[str], 'nargs', int, 'const', t.Optional[t.Any])):
        self._short_opts = []
        self._long_opts = []
        self.prefixes = set()
    # WARNING: Decompyle incomplete

    takes_value = (lambda self = None: self.action in ('store', 'append'))()
    
    def process(self = None, value = None, state = None):
        if self.action == 'store':
            state.opts[self.dest] = value
        elif self.action == 'store_const':
            state.opts[self.dest] = self.const
        elif self.action == 'append':
            state.opts.setdefault(self.dest, []).append(value)
        elif self.action == 'append_const':
            state.opts.setdefault(self.dest, []).append(self.const)
        elif self.action == 'count':
            state.opts[self.dest] = state.opts.get(self.dest, 0) + 1
        else:
            raise ValueError(f'''unknown action \'{self.action}\'''')
        state.order.append(self.obj)



class Argument:
    
    def __init__(self = None, obj = None, dest = None, nargs = (1,)):
        self.dest = dest
        self.nargs = nargs
        self.obj = obj

    
    def process(self = None, value = None, state = None):
        pass
    # WARNING: Decompyle incomplete



class ParsingState:
    
    def __init__(self = None, rargs = None):
        self.opts = { }
        self.largs = []
        self.rargs = rargs
        self.order = []



class OptionParser:
    """The option parser is an internal class that is ultimately used to
    parse options and arguments.  It's modelled after optparse and brings
    a similar but vastly simplified API.  It should generally not be used
    directly as the high level Click classes wrap it for you.

    It's not nearly as extensible as optparse or argparse as it does not
    implement features that are implemented on a higher level (such as
    types or defaults).

    :param ctx: optionally the :class:`~click.Context` where this parser
                should go with.
    """
    
    def __init__(self = None, ctx = None):
        self.ctx = ctx
        self.allow_interspersed_args = True
        self.ignore_unknown_options = False
    # WARNING: Decompyle incomplete

    
    def add_option(self, obj, opts = None, dest = None, action = None, nargs = (None, 1, None), const = ('obj', 'CoreOption', 'opts', t.Sequence[str], 'dest', t.Optional[str], 'action', t.Optional[str], 'nargs', int, 'const', t.Optional[t.Any], 'return', None)):
        '''Adds a new option named `dest` to the parser.  The destination
        is not inferred (unlike with optparse) and needs to be explicitly
        provided.  Action can be any of ``store``, ``store_const``,
        ``append``, ``append_const`` or ``count``.

        The `obj` can be used to identify the option in the order list
        that is returned from the parser.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def add_argument(self = None, obj = None, dest = None, nargs = (1,)):
        '''Adds a positional argument named `dest` to the parser.

        The `obj` can be used to identify the option in the order list
        that is returned from the parser.
        '''
        self._args.append(Argument(obj, dest = dest, nargs = nargs))

    
    def parse_args(self = None, args = None):
        '''Parses positional arguments and returns ``(values, args, order)``
        for the parsed options and arguments as well as the leftover
        arguments if there are any.  The order is a list of objects as they
        appear on the command line.  If arguments appear multiple times they
        will be memorized multiple times as well.
        '''
        state = ParsingState(args)
    # WARNING: Decompyle incomplete

    
    def _process_args_for_args(self = None, state = None):
        
        def <listcomp>(.0):
            return [ x.nargs for x in .0 ]

        (pargs, args) = state.largs + state.rargs(<listcomp>, self._args())
        for idx, arg in enumerate(self._args):
            arg.process(pargs[idx], state)
            state.largs = args
            state.rargs = []
            return None

    
    def _process_args_for_options(self = None, state = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _match_long_opt(self = None, opt = None, explicit_value = None, state = ('opt', str, 'explicit_value', t.Optional[str], 'state', ParsingState, 'return', None)):
        if opt not in self._long_opt:
            get_close_matches = get_close_matches
            import difflib
            possibilities = get_close_matches(opt, self._long_opt)
            raise NoSuchOption(opt, possibilities = possibilities, ctx = self.ctx)
        option = self._long_opt[opt]
    # WARNING: Decompyle incomplete

    
    def _match_short_opt(self = None, arg = None, state = None):
        stop = False
        i = 1
        prefix = arg[0]
        unknown_options = []
        for ch in arg[1:]:
            opt = normalize_opt(f'''{prefix}{ch}''', self.ctx)
            option = self._short_opt.get(opt)
            i += 1
            if not option:
                if self.ignore_unknown_options:
                    unknown_options.append(ch)
                    continue
                raise NoSuchOption(opt, ctx = self.ctx)
            if option.takes_value:
                if i < len(arg):
                    state.rargs.insert(0, arg[i:])
                    stop = True
                value = self._get_value_from_state(opt, option, state)
            else:
                value = None
            option.process(value, state)
            if stop:
                pass
            
            if self.ignore_unknown_options or unknown_options:
                state.largs.append(f'''{prefix}{''.join(unknown_options)}''')
                return None
            return None
            return None

    
    def _get_value_from_state(self = None, option_name = None, option = None, state = ('option_name', str, 'option', Option, 'state', ParsingState, 'return', t.Any)):
        nargs = option.nargs
        if len(state.rargs) < nargs:
            if option.obj._flag_needs_value:
                value = _flag_needs_value
            else:
                raise BadOptionUsage(option_name, ngettext('Option {name!r} requires an argument.', 'Option {name!r} requires {nargs} arguments.', nargs).format(name = option_name, nargs = nargs))
        if nargs == 1:
            next_rarg = state.rargs[0]
            if option.obj._flag_needs_value and isinstance(next_rarg, str) and next_rarg[:1] in self._opt_prefixes and len(next_rarg) > 1:
                value = _flag_needs_value
            else:
                value = state.rargs.pop(0)
        else:
            value = tuple(state.rargs[:nargs])
            del state.rargs[:nargs]
        return value

    
    def _process_opts(self = None, arg = None, state = None):
        explicit_value = None
        if '=' in arg:
            (long_opt, explicit_value) = arg.split('=', 1)
        else:
            long_opt = arg
        norm_long_opt = normalize_opt(long_opt, self.ctx)
        
        try:
            self._match_long_opt(norm_long_opt, explicit_value, state)
            return None
        except NoSuchOption:
            if arg[:2] not in self._opt_prefixes:
                self._match_short_opt(arg, state)
                return None
            if not None.ignore_unknown_options:
                raise 
            state.largs.append(arg)
            return None
