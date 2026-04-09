# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: platform_.pyc (Python 3.11)

import os
import pathlib
import platform

def _data_root_Windows():
    (release, version, csd, ptype) = platform.win32_ver()
    root = pathlib.Path(os.environ.get('LOCALAPPDATA', os.environ.get('ProgramData', '.')))
    return root / 'Python Keyring'


def _data_root_Linux():
