# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: options.pyc (Python 3.11)

import json
import os
from selenium.webdriver.chromium.options import ChromiumOptions as _ChromiumOptions

class ChromeOptions(_ChromiumOptions):
    _session = None
    _user_data_dir = None
    user_data_dir = (lambda self: self._user_data_dir)()
    user_data_dir = (lambda self = None, path = property: apath = os.path.abspath(path)self._user_data_dir = os.path.normpath(apath))()
    _undot_key = (lambda key, value: if '.' in key:
(key, rest) = key.split('.', 1)value = ChromeOptions._undot_key(rest, value){
key: value })()
    _merge_nested = (lambda a, b: for key in b:
if key in a and isinstance(a[key], dict) and isinstance(b[key], dict):
ChromeOptions._merge_nested(a[key], b[key])continuea[key] = b[key]a)()
    
    def handle_prefs(self, user_data_dir):
        prefs = self.experimental_options.get('prefs')
        if prefs:
            if not user_data_dir:
                user_data_dir = self._user_data_dir
                default_path = os.path.join(user_data_dir, 'Default')
                os.makedirs(default_path, exist_ok = True)
                undot_prefs = { }
                for key, value in prefs.items():
                    undot_prefs = self._merge_nested(undot_prefs, self._undot_key(key, value))
                    prefs_file = os.path.join(default_path, 'Preferences')
                    if os.path.exists(prefs_file):
                        f = open(prefs_file, encoding = 'latin1', mode = 'r')
                        undot_prefs = self._merge_nested(json.load(f), undot_prefs)
                        None(None, None)
                    else:
                        with None:
                            if not None:
                                pass
            f = open(prefs_file, encoding = 'latin1', mode = 'w')
            json.dump(undot_prefs, f)
            None(None, None)
        else:
            with None:
                if not None:
                    pass
        del self._experimental_options['prefs']
        return None

    from_options = (lambda cls, options: o = cls()o.__dict__.update(options.__dict__)o)()
