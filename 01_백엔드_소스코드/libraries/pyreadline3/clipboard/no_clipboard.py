# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: no_clipboard.pyc (Python 3.11)

GLOBAL_CLIPBOARD_BUFFER = ''

def get_clipboard_text():
    return GLOBAL_CLIPBOARD_BUFFER


def set_clipboard_text(text = None):
    global GLOBAL_CLIPBOARD_BUFFER
    GLOBAL_CLIPBOARD_BUFFER = text
