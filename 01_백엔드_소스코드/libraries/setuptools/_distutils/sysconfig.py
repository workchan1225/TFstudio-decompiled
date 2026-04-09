# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: setuptools\_distutils\sysconfig.py

"""Provide access to Python's configuration information.  The specific
configuration variables available depend heavily on the platform and
configuration.  The values may be retrieved using
get_config_var(name), and the list of variables is available via
get_config_vars().keys().  Additional convenience functions are also
available.

Written by:   Fred L. Drake, Jr.
Email:        <fdrake@acm.org>
"""

import os
import re
import sys
import sysconfig
import pathlib
from errors import DistutilsPlatformError
from  import py39compat
from _functools import pass_none

def _is_python_source_dir(d):
    """
    Return True if the target directory appears to point to an
    un-installed Python.
    """
    # 0 MAKE_CELL                1 (modules)
    # 44           2 RESUME                   0
    # 49           4 LOAD_GLOBAL              1 (NULL + pathlib)
    # 16 LOAD_ATTR                1 (Path)
    # 26 LOAD_FAST                0 (d)
    # 28 PRECALL                  1
    # 32 CALL                     1
    # 42 LOAD_METHOD              2 (joinpath)
    # 64 LOAD_CONST               1 ('Modules')
    # 66 PRECALL                  1
    # 70 CALL                     1
    # 80 STORE_DEREF              1 (modules)
    # 50          82 LOAD_GLOBAL              7 (NULL + any)
    # 94 LOAD_CLOSURE             1 (modules)
    # 96 BUILD_TUPLE              1
    # 98 LOAD_CONST               2 (<code object <genexpr> at 0x000001EBD7E48930, file "setuptools\_distutils\sysconfig.py", line 50>)
    # 100 MAKE_FUNCTION            8 (closure)
    # 102 LOAD_CONST               3 (('Setup', 'Setup.local'))
    # 104 GET_ITER
    # 106 PRECALL                  0
    # 110 CALL                     0
    # 120 PRECALL                  1
    # 124 CALL                     1
    # 134 RETURN_VALUE
    # Disassembly of <code object <genexpr> at 0x000001EBD7E48930, file "setuptools\_distutils\sysconfig.py", line 50>:
    # 0 COPY_FREE_VARS           1
    # 50           2 RETURN_GENERATOR
    # 4 POP_TOP
    # 6 RESUME                   0
    # 8 LOAD_FAST                0 (.0)
    # >>   10 FOR_ITER                43 (to 98)
    # 12 STORE_FAST               1 (fn)
    # 14 LOAD_DEREF               2 (modules)
    # 16 LOAD_METHOD              0 (joinpath)
    # 38 LOAD_FAST                1 (fn)
    # 40 PRECALL                  1
    # 44 CALL                     1
    # 54 LOAD_METHOD              1 (is_file)
    # 76 PRECALL                  0
    # 80 CALL                     0
    # 90 YIELD_VALUE
    # 92 RESUME                   1
    # 94 POP_TOP
    # 96 JUMP_BACKWARD           44 (to 10)
    # >>   98 LOAD_CONST               0 (None)
    # 100 RETURN_VALUE

def _is_parent(dir_a, dir_b):
    """
    Return True if a is a parent of b.
    """
    # 56           0 RESUME                   0
    # 60           2 LOAD_GLOBAL              0 (os)
    # 14 LOAD_ATTR                1 (path)
    # 24 LOAD_METHOD              2 (normcase)
    # 46 LOAD_FAST                0 (dir_a)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 LOAD_METHOD              3 (startswith)
    # 84 LOAD_GLOBAL              0 (os)
    # 96 LOAD_ATTR                1 (path)
    # 106 LOAD_METHOD              2 (normcase)
    # 128 LOAD_FAST                1 (dir_b)
    # 130 PRECALL                  1
    # 134 CALL                     1
    # 144 PRECALL                  1
    # 148 CALL                     1
    # 158 RETURN_VALUE

def _fix_pcbuild(d):
    # 0 MAKE_CELL                0 (d)
    # 65           2 RESUME                   0
    # 68           4 LOAD_GLOBAL              0 (PREFIX)
    # 16 LOAD_GLOBAL              2 (BASE_PREFIX)
    # 28 BUILD_TUPLE              2
    # 30 STORE_FAST               1 (prefixes)
    # 69          32 LOAD_CLOSURE             0 (d)
    # 34 BUILD_TUPLE              1
    # 36 LOAD_CONST               1 (<code object <genexpr> at 0x000001EBD7E30880, file "setuptools\_distutils\sysconfig.py", line 69>)
    # 38 MAKE_FUNCTION            8 (closure)
    # 71          40 LOAD_FAST                1 (prefixes)
    # 69          42 GET_ITER
    # 44 PRECALL                  0
    # 48 CALL                     0
    # 58 STORE_FAST               2 (matched)
    # 74          60 LOAD_GLOBAL              5 (NULL + next)
    # 72 LOAD_FAST                2 (matched)
    # 74 LOAD_DEREF               0 (d)
    # 76 PRECALL                  2
    # 80 CALL                     2
    # 90 RETURN_VALUE
    # Disassembly of <code object <genexpr> at 0x000001EBD7E30880, file "setuptools\_distutils\sysconfig.py", line 69>:
    # 0 COPY_FREE_VARS           1
    # 69           2 RETURN_GENERATOR
    # 4 POP_TOP
    # 6 RESUME                   0
    # 8 LOAD_FAST                0 (.0)
    # >>   10 FOR_ITER                52 (to 116)
    # 71          12 STORE_FAST               1 (prefix)
    # 72          14 LOAD_GLOBAL              1 (NULL + _is_parent)
    # 26 LOAD_DEREF               2 (d)
    # 28 LOAD_GLOBAL              2 (os)
    # 40 LOAD_ATTR                2 (path)
    # 50 LOAD_METHOD              3 (join)
    # 72 LOAD_FAST                1 (prefix)
    # 74 LOAD_CONST               0 ('PCbuild')
    # 76 PRECALL                  2
    # 80 CALL                     2
    # 90 PRECALL                  2
    # 94 CALL                     2
    # 69         104 POP_JUMP_BACKWARD_IF_FALSE    48 (to 10)
    # 70         106 LOAD_FAST                1 (prefix)
    # 69         108 YIELD_VALUE
    # 110 RESUME                   1
    # 112 POP_TOP
    # 114 JUMP_BACKWARD           53 (to 10)
    # >>  116 LOAD_CONST               1 (None)
    # 118 RETURN_VALUE

def _python_build():
    # 80           0 RESUME                   0
    # 81           2 LOAD_GLOBAL              0 (_sys_home)
    # 14 POP_JUMP_FORWARD_IF_FALSE    20 (to 56)
    # 82          16 LOAD_GLOBAL              3 (NULL + _is_python_source_dir)
    # 28 LOAD_GLOBAL              0 (_sys_home)
    # 40 PRECALL                  1
    # 44 CALL                     1
    # 54 RETURN_VALUE
    # 83     >>   56 LOAD_GLOBAL              3 (NULL + _is_python_source_dir)
    # 68 LOAD_GLOBAL              4 (project_base)
    # 80 PRECALL                  1
    # 84 CALL                     1
    # 94 RETURN_VALUE

def get_python_version():
    """Return a string containing the major and minor Python version,
    leaving off the patchlevel.  Sample return values could be '1.5'
    or '2.2'.
    """
    # 102           0 RESUME                   0
    # 107           2 LOAD_CONST               1 ('%d.%d')
    # 4 LOAD_GLOBAL              0 (sys)
    # 16 LOAD_ATTR                1 (version_info)
    # 26 LOAD_CONST               2 (None)
    # 28 LOAD_CONST               3 (2)
    # 30 BUILD_SLICE              2
    # 32 BINARY_SUBSCR
    # 42 BINARY_OP                6 (%)
    # 46 RETURN_VALUE

def get_python_inc(plat_specific, prefix):
    """Return the directory containing installed Python header files.

    If 'plat_specific' is false (the default), this is the path to the
    non-platform-specific header files, i.e. Python.h and so on;
    otherwise, this is the path to platform-specific header files
    (namely pyconfig.h).

    If 'prefix' is supplied, use it instead of sys.base_prefix or
    sys.base_exec_prefix -- i.e., ignore 'plat_specific'.
    """
    # 110           0 RESUME                   0
    # 121           2 LOAD_FAST                0 (plat_specific)
    # 4 POP_JUMP_FORWARD_IF_FALSE     7 (to 20)
    # 6 LOAD_GLOBAL              0 (BASE_EXEC_PREFIX)
    # 18 JUMP_FORWARD             6 (to 32)
    # >>   20 LOAD_GLOBAL              2 (BASE_PREFIX)
    # >>   32 STORE_FAST               2 (default_prefix)
    # 122          34 LOAD_FAST                1 (prefix)
    # 36 POP_JUMP_FORWARD_IF_NONE     2 (to 42)
    # 38 LOAD_FAST                1 (prefix)
    # 40 JUMP_FORWARD             1 (to 44)
    # >>   42 LOAD_FAST                2 (default_prefix)
    # >>   44 STORE_FAST               3 (resolved_prefix)
    # 123          46 NOP
    # 124          48 LOAD_GLOBAL              5 (NULL + globals)
    # 60 PRECALL                  0
    # 64 CALL                     0
    # 74 LOAD_CONST               2 ('_get_python_inc_')
    # 76 LOAD_GLOBAL              6 (os)
    # 88 LOAD_ATTR                4 (name)
    # 98 FORMAT_VALUE             0
    # 100 BUILD_STRING             2
    # 102 BINARY_SUBSCR
    # 112 STORE_FAST               4 (getter)
    # 114 JUMP_FORWARD            42 (to 200)
    # >>  116 PUSH_EXC_INFO
    # 125         118 LOAD_GLOBAL             10 (KeyError)
    # 130 CHECK_EXC_MATCH
    # 132 POP_JUMP_FORWARD_IF_FALSE    29 (to 192)
    # 134 POP_TOP
    # 126         136 LOAD_GLOBAL             13 (NULL + DistutilsPlatformError)
    # 127         148 LOAD_CONST               3 ("I don't know where Python installs its C header files on platform '%s'")
    # 128         150 LOAD_GLOBAL              6 (os)
    # 162 LOAD_ATTR                4 (name)
    # 127         172 BINARY_OP                6 (%)
    # 126         176 PRECALL                  1
    # 180 CALL                     1
    # 190 RAISE_VARARGS            1
    # 125     >>  192 RERAISE                  0
    # >>  194 COPY                     3
    # 196 POP_EXCEPT
    # 198 RERAISE                  1
    # 130     >>  200 PUSH_NULL
    # 202 LOAD_FAST                4 (getter)
    # 204 LOAD_FAST                3 (resolved_prefix)
    # 206 LOAD_FAST                1 (prefix)
    # 208 LOAD_FAST                0 (plat_specific)
    # 210 PRECALL                  3
    # 214 CALL                     3
    # 224 RETURN_VALUE
    # ExceptionTable:
    # 48 to 112 -> 116 [0]
    # 116 to 192 -> 194 [1] lasti

def _get_python_inc_posix(prefix, spec_prefix, plat_specific):
    # 133           0 RESUME                   0
    # 134           2 LOAD_GLOBAL              0 (IS_PYPY)
    # 14 POP_JUMP_FORWARD_IF_FALSE    48 (to 112)
    # 16 LOAD_GLOBAL              2 (sys)
    # 28 LOAD_ATTR                2 (version_info)
    # 38 LOAD_CONST               1 ((3, 8))
    # 40 COMPARE_OP               0 (<)
    # 46 POP_JUMP_FORWARD_IF_FALSE    32 (to 112)
    # 135          48 LOAD_GLOBAL              6 (os)
    # 60 LOAD_ATTR                4 (path)
    # 70 LOAD_METHOD              5 (join)
    # 92 LOAD_FAST                0 (prefix)
    # 94 LOAD_CONST               2 ('include')
    # 96 PRECALL                  2
    # 100 CALL                     2
    # 110 RETURN_VALUE
    # 137     >>  112 LOAD_GLOBAL             13 (NULL + _get_python_inc_posix_python)
    # 124 LOAD_FAST                2 (plat_specific)
    # 126 PRECALL                  1
    # 130 CALL                     1
    # 140 JUMP_IF_TRUE_OR_POP     30 (to 202)
    # 138         142 LOAD_GLOBAL             15 (NULL + _get_python_inc_from_config)
    # 154 LOAD_FAST                2 (plat_specific)
    # 156 LOAD_FAST                1 (spec_prefix)
    # 158 PRECALL                  2
    # 162 CALL                     2
    # 137         172 JUMP_IF_TRUE_OR_POP     14 (to 202)
    # 139         174 LOAD_GLOBAL             17 (NULL + _get_python_inc_posix_prefix)
    # 186 LOAD_FAST                0 (prefix)
    # 188 PRECALL                  1
    # 192 CALL                     1
    # 136     >>  202 RETURN_VALUE

def _get_python_inc_posix_python(plat_specific):
    """
    Assume the executable is in the build directory. The
    pyconfig.h file should be in the same directory. Since
    the build directory may not be the source directory,
    use "srcdir" from the makefile to find the "Include"
    directory.
    """
    # 143           0 RESUME                   0
    # 151           2 LOAD_GLOBAL              0 (python_build)
    # 14 POP_JUMP_FORWARD_IF_TRUE     2 (to 20)
    # 152          16 LOAD_CONST               1 (None)
    # 18 RETURN_VALUE
    # 153     >>   20 LOAD_FAST                0 (plat_specific)
    # 22 POP_JUMP_FORWARD_IF_FALSE    14 (to 52)
    # 154          24 LOAD_GLOBAL              2 (_sys_home)
    # 36 JUMP_IF_TRUE_OR_POP      6 (to 50)
    # 38 LOAD_GLOBAL              4 (project_base)
    # >>   50 RETURN_VALUE
    # 155     >>   52 LOAD_GLOBAL              6 (os)
    # 64 LOAD_ATTR                4 (path)
    # 74 LOAD_METHOD              5 (join)
    # 96 LOAD_GLOBAL             13 (NULL + get_config_var)
    # 108 LOAD_CONST               2 ('srcdir')
    # 110 PRECALL                  1
    # 114 CALL                     1
    # 124 LOAD_CONST               3 ('Include')
    # 126 PRECALL                  2
    # 130 CALL                     2
    # 140 STORE_FAST               1 (incdir)
    # 156         142 LOAD_GLOBAL              6 (os)
    # 154 LOAD_ATTR                4 (path)
    # 164 LOAD_METHOD              7 (normpath)
    # 186 LOAD_FAST                1 (incdir)
    # 188 PRECALL                  1
    # 192 CALL                     1
    # 202 RETURN_VALUE

def _get_python_inc_from_config(plat_specific, spec_prefix):
    """
    If no prefix was explicitly specified, provide the include
    directory from the config vars. Useful when
    cross-compiling, since the config vars may come from
    the host
    platform Python installation, while the current Python
    executable is from the build platform installation.

    >>> monkeypatch = getfixture('monkeypatch')
    >>> gpifc = _get_python_inc_from_config
    >>> monkeypatch.setitem(gpifc.__globals__, 'get_config_var', str.lower)
    >>> gpifc(False, '/usr/bin/')
    >>> gpifc(False, '')
    >>> gpifc(False, None)
    'includepy'
    >>> gpifc(True, None)
    'confincludepy'
    """
    # 159           0 RESUME                   0
    # 178           2 LOAD_FAST                1 (spec_prefix)
    # 4 POP_JUMP_FORWARD_IF_NOT_NONE    21 (to 48)
    # 179           6 LOAD_GLOBAL              1 (NULL + get_config_var)
    # 18 LOAD_CONST               2 ('CONF')
    # 20 LOAD_FAST                0 (plat_specific)
    # 22 BINARY_OP                5 (*)
    # 26 LOAD_CONST               3 ('INCLUDEPY')
    # 28 BINARY_OP                0 (+)
    # 32 PRECALL                  1
    # 36 CALL                     1
    # 46 RETURN_VALUE
    # 178     >>   48 LOAD_CONST               1 (None)
    # 50 RETURN_VALUE

def _get_python_inc_posix_prefix(prefix):
    # 182           0 RESUME                   0
    # 183           2 LOAD_GLOBAL              0 (IS_PYPY)
    # 14 POP_JUMP_FORWARD_IF_FALSE     2 (to 20)
    # 16 LOAD_CONST               1 ('pypy')
    # 18 JUMP_FORWARD             1 (to 22)
    # >>   20 LOAD_CONST               2 ('python')
    # >>   22 STORE_FAST               1 (implementation)
    # 184          24 LOAD_FAST                1 (implementation)
    # 26 LOAD_GLOBAL              3 (NULL + get_python_version)
    # 38 PRECALL                  0
    # 42 CALL                     0
    # 52 BINARY_OP                0 (+)
    # 56 LOAD_GLOBAL              4 (build_flags)
    # 68 BINARY_OP                0 (+)
    # 72 STORE_FAST               2 (python_dir)
    # 185          74 LOAD_GLOBAL              6 (os)
    # 86 LOAD_ATTR                4 (path)
    # 96 LOAD_METHOD              5 (join)
    # 118 LOAD_FAST                0 (prefix)
    # 120 LOAD_CONST               3 ('include')
    # 122 LOAD_FAST                2 (python_dir)
    # 124 PRECALL                  3
    # 128 CALL                     3
    # 138 RETURN_VALUE

def _get_python_inc_nt(prefix, spec_prefix, plat_specific):
    # 188           0 RESUME                   0
    # 189           2 LOAD_GLOBAL              0 (python_build)
    # 14 POP_JUMP_FORWARD_IF_FALSE    83 (to 182)
    # 193          16 LOAD_GLOBAL              2 (os)
    # 28 LOAD_ATTR                2 (path)
    # 38 LOAD_METHOD              3 (join)
    # 60 LOAD_FAST                0 (prefix)
    # 62 LOAD_CONST               1 ('include')
    # 64 PRECALL                  2
    # 68 CALL                     2
    # 194          78 LOAD_GLOBAL              2 (os)
    # 90 LOAD_ATTR                2 (path)
    # 100 LOAD_ATTR                4 (pathsep)
    # 193         110 BINARY_OP                0 (+)
    # 195         114 LOAD_GLOBAL              2 (os)
    # 126 LOAD_ATTR                2 (path)
    # 136 LOAD_METHOD              3 (join)
    # 158 LOAD_FAST                0 (prefix)
    # 160 LOAD_CONST               2 ('PC')
    # 162 PRECALL                  2
    # 166 CALL                     2
    # 193         176 BINARY_OP                0 (+)
    # 192         180 RETURN_VALUE
    # 197     >>  182 LOAD_GLOBAL              2 (os)
    # 194 LOAD_ATTR                2 (path)
    # 204 LOAD_METHOD              3 (join)
    # 226 LOAD_FAST                0 (prefix)
    # 228 LOAD_CONST               1 ('include')
    # 230 PRECALL                  2
    # 234 CALL                     2
    # 244 RETURN_VALUE

def _posix_lib(standard_lib, libpython, early_prefix, prefix):
    # 201           0 RESUME                   0
    # 202           2 LOAD_FAST                0 (standard_lib)
    # 4 POP_JUMP_FORWARD_IF_FALSE     2 (to 10)
    # 203           6 LOAD_FAST                1 (libpython)
    # 8 RETURN_VALUE
    # 205     >>   10 LOAD_GLOBAL              0 (os)
    # 22 LOAD_ATTR                1 (path)
    # 32 LOAD_METHOD              2 (join)
    # 54 LOAD_FAST                1 (libpython)
    # 56 LOAD_CONST               1 ('site-packages')
    # 58 PRECALL                  2
    # 62 CALL                     2
    # 72 RETURN_VALUE

def get_python_lib(plat_specific, standard_lib, prefix):
    """Return the directory containing the Python library (standard or
    site additions).

    If 'plat_specific' is true, return the directory containing
    platform-specific modules, i.e. any module from a non-pure-Python
    module distribution; otherwise, return the platform-shared library
    directory.  If 'standard_lib' is true, return the directory
    containing standard Python library modules; otherwise, return the
    directory for site-specific modules.

    If 'prefix' is supplied, use it instead of sys.base_prefix or
    sys.base_exec_prefix -- i.e., ignore 'plat_specific'.
    """
    # 208           0 RESUME                   0
    # 223           2 LOAD_GLOBAL              0 (IS_PYPY)
    # 14 POP_JUMP_FORWARD_IF_FALSE   108 (to 232)
    # 16 LOAD_GLOBAL              2 (sys)
    # 28 LOAD_ATTR                2 (version_info)
    # 38 LOAD_CONST               1 ((3, 8))
    # 40 COMPARE_OP               0 (<)
    # 46 POP_JUMP_FORWARD_IF_FALSE    92 (to 232)
    # 225          48 LOAD_FAST                2 (prefix)
    # 50 POP_JUMP_FORWARD_IF_NOT_NONE     7 (to 66)
    # 226          52 LOAD_GLOBAL              6 (PREFIX)
    # 64 STORE_FAST               2 (prefix)
    # 227     >>   66 LOAD_FAST                1 (standard_lib)
    # 68 POP_JUMP_FORWARD_IF_FALSE    49 (to 168)
    # 228          70 LOAD_GLOBAL              8 (os)
    # 82 LOAD_ATTR                5 (path)
    # 92 LOAD_METHOD              6 (join)
    # 114 LOAD_FAST                2 (prefix)
    # 116 LOAD_CONST               3 ('lib-python')
    # 118 LOAD_GLOBAL              2 (sys)
    # 130 LOAD_ATTR                7 (version)
    # 140 LOAD_CONST               4 (0)
    # 142 BINARY_SUBSCR
    # 152 PRECALL                  3
    # 156 CALL                     3
    # 166 RETURN_VALUE
    # 229     >>  168 LOAD_GLOBAL              8 (os)
    # 180 LOAD_ATTR                5 (path)
    # 190 LOAD_METHOD              6 (join)
    # 212 LOAD_FAST                2 (prefix)
    # 214 LOAD_CONST               5 ('site-packages')
    # 216 PRECALL                  2
    # 220 CALL                     2
    # 230 RETURN_VALUE
    # 231     >>  232 LOAD_FAST                2 (prefix)
    # 234 STORE_FAST               3 (early_prefix)
    # 233         236 LOAD_FAST                2 (prefix)
    # 238 POP_JUMP_FORWARD_IF_NOT_NONE    35 (to 310)
    # 234         240 LOAD_FAST                1 (standard_lib)
    # 242 POP_JUMP_FORWARD_IF_FALSE    17 (to 278)
    # 235         244 LOAD_FAST                0 (plat_specific)
    # 246 POP_JUMP_FORWARD_IF_FALSE     7 (to 262)
    # 248 LOAD_GLOBAL             16 (BASE_EXEC_PREFIX)
    # 260 JUMP_IF_TRUE_OR_POP      6 (to 274)
    # >>  262 LOAD_GLOBAL             18 (BASE_PREFIX)
    # >>  274 STORE_FAST               2 (prefix)
    # 276 JUMP_FORWARD            16 (to 310)
    # 237     >>  278 LOAD_FAST                0 (plat_specific)
    # 280 POP_JUMP_FORWARD_IF_FALSE     7 (to 296)
    # 282 LOAD_GLOBAL             20 (EXEC_PREFIX)
    # 294 JUMP_IF_TRUE_OR_POP      6 (to 308)
    # >>  296 LOAD_GLOBAL              6 (PREFIX)
    # >>  308 STORE_FAST               2 (prefix)
    # 239     >>  310 LOAD_GLOBAL              8 (os)
    # 322 LOAD_ATTR               11 (name)
    # 332 LOAD_CONST               6 ('posix')
    # 334 COMPARE_OP               2 (==)
    # 340 POP_JUMP_FORWARD_IF_FALSE   106 (to 554)
    # 240         342 LOAD_FAST                0 (plat_specific)
    # 344 POP_JUMP_FORWARD_IF_TRUE     2 (to 350)
    # 346 LOAD_FAST                1 (standard_lib)
    # 348 POP_JUMP_FORWARD_IF_FALSE    23 (to 396)
    # 243     >>  350 LOAD_GLOBAL             25 (NULL + getattr)
    # 362 LOAD_GLOBAL              2 (sys)
    # 374 LOAD_CONST               7 ('platlibdir')
    # 376 LOAD_CONST               8 ('lib')
    # 378 PRECALL                  3
    # 382 CALL                     3
    # 392 STORE_FAST               4 (libdir)
    # 394 JUMP_FORWARD             2 (to 400)
    # 246     >>  396 LOAD_CONST               8 ('lib')
    # 398 STORE_FAST               4 (libdir)
    # 247     >>  400 LOAD_GLOBAL              0 (IS_PYPY)
    # 412 POP_JUMP_FORWARD_IF_FALSE     2 (to 418)
    # 414 LOAD_CONST               9 ('pypy')
    # 416 JUMP_FORWARD             1 (to 420)
    # >>  418 LOAD_CONST              10 ('python')
    # >>  420 STORE_FAST               5 (implementation)
    # 248         422 LOAD_GLOBAL              8 (os)
    # 434 LOAD_ATTR                5 (path)
    # 444 LOAD_METHOD              6 (join)
    # 466 LOAD_FAST                2 (prefix)
    # 468 LOAD_FAST                4 (libdir)
    # 470 LOAD_FAST                5 (implementation)
    # 472 LOAD_GLOBAL             27 (NULL + get_python_version)
    # 484 PRECALL                  0
    # 488 CALL                     0
    # 498 BINARY_OP                0 (+)
    # 502 PRECALL                  3
    # 506 CALL                     3
    # 516 STORE_FAST               6 (libpython)
    # 249         518 LOAD_GLOBAL             29 (NULL + _posix_lib)
    # 530 LOAD_FAST                1 (standard_lib)
    # 532 LOAD_FAST                6 (libpython)
    # 534 LOAD_FAST                3 (early_prefix)
    # 536 LOAD_FAST                2 (prefix)
    # 538 PRECALL                  4
    # 542 CALL                     4
    # 552 RETURN_VALUE
    # 250     >>  554 LOAD_GLOBAL              8 (os)
    # 566 LOAD_ATTR               11 (name)
    # 576 LOAD_CONST              11 ('nt')
    # 578 COMPARE_OP               2 (==)
    # 584 POP_JUMP_FORWARD_IF_FALSE    67 (to 720)
    # 251         586 LOAD_FAST                1 (standard_lib)
    # 588 POP_JUMP_FORWARD_IF_FALSE    32 (to 654)
    # 252         590 LOAD_GLOBAL              8 (os)
    # 602 LOAD_ATTR                5 (path)
    # 612 LOAD_METHOD              6 (join)
    # 634 LOAD_FAST                2 (prefix)
    # 636 LOAD_CONST              12 ('Lib')
    # 638 PRECALL                  2
    # 642 CALL                     2
    # 652 RETURN_VALUE
    # 254     >>  654 LOAD_GLOBAL              8 (os)
    # 666 LOAD_ATTR                5 (path)
    # 676 LOAD_METHOD              6 (join)
    # 698 LOAD_FAST                2 (prefix)
    # 700 LOAD_CONST              12 ('Lib')
    # 702 LOAD_CONST               5 ('site-packages')
    # 704 PRECALL                  3
    # 708 CALL                     3
    # 718 RETURN_VALUE
    # 256     >>  720 LOAD_GLOBAL             31 (NULL + DistutilsPlatformError)
    # 257         732 LOAD_CONST              13 ("I don't know where Python installs its library on platform '%s'")
    # 258         734 LOAD_GLOBAL              8 (os)
    # 746 LOAD_ATTR               11 (name)
    # 257         756 BINARY_OP                6 (%)
    # 256         760 PRECALL                  1
    # 764 CALL                     1
    # 774 RAISE_VARARGS            1

def customize_compiler(compiler):
    """Do any platform-specific customization of a CCompiler instance.

    Mainly needed on Unix, so we can plug in the information that
    varies across Unices and is stored in Python's Makefile.
    """
    # 262           0 RESUME                   0
    # 268           2 LOAD_FAST                0 (compiler)
    # 4 LOAD_ATTR                0 (compiler_type)
    # 14 LOAD_CONST               1 ('unix')
    # 16 COMPARE_OP               2 (==)
    # 22 EXTENDED_ARG             2
    # 24 POP_JUMP_FORWARD_IF_FALSE   694 (to 1414)
    # 269          26 LOAD_GLOBAL              2 (sys)
    # 38 LOAD_ATTR                2 (platform)
    # 48 LOAD_CONST               2 ('darwin')
    # 50 COMPARE_OP               2 (==)
    # 56 POP_JUMP_FORWARD_IF_FALSE    55 (to 168)
    # 280          58 LOAD_GLOBAL              7 (NULL + get_config_var)
    # 70 LOAD_CONST               3 ('CUSTOMIZED_OSX_COMPILER')
    # 72 PRECALL                  1
    # 76 CALL                     1
    # 86 POP_JUMP_FORWARD_IF_TRUE    40 (to 168)
    # 281          88 LOAD_CONST               4 (0)
    # 90 LOAD_CONST               5 (None)
    # 92 IMPORT_NAME              4 (_osx_support)
    # 94 STORE_FAST               1 (_osx_support)
    # 283          96 LOAD_FAST                1 (_osx_support)
    # 98 LOAD_METHOD              5 (customize_compiler)
    # 120 LOAD_GLOBAL             12 (_config_vars)
    # 132 PRECALL                  1
    # 136 CALL                     1
    # 146 POP_TOP
    # 284         148 LOAD_CONST               6 ('True')
    # 150 LOAD_GLOBAL             12 (_config_vars)
    # 162 LOAD_CONST               3 ('CUSTOMIZED_OSX_COMPILER')
    # 164 STORE_SUBSCR
    # 295     >>  168 LOAD_GLOBAL             15 (NULL + get_config_vars)
    # 296         180 LOAD_CONST               7 ('CC')
    # 297         182 LOAD_CONST               8 ('CXX')
    # 298         184 LOAD_CONST               9 ('CFLAGS')
    # 299         186 LOAD_CONST              10 ('CCSHARED')
    # 300         188 LOAD_CONST              11 ('LDSHARED')
    # 301         190 LOAD_CONST              12 ('SHLIB_SUFFIX')
    # 302         192 LOAD_CONST              13 ('AR')
    # 303         194 LOAD_CONST              14 ('ARFLAGS')
    # 295         196 PRECALL                  8
    # 200 CALL                     8
    # 286         210 UNPACK_SEQUENCE          8
    # 287         214 STORE_FAST               2 (cc)
    # 288         216 STORE_FAST               3 (cxx)
    # 289         218 STORE_FAST               4 (cflags)
    # 290         220 STORE_FAST               5 (ccshared)
    # 291         222 STORE_FAST               6 (ldshared)
    # 292         224 STORE_FAST               7 (shlib_suffix)
    # 293         226 STORE_FAST               8 (ar)
    # 294         228 STORE_FAST               9 (ar_flags)
    # 306         230 LOAD_CONST               7 ('CC')
    # 232 LOAD_GLOBAL             16 (os)
    # 244 LOAD_ATTR                9 (environ)
    # 254 CONTAINS_OP              0
    # 256 POP_JUMP_FORWARD_IF_FALSE    81 (to 420)
    # 307         258 LOAD_GLOBAL             16 (os)
    # 270 LOAD_ATTR                9 (environ)
    # 280 LOAD_CONST               7 ('CC')
    # 282 BINARY_SUBSCR
    # 292 STORE_FAST              10 (newcc)
    # 308         294 LOAD_CONST              11 ('LDSHARED')
    # 296 LOAD_GLOBAL             16 (os)
    # 308 LOAD_ATTR                9 (environ)
    # 318 CONTAINS_OP              1
    # 320 POP_JUMP_FORWARD_IF_FALSE    47 (to 416)
    # 322 LOAD_FAST                6 (ldshared)
    # 324 LOAD_METHOD             10 (startswith)
    # 346 LOAD_FAST                2 (cc)
    # 348 PRECALL                  1
    # 352 CALL                     1
    # 362 POP_JUMP_FORWARD_IF_FALSE    26 (to 416)
    # 311         364 LOAD_FAST               10 (newcc)
    # 366 LOAD_FAST                6 (ldshared)
    # 368 LOAD_GLOBAL             23 (NULL + len)
    # 380 LOAD_FAST                2 (cc)
    # 382 PRECALL                  1
    # 386 CALL                     1
    # 396 LOAD_CONST               5 (None)
    # 398 BUILD_SLICE              2
    # 400 BINARY_SUBSCR
    # 410 BINARY_OP                0 (+)
    # 414 STORE_FAST               6 (ldshared)
    # 312     >>  416 LOAD_FAST               10 (newcc)
    # 418 STORE_FAST               2 (cc)
    # 313     >>  420 LOAD_CONST               8 ('CXX')
    # 422 LOAD_GLOBAL             16 (os)
    # 434 LOAD_ATTR                9 (environ)
    # 444 CONTAINS_OP              0
    # 446 POP_JUMP_FORWARD_IF_FALSE    18 (to 484)
    # 314         448 LOAD_GLOBAL             16 (os)
    # 460 LOAD_ATTR                9 (environ)
    # 470 LOAD_CONST               8 ('CXX')
    # 472 BINARY_SUBSCR
    # 482 STORE_FAST               3 (cxx)
    # 315     >>  484 LOAD_CONST              11 ('LDSHARED')
    # 486 LOAD_GLOBAL             16 (os)
    # 498 LOAD_ATTR                9 (environ)
    # 508 CONTAINS_OP              0
    # 510 POP_JUMP_FORWARD_IF_FALSE    18 (to 548)
    # 316         512 LOAD_GLOBAL             16 (os)
    # 524 LOAD_ATTR                9 (environ)
    # 534 LOAD_CONST              11 ('LDSHARED')
    # 536 BINARY_SUBSCR
    # 546 STORE_FAST               6 (ldshared)
    # 317     >>  548 LOAD_CONST              15 ('CPP')
    # 550 LOAD_GLOBAL             16 (os)
    # 562 LOAD_ATTR                9 (environ)
    # 572 CONTAINS_OP              0
    # 574 POP_JUMP_FORWARD_IF_FALSE    19 (to 614)
    # 318         576 LOAD_GLOBAL             16 (os)
    # 588 LOAD_ATTR                9 (environ)
    # 598 LOAD_CONST              15 ('CPP')
    # 600 BINARY_SUBSCR
    # 610 STORE_FAST              11 (cpp)
    # 612 JUMP_FORWARD             5 (to 624)
    # 320     >>  614 LOAD_FAST                2 (cc)
    # 616 LOAD_CONST              16 (' -E')
    # 618 BINARY_OP                0 (+)
    # 622 STORE_FAST              11 (cpp)
    # 321     >>  624 LOAD_CONST              17 ('LDFLAGS')
    # 626 LOAD_GLOBAL             16 (os)
    # 638 LOAD_ATTR                9 (environ)
    # 648 CONTAINS_OP              0
    # 650 POP_JUMP_FORWARD_IF_FALSE    24 (to 700)
    # 322         652 LOAD_FAST                6 (ldshared)
    # 654 LOAD_CONST              18 (' ')
    # 656 BINARY_OP                0 (+)
    # 660 LOAD_GLOBAL             16 (os)
    # 672 LOAD_ATTR                9 (environ)
    # 682 LOAD_CONST              17 ('LDFLAGS')
    # 684 BINARY_SUBSCR
    # 694 BINARY_OP                0 (+)
    # 698 STORE_FAST               6 (ldshared)
    # 323     >>  700 LOAD_CONST               9 ('CFLAGS')
    # 702 LOAD_GLOBAL             16 (os)
    # 714 LOAD_ATTR                9 (environ)
    # 724 CONTAINS_OP              0
    # 726 POP_JUMP_FORWARD_IF_FALSE    48 (to 824)
    # 324         728 LOAD_FAST                4 (cflags)
    # 730 LOAD_CONST              18 (' ')
    # 732 BINARY_OP                0 (+)
    # 736 LOAD_GLOBAL             16 (os)
    # 748 LOAD_ATTR                9 (environ)
    # 758 LOAD_CONST               9 ('CFLAGS')
    # 760 BINARY_SUBSCR
    # 770 BINARY_OP                0 (+)
    # 774 STORE_FAST               4 (cflags)
    # 325         776 LOAD_FAST                6 (ldshared)
    # 778 LOAD_CONST              18 (' ')
    # 780 BINARY_OP                0 (+)
    # 784 LOAD_GLOBAL             16 (os)
    # 796 LOAD_ATTR                9 (environ)
    # 806 LOAD_CONST               9 ('CFLAGS')
    # 808 BINARY_SUBSCR
    # 818 BINARY_OP                0 (+)
    # 822 STORE_FAST               6 (ldshared)
    # 326     >>  824 LOAD_CONST              19 ('CPPFLAGS')
    # 826 LOAD_GLOBAL             16 (os)
    # 838 LOAD_ATTR                9 (environ)
    # 848 CONTAINS_OP              0
    # 850 POP_JUMP_FORWARD_IF_FALSE    72 (to 996)
    # 327         852 LOAD_FAST               11 (cpp)
    # 854 LOAD_CONST              18 (' ')
    # 856 BINARY_OP                0 (+)
    # 860 LOAD_GLOBAL             16 (os)
    # 872 LOAD_ATTR                9 (environ)
    # 882 LOAD_CONST              19 ('CPPFLAGS')
    # 884 BINARY_SUBSCR
    # 894 BINARY_OP                0 (+)
    # 898 STORE_FAST              11 (cpp)
    # 328         900 LOAD_FAST                4 (cflags)
    # 902 LOAD_CONST              18 (' ')
    # 904 BINARY_OP                0 (+)
    # 908 LOAD_GLOBAL             16 (os)
    # 920 LOAD_ATTR                9 (environ)
    # 930 LOAD_CONST              19 ('CPPFLAGS')
    # 932 BINARY_SUBSCR
    # 942 BINARY_OP                0 (+)
    # 946 STORE_FAST               4 (cflags)
    # 329         948 LOAD_FAST                6 (ldshared)
    # 950 LOAD_CONST              18 (' ')
    # 952 BINARY_OP                0 (+)
    # 956 LOAD_GLOBAL             16 (os)
    # 968 LOAD_ATTR                9 (environ)
    # 978 LOAD_CONST              19 ('CPPFLAGS')
    # 980 BINARY_SUBSCR
    # 990 BINARY_OP                0 (+)
    # 994 STORE_FAST               6 (ldshared)
    # 330     >>  996 LOAD_CONST              13 ('AR')
    # 998 LOAD_GLOBAL             16 (os)
    # 1010 LOAD_ATTR                9 (environ)
    # 1020 CONTAINS_OP              0
    # 1022 POP_JUMP_FORWARD_IF_FALSE    18 (to 1060)
    # 331        1024 LOAD_GLOBAL             16 (os)
    # 1036 LOAD_ATTR                9 (environ)
    # 1046 LOAD_CONST              13 ('AR')
    # 1048 BINARY_SUBSCR
    # 1058 STORE_FAST               8 (ar)
    # 332     >> 1060 LOAD_CONST              14 ('ARFLAGS')
    # 1062 LOAD_GLOBAL             16 (os)
    # 1074 LOAD_ATTR                9 (environ)
    # 1084 CONTAINS_OP              0
    # 1086 POP_JUMP_FORWARD_IF_FALSE    25 (to 1138)
    # 333        1088 LOAD_FAST                8 (ar)
    # 1090 LOAD_CONST              18 (' ')
    # 1092 BINARY_OP                0 (+)
    # 1096 LOAD_GLOBAL             16 (os)
    # 1108 LOAD_ATTR                9 (environ)
    # 1118 LOAD_CONST              14 ('ARFLAGS')
    # 1120 BINARY_SUBSCR
    # 1130 BINARY_OP                0 (+)
    # 1134 STORE_FAST              12 (archiver)
    # 1136 JUMP_FORWARD             8 (to 1154)
    # 335     >> 1138 LOAD_FAST                8 (ar)
    # 1140 LOAD_CONST              18 (' ')
    # 1142 BINARY_OP                0 (+)
    # 1146 LOAD_FAST                9 (ar_flags)
    # 1148 BINARY_OP                0 (+)
    # 1152 STORE_FAST              12 (archiver)
    # 337     >> 1154 LOAD_FAST                2 (cc)
    # 1156 LOAD_CONST              18 (' ')
    # 1158 BINARY_OP                0 (+)
    # 1162 LOAD_FAST                4 (cflags)
    # 1164 BINARY_OP                0 (+)
    # 1168 STORE_FAST              13 (cc_cmd)
    # 338        1170 LOAD_FAST                0 (compiler)
    # 1172 LOAD_METHOD             12 (set_executables)
    # 339        1194 LOAD_FAST               11 (cpp)
    # 340        1196 LOAD_FAST               13 (cc_cmd)
    # 341        1198 LOAD_FAST               13 (cc_cmd)
    # 1200 LOAD_CONST              18 (' ')
    # 1202 BINARY_OP                0 (+)
    # 1206 LOAD_FAST                5 (ccshared)
    # 1208 BINARY_OP                0 (+)
    # 342        1212 LOAD_FAST                3 (cxx)
    # 343        1214 LOAD_FAST                6 (ldshared)
    # 344        1216 LOAD_FAST                2 (cc)
    # 345        1218 LOAD_FAST               12 (archiver)
    # 338        1220 KW_NAMES                20
    # 1222 PRECALL                  7
    # 1226 CALL                     7
    # 1236 POP_TOP
    # 348        1238 LOAD_CONST              21 ('RANLIB')
    # 1240 LOAD_GLOBAL             16 (os)
    # 1252 LOAD_ATTR                9 (environ)
    # 1262 CONTAINS_OP              0
    # 1264 POP_JUMP_FORWARD_IF_FALSE    65 (to 1396)
    # 1266 LOAD_FAST                0 (compiler)
    # 1268 LOAD_ATTR               13 (executables)
    # 1278 LOAD_METHOD             14 (get)
    # 1300 LOAD_CONST              22 ('ranlib')
    # 1302 LOAD_CONST               5 (None)
    # 1304 PRECALL                  2
    # 1308 CALL                     2
    # 1318 POP_JUMP_FORWARD_IF_FALSE    38 (to 1396)
    # 349        1320 LOAD_FAST                0 (compiler)
    # 1322 LOAD_METHOD             12 (set_executables)
    # 1344 LOAD_GLOBAL             16 (os)
    # 1356 LOAD_ATTR                9 (environ)
    # 1366 LOAD_CONST              21 ('RANLIB')
    # 1368 BINARY_SUBSCR
    # 1378 KW_NAMES                23
    # 1380 PRECALL                  1
    # 1384 CALL                     1
    # 1394 POP_TOP
    # 351     >> 1396 LOAD_FAST                7 (shlib_suffix)
    # 1398 LOAD_FAST                0 (compiler)
    # 1400 STORE_ATTR              15 (shared_lib_extension)
    # 1410 LOAD_CONST               5 (None)
    # 1412 RETURN_VALUE
    # 268     >> 1414 LOAD_CONST               5 (None)
    # 1416 RETURN_VALUE

def get_config_h_filename():
    """Return full pathname of installed pyconfig.h file."""
    # 354           0 RESUME                   0
    # 356           2 LOAD_GLOBAL              0 (python_build)
    # 14 POP_JUMP_FORWARD_IF_FALSE   107 (to 230)
    # 357          16 LOAD_GLOBAL              2 (os)
    # 28 LOAD_ATTR                2 (name)
    # 38 LOAD_CONST               1 ('nt')
    # 40 COMPARE_OP               2 (==)
    # 46 POP_JUMP_FORWARD_IF_FALSE    45 (to 138)
    # 358          48 LOAD_GLOBAL              2 (os)
    # 60 LOAD_ATTR                3 (path)
    # 70 LOAD_METHOD              4 (join)
    # 92 LOAD_GLOBAL             10 (_sys_home)
    # 104 JUMP_IF_TRUE_OR_POP      6 (to 118)
    # 106 LOAD_GLOBAL             12 (project_base)
    # >>  118 LOAD_CONST               2 ('PC')
    # 120 PRECALL                  2
    # 124 CALL                     2
    # 134 STORE_FAST               0 (inc_dir)
    # 136 JUMP_FORWARD            14 (to 166)
    # 360     >>  138 LOAD_GLOBAL             10 (_sys_home)
    # 150 JUMP_IF_TRUE_OR_POP      6 (to 164)
    # 152 LOAD_GLOBAL             12 (project_base)
    # >>  164 STORE_FAST               0 (inc_dir)
    # 361     >>  166 LOAD_GLOBAL              2 (os)
    # 178 LOAD_ATTR                3 (path)
    # 188 LOAD_METHOD              4 (join)
    # 210 LOAD_FAST                0 (inc_dir)
    # 212 LOAD_CONST               3 ('pyconfig.h')
    # 214 PRECALL                  2
    # 218 CALL                     2
    # 228 RETURN_VALUE
    # 363     >>  230 LOAD_GLOBAL             15 (NULL + sysconfig)
    # 242 LOAD_ATTR                8 (get_config_h_filename)
    # 252 PRECALL                  0
    # 256 CALL                     0
    # 266 RETURN_VALUE

def get_makefile_filename():
    """Return full pathname of installed Makefile from the Python build."""
    # 366           0 RESUME                   0
    # 368           2 LOAD_GLOBAL              1 (NULL + sysconfig)
    # 14 LOAD_ATTR                1 (get_makefile_filename)
    # 24 PRECALL                  0
    # 28 CALL                     0
    # 38 RETURN_VALUE

def parse_config_h(fp, g):
    """Parse a config.h-style file.

    A dictionary containing name/value pairs is returned.  If an
    optional dictionary is passed in as the second argument, it is
    used instead of a new dictionary.
    """
    # 371           0 RESUME                   0
    # 378           2 LOAD_GLOBAL              1 (NULL + sysconfig)
    # 14 LOAD_ATTR                1 (parse_config_h)
    # 24 LOAD_FAST                0 (fp)
    # 26 LOAD_FAST                1 (g)
    # 28 KW_NAMES                 1
    # 30 PRECALL                  2
    # 34 CALL                     2
    # 44 RETURN_VALUE

def parse_makefile(fn, g):
    """Parse a Makefile-style file.

    A dictionary containing name/value pairs is returned.  If an
    optional dictionary is passed in as the second argument, it is
    used instead of a new dictionary.
    """
    # 388           0 RESUME                   0
    # 395           2 LOAD_CONST               1 (0)
    # 4 LOAD_CONST               2 (('TextFile',))
    # 6 IMPORT_NAME              0 (distutils.text_file)
    # 8 IMPORT_FROM              1 (TextFile)
    # 10 STORE_FAST               2 (TextFile)
    # 12 POP_TOP
    # 397          14 PUSH_NULL
    # 16 LOAD_FAST                2 (TextFile)
    # 398          18 LOAD_FAST                0 (fn)
    # 20 LOAD_CONST               3 (1)
    # 22 LOAD_CONST               3 (1)
    # 24 LOAD_CONST               3 (1)
    # 26 LOAD_CONST               4 ('surrogateescape')
    # 397          28 KW_NAMES                 5
    # 30 PRECALL                  5
    # 34 CALL                     5
    # 44 STORE_FAST               3 (fp)
    # 401          46 LOAD_FAST                1 (g)
    # 48 POP_JUMP_FORWARD_IF_NOT_NONE     2 (to 54)
    # 402          50 BUILD_MAP                0
    # 52 STORE_FAST               1 (g)
    # 403     >>   54 BUILD_MAP                0
    # 56 STORE_FAST               4 (done)
    # 404          58 BUILD_MAP                0
    # 60 STORE_FAST               5 (notdone)
    # 406          62 NOP
    # 407     >>   64 LOAD_FAST                3 (fp)
    # 66 LOAD_METHOD              2 (readline)
    # 88 PRECALL                  0
    # 92 CALL                     0
    # 102 STORE_FAST               6 (line)
    # 408         104 LOAD_FAST                6 (line)
    # 106 POP_JUMP_FORWARD_IF_NOT_NONE     1 (to 110)
    # 409         108 JUMP_FORWARD           169 (to 448)
    # 410     >>  110 LOAD_GLOBAL              6 (_variable_rx)
    # 122 LOAD_METHOD              4 (match)
    # 144 LOAD_FAST                6 (line)
    # 146 PRECALL                  1
    # 150 CALL                     1
    # 160 STORE_FAST               7 (m)
    # 411         162 LOAD_FAST                7 (m)
    # 164 POP_JUMP_FORWARD_IF_FALSE   140 (to 446)
    # 412         166 LOAD_FAST                7 (m)
    # 168 LOAD_METHOD              5 (group)
    # 190 LOAD_CONST               3 (1)
    # 192 LOAD_CONST               8 (2)
    # 194 PRECALL                  2
    # 198 CALL                     2
    # 208 UNPACK_SEQUENCE          2
    # 212 STORE_FAST               8 (n)
    # 214 STORE_FAST               9 (v)
    # 413         216 LOAD_FAST                9 (v)
    # 218 LOAD_METHOD              6 (strip)
    # 240 PRECALL                  0
    # 244 CALL                     0
    # 254 STORE_FAST               9 (v)
    # 415         256 LOAD_FAST                9 (v)
    # 258 LOAD_METHOD              7 (replace)
    # 280 LOAD_CONST               9 ('$$')
    # 282 LOAD_CONST              10 ('')
    # 284 PRECALL                  2
    # 288 CALL                     2
    # 298 STORE_FAST              10 (tmpv)
    # 417         300 LOAD_CONST              11 ('$')
    # 302 LOAD_FAST               10 (tmpv)
    # 304 CONTAINS_OP              0
    # 306 POP_JUMP_FORWARD_IF_FALSE     6 (to 320)
    # 418         308 LOAD_FAST                9 (v)
    # 310 LOAD_FAST                5 (notdone)
    # 312 LOAD_FAST                8 (n)
    # 314 STORE_SUBSCR
    # 318 JUMP_FORWARD            63 (to 446)
    # 420     >>  320 NOP
    # 421         322 LOAD_GLOBAL             17 (NULL + int)
    # 334 LOAD_FAST                9 (v)
    # 336 PRECALL                  1
    # 340 CALL                     1
    # 350 STORE_FAST               9 (v)
    # 426         352 LOAD_FAST                9 (v)
    # 354 LOAD_FAST                4 (done)
    # 356 LOAD_FAST                8 (n)
    # 358 STORE_SUBSCR
    # 362 JUMP_FORWARD            41 (to 446)
    # >>  364 PUSH_EXC_INFO
    # 422         366 LOAD_GLOBAL             18 (ValueError)
    # 378 CHECK_EXC_MATCH
    # 380 POP_JUMP_FORWARD_IF_FALSE    28 (to 438)
    # 382 POP_TOP
    # 424         384 LOAD_FAST                9 (v)
    # 386 LOAD_METHOD              7 (replace)
    # 408 LOAD_CONST               9 ('$$')
    # 410 LOAD_CONST              11 ('$')
    # 412 PRECALL                  2
    # 416 CALL                     2
    # 426 LOAD_FAST                4 (done)
    # 428 LOAD_FAST                8 (n)
    # 430 STORE_SUBSCR
    # 434 POP_EXCEPT
    # 436 JUMP_FORWARD             4 (to 446)
    # 422     >>  438 RERAISE                  0
    # >>  440 COPY                     3
    # 442 POP_EXCEPT
    # 444 RERAISE                  1
    # 406     >>  446 JUMP_BACKWARD          192 (to 64)
    # 432     >>  448 LOAD_CONST              12 (('CFLAGS', 'LDFLAGS', 'CPPFLAGS'))
    # 450 STORE_FAST              11 (renamed_variables)
    # 435         452 LOAD_FAST                5 (notdone)
    # 454 EXTENDED_ARG             1
    # 456 POP_JUMP_FORWARD_IF_FALSE   453 (to 1364)
    # 436     >>  458 LOAD_GLOBAL             21 (NULL + list)
    # 470 LOAD_FAST                5 (notdone)
    # 472 PRECALL                  1
    # 476 CALL                     1
    # 486 GET_ITER
    # >>  488 EXTENDED_ARG             1
    # 490 FOR_ITER               433 (to 1358)
    # 492 STORE_FAST              12 (name)
    # 437         494 LOAD_FAST                5 (notdone)
    # 496 LOAD_FAST               12 (name)
    # 498 BINARY_SUBSCR
    # 508 STORE_FAST              13 (value)
    # 438         510 LOAD_GLOBAL             22 (_findvar1_rx)
    # 522 LOAD_METHOD             12 (search)
    # 544 LOAD_FAST               13 (value)
    # 546 PRECALL                  1
    # 550 CALL                     1
    # 560 JUMP_IF_TRUE_OR_POP     25 (to 612)
    # 562 LOAD_GLOBAL             26 (_findvar2_rx)
    # 574 LOAD_METHOD             12 (search)
    # 596 LOAD_FAST               13 (value)
    # 598 PRECALL                  1
    # 602 CALL                     1
    # >>  612 STORE_FAST               7 (m)
    # 439         614 LOAD_FAST                7 (m)
    # 616 EXTENDED_ARG             1
    # 618 POP_JUMP_FORWARD_IF_FALSE   364 (to 1348)
    # 440         620 LOAD_FAST                7 (m)
    # 622 LOAD_METHOD              5 (group)
    # 644 LOAD_CONST               3 (1)
    # 646 PRECALL                  1
    # 650 CALL                     1
    # 660 STORE_FAST               8 (n)
    # 441         662 LOAD_CONST               7 (True)
    # 664 STORE_FAST              14 (found)
    # 442         666 LOAD_FAST                8 (n)
    # 668 LOAD_FAST                4 (done)
    # 670 CONTAINS_OP              0
    # 672 POP_JUMP_FORWARD_IF_FALSE    22 (to 718)
    # 443         674 LOAD_GLOBAL             29 (NULL + str)
    # 686 LOAD_FAST                4 (done)
    # 688 LOAD_FAST                8 (n)
    # 690 BINARY_SUBSCR
    # 700 PRECALL                  1
    # 704 CALL                     1
    # 714 STORE_FAST              15 (item)
    # 716 JUMP_FORWARD           122 (to 962)
    # 444     >>  718 LOAD_FAST                8 (n)
    # 720 LOAD_FAST                5 (notdone)
    # 722 CONTAINS_OP              0
    # 724 POP_JUMP_FORWARD_IF_FALSE     3 (to 732)
    # 446         726 LOAD_CONST              13 (False)
    # 728 STORE_FAST              14 (found)
    # 730 JUMP_FORWARD           115 (to 962)
    # 447     >>  732 LOAD_FAST                8 (n)
    # 734 LOAD_GLOBAL             30 (os)
    # 746 LOAD_ATTR               16 (environ)
    # 756 CONTAINS_OP              0
    # 758 POP_JUMP_FORWARD_IF_FALSE    19 (to 798)
    # 449         760 LOAD_GLOBAL             30 (os)
    # 772 LOAD_ATTR               16 (environ)
    # 782 LOAD_FAST                8 (n)
    # 784 BINARY_SUBSCR
    # 794 STORE_FAST              15 (item)
    # 796 JUMP_FORWARD            82 (to 962)
    # 451     >>  798 LOAD_FAST                8 (n)
    # 800 LOAD_FAST               11 (renamed_variables)
    # 802 CONTAINS_OP              0
    # 804 POP_JUMP_FORWARD_IF_FALSE    71 (to 948)
    # 452         806 LOAD_FAST               12 (name)
    # 808 LOAD_METHOD             17 (startswith)
    # 830 LOAD_CONST              14 ('PY_')
    # 832 PRECALL                  1
    # 836 CALL                     1
    # 846 POP_JUMP_FORWARD_IF_FALSE    15 (to 878)
    # 848 LOAD_FAST               12 (name)
    # 850 LOAD_CONST              15 (3)
    # 852 LOAD_CONST               6 (None)
    # 854 BUILD_SLICE              2
    # 856 BINARY_SUBSCR
    # 866 LOAD_FAST               11 (renamed_variables)
    # 868 CONTAINS_OP              0
    # 870 POP_JUMP_FORWARD_IF_FALSE     3 (to 878)
    # 453         872 LOAD_CONST              10 ('')
    # 874 STORE_FAST              15 (item)
    # 876 JUMP_FORWARD            42 (to 962)
    # 455     >>  878 LOAD_CONST              14 ('PY_')
    # 880 LOAD_FAST                8 (n)
    # 882 BINARY_OP                0 (+)
    # 886 LOAD_FAST                5 (notdone)
    # 888 CONTAINS_OP              0
    # 890 POP_JUMP_FORWARD_IF_FALSE     3 (to 898)
    # 456         892 LOAD_CONST              13 (False)
    # 894 STORE_FAST              14 (found)
    # 896 JUMP_FORWARD            32 (to 962)
    # 459     >>  898 LOAD_GLOBAL             29 (NULL + str)
    # 910 LOAD_FAST                4 (done)
    # 912 LOAD_CONST              14 ('PY_')
    # 914 LOAD_FAST                8 (n)
    # 916 BINARY_OP                0 (+)
    # 920 BINARY_SUBSCR
    # 930 PRECALL                  1
    # 934 CALL                     1
    # 944 STORE_FAST              15 (item)
    # 946 JUMP_FORWARD             7 (to 962)
    # 461     >>  948 LOAD_CONST              10 ('')
    # 950 COPY                     1
    # 952 LOAD_FAST                4 (done)
    # 954 LOAD_FAST                8 (n)
    # 956 STORE_SUBSCR
    # 960 STORE_FAST              15 (item)
    # 462     >>  962 LOAD_FAST               14 (found)
    # 964 POP_JUMP_FORWARD_IF_FALSE   189 (to 1344)
    # 463         966 LOAD_FAST               13 (value)
    # 968 LOAD_FAST                7 (m)
    # 970 LOAD_METHOD             18 (end)
    # 992 PRECALL                  0
    # 996 CALL                     0
    # 1006 LOAD_CONST               6 (None)
    # 1008 BUILD_SLICE              2
    # 1010 BINARY_SUBSCR
    # 1020 STORE_FAST              16 (after)
    # 464        1022 LOAD_FAST               13 (value)
    # 1024 LOAD_CONST               6 (None)
    # 1026 LOAD_FAST                7 (m)
    # 1028 LOAD_METHOD             19 (start)
    # 1050 PRECALL                  0
    # 1054 CALL                     0
    # 1064 BUILD_SLICE              2
    # 1066 BINARY_SUBSCR
    # 1076 LOAD_FAST               15 (item)
    # 1078 BINARY_OP                0 (+)
    # 1082 LOAD_FAST               16 (after)
    # 1084 BINARY_OP                0 (+)
    # 1088 STORE_FAST              13 (value)
    # 465        1090 LOAD_CONST              11 ('$')
    # 1092 LOAD_FAST               16 (after)
    # 1094 CONTAINS_OP              0
    # 1096 POP_JUMP_FORWARD_IF_FALSE     7 (to 1112)
    # 466        1098 LOAD_FAST               13 (value)
    # 1100 LOAD_FAST                5 (notdone)
    # 1102 LOAD_FAST               12 (name)
    # 1104 STORE_SUBSCR
    # 1108 EXTENDED_ARG             1
    # 1110 JUMP_BACKWARD          312 (to 488)
    # 468     >> 1112 NOP
    # 469        1114 LOAD_GLOBAL             17 (NULL + int)
    # 1126 LOAD_FAST               13 (value)
    # 1128 PRECALL                  1
    # 1132 CALL                     1
    # 1142 STORE_FAST              13 (value)
    # 473        1144 LOAD_FAST               13 (value)
    # 1146 LOAD_FAST                4 (done)
    # 1148 LOAD_FAST               12 (name)
    # 1150 STORE_SUBSCR
    # 1154 JUMP_FORWARD            39 (to 1234)
    # >> 1156 PUSH_EXC_INFO
    # 470        1158 LOAD_GLOBAL             18 (ValueError)
    # 1170 CHECK_EXC_MATCH
    # 1172 POP_JUMP_FORWARD_IF_FALSE    26 (to 1226)
    # 1174 POP_TOP
    # 471        1176 LOAD_FAST               13 (value)
    # 1178 LOAD_METHOD              6 (strip)
    # 1200 PRECALL                  0
    # 1204 CALL                     0
    # 1214 LOAD_FAST                4 (done)
    # 1216 LOAD_FAST               12 (name)
    # 1218 STORE_SUBSCR
    # 1222 POP_EXCEPT
    # 1224 JUMP_FORWARD             4 (to 1234)
    # 470     >> 1226 RERAISE                  0
    # >> 1228 COPY                     3
    # 1230 POP_EXCEPT
    # 1232 RERAISE                  1
    # 474     >> 1234 LOAD_FAST                5 (notdone)
    # 1236 LOAD_FAST               12 (name)
    # 1238 DELETE_SUBSCR
    # 476        1240 LOAD_FAST               12 (name)
    # 1242 LOAD_METHOD             17 (startswith)
    # 1264 LOAD_CONST              14 ('PY_')
    # 1266 PRECALL                  1
    # 1270 CALL                     1
    # 1280 POP_JUMP_FORWARD_IF_FALSE    31 (to 1344)
    # 1282 LOAD_FAST               12 (name)
    # 1284 LOAD_CONST              15 (3)
    # 1286 LOAD_CONST               6 (None)
    # 1288 BUILD_SLICE              2
    # 1290 BINARY_SUBSCR
    # 1300 LOAD_FAST               11 (renamed_variables)
    # 1302 CONTAINS_OP              0
    # 1304 POP_JUMP_FORWARD_IF_FALSE    19 (to 1344)
    # 478        1306 LOAD_FAST               12 (name)
    # 1308 LOAD_CONST              15 (3)
    # 1310 LOAD_CONST               6 (None)
    # 1312 BUILD_SLICE              2
    # 1314 BINARY_SUBSCR
    # 1324 STORE_FAST              12 (name)
    # 479        1326 LOAD_FAST               12 (name)
    # 1328 LOAD_FAST                4 (done)
    # 1330 CONTAINS_OP              1
    # 1332 POP_JUMP_FORWARD_IF_FALSE     5 (to 1344)
    # 480        1334 LOAD_FAST               13 (value)
    # 1336 LOAD_FAST                4 (done)
    # 1338 LOAD_FAST               12 (name)
    # 1340 STORE_SUBSCR
    # >> 1344 EXTENDED_ARG             1
    # 1346 JUMP_BACKWARD          430 (to 488)
    # 483     >> 1348 LOAD_FAST                5 (notdone)
    # 1350 LOAD_FAST               12 (name)
    # 1352 DELETE_SUBSCR
    # 1354 EXTENDED_ARG             1
    # 1356 JUMP_BACKWARD          435 (to 488)
    # 435     >> 1358 LOAD_FAST                5 (notdone)
    # 1360 EXTENDED_ARG             1
    # 1362 POP_JUMP_BACKWARD_IF_TRUE   453 (to 458)
    # 485     >> 1364 LOAD_FAST                3 (fp)
    # 1366 LOAD_METHOD             20 (close)
    # 1388 PRECALL                  0
    # 1392 CALL                     0
    # 1402 POP_TOP
    # 488        1404 LOAD_FAST                4 (done)
    # 1406 LOAD_METHOD             21 (items)
    # 1428 PRECALL                  0
    # 1432 CALL                     0
    # 1442 GET_ITER
    # >> 1444 FOR_ITER                49 (to 1544)
    # 1446 UNPACK_SEQUENCE          2
    # 1450 STORE_FAST              17 (k)
    # 1452 STORE_FAST               9 (v)
    # 489        1454 LOAD_GLOBAL             45 (NULL + isinstance)
    # 1466 LOAD_FAST                9 (v)
    # 1468 LOAD_GLOBAL             28 (str)
    # 1480 PRECALL                  2
    # 1484 CALL                     2
    # 1494 POP_JUMP_FORWARD_IF_FALSE    23 (to 1542)
    # 490        1496 LOAD_FAST                9 (v)
    # 1498 LOAD_METHOD              6 (strip)
    # 1520 PRECALL                  0
    # 1524 CALL                     0
    # 1534 LOAD_FAST                4 (done)
    # 1536 LOAD_FAST               17 (k)
    # 1538 STORE_SUBSCR
    # >> 1542 JUMP_BACKWARD           50 (to 1444)
    # 493     >> 1544 LOAD_FAST                1 (g)
    # 1546 LOAD_METHOD             23 (update)
    # 1568 LOAD_FAST                4 (done)
    # 1570 PRECALL                  1
    # 1574 CALL                     1
    # 1584 POP_TOP
    # 494        1586 LOAD_FAST                1 (g)
    # 1588 RETURN_VALUE
    # ExceptionTable:
    # 322 to 350 -> 364 [0]
    # 364 to 432 -> 440 [1] lasti
    # 438 to 438 -> 440 [1] lasti
    # 1114 to 1142 -> 1156 [1]
    # 1156 to 1220 -> 1228 [2] lasti
    # 1226 to 1226 -> 1228 [2] lasti

def expand_makefile_vars(s, vars):
    """Expand Makefile-style variables -- "${foo}" or "$(foo)" -- in
    'string' according to 'vars' (a dictionary mapping variable names to
    values).  Variables not present in 'vars' are silently expanded to the
    empty string.  The variable values in 'vars' should not contain further
    variable expansions; if 'vars' is the output of 'parse_makefile()',
    you're fine.  Returns a variable-expanded version of 's'.
    """
    # 497           0 RESUME                   0
    # 512           2 NOP
    # 513     >>    4 LOAD_GLOBAL              0 (_findvar1_rx)
    # 16 LOAD_METHOD              1 (search)
    # 38 LOAD_FAST                0 (s)
    # 40 PRECALL                  1
    # 44 CALL                     1
    # 54 JUMP_IF_TRUE_OR_POP     25 (to 106)
    # 56 LOAD_GLOBAL              4 (_findvar2_rx)
    # 68 LOAD_METHOD              1 (search)
    # 90 LOAD_FAST                0 (s)
    # 92 PRECALL                  1
    # 96 CALL                     1
    # >>  106 STORE_FAST               2 (m)
    # 514         108 LOAD_FAST                2 (m)
    # 110 POP_JUMP_FORWARD_IF_FALSE    86 (to 284)
    # 515         112 LOAD_FAST                2 (m)
    # 114 LOAD_METHOD              3 (span)
    # 136 PRECALL                  0
    # 140 CALL                     0
    # 150 UNPACK_SEQUENCE          2
    # 154 STORE_FAST               3 (beg)
    # 156 STORE_FAST               4 (end)
    # 516         158 LOAD_FAST                0 (s)
    # 160 LOAD_CONST               2 (0)
    # 162 LOAD_FAST                3 (beg)
    # 164 BUILD_SLICE              2
    # 166 BINARY_SUBSCR
    # 176 LOAD_FAST                1 (vars)
    # 178 LOAD_METHOD              4 (get)
    # 200 LOAD_FAST                2 (m)
    # 202 LOAD_METHOD              5 (group)
    # 224 LOAD_CONST               3 (1)
    # 226 PRECALL                  1
    # 230 CALL                     1
    # 240 PRECALL                  1
    # 244 CALL                     1
    # 254 BINARY_OP                0 (+)
    # 258 LOAD_FAST                0 (s)
    # 260 LOAD_FAST                4 (end)
    # 262 LOAD_CONST               4 (None)
    # 264 BUILD_SLICE              2
    # 266 BINARY_SUBSCR
    # 276 BINARY_OP                0 (+)
    # 280 STORE_FAST               0 (s)
    # 282 JUMP_FORWARD             1 (to 286)
    # 518     >>  284 JUMP_FORWARD             1 (to 288)
    # 512     >>  286 JUMP_BACKWARD          142 (to 4)
    # 519     >>  288 LOAD_FAST                0 (s)
    # 290 RETURN_VALUE

def get_config_vars():
    """With no arguments, return a dictionary of all configuration
    variables relevant for the current platform.  Generally this includes
    everything needed to build extensions and install both pure modules and
    extensions.  On Unix, this means every variable defined in Python's
    installed Makefile; on Windows it's a much smaller set.

    With arguments, return a list of values that result from looking up
    each argument in the configuration variable dictionary.
    """
    # 525           0 RESUME                   0
    # 536           2 LOAD_GLOBAL              0 (_config_vars)
    # 14 POP_JUMP_FORWARD_IF_NOT_NONE    62 (to 140)
    # 537          16 LOAD_GLOBAL              3 (NULL + sysconfig)
    # 28 LOAD_ATTR                2 (get_config_vars)
    # 38 PRECALL                  0
    # 42 CALL                     0
    # 52 LOAD_METHOD              3 (copy)
    # 74 PRECALL                  0
    # 78 CALL                     0
    # 88 STORE_GLOBAL             0 (_config_vars)
    # 538          90 LOAD_GLOBAL              9 (NULL + py39compat)
    # 102 LOAD_ATTR                5 (add_ext_suffix)
    # 112 LOAD_GLOBAL              0 (_config_vars)
    # 124 PRECALL                  1
    # 128 CALL                     1
    # 138 POP_TOP
    # 540     >>  140 LOAD_FAST                0 (args)
    # 142 POP_JUMP_FORWARD_IF_FALSE    54 (to 252)
    # 541         144 BUILD_LIST               0
    # 146 STORE_FAST               1 (vals)
    # 542         148 LOAD_FAST                0 (args)
    # 150 GET_ITER
    # >>  152 FOR_ITER                47 (to 248)
    # 154 STORE_FAST               2 (name)
    # 543         156 LOAD_FAST                1 (vals)
    # 158 LOAD_METHOD              6 (append)
    # 180 LOAD_GLOBAL              0 (_config_vars)
    # 192 LOAD_METHOD              7 (get)
    # 214 LOAD_FAST                2 (name)
    # 216 PRECALL                  1
    # 220 CALL                     1
    # 230 PRECALL                  1
    # 234 CALL                     1
    # 244 POP_TOP
    # 246 JUMP_BACKWARD           48 (to 152)
    # 544     >>  248 LOAD_FAST                1 (vals)
    # 250 RETURN_VALUE
    # 546     >>  252 LOAD_GLOBAL              0 (_config_vars)
    # 264 RETURN_VALUE

def get_config_var(name):
    """Return the value of a single variable using the dictionary
    returned by 'get_config_vars()'.  Equivalent to
    get_config_vars().get(name)
    """
    # 549           0 RESUME                   0
    # 554           2 LOAD_FAST                0 (name)
    # 4 LOAD_CONST               1 ('SO')
    # 6 COMPARE_OP               2 (==)
    # 12 POP_JUMP_FORWARD_IF_FALSE    32 (to 78)
    # 555          14 LOAD_CONST               2 (0)
    # 16 LOAD_CONST               3 (None)
    # 18 IMPORT_NAME              0 (warnings)
    # 20 STORE_FAST               1 (warnings)
    # 557          22 LOAD_FAST                1 (warnings)
    # 24 LOAD_METHOD              1 (warn)
    # 46 LOAD_CONST               4 ('SO is deprecated, use EXT_SUFFIX')
    # 48 LOAD_GLOBAL              4 (DeprecationWarning)
    # 60 LOAD_CONST               5 (2)
    # 62 PRECALL                  3
    # 66 CALL                     3
    # 76 POP_TOP
    # 558     >>   78 LOAD_GLOBAL              7 (NULL + get_config_vars)
    # 90 PRECALL                  0
    # 94 CALL                     0
    # 104 LOAD_METHOD              4 (get)
    # 126 LOAD_FAST                0 (name)
    # 128 PRECALL                  1
    # 132 CALL                     1
    # 142 RETURN_VALUE
