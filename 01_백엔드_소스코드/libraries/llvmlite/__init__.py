# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

''

def _delvewheel_patch_1_11_2():
    import os
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'llvmlite.libs'))
    if os.path.isdir(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'llvmlite.libs'))):
        os.add_dll_directory(libs_dir)
        return None

_delvewheel_patch_1_11_2()
del _delvewheel_patch_1_11_2
from _version import get_versions
__version__ = get_versions()['version']
del get_versions

def _ir_layer_typed_pointers_enabled():
    import os
    return os.environ.get('LLVMLITE_ENABLE_IR_LAYER_TYPED_POINTERS', '1') == '1'

ir_layer_typed_pointers_enabled = _ir_layer_typed_pointers_enabled()
del _ir_layer_typed_pointers_enabled
