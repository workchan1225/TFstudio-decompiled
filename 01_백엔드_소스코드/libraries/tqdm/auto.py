# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: auto.pyc (Python 3.11)

'''
Enables multiple commonly used features.

Method resolution order:

- `tqdm.autonotebook` without import warnings
- `tqdm.asyncio`
- `tqdm.std` base class

Usage:
>>> from tqdm.auto import trange, tqdm
>>> for i in trange(10):
...     ...
'''
import warnings
from std import TqdmExperimentalWarning
warnings.catch_warnings()
warnings.simplefilter('ignore', category = TqdmExperimentalWarning)
from autonotebook import tqdm as notebook_tqdm
None(None, None)
