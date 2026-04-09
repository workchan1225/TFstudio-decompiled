# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fancy_getopt.pyc (Python 3.11)

'''distutils.fancy_getopt

Wrapper around the standard getopt module that provides the following
additional features:
  * short and long options are tied together
  * options have help strings, so fancy_getopt could potentially
    create a complete usage summary
  * options set attributes of a passed-in object
'''
import sys
import string
import re
import getopt
from distutils.errors import DistutilsGetoptError, DistutilsArgError
longopt_pat = '[a-zA-Z](?:[a-zA-Z0-9-]*)'
longopt_re = re.compile('^%s$' % longopt_pat)
neg_alias_re = re.compile('^({})=!({})$'.format(longopt_pat, longopt_pat))
longopt_xlate = str.maketrans('-', '_')

class FancyGetopt:
    '''Wrapper around the standard \'getopt()\' module that provides some
    handy extra functionality:
      * short and long options are tied together
      * options have help strings, and help text can be assembled
        from them
      * options set attributes of a passed-in object
      * boolean options can have "negative aliases" -- eg. if
        --quiet is the "negative alias" of --verbose, then "--quiet"
        on the command line sets \'verbose\' to false
    '''
    
    def __init__(self, option_table = (None,)):
        self.option_table = option_table
        self.option_index = { }
        if self.option_table:
            self._build_index()
        self.alias = { }
        self.negative_alias = { }
        self.short_opts = []
        self.long_opts = []
        self.short2long = { }
        self.attr_name = { }
        self.takes_arg = { }
        self.option_order = []

    
    def _build_index(self):
        self.option_index.clear()
        for option in self.option_table:
            self.option_index[option[0]] = option
            return None

    
    def set_option_table(self, option_table):
        self.option_table = option_table
        self._build_index()

    
    def add_option(self, long_option, short_option, help_string = (None, None)):
        if long_option in self.option_index:
            raise DistutilsGetoptError("option conflict: already an option '%s'" % long_option)
        option = (long_option, short_option, help_string)
        self.option_table.append(option)
        self.option_index[long_option] = option

    
    def has_option(self, long_option):
        """Return true if the option table for this parser has an
        option with long name 'long_option'."""
        return long_option in self.option_index

    
    def get_attr_name(self, long_option):
        """Translate long option name 'long_option' to the form it
        has as an attribute of some object: ie., translate hyphens
        to underscores."""
        return long_option.translate(longopt_xlate)

    
    def _check_alias_dict(self, aliases, what):
        pass
    # WARNING: Decompyle incomplete

    
    def set_aliases(self, alias):
        '''Set the aliases for this option parser.'''
        self._check_alias_dict(alias, 'alias')
        self.alias = alias

    
    def set_negative_aliases(self, negative_alias):
        """Set the negative aliases for this option parser.
        'negative_alias' should be a dictionary mapping option names to
        option names, both the key and value must already be defined
        in the option table."""
        self._check_alias_dict(negative_alias, 'negative alias')
        self.negative_alias = negative_alias

    
    def _grok_option_table(self):
        """Populate the various data structures that keep tabs on the
        option table.  Called by 'getopt()' before it can do anything
        worthwhile.
        """
        self.long_opts = []
        self.short_opts = []
        self.short2long.clear()
        self.repeat = { }
    # WARNING: Decompyle incomplete

    
    def getopt(self, args, object = (None, None)):
        """Parse command-line options in args. Store as attributes on object.

        If 'args' is None or not supplied, uses 'sys.argv[1:]'.  If
        'object' is None or not supplied, creates a new OptionDummy
        object, stores option values there, and returns a tuple (args,
        object).  If 'object' is supplied, it is modified in place and
        'getopt()' just returns 'args'; in both cases, the returned
        'args' is a modified copy of the passed-in 'args' list, which
        is left untouched.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def get_option_order(self):
        """Returns the list of (option, value) tuples processed by the
        previous run of 'getopt()'.  Raises RuntimeError if
        'getopt()' hasn't been called yet.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def generate_help(self, header = (None,)):
        '''Generate help text (a list of strings, one per suggested line of
        output) from the option table for this FancyGetopt object.
        '''
        max_opt = 0
    # WARNING: Decompyle incomplete

    
    def print_help(self, header, file = (None, None)):
        pass
    # WARNING: Decompyle incomplete



def fancy_getopt(options, negative_opt, object, args):
    parser = FancyGetopt(options)
    parser.set_negative_aliases(negative_opt)
    return parser.getopt(args, object)

WS_TRANS = string.whitespace()

def wrap_text(text, width):
    """wrap_text(text : string, width : int) -> [string]

    Split 'text' into multiple lines of no more than 'width' characters
    each, and return the list of strings that results.
    """
    pass
# WARNING: Decompyle incomplete


def translate_longopt(opt):
    '''Convert a long option name to a valid Python identifier by
    changing "-" to "_".
    '''
    return opt.translate(longopt_xlate)


class OptionDummy:
    '''Dummy class just used as a place to hold command-line option
    values as instance attributes.'''
    
    def __init__(self, options = ([],)):
        """Create a new OptionDummy instance.  The attributes listed in
        'options' will be initialized to None."""
        for opt in options:
            setattr(self, opt, None)
            return None


if __name__ == '__main__':
    text = 'Tra-la-la, supercalifragilisticexpialidocious.\nHow *do* you spell that odd word, anyways?\n(Someone ask Mary -- she\'ll know [or she\'ll\nsay, "How should I know?"].)'
    for w in (10, 20, 30, 40):
        print('width: %d' % w)
        print('\n'.join(wrap_text(text, w)))
        print()
        return None
        return None
