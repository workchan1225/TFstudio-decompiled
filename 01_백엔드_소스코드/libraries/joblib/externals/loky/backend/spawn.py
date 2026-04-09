# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: spawn.pyc (Python 3.11)

import os
import sys
import runpy
import textwrap
import types
from multiprocessing import process, util
if sys.platform != 'win32':
    WINEXE = False
    WINSERVICE = False
else:
    import msvcrt
    from multiprocessing.reduction import duplicate
    if sys.platform == 'win32':
        WINEXE = getattr(sys, 'frozen', False)
        WINSERVICE = sys.executable.lower().endswith('pythonservice.exe')
        if WINSERVICE:
            _python_exe = os.path.join(sys.exec_prefix, 'python.exe')
        else:
            _python_exe = sys.executable

def get_executable():
    return _python_exe


def _check_not_importing_main():
    if getattr(process.current_process(), '_inheriting', False):
        raise RuntimeError(textwrap.dedent('            An attempt has been made to start a new process before the\n            current process has finished its bootstrapping phase.\n\n            This probably means that you are not using fork to start your\n            child processes and you have forgotten to use the proper idiom\n            in the main module:\n\n                if __name__ == \'__main__\':\n                    freeze_support()\n                    ...\n\n            The "freeze_support()" line can be omitted if the program\n            is not going to be frozen to produce an executable.'))


def get_preparation_data(name, init_main_module = (True,)):
    '''Return info about parent needed by child to unpickle process object.'''
    _check_not_importing_main()
    d = dict(log_to_stderr = util._log_to_stderr, authkey = bytes(process.current_process().authkey), name = name, sys_argv = sys.argv, orig_dir = process.ORIGINAL_DIR, dir = os.getcwd())
    d['sys_path'] = sys.path()
# WARNING: Decompyle incomplete

old_main_modules = []

def prepare(data, parent_sentinel = (None,)):
    '''Try to get current process ready to unpickle process object.'''
    if 'name' in data:
        process.current_process().name = data['name']
    if 'authkey' in data:
        process.current_process().authkey = data['authkey']
    if 'log_to_stderr' in data and data['log_to_stderr']:
        util.log_to_stderr()
    if 'log_level' in data:
        util.get_logger().setLevel(data['log_level'])
    if 'log_fmt' in data:
        import logging
        util.get_logger().handlers[0].setFormatter(logging.Formatter(data['log_fmt']))
    if 'sys_path' in data:
        sys.path = data['sys_path']
    if 'sys_argv' in data:
        sys.argv = data['sys_argv']
    if 'dir' in data:
        os.chdir(data['dir'])
    if 'orig_dir' in data:
        process.ORIGINAL_DIR = data['orig_dir']
    if 'mp_tracker_fd' in data:
        mp_resource_tracker = _resource_tracker
        import multiprocessing.resource_tracker
        mp_resource_tracker._fd = data['mp_tracker_fd']
    if 'tracker_fd' in data:
        _resource_tracker = _resource_tracker
        import resource_tracker
        if sys.platform == 'win32':
            handle = data['tracker_fd']
            handle = duplicate(handle, source_process = parent_sentinel)
            _resource_tracker._fd = msvcrt.open_osfhandle(handle, os.O_RDONLY)
        else:
            _resource_tracker._fd = data['tracker_fd']
    if 'init_main_from_name' in data:
        _fixup_main_from_name(data['init_main_from_name'])
        return None
    if None in data:
        _fixup_main_from_path(data['init_main_from_path'])
        return None


def _fixup_main_from_name(mod_name):
    current_main = sys.modules['__main__']
    if mod_name == '__main__' or mod_name.endswith('.__main__'):
        return None
    if None(current_main.__spec__, 'name', None) == mod_name:
        return None
    None.append(current_main)
    main_module = types.ModuleType('__mp_main__')
    main_content = runpy.run_module(mod_name, run_name = '__mp_main__', alter_sys = True)
    main_module.__dict__.update(main_content)
    sys.modules['__main__'] = main_module
    sys.modules['__mp_main__'] = main_module


def _fixup_main_from_path(main_path):
    current_main = sys.modules['__main__']
    main_name = os.path.splitext(os.path.basename(main_path))[0]
    if main_name == 'ipython':
        return None
    if None(current_main, '__file__', None) == main_path:
        return None
    None.append(current_main)
    main_module = types.ModuleType('__mp_main__')
    main_content = runpy.run_path(main_path, run_name = '__mp_main__')
    main_module.__dict__.update(main_content)
    sys.modules['__main__'] = main_module
    sys.modules['__mp_main__'] = main_module
