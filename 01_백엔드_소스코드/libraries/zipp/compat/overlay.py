# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: overlay.pyc (Python 3.11)

__doc__ = "\nExpose zipp.Path as .zipfile.Path.\n\nIncludes everything else in ``zipfile`` to match future usage. Just\nuse:\n\n>>> from zipp.compat.overlay import zipfile\n\nin place of ``import zipfile``.\n\nRelative imports are supported too.\n\n>>> from zipp.compat.overlay.zipfile import ZipInfo\n\nThe ``zipfile`` object added to ``sys.modules`` needs to be\nhashable (#126).\n\n>>> _ = hash(sys.modules['zipp.compat.overlay.zipfile'])\n"
import importlib
import sys
import types
import zipp

class HashableNamespace(types.SimpleNamespace):
    
    def __hash__(self):
        return hash(tuple(vars(self)))


# WARNING: Decompyle incomplete
