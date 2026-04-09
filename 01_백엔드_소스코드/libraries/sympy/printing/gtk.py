# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: gtk.pyc (Python 3.11)

from sympy.printing.mathml import mathml
from sympy.utilities.mathml import c2p
import tempfile
import subprocess

def print_gtk(x, start_viewer = (True,)):
    '''Print to Gtkmathview, a gtk widget capable of rendering MathML.

    Needs libgtkmathview-bin'''
    file = tempfile.NamedTemporaryFile('w')
    file.write(c2p(mathml(x), simple = True))
    file.flush()
    if start_viewer:
        subprocess.check_call(('mathmlviewer', file.name))
    None(None, None)
    return None
    with None:
        if not None:
            pass
