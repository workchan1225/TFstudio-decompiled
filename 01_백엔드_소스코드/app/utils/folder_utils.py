# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: folder_utils.pyc (Python 3.11)

'''
Folder Utilities

Cross-platform folder opening with foreground window support.
On Windows, uses Alt key simulation to bypass foreground window restrictions
(required for pywebview environment).
'''
import sys
import subprocess
import time
import logging
logger = logging.getLogger(__name__)

def open_folder_foreground(folder_path = None, select_file = None):
    '''
    Open folder in file explorer and bring to foreground.

    On Windows, uses ctypes and Alt key simulation to bypass foreground
    window restrictions that occur in pywebview environments.

    Args:
        folder_path: Path to the folder to open
        select_file: Optional filename to select within the folder

    Returns:
        True if successful, False otherwise
    '''
    
    try:
        if sys.platform == 'win32':
            return _open_folder_foreground_windows(folder_path, select_file)
        if None.platform == 'darwin':
            return _open_folder_macos(folder_path, select_file)
        return None(folder_path)
    except Exception:
        e = None
        logger.error(f'''Failed to open folder: {e}''')
        e = None
        del e
        return False
        e = None
        del e



def _open_folder_foreground_windows(folder_path = None, select_file = None):
    '''
    Open folder in Windows Explorer and bring to foreground.
    Uses multiple techniques to bypass foreground window restrictions.

    Returns True if successful, False otherwise.
    '''
    pass
# WARNING: Decompyle incomplete


def _open_folder_macos(folder_path = None, select_file = None):
    '''Open folder in Finder on macOS.'''
    
    try:
        if select_file:
            file_path = f'''{folder_path}/{select_file}'''
            subprocess.run([
                'open',
                '-R',
                file_path], check = False)
        else:
            subprocess.run([
                'open',
                folder_path], check = False)
        return True
    except Exception:
        e = None
        logger.error(f'''Failed to open folder (macOS): {e}''')
        e = None
        del e
        return False
        e = None
        del e



def _open_folder_linux(folder_path = None):
    '''Open folder in file manager on Linux.'''
    
    try:
        subprocess.run([
            'xdg-open',
            folder_path], check = False)
        return True
    except Exception:
        e = None
        logger.error(f'''Failed to open folder (Linux): {e}''')
        e = None
        del e
        return False
        e = None
        del e
