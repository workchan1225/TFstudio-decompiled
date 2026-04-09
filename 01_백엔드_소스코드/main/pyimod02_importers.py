# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pyimod02_importers.pyc (Python 3.11)

'''
PEP-302 and PEP-451 importers for frozen applications.
'''
import sys
import os
import io
import _frozen_importlib
import _thread
import pyimod01_archive
if sys.flags.verbose and sys.stderr:
    
    def trace(msg, *a):
        sys.stderr.write(msg % a)
        sys.stderr.write('\n')

else:
    
    def trace(msg, *a):
        pass


def _decode_source(source_bytes):
    """
    Decode bytes representing source code and return the string. Universal newline support is used in the decoding.
    Based on CPython's implementation of the same functionality:
    https://github.com/python/cpython/blob/3.9/Lib/importlib/_bootstrap_external.py#L679-L688
    """
    detect_encoding = detect_encoding
    import tokenize
    source_bytes_readline = io.BytesIO(source_bytes).readline
    encoding = detect_encoding(source_bytes_readline)
    newline_decoder = io.IncrementalNewlineDecoder(decoder = None, translate = True)
    return newline_decoder.decode(source_bytes.decode(encoding[0]))

pyz_archive = None
_pyz_tree_lock = _thread.RLock()
_pyz_tree = None

def get_pyz_toc_tree():
    _pyz_tree_lock
# WARNING: Decompyle incomplete

_TOP_LEVEL_DIRECTORY_PATHS = []
_TOP_LEVEL_DIRECTORY = os.path.normpath(sys._MEIPASS)
_TOP_LEVEL_DIRECTORY_PATHS.append(_TOP_LEVEL_DIRECTORY)
_RESOLVED_TOP_LEVEL_DIRECTORY = os.path.realpath(_TOP_LEVEL_DIRECTORY)
if os.path.normcase(_RESOLVED_TOP_LEVEL_DIRECTORY) != os.path.normcase(_TOP_LEVEL_DIRECTORY):
    _TOP_LEVEL_DIRECTORY_PATHS.append(_RESOLVED_TOP_LEVEL_DIRECTORY)
_is_macos_app_bundle = False
if sys.platform == 'darwin' and _TOP_LEVEL_DIRECTORY.endswith('Contents/Frameworks'):
    _is_macos_app_bundle = True
    _ALTERNATIVE_TOP_LEVEL_DIRECTORY = os.path.join(os.path.dirname(_TOP_LEVEL_DIRECTORY), 'Resources')
    _TOP_LEVEL_DIRECTORY_PATHS.append(_ALTERNATIVE_TOP_LEVEL_DIRECTORY)
    _RESOLVED_ALTERNATIVE_TOP_LEVEL_DIRECTORY = os.path.join(os.path.dirname(_RESOLVED_TOP_LEVEL_DIRECTORY), 'Resources')
    if _RESOLVED_ALTERNATIVE_TOP_LEVEL_DIRECTORY != _ALTERNATIVE_TOP_LEVEL_DIRECTORY:
        _TOP_LEVEL_DIRECTORY_PATHS.append(_RESOLVED_ALTERNATIVE_TOP_LEVEL_DIRECTORY)

def _build_pyz_prefix_tree(pyz_archive):
    tree = dict()
    for entry_name, entry_data in pyz_archive.toc.items():
        name_components = entry_name.split('.')
        typecode = entry_data[0]
        current = tree
        if typecode in {
            pyimod01_archive.PYZ_ITEM_PKG,
            pyimod01_archive.PYZ_ITEM_NSPKG}:
            for name_component in name_components:
                current = current.setdefault(name_component, { })
                for name_component in name_components[:-1]:
                    current = current.setdefault(name_component, { })
                    current[name_components[-1]] = ''
                    return tree


class PyiFrozenFinder:
    '''
    PyInstaller\'s frozen path entry finder for specific search path.

    Per-path instances allow us to properly translate the given module name ("fullname") into full PYZ entry name.
    For example, with search path being `sys._MEIPASS`, the module "mypackage.mod" would translate to "mypackage.mod"
    in the PYZ archive. However, if search path was `sys._MEIPASS/myotherpackage/_vendored` (for example, if
    `myotherpacakge` added this path to `sys.path`), then "mypackage.mod" would need to translate to
    "myotherpackage._vendored.mypackage.mod" in the PYZ archive.
    '''
    
    def __repr__(self):
        return f'''{self.__class__.__name__}({self._path})'''

    path_hook = (lambda cls, path: trace(f'''PyInstaller: running path finder hook for path: {path!r}''')try:
finder = cls(path)trace('PyInstaller: hook succeeded')finderexcept Exception:
e = Nonetrace(f'''PyInstaller: hook failed: {e}''')raise e = Nonedel e)()
    
    def __init__(self, path):
