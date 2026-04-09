# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from torch import *
import torch
for n in dir(torch):
    if n.startswith('_') and n.endswith('_') and 'cuda' in n and 'cpu' in n or 'backward' in n:
        continue
    exec(f'''{n} = torch.{n}''')
    del n
    from _aliases import *
    __import__(__package__ + '.linalg')
    __import__(__package__ + '.fft')
    __array_api_version__ = '2024.12'
    return None
