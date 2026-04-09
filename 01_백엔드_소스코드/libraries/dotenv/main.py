# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: main.pyc (Python 3.11)

import io
import logging
import os
import shutil
import sys
import tempfile
from collections import OrderedDict
from contextlib import contextmanager
from typing import IO, Dict, Iterable, Iterator, Mapping, Optional, Tuple, Union
from parser import Binding, parse_stream
from variables import parse_variables
StrPath = Union[(str, 'os.PathLike[str]')]
logger = logging.getLogger(__name__)

def with_warn_for_invalid_lines(mappings = None):
    pass
# WARNING: Decompyle incomplete


class DotEnv:
    
    def __init__(self, dotenv_path, stream = None, verbose = None, encoding = None, interpolate = (None, False, None, True, True), override = ('dotenv_path', Optional[StrPath], 'stream', Optional[IO[str]], 'verbose', bool, 'encoding', Optional[str], 'interpolate', bool, 'override', bool, 'return', None)):
        self.dotenv_path = dotenv_path
        self.stream = stream
        self._dict = None
        self.verbose = verbose
        self.encoding = encoding
        self.interpolate = interpolate
        self.override = override

    _get_stream = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def dict(self = None):
        '''Return dotenv as dict'''
        if self._dict:
            return self._dict
        raw_values = None.parse()
        if self.interpolate:
            self._dict = OrderedDict(resolve_variables(raw_values, override = self.override))
        else:
            self._dict = OrderedDict(raw_values)
        return self._dict

    
    def parse(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def set_as_environment_variables(self = None):
        '''
        Load the current dotenv as system environment variable.
        '''
        if not self.dict():
            return False
    # WARNING: Decompyle incomplete

    
    def get(self = None, key = None):
        '''
        '''
        data = self.dict()
        if key in data:
            return data[key]
        if None.verbose:
            logger.warning('Key %s not found in %s.', key, self.dotenv_path)



def get_key(dotenv_path = None, key_to_get = None, encoding = None):
    """
    Get the value of a given key from the given .env.

    Returns `None` if the key isn't found or doesn't have a value.
    """
    return DotEnv(dotenv_path, verbose = True, encoding = encoding).get(key_to_get)

rewrite = (lambda path = None, encoding = None: pass# WARNING: Decompyle incomplete
)()

def set_key(dotenv_path, key_to_set = None, value_to_set = None, quote_mode = None, export = ('always', False, 'utf-8'), encoding = ('dotenv_path', StrPath, 'key_to_set', str, 'value_to_set', str, 'quote_mode', str, 'export', bool, 'encoding', Optional[str], 'return', Tuple[(Optional[bool], str, str)])):
    """
    Adds or Updates a key/value to the given .env

    If the .env path given doesn't exist, fails instead of risking creating
    an orphan .env somewhere in the filesystem
    """
    if quote_mode not in ('always', 'auto', 'never'):
        raise ValueError(f'''Unknown quote_mode: {quote_mode}''')
    if not quote_mode == 'always':
        if quote_mode == 'auto':
            quote = not value_to_set.isalnum()
            if quote:
                value_out = "'{}'".format(value_to_set.replace("'", "\\'"))
            else:
                value_out = value_to_set
    if export:
        line_out = f'''export {key_to_set}={value_out}\n'''
    else:
        line_out = f'''{key_to_set}={value_out}\n'''
    (source, dest) = rewrite(dotenv_path, encoding = encoding)
    replaced = False
    missing_newline = False
    for mapping in with_warn_for_invalid_lines(parse_stream(source)):
        if mapping.key == key_to_set:
            dest.write(line_out)
            replaced = True
            continue
        dest.write(mapping.original.string)
        missing_newline = not mapping.original.string.endswith('\n')
        if not replaced:
            if missing_newline:
                dest.write('\n')
            dest.write(line_out)
    None(None, None)


def unset_key(dotenv_path = None, key_to_unset = None, quote_mode = None, encoding = ('always', 'utf-8')):
    """
    Removes a given key from the given `.env` file.

    If the .env path given doesn't exist, fails.
    If the given key doesn't exist in the .env, fails.
    """
    if not os.path.exists(dotenv_path):
        logger.warning("Can't delete from %s - it doesn't exist.", dotenv_path)
        return (None, key_to_unset)
    removed = None
    (source, dest) = rewrite(dotenv_path, encoding = encoding)
    for mapping in with_warn_for_invalid_lines(parse_stream(source)):
        if mapping.key == key_to_unset:
            removed = True
            continue
        dest.write(mapping.original.string)
        None(None, None)
    with None:
        if not None:
            pass
    if not removed:
        logger.warning("Key %s not removed from %s - key doesn't exist.", key_to_unset, dotenv_path)
        return (None, key_to_unset)
    return (None, key_to_unset)


def resolve_variables(values = None, override = None):
    pass
# WARNING: Decompyle incomplete


def _walk_to_root(path = None):
    '''
    Yield directories starting from the given directory up to the root
    '''
    pass
# WARNING: Decompyle incomplete


def find_dotenv(filename = None, raise_error_if_not_found = None, usecwd = None):
    '''
    Search in increasingly higher folders for the given file

    Returns path to the file if found, or an empty string otherwise
    '''
    
    def _is_interactive():
        ''' Decide whether this is running in a REPL or IPython notebook '''
        main = __import__('__main__', None, None, fromlist = [
            '__file__'])
        return not hasattr(main, '__file__')

    if usecwd and _is_interactive() or getattr(sys, 'frozen', False):
        path = os.getcwd()
# WARNING: Decompyle incomplete


def load_dotenv(dotenv_path, stream = None, verbose = None, override = None, interpolate = (None, None, False, False, True, 'utf-8'), encoding = ('dotenv_path', Optional[StrPath], 'stream', Optional[IO[str]], 'verbose', bool, 'override', bool, 'interpolate', bool, 'encoding', Optional[str], 'return', bool)):
    '''Parse a .env file and then load all the variables found as environment variables.

    Parameters:
        dotenv_path: Absolute or relative path to .env file.
        stream: Text stream (such as `io.StringIO`) with .env content, used if
            `dotenv_path` is `None`.
        verbose: Whether to output a warning the .env file is missing.
        override: Whether to override the system environment variables with the variables
            from the `.env` file.
        encoding: Encoding to be used to read the file.
    Returns:
        Bool: True if at least one environment variable is set else False

    If both `dotenv_path` and `stream` are `None`, `find_dotenv()` is used to find the
    .env file.
    '''
    pass
# WARNING: Decompyle incomplete


def dotenv_values(dotenv_path = None, stream = None, verbose = None, interpolate = (None, None, False, True, 'utf-8'), encoding = ('dotenv_path', Optional[StrPath], 'stream', Optional[IO[str]], 'verbose', bool, 'interpolate', bool, 'encoding', Optional[str], 'return', Dict[(str, Optional[str])])):
    '''
    Parse a .env file and return its content as a dict.

    The returned dict will have `None` values for keys without values in the .env file.
    For example, `foo=bar` results in `{"foo": "bar"}` whereas `foo` alone results in
    `{"foo": None}`

    Parameters:
        dotenv_path: Absolute or relative path to the .env file.
        stream: `StringIO` object with .env content, used if `dotenv_path` is `None`.
        verbose: Whether to output a warning if the .env file is missing.
        encoding: Encoding to be used to read the file.

    If both `dotenv_path` and `stream` are `None`, `find_dotenv()` is used to find the
    .env file.
    '''
    pass
# WARNING: Decompyle incomplete
