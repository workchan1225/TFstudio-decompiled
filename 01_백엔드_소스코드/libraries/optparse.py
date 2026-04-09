# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: optparse.pyc (Python 3.11)

'''A powerful, extensible, and easy-to-use option parser.

By Greg Ward <gward@python.net>

Originally distributed as Optik.

For support, use the optik-users@lists.sourceforge.net mailing list
(http://lists.sourceforge.net/lists/listinfo/optik-users).

Simple usage example:

   from optparse import OptionParser

   parser = OptionParser()
   parser.add_option("-f", "--file", dest="filename",
                     help="write report to FILE", metavar="FILE")
   parser.add_option("-q", "--quiet",
                     action="store_false", dest="verbose", default=True,
                     help="don\'t print status messages to stdout")

   (options, args) = parser.parse_args()
'''
__version__ = '1.5.3'
__all__ = [
    'Option',
    'make_option',
    'SUPPRESS_HELP',
    'SUPPRESS_USAGE',
    'Values',
    'OptionContainer',
    'OptionGroup',
    'OptionParser',
    'HelpFormatter',
    'IndentedHelpFormatter',
    'TitledHelpFormatter',
    'OptParseError',
    'OptionError',
    'OptionConflictError',
    'OptionValueError',
    'BadOptionError',
    'check_choice']
__copyright__ = '\nCopyright (c) 2001-2006 Gregory P. Ward.  All rights reserved.\nCopyright (c) 2002-2006 Python Software Foundation.  All rights reserved.\n\nRedistribution and use in source and binary forms, with or without\nmodification, are permitted provided that the following conditions are\nmet:\n\n  * Redistributions of source code must retain the above copyright\n    notice, this list of conditions and the following disclaimer.\n\n  * Redistributions in binary form must reproduce the above copyright\n    notice, this list of conditions and the following disclaimer in the\n    documentation and/or other materials provided with the distribution.\n\n  * Neither the name of the author nor the names of its\n    contributors may be used to endorse or promote products derived from\n    this software without specific prior written permission.\n\nTHIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS\nIS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED\nTO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A\nPARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR\nCONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,\nEXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,\nPROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR\nPROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF\nLIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING\nNEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS\nSOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n'
import sys
import os
import textwrap

def _repr(self):
    return '<%s at 0x%x: %s>' % (self.__class__.__name__, id(self), self)


try:
    from gettext import gettext, ngettext
except ImportError:
    
    def gettext(message):
        return message

    
    def ngettext(singular, plural, n):
        if n == 1:
            return singular


_ = gettext

class OptParseError(Exception):
    
    def __init__(self, msg):
        self.msg = msg

    
    def __str__(self):
        return self.msg



class OptionError(OptParseError):
    '''
    Raised if an Option instance is created with invalid or
    inconsistent arguments.
    '''
    
    def __init__(self, msg, option):
        self.msg = msg
        self.option_id = str(option)

    
    def __str__(self):
        if self.option_id:
            return f'''option {self.option_id!s}: {self.msg!s}'''
        return None.msg



class OptionConflictError(OptionError):
    '''
    Raised if conflicting options are added to an OptionParser.
    '''
    pass


class OptionValueError(OptParseError):
    '''
    Raised if an invalid option value is encountered on the command
    line.
    '''
    pass


class BadOptionError(OptParseError):
    '''
    Raised if an invalid option is seen on the command line.
    '''
    
    def __init__(self, opt_str):
        self.opt_str = opt_str

    
    def __str__(self):
        return _('no such option: %s') % self.opt_str



class AmbiguousOptionError(BadOptionError):
    '''
    Raised if an ambiguous option is seen on the command line.
    '''
    
    def __init__(self, opt_str, possibilities):
        BadOptionError.__init__(self, opt_str)
        self.possibilities = possibilities

    
    def __str__(self):
        return _('ambiguous option: %s (%s?)') % (self.opt_str, ', '.join(self.possibilities))



class HelpFormatter:
    '''
    Abstract base class for formatting option help.  OptionParser
    instances should use one of the HelpFormatter subclasses for
    formatting help; by default IndentedHelpFormatter is used.

    Instance attributes:
      parser : OptionParser
        the controlling OptionParser instance
      indent_increment : int
        the number of columns to indent per nesting level
      max_help_position : int
        the maximum starting column for option help text
      help_position : int
        the calculated starting column for option help text;
        initially the same as the maximum
      width : int
        total number of columns for output (pass None to constructor for
        this value to be taken from the $COLUMNS environment variable)
      level : int
        current indentation level
      current_indent : int
        current indentation level (in columns)
      help_width : int
        number of columns available for option help text (calculated)
      default_tag : str
        text to replace with each option\'s default value, "%default"
        by default.  Set to false value to disable default value expansion.
      option_strings : { Option : str }
        maps Option instances to the snippet of help text explaining
        the syntax of that option, e.g. "-h, --help" or
        "-fFILE, --file=FILE"
      _short_opt_fmt : str
        format string controlling how short options with values are
        printed in help text.  Must be either "%s%s" ("-fFILE") or
        "%s %s" ("-f FILE"), because those are the two syntaxes that
        Optik supports.
      _long_opt_fmt : str
        similar but for long options; must be either "%s %s" ("--file FILE")
        or "%s=%s" ("--file=FILE").
    '''
    NO_DEFAULT_VALUE = 'none'
    
    def __init__(self, indent_increment, max_help_position, width, short_first):
        self.parser = None
        self.indent_increment = indent_increment
    # WARNING: Decompyle incomplete

    
    def set_parser(self, parser):
        self.parser = parser

    
    def set_short_opt_delimiter(self, delim):
        if delim not in ('', ' '):
            raise ValueError('invalid metavar delimiter for short options: %r' % delim)
        self._short_opt_fmt = '%s' + delim + '%s'

    
    def set_long_opt_delimiter(self, delim):
        if delim not in ('=', ' '):
            raise ValueError('invalid metavar delimiter for long options: %r' % delim)
        self._long_opt_fmt = '%s' + delim + '%s'

    
    def indent(self):
        pass

    
    def dedent(self):
        pass
    # WARNING: Decompyle incomplete

    
    def format_usage(self, usage):
        raise NotImplementedError('subclasses must implement')

    
    def format_heading(self, heading):
        raise NotImplementedError('subclasses must implement')

    
    def _format_text(self, text):
        '''
        Format a paragraph of free-form text for inclusion in the
        help output at the current indentation level.
        '''
        text_width = max(self.width - self.current_indent, 11)
        indent = ' ' * self.current_indent
        return textwrap.fill(text, text_width, initial_indent = indent, subsequent_indent = indent)

    
    def format_description(self, description):
        if description:
            return self._format_text(description) + '\n'

    
    def format_epilog(self, epilog):
        if epilog:
            return '\n' + self._format_text(epilog) + '\n'

    
    def expand_default(self, option):
        pass
    # WARNING: Decompyle incomplete

    
    def format_option(self, option):
        pass
    # WARNING: Decompyle incomplete

    
    def store_option_strings(self, parser):
        self.indent()
        max_len = 0
        for opt in parser.option_list:
            strings = self.format_option_strings(opt)
            self.option_strings[opt] = strings
            max_len = max(max_len, len(strings) + self.current_indent)
            self.indent()
            for group in parser.option_groups:
                for opt in group.option_list:
                    strings = self.format_option_strings(opt)
                    self.option_strings[opt] = strings
                    max_len = max(max_len, len(strings) + self.current_indent)
                    self.dedent()
                    self.dedent()
                    self.help_position = min(max_len + 2, self.max_help_position)
                    self.help_width = max(self.width - self.help_position, 11)
                    return None

    
    def format_option_strings(self, option):
        '''Return a comma-separated list of option strings & metavariables.'''
        pass
    # WARNING: Decompyle incomplete



class IndentedHelpFormatter(HelpFormatter):
    '''Format help with indented section bodies.
    '''
    
    def __init__(self, indent_increment, max_help_position, width, short_first = (2, 24, None, 1)):
        HelpFormatter.__init__(self, indent_increment, max_help_position, width, short_first)

    
    def format_usage(self, usage):
        return _('Usage: %s\n') % usage

    
    def format_heading(self, heading):
        return '%*s%s:\n' % (self.current_indent, '', heading)



class TitledHelpFormatter(HelpFormatter):
    '''Format help with underlined section headers.
    '''
    
    def __init__(self, indent_increment, max_help_position, width, short_first = (0, 24, None, 0)):
        HelpFormatter.__init__(self, indent_increment, max_help_position, width, short_first)

    
    def format_usage(self, usage):
        return f'''{self.format_heading(_('Usage'))!s}  {usage!s}\n'''

    
    def format_heading(self, heading):
        return f'''{heading!s}\n{'=-'[self.level] * len(heading)!s}\n'''



def _parse_num(val, type):
    if val[:2].lower() == '0x':
        radix = 16
    elif val[:2].lower() == '0b':
        radix = 2
        if not val[2:]:
            val = '0'
        elif val[:1] == '0':
            radix = 8
        else:
            radix = 10
    return type(val, radix)


def _parse_int(val):
    return _parse_num(val, int)

_builtin_cvt = {
    'int': (_parse_int, _('integer')),
    'long': (_parse_int, _('integer')),
    'float': (float, _('floating-point')),
    'complex': (complex, _('complex')) }

def check_builtin(option, opt, value):
    (cvt, what) = _builtin_cvt[option.type]
    
    try:
        return cvt(value)
    except ValueError:
        raise OptionValueError(_('option %s: invalid %s value: %r') % (opt, what, value))



def check_choice(option, opt, value):
    if value in option.choices:
        return value
    choices = None.join(map(repr, option.choices))
    raise OptionValueError(_('option %s: invalid choice: %r (choose from %s)') % (opt, value, choices))

NO_DEFAULT = ('NO', 'DEFAULT')

class Option:
    '''
    Instance attributes:
      _short_opts : [string]
      _long_opts : [string]

      action : string
      type : string
      dest : string
      default : any
      nargs : int
      const : any
      choices : [string]
      callback : function
      callback_args : (any*)
      callback_kwargs : { string : any }
      help : string
      metavar : string
    '''
    ATTRS = [
        'action',
        'type',
        'dest',
        'default',
        'nargs',
        'const',
        'choices',
        'callback',
        'callback_args',
        'callback_kwargs',
        'help',
        'metavar']
    ACTIONS = ('store', 'store_const', 'store_true', 'store_false', 'append', 'append_const', 'count', 'callback', 'help', 'version')
    STORE_ACTIONS = ('store', 'store_const', 'store_true', 'store_false', 'append', 'append_const', 'count')
    TYPED_ACTIONS = ('store', 'append', 'callback')
    ALWAYS_TYPED_ACTIONS = ('store', 'append')
    CONST_ACTIONS = ('store_const', 'append_const')
    TYPES = ('string', 'int', 'long', 'float', 'complex', 'choice')
    TYPE_CHECKER = {
        'int': check_builtin,
        'long': check_builtin,
        'float': check_builtin,
        'complex': check_builtin,
        'choice': check_choice }
    CHECK_METHODS = None
    
    def __init__(self, *opts, **attrs):
        self._short_opts = []
        self._long_opts = []
        opts = self._check_opt_strings(opts)
        self._set_opt_strings(opts)
        self._set_attrs(attrs)
        for checker in self.CHECK_METHODS:
            checker(self)
            return None

    
    def _check_opt_strings(self, opts):
        opts = opts()
        if not opts:
            raise TypeError('at least one option string must be supplied')
        return opts

    
    def _set_opt_strings(self, opts):
        for opt in opts:
            if len(opt) < 2:
                raise OptionError('invalid option string %r: must be at least two characters long' % opt, self)
            if len(opt) == 2:
                if not opt[0] == '-' or opt[1] != '-':
                    raise OptionError('invalid short option string %r: must be of the form -x, (x any non-dash char)' % opt, self)
                self._short_opts.append(opt)
                continue
            if not opt[0:2] == '--' or opt[2] != '-':
                raise OptionError('invalid long option string %r: must start with --, followed by non-dash' % opt, self)
            self._long_opts.append(opt)
            return None

    
    def _set_attrs(self, attrs):
        for attr in self.ATTRS:
            if attr in attrs:
                setattr(self, attr, attrs[attr])
                del attrs[attr]
                continue
            if attr == 'default':
                setattr(self, attr, NO_DEFAULT)
                continue
            setattr(self, attr, None)
            if attrs:
                attrs = sorted(attrs.keys())
                raise OptionError('invalid keyword arguments: %s' % ', '.join(attrs), self)
            return None

    
    def _check_action(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _check_type(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _check_choice(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _check_dest(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _check_const(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _check_nargs(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _check_callback(self):
        pass
    # WARNING: Decompyle incomplete

    CHECK_METHODS = [
        _check_action,
        _check_type,
        _check_choice,
        _check_dest,
        _check_const,
        _check_nargs,
        _check_callback]
    
    def __str__(self):
        return '/'.join(self._short_opts + self._long_opts)

    __repr__ = _repr
    
    def takes_value(self):
        return self.type is not None

    
    def get_opt_string(self):
        if self._long_opts:
            return self._long_opts[0]
        return None._short_opts[0]

    
    def check_value(self, opt, value):
        checker = self.TYPE_CHECKER.get(self.type)
    # WARNING: Decompyle incomplete

    
    def convert_value(self, opt, value):
        pass
    # WARNING: Decompyle incomplete

    
    def process(self, opt, value, values, parser):
        value = self.convert_value(opt, value)
        return self.take_action(self.action, self.dest, opt, value, values, parser)

    
    def take_action(self, action, dest, opt, value, values, parser):
        if action == 'store':
            setattr(values, dest, value)
        elif action == 'store_const':
            setattr(values, dest, self.const)
        elif action == 'store_true':
            setattr(values, dest, True)
        elif action == 'store_false':
            setattr(values, dest, False)
        elif action == 'append':
            values.ensure_value(dest, []).append(value)
        elif action == 'append_const':
            values.ensure_value(dest, []).append(self.const)
        elif action == 'count':
            setattr(values, dest, values.ensure_value(dest, 0) + 1)
    # WARNING: Decompyle incomplete


SUPPRESS_HELP = 'SUPPRESSHELP'
SUPPRESS_USAGE = 'SUPPRESSUSAGE'

class Values:
    
    def __init__(self, defaults = (None,)):
        if defaults:
            for attr, val in defaults.items():
                setattr(self, attr, val)
        return None

    
    def __str__(self):
        return str(self.__dict__)

    __repr__ = _repr
    
    def __eq__(self, other):
        if isinstance(other, Values):
            return self.__dict__ == other.__dict__
        if None(other, dict):
            return self.__dict__ == other

    
    def _update_careful(self, dict):
        '''
        Update the option values from an arbitrary dictionary, but only
        use keys from dict that already have a corresponding attribute
        in self.  Any keys in dict without a corresponding attribute
        are silently ignored.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _update_loose(self, dict):
        '''
        Update the option values from an arbitrary dictionary,
        using all keys from the dictionary regardless of whether
        they have a corresponding attribute in self or not.
        '''
        self.__dict__.update(dict)

    
    def _update(self, dict, mode):
        if mode == 'careful':
            self._update_careful(dict)
            return None
        if None == 'loose':
            self._update_loose(dict)
            return None
        raise None('invalid update mode: %r' % mode)

    
    def read_module(self, modname, mode = ('careful',)):
        __import__(modname)
        mod = sys.modules[modname]
        self._update(vars(mod), mode)

    
    def read_file(self, filename, mode = ('careful',)):
        vars = { }
        exec(open(filename).read(), vars)
        self._update(vars, mode)

    
    def ensure_value(self, attr, value):
        pass
    # WARNING: Decompyle incomplete



class OptionContainer:
    '''
    Abstract base class.

    Class attributes:
      standard_option_list : [Option]
        list of standard options that will be accepted by all instances
        of this parser class (intended to be overridden by subclasses).

    Instance attributes:
      option_list : [Option]
        the list of Option objects contained by this OptionContainer
      _short_opt : { string : Option }
        dictionary mapping short option strings, eg. "-f" or "-X",
        to the Option instances that implement them.  If an Option
        has multiple short option strings, it will appear in this
        dictionary multiple times. [1]
      _long_opt : { string : Option }
        dictionary mapping long option strings, eg. "--file" or
        "--exclude", to the Option instances that implement them.
        Again, a given Option can occur multiple times in this
        dictionary. [1]
      defaults : { string : any }
        dictionary mapping option destination names to default
        values for each destination [1]

    [1] These mappings are common to (shared by) all components of the
        controlling OptionParser, where they are initially created.

    '''
    
    def __init__(self, option_class, conflict_handler, description):
        self._create_option_list()
        self.option_class = option_class
        self.set_conflict_handler(conflict_handler)
        self.set_description(description)

    
    def _create_option_mappings(self):
        self._short_opt = { }
        self._long_opt = { }
        self.defaults = { }

    
    def _share_option_mappings(self, parser):
        self._short_opt = parser._short_opt
        self._long_opt = parser._long_opt
        self.defaults = parser.defaults

    
    def set_conflict_handler(self, handler):
        if handler not in ('error', 'resolve'):
            raise ValueError('invalid conflict_resolution value %r' % handler)
        self.conflict_handler = handler

    
    def set_description(self, description):
        self.description = description

    
    def get_description(self):
        return self.description

    
    def destroy(self):
        '''see OptionParser.destroy().'''
        del self._short_opt
        del self._long_opt
        del self.defaults

    
    def _check_conflict(self, option):
        conflict_opts = []
        for opt in option._short_opts:
            if opt in self._short_opt:
                conflict_opts.append((opt, self._short_opt[opt]))
            for opt in option._long_opts:
                if opt in self._long_opt:
                    conflict_opts.append((opt, self._long_opt[opt]))
                if conflict_opts:
                    handler = self.conflict_handler
                    if handler == 'error':
                        raise 'conflicting option string(s): %s'(', '.join % (lambda .0: [ co[0] for co in .0 ])(conflict_opts()), option)
                    if handler == 'resolve':
                        for opt, c_option in conflict_opts:
                            if opt.startswith('--'):
                                c_option._long_opts.remove(opt)
                                del self._long_opt[opt]
                            else:
                                c_option._short_opts.remove(opt)
                                del self._short_opt[opt]
                            if not c_option._short_opts and c_option._long_opts:
                                c_option.container.option_list.remove(c_option)
                            return None
                            return None
                            return None

    
    def add_option(self, *args, **kwargs):
        '''add_option(Option)
           add_option(opt_str, ..., kwarg=val, ...)
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def add_options(self, option_list):
        for option in option_list:
            self.add_option(option)
            return None

    
    def get_option(self, opt_str):
