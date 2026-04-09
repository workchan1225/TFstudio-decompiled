# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _pybind_state.pyc (Python 3.11)

'''
Ensure that dependencies are available and then load the extension module.
'''
import os
import platform
import warnings
from  import _ld_preload
if platform.system() == 'Windows':
    from  import version_info
    if version_info.vs2019 and platform.architecture()[0] == '64bit':
        if not os.getenv('SystemRoot'):
            system_root = 'C:\\Windows'
            if not os.path.isfile(os.path.join(system_root, 'System32', 'vcruntime140_1.dll')):
                warnings.warn("Please install the 2019 Visual C++ runtime and then try again. If you've installed the runtime in a non-standard location (other than %SystemRoot%\\System32), make sure it can be found by setting the correct path.")
from onnxruntime_pybind11_state import *
