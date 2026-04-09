# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: config.pyc (Python 3.11)

from __future__ import annotations
import configparser
import json
import os
import warnings
from typing import Any
conf: 'dict[str, dict[str, Any]]' = { }
default_conf_dir = os.path.join(os.path.expanduser('~'), '.config/fsspec')
conf_dir = os.environ.get('FSSPEC_CONFIG_DIR', default_conf_dir)

def set_conf_env(conf_dict, envdict = (os.environ,)):
    '''Set config values from environment variables

    Looks for variables of the form ``FSSPEC_<protocol>`` and
    ``FSSPEC_<protocol>_<kwarg>``. For ``FSSPEC_<protocol>`` the value is parsed
    as a json dictionary and used to ``update`` the config of the
    corresponding protocol. For ``FSSPEC_<protocol>_<kwarg>`` there is no
    attempt to convert the string value, but the kwarg keys will be lower-cased.

    The ``FSSPEC_<protocol>_<kwarg>`` variables are applied after the
    ``FSSPEC_<protocol>`` ones.

    Parameters
    ----------
    conf_dict : dict(str, dict)
        This dict will be mutated
    envdict : dict-like(str, str)
        Source for the values - usually the real environment
    '''
    kwarg_keys = []
    for key in envdict:
        if key.startswith('FSSPEC_') and len(key) > 7 and key[7] != '_':
            if key.count('_') > 1:
                kwarg_keys.append(key)
                continue
            value = json.loads(envdict[key])
            if isinstance(value, dict):
                (_, proto) = key.split('_', 1)
                conf_dict.setdefault(proto.lower(), { }).update(value)
                continue
            warnings.warn(f'''Ignoring environment variable {key} due to not being a dict: {type(value)}''')
            continue
            except json.decoder.JSONDecodeError:
                ex = None
                warnings.warn(f'''Ignoring environment variable {key} due to a parse failure: {ex}''')
                ex = None
                del ex
                continue
                ex = None
                del ex
        if key.startswith('FSSPEC'):
            warnings.warn(f'''Ignoring environment variable {key} due to having an unexpected name''')
        for key in kwarg_keys:
            (_, proto, kwarg) = key.split('_', 2)
            conf_dict.setdefault(proto.lower(), { })[kwarg.lower()] = envdict[key]
            return None


def set_conf_files(cdir, conf_dict):
    '''Set config values from files

    Scans for INI and JSON files in the given dictionary, and uses their
    contents to set the config. In case of repeated values, later values
    win.

    In the case of INI files, all values are strings, and these will not
    be converted.

    Parameters
    ----------
    cdir : str
        Directory to search
    conf_dict : dict(str, dict)
        This dict will be mutated
    '''
    if not os.path.isdir(cdir):
        return None
    allfiles = None(os.listdir(cdir))
    for fn in allfiles:
        if fn.endswith('.ini'):
            ini = configparser.ConfigParser()
            ini.read(os.path.join(cdir, fn))
            for key in ini:
                if key == 'DEFAULT':
                    continue
                conf_dict.setdefault(key, { }).update(dict(ini[key]))
                if fn.endswith('.json'):
                    f = open(os.path.join(cdir, fn))
                    js = json.load(f)
                    None(None, None)
                else:
                    with None:
                        if not None:
                            pass
        for key in js:
            conf_dict.setdefault(key, { }).update(dict(js[key]))
            return None


def apply_config(cls, kwargs, conf_dict = (None,)):
    '''Supply default values for kwargs when instantiating class

    Augments the passed kwargs, by finding entries in the config dict
    which match the classes ``.protocol`` attribute (one or more str)

    Parameters
    ----------
    cls : file system implementation
    kwargs : dict
    conf_dict : dict of dict
        Typically this is the global configuration

    Returns
    -------
    dict : the modified set of kwargs
    '''
    pass
# WARNING: Decompyle incomplete

set_conf_files(conf_dir, conf)
set_conf_env(conf)
