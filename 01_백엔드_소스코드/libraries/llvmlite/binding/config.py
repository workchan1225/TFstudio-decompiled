# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: config.pyc (Python 3.11)

import os
import warnings
from functools import cache
from ctypes import c_int, c_char_p
from llvmlite.binding import ffi
ffi.lib.LLVMPY_HasSVMLSupport.argtypes = ()
ffi.lib.LLVMPY_HasSVMLSupport.restype = c_int
ffi.lib.LLVMPY_IsStaticLibstdcxxLinkageBuild.argtypes = ()
ffi.lib.LLVMPY_IsStaticLibstdcxxLinkageBuild.restype = c_int
ffi.lib.LLVMPY_IsDynamicLLVMLinkageBuild.argtypes = ()
ffi.lib.LLVMPY_IsDynamicLLVMLinkageBuild.restype = c_int
ffi.lib.LLVMPY_PackageFormat.argtypes = ()
ffi.lib.LLVMPY_PackageFormat.restype = c_char_p
ffi.lib.LLVMPY_LlvmAssertionsState.argtypes = ()
ffi.lib.LLVMPY_LlvmAssertionsState.restype = c_char_p

def _has_svml():
    '''
    Returns True if SVML was enabled at FFI support compile time.
    '''
    if ffi.lib.LLVMPY_HasSVMLSupport() == 0:
        return False

has_svml = _has_svml()

def _build_llvm_linkage_type():
    '''
    Returns "static" if the FFI support is statically linked against LLVM,
    returns "dynamic" otherwise.
    '''
    if ffi.lib.LLVMPY_IsDynamicLLVMLinkageBuild() == 0:
        return 'static'

build_llvm_linkage_type = _build_llvm_linkage_type()

def _build_libstdcxx_linkage_type():
    '''
    Returns "static" if the FFI support is statically linked against libstdc++,
    returns "dynamic" otherwise.
    '''
    if ffi.lib.LLVMPY_IsStaticLibstdcxxLinkageBuild() == 1:
        return 'static'

build_libstdcxx_linkage_type = _build_libstdcxx_linkage_type()

def _package_format():
    '''
    Returns "wheel", "conda" or "unspecified"
    '''
    return ffi.lib.LLVMPY_PackageFormat().decode()

package_format = _package_format()

def _llvm_assertions_state():
    '''
    Returns one of "on", "off" or "unknown". Depending on whether it is
    determined that LLVM was build with assertions on, off, or is not known.
    "Is not known" is typically from a dynamic linkage against LLVM in which
    case it\'s not easily identified whether LLVM was built with assertions.
    '''
    return ffi.lib.LLVMPY_LlvmAssertionsState().decode()

llvm_assertions_state = _llvm_assertions_state()
get_sysinfo = (lambda : d = dict()d['ffi_lib_location'] = ffi.lib._named['package_format'] = package_formatd['llvm_linkage_type'] = build_llvm_linkage_typed['libstdcxx_linkage_type'] = build_libstdcxx_linkage_typed['llvm_assertions_state'] = llvm_assertions_stateHAVE_LIEF = Falsetry:
import liefHAVE_LIEF = Trueexcept ImportError:
msg = 'py-lief package not found, sysinfo is limited as a result'warnings.warn(msg)d['lief_probe_status'] = HAVE_LIEFd['linked_libraries'] = Noned['canonicalised_linked_libraries'] = None
def canonicalise_library_type(dso):
'''Canonicalises the representation of the binary::libraries as a
        sequence of strings'''
dso.libraries()
def canonicalise_library_spelling(libs):
fixes = []for lib in libs:
path_stripped = os.path.split(lib)[-1]prefix_libname = path_stripped.split('.')[0]linker_name = prefix_libname.replace('lib', '').replace('LIB', '')fixes.append(linker_name.lower())fixesif HAVE_LIEF:
dso = lief.parse(d['ffi_lib_location'])link_libs = tuple(canonicalise_library_type(dso))d['linked_libraries'] = link_libscanonicalised_libs = canonicalise_library_spelling(link_libs)d['canonicalised_linked_libraries'] = canonicalised_libsd)()
