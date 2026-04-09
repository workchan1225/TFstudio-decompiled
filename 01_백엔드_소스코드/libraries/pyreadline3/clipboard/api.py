# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: api.pyc (Python 3.11)

from pyreadline3.py3k_compat import is_ironpython
if is_ironpython:
    
    try:
        from ironpython_clipboard import get_clipboard_text, set_clipboard_text
    except ImportError:
        from no_clipboard import get_clipboard_text, set_clipboard_text
    except:
        
        try:
            from win32_clipboard import get_clipboard_text, set_clipboard_text
        except ImportError:
            from no_clipboard import get_clipboard_text, set_clipboard_text

        __all__ = [
            'get_clipboard_text',
            'set_clipboard_text']
        return None
