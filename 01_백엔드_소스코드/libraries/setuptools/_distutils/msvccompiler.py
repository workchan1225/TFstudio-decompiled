# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: setuptools\_distutils\msvccompiler.py

"""distutils.msvccompiler

Contains MSVCCompiler, an implementation of the abstract CCompiler class
for the Microsoft Visual Studio.
"""

import sys
import os
import warnings
from distutils.errors import DistutilsExecError
from distutils.ccompiler import CCompiler
from distutils import log
import winreg
import win32api
import win32con
from distutils.msvc9compiler import MSVCCompiler
from distutils.msvc9compiler import MacroExpander

def read_keys(base, key):
    """Return list of registry keys."""
    # 74           0 RESUME                   0
    # 76           2 NOP
    # 77           4 LOAD_GLOBAL              1 (NULL + RegOpenKeyEx)
    # 16 LOAD_FAST                0 (base)
    # 18 LOAD_FAST                1 (key)
    # 20 PRECALL                  2
    # 24 CALL                     2
    # 34 STORE_FAST               2 (handle)
    # 36 JUMP_FORWARD            17 (to 72)
    # >>   38 PUSH_EXC_INFO
    # 78          40 LOAD_GLOBAL              2 (RegError)
    # 52 CHECK_EXC_MATCH
    # 54 POP_JUMP_FORWARD_IF_FALSE     4 (to 64)
    # 56 POP_TOP
    # 79          58 POP_EXCEPT
    # 60 LOAD_CONST               1 (None)
    # 62 RETURN_VALUE
    # 78     >>   64 RERAISE                  0
    # >>   66 COPY                     3
    # 68 POP_EXCEPT
    # 70 RERAISE                  1
    # 80     >>   72 BUILD_LIST               0
    # 74 STORE_FAST               3 (L)
    # 81          76 LOAD_CONST               2 (0)
    # 78 STORE_FAST               4 (i)
    # 82          80 NOP
    # 83     >>   82 NOP
    # 84          84 LOAD_GLOBAL              5 (NULL + RegEnumKey)
    # 96 LOAD_FAST                2 (handle)
    # 98 LOAD_FAST                4 (i)
    # 100 PRECALL                  2
    # 104 CALL                     2
    # 114 STORE_FAST               5 (k)
    # 116 JUMP_FORWARD            16 (to 150)
    # >>  118 PUSH_EXC_INFO
    # 85         120 LOAD_GLOBAL              2 (RegError)
    # 132 CHECK_EXC_MATCH
    # 134 POP_JUMP_FORWARD_IF_FALSE     3 (to 142)
    # 136 POP_TOP
    # 86         138 POP_EXCEPT
    # 140 JUMP_FORWARD            31 (to 204)
    # 85     >>  142 RERAISE                  0
    # >>  144 COPY                     3
    # 146 POP_EXCEPT
    # 148 RERAISE                  1
    # 87     >>  150 LOAD_FAST                3 (L)
    # 152 LOAD_METHOD              3 (append)
    # 174 LOAD_FAST                5 (k)
    # 176 PRECALL                  1
    # 180 CALL                     1
    # 190 POP_TOP
    # 88         192 LOAD_FAST                4 (i)
    # 194 LOAD_CONST               4 (1)
    # 196 BINARY_OP               13 (+=)
    # 200 STORE_FAST               4 (i)
    # 82         202 JUMP_BACKWARD           61 (to 82)
    # 89     >>  204 LOAD_FAST                3 (L)
    # 206 RETURN_VALUE
    # ExceptionTable:
    # 4 to 34 -> 38 [0]
    # 38 to 56 -> 66 [1] lasti
    # 64 to 64 -> 66 [1] lasti
    # 84 to 114 -> 118 [0]
    # 118 to 136 -> 144 [1] lasti
    # 142 to 142 -> 144 [1] lasti

def read_values(base, key):
    """Return dict of registry keys and values.

    All names are converted to lowercase.
    """
    # 92           0 RESUME                   0
    # 97           2 NOP
    # 98           4 LOAD_GLOBAL              1 (NULL + RegOpenKeyEx)
    # 16 LOAD_FAST                0 (base)
    # 18 LOAD_FAST                1 (key)
    # 20 PRECALL                  2
    # 24 CALL                     2
    # 34 STORE_FAST               2 (handle)
    # 36 JUMP_FORWARD            17 (to 72)
    # >>   38 PUSH_EXC_INFO
    # 99          40 LOAD_GLOBAL              2 (RegError)
    # 52 CHECK_EXC_MATCH
    # 54 POP_JUMP_FORWARD_IF_FALSE     4 (to 64)
    # 56 POP_TOP
    # 100          58 POP_EXCEPT
    # 60 LOAD_CONST               1 (None)
    # 62 RETURN_VALUE
    # 99     >>   64 RERAISE                  0
    # >>   66 COPY                     3
    # 68 POP_EXCEPT
    # 70 RERAISE                  1
    # 101     >>   72 BUILD_MAP                0
    # 74 STORE_FAST               3 (d)
    # 102          76 LOAD_CONST               2 (0)
    # 78 STORE_FAST               4 (i)
    # 103          80 NOP
    # 104     >>   82 NOP
    # 105          84 LOAD_GLOBAL              5 (NULL + RegEnumValue)
    # 96 LOAD_FAST                2 (handle)
    # 98 LOAD_FAST                4 (i)
    # 100 PRECALL                  2
    # 104 CALL                     2
    # 114 UNPACK_SEQUENCE          3
    # 118 STORE_FAST               5 (name)
    # 120 STORE_FAST               6 (value)
    # 122 STORE_FAST               7 (type)
    # 124 JUMP_FORWARD            16 (to 158)
    # >>  126 PUSH_EXC_INFO
    # 106         128 LOAD_GLOBAL              2 (RegError)
    # 140 CHECK_EXC_MATCH
    # 142 POP_JUMP_FORWARD_IF_FALSE     3 (to 150)
    # 144 POP_TOP
    # 107         146 POP_EXCEPT
    # 148 JUMP_FORWARD            61 (to 272)
    # 106     >>  150 RERAISE                  0
    # >>  152 COPY                     3
    # 154 POP_EXCEPT
    # 156 RERAISE                  1
    # 108     >>  158 LOAD_FAST                5 (name)
    # 160 LOAD_METHOD              3 (lower)
    # 182 PRECALL                  0
    # 186 CALL                     0
    # 196 STORE_FAST               5 (name)
    # 109         198 LOAD_GLOBAL              9 (NULL + convert_mbcs)
    # 210 LOAD_FAST                6 (value)
    # 212 PRECALL                  1
    # 216 CALL                     1
    # 226 LOAD_FAST                3 (d)
    # 228 LOAD_GLOBAL              9 (NULL + convert_mbcs)
    # 240 LOAD_FAST                5 (name)
    # 242 PRECALL                  1
    # 246 CALL                     1
    # 256 STORE_SUBSCR
    # 110         260 LOAD_FAST                4 (i)
    # 262 LOAD_CONST               4 (1)
    # 264 BINARY_OP               13 (+=)
    # 268 STORE_FAST               4 (i)
    # 103         270 JUMP_BACKWARD           95 (to 82)
    # 111     >>  272 LOAD_FAST                3 (d)
    # 274 RETURN_VALUE
    # ExceptionTable:
    # 4 to 34 -> 38 [0]
    # 38 to 56 -> 66 [1] lasti
    # 64 to 64 -> 66 [1] lasti
    # 84 to 122 -> 126 [0]
    # 126 to 144 -> 152 [1] lasti
    # 150 to 150 -> 152 [1] lasti

def convert_mbcs(s):
    # 114           0 RESUME                   0
    # 115           2 LOAD_GLOBAL              1 (NULL + getattr)
    # 14 LOAD_FAST                0 (s)
    # 16 LOAD_CONST               1 ('decode')
    # 18 LOAD_CONST               0 (None)
    # 20 PRECALL                  3
    # 24 CALL                     3
    # 34 STORE_FAST               1 (dec)
    # 116          36 LOAD_FAST                1 (dec)
    # 38 POP_JUMP_FORWARD_IF_NONE    29 (to 98)
    # 117          40 NOP
    # 118          42 PUSH_NULL
    # 44 LOAD_FAST                1 (dec)
    # 46 LOAD_CONST               2 ('mbcs')
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               0 (s)
    # 64 JUMP_FORWARD            16 (to 98)
    # >>   66 PUSH_EXC_INFO
    # 119          68 LOAD_GLOBAL              2 (UnicodeError)
    # 80 CHECK_EXC_MATCH
    # 82 POP_JUMP_FORWARD_IF_FALSE     3 (to 90)
    # 84 POP_TOP
    # 120          86 POP_EXCEPT
    # 88 JUMP_FORWARD             4 (to 98)
    # 119     >>   90 RERAISE                  0
    # >>   92 COPY                     3
    # 94 POP_EXCEPT
    # 96 RERAISE                  1
    # 121     >>   98 LOAD_FAST                0 (s)
    # 100 RETURN_VALUE
    # ExceptionTable:
    # 42 to 62 -> 66 [0]
    # 66 to 84 -> 92 [1] lasti
    # 90 to 90 -> 92 [1] lasti

class MacroExpander:
    """MacroExpander"""
    def __init__(self, version):
        # 125           0 RESUME                   0
        # 126           2 BUILD_MAP                0
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (macros)
        # 127          16 LOAD_FAST                0 (self)
        # 18 LOAD_METHOD              1 (load_macros)
        # 40 LOAD_FAST                1 (version)
        # 42 PRECALL                  1
        # 46 CALL                     1
        # 56 POP_TOP
        # 58 LOAD_CONST               0 (None)
        # 60 RETURN_VALUE

    def set_macro(self, macro, path, key):
        # 129           0 RESUME                   0
        # 130           2 LOAD_GLOBAL              0 (HKEYS)
        # 14 GET_ITER
        # >>   16 FOR_ITER                42 (to 102)
        # 18 STORE_FAST               4 (base)
        # 131          20 LOAD_GLOBAL              3 (NULL + read_values)
        # 32 LOAD_FAST                4 (base)
        # 34 LOAD_FAST                2 (path)
        # 36 PRECALL                  2
        # 40 CALL                     2
        # 50 STORE_FAST               5 (d)
        # 132          52 LOAD_FAST                5 (d)
        # 54 POP_JUMP_FORWARD_IF_FALSE    22 (to 100)
        # 133          56 LOAD_FAST                5 (d)
        # 58 LOAD_FAST                3 (key)
        # 60 BINARY_SUBSCR
        # 70 LOAD_FAST                0 (self)
        # 72 LOAD_ATTR                2 (macros)
        # 82 LOAD_CONST               1 ('$(%s)')
        # 84 LOAD_FAST                1 (macro)
        # 86 BINARY_OP                6 (%)
        # 90 STORE_SUBSCR
        # 134          94 POP_TOP
        # 96 LOAD_CONST               0 (None)
        # 98 RETURN_VALUE
        # 132     >>  100 JUMP_BACKWARD           43 (to 16)
        # 130     >>  102 LOAD_CONST               0 (None)
        # 104 RETURN_VALUE

    def load_macros(self, version):
        # 136           0 RESUME                   0
        # 137           2 LOAD_CONST               1 ('Software\\Microsoft\\VisualStudio\\%0.1f')
        # 4 LOAD_FAST                1 (version)
        # 6 BINARY_OP                6 (%)
        # 10 STORE_FAST               2 (vsbase)
        # 138          12 LOAD_FAST                0 (self)
        # 14 LOAD_METHOD              0 (set_macro)
        # 36 LOAD_CONST               2 ('VCInstallDir')
        # 38 LOAD_FAST                2 (vsbase)
        # 40 LOAD_CONST               3 ('\\Setup\\VC')
        # 42 BINARY_OP                0 (+)
        # 46 LOAD_CONST               4 ('productdir')
        # 48 PRECALL                  3
        # 52 CALL                     3
        # 62 POP_TOP
        # 139          64 LOAD_FAST                0 (self)
        # 66 LOAD_METHOD              0 (set_macro)
        # 88 LOAD_CONST               5 ('VSInstallDir')
        # 90 LOAD_FAST                2 (vsbase)
        # 92 LOAD_CONST               6 ('\\Setup\\VS')
        # 94 BINARY_OP                0 (+)
        # 98 LOAD_CONST               4 ('productdir')
        # 100 PRECALL                  3
        # 104 CALL                     3
        # 114 POP_TOP
        # 140         116 LOAD_CONST               7 ('Software\\Microsoft\\.NETFramework')
        # 118 STORE_FAST               3 (net)
        # 141         120 LOAD_FAST                0 (self)
        # 122 LOAD_METHOD              0 (set_macro)
        # 144 LOAD_CONST               8 ('FrameworkDir')
        # 146 LOAD_FAST                3 (net)
        # 148 LOAD_CONST               9 ('installroot')
        # 150 PRECALL                  3
        # 154 CALL                     3
        # 164 POP_TOP
        # 142         166 NOP
        # 143         168 LOAD_FAST                1 (version)
        # 170 LOAD_CONST              10 (7.0)
        # 172 COMPARE_OP               4 (>)
        # 178 POP_JUMP_FORWARD_IF_FALSE    24 (to 228)
        # 144         180 LOAD_FAST                0 (self)
        # 182 LOAD_METHOD              0 (set_macro)
        # 204 LOAD_CONST              11 ('FrameworkSDKDir')
        # 206 LOAD_FAST                3 (net)
        # 208 LOAD_CONST              12 ('sdkinstallrootv1.1')
        # 210 PRECALL                  3
        # 214 CALL                     3
        # 224 POP_TOP
        # 226 JUMP_FORWARD            23 (to 274)
        # 146     >>  228 LOAD_FAST                0 (self)
        # 230 LOAD_METHOD              0 (set_macro)
        # 252 LOAD_CONST              11 ('FrameworkSDKDir')
        # 254 LOAD_FAST                3 (net)
        # 256 LOAD_CONST              13 ('sdkinstallroot')
        # 258 PRECALL                  3
        # 262 CALL                     3
        # 272 POP_TOP
        # >>  274 JUMP_FORWARD            29 (to 334)
        # >>  276 PUSH_EXC_INFO
        # 147         278 LOAD_GLOBAL              2 (KeyError)
        # 290 CHECK_EXC_MATCH
        # 292 POP_JUMP_FORWARD_IF_FALSE    16 (to 326)
        # 294 POP_TOP
        # 148         296 LOAD_GLOBAL              5 (NULL + DistutilsPlatformError)
        # 149         308 LOAD_CONST              14 ('Python was built with Visual Studio 2003;\nextensions must be built with a compiler than can generate compatible binaries.\nVisual Studio 2003 was not found on this system. If you have Cygwin installed,\nyou can try compiling with MingW32, by passing "-c mingw32" to setup.py.')
        # 148         310 PRECALL                  1
        # 314 CALL                     1
        # 324 RAISE_VARARGS            1
        # 147     >>  326 RERAISE                  0
        # >>  328 COPY                     3
        # 330 POP_EXCEPT
        # 332 RERAISE                  1
        # 155     >>  334 LOAD_CONST              15 ('Software\\Microsoft\\NET Framework Setup\\Product')
        # 336 STORE_FAST               4 (p)
        # 156         338 LOAD_GLOBAL              6 (HKEYS)
        # 350 GET_ITER
        # >>  352 FOR_ITER               104 (to 562)
        # 354 STORE_FAST               5 (base)
        # 157         356 NOP
        # 158         358 LOAD_GLOBAL              9 (NULL + RegOpenKeyEx)
        # 370 LOAD_FAST                5 (base)
        # 372 LOAD_FAST                4 (p)
        # 374 PRECALL                  2
        # 378 CALL                     2
        # 388 STORE_FAST               6 (h)
        # 390 JUMP_FORWARD            16 (to 424)
        # >>  392 PUSH_EXC_INFO
        # 159         394 LOAD_GLOBAL             10 (RegError)
        # 406 CHECK_EXC_MATCH
        # 408 POP_JUMP_FORWARD_IF_FALSE     3 (to 416)
        # 410 POP_TOP
        # 160         412 POP_EXCEPT
        # 414 JUMP_BACKWARD           32 (to 352)
        # 159     >>  416 RERAISE                  0
        # >>  418 COPY                     3
        # 420 POP_EXCEPT
        # 422 RERAISE                  1
        # 161     >>  424 LOAD_GLOBAL             13 (NULL + RegEnumKey)
        # 436 LOAD_FAST                6 (h)
        # 438 LOAD_CONST              16 (0)
        # 440 PRECALL                  2
        # 444 CALL                     2
        # 454 STORE_FAST               7 (key)
        # 162         456 LOAD_GLOBAL             15 (NULL + read_values)
        # 468 LOAD_FAST                5 (base)
        # 470 LOAD_CONST              17 ('{}\\{}')
        # 472 LOAD_METHOD              8 (format)
        # 494 LOAD_FAST                4 (p)
        # 496 LOAD_FAST                7 (key)
        # 498 PRECALL                  2
        # 502 CALL                     2
        # 512 PRECALL                  2
        # 516 CALL                     2
        # 526 STORE_FAST               8 (d)
        # 163         528 LOAD_FAST                8 (d)
        # 530 LOAD_CONST              18 ('version')
        # 532 BINARY_SUBSCR
        # 542 LOAD_FAST                0 (self)
        # 544 LOAD_ATTR                9 (macros)
        # 554 LOAD_CONST              19 ('$(FrameworkVersion)')
        # 556 STORE_SUBSCR
        # 560 JUMP_BACKWARD          105 (to 352)
        # 156     >>  562 LOAD_CONST               0 (None)
        # 564 RETURN_VALUE
        # ExceptionTable:
        # 168 to 272 -> 276 [0]
        # 276 to 326 -> 328 [1] lasti
        # 358 to 388 -> 392 [1]
        # 392 to 410 -> 418 [2] lasti
        # 416 to 416 -> 418 [2] lasti

    def sub(self, s):
        # 165           0 RESUME                   0
        # 166           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (macros)
        # 14 LOAD_METHOD              1 (items)
        # 36 PRECALL                  0
        # 40 CALL                     0
        # 50 GET_ITER
        # >>   52 FOR_ITER                27 (to 108)
        # 54 UNPACK_SEQUENCE          2
        # 58 STORE_FAST               2 (k)
        # 60 STORE_FAST               3 (v)
        # 167          62 LOAD_FAST                1 (s)
        # 64 LOAD_METHOD              2 (replace)
        # 86 LOAD_FAST                2 (k)
        # 88 LOAD_FAST                3 (v)
        # 90 PRECALL                  2
        # 94 CALL                     2
        # 104 STORE_FAST               1 (s)
        # 106 JUMP_BACKWARD           28 (to 52)
        # 168     >>  108 LOAD_FAST                1 (s)
        # 110 RETURN_VALUE


def get_build_version():
    """Return the version of MSVC that was used to build Python.

    For Python 2.3 and up, the version number is included in
    sys.version.  For earlier versions, assume the compiler is MSVC 6.
    """
    # 171           0 RESUME                   0
    # 177           2 LOAD_CONST               1 ('MSC v.')
    # 4 STORE_FAST               0 (prefix)
    # 178           6 LOAD_GLOBAL              0 (sys)
    # 18 LOAD_ATTR                1 (version)
    # 28 LOAD_METHOD              2 (find)
    # 50 LOAD_FAST                0 (prefix)
    # 52 PRECALL                  1
    # 56 CALL                     1
    # 66 STORE_FAST               1 (i)
    # 179          68 LOAD_FAST                1 (i)
    # 70 LOAD_CONST               2 (-1)
    # 72 COMPARE_OP               2 (==)
    # 78 POP_JUMP_FORWARD_IF_FALSE     2 (to 84)
    # 180          80 LOAD_CONST               3 (6)
    # 82 RETURN_VALUE
    # 181     >>   84 LOAD_FAST                1 (i)
    # 86 LOAD_GLOBAL              7 (NULL + len)
    # 98 LOAD_FAST                0 (prefix)
    # 100 PRECALL                  1
    # 104 CALL                     1
    # 114 BINARY_OP                0 (+)
    # 118 STORE_FAST               1 (i)
    # 182         120 LOAD_GLOBAL              0 (sys)
    # 132 LOAD_ATTR                1 (version)
    # 142 LOAD_FAST                1 (i)
    # 144 LOAD_CONST               4 (None)
    # 146 BUILD_SLICE              2
    # 148 BINARY_SUBSCR
    # 158 LOAD_METHOD              4 (split)
    # 180 LOAD_CONST               5 (' ')
    # 182 LOAD_CONST               6 (1)
    # 184 PRECALL                  2
    # 188 CALL                     2
    # 198 UNPACK_SEQUENCE          2
    # 202 STORE_FAST               2 (s)
    # 204 STORE_FAST               3 (rest)
    # 183         206 LOAD_GLOBAL             11 (NULL + int)
    # 218 LOAD_FAST                2 (s)
    # 220 LOAD_CONST               4 (None)
    # 222 LOAD_CONST               7 (-2)
    # 224 BUILD_SLICE              2
    # 226 BINARY_SUBSCR
    # 236 PRECALL                  1
    # 240 CALL                     1
    # 250 LOAD_CONST               3 (6)
    # 252 BINARY_OP               10 (-)
    # 256 STORE_FAST               4 (majorVersion)
    # 184         258 LOAD_FAST                4 (majorVersion)
    # 260 LOAD_CONST               8 (13)
    # 262 COMPARE_OP               5 (>=)
    # 268 POP_JUMP_FORWARD_IF_FALSE     5 (to 280)
    # 186         270 LOAD_FAST                4 (majorVersion)
    # 272 LOAD_CONST               6 (1)
    # 274 BINARY_OP               13 (+=)
    # 278 STORE_FAST               4 (majorVersion)
    # 187     >>  280 LOAD_GLOBAL             11 (NULL + int)
    # 292 LOAD_FAST                2 (s)
    # 294 LOAD_CONST               9 (2)
    # 296 LOAD_CONST              10 (3)
    # 298 BUILD_SLICE              2
    # 300 BINARY_SUBSCR
    # 310 PRECALL                  1
    # 314 CALL                     1
    # 324 LOAD_CONST              11 (10.0)
    # 326 BINARY_OP               11 (/)
    # 330 STORE_FAST               5 (minorVersion)
    # 189         332 LOAD_FAST                4 (majorVersion)
    # 334 LOAD_CONST               3 (6)
    # 336 COMPARE_OP               2 (==)
    # 342 POP_JUMP_FORWARD_IF_FALSE     2 (to 348)
    # 190         344 LOAD_CONST              12 (0)
    # 346 STORE_FAST               5 (minorVersion)
    # 191     >>  348 LOAD_FAST                4 (majorVersion)
    # 350 LOAD_CONST               3 (6)
    # 352 COMPARE_OP               5 (>=)
    # 358 POP_JUMP_FORWARD_IF_FALSE     5 (to 370)
    # 192         360 LOAD_FAST                4 (majorVersion)
    # 362 LOAD_FAST                5 (minorVersion)
    # 364 BINARY_OP                0 (+)
    # 368 RETURN_VALUE
    # 194     >>  370 LOAD_CONST               4 (None)
    # 372 RETURN_VALUE

def get_build_architecture():
    """Return the processor architecture.

    Possible results are "Intel" or "AMD64".
    """
    # 197           0 RESUME                   0
    # 203           2 LOAD_CONST               1 (' bit (')
    # 4 STORE_FAST               0 (prefix)
    # 204           6 LOAD_GLOBAL              0 (sys)
    # 18 LOAD_ATTR                1 (version)
    # 28 LOAD_METHOD              2 (find)
    # 50 LOAD_FAST                0 (prefix)
    # 52 PRECALL                  1
    # 56 CALL                     1
    # 66 STORE_FAST               1 (i)
    # 205          68 LOAD_FAST                1 (i)
    # 70 LOAD_CONST               2 (-1)
    # 72 COMPARE_OP               2 (==)
    # 78 POP_JUMP_FORWARD_IF_FALSE     2 (to 84)
    # 206          80 LOAD_CONST               3 ('Intel')
    # 82 RETURN_VALUE
    # 207     >>   84 LOAD_GLOBAL              0 (sys)
    # 96 LOAD_ATTR                1 (version)
    # 106 LOAD_METHOD              2 (find)
    # 128 LOAD_CONST               4 (')')
    # 130 LOAD_FAST                1 (i)
    # 132 PRECALL                  2
    # 136 CALL                     2
    # 146 STORE_FAST               2 (j)
    # 208         148 LOAD_GLOBAL              0 (sys)
    # 160 LOAD_ATTR                1 (version)
    # 170 LOAD_FAST                1 (i)
    # 172 LOAD_GLOBAL              7 (NULL + len)
    # 184 LOAD_FAST                0 (prefix)
    # 186 PRECALL                  1
    # 190 CALL                     1
    # 200 BINARY_OP                0 (+)
    # 204 LOAD_FAST                2 (j)
    # 206 BUILD_SLICE              2
    # 208 BINARY_SUBSCR
    # 218 RETURN_VALUE

def normalize_and_reduce_paths(paths):
    """Return a list of normalized paths with duplicates removed.

    The current order of paths is maintained.
    """
    # 211           0 RESUME                   0
    # 217           2 BUILD_LIST               0
    # 4 STORE_FAST               1 (reduced_paths)
    # 218           6 LOAD_FAST                0 (paths)
    # 8 GET_ITER
    # >>   10 FOR_ITER                58 (to 128)
    # 12 STORE_FAST               2 (p)
    # 219          14 LOAD_GLOBAL              0 (os)
    # 26 LOAD_ATTR                1 (path)
    # 36 LOAD_METHOD              2 (normpath)
    # 58 LOAD_FAST                2 (p)
    # 60 PRECALL                  1
    # 64 CALL                     1
    # 74 STORE_FAST               3 (np)
    # 221          76 LOAD_FAST                3 (np)
    # 78 LOAD_FAST                1 (reduced_paths)
    # 80 CONTAINS_OP              1
    # 82 POP_JUMP_FORWARD_IF_FALSE    21 (to 126)
    # 222          84 LOAD_FAST                1 (reduced_paths)
    # 86 LOAD_METHOD              3 (append)
    # 108 LOAD_FAST                3 (np)
    # 110 PRECALL                  1
    # 114 CALL                     1
    # 124 POP_TOP
    # >>  126 JUMP_BACKWARD           59 (to 10)
    # 223     >>  128 LOAD_FAST                1 (reduced_paths)
    # 130 RETURN_VALUE

class MSVCCompiler:
    """MSVCCompiler"""
    def __init__(self, verbose, dry_run, force):
        # 0 COPY_FREE_VARS           1
        # 255           2 RESUME                   0
        # 256           4 LOAD_GLOBAL              1 (NULL + super)
        # 16 PRECALL                  0
        # 20 CALL                     0
        # 30 LOAD_METHOD              1 (__init__)
        # 52 LOAD_FAST                1 (verbose)
        # 54 LOAD_FAST                2 (dry_run)
        # 56 LOAD_FAST                3 (force)
        # 58 PRECALL                  3
        # 62 CALL                     3
        # 72 POP_TOP
        # 257          74 LOAD_GLOBAL              5 (NULL + get_build_version)
        # 86 PRECALL                  0
        # 90 CALL                     0
        # 100 LOAD_FAST                0 (self)
        # 102 STORE_ATTR               3 (_MSVCCompiler__version)
        # 258         112 LOAD_GLOBAL              9 (NULL + get_build_architecture)
        # 124 PRECALL                  0
        # 128 CALL                     0
        # 138 LOAD_FAST                0 (self)
        # 140 STORE_ATTR               5 (_MSVCCompiler__arch)
        # 259         150 LOAD_FAST                0 (self)
        # 152 LOAD_ATTR                5 (_MSVCCompiler__arch)
        # 162 LOAD_CONST               1 ('Intel')
        # 164 COMPARE_OP               2 (==)
        # 170 POP_JUMP_FORWARD_IF_FALSE    67 (to 306)
        # 261         172 LOAD_FAST                0 (self)
        # 174 LOAD_ATTR                3 (_MSVCCompiler__version)
        # 184 LOAD_CONST               2 (7)
        # 186 COMPARE_OP               5 (>=)
        # 192 POP_JUMP_FORWARD_IF_FALSE    33 (to 260)
        # 262         194 LOAD_CONST               3 ('Software\\Microsoft\\VisualStudio')
        # 196 LOAD_FAST                0 (self)
        # 198 STORE_ATTR               6 (_MSVCCompiler__root)
        # 263         208 LOAD_GLOBAL             15 (NULL + MacroExpander)
        # 220 LOAD_FAST                0 (self)
        # 222 LOAD_ATTR                3 (_MSVCCompiler__version)
        # 232 PRECALL                  1
        # 236 CALL                     1
        # 246 LOAD_FAST                0 (self)
        # 248 STORE_ATTR               8 (_MSVCCompiler__macros)
        # 258 JUMP_FORWARD             7 (to 274)
        # 265     >>  260 LOAD_CONST               4 ('Software\\Microsoft\\Devstudio')
        # 262 LOAD_FAST                0 (self)
        # 264 STORE_ATTR               6 (_MSVCCompiler__root)
        # 266     >>  274 LOAD_CONST               5 ('Visual Studio version %s')
        # 276 LOAD_FAST                0 (self)
        # 278 LOAD_ATTR                3 (_MSVCCompiler__version)
        # 288 BINARY_OP                6 (%)
        # 292 LOAD_FAST                0 (self)
        # 294 STORE_ATTR               9 (_MSVCCompiler__product)
        # 304 JUMP_FORWARD            18 (to 342)
        # 269     >>  306 LOAD_CONST               6 ('Microsoft SDK compiler %s')
        # 308 LOAD_FAST                0 (self)
        # 310 LOAD_ATTR                3 (_MSVCCompiler__version)
        # 320 LOAD_CONST               7 (6)
        # 322 BINARY_OP                0 (+)
        # 326 BINARY_OP                6 (%)
        # 330 LOAD_FAST                0 (self)
        # 332 STORE_ATTR               9 (_MSVCCompiler__product)
        # 271     >>  342 LOAD_CONST               8 (False)
        # 344 LOAD_FAST                0 (self)
        # 346 STORE_ATTR              10 (initialized)
        # 356 LOAD_CONST               0 (None)
        # 358 RETURN_VALUE

    def initialize(self):
        # 273           0 RESUME                   0
        # 274           2 BUILD_LIST               0
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (_MSVCCompiler__paths)
        # 276          16 LOAD_CONST               1 ('DISTUTILS_USE_SDK')
        # 18 LOAD_GLOBAL              2 (os)
        # 30 LOAD_ATTR                2 (environ)
        # 40 CONTAINS_OP              0
        # 42 POP_JUMP_FORWARD_IF_FALSE    71 (to 186)
        # 277          44 LOAD_CONST               2 ('MSSdk')
        # 46 LOAD_GLOBAL              2 (os)
        # 58 LOAD_ATTR                2 (environ)
        # 68 CONTAINS_OP              0
        # 70 POP_JUMP_FORWARD_IF_FALSE    57 (to 186)
        # 278          72 LOAD_FAST                0 (self)
        # 74 LOAD_METHOD              3 (find_exe)
        # 96 LOAD_CONST               3 ('cl.exe')
        # 98 PRECALL                  1
        # 102 CALL                     1
        # 277         112 POP_JUMP_FORWARD_IF_FALSE    36 (to 186)
        # 282         114 LOAD_CONST               3 ('cl.exe')
        # 116 LOAD_FAST                0 (self)
        # 118 STORE_ATTR               4 (cc)
        # 283         128 LOAD_CONST               4 ('link.exe')
        # 130 LOAD_FAST                0 (self)
        # 132 STORE_ATTR               5 (linker)
        # 284         142 LOAD_CONST               5 ('lib.exe')
        # 144 LOAD_FAST                0 (self)
        # 146 STORE_ATTR               6 (lib)
        # 285         156 LOAD_CONST               6 ('rc.exe')
        # 158 LOAD_FAST                0 (self)
        # 160 STORE_ATTR               7 (rc)
        # 286         170 LOAD_CONST               7 ('mc.exe')
        # 172 LOAD_FAST                0 (self)
        # 174 STORE_ATTR               8 (mc)
        # 184 JUMP_FORWARD           245 (to 676)
        # 288     >>  186 LOAD_FAST                0 (self)
        # 188 LOAD_METHOD              9 (get_msvc_paths)
        # 210 LOAD_CONST               8 ('path')
        # 212 PRECALL                  1
        # 216 CALL                     1
        # 226 LOAD_FAST                0 (self)
        # 228 STORE_ATTR               0 (_MSVCCompiler__paths)
        # 290         238 LOAD_GLOBAL             21 (NULL + len)
        # 250 LOAD_FAST                0 (self)
        # 252 LOAD_ATTR                0 (_MSVCCompiler__paths)
        # 262 PRECALL                  1
        # 266 CALL                     1
        # 276 LOAD_CONST               9 (0)
        # 278 COMPARE_OP               2 (==)
        # 284 POP_JUMP_FORWARD_IF_FALSE    23 (to 332)
        # 291         286 LOAD_GLOBAL             23 (NULL + DistutilsPlatformError)
        # 292         298 LOAD_CONST              10 ("Python was built with %s, and extensions need to be built with the same version of the compiler, but it isn't installed.")
        # 294         300 LOAD_FAST                0 (self)
        # 302 LOAD_ATTR               12 (_MSVCCompiler__product)
        # 292         312 BINARY_OP                6 (%)
        # 291         316 PRECALL                  1
        # 320 CALL                     1
        # 330 RAISE_VARARGS            1
        # 297     >>  332 LOAD_FAST                0 (self)
        # 334 LOAD_METHOD              3 (find_exe)
        # 356 LOAD_CONST               3 ('cl.exe')
        # 358 PRECALL                  1
        # 362 CALL                     1
        # 372 LOAD_FAST                0 (self)
        # 374 STORE_ATTR               4 (cc)
        # 298         384 LOAD_FAST                0 (self)
        # 386 LOAD_METHOD              3 (find_exe)
        # 408 LOAD_CONST               4 ('link.exe')
        # 410 PRECALL                  1
        # 414 CALL                     1
        # 424 LOAD_FAST                0 (self)
        # 426 STORE_ATTR               5 (linker)
        # 299         436 LOAD_FAST                0 (self)
        # 438 LOAD_METHOD              3 (find_exe)
        # 460 LOAD_CONST               5 ('lib.exe')
        # 462 PRECALL                  1
        # 466 CALL                     1
        # 476 LOAD_FAST                0 (self)
        # 478 STORE_ATTR               6 (lib)
        # 300         488 LOAD_FAST                0 (self)
        # 490 LOAD_METHOD              3 (find_exe)
        # 512 LOAD_CONST               6 ('rc.exe')
        # 514 PRECALL                  1
        # 518 CALL                     1
        # 528 LOAD_FAST                0 (self)
        # 530 STORE_ATTR               7 (rc)
        # 301         540 LOAD_FAST                0 (self)
        # 542 LOAD_METHOD              3 (find_exe)
        # 564 LOAD_CONST               7 ('mc.exe')
        # 566 PRECALL                  1
        # 570 CALL                     1
        # 580 LOAD_FAST                0 (self)
        # 582 STORE_ATTR               8 (mc)
        # 302         592 LOAD_FAST                0 (self)
        # 594 LOAD_METHOD             13 (set_path_env_var)
        # 616 LOAD_CONST              11 ('lib')
        # 618 PRECALL                  1
        # 622 CALL                     1
        # 632 POP_TOP
        # 303         634 LOAD_FAST                0 (self)
        # 636 LOAD_METHOD             13 (set_path_env_var)
        # 658 LOAD_CONST              12 ('include')
        # 660 PRECALL                  1
        # 664 CALL                     1
        # 674 POP_TOP
        # 306     >>  676 NOP
        # 307         678 LOAD_GLOBAL              2 (os)
        # 690 LOAD_ATTR                2 (environ)
        # 700 LOAD_CONST               8 ('path')
        # 702 BINARY_SUBSCR
        # 712 LOAD_METHOD             14 (split)
        # 734 LOAD_CONST              13 (';')
        # 736 PRECALL                  1
        # 740 CALL                     1
        # 750 GET_ITER
        # >>  752 FOR_ITER                28 (to 810)
        # 754 STORE_FAST               1 (p)
        # 308         756 LOAD_FAST                0 (self)
        # 758 LOAD_ATTR                0 (_MSVCCompiler__paths)
        # 768 LOAD_METHOD             15 (append)
        # 790 LOAD_FAST                1 (p)
        # 792 PRECALL                  1
        # 796 CALL                     1
        # 806 POP_TOP
        # 808 JUMP_BACKWARD           29 (to 752)
        # 307     >>  810 JUMP_FORWARD            16 (to 844)
        # >>  812 PUSH_EXC_INFO
        # 309         814 LOAD_GLOBAL             32 (KeyError)
        # 826 CHECK_EXC_MATCH
        # 828 POP_JUMP_FORWARD_IF_FALSE     3 (to 836)
        # 830 POP_TOP
        # 310         832 POP_EXCEPT
        # 834 JUMP_FORWARD             4 (to 844)
        # 309     >>  836 RERAISE                  0
        # >>  838 COPY                     3
        # 840 POP_EXCEPT
        # 842 RERAISE                  1
        # 311     >>  844 LOAD_GLOBAL             35 (NULL + normalize_and_reduce_paths)
        # 856 LOAD_FAST                0 (self)
        # 858 LOAD_ATTR                0 (_MSVCCompiler__paths)
        # 868 PRECALL                  1
        # 872 CALL                     1
        # 882 LOAD_FAST                0 (self)
        # 884 STORE_ATTR               0 (_MSVCCompiler__paths)
        # 312         894 LOAD_CONST              13 (';')
        # 896 LOAD_METHOD             18 (join)
        # 918 LOAD_FAST                0 (self)
        # 920 LOAD_ATTR                0 (_MSVCCompiler__paths)
        # 930 PRECALL                  1
        # 934 CALL                     1
        # 944 LOAD_GLOBAL              2 (os)
        # 956 LOAD_ATTR                2 (environ)
        # 966 LOAD_CONST               8 ('path')
        # 968 STORE_SUBSCR
        # 314         972 LOAD_CONST               0 (None)
        # 974 LOAD_FAST                0 (self)
        # 976 STORE_ATTR              19 (preprocess_options)
        # 315         986 LOAD_FAST                0 (self)
        # 988 LOAD_ATTR               20 (_MSVCCompiler__arch)
        # 998 LOAD_CONST              14 ('Intel')
        # 1000 COMPARE_OP               2 (==)
        # 1006 POP_JUMP_FORWARD_IF_FALSE    19 (to 1046)
        # 316        1008 BUILD_LIST               0
        # 1010 LOAD_CONST              15 (('/nologo', '/O2', '/MD', '/W3', '/GX', '/DNDEBUG'))
        # 1012 LIST_EXTEND              1
        # 1014 LOAD_FAST                0 (self)
        # 1016 STORE_ATTR              21 (compile_options)
        # 317        1026 BUILD_LIST               0
        # 1028 LOAD_CONST              16 (('/nologo', '/Od', '/MDd', '/W3', '/GX', '/Z7', '/D_DEBUG'))
        # 1030 LIST_EXTEND              1
        # 1032 LOAD_FAST                0 (self)
        # 1034 STORE_ATTR              22 (compile_options_debug)
        # 1044 JUMP_FORWARD            18 (to 1082)
        # 328     >> 1046 BUILD_LIST               0
        # 1048 LOAD_CONST              17 (('/nologo', '/O2', '/MD', '/W3', '/GS-', '/DNDEBUG'))
        # 1050 LIST_EXTEND              1
        # 1052 LOAD_FAST                0 (self)
        # 1054 STORE_ATTR              21 (compile_options)
        # 329        1064 BUILD_LIST               0
        # 1066 LOAD_CONST              18 (('/nologo', '/Od', '/MDd', '/W3', '/GS-', '/Z7', '/D_DEBUG'))
        # 1068 LIST_EXTEND              1
        # 1070 LOAD_FAST                0 (self)
        # 1072 STORE_ATTR              22 (compile_options_debug)
        # 339     >> 1082 BUILD_LIST               0
        # 1084 LOAD_CONST              19 (('/DLL', '/nologo', '/INCREMENTAL:NO'))
        # 1086 LIST_EXTEND              1
        # 1088 LOAD_FAST                0 (self)
        # 1090 STORE_ATTR              23 (ldflags_shared)
        # 340        1100 LOAD_FAST                0 (self)
        # 1102 LOAD_ATTR               24 (_MSVCCompiler__version)
        # 1112 LOAD_CONST              20 (7)
        # 1114 COMPARE_OP               5 (>=)
        # 1120 POP_JUMP_FORWARD_IF_FALSE    10 (to 1142)
        # 341        1122 BUILD_LIST               0
        # 1124 LOAD_CONST              21 (('/DLL', '/nologo', '/INCREMENTAL:no', '/DEBUG'))
        # 1126 LIST_EXTEND              1
        # 1128 LOAD_FAST                0 (self)
        # 1130 STORE_ATTR              25 (ldflags_shared_debug)
        # 1140 JUMP_FORWARD             9 (to 1160)
        # 343     >> 1142 BUILD_LIST               0
        # 1144 LOAD_CONST              22 (('/DLL', '/nologo', '/INCREMENTAL:no', '/pdb:None', '/DEBUG'))
        # 1146 LIST_EXTEND              1
        # 1148 LOAD_FAST                0 (self)
        # 1150 STORE_ATTR              25 (ldflags_shared_debug)
        # 350     >> 1160 LOAD_CONST              23 ('/nologo')
        # 1162 BUILD_LIST               1
        # 1164 LOAD_FAST                0 (self)
        # 1166 STORE_ATTR              26 (ldflags_static)
        # 352        1176 LOAD_CONST              24 (True)
        # 1178 LOAD_FAST                0 (self)
        # 1180 STORE_ATTR              27 (initialized)
        # 1190 LOAD_CONST               0 (None)
        # 1192 RETURN_VALUE
        # ExceptionTable:
        # 678 to 808 -> 812 [0]
        # 812 to 830 -> 838 [1] lasti
        # 836 to 836 -> 838 [1] lasti

    def object_filenames(self, source_filenames, strip_dir, output_dir):
        # 356           0 RESUME                   0
        # 359           2 LOAD_FAST                3 (output_dir)
        # 4 POP_JUMP_FORWARD_IF_NOT_NONE     2 (to 10)
        # 360           6 LOAD_CONST               1 ('')
        # 8 STORE_FAST               3 (output_dir)
        # 361     >>   10 BUILD_LIST               0
        # 12 STORE_FAST               4 (obj_names)
        # 362          14 LOAD_FAST                1 (source_filenames)
        # 16 GET_ITER
        # >>   18 EXTENDED_ARG             1
        # 20 FOR_ITER               371 (to 764)
        # 22 STORE_FAST               5 (src_name)
        # 363          24 LOAD_GLOBAL              0 (os)
        # 36 LOAD_ATTR                1 (path)
        # 46 LOAD_METHOD              2 (splitext)
        # 68 LOAD_FAST                5 (src_name)
        # 70 PRECALL                  1
        # 74 CALL                     1
        # 84 UNPACK_SEQUENCE          2
        # 88 STORE_FAST               6 (base)
        # 90 STORE_FAST               7 (ext)
        # 364          92 LOAD_GLOBAL              0 (os)
        # 104 LOAD_ATTR                1 (path)
        # 114 LOAD_METHOD              3 (splitdrive)
        # 136 LOAD_FAST                6 (base)
        # 138 PRECALL                  1
        # 142 CALL                     1
        # 152 LOAD_CONST               2 (1)
        # 154 BINARY_SUBSCR
        # 164 STORE_FAST               6 (base)
        # 365         166 LOAD_FAST                6 (base)
        # 168 LOAD_GLOBAL              0 (os)
        # 180 LOAD_ATTR                1 (path)
        # 190 LOAD_METHOD              4 (isabs)
        # 212 LOAD_FAST                6 (base)
        # 214 PRECALL                  1
        # 218 CALL                     1
        # 228 LOAD_CONST               0 (None)
        # 230 BUILD_SLICE              2
        # 232 BINARY_SUBSCR
        # 242 STORE_FAST               6 (base)
        # 366         244 LOAD_FAST                7 (ext)
        # 246 LOAD_FAST                0 (self)
        # 248 LOAD_ATTR                5 (src_extensions)
        # 258 CONTAINS_OP              1
        # 260 POP_JUMP_FORWARD_IF_FALSE    18 (to 298)
        # 370         262 LOAD_GLOBAL             13 (NULL + CompileError)
        # 274 LOAD_CONST               3 ("Don't know how to compile %s")
        # 276 LOAD_FAST                5 (src_name)
        # 278 BINARY_OP                6 (%)
        # 282 PRECALL                  1
        # 286 CALL                     1
        # 296 RAISE_VARARGS            1
        # 371     >>  298 LOAD_FAST                2 (strip_dir)
        # 300 POP_JUMP_FORWARD_IF_FALSE    31 (to 364)
        # 372         302 LOAD_GLOBAL              0 (os)
        # 314 LOAD_ATTR                1 (path)
        # 324 LOAD_METHOD              7 (basename)
        # 346 LOAD_FAST                6 (base)
        # 348 PRECALL                  1
        # 352 CALL                     1
        # 362 STORE_FAST               6 (base)
        # 373     >>  364 LOAD_FAST                7 (ext)
        # 366 LOAD_FAST                0 (self)
        # 368 LOAD_ATTR                8 (_rc_extensions)
        # 378 CONTAINS_OP              0
        # 380 POP_JUMP_FORWARD_IF_FALSE    60 (to 502)
        # 374         382 LOAD_FAST                4 (obj_names)
        # 384 LOAD_METHOD              9 (append)
        # 406 LOAD_GLOBAL              0 (os)
        # 418 LOAD_ATTR                1 (path)
        # 428 LOAD_METHOD             10 (join)
        # 450 LOAD_FAST                3 (output_dir)
        # 452 LOAD_FAST                6 (base)
        # 454 LOAD_FAST                0 (self)
        # 456 LOAD_ATTR               11 (res_extension)
        # 466 BINARY_OP                0 (+)
        # 470 PRECALL                  2
        # 474 CALL                     2
        # 484 PRECALL                  1
        # 488 CALL                     1
        # 498 POP_TOP
        # 500 JUMP_BACKWARD          242 (to 18)
        # 375     >>  502 LOAD_FAST                7 (ext)
        # 504 LOAD_FAST                0 (self)
        # 506 LOAD_ATTR               12 (_mc_extensions)
        # 516 CONTAINS_OP              0
        # 518 POP_JUMP_FORWARD_IF_FALSE    61 (to 642)
        # 376         520 LOAD_FAST                4 (obj_names)
        # 522 LOAD_METHOD              9 (append)
        # 544 LOAD_GLOBAL              0 (os)
        # 556 LOAD_ATTR                1 (path)
        # 566 LOAD_METHOD             10 (join)
        # 588 LOAD_FAST                3 (output_dir)
        # 590 LOAD_FAST                6 (base)
        # 592 LOAD_FAST                0 (self)
        # 594 LOAD_ATTR               11 (res_extension)
        # 604 BINARY_OP                0 (+)
        # 608 PRECALL                  2
        # 612 CALL                     2
        # 622 PRECALL                  1
        # 626 CALL                     1
        # 636 POP_TOP
        # 638 EXTENDED_ARG             1
        # 640 JUMP_BACKWARD          312 (to 18)
        # 378     >>  642 LOAD_FAST                4 (obj_names)
        # 644 LOAD_METHOD              9 (append)
        # 666 LOAD_GLOBAL              0 (os)
        # 678 LOAD_ATTR                1 (path)
        # 688 LOAD_METHOD             10 (join)
        # 710 LOAD_FAST                3 (output_dir)
        # 712 LOAD_FAST                6 (base)
        # 714 LOAD_FAST                0 (self)
        # 716 LOAD_ATTR               13 (obj_extension)
        # 726 BINARY_OP                0 (+)
        # 730 PRECALL                  2
        # 734 CALL                     2
        # 744 PRECALL                  1
        # 748 CALL                     1
        # 758 POP_TOP
        # 760 EXTENDED_ARG             1
        # 762 JUMP_BACKWARD          373 (to 18)
        # 379     >>  764 LOAD_FAST                4 (obj_names)
        # 766 RETURN_VALUE

    def compile(self, sources, output_dir, macros, include_dirs, debug, extra_preargs, extra_postargs, depends):
        # 381           0 RESUME                   0
        # 393           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (initialized)
        # 14 POP_JUMP_FORWARD_IF_TRUE    20 (to 56)
        # 394          16 LOAD_FAST                0 (self)
        # 18 LOAD_METHOD              1 (initialize)
        # 40 PRECALL                  0
        # 44 CALL                     0
        # 54 POP_TOP
        # 395     >>   56 LOAD_FAST                0 (self)
        # 58 LOAD_METHOD              2 (_setup_compile)
        # 396          80 LOAD_FAST                2 (output_dir)
        # 82 LOAD_FAST                3 (macros)
        # 84 LOAD_FAST                4 (include_dirs)
        # 86 LOAD_FAST                1 (sources)
        # 88 LOAD_FAST                8 (depends)
        # 90 LOAD_FAST                7 (extra_postargs)
        # 395          92 PRECALL                  6
        # 96 CALL                     6
        # 106 STORE_FAST               9 (compile_info)
        # 398         108 LOAD_FAST                9 (compile_info)
        # 110 UNPACK_SEQUENCE          5
        # 114 STORE_FAST               3 (macros)
        # 116 STORE_FAST              10 (objects)
        # 118 STORE_FAST               7 (extra_postargs)
        # 120 STORE_FAST              11 (pp_opts)
        # 122 STORE_FAST              12 (build)
        # 400         124 LOAD_FAST                6 (extra_preargs)
        # 126 JUMP_IF_TRUE_OR_POP      1 (to 130)
        # 128 BUILD_LIST               0
        # >>  130 STORE_FAST              13 (compile_opts)
        # 401         132 LOAD_FAST               13 (compile_opts)
        # 134 LOAD_METHOD              3 (append)
        # 156 LOAD_CONST               1 ('/c')
        # 158 PRECALL                  1
        # 162 CALL                     1
        # 172 POP_TOP
        # 402         174 LOAD_FAST                5 (debug)
        # 176 POP_JUMP_FORWARD_IF_FALSE    27 (to 232)
        # 403         178 LOAD_FAST               13 (compile_opts)
        # 180 LOAD_METHOD              4 (extend)
        # 202 LOAD_FAST                0 (self)
        # 204 LOAD_ATTR                5 (compile_options_debug)
        # 214 PRECALL                  1
        # 218 CALL                     1
        # 228 POP_TOP
        # 230 JUMP_FORWARD            26 (to 284)
        # 405     >>  232 LOAD_FAST               13 (compile_opts)
        # 234 LOAD_METHOD              4 (extend)
        # 256 LOAD_FAST                0 (self)
        # 258 LOAD_ATTR                6 (compile_options)
        # 268 PRECALL                  1
        # 272 CALL                     1
        # 282 POP_TOP
        # 407     >>  284 LOAD_FAST               10 (objects)
        # 286 GET_ITER
        # >>  288 EXTENDED_ARG             2
        # 290 FOR_ITER               585 (to 1462)
        # 292 STORE_FAST              14 (obj)
        # 408         294 NOP
        # 409         296 LOAD_FAST               12 (build)
        # 298 LOAD_FAST               14 (obj)
        # 300 BINARY_SUBSCR
        # 310 UNPACK_SEQUENCE          2
        # 314 STORE_FAST              15 (src)
        # 316 STORE_FAST              16 (ext)
        # 318 JUMP_FORWARD            16 (to 352)
        # >>  320 PUSH_EXC_INFO
        # 410         322 LOAD_GLOBAL             14 (KeyError)
        # 334 CHECK_EXC_MATCH
        # 336 POP_JUMP_FORWARD_IF_FALSE     3 (to 344)
        # 338 POP_TOP
        # 411         340 POP_EXCEPT
        # 342 JUMP_BACKWARD           28 (to 288)
        # 410     >>  344 RERAISE                  0
        # >>  346 COPY                     3
        # 348 POP_EXCEPT
        # 350 RERAISE                  1
        # 412     >>  352 LOAD_FAST                5 (debug)
        # 354 POP_JUMP_FORWARD_IF_FALSE    31 (to 418)
        # 416         356 LOAD_GLOBAL             16 (os)
        # 368 LOAD_ATTR                9 (path)
        # 378 LOAD_METHOD             10 (abspath)
        # 400 LOAD_FAST               15 (src)
        # 402 PRECALL                  1
        # 406 CALL                     1
        # 416 STORE_FAST              15 (src)
        # 418     >>  418 LOAD_FAST               16 (ext)
        # 420 LOAD_FAST                0 (self)
        # 422 LOAD_ATTR               11 (_c_extensions)
        # 432 CONTAINS_OP              0
        # 434 POP_JUMP_FORWARD_IF_FALSE     7 (to 450)
        # 419         436 LOAD_CONST               2 ('/Tc')
        # 438 LOAD_FAST               15 (src)
        # 440 BINARY_OP                0 (+)
        # 444 STORE_FAST              17 (input_opt)
        # 446 EXTENDED_ARG             1
        # 448 JUMP_FORWARD           424 (to 1298)
        # 420     >>  450 LOAD_FAST               16 (ext)
        # 452 LOAD_FAST                0 (self)
        # 454 LOAD_ATTR               12 (_cpp_extensions)
        # 464 CONTAINS_OP              0
        # 466 POP_JUMP_FORWARD_IF_FALSE     7 (to 482)
        # 421         468 LOAD_CONST               3 ('/Tp')
        # 470 LOAD_FAST               15 (src)
        # 472 BINARY_OP                0 (+)
        # 476 STORE_FAST              17 (input_opt)
        # 478 EXTENDED_ARG             1
        # 480 JUMP_FORWARD           408 (to 1298)
        # 422     >>  482 LOAD_FAST               16 (ext)
        # 484 LOAD_FAST                0 (self)
        # 486 LOAD_ATTR               13 (_rc_extensions)
        # 496 CONTAINS_OP              0
        # 498 POP_JUMP_FORWARD_IF_FALSE    81 (to 662)
        # 424         500 LOAD_FAST               15 (src)
        # 502 STORE_FAST              17 (input_opt)
        # 425         504 LOAD_CONST               4 ('/fo')
        # 506 LOAD_FAST               14 (obj)
        # 508 BINARY_OP                0 (+)
        # 512 STORE_FAST              18 (output_opt)
        # 426         514 NOP
        # 427         516 LOAD_FAST                0 (self)
        # 518 LOAD_METHOD             14 (spawn)
        # 540 LOAD_FAST                0 (self)
        # 542 LOAD_ATTR               15 (rc)
        # 552 BUILD_LIST               1
        # 554 LOAD_FAST               11 (pp_opts)
        # 556 BINARY_OP                0 (+)
        # 560 LOAD_FAST               18 (output_opt)
        # 562 BUILD_LIST               1
        # 564 BINARY_OP                0 (+)
        # 568 LOAD_FAST               17 (input_opt)
        # 570 BUILD_LIST               1
        # 572 BINARY_OP                0 (+)
        # 576 PRECALL                  1
        # 580 CALL                     1
        # 590 POP_TOP
        # 592 JUMP_FORWARD            33 (to 660)
        # >>  594 PUSH_EXC_INFO
        # 428         596 LOAD_GLOBAL             32 (DistutilsExecError)
        # 608 CHECK_EXC_MATCH
        # 610 POP_JUMP_FORWARD_IF_FALSE    20 (to 652)
        # 612 STORE_FAST              19 (msg)
        # 429         614 LOAD_GLOBAL             35 (NULL + CompileError)
        # 626 LOAD_FAST               19 (msg)
        # 628 PRECALL                  1
        # 632 CALL                     1
        # 642 RAISE_VARARGS            1
        # >>  644 LOAD_CONST               0 (None)
        # 646 STORE_FAST              19 (msg)
        # 648 DELETE_FAST             19 (msg)
        # 650 RERAISE                  1
        # 428     >>  652 RERAISE                  0
        # >>  654 COPY                     3
        # 656 POP_EXCEPT
        # 658 RERAISE                  1
        # 430     >>  660 JUMP_BACKWARD          187 (to 288)
        # 431     >>  662 LOAD_FAST               16 (ext)
        # 664 LOAD_FAST                0 (self)
        # 666 LOAD_ATTR               18 (_mc_extensions)
        # 676 CONTAINS_OP              0
        # 678 EXTENDED_ARG             1
        # 680 POP_JUMP_FORWARD_IF_FALSE   273 (to 1228)
        # 443         682 LOAD_GLOBAL             16 (os)
        # 694 LOAD_ATTR                9 (path)
        # 704 LOAD_METHOD             19 (dirname)
        # 726 LOAD_FAST               15 (src)
        # 728 PRECALL                  1
        # 732 CALL                     1
        # 742 STORE_FAST              20 (h_dir)
        # 444         744 LOAD_GLOBAL             16 (os)
        # 756 LOAD_ATTR                9 (path)
        # 766 LOAD_METHOD             19 (dirname)
        # 788 LOAD_FAST               14 (obj)
        # 790 PRECALL                  1
        # 794 CALL                     1
        # 804 STORE_FAST              21 (rc_dir)
        # 445         806 NOP
        # 447         808 LOAD_FAST                0 (self)
        # 810 LOAD_METHOD             14 (spawn)
        # 832 LOAD_FAST                0 (self)
        # 834 LOAD_ATTR               20 (mc)
        # 844 BUILD_LIST               1
        # 846 LOAD_CONST               5 ('-h')
        # 848 LOAD_FAST               20 (h_dir)
        # 850 LOAD_CONST               6 ('-r')
        # 852 LOAD_FAST               21 (rc_dir)
        # 854 BUILD_LIST               4
        # 856 BINARY_OP                0 (+)
        # 860 LOAD_FAST               15 (src)
        # 862 BUILD_LIST               1
        # 864 BINARY_OP                0 (+)
        # 868 PRECALL                  1
        # 872 CALL                     1
        # 882 POP_TOP
        # 448         884 LOAD_GLOBAL             16 (os)
        # 896 LOAD_ATTR                9 (path)
        # 906 LOAD_METHOD             21 (splitext)
        # 928 LOAD_GLOBAL             16 (os)
        # 940 LOAD_ATTR                9 (path)
        # 950 LOAD_METHOD             22 (basename)
        # 972 LOAD_FAST               15 (src)
        # 974 PRECALL                  1
        # 978 CALL                     1
        # 988 PRECALL                  1
        # 992 CALL                     1
        # 1002 UNPACK_SEQUENCE          2
        # 1006 STORE_FAST              22 (base)
        # 1008 STORE_FAST              23 (_)
        # 449        1010 LOAD_GLOBAL             16 (os)
        # 1022 LOAD_ATTR                9 (path)
        # 1032 LOAD_METHOD             23 (join)
        # 1054 LOAD_FAST               21 (rc_dir)
        # 1056 LOAD_FAST               22 (base)
        # 1058 LOAD_CONST               7 ('.rc')
        # 1060 BINARY_OP                0 (+)
        # 1064 PRECALL                  2
        # 1068 CALL                     2
        # 1078 STORE_FAST              24 (rc_file)
        # 451        1080 LOAD_FAST                0 (self)
        # 1082 LOAD_METHOD             14 (spawn)
        # 1104 LOAD_FAST                0 (self)
        # 1106 LOAD_ATTR               15 (rc)
        # 1116 BUILD_LIST               1
        # 1118 LOAD_CONST               4 ('/fo')
        # 1120 LOAD_FAST               14 (obj)
        # 1122 BINARY_OP                0 (+)
        # 1126 BUILD_LIST               1
        # 1128 BINARY_OP                0 (+)
        # 1132 LOAD_FAST               24 (rc_file)
        # 1134 BUILD_LIST               1
        # 1136 BINARY_OP                0 (+)
        # 1140 PRECALL                  1
        # 1144 CALL                     1
        # 1154 POP_TOP
        # 1156 JUMP_FORWARD            33 (to 1224)
        # >> 1158 PUSH_EXC_INFO
        # 453        1160 LOAD_GLOBAL             32 (DistutilsExecError)
        # 1172 CHECK_EXC_MATCH
        # 1174 POP_JUMP_FORWARD_IF_FALSE    20 (to 1216)
        # 1176 STORE_FAST              19 (msg)
        # 454        1178 LOAD_GLOBAL             35 (NULL + CompileError)
        # 1190 LOAD_FAST               19 (msg)
        # 1192 PRECALL                  1
        # 1196 CALL                     1
        # 1206 RAISE_VARARGS            1
        # >> 1208 LOAD_CONST               0 (None)
        # 1210 STORE_FAST              19 (msg)
        # 1212 DELETE_FAST             19 (msg)
        # 1214 RERAISE                  1
        # 453     >> 1216 RERAISE                  0
        # >> 1218 COPY                     3
        # 1220 POP_EXCEPT
        # 1222 RERAISE                  1
        # 455     >> 1224 EXTENDED_ARG             1
        # 1226 JUMP_BACKWARD          470 (to 288)
        # 458     >> 1228 LOAD_GLOBAL             35 (NULL + CompileError)
        # 459        1240 LOAD_CONST               8 ("Don't know how to compile {} to {}")
        # 1242 LOAD_METHOD             24 (format)
        # 1264 LOAD_FAST               15 (src)
        # 1266 LOAD_FAST               14 (obj)
        # 1268 PRECALL                  2
        # 1272 CALL                     2
        # 458        1282 PRECALL                  1
        # 1286 CALL                     1
        # 1296 RAISE_VARARGS            1
        # 462     >> 1298 LOAD_CONST               9 ('/Fo')
        # 1300 LOAD_FAST               14 (obj)
        # 1302 BINARY_OP                0 (+)
        # 1306 STORE_FAST              18 (output_opt)
        # 463        1308 NOP
        # 464        1310 LOAD_FAST                0 (self)
        # 1312 LOAD_METHOD             14 (spawn)
        # 465        1334 LOAD_FAST                0 (self)
        # 1336 LOAD_ATTR               25 (cc)
        # 1346 BUILD_LIST               1
        # 466        1348 LOAD_FAST               13 (compile_opts)
        # 465        1350 BINARY_OP                0 (+)
        # 467        1354 LOAD_FAST               11 (pp_opts)
        # 465        1356 BINARY_OP                0 (+)
        # 468        1360 LOAD_FAST               17 (input_opt)
        # 1362 LOAD_FAST               18 (output_opt)
        # 1364 BUILD_LIST               2
        # 465        1366 BINARY_OP                0 (+)
        # 469        1370 LOAD_FAST                7 (extra_postargs)
        # 465        1372 BINARY_OP                0 (+)
        # 464        1376 PRECALL                  1
        # 1380 CALL                     1
        # 1390 POP_TOP
        # 1392 EXTENDED_ARG             2
        # 1394 JUMP_BACKWARD          554 (to 288)
        # >> 1396 PUSH_EXC_INFO
        # 471        1398 LOAD_GLOBAL             32 (DistutilsExecError)
        # 1410 CHECK_EXC_MATCH
        # 1412 POP_JUMP_FORWARD_IF_FALSE    20 (to 1454)
        # 1414 STORE_FAST              19 (msg)
        # 472        1416 LOAD_GLOBAL             35 (NULL + CompileError)
        # 1428 LOAD_FAST               19 (msg)
        # 1430 PRECALL                  1
        # 1434 CALL                     1
        # 1444 RAISE_VARARGS            1
        # >> 1446 LOAD_CONST               0 (None)
        # 1448 STORE_FAST              19 (msg)
        # 1450 DELETE_FAST             19 (msg)
        # 1452 RERAISE                  1
        # 471     >> 1454 RERAISE                  0
        # >> 1456 COPY                     3
        # 1458 POP_EXCEPT
        # 1460 RERAISE                  1
        # 474     >> 1462 LOAD_FAST               10 (objects)
        # 1464 RETURN_VALUE
        # ExceptionTable:
        # 296 to 316 -> 320 [1]
        # 320 to 338 -> 346 [2] lasti
        # 344 to 344 -> 346 [2] lasti
        # 516 to 590 -> 594 [1]
        # 594 to 612 -> 654 [2] lasti
        # 614 to 642 -> 644 [2] lasti
        # 644 to 652 -> 654 [2] lasti
        # 808 to 1154 -> 1158 [1]
        # 1158 to 1176 -> 1218 [2] lasti
        # 1178 to 1206 -> 1208 [2] lasti
        # 1208 to 1216 -> 1218 [2] lasti
        # 1310 to 1390 -> 1396 [1]
        # 1396 to 1414 -> 1456 [2] lasti
        # 1416 to 1444 -> 1446 [2] lasti
        # 1446 to 1454 -> 1456 [2] lasti

    def create_static_lib(self, objects, output_libname, output_dir, debug, target_lang):
        # 476           0 RESUME                   0
        # 480           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (initialized)
        # 14 POP_JUMP_FORWARD_IF_TRUE    20 (to 56)
        # 481          16 LOAD_FAST                0 (self)
        # 18 LOAD_METHOD              1 (initialize)
        # 40 PRECALL                  0
        # 44 CALL                     0
        # 54 POP_TOP
        # 482     >>   56 LOAD_FAST                0 (self)
        # 58 LOAD_METHOD              2 (_fix_object_args)
        # 80 LOAD_FAST                1 (objects)
        # 82 LOAD_FAST                3 (output_dir)
        # 84 PRECALL                  2
        # 88 CALL                     2
        # 98 UNPACK_SEQUENCE          2
        # 102 STORE_FAST               1 (objects)
        # 104 STORE_FAST               3 (output_dir)
        # 483         106 LOAD_FAST                0 (self)
        # 108 LOAD_METHOD              3 (library_filename)
        # 130 LOAD_FAST                2 (output_libname)
        # 132 LOAD_FAST                3 (output_dir)
        # 134 KW_NAMES                 1
        # 136 PRECALL                  2
        # 140 CALL                     2
        # 150 STORE_FAST               6 (output_filename)
        # 485         152 LOAD_FAST                0 (self)
        # 154 LOAD_METHOD              4 (_need_link)
        # 176 LOAD_FAST                1 (objects)
        # 178 LOAD_FAST                6 (output_filename)
        # 180 PRECALL                  2
        # 184 CALL                     2
        # 194 POP_JUMP_FORWARD_IF_FALSE    78 (to 352)
        # 486         196 LOAD_FAST                1 (objects)
        # 198 LOAD_CONST               2 ('/OUT:')
        # 200 LOAD_FAST                6 (output_filename)
        # 202 BINARY_OP                0 (+)
        # 206 BUILD_LIST               1
        # 208 BINARY_OP                0 (+)
        # 212 STORE_FAST               7 (lib_args)
        # 487         214 LOAD_FAST                4 (debug)
        # 216 POP_JUMP_FORWARD_IF_FALSE     1 (to 220)
        # 488         218 NOP
        # 489     >>  220 NOP
        # 490         222 LOAD_FAST                0 (self)
        # 224 LOAD_METHOD              5 (spawn)
        # 246 LOAD_FAST                0 (self)
        # 248 LOAD_ATTR                6 (lib)
        # 258 BUILD_LIST               1
        # 260 LOAD_FAST                7 (lib_args)
        # 262 BINARY_OP                0 (+)
        # 266 PRECALL                  1
        # 270 CALL                     1
        # 280 POP_TOP
        # 282 LOAD_CONST               0 (None)
        # 284 RETURN_VALUE
        # >>  286 PUSH_EXC_INFO
        # 491         288 LOAD_GLOBAL             14 (DistutilsExecError)
        # 300 CHECK_EXC_MATCH
        # 302 POP_JUMP_FORWARD_IF_FALSE    20 (to 344)
        # 304 STORE_FAST               8 (msg)
        # 492         306 LOAD_GLOBAL             17 (NULL + LibError)
        # 318 LOAD_FAST                8 (msg)
        # 320 PRECALL                  1
        # 324 CALL                     1
        # 334 RAISE_VARARGS            1
        # >>  336 LOAD_CONST               0 (None)
        # 338 STORE_FAST               8 (msg)
        # 340 DELETE_FAST              8 (msg)
        # 342 RERAISE                  1
        # 491     >>  344 RERAISE                  0
        # >>  346 COPY                     3
        # 348 POP_EXCEPT
        # 350 RERAISE                  1
        # 494     >>  352 LOAD_GLOBAL             19 (NULL + log)
        # 364 LOAD_ATTR               10 (debug)
        # 374 LOAD_CONST               3 ('skipping %s (up-to-date)')
        # 376 LOAD_FAST                6 (output_filename)
        # 378 PRECALL                  2
        # 382 CALL                     2
        # 392 POP_TOP
        # 394 LOAD_CONST               0 (None)
        # 396 RETURN_VALUE
        # ExceptionTable:
        # 222 to 280 -> 286 [0]
        # 286 to 304 -> 346 [1] lasti
        # 306 to 334 -> 336 [1] lasti
        # 336 to 344 -> 346 [1] lasti

    def link(self, target_desc, objects, output_filename, output_dir, libraries, library_dirs, runtime_library_dirs, export_symbols, debug, extra_preargs, extra_postargs, build_temp, target_lang):
        # 496           0 RESUME                   0
        # 513           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (initialized)
        # 14 POP_JUMP_FORWARD_IF_TRUE    20 (to 56)
        # 514          16 LOAD_FAST                0 (self)
        # 18 LOAD_METHOD              1 (initialize)
        # 40 PRECALL                  0
        # 44 CALL                     0
        # 54 POP_TOP
        # 515     >>   56 LOAD_FAST                0 (self)
        # 58 LOAD_METHOD              2 (_fix_object_args)
        # 80 LOAD_FAST                2 (objects)
        # 82 LOAD_FAST                4 (output_dir)
        # 84 PRECALL                  2
        # 88 CALL                     2
        # 98 UNPACK_SEQUENCE          2
        # 102 STORE_FAST               2 (objects)
        # 104 STORE_FAST               4 (output_dir)
        # 516         106 LOAD_FAST                0 (self)
        # 108 LOAD_METHOD              3 (_fix_lib_args)
        # 130 LOAD_FAST                5 (libraries)
        # 132 LOAD_FAST                6 (library_dirs)
        # 134 LOAD_FAST                7 (runtime_library_dirs)
        # 136 PRECALL                  3
        # 140 CALL                     3
        # 150 STORE_FAST              14 (fixed_args)
        # 517         152 LOAD_FAST               14 (fixed_args)
        # 154 UNPACK_SEQUENCE          3
        # 158 STORE_FAST               5 (libraries)
        # 160 STORE_FAST               6 (library_dirs)
        # 162 STORE_FAST               7 (runtime_library_dirs)
        # 519         164 LOAD_FAST                7 (runtime_library_dirs)
        # 166 POP_JUMP_FORWARD_IF_FALSE    37 (to 242)
        # 520         168 LOAD_FAST                0 (self)
        # 170 LOAD_METHOD              4 (warn)
        # 521         192 LOAD_CONST               1 ("I don't know what to do with 'runtime_library_dirs': ")
        # 522         194 LOAD_GLOBAL             11 (NULL + str)
        # 206 LOAD_FAST                7 (runtime_library_dirs)
        # 208 PRECALL                  1
        # 212 CALL                     1
        # 521         222 BINARY_OP                0 (+)
        # 520         226 PRECALL                  1
        # 230 CALL                     1
        # 240 POP_TOP
        # 525     >>  242 LOAD_GLOBAL             13 (NULL + gen_lib_options)
        # 254 LOAD_FAST                0 (self)
        # 256 LOAD_FAST                6 (library_dirs)
        # 258 LOAD_FAST                7 (runtime_library_dirs)
        # 260 LOAD_FAST                5 (libraries)
        # 262 PRECALL                  4
        # 266 CALL                     4
        # 276 STORE_FAST              15 (lib_opts)
        # 526         278 LOAD_FAST                4 (output_dir)
        # 280 POP_JUMP_FORWARD_IF_NONE    32 (to 346)
        # 527         282 LOAD_GLOBAL             14 (os)
        # 294 LOAD_ATTR                8 (path)
        # 304 LOAD_METHOD              9 (join)
        # 326 LOAD_FAST                4 (output_dir)
        # 328 LOAD_FAST                3 (output_filename)
        # 330 PRECALL                  2
        # 334 CALL                     2
        # 344 STORE_FAST               3 (output_filename)
        # 529     >>  346 LOAD_FAST                0 (self)
        # 348 LOAD_METHOD             10 (_need_link)
        # 370 LOAD_FAST                2 (objects)
        # 372 LOAD_FAST                3 (output_filename)
        # 374 PRECALL                  2
        # 378 CALL                     2
        # 388 EXTENDED_ARG             1
        # 390 POP_JUMP_FORWARD_IF_FALSE   441 (to 1274)
        # 530         392 LOAD_FAST                1 (target_desc)
        # 394 LOAD_GLOBAL             22 (CCompiler)
        # 406 LOAD_ATTR               12 (EXECUTABLE)
        # 416 COMPARE_OP               2 (==)
        # 422 POP_JUMP_FORWARD_IF_FALSE    34 (to 492)
        # 531         424 LOAD_FAST                9 (debug)
        # 426 POP_JUMP_FORWARD_IF_FALSE    16 (to 460)
        # 532         428 LOAD_FAST                0 (self)
        # 430 LOAD_ATTR               13 (ldflags_shared_debug)
        # 440 LOAD_CONST               2 (1)
        # 442 LOAD_CONST               0 (None)
        # 444 BUILD_SLICE              2
        # 446 BINARY_SUBSCR
        # 456 STORE_FAST              16 (ldflags)
        # 458 JUMP_FORWARD            33 (to 526)
        # 534     >>  460 LOAD_FAST                0 (self)
        # 462 LOAD_ATTR               14 (ldflags_shared)
        # 472 LOAD_CONST               2 (1)
        # 474 LOAD_CONST               0 (None)
        # 476 BUILD_SLICE              2
        # 478 BINARY_SUBSCR
        # 488 STORE_FAST              16 (ldflags)
        # 490 JUMP_FORWARD            17 (to 526)
        # 536     >>  492 LOAD_FAST                9 (debug)
        # 494 POP_JUMP_FORWARD_IF_FALSE     8 (to 512)
        # 537         496 LOAD_FAST                0 (self)
        # 498 LOAD_ATTR               13 (ldflags_shared_debug)
        # 508 STORE_FAST              16 (ldflags)
        # 510 JUMP_FORWARD             7 (to 526)
        # 539     >>  512 LOAD_FAST                0 (self)
        # 514 LOAD_ATTR               14 (ldflags_shared)
        # 524 STORE_FAST              16 (ldflags)
        # 541     >>  526 BUILD_LIST               0
        # 528 STORE_FAST              17 (export_opts)
        # 542         530 LOAD_FAST                8 (export_symbols)
        # 532 JUMP_IF_TRUE_OR_POP      1 (to 536)
        # 534 BUILD_LIST               0
        # >>  536 GET_ITER
        # >>  538 FOR_ITER                26 (to 592)
        # 540 STORE_FAST              18 (sym)
        # 543         542 LOAD_FAST               17 (export_opts)
        # 544 LOAD_METHOD             15 (append)
        # 566 LOAD_CONST               3 ('/EXPORT:')
        # 568 LOAD_FAST               18 (sym)
        # 570 BINARY_OP                0 (+)
        # 574 PRECALL                  1
        # 578 CALL                     1
        # 588 POP_TOP
        # 590 JUMP_BACKWARD           27 (to 538)
        # 546     >>  592 LOAD_FAST               16 (ldflags)
        # 594 LOAD_FAST               15 (lib_opts)
        # 596 BINARY_OP                0 (+)
        # 600 LOAD_FAST               17 (export_opts)
        # 602 BINARY_OP                0 (+)
        # 606 LOAD_FAST                2 (objects)
        # 608 BINARY_OP                0 (+)
        # 612 LOAD_CONST               4 ('/OUT:')
        # 614 LOAD_FAST                3 (output_filename)
        # 616 BINARY_OP                0 (+)
        # 620 BUILD_LIST               1
        # 622 BINARY_OP                0 (+)
        # 545         626 STORE_FAST              19 (ld_args)
        # 554         628 LOAD_FAST                8 (export_symbols)
        # 630 POP_JUMP_FORWARD_IF_NONE   173 (to 978)
        # 555         632 LOAD_GLOBAL             14 (os)
        # 644 LOAD_ATTR                8 (path)
        # 654 LOAD_METHOD             16 (splitext)
        # 556         676 LOAD_GLOBAL             14 (os)
        # 688 LOAD_ATTR                8 (path)
        # 698 LOAD_METHOD             17 (basename)
        # 720 LOAD_FAST                3 (output_filename)
        # 722 PRECALL                  1
        # 726 CALL                     1
        # 555         736 PRECALL                  1
        # 740 CALL                     1
        # 750 UNPACK_SEQUENCE          2
        # 754 STORE_FAST              20 (dll_name)
        # 756 STORE_FAST              21 (dll_ext)
        # 558         758 LOAD_GLOBAL             14 (os)
        # 770 LOAD_ATTR                8 (path)
        # 780 LOAD_METHOD              9 (join)
        # 559         802 LOAD_GLOBAL             14 (os)
        # 814 LOAD_ATTR                8 (path)
        # 824 LOAD_METHOD             18 (dirname)
        # 846 LOAD_FAST                2 (objects)
        # 848 LOAD_CONST               5 (0)
        # 850 BINARY_SUBSCR
        # 860 PRECALL                  1
        # 864 CALL                     1
        # 874 LOAD_FAST                0 (self)
        # 876 LOAD_METHOD             19 (library_filename)
        # 898 LOAD_FAST               20 (dll_name)
        # 900 PRECALL                  1
        # 904 CALL                     1
        # 558         914 PRECALL                  2
        # 918 CALL                     2
        # 928 STORE_FAST              22 (implib_file)
        # 561         930 LOAD_FAST               19 (ld_args)
        # 932 LOAD_METHOD             15 (append)
        # 954 LOAD_CONST               6 ('/IMPLIB:')
        # 956 LOAD_FAST               22 (implib_file)
        # 958 BINARY_OP                0 (+)
        # 962 PRECALL                  1
        # 966 CALL                     1
        # 976 POP_TOP
        # 563     >>  978 LOAD_FAST               10 (extra_preargs)
        # 980 POP_JUMP_FORWARD_IF_FALSE     7 (to 996)
        # 564         982 LOAD_FAST               10 (extra_preargs)
        # 984 LOAD_FAST               19 (ld_args)
        # 986 LOAD_CONST               0 (None)
        # 988 LOAD_CONST               5 (0)
        # 990 BUILD_SLICE              2
        # 992 STORE_SUBSCR
        # 565     >>  996 LOAD_FAST               11 (extra_postargs)
        # 998 POP_JUMP_FORWARD_IF_FALSE    21 (to 1042)
        # 566        1000 LOAD_FAST               19 (ld_args)
        # 1002 LOAD_METHOD             20 (extend)
        # 1024 LOAD_FAST               11 (extra_postargs)
        # 1026 PRECALL                  1
        # 1030 CALL                     1
        # 1040 POP_TOP
        # 568     >> 1042 LOAD_FAST                0 (self)
        # 1044 LOAD_METHOD             21 (mkpath)
        # 1066 LOAD_GLOBAL             14 (os)
        # 1078 LOAD_ATTR                8 (path)
        # 1088 LOAD_METHOD             18 (dirname)
        # 1110 LOAD_FAST                3 (output_filename)
        # 1112 PRECALL                  1
        # 1116 CALL                     1
        # 1126 PRECALL                  1
        # 1130 CALL                     1
        # 1140 POP_TOP
        # 569        1142 NOP
        # 570        1144 LOAD_FAST                0 (self)
        # 1146 LOAD_METHOD             22 (spawn)
        # 1168 LOAD_FAST                0 (self)
        # 1170 LOAD_ATTR               23 (linker)
        # 1180 BUILD_LIST               1
        # 1182 LOAD_FAST               19 (ld_args)
        # 1184 BINARY_OP                0 (+)
        # 1188 PRECALL                  1
        # 1192 CALL                     1
        # 1202 POP_TOP
        # 1204 LOAD_CONST               0 (None)
        # 1206 RETURN_VALUE
        # >> 1208 PUSH_EXC_INFO
        # 571        1210 LOAD_GLOBAL             48 (DistutilsExecError)
        # 1222 CHECK_EXC_MATCH
        # 1224 POP_JUMP_FORWARD_IF_FALSE    20 (to 1266)
        # 1226 STORE_FAST              23 (msg)
        # 572        1228 LOAD_GLOBAL             51 (NULL + LinkError)
        # 1240 LOAD_FAST               23 (msg)
        # 1242 PRECALL                  1
        # 1246 CALL                     1
        # 1256 RAISE_VARARGS            1
        # >> 1258 LOAD_CONST               0 (None)
        # 1260 STORE_FAST              23 (msg)
        # 1262 DELETE_FAST             23 (msg)
        # 1264 RERAISE                  1
        # 571     >> 1266 RERAISE                  0
        # >> 1268 COPY                     3
        # 1270 POP_EXCEPT
        # 1272 RERAISE                  1
        # 575     >> 1274 LOAD_GLOBAL             53 (NULL + log)
        # 1286 LOAD_ATTR               27 (debug)
        # 1296 LOAD_CONST               7 ('skipping %s (up-to-date)')
        # 1298 LOAD_FAST                3 (output_filename)
        # 1300 PRECALL                  2
        # 1304 CALL                     2
        # 1314 POP_TOP
        # 1316 LOAD_CONST               0 (None)
        # 1318 RETURN_VALUE
        # ExceptionTable:
        # 1144 to 1202 -> 1208 [0]
        # 1208 to 1226 -> 1268 [1] lasti
        # 1228 to 1256 -> 1258 [1] lasti
        # 1258 to 1266 -> 1268 [1] lasti

    def library_dir_option(self, dir):
        # 581           0 RESUME                   0
        # 582           2 LOAD_CONST               1 ('/LIBPATH:')
        # 4 LOAD_FAST                1 (dir)
        # 6 BINARY_OP                0 (+)
        # 10 RETURN_VALUE

    def runtime_library_dir_option(self, dir):
        # 584           0 RESUME                   0
        # 585           2 LOAD_GLOBAL              1 (NULL + DistutilsPlatformError)
        # 586          14 LOAD_CONST               1 ("don't know how to set runtime library search path for MSVC++")
        # 585          16 PRECALL                  1
        # 20 CALL                     1
        # 30 RAISE_VARARGS            1

    def library_option(self, lib):
        # 589           0 RESUME                   0
        # 590           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (library_filename)
        # 26 LOAD_FAST                1 (lib)
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 RETURN_VALUE

    def find_library_file(self, dirs, lib, debug):
        # 592           0 RESUME                   0
        # 595           2 LOAD_FAST                3 (debug)
        # 4 POP_JUMP_FORWARD_IF_FALSE     8 (to 22)
        # 596           6 LOAD_FAST                2 (lib)
        # 8 LOAD_CONST               1 ('_d')
        # 10 BINARY_OP                0 (+)
        # 14 LOAD_FAST                2 (lib)
        # 16 BUILD_LIST               2
        # 18 STORE_FAST               4 (try_names)
        # 20 JUMP_FORWARD             3 (to 28)
        # 598     >>   22 LOAD_FAST                2 (lib)
        # 24 BUILD_LIST               1
        # 26 STORE_FAST               4 (try_names)
        # 599     >>   28 LOAD_FAST                1 (dirs)
        # 30 GET_ITER
        # >>   32 FOR_ITER                95 (to 224)
        # 34 STORE_FAST               5 (dir)
        # 600          36 LOAD_FAST                4 (try_names)
        # 38 GET_ITER
        # >>   40 FOR_ITER                90 (to 222)
        # 42 STORE_FAST               6 (name)
        # 601          44 LOAD_GLOBAL              0 (os)
        # 56 LOAD_ATTR                1 (path)
        # 66 LOAD_METHOD              2 (join)
        # 88 LOAD_FAST                5 (dir)
        # 90 LOAD_FAST                0 (self)
        # 92 LOAD_METHOD              3 (library_filename)
        # 114 LOAD_FAST                6 (name)
        # 116 PRECALL                  1
        # 120 CALL                     1
        # 130 PRECALL                  2
        # 134 CALL                     2
        # 144 STORE_FAST               7 (libfile)
        # 602         146 LOAD_GLOBAL              0 (os)
        # 158 LOAD_ATTR                1 (path)
        # 168 LOAD_METHOD              4 (exists)
        # 190 LOAD_FAST                7 (libfile)
        # 192 PRECALL                  1
        # 196 CALL                     1
        # 206 POP_JUMP_FORWARD_IF_FALSE     6 (to 220)
        # 603         208 LOAD_FAST                7 (libfile)
        # 210 SWAP                     2
        # 212 POP_TOP
        # 214 SWAP                     2
        # 216 POP_TOP
        # 218 RETURN_VALUE
        # 602     >>  220 JUMP_BACKWARD           91 (to 40)
        # 600     >>  222 JUMP_BACKWARD           96 (to 32)
        # 606     >>  224 LOAD_CONST               0 (None)
        # 226 RETURN_VALUE

    def find_exe(self, exe):
        """Return path to an MSVC executable program.

        Tries to find the program in several places: first, one of the
        MSVC program search paths from the registry; next, the directories
        in the PATH environment variable.  If any of those work, return an
        absolute path that is known to exist.  If none of them work, just
        return the original program name, 'exe'.
        """
        # 610           0 RESUME                   0
        # 619           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_MSVCCompiler__paths)
        # 14 GET_ITER
        # >>   16 FOR_ITER                98 (to 214)
        # 18 STORE_FAST               2 (p)
        # 620          20 LOAD_GLOBAL              2 (os)
        # 32 LOAD_ATTR                2 (path)
        # 42 LOAD_METHOD              3 (join)
        # 64 LOAD_GLOBAL              2 (os)
        # 76 LOAD_ATTR                2 (path)
        # 86 LOAD_METHOD              4 (abspath)
        # 108 LOAD_FAST                2 (p)
        # 110 PRECALL                  1
        # 114 CALL                     1
        # 124 LOAD_FAST                1 (exe)
        # 126 PRECALL                  2
        # 130 CALL                     2
        # 140 STORE_FAST               3 (fn)
        # 621         142 LOAD_GLOBAL              2 (os)
        # 154 LOAD_ATTR                2 (path)
        # 164 LOAD_METHOD              5 (isfile)
        # 186 LOAD_FAST                3 (fn)
        # 188 PRECALL                  1
        # 192 CALL                     1
        # 202 POP_JUMP_FORWARD_IF_FALSE     4 (to 212)
        # 622         204 LOAD_FAST                3 (fn)
        # 206 SWAP                     2
        # 208 POP_TOP
        # 210 RETURN_VALUE
        # 621     >>  212 JUMP_BACKWARD           99 (to 16)
        # 625     >>  214 LOAD_GLOBAL              2 (os)
        # 226 LOAD_ATTR                6 (environ)
        # 236 LOAD_CONST               1 ('Path')
        # 238 BINARY_SUBSCR
        # 248 LOAD_METHOD              7 (split)
        # 270 LOAD_CONST               2 (';')
        # 272 PRECALL                  1
        # 276 CALL                     1
        # 286 GET_ITER
        # >>  288 FOR_ITER                98 (to 486)
        # 290 STORE_FAST               2 (p)
        # 626         292 LOAD_GLOBAL              2 (os)
        # 304 LOAD_ATTR                2 (path)
        # 314 LOAD_METHOD              3 (join)
        # 336 LOAD_GLOBAL              2 (os)
        # 348 LOAD_ATTR                2 (path)
        # 358 LOAD_METHOD              4 (abspath)
        # 380 LOAD_FAST                2 (p)
        # 382 PRECALL                  1
        # 386 CALL                     1
        # 396 LOAD_FAST                1 (exe)
        # 398 PRECALL                  2
        # 402 CALL                     2
        # 412 STORE_FAST               3 (fn)
        # 627         414 LOAD_GLOBAL              2 (os)
        # 426 LOAD_ATTR                2 (path)
        # 436 LOAD_METHOD              5 (isfile)
        # 458 LOAD_FAST                3 (fn)
        # 460 PRECALL                  1
        # 464 CALL                     1
        # 474 POP_JUMP_FORWARD_IF_FALSE     4 (to 484)
        # 628         476 LOAD_FAST                3 (fn)
        # 478 SWAP                     2
        # 480 POP_TOP
        # 482 RETURN_VALUE
        # 627     >>  484 JUMP_BACKWARD           99 (to 288)
        # 630     >>  486 LOAD_FAST                1 (exe)
        # 488 RETURN_VALUE

    def get_msvc_paths(self, path, platform):
        """Get a list of devstudio directories (include, lib or path).

        Return a list of strings.  The list will be empty if unable to
        access the registry or appropriate registry keys not found.
        """
        # 632           0 RESUME                   0
        # 638           2 LOAD_GLOBAL              0 (_can_read_reg)
        # 14 POP_JUMP_FORWARD_IF_TRUE     2 (to 20)
        # 639          16 BUILD_LIST               0
        # 18 RETURN_VALUE
        # 641     >>   20 LOAD_FAST                1 (path)
        # 22 LOAD_CONST               1 (' dirs')
        # 24 BINARY_OP                0 (+)
        # 28 STORE_FAST               1 (path)
        # 642          30 LOAD_FAST                0 (self)
        # 32 LOAD_ATTR                1 (_MSVCCompiler__version)
        # 42 LOAD_CONST               2 (7)
        # 44 COMPARE_OP               5 (>=)
        # 50 POP_JUMP_FORWARD_IF_FALSE    33 (to 118)
        # 643          52 LOAD_CONST               3 ('{}\\{:0.1f}\\VC\\VC_OBJECTS_PLATFORM_INFO\\Win32\\Directories')
        # 54 LOAD_METHOD              2 (format)
        # 644          76 LOAD_FAST                0 (self)
        # 78 LOAD_ATTR                3 (_MSVCCompiler__root)
        # 645          88 LOAD_FAST                0 (self)
        # 90 LOAD_ATTR                1 (_MSVCCompiler__version)
        # 643         100 PRECALL                  2
        # 104 CALL                     2
        # 114 STORE_FAST               3 (key)
        # 116 JUMP_FORWARD            13 (to 144)
        # 650     >>  118 LOAD_FAST                0 (self)
        # 120 LOAD_ATTR                3 (_MSVCCompiler__root)
        # 130 FORMAT_VALUE             1 (str)
        # 132 LOAD_CONST               4 ('\\6.0\\Build System\\Components\\Platforms\\Win32 (')
        # 134 LOAD_FAST                2 (platform)
        # 136 FORMAT_VALUE             1 (str)
        # 138 LOAD_CONST               5 (')\\Directories')
        # 649         140 BUILD_STRING             4
        # 648         142 STORE_FAST               3 (key)
        # 653     >>  144 LOAD_GLOBAL              8 (HKEYS)
        # 156 GET_ITER
        # >>  158 FOR_ITER               113 (to 386)
        # 160 STORE_FAST               4 (base)
        # 654         162 LOAD_GLOBAL             11 (NULL + read_values)
        # 174 LOAD_FAST                4 (base)
        # 176 LOAD_FAST                3 (key)
        # 178 PRECALL                  2
        # 182 CALL                     2
        # 192 STORE_FAST               5 (d)
        # 655         194 LOAD_FAST                5 (d)
        # 196 POP_JUMP_FORWARD_IF_FALSE    93 (to 384)
        # 656         198 LOAD_FAST                0 (self)
        # 200 LOAD_ATTR                1 (_MSVCCompiler__version)
        # 210 LOAD_CONST               2 (7)
        # 212 COMPARE_OP               5 (>=)
        # 218 POP_JUMP_FORWARD_IF_FALSE    53 (to 326)
        # 657         220 LOAD_FAST                0 (self)
        # 222 LOAD_ATTR                6 (_MSVCCompiler__macros)
        # 232 LOAD_METHOD              7 (sub)
        # 254 LOAD_FAST                5 (d)
        # 256 LOAD_FAST                1 (path)
        # 258 BINARY_SUBSCR
        # 268 PRECALL                  1
        # 272 CALL                     1
        # 282 LOAD_METHOD              8 (split)
        # 304 LOAD_CONST               6 (';')
        # 306 PRECALL                  1
        # 310 CALL                     1
        # 320 SWAP                     2
        # 322 POP_TOP
        # 324 RETURN_VALUE
        # 659     >>  326 LOAD_FAST                5 (d)
        # 328 LOAD_FAST                1 (path)
        # 330 BINARY_SUBSCR
        # 340 LOAD_METHOD              8 (split)
        # 362 LOAD_CONST               6 (';')
        # 364 PRECALL                  1
        # 368 CALL                     1
        # 378 SWAP                     2
        # 380 POP_TOP
        # 382 RETURN_VALUE
        # 655     >>  384 JUMP_BACKWARD          114 (to 158)
        # 662     >>  386 LOAD_FAST                0 (self)
        # 388 LOAD_ATTR                1 (_MSVCCompiler__version)
        # 398 LOAD_CONST               7 (6)
        # 400 COMPARE_OP               2 (==)
        # 406 POP_JUMP_FORWARD_IF_FALSE    57 (to 522)
        # 663         408 LOAD_GLOBAL              8 (HKEYS)
        # 420 GET_ITER
        # >>  422 FOR_ITER                49 (to 522)
        # 424 STORE_FAST               4 (base)
        # 664         426 LOAD_GLOBAL             11 (NULL + read_values)
        # 438 LOAD_FAST                4 (base)
        # 440 LOAD_CONST               8 ('%s\\6.0')
        # 442 LOAD_FAST                0 (self)
        # 444 LOAD_ATTR                3 (_MSVCCompiler__root)
        # 454 BINARY_OP                6 (%)
        # 458 PRECALL                  2
        # 462 CALL                     2
        # 472 POP_JUMP_FORWARD_IF_NONE    23 (to 520)
        # 665         474 LOAD_FAST                0 (self)
        # 476 LOAD_METHOD              9 (warn)
        # 666         498 LOAD_CONST              10 ('It seems you have Visual Studio 6 installed, but the expected registry settings are not present.\nYou must at least run the Visual Studio GUI once so that these entries are created.')
        # 665         500 PRECALL                  1
        # 504 CALL                     1
        # 514 POP_TOP
        # 671         516 POP_TOP
        # 518 JUMP_FORWARD             1 (to 522)
        # 664     >>  520 JUMP_BACKWARD           50 (to 422)
        # 672     >>  522 BUILD_LIST               0
        # 524 RETURN_VALUE

    def set_path_env_var(self, name):
        """Set environment variable 'name' to an MSVC path type value.

        This is equivalent to a SET command prior to execution of spawned
        commands.
        """
        # 674           0 RESUME                   0
        # 681           2 LOAD_FAST                1 (name)
        # 4 LOAD_CONST               1 ('lib')
        # 6 COMPARE_OP               2 (==)
        # 12 POP_JUMP_FORWARD_IF_FALSE    22 (to 58)
        # 682          14 LOAD_FAST                0 (self)
        # 16 LOAD_METHOD              0 (get_msvc_paths)
        # 38 LOAD_CONST               2 ('library')
        # 40 PRECALL                  1
        # 44 CALL                     1
        # 54 STORE_FAST               2 (p)
        # 56 JUMP_FORWARD            21 (to 100)
        # 684     >>   58 LOAD_FAST                0 (self)
        # 60 LOAD_METHOD              0 (get_msvc_paths)
        # 82 LOAD_FAST                1 (name)
        # 84 PRECALL                  1
        # 88 CALL                     1
        # 98 STORE_FAST               2 (p)
        # 685     >>  100 LOAD_FAST                2 (p)
        # 102 POP_JUMP_FORWARD_IF_FALSE    36 (to 176)
        # 686         104 LOAD_CONST               3 (';')
        # 106 LOAD_METHOD              1 (join)
        # 128 LOAD_FAST                2 (p)
        # 130 PRECALL                  1
        # 134 CALL                     1
        # 144 LOAD_GLOBAL              4 (os)
        # 156 LOAD_ATTR                3 (environ)
        # 166 LOAD_FAST                1 (name)
        # 168 STORE_SUBSCR
        # 172 LOAD_CONST               4 (None)
        # 174 RETURN_VALUE
        # 685     >>  176 LOAD_CONST               4 (None)
        # 178 RETURN_VALUE

