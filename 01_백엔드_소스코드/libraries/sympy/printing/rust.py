# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rust.pyc (Python 3.11)

__doc__ = '\nRust code printer\n\nThe `RustCodePrinter` converts SymPy expressions into Rust expressions.\n\nA complete code generator, which uses `rust_code` extensively, can be found\nin `sympy.utilities.codegen`. The `codegen` module can be used to generate\ncomplete source code files.\n\n'
from __future__ import annotations
from typing import Any
from sympy.core import S, Rational, Float, Lambda
from sympy.core.numbers import equal_valued
from sympy.printing.codeprinter import CodePrinter
# WARNING: Decompyle incomplete
