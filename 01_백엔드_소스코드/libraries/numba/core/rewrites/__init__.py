# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
A subpackage hosting Numba IR rewrite passes.
'''
from registry import register_rewrite, rewrite_registry, Rewrite
from numba.core.rewrites import static_getitem, static_raise, static_binop, ir_print
