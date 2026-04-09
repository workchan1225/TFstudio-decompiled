# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cxx.pyc (Python 3.11)

'''
C++ code printer
'''
from itertools import chain
from sympy.codegen.ast import Type, none
from codeprinter import requires
from c import C89CodePrinter, C99CodePrinter
from sympy.printing.codeprinter import cxxcode
reserved = {
    'C++98': [
        'and',
        'and_eq',
        'asm',
        'auto',
        'bitand',
        'bitor',
        'bool',
        'break',
        'case',
        'catch,',
        'char',
        'class',
        'compl',
        'const',
        'const_cast',
        'continue',
        'default',
        'delete',
        'do',
        'double',
        'dynamic_cast',
        'else',
        'enum',
        'explicit',
        'export',
        'extern',
        'false',
        'float',
        'for',
        'friend',
        'goto',
        'if',
        'inline',
        'int',
        'long',
        'mutable',
        'namespace',
        'new',
        'not',
        'not_eq',
        'operator',
        'or',
        'or_eq',
        'private',
        'protected',
        'public',
        'register',
        'reinterpret_cast',
        'return',
        'short',
        'signed',
        'sizeof',
        'static',
        'static_cast',
        'struct',
        'switch',
        'template',
        'this',
        'throw',
        'true',
        'try',
        'typedef',
        'typeid',
        'typename',
        'union',
        'unsigned',
        'using',
        'virtual',
        'void',
        'volatile',
        'wchar_t',
        'while',
        'xor',
        'xor_eq'] }
reserved['C++11'] = reserved['C++98'][:] + [
    'alignas',
    'alignof',
    'char16_t',
    'char32_t',
    'constexpr',
    'decltype',
    'noexcept',
    'nullptr',
    'static_assert',
    'thread_local']
reserved['C++17'] = reserved['C++11'][:]
reserved['C++17'].remove('register')
_math_functions = {
    'C++98': {
        'Mod': 'fmod',
        'ceiling': 'ceil' },
    'C++11': {
        'gamma': 'tgamma' },
    'C++17': {
        'beta': 'beta',
        'Ei': 'expint',
        'zeta': 'riemann_zeta' } }
for k in ('Abs', 'exp', 'log', 'log10', 'sqrt', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'atan2', 'sinh', 'cosh', 'tanh', 'floor'):
    _math_functions['C++98'][k] = k.lower()
    for k in ('asinh', 'acosh', 'atanh', 'erf', 'erfc'):
        _math_functions['C++11'][k] = k.lower()
        
        def _attach_print_method(cls, sympy_name, func_name):
            pass
        # WARNING: Decompyle incomplete

        
        def _attach_print_methods(cls, cont):
            for sympy_name, cxx_name in cont[cls.standard].items():
                _attach_print_method(cls, sympy_name, cxx_name)
                return None

        
        class _CXXCodePrinterBase:
            pass
        # WARNING: Decompyle incomplete

        
        class CXX98CodePrinter(C89CodePrinter, _CXXCodePrinterBase):
            standard = 'C++98'
            reserved_words = set(reserved['C++98'])

        
        class CXX11CodePrinter(C99CodePrinter, _CXXCodePrinterBase):
            pass
        # WARNING: Decompyle incomplete

        
        class CXX17CodePrinter(C99CodePrinter, _CXXCodePrinterBase):
            __module__ = __name__
            __qualname__ = 'CXX17CodePrinter'
            standard = 'C++17'
            reserved_words = set(reserved['C++17'])
        # WARNING: Decompyle incomplete

        cxx_code_printers = {
            'c++98': CXX98CodePrinter,
            'c++11': CXX11CodePrinter,
            'c++17': CXX17CodePrinter }
        return None
