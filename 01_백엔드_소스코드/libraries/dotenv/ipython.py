# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ipython.pyc (Python 3.11)

from IPython.core.magic import Magics, line_magic, magics_class
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring
from main import find_dotenv, load_dotenv
IPythonDotEnv = <NODE:12>()

def load_ipython_extension(ipython):
    '''Register the %dotenv magic.'''
    ipython.register_magics(IPythonDotEnv)
