# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: onnxruntime_validation.pyc (Python 3.11)

'''
Check OS requirements for ONNX Runtime Python Bindings.
'''
import linecache
import platform
import warnings

def check_distro_info():
    __my_distro__ = ''
    __my_distro_ver__ = ''
    __my_system__ = platform.system().lower()
    __OS_RELEASE_FILE__ = '/etc/os-release'
    __LSB_RELEASE_FILE__ = '/etc/lsb-release'
    if __my_system__ == 'windows':
        __my_distro__ = __my_system__
        __my_distro_ver__ = platform.release().lower()
        if __my_distro_ver__ not in ('10', '11', '2016server', '2019server', '2022server', '2025server'):
            warnings.warn(f'''Unsupported Windows version ({__my_distro_ver__}). ONNX Runtime supports Windows 10 and above, or Windows Server 2016 and above.''')
            return None
        return None
    if None == 'linux':
        __my_distro__ = linecache.getline(__OS_RELEASE_FILE__, 3)[3:-1]
        __my_distro_ver__ = linecache.getline(__OS_RELEASE_FILE__, 6)[12:-2]
        if not __my_distro__:
            __my_distro__ = linecache.getline(__LSB_RELEASE_FILE__, 1)[11:-1]
            __my_distro_ver__ = linecache.getline(__LSB_RELEASE_FILE__, 2)[16:-1]
        __my_distro__ = __my_distro__.lower()
        __my_distro_ver__ = __my_distro_ver__.lower()
        return None
    if None == 'darwin':
        __my_distro__ = __my_system__
        __my_distro_ver__ = platform.release().lower()
        if int(__my_distro_ver__.split('.')[0]) < 11:
            warnings.warn(f'''Unsupported macOS version ({__my_distro_ver__}). ONNX Runtime supports macOS 11.0 or later.''')
            return None
        return None
    if None == 'aix':
        import subprocess
        returned_output = subprocess.check_output('oslevel')
        __my_distro_ver__str = returned_output.decode('utf-8')
        __my_distro_ver = __my_distro_ver__str[:3]
        return None
    None.warn(f'''Unsupported platform ({__my_system__}). ONNX Runtime supports Linux, macOS, AIX and Windows platforms, only.''')


def get_package_name_and_version_info():
    package_name = ''
    version = ''
    cuda_version = ''
    
    try:
        version = __version__
        import build_and_package_info
        package_name = package_name
        import build_and_package_info
        
        try:
            cuda_version = cuda_version
            import build_and_package_info
            
            try:
                pass
            except ImportError:
                
                try:
                    pass
                try:
                    pass
                except Exception:
                    e = None
                    warnings.warn('WARNING: failed to collect package name and version info')
                    print(e)
                    e = None
                    del e
                except:
                    e = None
                    del e

                return (package_name, version, cuda_version)





def check_training_module():
    pass
# WARNING: Decompyle incomplete
