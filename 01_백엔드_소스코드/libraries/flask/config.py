# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: config.pyc (Python 3.11)

from __future__ import annotations
import errno
import json
import os
import types
import typing as t
from werkzeug.utils import import_string

class ConfigAttribute:
    '''Makes an attribute forward to the config'''
    
    def __init__(self = None, name = None, get_converter = None):
        self.__name__ = name
        self.get_converter = get_converter

    
    def __get__(self = None, obj = None, owner = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __set__(self = None, obj = None, value = None):
        obj.config[self.__name__] = value



class Config(dict):
    pass
# WARNING: Decompyle incomplete
