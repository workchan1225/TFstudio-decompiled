# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: func_inspect.pyc (Python 3.11)

'''
My own variation on function-specific inspect-like features.
'''
import collections
import inspect
import os
import re
import warnings
from itertools import islice
from tokenize import open as open_py_source
from logger import pformat
full_argspec_fields = 'args varargs varkw defaults kwonlyargs kwonlydefaults annotations'
full_argspec_type = collections.namedtuple('FullArgSpec', full_argspec_fields)

def get_func_code(func):
    """Attempts to retrieve a reliable function code hash.

    The reason we don't use inspect.getsource is that it caches the
    source, whereas we want this to be modified on the fly when the
    function is modified.

    Returns
    -------
    func_code: string
        The function code
    source_file: string
        The path to the file in which the function is defined.
    first_line: int
        The first line of the code in the source file.

    Notes
    ------
    This function does a bit more magic than inspect, and is thus
    more robust.
    """
    source_file = None
    
    try:
        code = func.__code__
        source_file = code.co_filename
        if not os.path.exists(source_file):
            source_code = ''.join(inspect.getsourcelines(func)[0])
            line_no = 1
            if source_file.startswith('<doctest '):
                (source_file, line_no) = re.match('\\<doctest (.*\\.rst)\\[(.*)\\]\\>', source_file).groups()
                line_no = int(line_no)
                source_file = '<doctest %s>' % source_file
            return (source_code, source_file, line_no)
        source_file_obj = None(source_file)
        first_line = code.co_firstlineno
        source_lines = list(islice(source_file_obj, first_line - 1, None))
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        return (''.join(inspect.getblock(source_lines)), source_file, first_line)
                    except:
                        if hasattr(func, '__code__'):
                            return 
                        return 






def _clean_win_chars(string):
    '''Windows cannot encode some characters in filename.'''
    import urllib
    if hasattr(urllib, 'quote'):
        quote = urllib.quote
    else:
        import urllib.parse as urllib
        quote = urllib.parse.quote
    for char in ('<', '>', '!', ':', '\\'):
        string = string.replace(char, quote(char))
        return string


def get_func_name(func, resolv_alias, win_characters = (True, True)):
    '''Return the function import path (as a list of module names), and
    a name for the function.

    Parameters
    ----------
    func: callable
        The func to inspect
    resolv_alias: boolean, optional
        If true, possible local aliases are indicated.
    win_characters: boolean, optional
        If true, substitute special characters using urllib.quote
        This is useful in Windows, as it cannot encode some filenames
    '''
    if hasattr(func, '__module__'):
        module = func.__module__
# WARNING: Decompyle incomplete


def _signature_str(function_name, arg_sig):
    '''Helper function to output a function signature'''
    return '{}{}'.format(function_name, arg_sig)


def _function_called_str(function_name, args, kwargs):
    '''Helper function to output a function call'''
    template_str = '{0}({1}, {2})'
    args_str = repr(args)[1:-1]
    kwargs_str = (lambda .0: pass# WARNING: Decompyle incomplete
)(kwargs.items()())
    return template_str.format(function_name, args_str, kwargs_str)


def filter_args(func, ignore_lst, args, kwargs = ((), dict())):
    """Filters the given args and kwargs using a list of arguments to
    ignore, and a function specification.

    Parameters
    ----------
    func: callable
        Function giving the argument specification
    ignore_lst: list of strings
        List of arguments to ignore (either a name of an argument
        in the function spec, or '*', or '**')
    *args: list
        Positional arguments passed to the function.
    **kwargs: dict
        Keyword arguments passed to the function

    Returns
    -------
    filtered_args: list
        List of filtered positional and keyword arguments.
    """
    args = list(args)
    if isinstance(ignore_lst, str):
        raise ValueError(f'''ignore_lst must be a list of parameters to ignore {ignore_lst!s} (type {type(ignore_lst)!s}) was given''')
    if not inspect.ismethod(func) and inspect.isfunction(func):
        if ignore_lst:
            warnings.warn('Cannot inspect object %s, ignore list will not work.' % func, stacklevel = 2)
        return {
            '*': args,
            '**': kwargs }
    arg_sig = None.signature(func)
    arg_names = []
    arg_defaults = []
    arg_kwonlyargs = []
    arg_varargs = None
    arg_varkw = None
    for param in arg_sig.parameters.values():
        if param.kind is param.POSITIONAL_OR_KEYWORD:
            arg_names.append(param.name)
        elif param.kind is param.KEYWORD_ONLY:
            arg_names.append(param.name)
            arg_kwonlyargs.append(param.name)
        elif param.kind is param.VAR_POSITIONAL:
            arg_varargs = param.name
        elif param.kind is param.VAR_KEYWORD:
            arg_varkw = param.name
        if param.default is not param.empty:
            arg_defaults.append(param.default)
        if inspect.ismethod(func):
            args = [
                func.__self__] + args
            class_method_sig = inspect.signature(func.__func__)
            self_name = next(iter(class_method_sig.parameters))
            arg_names = [
                self_name] + arg_names
    (_, name) = get_func_name(func, resolv_alias = False)
    arg_dict = dict()
    arg_position = -1
# WARNING: Decompyle incomplete


def _format_arg(arg):
    formatted_arg = pformat(arg, indent = 2)
    if len(formatted_arg) > 1500:
        formatted_arg = '%s...' % formatted_arg[:700]
    return formatted_arg


def format_signature(func, *args, **kwargs):
    (module, name) = get_func_name(func)
    module = module()
    arg_str = list()
    previous_length = 0
    for arg in args:
        formatted_arg = _format_arg(arg)
        if previous_length > 80:
            formatted_arg = '\n%s' % formatted_arg
        previous_length = len(formatted_arg)
        arg_str.append(formatted_arg)
        (lambda .0: [ f'''{v!s}={_format_arg(i)!s}''' for v, i in .0 ])(kwargs.items()())
        arg_str = ', '.join(arg_str)
        signature = f'''{name!s}({arg_str!s})'''
        return (module_path, signature)


def format_call(func, args, kwargs, object_name = ('Memory',)):
    '''Returns a nicely formatted statement displaying the function
    call with the given arguments.
    '''
    pass
# WARNING: Decompyle incomplete
