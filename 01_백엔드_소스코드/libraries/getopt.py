# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: getopt.pyc (Python 3.11)

"""Parser for command line options.

This module helps scripts to parse the command line arguments in
sys.argv.  It supports the same conventions as the Unix getopt()
function (including the special meanings of arguments of the form `-'
and `--').  Long options similar to those supported by GNU software
may be used as well via an optional third argument.  This module
provides two functions and an exception:

getopt() -- Parse command line options
gnu_getopt() -- Like getopt(), but allow option and non-option arguments
to be intermixed.
GetoptError -- exception (class) raised with 'opt' attribute, which is the
option involved with the exception.
"""
__all__ = [
    'GetoptError',
    'error',
    'getopt',
    'gnu_getopt']
import os

try:
    from gettext import gettext as _
except ImportError:
    
    def _(s):
        return s



class GetoptError(Exception):
    opt = ''
    msg = ''
    
    def __init__(self, msg, opt = ('',)):
        self.msg = msg
        self.opt = opt
        Exception.__init__(self, msg, opt)

    
    def __str__(self):
        return self.msg


error = GetoptError

def getopt(args, shortopts, longopts = ([],)):
    '''getopt(args, options[, long_options]) -> opts, args

    Parses command line options and parameter list.  args is the
    argument list to be parsed, without the leading reference to the
    running program.  Typically, this means "sys.argv[1:]".  shortopts
    is the string of option letters that the script wants to
    recognize, with options that require an argument followed by a
    colon (i.e., the same format that Unix getopt() uses).  If
    specified, longopts is a list of strings with the names of the
    long options which should be supported.  The leading \'--\'
    characters should not be included in the option name.  Options
    which require an argument should be followed by an equal sign
    (\'=\').

    The return value consists of two elements: the first is a list of
    (option, value) pairs; the second is the list of program arguments
    left after the option list was stripped (this is a trailing slice
    of the first argument).  Each option-and-value pair returned has
    the option as its first element, prefixed with a hyphen (e.g.,
    \'-x\'), and the option argument as its second element, or an empty
    string if the option has no argument.  The options occur in the
    list in the same order in which they were found, thus allowing
    multiple occurrences.  Long and short options may be mixed.

    '''
    opts = []
    if type(longopts) == type(''):
        longopts = [
            longopts]
    else:
        longopts = list(longopts)
# WARNING: Decompyle incomplete


def gnu_getopt(args, shortopts, longopts = ([],)):
    """getopt(args, options[, long_options]) -> opts, args

    This function works like getopt(), except that GNU style scanning
    mode is used by default. This means that option and non-option
    arguments may be intermixed. The getopt() function stops
    processing options as soon as a non-option argument is
    encountered.

    If the first character of the option string is `+', or if the
    environment variable POSIXLY_CORRECT is set, then option
    processing stops as soon as a non-option argument is encountered.

    """
    opts = []
    prog_args = []
    if isinstance(longopts, str):
        longopts = [
            longopts]
    else:
        longopts = list(longopts)
    if shortopts.startswith('+'):
        shortopts = shortopts[1:]
        all_options_first = True
    elif os.environ.get('POSIXLY_CORRECT'):
        all_options_first = True
    else:
        all_options_first = False
# WARNING: Decompyle incomplete


def do_longs(opts, opt, longopts, args):
    
    try:
        i = opt.index('=')
        optarg = opt[i + 1:]
        opt = opt[:i]
    except ValueError:
        optarg = None

    (has_arg, opt) = long_has_args(opt, longopts)
# WARNING: Decompyle incomplete


def long_has_args(opt, longopts):
    pass
# WARNING: Decompyle incomplete


def do_shorts(opts, optstring, shortopts, args):
    pass
# WARNING: Decompyle incomplete


def short_has_arg(opt, shortopts):
    for i in range(len(shortopts)):
        if  == opt, shortopts[i] or opt, shortopts[i] != ':':
            pass
        
        
        return None, shortopts.startswith(':', i + 1)
        raise GetoptError(_('option -%s not recognized') % opt, opt)

if __name__ == '__main__':
    import sys
    print(getopt(sys.argv[1:], 'a:b', [
        'alpha=',
        'beta']))
    return None
