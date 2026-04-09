# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ironpython_clipboard.pyc (Python 3.11)

import clr


Clipboard
clr.AddReferenceByPartialName('System.Windows.Forms')
(lambda : text = ''if cb.ContainsText():
text = cb.GetText()text) = None

def set_clipboard_text(text = None):
    cb.SetText(text)

if __name__ == '__main__':
    txt = get_clipboard_text()
    print(txt)
    return None
