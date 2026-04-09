# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: setuptools\_vendor\typing_extensions.py

import abc
import collections
import collections.abc
import operator
import sys
import typing
from typing import GenericMeta
from _collections_abc import _check_methods
from typing import _collect_type_vars
from typing import _next_in_mro
from typing import _BaseGenericAlias
from typing import GenericAlias

def _no_slots_copy(dct):
    # 23           0 RESUME                   0
    # 24           2 LOAD_GLOBAL              1 (NULL + dict)
    # 14 LOAD_FAST                0 (dct)
    # 16 PRECALL                  1
    # 20 CALL                     1
    # 30 STORE_FAST               1 (dict_copy)
    # 25          32 LOAD_CONST               1 ('__slots__')
    # 34 LOAD_FAST                1 (dict_copy)
    # 36 CONTAINS_OP              0
    # 38 POP_JUMP_FORWARD_IF_FALSE    33 (to 106)
    # 26          40 LOAD_FAST                1 (dict_copy)
    # 42 LOAD_CONST               1 ('__slots__')
    # 44 BINARY_SUBSCR
    # 54 GET_ITER
    # >>   56 FOR_ITER                24 (to 106)
    # 58 STORE_FAST               2 (slot)
    # 27          60 LOAD_FAST                1 (dict_copy)
    # 62 LOAD_METHOD              1 (pop)
    # 84 LOAD_FAST                2 (slot)
    # 86 LOAD_CONST               0 (None)
    # 88 PRECALL                  2
    # 92 CALL                     2
    # 102 POP_TOP
    # 104 JUMP_BACKWARD           25 (to 56)
    # 28     >>  106 LOAD_FAST                1 (dict_copy)
    # 108 RETURN_VALUE

def _check_generic(cls, parameters):
    # 31           0 RESUME                   0
    # 32           2 LOAD_FAST                0 (cls)
    # 4 LOAD_ATTR                0 (__parameters__)
    # 14 POP_JUMP_FORWARD_IF_TRUE    18 (to 52)
    # 33          16 LOAD_GLOBAL              3 (NULL + TypeError)
    # 28 LOAD_FAST                0 (cls)
    # 30 FORMAT_VALUE             0
    # 32 LOAD_CONST               1 (' is not a generic class')
    # 34 BUILD_STRING             2
    # 36 PRECALL                  1
    # 40 CALL                     1
    # 50 RAISE_VARARGS            1
    # 34     >>   52 LOAD_GLOBAL              5 (NULL + len)
    # 64 LOAD_FAST                1 (parameters)
    # 66 PRECALL                  1
    # 70 CALL                     1
    # 80 STORE_FAST               2 (alen)
    # 35          82 LOAD_GLOBAL              5 (NULL + len)
    # 94 LOAD_FAST                0 (cls)
    # 96 LOAD_ATTR                0 (__parameters__)
    # 106 PRECALL                  1
    # 110 CALL                     1
    # 120 STORE_FAST               3 (elen)
    # 36         122 LOAD_FAST                2 (alen)
    # 124 LOAD_FAST                3 (elen)
    # 126 COMPARE_OP               3 (!=)
    # 132 POP_JUMP_FORWARD_IF_FALSE    35 (to 204)
    # 37         134 LOAD_GLOBAL              3 (NULL + TypeError)
    # 146 LOAD_CONST               2 ('Too ')
    # 148 LOAD_FAST                2 (alen)
    # 150 LOAD_FAST                3 (elen)
    # 152 COMPARE_OP               4 (>)
    # 158 POP_JUMP_FORWARD_IF_FALSE     2 (to 164)
    # 160 LOAD_CONST               3 ('many')
    # 162 JUMP_FORWARD             1 (to 166)
    # >>  164 LOAD_CONST               4 ('few')
    # >>  166 FORMAT_VALUE             0
    # 168 LOAD_CONST               5 (' arguments for ')
    # 170 LOAD_FAST                0 (cls)
    # 172 FORMAT_VALUE             0
    # 174 LOAD_CONST               6 ('; actual ')
    # 38         176 LOAD_FAST                2 (alen)
    # 37         178 FORMAT_VALUE             0
    # 180 LOAD_CONST               7 (', expected ')
    # 38         182 LOAD_FAST                3 (elen)
    # 37         184 FORMAT_VALUE             0
    # 186 BUILD_STRING             8
    # 188 PRECALL                  1
    # 192 CALL                     1
    # 202 RAISE_VARARGS            1
    # 36     >>  204 LOAD_CONST               0 (None)
    # 206 RETURN_VALUE

class _NoReturn:
    """_NoReturn"""
    def __instancecheck__(self, obj):
        # 109           0 RESUME                   0
        # 110           2 LOAD_GLOBAL              1 (NULL + TypeError)
        # 14 LOAD_CONST               1 ('NoReturn cannot be used with isinstance().')
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 RAISE_VARARGS            1

    def __subclasscheck__(self, cls):
        # 112           0 RESUME                   0
        # 113           2 LOAD_GLOBAL              1 (NULL + TypeError)
        # 14 LOAD_CONST               1 ('NoReturn cannot be used with issubclass().')
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 RAISE_VARARGS            1


class _FinalForm:
    """_FinalForm"""
    def __repr__(self):
        # 135           0 RESUME                   0
        # 136           2 LOAD_CONST               1 ('typing_extensions.')
        # 4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (_name)
        # 16 BINARY_OP                0 (+)
        # 20 RETURN_VALUE

    def __getitem__(self, parameters):
        # 138           0 RESUME                   0
        # 139           2 LOAD_GLOBAL              1 (NULL + typing)
        # 14 LOAD_ATTR                1 (_type_check)
        # 24 LOAD_FAST                1 (parameters)
        # 140          26 LOAD_FAST                0 (self)
        # 28 LOAD_ATTR                2 (_name)
        # 38 FORMAT_VALUE             0
        # 40 LOAD_CONST               1 (' accepts only single type')
        # 42 BUILD_STRING             2
        # 139          44 PRECALL                  2
        # 48 CALL                     2
        # 58 STORE_FAST               2 (item)
        # 141          60 LOAD_GLOBAL              1 (NULL + typing)
        # 72 LOAD_ATTR                3 (_GenericAlias)
        # 82 LOAD_FAST                0 (self)
        # 84 LOAD_FAST                2 (item)
        # 86 BUILD_TUPLE              1
        # 88 PRECALL                  2
        # 92 CALL                     2
        # 102 RETURN_VALUE


class _Final:
    """_Final"""
    def __init__(self, tp):
        # 177           0 RESUME                   0
        # 178           2 LOAD_FAST                1 (tp)
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (__type__)
        # 16 LOAD_CONST               0 (None)
        # 18 RETURN_VALUE

    def __getitem__(self, item):
        # 180           0 RESUME                   0
        # 181           2 LOAD_GLOBAL              1 (NULL + type)
        # 14 LOAD_FAST                0 (self)
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 STORE_FAST               2 (cls)
        # 182          32 LOAD_FAST                0 (self)
        # 34 LOAD_ATTR                1 (__type__)
        # 44 POP_JUMP_FORWARD_IF_NOT_NONE    48 (to 142)
        # 183          46 PUSH_NULL
        # 48 LOAD_FAST                2 (cls)
        # 50 LOAD_GLOBAL              5 (NULL + typing)
        # 62 LOAD_ATTR                3 (_type_check)
        # 72 LOAD_FAST                1 (item)
        # 184          74 LOAD_FAST                2 (cls)
        # 76 LOAD_ATTR                4 (__name__)
        # 86 LOAD_CONST               1 (1)
        # 88 LOAD_CONST               0 (None)
        # 90 BUILD_SLICE              2
        # 92 BINARY_SUBSCR
        # 102 FORMAT_VALUE             0
        # 104 LOAD_CONST               2 (' accepts only single type.')
        # 106 BUILD_STRING             2
        # 183         108 PRECALL                  2
        # 112 CALL                     2
        # 185         122 LOAD_CONST               3 (True)
        # 183         124 KW_NAMES                 4
        # 126 PRECALL                  2
        # 130 CALL                     2
        # 140 RETURN_VALUE
        # 186     >>  142 LOAD_GLOBAL             11 (NULL + TypeError)
        # 154 LOAD_FAST                2 (cls)
        # 156 LOAD_ATTR                4 (__name__)
        # 166 LOAD_CONST               1 (1)
        # 168 LOAD_CONST               0 (None)
        # 170 BUILD_SLICE              2
        # 172 BINARY_SUBSCR
        # 182 FORMAT_VALUE             0
        # 184 LOAD_CONST               5 (' cannot be further subscripted')
        # 186 BUILD_STRING             2
        # 188 PRECALL                  1
        # 192 CALL                     1
        # 202 RAISE_VARARGS            1

    def _eval_type(self, globalns, localns):
        # 188           0 RESUME                   0
        # 189           2 LOAD_GLOBAL              1 (NULL + typing)
        # 14 LOAD_ATTR                1 (_eval_type)
        # 24 LOAD_FAST                0 (self)
        # 26 LOAD_ATTR                2 (__type__)
        # 36 LOAD_FAST                1 (globalns)
        # 38 LOAD_FAST                2 (localns)
        # 40 PRECALL                  3
        # 44 CALL                     3
        # 54 STORE_FAST               3 (new_tp)
        # 190          56 LOAD_FAST                3 (new_tp)
        # 58 LOAD_FAST                0 (self)
        # 60 LOAD_ATTR                2 (__type__)
        # 70 COMPARE_OP               2 (==)
        # 76 POP_JUMP_FORWARD_IF_FALSE     2 (to 82)
        # 191          78 LOAD_FAST                0 (self)
        # 80 RETURN_VALUE
        # 192     >>   82 PUSH_NULL
        # 84 LOAD_GLOBAL              7 (NULL + type)
        # 96 LOAD_FAST                0 (self)
        # 98 PRECALL                  1
        # 102 CALL                     1
        # 112 LOAD_FAST                3 (new_tp)
        # 114 LOAD_CONST               1 (True)
        # 116 KW_NAMES                 2
        # 118 PRECALL                  2
        # 122 CALL                     2
        # 132 RETURN_VALUE

    def __repr__(self):
        # 0 COPY_FREE_VARS           1
        # 194           2 RESUME                   0
        # 195           4 LOAD_GLOBAL              1 (NULL + super)
        # 16 PRECALL                  0
        # 20 CALL                     0
        # 30 LOAD_METHOD              1 (__repr__)
        # 52 PRECALL                  0
        # 56 CALL                     0
        # 66 STORE_FAST               1 (r)
        # 196          68 LOAD_FAST                0 (self)
        # 70 LOAD_ATTR                2 (__type__)
        # 80 POP_JUMP_FORWARD_IF_NONE    32 (to 146)
        # 197          82 LOAD_FAST                1 (r)
        # 84 LOAD_CONST               1 ('[')
        # 86 LOAD_GLOBAL              7 (NULL + typing)
        # 98 LOAD_ATTR                4 (_type_repr)
        # 108 LOAD_FAST                0 (self)
        # 110 LOAD_ATTR                2 (__type__)
        # 120 PRECALL                  1
        # 124 CALL                     1
        # 134 FORMAT_VALUE             0
        # 136 LOAD_CONST               2 (']')
        # 138 BUILD_STRING             3
        # 140 BINARY_OP               13 (+=)
        # 144 STORE_FAST               1 (r)
        # 198     >>  146 LOAD_FAST                1 (r)
        # 148 RETURN_VALUE

    def __hash__(self):
        # 200           0 RESUME                   0
        # 201           2 LOAD_GLOBAL              1 (NULL + hash)
        # 14 LOAD_GLOBAL              3 (NULL + type)
        # 26 LOAD_FAST                0 (self)
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 LOAD_ATTR                2 (__name__)
        # 52 LOAD_FAST                0 (self)
        # 54 LOAD_ATTR                3 (__type__)
        # 64 BUILD_TUPLE              2
        # 66 PRECALL                  1
        # 70 CALL                     1
        # 80 RETURN_VALUE

    def __eq__(self, other):
        # 203           0 RESUME                   0
        # 204           2 LOAD_GLOBAL              1 (NULL + isinstance)
        # 14 LOAD_FAST                1 (other)
        # 16 LOAD_GLOBAL              2 (_Final)
        # 28 PRECALL                  2
        # 32 CALL                     2
        # 42 POP_JUMP_FORWARD_IF_TRUE     7 (to 58)
        # 205          44 LOAD_GLOBAL              4 (NotImplemented)
        # 56 RETURN_VALUE
        # 206     >>   58 LOAD_FAST                0 (self)
        # 60 LOAD_ATTR                3 (__type__)
        # 70 POP_JUMP_FORWARD_IF_NONE    16 (to 104)
        # 207          72 LOAD_FAST                0 (self)
        # 74 LOAD_ATTR                3 (__type__)
        # 84 LOAD_FAST                1 (other)
        # 86 LOAD_ATTR                3 (__type__)
        # 96 COMPARE_OP               2 (==)
        # 102 RETURN_VALUE
        # 208     >>  104 LOAD_FAST                0 (self)
        # 106 LOAD_FAST                1 (other)
        # 108 IS_OP                    0
        # 110 RETURN_VALUE


def final(f):
    """This decorator can be used to indicate to type checkers that
        the decorated method cannot be overridden, and decorated class
        cannot be subclassed. For example:

            class Base:
                @final
                def done(self) -> None:
                    ...
            class Sub(Base):
                def done(self) -> None:  # Error reported by type checker
                    ...
            @final
            class Leaf:
                ...
            class Other(Leaf):  # Error reported by type checker
                ...

        There is no runtime checking of these properties.
        """
    # 218           0 RESUME                   0
    # 238           2 LOAD_FAST                0 (f)
    # 4 RETURN_VALUE

def IntVar(name):
    # 241           0 RESUME                   0
    # 242           2 LOAD_GLOBAL              1 (NULL + typing)
    # 14 LOAD_ATTR                1 (TypeVar)
    # 24 LOAD_FAST                0 (name)
    # 26 PRECALL                  1
    # 30 CALL                     1
    # 40 RETURN_VALUE

class _LiteralForm:
    """_LiteralForm"""
    def __repr__(self):
        # 252           0 RESUME                   0
        # 253           2 LOAD_CONST               1 ('typing_extensions.')
        # 4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (_name)
        # 16 BINARY_OP                0 (+)
        # 20 RETURN_VALUE

    def __getitem__(self, parameters):
        # 255           0 RESUME                   0
        # 256           2 LOAD_GLOBAL              1 (NULL + typing)
        # 14 LOAD_ATTR                1 (_GenericAlias)
        # 24 LOAD_FAST                0 (self)
        # 26 LOAD_FAST                1 (parameters)
        # 28 PRECALL                  2
        # 32 CALL                     2
        # 42 RETURN_VALUE


class _Literal:
    """_Literal"""
    def __init__(self, values):
        # 289           0 RESUME                   0
        # 290           2 LOAD_FAST                1 (values)
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (__values__)
        # 16 LOAD_CONST               0 (None)
        # 18 RETURN_VALUE

    def __getitem__(self, values):
        # 292           0 RESUME                   0
        # 293           2 LOAD_GLOBAL              1 (NULL + type)
        # 14 LOAD_FAST                0 (self)
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 STORE_FAST               2 (cls)
        # 294          32 LOAD_FAST                0 (self)
        # 34 LOAD_ATTR                1 (__values__)
        # 44 POP_JUMP_FORWARD_IF_NOT_NONE    37 (to 120)
        # 295          46 LOAD_GLOBAL              5 (NULL + isinstance)
        # 58 LOAD_FAST                1 (values)
        # 60 LOAD_GLOBAL              6 (tuple)
        # 72 PRECALL                  2
        # 76 CALL                     2
        # 86 POP_JUMP_FORWARD_IF_TRUE     3 (to 94)
        # 296          88 LOAD_FAST                1 (values)
        # 90 BUILD_TUPLE              1
        # 92 STORE_FAST               1 (values)
        # 297     >>   94 PUSH_NULL
        # 96 LOAD_FAST                2 (cls)
        # 98 LOAD_FAST                1 (values)
        # 100 LOAD_CONST               1 (True)
        # 102 KW_NAMES                 2
        # 104 PRECALL                  2
        # 108 CALL                     2
        # 118 RETURN_VALUE
        # 298     >>  120 LOAD_GLOBAL              9 (NULL + TypeError)
        # 132 LOAD_FAST                2 (cls)
        # 134 LOAD_ATTR                5 (__name__)
        # 144 LOAD_CONST               3 (1)
        # 146 LOAD_CONST               0 (None)
        # 148 BUILD_SLICE              2
        # 150 BINARY_SUBSCR
        # 160 FORMAT_VALUE             0
        # 162 LOAD_CONST               4 (' cannot be further subscripted')
        # 164 BUILD_STRING             2
        # 166 PRECALL                  1
        # 170 CALL                     1
        # 180 RAISE_VARARGS            1

    def _eval_type(self, globalns, localns):
        # 300           0 RESUME                   0
        # 301           2 LOAD_FAST                0 (self)
        # 4 RETURN_VALUE

    def __repr__(self):
        # 0 COPY_FREE_VARS           1
        # 303           2 RESUME                   0
        # 304           4 LOAD_GLOBAL              1 (NULL + super)
        # 16 PRECALL                  0
        # 20 CALL                     0
        # 30 LOAD_METHOD              1 (__repr__)
        # 52 PRECALL                  0
        # 56 CALL                     0
        # 66 STORE_FAST               1 (r)
        # 305          68 LOAD_FAST                0 (self)
        # 70 LOAD_ATTR                2 (__values__)
        # 80 POP_JUMP_FORWARD_IF_NONE    57 (to 196)
        # 306          82 LOAD_FAST                1 (r)
        # 84 LOAD_CONST               1 ('[')
        # 86 LOAD_CONST               2 (', ')
        # 88 LOAD_METHOD              3 (join)
        # 110 LOAD_GLOBAL              9 (NULL + map)
        # 122 LOAD_GLOBAL             10 (typing)
        # 134 LOAD_ATTR                6 (_type_repr)
        # 144 LOAD_FAST                0 (self)
        # 146 LOAD_ATTR                2 (__values__)
        # 156 PRECALL                  2
        # 160 CALL                     2
        # 170 PRECALL                  1
        # 174 CALL                     1
        # 184 FORMAT_VALUE             0
        # 186 LOAD_CONST               3 (']')
        # 188 BUILD_STRING             3
        # 190 BINARY_OP               13 (+=)
        # 194 STORE_FAST               1 (r)
        # 307     >>  196 LOAD_FAST                1 (r)
        # 198 RETURN_VALUE

    def __hash__(self):
        # 309           0 RESUME                   0
        # 310           2 LOAD_GLOBAL              1 (NULL + hash)
        # 14 LOAD_GLOBAL              3 (NULL + type)
        # 26 LOAD_FAST                0 (self)
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 LOAD_ATTR                2 (__name__)
        # 52 LOAD_FAST                0 (self)
        # 54 LOAD_ATTR                3 (__values__)
        # 64 BUILD_TUPLE              2
        # 66 PRECALL                  1
        # 70 CALL                     1
        # 80 RETURN_VALUE

    def __eq__(self, other):
        # 312           0 RESUME                   0
        # 313           2 LOAD_GLOBAL              1 (NULL + isinstance)
        # 14 LOAD_FAST                1 (other)
        # 16 LOAD_GLOBAL              2 (_Literal)
        # 28 PRECALL                  2
        # 32 CALL                     2
        # 42 POP_JUMP_FORWARD_IF_TRUE     7 (to 58)
        # 314          44 LOAD_GLOBAL              4 (NotImplemented)
        # 56 RETURN_VALUE
        # 315     >>   58 LOAD_FAST                0 (self)
        # 60 LOAD_ATTR                3 (__values__)
        # 70 POP_JUMP_FORWARD_IF_NONE    16 (to 104)
        # 316          72 LOAD_FAST                0 (self)
        # 74 LOAD_ATTR                3 (__values__)
        # 84 LOAD_FAST                1 (other)
        # 86 LOAD_ATTR                3 (__values__)
        # 96 COMPARE_OP               2 (==)
        # 102 RETURN_VALUE
        # 317     >>  104 LOAD_FAST                0 (self)
        # 106 LOAD_FAST                1 (other)
        # 108 IS_OP                    0
        # 110 RETURN_VALUE


class _ExtensionsGenericMeta:
    """_ExtensionsGenericMeta"""
    def __subclasscheck__(self, subclass):
        """This mimics a more modern GenericMeta.__subclasscheck__() logic
        (that does not have problems with recursion) to work around interactions
        between collections, typing, and typing_extensions on older
        versions of Python, see https://github.com/python/typing/issues/501.
        """
        # 0 COPY_FREE_VARS           1
        # 334           2 RESUME                   0
        # 340           4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (__origin__)
        # 16 POP_JUMP_FORWARD_IF_NONE    50 (to 118)
        # 341          18 LOAD_GLOBAL              3 (NULL + sys)
        # 30 LOAD_ATTR                2 (_getframe)
        # 40 LOAD_CONST               2 (1)
        # 42 PRECALL                  1
        # 46 CALL                     1
        # 56 LOAD_ATTR                3 (f_globals)
        # 66 LOAD_CONST               3 ('__name__')
        # 68 BINARY_SUBSCR
        # 78 LOAD_CONST               4 (('abc', 'functools'))
        # 80 CONTAINS_OP              1
        # 82 POP_JUMP_FORWARD_IF_FALSE    15 (to 114)
        # 342          84 LOAD_GLOBAL              9 (NULL + TypeError)
        # 96 LOAD_CONST               5 ('Parameterized generics cannot be used with class or instance checks')
        # 98 PRECALL                  1
        # 102 CALL                     1
        # 112 RAISE_VARARGS            1
        # 344     >>  114 LOAD_CONST               6 (False)
        # 116 RETURN_VALUE
        # 345     >>  118 LOAD_FAST                0 (self)
        # 120 LOAD_ATTR                5 (__extra__)
        # 130 POP_JUMP_FORWARD_IF_TRUE    33 (to 198)
        # 346         132 LOAD_GLOBAL             13 (NULL + super)
        # 144 PRECALL                  0
        # 148 CALL                     0
        # 158 LOAD_METHOD              7 (__subclasscheck__)
        # 180 LOAD_FAST                1 (subclass)
        # 182 PRECALL                  1
        # 186 CALL                     1
        # 196 RETURN_VALUE
        # 347     >>  198 LOAD_FAST                0 (self)
        # 200 LOAD_ATTR                5 (__extra__)
        # 210 LOAD_METHOD              8 (__subclasshook__)
        # 232 LOAD_FAST                1 (subclass)
        # 234 PRECALL                  1
        # 238 CALL                     1
        # 248 STORE_FAST               2 (res)
        # 348         250 LOAD_FAST                2 (res)
        # 252 LOAD_GLOBAL             18 (NotImplemented)
        # 264 IS_OP                    1
        # 266 POP_JUMP_FORWARD_IF_FALSE     2 (to 272)
        # 349         268 LOAD_FAST                2 (res)
        # 270 RETURN_VALUE
        # 350     >>  272 LOAD_FAST                0 (self)
        # 274 LOAD_ATTR                5 (__extra__)
        # 284 LOAD_FAST                1 (subclass)
        # 286 LOAD_ATTR               10 (__mro__)
        # 296 CONTAINS_OP              0
        # 298 POP_JUMP_FORWARD_IF_FALSE     2 (to 304)
        # 351         300 LOAD_CONST               7 (True)
        # 302 RETURN_VALUE
        # 352     >>  304 LOAD_FAST                0 (self)
        # 306 LOAD_ATTR                5 (__extra__)
        # 316 LOAD_METHOD             11 (__subclasses__)
        # 338 PRECALL                  0
        # 342 CALL                     0
        # 352 GET_ITER
        # >>  354 FOR_ITER                43 (to 442)
        # 356 STORE_FAST               3 (scls)
        # 353         358 LOAD_GLOBAL             25 (NULL + isinstance)
        # 370 LOAD_FAST                3 (scls)
        # 372 LOAD_GLOBAL             26 (GenericMeta)
        # 384 PRECALL                  2
        # 388 CALL                     2
        # 398 POP_JUMP_FORWARD_IF_FALSE     1 (to 402)
        # 354         400 JUMP_BACKWARD           24 (to 354)
        # 355     >>  402 LOAD_GLOBAL             29 (NULL + issubclass)
        # 414 LOAD_FAST                1 (subclass)
        # 416 LOAD_FAST                3 (scls)
        # 418 PRECALL                  2
        # 422 CALL                     2
        # 432 POP_JUMP_FORWARD_IF_FALSE     3 (to 440)
        # 356         434 POP_TOP
        # 436 LOAD_CONST               7 (True)
        # 438 RETURN_VALUE
        # 355     >>  440 JUMP_BACKWARD           44 (to 354)
        # 357     >>  442 LOAD_CONST               6 (False)
        # 444 RETURN_VALUE


class Deque:
    """Deque"""
    def __new__(cls):
        # 375           0 RESUME                   0
        # 376           2 LOAD_FAST                0 (cls)
        # 4 LOAD_ATTR                0 (_gorg)
        # 14 LOAD_GLOBAL              2 (Deque)
        # 26 IS_OP                    0
        # 28 POP_JUMP_FORWARD_IF_FALSE    17 (to 64)
        # 377          30 LOAD_GLOBAL              5 (NULL + collections)
        # 42 LOAD_ATTR                3 (deque)
        # 52 LOAD_FAST                1 (args)
        # 54 BUILD_MAP                0
        # 56 LOAD_FAST                2 (kwds)
        # 58 DICT_MERGE               1
        # 60 CALL_FUNCTION_EX         1
        # 62 RETURN_VALUE
        # 378     >>   64 LOAD_GLOBAL              9 (NULL + typing)
        # 76 LOAD_ATTR                5 (_generic_new)
        # 86 LOAD_GLOBAL              4 (collections)
        # 98 LOAD_ATTR                3 (deque)
        # 108 LOAD_FAST                0 (cls)
        # 110 BUILD_LIST               2
        # 112 LOAD_FAST                1 (args)
        # 114 LIST_EXTEND              1
        # 116 LIST_TO_TUPLE
        # 118 BUILD_MAP                0
        # 120 LOAD_FAST                2 (kwds)
        # 122 DICT_MERGE               1
        # 124 CALL_FUNCTION_EX         1
        # 126 RETURN_VALUE


class AsyncContextManager:
    """AsyncContextManager"""
    def __aenter__(self):
        # 391           0 RETURN_GENERATOR
        # 2 POP_TOP
        # 4 RESUME                   0
        # 392           6 LOAD_FAST                0 (self)
        # 8 RETURN_VALUE

    def __aexit__(self, exc_type, exc_value, traceback):
        # 394           0 RETURN_GENERATOR
        # 2 POP_TOP
        # 4 RESUME                   0
        # 396           6 LOAD_CONST               0 (None)
        # 8 RETURN_VALUE

    def __subclasshook__(cls, C):
        # 398           0 RESUME                   0
        # 400           2 LOAD_FAST                0 (cls)
        # 4 LOAD_GLOBAL              0 (AsyncContextManager)
        # 16 IS_OP                    0
        # 18 POP_JUMP_FORWARD_IF_FALSE    17 (to 54)
        # 401          20 LOAD_GLOBAL              3 (NULL + _check_methods_in_mro)
        # 32 LOAD_FAST                1 (C)
        # 34 LOAD_CONST               1 ('__aenter__')
        # 36 LOAD_CONST               2 ('__aexit__')
        # 38 PRECALL                  3
        # 42 CALL                     3
        # 52 RETURN_VALUE
        # 402     >>   54 LOAD_GLOBAL              4 (NotImplemented)
        # 66 RETURN_VALUE


class OrderedDict:
    """OrderedDict"""
    def __new__(cls):
        # 420           0 RESUME                   0
        # 421           2 LOAD_FAST                0 (cls)
        # 4 LOAD_ATTR                0 (_gorg)
        # 14 LOAD_GLOBAL              2 (OrderedDict)
        # 26 IS_OP                    0
        # 28 POP_JUMP_FORWARD_IF_FALSE    17 (to 64)
        # 422          30 LOAD_GLOBAL              5 (NULL + collections)
        # 42 LOAD_ATTR                1 (OrderedDict)
        # 52 LOAD_FAST                1 (args)
        # 54 BUILD_MAP                0
        # 56 LOAD_FAST                2 (kwds)
        # 58 DICT_MERGE               1
        # 60 CALL_FUNCTION_EX         1
        # 62 RETURN_VALUE
        # 423     >>   64 LOAD_GLOBAL              7 (NULL + typing)
        # 76 LOAD_ATTR                4 (_generic_new)
        # 86 LOAD_GLOBAL              4 (collections)
        # 98 LOAD_ATTR                1 (OrderedDict)
        # 108 LOAD_FAST                0 (cls)
        # 110 BUILD_LIST               2
        # 112 LOAD_FAST                1 (args)
        # 114 LIST_EXTEND              1
        # 116 LIST_TO_TUPLE
        # 118 BUILD_MAP                0
        # 120 LOAD_FAST                2 (kwds)
        # 122 DICT_MERGE               1
        # 124 CALL_FUNCTION_EX         1
        # 126 RETURN_VALUE


class Counter:
    """Counter"""
    def __new__(cls):
        # 436           0 RESUME                   0
        # 437           2 LOAD_FAST                0 (cls)
        # 4 LOAD_ATTR                0 (_gorg)
        # 14 LOAD_GLOBAL              2 (Counter)
        # 26 IS_OP                    0
        # 28 POP_JUMP_FORWARD_IF_FALSE    17 (to 64)
        # 438          30 LOAD_GLOBAL              5 (NULL + collections)
        # 42 LOAD_ATTR                1 (Counter)
        # 52 LOAD_FAST                1 (args)
        # 54 BUILD_MAP                0
        # 56 LOAD_FAST                2 (kwds)
        # 58 DICT_MERGE               1
        # 60 CALL_FUNCTION_EX         1
        # 62 RETURN_VALUE
        # 439     >>   64 LOAD_GLOBAL              7 (NULL + typing)
        # 76 LOAD_ATTR                4 (_generic_new)
        # 86 LOAD_GLOBAL              4 (collections)
        # 98 LOAD_ATTR                1 (Counter)
        # 108 LOAD_FAST                0 (cls)
        # 110 BUILD_LIST               2
        # 112 LOAD_FAST                1 (args)
        # 114 LIST_EXTEND              1
        # 116 LIST_TO_TUPLE
        # 118 BUILD_MAP                0
        # 120 LOAD_FAST                2 (kwds)
        # 122 DICT_MERGE               1
        # 124 CALL_FUNCTION_EX         1
        # 126 RETURN_VALUE


class ChainMap:
    """ChainMap"""
    def __new__(cls):
        # 451           0 RESUME                   0
        # 452           2 LOAD_FAST                0 (cls)
        # 4 LOAD_ATTR                0 (_gorg)
        # 14 LOAD_GLOBAL              2 (ChainMap)
        # 26 IS_OP                    0
        # 28 POP_JUMP_FORWARD_IF_FALSE    17 (to 64)
        # 453          30 LOAD_GLOBAL              5 (NULL + collections)
        # 42 LOAD_ATTR                1 (ChainMap)
        # 52 LOAD_FAST                1 (args)
        # 54 BUILD_MAP                0
        # 56 LOAD_FAST                2 (kwds)
        # 58 DICT_MERGE               1
        # 60 CALL_FUNCTION_EX         1
        # 62 RETURN_VALUE
        # 454     >>   64 LOAD_GLOBAL              7 (NULL + typing)
        # 76 LOAD_ATTR                4 (_generic_new)
        # 86 LOAD_GLOBAL              4 (collections)
        # 98 LOAD_ATTR                1 (ChainMap)
        # 108 LOAD_FAST                0 (cls)
        # 110 BUILD_LIST               2
        # 112 LOAD_FAST                1 (args)
        # 114 LIST_EXTEND              1
        # 116 LIST_TO_TUPLE
        # 118 BUILD_MAP                0
        # 120 LOAD_FAST                2 (kwds)
        # 122 DICT_MERGE               1
        # 124 CALL_FUNCTION_EX         1
        # 126 RETURN_VALUE


class AsyncGenerator:
    """AsyncGenerator"""

def _gorg(cls):
    """This function exists for compatibility with old typing versions."""
    # 471           0 RESUME                   0
    # 473           2 LOAD_GLOBAL              1 (NULL + isinstance)
    # 14 LOAD_FAST                0 (cls)
    # 16 LOAD_GLOBAL              2 (GenericMeta)
    # 28 PRECALL                  2
    # 32 CALL                     2
    # 42 POP_JUMP_FORWARD_IF_TRUE     2 (to 48)
    # 44 LOAD_ASSERTION_ERROR
    # 46 RAISE_VARARGS            1
    # 474     >>   48 LOAD_GLOBAL              5 (NULL + hasattr)
    # 60 LOAD_FAST                0 (cls)
    # 62 LOAD_CONST               1 ('_gorg')
    # 64 PRECALL                  2
    # 68 CALL                     2
    # 78 POP_JUMP_FORWARD_IF_FALSE     7 (to 94)
    # 475          80 LOAD_FAST                0 (cls)
    # 82 LOAD_ATTR                3 (_gorg)
    # 92 RETURN_VALUE
    # 476     >>   94 LOAD_FAST                0 (cls)
    # 96 LOAD_ATTR                4 (__origin__)
    # 106 POP_JUMP_FORWARD_IF_NONE    14 (to 136)
    # 477     >>  108 LOAD_FAST                0 (cls)
    # 110 LOAD_ATTR                4 (__origin__)
    # 120 STORE_FAST               0 (cls)
    # 476         122 LOAD_FAST                0 (cls)
    # 124 LOAD_ATTR                4 (__origin__)
    # 134 POP_JUMP_BACKWARD_IF_NOT_NONE    14 (to 108)
    # 478     >>  136 LOAD_FAST                0 (cls)
    # 138 RETURN_VALUE

def _get_protocol_attrs(cls):
    # 487           0 RESUME                   0
    # 488           2 LOAD_GLOBAL              1 (NULL + set)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 STORE_FAST               1 (attrs)
    # 489          30 LOAD_FAST                0 (cls)
    # 32 LOAD_ATTR                1 (__mro__)
    # 42 LOAD_CONST               0 (None)
    # 44 LOAD_CONST               1 (-1)
    # 46 BUILD_SLICE              2
    # 48 BINARY_SUBSCR
    # 58 GET_ITER
    # >>   60 FOR_ITER               150 (to 362)
    # 62 STORE_FAST               2 (base)
    # 490          64 LOAD_FAST                2 (base)
    # 66 LOAD_ATTR                2 (__name__)
    # 76 LOAD_CONST               2 (('Protocol', 'Generic'))
    # 78 CONTAINS_OP              0
    # 80 POP_JUMP_FORWARD_IF_FALSE     1 (to 84)
    # 491          82 JUMP_BACKWARD           12 (to 60)
    # 492     >>   84 LOAD_GLOBAL              7 (NULL + getattr)
    # 96 LOAD_FAST                2 (base)
    # 98 LOAD_CONST               3 ('__annotations__')
    # 100 BUILD_MAP                0
    # 102 PRECALL                  3
    # 106 CALL                     3
    # 116 STORE_FAST               3 (annotations)
    # 493         118 LOAD_GLOBAL              9 (NULL + list)
    # 130 LOAD_FAST                2 (base)
    # 132 LOAD_ATTR                5 (__dict__)
    # 142 LOAD_METHOD              6 (keys)
    # 164 PRECALL                  0
    # 168 CALL                     0
    # 178 PRECALL                  1
    # 182 CALL                     1
    # 192 LOAD_GLOBAL              9 (NULL + list)
    # 204 LOAD_FAST                3 (annotations)
    # 206 LOAD_METHOD              6 (keys)
    # 228 PRECALL                  0
    # 232 CALL                     0
    # 242 PRECALL                  1
    # 246 CALL                     1
    # 256 BINARY_OP                0 (+)
    # 260 GET_ITER
    # >>  262 FOR_ITER                48 (to 360)
    # 264 STORE_FAST               4 (attr)
    # 494         266 LOAD_FAST                4 (attr)
    # 268 LOAD_METHOD              7 (startswith)
    # 290 LOAD_CONST               4 ('_abc_')
    # 292 PRECALL                  1
    # 296 CALL                     1
    # 306 POP_JUMP_FORWARD_IF_TRUE    25 (to 358)
    # 308 LOAD_FAST                4 (attr)
    # 310 LOAD_CONST               5 (('__abstractmethods__', '__annotations__', '__weakref__', '_is_protocol', '_is_runtime_protocol', '__dict__', '__args__', '__slots__', '__next_in_mro__', '__parameters__', '__origin__', '__orig_bases__', '__extra__', '__tree_hash__', '__doc__', '__subclasshook__', '__init__', '__new__', '__module__', '_MutableMapping__marker', '_gorg'))
    # 312 CONTAINS_OP              1
    # 314 POP_JUMP_FORWARD_IF_FALSE    21 (to 358)
    # 502         316 LOAD_FAST                1 (attrs)
    # 318 LOAD_METHOD              8 (add)
    # 340 LOAD_FAST                4 (attr)
    # 342 PRECALL                  1
    # 346 CALL                     1
    # 356 POP_TOP
    # >>  358 JUMP_BACKWARD           49 (to 262)
    # 493     >>  360 JUMP_BACKWARD          151 (to 60)
    # 503     >>  362 LOAD_FAST                1 (attrs)
    # 364 RETURN_VALUE

def _is_callable_members_only(cls):
    # 0 MAKE_CELL                0 (cls)
    # 506           2 RESUME                   0
    # 507           4 LOAD_GLOBAL              1 (NULL + all)
    # 16 LOAD_CLOSURE             0 (cls)
    # 18 BUILD_TUPLE              1
    # 20 LOAD_CONST               1 (<code object <genexpr> at 0x000001EBD7E45F00, file "setuptools\_vendor\typing_extensions.py", line 507>)
    # 22 MAKE_FUNCTION            8 (closure)
    # 24 LOAD_GLOBAL              3 (NULL + _get_protocol_attrs)
    # 36 LOAD_DEREF               0 (cls)
    # 38 PRECALL                  1
    # 42 CALL                     1
    # 52 GET_ITER
    # 54 PRECALL                  0
    # 58 CALL                     0
    # 68 PRECALL                  1
    # 72 CALL                     1
    # 82 RETURN_VALUE
    # Disassembly of <code object <genexpr> at 0x000001EBD7E45F00, file "setuptools\_vendor\typing_extensions.py", line 507>:
    # 0 COPY_FREE_VARS           1
    # 507           2 RETURN_GENERATOR
    # 4 POP_TOP
    # 6 RESUME                   0
    # 8 LOAD_FAST                0 (.0)
    # >>   10 FOR_ITER                34 (to 80)
    # 12 STORE_FAST               1 (attr)
    # 14 LOAD_GLOBAL              1 (NULL + callable)
    # 26 LOAD_GLOBAL              3 (NULL + getattr)
    # 38 LOAD_DEREF               2 (cls)
    # 40 LOAD_FAST                1 (attr)
    # 42 LOAD_CONST               0 (None)
    # 44 PRECALL                  3
    # 48 CALL                     3
    # 58 PRECALL                  1
    # 62 CALL                     1
    # 72 YIELD_VALUE
    # 74 RESUME                   1
    # 76 POP_TOP
    # 78 JUMP_BACKWARD           35 (to 10)
    # >>   80 LOAD_CONST               0 (None)
    # 82 RETURN_VALUE

def _no_init(self):
    # 517           0 RESUME                   0
    # 518           2 LOAD_GLOBAL              1 (NULL + type)
    # 14 LOAD_FAST                0 (self)
    # 16 PRECALL                  1
    # 20 CALL                     1
    # 30 LOAD_ATTR                1 (_is_protocol)
    # 40 POP_JUMP_FORWARD_IF_FALSE    15 (to 72)
    # 519          42 LOAD_GLOBAL              5 (NULL + TypeError)
    # 54 LOAD_CONST               1 ('Protocols cannot be instantiated')
    # 56 PRECALL                  1
    # 60 CALL                     1
    # 70 RAISE_VARARGS            1
    # 518     >>   72 LOAD_CONST               0 (None)
    # 74 RETURN_VALUE

class _ProtocolMeta:
    """_ProtocolMeta"""
    def __instancecheck__(cls, instance):
        # 0 COPY_FREE_VARS           1
        # 2 MAKE_CELL                0 (cls)
        # 4 MAKE_CELL                1 (instance)
        # 524           6 RESUME                   0
        # 527           8 LOAD_GLOBAL              1 (NULL + getattr)
        # 20 LOAD_DEREF               0 (cls)
        # 22 LOAD_CONST               1 ('_is_protocol')
        # 24 LOAD_CONST               2 (False)
        # 26 PRECALL                  3
        # 30 CALL                     3
        # 40 POP_JUMP_FORWARD_IF_FALSE    15 (to 72)
        # 528          42 LOAD_GLOBAL              3 (NULL + _is_callable_members_only)
        # 54 LOAD_DEREF               0 (cls)
        # 56 PRECALL                  1
        # 60 CALL                     1
        # 527          70 POP_JUMP_FORWARD_IF_FALSE    23 (to 118)
        # 529     >>   72 LOAD_GLOBAL              5 (NULL + issubclass)
        # 84 LOAD_DEREF               1 (instance)
        # 86 LOAD_ATTR                3 (__class__)
        # 96 LOAD_DEREF               0 (cls)
        # 98 PRECALL                  2
        # 102 CALL                     2
        # 527         112 POP_JUMP_FORWARD_IF_FALSE     2 (to 118)
        # 530         114 LOAD_CONST               3 (True)
        # 116 RETURN_VALUE
        # 531     >>  118 LOAD_DEREF               0 (cls)
        # 120 LOAD_ATTR                4 (_is_protocol)
        # 130 POP_JUMP_FORWARD_IF_FALSE    43 (to 218)
        # 532         132 LOAD_GLOBAL             11 (NULL + all)
        # 144 LOAD_CLOSURE             0 (cls)
        # 146 LOAD_CLOSURE             1 (instance)
        # 148 BUILD_TUPLE              2
        # 150 LOAD_CONST               4 (<code object <genexpr> at 0x000001EBD72CB9F0, file "setuptools\_vendor\typing_extensions.py", line 532>)
        # 152 MAKE_FUNCTION            8 (closure)
        # 535         154 LOAD_GLOBAL             13 (NULL + _get_protocol_attrs)
        # 166 LOAD_DEREF               0 (cls)
        # 168 PRECALL                  1
        # 172 CALL                     1
        # 532         182 GET_ITER
        # 184 PRECALL                  0
        # 188 CALL                     0
        # 198 PRECALL                  1
        # 202 CALL                     1
        # 212 POP_JUMP_FORWARD_IF_FALSE     2 (to 218)
        # 536         214 LOAD_CONST               3 (True)
        # 216 RETURN_VALUE
        # 537     >>  218 LOAD_GLOBAL             15 (NULL + super)
        # 230 PRECALL                  0
        # 234 CALL                     0
        # 244 LOAD_METHOD              8 (__instancecheck__)
        # 266 LOAD_DEREF               1 (instance)
        # 268 PRECALL                  1
        # 272 CALL                     1
        # 282 RETURN_VALUE
        # Disassembly of <code object <genexpr> at 0x000001EBD72CB9F0, file "setuptools\_vendor\typing_extensions.py", line 532>:
        # 0 COPY_FREE_VARS           2
        # 532           2 RETURN_GENERATOR
        # 4 POP_TOP
        # 6 RESUME                   0
        # 8 LOAD_FAST                0 (.0)
        # >>   10 FOR_ITER                69 (to 150)
        # 535          12 STORE_FAST               1 (attr)
        # 532          14 LOAD_GLOBAL              1 (NULL + hasattr)
        # 26 LOAD_DEREF               3 (instance)
        # 28 LOAD_FAST                1 (attr)
        # 30 PRECALL                  2
        # 34 CALL                     2
        # 44 JUMP_IF_FALSE_OR_POP    48 (to 142)
        # 533          46 LOAD_GLOBAL              3 (NULL + callable)
        # 58 LOAD_GLOBAL              5 (NULL + getattr)
        # 70 LOAD_DEREF               2 (cls)
        # 72 LOAD_FAST                1 (attr)
        # 74 LOAD_CONST               0 (None)
        # 76 PRECALL                  3
        # 80 CALL                     3
        # 90 PRECALL                  1
        # 94 CALL                     1
        # 104 UNARY_NOT
        # 106 JUMP_IF_TRUE_OR_POP     17 (to 142)
        # 534         108 LOAD_GLOBAL              5 (NULL + getattr)
        # 120 LOAD_DEREF               3 (instance)
        # 122 LOAD_FAST                1 (attr)
        # 124 PRECALL                  2
        # 128 CALL                     2
        # 138 LOAD_CONST               0 (None)
        # 140 IS_OP                    1
        # 532     >>  142 YIELD_VALUE
        # 144 RESUME                   1
        # 146 POP_TOP
        # 148 JUMP_BACKWARD           70 (to 10)
        # >>  150 LOAD_CONST               0 (None)
        # 152 RETURN_VALUE


class Protocol:
    """Protocol"""
    def __new__(cls):
        # 0 COPY_FREE_VARS           1
        # 574           2 RESUME                   0
        # 575           4 LOAD_FAST                0 (cls)
        # 6 LOAD_GLOBAL              0 (Protocol)
        # 18 IS_OP                    0
        # 20 POP_JUMP_FORWARD_IF_FALSE    15 (to 52)
        # 576          22 LOAD_GLOBAL              3 (NULL + TypeError)
        # 34 LOAD_CONST               1 ('Type Protocol cannot be instantiated; it can only be used as a base class')
        # 36 PRECALL                  1
        # 40 CALL                     1
        # 50 RAISE_VARARGS            1
        # 578     >>   52 LOAD_GLOBAL              5 (NULL + super)
        # 64 PRECALL                  0
        # 68 CALL                     0
        # 78 LOAD_METHOD              3 (__new__)
        # 100 LOAD_FAST                0 (cls)
        # 102 PRECALL                  1
        # 106 CALL                     1
        # 116 RETURN_VALUE

    def __class_getitem__(cls, params):
        # 0 MAKE_CELL                3 (msg)
        # 580           2 RESUME                   0
        # 582           4 LOAD_GLOBAL              1 (NULL + isinstance)
        # 16 LOAD_FAST                1 (params)
        # 18 LOAD_GLOBAL              2 (tuple)
        # 30 PRECALL                  2
        # 34 CALL                     2
        # 44 POP_JUMP_FORWARD_IF_TRUE     3 (to 52)
        # 583          46 LOAD_FAST                1 (params)
        # 48 BUILD_TUPLE              1
        # 50 STORE_FAST               1 (params)
        # 584     >>   52 LOAD_FAST                1 (params)
        # 54 POP_JUMP_FORWARD_IF_TRUE    38 (to 132)
        # 56 LOAD_FAST                0 (cls)
        # 58 LOAD_GLOBAL              4 (typing)
        # 70 LOAD_ATTR                3 (Tuple)
        # 80 IS_OP                    1
        # 82 POP_JUMP_FORWARD_IF_FALSE    24 (to 132)
        # 585          84 LOAD_GLOBAL              9 (NULL + TypeError)
        # 586          96 LOAD_CONST               1 ('Parameter list to ')
        # 98 LOAD_FAST                0 (cls)
        # 100 LOAD_ATTR                5 (__qualname__)
        # 110 FORMAT_VALUE             0
        # 112 LOAD_CONST               2 ('[...] cannot be empty')
        # 114 BUILD_STRING             3
        # 585         116 PRECALL                  1
        # 120 CALL                     1
        # 130 RAISE_VARARGS            1
        # 587     >>  132 LOAD_CONST               3 ('Parameters to generic types must be types.')
        # 134 STORE_DEREF              3 (msg)
        # 588         136 LOAD_GLOBAL              3 (NULL + tuple)
        # 148 LOAD_CLOSURE             3 (msg)
        # 150 BUILD_TUPLE              1
        # 152 LOAD_CONST               4 (<code object <genexpr> at 0x000001EBD7DF0830, file "setuptools\_vendor\typing_extensions.py", line 588>)
        # 154 MAKE_FUNCTION            8 (closure)
        # 156 LOAD_FAST                1 (params)
        # 158 GET_ITER
        # 160 PRECALL                  0
        # 164 CALL                     0
        # 174 PRECALL                  1
        # 178 CALL                     1
        # 188 STORE_FAST               1 (params)
        # 589         190 LOAD_FAST                0 (cls)
        # 192 LOAD_GLOBAL             12 (Protocol)
        # 204 IS_OP                    0
        # 206 POP_JUMP_FORWARD_IF_FALSE   187 (to 582)
        # 591         208 LOAD_GLOBAL             15 (NULL + all)
        # 220 LOAD_CONST               5 (<code object <genexpr> at 0x000001EBD7E46230, file "setuptools\_vendor\typing_extensions.py", line 591>)
        # 222 MAKE_FUNCTION            0
        # 224 LOAD_FAST                1 (params)
        # 226 GET_ITER
        # 228 PRECALL                  0
        # 232 CALL                     0
        # 242 PRECALL                  1
        # 246 CALL                     1
        # 256 POP_JUMP_FORWARD_IF_TRUE   101 (to 460)
        # 592         258 LOAD_CONST               6 (0)
        # 260 STORE_FAST               2 (i)
        # 593         262 LOAD_GLOBAL              1 (NULL + isinstance)
        # 274 LOAD_FAST                1 (params)
        # 276 LOAD_FAST                2 (i)
        # 278 BINARY_SUBSCR
        # 288 LOAD_GLOBAL              4 (typing)
        # 300 LOAD_ATTR                8 (TypeVar)
        # 310 PRECALL                  2
        # 314 CALL                     2
        # 324 POP_JUMP_FORWARD_IF_FALSE    37 (to 400)
        # 594     >>  326 LOAD_FAST                2 (i)
        # 328 LOAD_CONST               7 (1)
        # 330 BINARY_OP               13 (+=)
        # 334 STORE_FAST               2 (i)
        # 593         336 LOAD_GLOBAL              1 (NULL + isinstance)
        # 348 LOAD_FAST                1 (params)
        # 350 LOAD_FAST                2 (i)
        # 352 BINARY_SUBSCR
        # 362 LOAD_GLOBAL              4 (typing)
        # 374 LOAD_ATTR                8 (TypeVar)
        # 384 PRECALL                  2
        # 388 CALL                     2
        # 398 POP_JUMP_BACKWARD_IF_TRUE    37 (to 326)
        # 595     >>  400 LOAD_GLOBAL              9 (NULL + TypeError)
        # 596         412 LOAD_CONST               8 ('Parameters to Protocol[...] must all be type variables. Parameter ')
        # 597         414 LOAD_FAST                2 (i)
        # 416 LOAD_CONST               7 (1)
        # 418 BINARY_OP                0 (+)
        # 596         422 FORMAT_VALUE             0
        # 424 LOAD_CONST               9 (' is ')
        # 597         426 LOAD_FAST                1 (params)
        # 428 LOAD_FAST                2 (i)
        # 430 BINARY_SUBSCR
        # 596         440 FORMAT_VALUE             0
        # 442 BUILD_STRING             4
        # 595         444 PRECALL                  1
        # 448 CALL                     1
        # 458 RAISE_VARARGS            1
        # 598     >>  460 LOAD_GLOBAL             19 (NULL + len)
        # 472 LOAD_GLOBAL             21 (NULL + set)
        # 484 LOAD_FAST                1 (params)
        # 486 PRECALL                  1
        # 490 CALL                     1
        # 500 PRECALL                  1
        # 504 CALL                     1
        # 514 LOAD_GLOBAL             19 (NULL + len)
        # 526 LOAD_FAST                1 (params)
        # 528 PRECALL                  1
        # 532 CALL                     1
        # 542 COMPARE_OP               3 (!=)
        # 548 POP_JUMP_FORWARD_IF_FALSE    15 (to 580)
        # 599         550 LOAD_GLOBAL              9 (NULL + TypeError)
        # 600         562 LOAD_CONST              10 ('Parameters to Protocol[...] must all be unique')
        # 599         564 PRECALL                  1
        # 568 CALL                     1
        # 578 RAISE_VARARGS            1
        # 598     >>  580 JUMP_FORWARD            16 (to 614)
        # 603     >>  582 LOAD_GLOBAL             23 (NULL + _check_generic)
        # 594 LOAD_FAST                0 (cls)
        # 596 LOAD_FAST                1 (params)
        # 598 PRECALL                  2
        # 602 CALL                     2
        # 612 POP_TOP
        # 604     >>  614 LOAD_GLOBAL              5 (NULL + typing)
        # 626 LOAD_ATTR               12 (_GenericAlias)
        # 636 LOAD_FAST                0 (cls)
        # 638 LOAD_FAST                1 (params)
        # 640 PRECALL                  2
        # 644 CALL                     2
        # 654 RETURN_VALUE
        # Disassembly of <code object <genexpr> at 0x000001EBD7DF0830, file "setuptools\_vendor\typing_extensions.py", line 588>:
        # 0 COPY_FREE_VARS           1
        # 588           2 RETURN_GENERATOR
        # 4 POP_TOP
        # 6 RESUME                   0
        # 8 LOAD_FAST                0 (.0)
        # >>   10 FOR_ITER                25 (to 62)
        # 12 STORE_FAST               1 (p)
        # 14 LOAD_GLOBAL              1 (NULL + typing)
        # 26 LOAD_ATTR                1 (_type_check)
        # 36 LOAD_FAST                1 (p)
        # 38 LOAD_DEREF               2 (msg)
        # 40 PRECALL                  2
        # 44 CALL                     2
        # 54 YIELD_VALUE
        # 56 RESUME                   1
        # 58 POP_TOP
        # 60 JUMP_BACKWARD           26 (to 10)
        # >>   62 LOAD_CONST               0 (None)
        # 64 RETURN_VALUE
        # Disassembly of <code object <genexpr> at 0x000001EBD7E46230, file "setuptools\_vendor\typing_extensions.py", line 591>:
        # 591           0 RETURN_GENERATOR
        # 2 POP_TOP
        # 4 RESUME                   0
        # 6 LOAD_FAST                0 (.0)
        # >>    8 FOR_ITER                30 (to 70)
        # 10 STORE_FAST               1 (p)
        # 12 LOAD_GLOBAL              1 (NULL + isinstance)
        # 24 LOAD_FAST                1 (p)
        # 26 LOAD_GLOBAL              2 (typing)
        # 38 LOAD_ATTR                2 (TypeVar)
        # 48 PRECALL                  2
        # 52 CALL                     2
        # 62 YIELD_VALUE
        # 64 RESUME                   1
        # 66 POP_TOP
        # 68 JUMP_BACKWARD           31 (to 8)
        # >>   70 LOAD_CONST               0 (None)
        # 72 RETURN_VALUE

    def __init_subclass__(cls):
        # 0 MAKE_CELL                0 (cls)
        # 2 MAKE_CELL               12 (gvarset)
        # 606           4 RESUME                   0
        # 607           6 BUILD_LIST               0
        # 8 STORE_FAST               3 (tvars)
        # 608          10 LOAD_CONST               1 ('__orig_bases__')
        # 12 LOAD_DEREF               0 (cls)
        # 14 LOAD_ATTR                0 (__dict__)
        # 24 CONTAINS_OP              0
        # 26 POP_JUMP_FORWARD_IF_FALSE    20 (to 68)
        # 609          28 LOAD_GLOBAL              2 (typing)
        # 40 LOAD_ATTR                2 (Generic)
        # 50 LOAD_DEREF               0 (cls)
        # 52 LOAD_ATTR                3 (__orig_bases__)
        # 62 CONTAINS_OP              0
        # 64 STORE_FAST               4 (error)
        # 66 JUMP_FORWARD            19 (to 106)
        # 611     >>   68 LOAD_GLOBAL              2 (typing)
        # 80 LOAD_ATTR                2 (Generic)
        # 90 LOAD_DEREF               0 (cls)
        # 92 LOAD_ATTR                4 (__bases__)
        # 102 CONTAINS_OP              0
        # 104 STORE_FAST               4 (error)
        # 612     >>  106 LOAD_FAST                4 (error)
        # 108 POP_JUMP_FORWARD_IF_FALSE    15 (to 140)
        # 613         110 LOAD_GLOBAL             11 (NULL + TypeError)
        # 122 LOAD_CONST               2 ('Cannot inherit from plain Generic')
        # 124 PRECALL                  1
        # 128 CALL                     1
        # 138 RAISE_VARARGS            1
        # 614     >>  140 LOAD_CONST               1 ('__orig_bases__')
        # 142 LOAD_DEREF               0 (cls)
        # 144 LOAD_ATTR                0 (__dict__)
        # 154 CONTAINS_OP              0
        # 156 POP_JUMP_FORWARD_IF_FALSE   252 (to 662)
        # 615         158 LOAD_GLOBAL             13 (NULL + _collect_type_vars)
        # 170 LOAD_DEREF               0 (cls)
        # 172 LOAD_ATTR                3 (__orig_bases__)
        # 182 PRECALL                  1
        # 186 CALL                     1
        # 196 STORE_FAST               3 (tvars)
        # 621         198 LOAD_CONST               0 (None)
        # 200 STORE_FAST               5 (gvars)
        # 622         202 LOAD_DEREF               0 (cls)
        # 204 LOAD_ATTR                3 (__orig_bases__)
        # 214 GET_ITER
        # >>  216 FOR_ITER                90 (to 398)
        # 218 STORE_FAST               6 (base)
        # 623         220 LOAD_GLOBAL             15 (NULL + isinstance)
        # 232 LOAD_FAST                6 (base)
        # 234 LOAD_GLOBAL              2 (typing)
        # 246 LOAD_ATTR                8 (_GenericAlias)
        # 256 PRECALL                  2
        # 260 CALL                     2
        # 270 POP_JUMP_FORWARD_IF_FALSE    62 (to 396)
        # 624         272 LOAD_FAST                6 (base)
        # 274 LOAD_ATTR                9 (__origin__)
        # 284 LOAD_GLOBAL              2 (typing)
        # 296 LOAD_ATTR                2 (Generic)
        # 306 LOAD_GLOBAL             20 (Protocol)
        # 318 BUILD_TUPLE              2
        # 320 CONTAINS_OP              0
        # 322 POP_JUMP_FORWARD_IF_FALSE    36 (to 396)
        # 626         324 LOAD_FAST                6 (base)
        # 326 LOAD_ATTR                9 (__origin__)
        # 336 LOAD_ATTR               11 (__name__)
        # 346 STORE_FAST               7 (the_base)
        # 627         348 LOAD_FAST                5 (gvars)
        # 350 POP_JUMP_FORWARD_IF_NONE    15 (to 382)
        # 628         352 LOAD_GLOBAL             11 (NULL + TypeError)
        # 629         364 LOAD_CONST               3 ('Cannot inherit from Generic[...] and/or Protocol[...] multiple types.')
        # 628         366 PRECALL                  1
        # 370 CALL                     1
        # 380 RAISE_VARARGS            1
        # 631     >>  382 LOAD_FAST                6 (base)
        # 384 LOAD_ATTR               12 (__parameters__)
        # 394 STORE_FAST               5 (gvars)
        # >>  396 JUMP_BACKWARD           91 (to 216)
        # 632     >>  398 LOAD_FAST                5 (gvars)
        # 400 POP_JUMP_FORWARD_IF_NOT_NONE     3 (to 408)
        # 633         402 LOAD_FAST                3 (tvars)
        # 404 STORE_FAST               5 (gvars)
        # 406 JUMP_FORWARD           127 (to 662)
        # 635     >>  408 LOAD_GLOBAL             27 (NULL + set)
        # 420 LOAD_FAST                3 (tvars)
        # 422 PRECALL                  1
        # 426 CALL                     1
        # 436 STORE_FAST               8 (tvarset)
        # 636         438 LOAD_GLOBAL             27 (NULL + set)
        # 450 LOAD_FAST                5 (gvars)
        # 452 PRECALL                  1
        # 456 CALL                     1
        # 466 STORE_DEREF             12 (gvarset)
        # 637         468 LOAD_FAST                8 (tvarset)
        # 470 LOAD_DEREF              12 (gvarset)
        # 472 COMPARE_OP               1 (<=)
        # 478 POP_JUMP_FORWARD_IF_TRUE    89 (to 658)
        # 638         480 LOAD_CONST               4 (', ')
        # 482 LOAD_METHOD             14 (join)
        # 504 LOAD_CLOSURE            12 (gvarset)
        # 506 BUILD_TUPLE              1
        # 508 LOAD_CONST               5 (<code object <genexpr> at 0x000001EBD7DF3030, file "setuptools\_vendor\typing_extensions.py", line 638>)
        # 510 MAKE_FUNCTION            8 (closure)
        # 512 LOAD_FAST                3 (tvars)
        # 514 GET_ITER
        # 516 PRECALL                  0
        # 520 CALL                     0
        # 530 PRECALL                  1
        # 534 CALL                     1
        # 544 STORE_FAST               9 (s_vars)
        # 639         546 LOAD_CONST               4 (', ')
        # 548 LOAD_METHOD             14 (join)
        # 570 LOAD_CONST               6 (<code object <genexpr> at 0x000001EBD7EE8E40, file "setuptools\_vendor\typing_extensions.py", line 639>)
        # 572 MAKE_FUNCTION            0
        # 574 LOAD_FAST                5 (gvars)
        # 576 GET_ITER
        # 578 PRECALL                  0
        # 582 CALL                     0
        # 592 PRECALL                  1
        # 596 CALL                     1
        # 606 STORE_FAST              10 (s_args)
        # 640         608 LOAD_GLOBAL             11 (NULL + TypeError)
        # 620 LOAD_CONST               7 ('Some type variables (')
        # 622 LOAD_FAST                9 (s_vars)
        # 624 FORMAT_VALUE             0
        # 626 LOAD_CONST               8 (') are not listed in ')
        # 641         628 LOAD_FAST                7 (the_base)
        # 640         630 FORMAT_VALUE             0
        # 632 LOAD_CONST               9 ('[')
        # 641         634 LOAD_FAST               10 (s_args)
        # 640         636 FORMAT_VALUE             0
        # 638 LOAD_CONST              10 (']')
        # 640 BUILD_STRING             7
        # 642 PRECALL                  1
        # 646 CALL                     1
        # 656 RAISE_VARARGS            1
        # 642     >>  658 LOAD_FAST                5 (gvars)
        # 660 STORE_FAST               3 (tvars)
        # 643     >>  662 LOAD_GLOBAL             31 (NULL + tuple)
        # 674 LOAD_FAST                3 (tvars)
        # 676 PRECALL                  1
        # 680 CALL                     1
        # 690 LOAD_DEREF               0 (cls)
        # 692 STORE_ATTR              12 (__parameters__)
        # 646         702 LOAD_DEREF               0 (cls)
        # 704 LOAD_ATTR                0 (__dict__)
        # 714 LOAD_METHOD             16 (get)
        # 736 LOAD_CONST              11 ('_is_protocol')
        # 738 LOAD_CONST               0 (None)
        # 740 PRECALL                  2
        # 744 CALL                     2
        # 754 POP_JUMP_FORWARD_IF_TRUE    35 (to 826)
        # 647         756 LOAD_GLOBAL             35 (NULL + any)
        # 768 LOAD_CONST              12 (<code object <genexpr> at 0x000001EBD7EBA170, file "setuptools\_vendor\typing_extensions.py", line 647>)
        # 770 MAKE_FUNCTION            0
        # 772 LOAD_DEREF               0 (cls)
        # 774 LOAD_ATTR                4 (__bases__)
        # 784 GET_ITER
        # 786 PRECALL                  0
        # 790 CALL                     0
        # 800 PRECALL                  1
        # 804 CALL                     1
        # 814 LOAD_DEREF               0 (cls)
        # 816 STORE_ATTR              18 (_is_protocol)
        # 650     >>  826 LOAD_CLOSURE             0 (cls)
        # 828 BUILD_TUPLE              1
        # 830 LOAD_CONST              13 (<code object _proto_hook at 0x000001EBD7596070, file "setuptools\_vendor\typing_extensions.py", line 650>)
        # 832 MAKE_FUNCTION            8 (closure)
        # 834 STORE_FAST              11 (_proto_hook)
        # 681         836 LOAD_CONST              14 ('__subclasshook__')
        # 838 LOAD_DEREF               0 (cls)
        # 840 LOAD_ATTR                0 (__dict__)
        # 850 CONTAINS_OP              1
        # 852 POP_JUMP_FORWARD_IF_FALSE     7 (to 868)
        # 682         854 LOAD_FAST               11 (_proto_hook)
        # 856 LOAD_DEREF               0 (cls)
        # 858 STORE_ATTR              19 (__subclasshook__)
        # 685     >>  868 LOAD_DEREF               0 (cls)
        # 870 LOAD_ATTR               18 (_is_protocol)
        # 880 POP_JUMP_FORWARD_IF_TRUE     2 (to 886)
        # 686         882 LOAD_CONST               0 (None)
        # 884 RETURN_VALUE
        # 689     >>  886 LOAD_DEREF               0 (cls)
        # 888 LOAD_ATTR                4 (__bases__)
        # 898 GET_ITER
        # >>  900 FOR_ITER               107 (to 1116)
        # 902 STORE_FAST               6 (base)
        # 690         904 LOAD_FAST                6 (base)
        # 906 LOAD_GLOBAL             40 (object)
        # 918 LOAD_GLOBAL              2 (typing)
        # 930 LOAD_ATTR                2 (Generic)
        # 940 BUILD_TUPLE              2
        # 942 CONTAINS_OP              0
        # 944 POP_JUMP_FORWARD_IF_TRUE    84 (to 1114)
        # 691         946 LOAD_FAST                6 (base)
        # 948 LOAD_ATTR               21 (__module__)
        # 958 LOAD_CONST              15 ('collections.abc')
        # 960 COMPARE_OP               2 (==)
        # 966 POP_JUMP_FORWARD_IF_FALSE    14 (to 996)
        # 692         968 LOAD_FAST                6 (base)
        # 970 LOAD_ATTR               11 (__name__)
        # 980 LOAD_GLOBAL             44 (_PROTO_WHITELIST)
        # 992 CONTAINS_OP              0
        # 994 POP_JUMP_FORWARD_IF_TRUE    59 (to 1114)
        # 693     >>  996 LOAD_GLOBAL             15 (NULL + isinstance)
        # 1008 LOAD_FAST                6 (base)
        # 1010 LOAD_GLOBAL             46 (_ProtocolMeta)
        # 1022 PRECALL                  2
        # 1026 CALL                     2
        # 692        1036 POP_JUMP_FORWARD_IF_FALSE     7 (to 1052)
        # 693        1038 LOAD_FAST                6 (base)
        # 1040 LOAD_ATTR               18 (_is_protocol)
        # 692        1050 POP_JUMP_FORWARD_IF_TRUE    31 (to 1114)
        # 694     >> 1052 LOAD_GLOBAL             11 (NULL + TypeError)
        # 1064 LOAD_CONST              16 ('Protocols can only inherit from other protocols, got ')
        # 695        1066 LOAD_GLOBAL             49 (NULL + repr)
        # 1078 LOAD_FAST                6 (base)
        # 1080 PRECALL                  1
        # 1084 CALL                     1
        # 694        1094 FORMAT_VALUE             0
        # 1096 BUILD_STRING             2
        # 1098 PRECALL                  1
        # 1102 CALL                     1
        # 1112 RAISE_VARARGS            1
        # >> 1114 JUMP_BACKWARD          108 (to 900)
        # 696     >> 1116 LOAD_GLOBAL             50 (_no_init)
        # 1128 LOAD_DEREF               0 (cls)
        # 1130 STORE_ATTR              26 (__init__)
        # 1140 LOAD_CONST               0 (None)
        # 1142 RETURN_VALUE
        # Disassembly of <code object <genexpr> at 0x000001EBD7DF3030, file "setuptools\_vendor\typing_extensions.py", line 638>:
        # 0 COPY_FREE_VARS           1
        # 638           2 RETURN_GENERATOR
        # 4 POP_TOP
        # 6 RESUME                   0
        # 8 LOAD_FAST                0 (.0)
        # >>   10 FOR_ITER                23 (to 58)
        # 12 STORE_FAST               1 (t)
        # 14 LOAD_FAST                1 (t)
        # 16 LOAD_DEREF               2 (gvarset)
        # 18 CONTAINS_OP              1
        # 20 POP_JUMP_BACKWARD_IF_FALSE     6 (to 10)
        # 22 LOAD_GLOBAL              1 (NULL + str)
        # 34 LOAD_FAST                1 (t)
        # 36 PRECALL                  1
        # 40 CALL                     1
        # 50 YIELD_VALUE
        # 52 RESUME                   1
        # 54 POP_TOP
        # 56 JUMP_BACKWARD           24 (to 10)
        # >>   58 LOAD_CONST               0 (None)
        # 60 RETURN_VALUE
        # Disassembly of <code object <genexpr> at 0x000001EBD7EE8E40, file "setuptools\_vendor\typing_extensions.py", line 639>:
        # 639           0 RETURN_GENERATOR
        # 2 POP_TOP
        # 4 RESUME                   0
        # 6 LOAD_FAST                0 (.0)
        # >>    8 FOR_ITER                19 (to 48)
        # 10 STORE_FAST               1 (g)
        # 12 LOAD_GLOBAL              1 (NULL + str)
        # 24 LOAD_FAST                1 (g)
        # 26 PRECALL                  1
        # 30 CALL                     1
        # 40 YIELD_VALUE
        # 42 RESUME                   1
        # 44 POP_TOP
        # 46 JUMP_BACKWARD           20 (to 8)
        # >>   48 LOAD_CONST               0 (None)
        # 50 RETURN_VALUE
        # Disassembly of <code object <genexpr> at 0x000001EBD7EBA170, file "setuptools\_vendor\typing_extensions.py", line 647>:
        # 647           0 RETURN_GENERATOR
        # 2 POP_TOP
        # 4 RESUME                   0
        # 6 LOAD_FAST                0 (.0)
        # >>    8 FOR_ITER                13 (to 36)
        # 10 STORE_FAST               1 (b)
        # 12 LOAD_FAST                1 (b)
        # 14 LOAD_GLOBAL              0 (Protocol)
        # 26 IS_OP                    0
        # 28 YIELD_VALUE
        # 30 RESUME                   1
        # 32 POP_TOP
        # 34 JUMP_BACKWARD           14 (to 8)
        # >>   36 LOAD_CONST               0 (None)
        # 38 RETURN_VALUE
        # Disassembly of <code object _proto_hook at 0x000001EBD7596070, file "setuptools\_vendor\typing_extensions.py", line 650>:
        # 0 COPY_FREE_VARS           1
        # 650           2 RESUME                   0
        # 651           4 LOAD_DEREF               4 (cls)
        # 6 LOAD_ATTR                0 (__dict__)
        # 16 LOAD_METHOD              1 (get)
        # 38 LOAD_CONST               1 ('_is_protocol')
        # 40 LOAD_CONST               0 (None)
        # 42 PRECALL                  2
        # 46 CALL                     2
        # 56 POP_JUMP_FORWARD_IF_TRUE     7 (to 72)
        # 652          58 LOAD_GLOBAL              4 (NotImplemented)
        # 70 RETURN_VALUE
        # 653     >>   72 LOAD_GLOBAL              7 (NULL + getattr)
        # 84 LOAD_DEREF               4 (cls)
        # 86 LOAD_CONST               2 ('_is_runtime_protocol')
        # 88 LOAD_CONST               3 (False)
        # 90 PRECALL                  3
        # 94 CALL                     3
        # 104 POP_JUMP_FORWARD_IF_TRUE    55 (to 216)
        # 654         106 LOAD_GLOBAL              9 (NULL + sys)
        # 118 LOAD_ATTR                5 (_getframe)
        # 128 LOAD_CONST               4 (2)
        # 130 PRECALL                  1
        # 134 CALL                     1
        # 144 LOAD_ATTR                6 (f_globals)
        # 154 LOAD_CONST               5 ('__name__')
        # 156 BINARY_SUBSCR
        # 166 LOAD_CONST               6 (('abc', 'functools'))
        # 168 CONTAINS_OP              0
        # 170 POP_JUMP_FORWARD_IF_FALSE     7 (to 186)
        # 655         172 LOAD_GLOBAL              4 (NotImplemented)
        # 184 RETURN_VALUE
        # 656     >>  186 LOAD_GLOBAL             15 (NULL + TypeError)
        # 198 LOAD_CONST               7 ('Instance and class checks can only be used with @runtime protocols')
        # 200 PRECALL                  1
        # 204 CALL                     1
        # 214 RAISE_VARARGS            1
        # 658     >>  216 LOAD_GLOBAL             17 (NULL + _is_callable_members_only)
        # 228 LOAD_DEREF               4 (cls)
        # 230 PRECALL                  1
        # 234 CALL                     1
        # 244 POP_JUMP_FORWARD_IF_TRUE    55 (to 356)
        # 659         246 LOAD_GLOBAL              9 (NULL + sys)
        # 258 LOAD_ATTR                5 (_getframe)
        # 268 LOAD_CONST               4 (2)
        # 270 PRECALL                  1
        # 274 CALL                     1
        # 284 LOAD_ATTR                6 (f_globals)
        # 294 LOAD_CONST               5 ('__name__')
        # 296 BINARY_SUBSCR
        # 306 LOAD_CONST               6 (('abc', 'functools'))
        # 308 CONTAINS_OP              0
        # 310 POP_JUMP_FORWARD_IF_FALSE     7 (to 326)
        # 660         312 LOAD_GLOBAL              4 (NotImplemented)
        # 324 RETURN_VALUE
        # 661     >>  326 LOAD_GLOBAL             15 (NULL + TypeError)
        # 338 LOAD_CONST               8 ("Protocols with non-method members don't support issubclass()")
        # 340 PRECALL                  1
        # 344 CALL                     1
        # 354 RAISE_VARARGS            1
        # 663     >>  356 LOAD_GLOBAL             19 (NULL + isinstance)
        # 368 LOAD_FAST                0 (other)
        # 370 LOAD_GLOBAL             20 (type)
        # 382 PRECALL                  2
        # 386 CALL                     2
        # 396 POP_JUMP_FORWARD_IF_TRUE    15 (to 428)
        # 665         398 LOAD_GLOBAL             15 (NULL + TypeError)
        # 410 LOAD_CONST               9 ('issubclass() arg 1 must be a class')
        # 412 PRECALL                  1
        # 416 CALL                     1
        # 426 RAISE_VARARGS            1
        # 666     >>  428 LOAD_GLOBAL             23 (NULL + _get_protocol_attrs)
        # 440 LOAD_DEREF               4 (cls)
        # 442 PRECALL                  1
        # 446 CALL                     1
        # 456 GET_ITER
        # >>  458 FOR_ITER               133 (to 726)
        # 460 STORE_FAST               1 (attr)
        # 667         462 LOAD_FAST                0 (other)
        # 464 LOAD_ATTR               12 (__mro__)
        # 474 GET_ITER
        # >>  476 FOR_ITER               114 (to 706)
        # 478 STORE_FAST               2 (base)
        # 668         480 LOAD_FAST                1 (attr)
        # 482 LOAD_FAST                2 (base)
        # 484 LOAD_ATTR                0 (__dict__)
        # 494 CONTAINS_OP              0
        # 496 POP_JUMP_FORWARD_IF_FALSE    26 (to 550)
        # 669         498 LOAD_FAST                2 (base)
        # 500 LOAD_ATTR                0 (__dict__)
        # 510 LOAD_FAST                1 (attr)
        # 512 BINARY_SUBSCR
        # 522 POP_JUMP_FORWARD_IF_NOT_NONE    11 (to 546)
        # 670         524 LOAD_GLOBAL              4 (NotImplemented)
        # 536 SWAP                     2
        # 538 POP_TOP
        # 540 SWAP                     2
        # 542 POP_TOP
        # 544 RETURN_VALUE
        # 671     >>  546 POP_TOP
        # 548 JUMP_FORWARD            87 (to 724)
        # 672     >>  550 LOAD_GLOBAL              7 (NULL + getattr)
        # 562 LOAD_FAST                2 (base)
        # 564 LOAD_CONST              10 ('__annotations__')
        # 566 BUILD_MAP                0
        # 568 PRECALL                  3
        # 572 CALL                     3
        # 582 STORE_FAST               3 (annotations)
        # 673         584 LOAD_GLOBAL             19 (NULL + isinstance)
        # 596 LOAD_FAST                3 (annotations)
        # 598 LOAD_GLOBAL             26 (typing)
        # 610 LOAD_ATTR               14 (Mapping)
        # 620 PRECALL                  2
        # 624 CALL                     2
        # 634 POP_JUMP_FORWARD_IF_FALSE    34 (to 704)
        # 674         636 LOAD_FAST                1 (attr)
        # 638 LOAD_FAST                3 (annotations)
        # 640 CONTAINS_OP              0
        # 642 POP_JUMP_FORWARD_IF_FALSE    30 (to 704)
        # 675         644 LOAD_GLOBAL             19 (NULL + isinstance)
        # 656 LOAD_FAST                0 (other)
        # 658 LOAD_GLOBAL             30 (_ProtocolMeta)
        # 670 PRECALL                  2
        # 674 CALL                     2
        # 674         684 POP_JUMP_FORWARD_IF_FALSE     9 (to 704)
        # 676         686 LOAD_FAST                0 (other)
        # 688 LOAD_ATTR               16 (_is_protocol)
        # 674         698 POP_JUMP_FORWARD_IF_FALSE     2 (to 704)
        # 677         700 POP_TOP
        # 702 JUMP_FORWARD            10 (to 724)
        # >>  704 JUMP_BACKWARD          115 (to 476)
        # 679     >>  706 LOAD_GLOBAL              4 (NotImplemented)
        # 718 SWAP                     2
        # 720 POP_TOP
        # 722 RETURN_VALUE
        # >>  724 JUMP_BACKWARD          134 (to 458)
        # 680     >>  726 LOAD_CONST              11 (True)
        # 728 RETURN_VALUE


def runtime_checkable(cls):
    """Mark a protocol class as a runtime protocol, so that it
        can be used with isinstance() and issubclass(). Raise TypeError
        if applied to a non-protocol class.

        This allows a simple-minded structural check very similar to the
        one-offs in collections.abc such as Hashable.
        """
    # 942           0 RESUME                   0
    # 950           2 LOAD_GLOBAL              1 (NULL + isinstance)
    # 14 LOAD_FAST                0 (cls)
    # 16 LOAD_GLOBAL              2 (_ProtocolMeta)
    # 28 PRECALL                  2
    # 32 CALL                     2
    # 42 POP_JUMP_FORWARD_IF_FALSE     7 (to 58)
    # 44 LOAD_FAST                0 (cls)
    # 46 LOAD_ATTR                2 (_is_protocol)
    # 56 POP_JUMP_FORWARD_IF_TRUE    18 (to 94)
    # 951     >>   58 LOAD_GLOBAL              7 (NULL + TypeError)
    # 70 LOAD_CONST               1 ('@runtime_checkable can be only applied to protocol classes, got ')
    # 952          72 LOAD_FAST                0 (cls)
    # 951          74 FORMAT_VALUE             2 (repr)
    # 76 BUILD_STRING             2
    # 78 PRECALL                  1
    # 82 CALL                     1
    # 92 RAISE_VARARGS            1
    # 953     >>   94 LOAD_CONST               2 (True)
    # 96 LOAD_FAST                0 (cls)
    # 98 STORE_ATTR               4 (_is_runtime_protocol)
    # 954         108 LOAD_FAST                0 (cls)
    # 110 RETURN_VALUE

class SupportsIndex:
    """SupportsIndex"""
    def __index__(self):
        # 970           0 RESUME                   0
        # 972           2 LOAD_CONST               0 (None)
        # 4 RETURN_VALUE


def _check_fails(cls, other):
    # 982           0 RESUME                   0
    # 983           2 NOP
    # 984           4 LOAD_GLOBAL              1 (NULL + sys)
    # 16 LOAD_ATTR                1 (_getframe)
    # 26 LOAD_CONST               1 (1)
    # 28 PRECALL                  1
    # 32 CALL                     1
    # 42 LOAD_ATTR                2 (f_globals)
    # 52 LOAD_CONST               2 ('__name__')
    # 54 BINARY_SUBSCR
    # 64 LOAD_CONST               3 (('abc', 'functools', 'typing'))
    # 66 CONTAINS_OP              1
    # 68 POP_JUMP_FORWARD_IF_FALSE    15 (to 100)
    # 988          70 LOAD_GLOBAL              7 (NULL + TypeError)
    # 82 LOAD_CONST               4 ('TypedDict does not support instance and class checks')
    # 84 PRECALL                  1
    # 88 CALL                     1
    # 98 RAISE_VARARGS            1
    # 984     >>  100 JUMP_FORWARD            23 (to 148)
    # >>  102 PUSH_EXC_INFO
    # 989         104 LOAD_GLOBAL              8 (AttributeError)
    # 116 LOAD_GLOBAL             10 (ValueError)
    # 128 BUILD_TUPLE              2
    # 130 CHECK_EXC_MATCH
    # 132 POP_JUMP_FORWARD_IF_FALSE     3 (to 140)
    # 134 POP_TOP
    # 990         136 POP_EXCEPT
    # 138 JUMP_FORWARD             4 (to 148)
    # 989     >>  140 RERAISE                  0
    # >>  142 COPY                     3
    # 144 POP_EXCEPT
    # 146 RERAISE                  1
    # 991     >>  148 LOAD_CONST               5 (False)
    # 150 RETURN_VALUE
    # ExceptionTable:
    # 4 to 98 -> 102 [0]
    # 102 to 134 -> 142 [1] lasti
    # 140 to 140 -> 142 [1] lasti

def _dict_new():
    # 993           0 RESUME                   0
    # 994           2 LOAD_FAST                0 (args)
    # 4 POP_JUMP_FORWARD_IF_TRUE    15 (to 36)
    # 995           6 LOAD_GLOBAL              1 (NULL + TypeError)
    # 18 LOAD_CONST               1 ('TypedDict.__new__(): not enough arguments')
    # 20 PRECALL                  1
    # 24 CALL                     1
    # 34 RAISE_VARARGS            1
    # 996     >>   36 LOAD_FAST                0 (args)
    # 38 LOAD_CONST               2 (0)
    # 40 BINARY_SUBSCR
    # 50 LOAD_FAST                0 (args)
    # 52 LOAD_CONST               3 (1)
    # 54 LOAD_CONST               0 (None)
    # 56 BUILD_SLICE              2
    # 58 BINARY_SUBSCR
    # 68 STORE_FAST               0 (args)
    # 70 STORE_FAST               2 (_)
    # 997          72 LOAD_GLOBAL              3 (NULL + dict)
    # 84 LOAD_FAST                0 (args)
    # 86 BUILD_MAP                0
    # 88 LOAD_FAST                1 (kwargs)
    # 90 DICT_MERGE               1
    # 92 CALL_FUNCTION_EX         1
    # 94 RETURN_VALUE

def _typeddict_new(*, total):
    # 1001           0 RESUME                   0
    # 1002           2 LOAD_FAST                1 (args)
    # 4 POP_JUMP_FORWARD_IF_TRUE    15 (to 36)
    # 1003           6 LOAD_GLOBAL              1 (NULL + TypeError)
    # 18 LOAD_CONST               1 ('TypedDict.__new__(): not enough arguments')
    # 20 PRECALL                  1
    # 24 CALL                     1
    # 34 RAISE_VARARGS            1
    # 1004     >>   36 LOAD_FAST                1 (args)
    # 38 LOAD_CONST               2 (0)
    # 40 BINARY_SUBSCR
    # 50 LOAD_FAST                1 (args)
    # 52 LOAD_CONST               3 (1)
    # 54 LOAD_CONST               0 (None)
    # 56 BUILD_SLICE              2
    # 58 BINARY_SUBSCR
    # 68 STORE_FAST               1 (args)
    # 70 STORE_FAST               3 (_)
    # 1005          72 LOAD_FAST                1 (args)
    # 74 POP_JUMP_FORWARD_IF_FALSE    19 (to 114)
    # 1006          76 LOAD_FAST                1 (args)
    # 78 LOAD_CONST               2 (0)
    # 80 BINARY_SUBSCR
    # 90 LOAD_FAST                1 (args)
    # 92 LOAD_CONST               3 (1)
    # 94 LOAD_CONST               0 (None)
    # 96 BUILD_SLICE              2
    # 98 BINARY_SUBSCR
    # 108 STORE_FAST               1 (args)
    # 110 STORE_FAST               4 (typename)
    # 112 JUMP_FORWARD            74 (to 262)
    # 1007     >>  114 LOAD_CONST               4 ('_typename')
    # 116 LOAD_FAST                2 (kwargs)
    # 118 CONTAINS_OP              0
    # 120 POP_JUMP_FORWARD_IF_FALSE    55 (to 232)
    # 1008         122 LOAD_FAST                2 (kwargs)
    # 124 LOAD_METHOD              1 (pop)
    # 146 LOAD_CONST               4 ('_typename')
    # 148 PRECALL                  1
    # 152 CALL                     1
    # 162 STORE_FAST               4 (typename)
    # 1009         164 LOAD_CONST               2 (0)
    # 166 LOAD_CONST               0 (None)
    # 168 IMPORT_NAME              2 (warnings)
    # 170 STORE_FAST               5 (warnings)
    # 1010         172 LOAD_FAST                5 (warnings)
    # 174 LOAD_METHOD              3 (warn)
    # 196 LOAD_CONST               5 ("Passing '_typename' as keyword argument is deprecated")
    # 1011         198 LOAD_GLOBAL              8 (DeprecationWarning)
    # 210 LOAD_CONST               6 (2)
    # 1010         212 KW_NAMES                 7
    # 214 PRECALL                  3
    # 218 CALL                     3
    # 228 POP_TOP
    # 230 JUMP_FORWARD            15 (to 262)
    # 1013     >>  232 LOAD_GLOBAL              1 (NULL + TypeError)
    # 244 LOAD_CONST               8 ("TypedDict.__new__() missing 1 required positional argument: '_typename'")
    # 246 PRECALL                  1
    # 250 CALL                     1
    # 260 RAISE_VARARGS            1
    # 1015     >>  262 LOAD_FAST                1 (args)
    # 264 POP_JUMP_FORWARD_IF_FALSE    55 (to 376)
    # 1016         266 NOP
    # 1017         268 LOAD_FAST                1 (args)
    # 270 UNPACK_SEQUENCE          1
    # 274 STORE_FAST               6 (fields)
    # 276 JUMP_FORWARD           129 (to 536)
    # >>  278 PUSH_EXC_INFO
    # 1018         280 LOAD_GLOBAL             10 (ValueError)
    # 292 CHECK_EXC_MATCH
    # 294 POP_JUMP_FORWARD_IF_FALSE    36 (to 368)
    # 296 POP_TOP
    # 1019         298 LOAD_GLOBAL              1 (NULL + TypeError)
    # 310 LOAD_CONST               9 ('TypedDict.__new__() takes from 2 to 3 positional arguments but ')
    # 1020         312 LOAD_GLOBAL             13 (NULL + len)
    # 324 LOAD_FAST                1 (args)
    # 326 PRECALL                  1
    # 330 CALL                     1
    # 340 LOAD_CONST               6 (2)
    # 342 BINARY_OP                0 (+)
    # 1019         346 FORMAT_VALUE             0
    # 348 LOAD_CONST              10 (' were given')
    # 350 BUILD_STRING             3
    # 352 PRECALL                  1
    # 356 CALL                     1
    # 366 RAISE_VARARGS            1
    # 1018     >>  368 RERAISE                  0
    # >>  370 COPY                     3
    # 372 POP_EXCEPT
    # 374 RERAISE                  1
    # 1022     >>  376 LOAD_CONST              11 ('_fields')
    # 378 LOAD_FAST                2 (kwargs)
    # 380 CONTAINS_OP              0
    # 382 POP_JUMP_FORWARD_IF_FALSE    74 (to 532)
    # 384 LOAD_GLOBAL             13 (NULL + len)
    # 396 LOAD_FAST                2 (kwargs)
    # 398 PRECALL                  1
    # 402 CALL                     1
    # 412 LOAD_CONST               3 (1)
    # 414 COMPARE_OP               2 (==)
    # 420 POP_JUMP_FORWARD_IF_FALSE    55 (to 532)
    # 1023         422 LOAD_FAST                2 (kwargs)
    # 424 LOAD_METHOD              1 (pop)
    # 446 LOAD_CONST              11 ('_fields')
    # 448 PRECALL                  1
    # 452 CALL                     1
    # 462 STORE_FAST               6 (fields)
    # 1024         464 LOAD_CONST               2 (0)
    # 466 LOAD_CONST               0 (None)
    # 468 IMPORT_NAME              2 (warnings)
    # 470 STORE_FAST               5 (warnings)
    # 1025         472 LOAD_FAST                5 (warnings)
    # 474 LOAD_METHOD              3 (warn)
    # 496 LOAD_CONST              12 ("Passing '_fields' as keyword argument is deprecated")
    # 1026         498 LOAD_GLOBAL              8 (DeprecationWarning)
    # 510 LOAD_CONST               6 (2)
    # 1025         512 KW_NAMES                 7
    # 514 PRECALL                  3
    # 518 CALL                     3
    # 528 POP_TOP
    # 530 JUMP_FORWARD             2 (to 536)
    # 1028     >>  532 LOAD_CONST               0 (None)
    # 534 STORE_FAST               6 (fields)
    # 1030     >>  536 LOAD_FAST                6 (fields)
    # 538 POP_JUMP_FORWARD_IF_NOT_NONE     3 (to 546)
    # 1031         540 LOAD_FAST                2 (kwargs)
    # 542 STORE_FAST               6 (fields)
    # 544 JUMP_FORWARD            17 (to 580)
    # 1032     >>  546 LOAD_FAST                2 (kwargs)
    # 548 POP_JUMP_FORWARD_IF_FALSE    15 (to 580)
    # 1033         550 LOAD_GLOBAL              1 (NULL + TypeError)
    # 562 LOAD_CONST              13 ('TypedDict takes either a dict or keyword arguments, but not both')
    # 564 PRECALL                  1
    # 568 CALL                     1
    # 578 RAISE_VARARGS            1
    # 1036     >>  580 LOAD_CONST              14 ('__annotations__')
    # 582 LOAD_GLOBAL             15 (NULL + dict)
    # 594 LOAD_FAST                6 (fields)
    # 596 PRECALL                  1
    # 600 CALL                     1
    # 610 BUILD_MAP                1
    # 612 STORE_FAST               7 (ns)
    # 1037         614 NOP
    # 1039         616 LOAD_GLOBAL             17 (NULL + sys)
    # 628 LOAD_ATTR                9 (_getframe)
    # 638 LOAD_CONST               3 (1)
    # 640 PRECALL                  1
    # 644 CALL                     1
    # 654 LOAD_ATTR               10 (f_globals)
    # 664 LOAD_METHOD             11 (get)
    # 686 LOAD_CONST              15 ('__name__')
    # 688 LOAD_CONST              16 ('__main__')
    # 690 PRECALL                  2
    # 694 CALL                     2
    # 704 LOAD_FAST                7 (ns)
    # 706 LOAD_CONST              17 ('__module__')
    # 708 STORE_SUBSCR
    # 712 JUMP_FORWARD            23 (to 760)
    # >>  714 PUSH_EXC_INFO
    # 1040         716 LOAD_GLOBAL             24 (AttributeError)
    # 728 LOAD_GLOBAL             10 (ValueError)
    # 740 BUILD_TUPLE              2
    # 742 CHECK_EXC_MATCH
    # 744 POP_JUMP_FORWARD_IF_FALSE     3 (to 752)
    # 746 POP_TOP
    # 1041         748 POP_EXCEPT
    # 750 JUMP_FORWARD             4 (to 760)
    # 1040     >>  752 RERAISE                  0
    # >>  754 COPY                     3
    # 756 POP_EXCEPT
    # 758 RERAISE                  1
    # 1043     >>  760 LOAD_GLOBAL             27 (NULL + _TypedDictMeta)
    # 772 LOAD_FAST                4 (typename)
    # 774 LOAD_CONST              18 (())
    # 776 LOAD_FAST                7 (ns)
    # 778 LOAD_FAST                0 (total)
    # 780 KW_NAMES                19
    # 782 PRECALL                  4
    # 786 CALL                     4
    # 796 RETURN_VALUE
    # ExceptionTable:
    # 268 to 274 -> 278 [0]
    # 278 to 368 -> 370 [1] lasti
    # 616 to 710 -> 714 [0]
    # 714 to 746 -> 754 [1] lasti
    # 752 to 752 -> 754 [1] lasti

class _TypedDictMeta:
    """_TypedDictMeta"""
    def __init__(cls, name, bases, ns, total):
        # 0 COPY_FREE_VARS           1
        # 1049           2 RESUME                   0
        # 1050           4 LOAD_GLOBAL              1 (NULL + super)
        # 16 PRECALL                  0
        # 20 CALL                     0
        # 30 LOAD_METHOD              1 (__init__)
        # 52 LOAD_FAST                1 (name)
        # 54 LOAD_FAST                2 (bases)
        # 56 LOAD_FAST                3 (ns)
        # 58 PRECALL                  3
        # 62 CALL                     3
        # 72 POP_TOP
        # 74 LOAD_CONST               0 (None)
        # 76 RETURN_VALUE

    def __new__(cls, name, bases, ns, total):
        # 0 COPY_FREE_VARS           1
        # 2 MAKE_CELL               12 (msg)
        # 1052           4 RESUME                   0
        # 1059           6 LOAD_FAST                1 (name)
        # 8 LOAD_CONST               1 ('TypedDict')
        # 10 COMPARE_OP               2 (==)
        # 16 POP_JUMP_FORWARD_IF_FALSE     7 (to 32)
        # 18 LOAD_GLOBAL              0 (_typeddict_new)
        # 30 JUMP_FORWARD             6 (to 44)
        # >>   32 LOAD_GLOBAL              2 (_dict_new)
        # >>   44 LOAD_FAST                3 (ns)
        # 46 LOAD_CONST               2 ('__new__')
        # 48 STORE_SUBSCR
        # 1060          52 LOAD_GLOBAL              5 (NULL + super)
        # 64 PRECALL                  0
        # 68 CALL                     0
        # 78 LOAD_METHOD              3 (__new__)
        # 100 LOAD_FAST                0 (cls)
        # 102 LOAD_FAST                1 (name)
        # 104 LOAD_GLOBAL              8 (dict)
        # 116 BUILD_TUPLE              1
        # 118 LOAD_FAST                3 (ns)
        # 120 PRECALL                  4
        # 124 CALL                     4
        # 134 STORE_FAST               5 (tp_dict)
        # 1062         136 BUILD_MAP                0
        # 138 STORE_FAST               6 (annotations)
        # 1063         140 LOAD_FAST                3 (ns)
        # 142 LOAD_METHOD              5 (get)
        # 164 LOAD_CONST               3 ('__annotations__')
        # 166 BUILD_MAP                0
        # 168 PRECALL                  2
        # 172 CALL                     2
        # 182 STORE_FAST               7 (own_annotations)
        # 1064         184 LOAD_GLOBAL             13 (NULL + set)
        # 196 LOAD_FAST                7 (own_annotations)
        # 198 LOAD_METHOD              7 (keys)
        # 220 PRECALL                  0
        # 224 CALL                     0
        # 234 PRECALL                  1
        # 238 CALL                     1
        # 248 STORE_FAST               8 (own_annotation_keys)
        # 1065         250 LOAD_CONST               4 ("TypedDict('Name', {f0: t0, f1: t1, ...}); each t must be a type")
        # 252 STORE_DEREF             12 (msg)
        # 1066         254 LOAD_CLOSURE            12 (msg)
        # 256 BUILD_TUPLE              1
        # 258 LOAD_CONST               5 (<code object <dictcomp> at 0x000001EBD7DF3330, file "setuptools\_vendor\typing_extensions.py", line 1066>)
        # 260 MAKE_FUNCTION            8 (closure)
        # 1067         262 LOAD_FAST                7 (own_annotations)
        # 264 LOAD_METHOD              8 (items)
        # 286 PRECALL                  0
        # 290 CALL                     0
        # 1066         300 GET_ITER
        # 302 PRECALL                  0
        # 306 CALL                     0
        # 316 STORE_FAST               7 (own_annotations)
        # 1069         318 LOAD_GLOBAL             13 (NULL + set)
        # 330 PRECALL                  0
        # 334 CALL                     0
        # 344 STORE_FAST               9 (required_keys)
        # 1070         346 LOAD_GLOBAL             13 (NULL + set)
        # 358 PRECALL                  0
        # 362 CALL                     0
        # 372 STORE_FAST              10 (optional_keys)
        # 1072         374 LOAD_FAST                2 (bases)
        # 376 GET_ITER
        # >>  378 FOR_ITER               140 (to 660)
        # 380 STORE_FAST              11 (base)
        # 1073         382 LOAD_FAST                6 (annotations)
        # 384 LOAD_METHOD              9 (update)
        # 406 LOAD_FAST               11 (base)
        # 408 LOAD_ATTR               10 (__dict__)
        # 418 LOAD_METHOD              5 (get)
        # 440 LOAD_CONST               3 ('__annotations__')
        # 442 BUILD_MAP                0
        # 444 PRECALL                  2
        # 448 CALL                     2
        # 458 PRECALL                  1
        # 462 CALL                     1
        # 472 POP_TOP
        # 1074         474 LOAD_FAST                9 (required_keys)
        # 476 LOAD_METHOD              9 (update)
        # 498 LOAD_FAST               11 (base)
        # 500 LOAD_ATTR               10 (__dict__)
        # 510 LOAD_METHOD              5 (get)
        # 532 LOAD_CONST               6 ('__required_keys__')
        # 534 LOAD_CONST               7 (())
        # 536 PRECALL                  2
        # 540 CALL                     2
        # 550 PRECALL                  1
        # 554 CALL                     1
        # 564 POP_TOP
        # 1075         566 LOAD_FAST               10 (optional_keys)
        # 568 LOAD_METHOD              9 (update)
        # 590 LOAD_FAST               11 (base)
        # 592 LOAD_ATTR               10 (__dict__)
        # 602 LOAD_METHOD              5 (get)
        # 624 LOAD_CONST               8 ('__optional_keys__')
        # 626 LOAD_CONST               7 (())
        # 628 PRECALL                  2
        # 632 CALL                     2
        # 642 PRECALL                  1
        # 646 CALL                     1
        # 656 POP_TOP
        # 658 JUMP_BACKWARD          141 (to 378)
        # 1077     >>  660 LOAD_FAST                6 (annotations)
        # 662 LOAD_METHOD              9 (update)
        # 684 LOAD_FAST                7 (own_annotations)
        # 686 PRECALL                  1
        # 690 CALL                     1
        # 700 POP_TOP
        # 1078         702 LOAD_FAST                4 (total)
        # 704 POP_JUMP_FORWARD_IF_FALSE    22 (to 750)
        # 1079         706 LOAD_FAST                9 (required_keys)
        # 708 LOAD_METHOD              9 (update)
        # 730 LOAD_FAST                8 (own_annotation_keys)
        # 732 PRECALL                  1
        # 736 CALL                     1
        # 746 POP_TOP
        # 748 JUMP_FORWARD            21 (to 792)
        # 1081     >>  750 LOAD_FAST               10 (optional_keys)
        # 752 LOAD_METHOD              9 (update)
        # 774 LOAD_FAST                8 (own_annotation_keys)
        # 776 PRECALL                  1
        # 780 CALL                     1
        # 790 POP_TOP
        # 1083     >>  792 LOAD_FAST                6 (annotations)
        # 794 LOAD_FAST                5 (tp_dict)
        # 796 STORE_ATTR              11 (__annotations__)
        # 1084         806 LOAD_GLOBAL             25 (NULL + frozenset)
        # 818 LOAD_FAST                9 (required_keys)
        # 820 PRECALL                  1
        # 824 CALL                     1
        # 834 LOAD_FAST                5 (tp_dict)
        # 836 STORE_ATTR              13 (__required_keys__)
        # 1085         846 LOAD_GLOBAL             25 (NULL + frozenset)
        # 858 LOAD_FAST               10 (optional_keys)
        # 860 PRECALL                  1
        # 864 CALL                     1
        # 874 LOAD_FAST                5 (tp_dict)
        # 876 STORE_ATTR              14 (__optional_keys__)
        # 1086         886 LOAD_GLOBAL             31 (NULL + hasattr)
        # 898 LOAD_FAST                5 (tp_dict)
        # 900 LOAD_CONST               9 ('__total__')
        # 902 PRECALL                  2
        # 906 CALL                     2
        # 916 POP_JUMP_FORWARD_IF_TRUE     7 (to 932)
        # 1087         918 LOAD_FAST                4 (total)
        # 920 LOAD_FAST                5 (tp_dict)
        # 922 STORE_ATTR              16 (__total__)
        # 1088     >>  932 LOAD_FAST                5 (tp_dict)
        # 934 RETURN_VALUE
        # Disassembly of <code object <dictcomp> at 0x000001EBD7DF3330, file "setuptools\_vendor\typing_extensions.py", line 1066>:
        # 0 COPY_FREE_VARS           1
        # 1066           2 RESUME                   0
        # 4 BUILD_MAP                0
        # 6 LOAD_FAST                0 (.0)
        # >>    8 FOR_ITER                27 (to 64)
        # 1067          10 UNPACK_SEQUENCE          2
        # 14 STORE_FAST               1 (n)
        # 16 STORE_FAST               2 (tp)
        # 18 LOAD_FAST                1 (n)
        # 20 LOAD_GLOBAL              1 (NULL + typing)
        # 32 LOAD_ATTR                1 (_type_check)
        # 42 LOAD_FAST                2 (tp)
        # 44 LOAD_DEREF               3 (msg)
        # 46 PRECALL                  2
        # 50 CALL                     2
        # 1066          60 MAP_ADD                  2
        # 62 JUMP_BACKWARD           28 (to 8)
        # >>   64 RETURN_VALUE


class _AnnotatedAlias:
    """_AnnotatedAlias"""
    def __init__(self, origin, metadata):
        # 0 COPY_FREE_VARS           1
        # 1142           2 RESUME                   0
        # 1143           4 LOAD_GLOBAL              1 (NULL + isinstance)
        # 16 LOAD_FAST                1 (origin)
        # 18 LOAD_GLOBAL              2 (_AnnotatedAlias)
        # 30 PRECALL                  2
        # 34 CALL                     2
        # 44 POP_JUMP_FORWARD_IF_FALSE    17 (to 80)
        # 1144          46 LOAD_FAST                1 (origin)
        # 48 LOAD_ATTR                2 (__metadata__)
        # 58 LOAD_FAST                2 (metadata)
        # 60 BINARY_OP                0 (+)
        # 64 STORE_FAST               2 (metadata)
        # 1145          66 LOAD_FAST                1 (origin)
        # 68 LOAD_ATTR                3 (__origin__)
        # 78 STORE_FAST               1 (origin)
        # 1146     >>   80 LOAD_GLOBAL              9 (NULL + super)
        # 92 PRECALL                  0
        # 96 CALL                     0
        # 106 LOAD_METHOD              5 (__init__)
        # 128 LOAD_FAST                1 (origin)
        # 130 LOAD_FAST                1 (origin)
        # 132 PRECALL                  2
        # 136 CALL                     2
        # 146 POP_TOP
        # 1147         148 LOAD_FAST                2 (metadata)
        # 150 LOAD_FAST                0 (self)
        # 152 STORE_ATTR               2 (__metadata__)
        # 162 LOAD_CONST               0 (None)
        # 164 RETURN_VALUE

    def copy_with(self, params):
        # 1149           0 RESUME                   0
        # 1150           2 LOAD_GLOBAL              1 (NULL + len)
        # 14 LOAD_FAST                1 (params)
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 LOAD_CONST               1 (1)
        # 32 COMPARE_OP               2 (==)
        # 38 POP_JUMP_FORWARD_IF_TRUE     2 (to 44)
        # 40 LOAD_ASSERTION_ERROR
        # 42 RAISE_VARARGS            1
        # 1151     >>   44 LOAD_FAST                1 (params)
        # 46 LOAD_CONST               2 (0)
        # 48 BINARY_SUBSCR
        # 58 STORE_FAST               2 (new_type)
        # 1152          60 LOAD_GLOBAL              3 (NULL + _AnnotatedAlias)
        # 72 LOAD_FAST                2 (new_type)
        # 74 LOAD_FAST                0 (self)
        # 76 LOAD_ATTR                2 (__metadata__)
        # 86 PRECALL                  2
        # 90 CALL                     2
        # 100 RETURN_VALUE

    def __repr__(self):
        # 1154           0 RESUME                   0
        # 1155           2 LOAD_CONST               1 ('typing_extensions.Annotated[')
        # 4 LOAD_GLOBAL              1 (NULL + typing)
        # 16 LOAD_ATTR                1 (_type_repr)
        # 26 LOAD_FAST                0 (self)
        # 28 LOAD_ATTR                2 (__origin__)
        # 38 PRECALL                  1
        # 42 CALL                     1
        # 52 FORMAT_VALUE             0
        # 54 LOAD_CONST               2 (', ')
        # 1156          56 LOAD_CONST               2 (', ')
        # 58 LOAD_METHOD              3 (join)
        # 80 LOAD_CONST               3 (<code object <genexpr> at 0x000001EBD7EE95C0, file "setuptools\_vendor\typing_extensions.py", line 1156>)
        # 82 MAKE_FUNCTION            0
        # 84 LOAD_FAST                0 (self)
        # 86 LOAD_ATTR                4 (__metadata__)
        # 96 GET_ITER
        # 98 PRECALL                  0
        # 102 CALL                     0
        # 112 PRECALL                  1
        # 116 CALL                     1
        # 1155         126 FORMAT_VALUE             0
        # 128 LOAD_CONST               4 (']')
        # 130 BUILD_STRING             5
        # 132 RETURN_VALUE
        # Disassembly of <code object <genexpr> at 0x000001EBD7EE95C0, file "setuptools\_vendor\typing_extensions.py", line 1156>:
        # 1156           0 RETURN_GENERATOR
        # 2 POP_TOP
        # 4 RESUME                   0
        # 6 LOAD_FAST                0 (.0)
        # >>    8 FOR_ITER                19 (to 48)
        # 10 STORE_FAST               1 (a)
        # 12 LOAD_GLOBAL              1 (NULL + repr)
        # 24 LOAD_FAST                1 (a)
        # 26 PRECALL                  1
        # 30 CALL                     1
        # 40 YIELD_VALUE
        # 42 RESUME                   1
        # 44 POP_TOP
        # 46 JUMP_BACKWARD           20 (to 8)
        # >>   48 LOAD_CONST               0 (None)
        # 50 RETURN_VALUE

    def __reduce__(self):
        # 1158           0 RESUME                   0
        # 1159           2 LOAD_GLOBAL              0 (operator)
        # 14 LOAD_ATTR                1 (getitem)
        # 1160          24 LOAD_GLOBAL              4 (Annotated)
        # 36 LOAD_FAST                0 (self)
        # 38 LOAD_ATTR                3 (__origin__)
        # 48 BUILD_TUPLE              1
        # 50 LOAD_FAST                0 (self)
        # 52 LOAD_ATTR                4 (__metadata__)
        # 62 BINARY_OP                0 (+)
        # 1159          66 BUILD_TUPLE              2
        # 68 BUILD_TUPLE              2
        # 70 RETURN_VALUE

    def __eq__(self, other):
        # 1163           0 RESUME                   0
        # 1164           2 LOAD_GLOBAL              1 (NULL + isinstance)
        # 14 LOAD_FAST                1 (other)
        # 16 LOAD_GLOBAL              2 (_AnnotatedAlias)
        # 28 PRECALL                  2
        # 32 CALL                     2
        # 42 POP_JUMP_FORWARD_IF_TRUE     7 (to 58)
        # 1165          44 LOAD_GLOBAL              4 (NotImplemented)
        # 56 RETURN_VALUE
        # 1166     >>   58 LOAD_FAST                0 (self)
        # 60 LOAD_ATTR                3 (__origin__)
        # 70 LOAD_FAST                1 (other)
        # 72 LOAD_ATTR                3 (__origin__)
        # 82 COMPARE_OP               3 (!=)
        # 88 POP_JUMP_FORWARD_IF_FALSE     2 (to 94)
        # 1167          90 LOAD_CONST               1 (False)
        # 92 RETURN_VALUE
        # 1168     >>   94 LOAD_FAST                0 (self)
        # 96 LOAD_ATTR                4 (__metadata__)
        # 106 LOAD_FAST                1 (other)
        # 108 LOAD_ATTR                4 (__metadata__)
        # 118 COMPARE_OP               2 (==)
        # 124 RETURN_VALUE

    def __hash__(self):
        # 1170           0 RESUME                   0
        # 1171           2 LOAD_GLOBAL              1 (NULL + hash)
        # 14 LOAD_FAST                0 (self)
        # 16 LOAD_ATTR                1 (__origin__)
        # 26 LOAD_FAST                0 (self)
        # 28 LOAD_ATTR                2 (__metadata__)
        # 38 BUILD_TUPLE              2
        # 40 PRECALL                  1
        # 44 CALL                     1
        # 54 RETURN_VALUE


class Annotated:
    """Annotated"""
    def __new__(cls):
        # 1208           0 RESUME                   0
        # 1209           2 LOAD_GLOBAL              1 (NULL + TypeError)
        # 14 LOAD_CONST               1 ('Type Annotated cannot be instantiated.')
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 RAISE_VARARGS            1

    def __class_getitem__(cls, params):
        # 1211           0 RESUME                   0
        # 1213           2 LOAD_GLOBAL              1 (NULL + isinstance)
        # 14 LOAD_FAST                1 (params)
        # 16 LOAD_GLOBAL              2 (tuple)
        # 28 PRECALL                  2
        # 32 CALL                     2
        # 42 POP_JUMP_FORWARD_IF_FALSE    19 (to 82)
        # 44 LOAD_GLOBAL              5 (NULL + len)
        # 56 LOAD_FAST                1 (params)
        # 58 PRECALL                  1
        # 62 CALL                     1
        # 72 LOAD_CONST               1 (2)
        # 74 COMPARE_OP               0 (<)
        # 80 POP_JUMP_FORWARD_IF_FALSE    15 (to 112)
        # 1214     >>   82 LOAD_GLOBAL              7 (NULL + TypeError)
        # 94 LOAD_CONST               2 ('Annotated[...] should be used with at least two arguments (a type and an annotation).')
        # 96 PRECALL                  1
        # 100 CALL                     1
        # 110 RAISE_VARARGS            1
        # 1217     >>  112 LOAD_CONST               3 ('Annotated[t, ...]: t must be a type.')
        # 114 STORE_FAST               2 (msg)
        # 1218         116 LOAD_GLOBAL              9 (NULL + typing)
        # 128 LOAD_ATTR                5 (_type_check)
        # 138 LOAD_FAST                1 (params)
        # 140 LOAD_CONST               4 (0)
        # 142 BINARY_SUBSCR
        # 152 LOAD_FAST                2 (msg)
        # 154 PRECALL                  2
        # 158 CALL                     2
        # 168 STORE_FAST               3 (origin)
        # 1219         170 LOAD_GLOBAL              3 (NULL + tuple)
        # 182 LOAD_FAST                1 (params)
        # 184 LOAD_CONST               5 (1)
        # 186 LOAD_CONST               0 (None)
        # 188 BUILD_SLICE              2
        # 190 BINARY_SUBSCR
        # 200 PRECALL                  1
        # 204 CALL                     1
        # 214 STORE_FAST               4 (metadata)
        # 1220         216 LOAD_GLOBAL             13 (NULL + _AnnotatedAlias)
        # 228 LOAD_FAST                3 (origin)
        # 230 LOAD_FAST                4 (metadata)
        # 232 PRECALL                  2
        # 236 CALL                     2
        # 246 RETURN_VALUE

    def __init_subclass__(cls):
        # 1222           0 RESUME                   0
        # 1223           2 LOAD_GLOBAL              1 (NULL + TypeError)
        # 1224          14 LOAD_CONST               1 ('Cannot subclass ')
        # 16 LOAD_FAST                0 (cls)
        # 18 LOAD_ATTR                1 (__module__)
        # 28 FORMAT_VALUE             0
        # 30 LOAD_CONST               2 ('.Annotated')
        # 32 BUILD_STRING             3
        # 1223          34 PRECALL                  1
        # 38 CALL                     1
        # 48 RAISE_VARARGS            1


def _strip_annotations(t):
    """Strips the annotations from a given type.
        """
    # 1227           0 RESUME                   0
    # 1230           2 LOAD_GLOBAL              1 (NULL + isinstance)
    # 14 LOAD_FAST                0 (t)
    # 16 LOAD_GLOBAL              2 (_AnnotatedAlias)
    # 28 PRECALL                  2
    # 32 CALL                     2
    # 42 POP_JUMP_FORWARD_IF_FALSE    20 (to 84)
    # 1231          44 LOAD_GLOBAL              5 (NULL + _strip_annotations)
    # 56 LOAD_FAST                0 (t)
    # 58 LOAD_ATTR                3 (__origin__)
    # 68 PRECALL                  1
    # 72 CALL                     1
    # 82 RETURN_VALUE
    # 1232     >>   84 LOAD_GLOBAL              1 (NULL + isinstance)
    # 96 LOAD_FAST                0 (t)
    # 98 LOAD_GLOBAL              8 (typing)
    # 110 LOAD_ATTR                5 (_GenericAlias)
    # 120 PRECALL                  2
    # 124 CALL                     2
    # 134 POP_JUMP_FORWARD_IF_FALSE    78 (to 292)
    # 1233         136 LOAD_GLOBAL             13 (NULL + tuple)
    # 148 LOAD_CONST               1 (<code object <genexpr> at 0x000001EBD7EE9890, file "setuptools\_vendor\typing_extensions.py", line 1233>)
    # 150 MAKE_FUNCTION            0
    # 152 LOAD_FAST                0 (t)
    # 154 LOAD_ATTR                7 (__args__)
    # 164 GET_ITER
    # 166 PRECALL                  0
    # 170 CALL                     0
    # 180 PRECALL                  1
    # 184 CALL                     1
    # 194 STORE_FAST               1 (stripped_args)
    # 1234         196 LOAD_FAST                1 (stripped_args)
    # 198 LOAD_FAST                0 (t)
    # 200 LOAD_ATTR                7 (__args__)
    # 210 COMPARE_OP               2 (==)
    # 216 POP_JUMP_FORWARD_IF_FALSE     2 (to 222)
    # 1235         218 LOAD_FAST                0 (t)
    # 220 RETURN_VALUE
    # 1236     >>  222 LOAD_FAST                0 (t)
    # 224 LOAD_METHOD              8 (copy_with)
    # 246 LOAD_FAST                1 (stripped_args)
    # 248 PRECALL                  1
    # 252 CALL                     1
    # 262 STORE_FAST               2 (res)
    # 1237         264 LOAD_FAST                0 (t)
    # 266 LOAD_ATTR                9 (_special)
    # 276 LOAD_FAST                2 (res)
    # 278 STORE_ATTR               9 (_special)
    # 1238         288 LOAD_FAST                2 (res)
    # 290 RETURN_VALUE
    # 1239     >>  292 LOAD_FAST                0 (t)
    # 294 RETURN_VALUE
    # Disassembly of <code object <genexpr> at 0x000001EBD7EE9890, file "setuptools\_vendor\typing_extensions.py", line 1233>:
    # 1233           0 RETURN_GENERATOR
    # 2 POP_TOP
    # 4 RESUME                   0
    # 6 LOAD_FAST                0 (.0)
    # >>    8 FOR_ITER                19 (to 48)
    # 10 STORE_FAST               1 (a)
    # 12 LOAD_GLOBAL              1 (NULL + _strip_annotations)
    # 24 LOAD_FAST                1 (a)
    # 26 PRECALL                  1
    # 30 CALL                     1
    # 40 YIELD_VALUE
    # 42 RESUME                   1
    # 44 POP_TOP
    # 46 JUMP_BACKWARD           20 (to 8)
    # >>   48 LOAD_CONST               0 (None)
    # 50 RETURN_VALUE

def get_type_hints(obj, globalns, localns, include_extras):
    """Return type hints for an object.

        This is often the same as obj.__annotations__, but it handles
        forward references encoded as string literals, adds Optional[t] if a
        default value equal to None is set and recursively replaces all
        'Annotated[T, ...]' with 'T' (unless 'include_extras=True').

        The argument may be a module, class, method, or function. The annotations
        are returned as a dictionary. For classes, annotations include also
        inherited members.

        TypeError is raised if the argument is not of a type that can contain
        annotations, and an empty dictionary is returned if no annotations are
        present.

        BEWARE -- the behavior of globalns and localns is counterintuitive
        (unless you are familiar with how eval() and exec() work).  The
        search order is locals first, then globals.

        - If no dict arguments are passed, an attempt is made to use the
          globals from obj (or the respective module's globals for classes),
          and these are also used as the locals.  If the object does not appear
          to have globals, an empty dictionary is used.

        - If one dict argument is passed, it is used for both globals and
          locals.

        - If two dict arguments are passed, they specify globals and
          locals, respectively.
        """
    # 1241           0 RESUME                   0
    # 1272           2 LOAD_GLOBAL              1 (NULL + typing)
    # 14 LOAD_ATTR                1 (get_type_hints)
    # 24 LOAD_FAST                0 (obj)
    # 26 LOAD_FAST                1 (globalns)
    # 28 LOAD_FAST                2 (localns)
    # 30 KW_NAMES                 1
    # 32 PRECALL                  3
    # 36 CALL                     3
    # 46 STORE_FAST               4 (hint)
    # 1273          48 LOAD_FAST                3 (include_extras)
    # 50 POP_JUMP_FORWARD_IF_FALSE     2 (to 56)
    # 1274          52 LOAD_FAST                4 (hint)
    # 54 RETURN_VALUE
    # 1275     >>   56 LOAD_CONST               2 (<code object <dictcomp> at 0x000001EBD7EE9980, file "setuptools\_vendor\typing_extensions.py", line 1275>)
    # 58 MAKE_FUNCTION            0
    # 60 LOAD_FAST                4 (hint)
    # 62 LOAD_METHOD              2 (items)
    # 84 PRECALL                  0
    # 88 CALL                     0
    # 98 GET_ITER
    # 100 PRECALL                  0
    # 104 CALL                     0
    # 114 RETURN_VALUE
    # Disassembly of <code object <dictcomp> at 0x000001EBD7EE9980, file "setuptools\_vendor\typing_extensions.py", line 1275>:
    # 1275           0 RESUME                   0
    # 2 BUILD_MAP                0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER                21 (to 50)
    # 8 UNPACK_SEQUENCE          2
    # 12 STORE_FAST               1 (k)
    # 14 STORE_FAST               2 (t)
    # 16 LOAD_FAST                1 (k)
    # 18 LOAD_GLOBAL              1 (NULL + _strip_annotations)
    # 30 LOAD_FAST                2 (t)
    # 32 PRECALL                  1
    # 36 CALL                     1
    # 46 MAP_ADD                  2
    # 48 JUMP_BACKWARD           22 (to 6)
    # >>   50 RETURN_VALUE

def _is_dunder(name):
    """Returns True if name is a __dunder_variable_name__."""
    # 1279           0 RESUME                   0
    # 1281           2 LOAD_GLOBAL              1 (NULL + len)
    # 14 LOAD_FAST                0 (name)
    # 16 PRECALL                  1
    # 20 CALL                     1
    # 30 LOAD_CONST               1 (4)
    # 32 COMPARE_OP               4 (>)
    # 38 JUMP_IF_FALSE_OR_POP    41 (to 122)
    # 40 LOAD_FAST                0 (name)
    # 42 LOAD_METHOD              1 (startswith)
    # 64 LOAD_CONST               2 ('__')
    # 66 PRECALL                  1
    # 70 CALL                     1
    # 80 JUMP_IF_FALSE_OR_POP    20 (to 122)
    # 82 LOAD_FAST                0 (name)
    # 84 LOAD_METHOD              2 (endswith)
    # 106 LOAD_CONST               2 ('__')
    # 108 PRECALL                  1
    # 112 CALL                     1
    # >>  122 RETURN_VALUE

class AnnotatedMeta:
    """AnnotatedMeta"""
    def __new__(cls, name, bases, namespace):
        # 0 COPY_FREE_VARS           1
        # 1290           2 RESUME                   0
        # 1291           4 LOAD_GLOBAL              1 (NULL + any)
        # 16 LOAD_CONST               1 (<code object <genexpr> at 0x000001EBD7EBA790, file "setuptools\_vendor\typing_extensions.py", line 1291>)
        # 18 MAKE_FUNCTION            0
        # 20 LOAD_FAST                2 (bases)
        # 22 GET_ITER
        # 24 PRECALL                  0
        # 28 CALL                     0
        # 38 PRECALL                  1
        # 42 CALL                     1
        # 52 POP_JUMP_FORWARD_IF_FALSE    36 (to 126)
        # 1292          54 LOAD_GLOBAL              3 (NULL + TypeError)
        # 66 LOAD_CONST               2 ('Cannot subclass ')
        # 68 LOAD_GLOBAL              5 (NULL + str)
        # 80 LOAD_GLOBAL              6 (Annotated)
        # 92 PRECALL                  1
        # 96 CALL                     1
        # 106 BINARY_OP                0 (+)
        # 110 PRECALL                  1
        # 114 CALL                     1
        # 124 RAISE_VARARGS            1
        # 1293     >>  126 PUSH_NULL
        # 128 LOAD_GLOBAL              9 (NULL + super)
        # 140 PRECALL                  0
        # 144 CALL                     0
        # 154 LOAD_ATTR                5 (__new__)
        # 164 LOAD_FAST                0 (cls)
        # 166 LOAD_FAST                1 (name)
        # 168 LOAD_FAST                2 (bases)
        # 170 LOAD_FAST                3 (namespace)
        # 172 BUILD_TUPLE              4
        # 174 BUILD_MAP                0
        # 176 LOAD_FAST                4 (kwargs)
        # 178 DICT_MERGE               1
        # 180 CALL_FUNCTION_EX         1
        # 182 RETURN_VALUE
        # Disassembly of <code object <genexpr> at 0x000001EBD7EBA790, file "setuptools\_vendor\typing_extensions.py", line 1291>:
        # 1291           0 RETURN_GENERATOR
        # 2 POP_TOP
        # 4 RESUME                   0
        # 6 LOAD_FAST                0 (.0)
        # >>    8 FOR_ITER                13 (to 36)
        # 10 STORE_FAST               1 (b)
        # 12 LOAD_FAST                1 (b)
        # 14 LOAD_GLOBAL              0 (object)
        # 26 IS_OP                    1
        # 28 YIELD_VALUE
        # 30 RESUME                   1
        # 32 POP_TOP
        # 34 JUMP_BACKWARD           14 (to 8)
        # >>   36 LOAD_CONST               0 (None)
        # 38 RETURN_VALUE

    def __metadata__(self):
        # 1295           0 RESUME                   0
        # 1297           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (_subs_tree)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 LOAD_CONST               1 (2)
        # 42 BINARY_SUBSCR
        # 52 RETURN_VALUE

    def _tree_repr(self, tree):
        # 1299           0 RESUME                   0
        # 1300           2 LOAD_FAST                1 (tree)
        # 4 UNPACK_SEQUENCE          3
        # 8 STORE_FAST               2 (cls)
        # 10 STORE_FAST               3 (origin)
        # 12 STORE_FAST               4 (metadata)
        # 1301          14 LOAD_GLOBAL              1 (NULL + isinstance)
        # 26 LOAD_FAST                3 (origin)
        # 28 LOAD_GLOBAL              2 (tuple)
        # 40 PRECALL                  2
        # 44 CALL                     2
        # 54 POP_JUMP_FORWARD_IF_TRUE    21 (to 98)
        # 1302          56 LOAD_GLOBAL              5 (NULL + typing)
        # 68 LOAD_ATTR                3 (_type_repr)
        # 78 LOAD_FAST                3 (origin)
        # 80 PRECALL                  1
        # 84 CALL                     1
        # 94 STORE_FAST               5 (tp_repr)
        # 96 JUMP_FORWARD            27 (to 152)
        # 1304     >>   98 LOAD_FAST                3 (origin)
        # 100 LOAD_CONST               1 (0)
        # 102 BINARY_SUBSCR
        # 112 LOAD_METHOD              4 (_tree_repr)
        # 134 LOAD_FAST                3 (origin)
        # 136 PRECALL                  1
        # 140 CALL                     1
        # 150 STORE_FAST               5 (tp_repr)
        # 1305     >>  152 LOAD_CONST               2 (', ')
        # 154 LOAD_METHOD              5 (join)
        # 176 LOAD_CONST               3 (<code object <genexpr> at 0x000001EBD7EE9B60, file "setuptools\_vendor\typing_extensions.py", line 1305>)
        # 178 MAKE_FUNCTION            0
        # 180 LOAD_FAST                4 (metadata)
        # 182 GET_ITER
        # 184 PRECALL                  0
        # 188 CALL                     0
        # 198 PRECALL                  1
        # 202 CALL                     1
        # 212 STORE_FAST               6 (metadata_reprs)
        # 1306         214 LOAD_FAST                2 (cls)
        # 216 FORMAT_VALUE             0
        # 218 LOAD_CONST               4 ('[')
        # 220 LOAD_FAST                5 (tp_repr)
        # 222 FORMAT_VALUE             0
        # 224 LOAD_CONST               2 (', ')
        # 226 LOAD_FAST                6 (metadata_reprs)
        # 228 FORMAT_VALUE             0
        # 230 LOAD_CONST               5 (']')
        # 232 BUILD_STRING             6
        # 234 RETURN_VALUE
        # Disassembly of <code object <genexpr> at 0x000001EBD7EE9B60, file "setuptools\_vendor\typing_extensions.py", line 1305>:
        # 1305           0 RETURN_GENERATOR
        # 2 POP_TOP
        # 4 RESUME                   0
        # 6 LOAD_FAST                0 (.0)
        # >>    8 FOR_ITER                19 (to 48)
        # 10 STORE_FAST               1 (arg)
        # 12 LOAD_GLOBAL              1 (NULL + repr)
        # 24 LOAD_FAST                1 (arg)
        # 26 PRECALL                  1
        # 30 CALL                     1
        # 40 YIELD_VALUE
        # 42 RESUME                   1
        # 44 POP_TOP
        # 46 JUMP_BACKWARD           20 (to 8)
        # >>   48 LOAD_CONST               0 (None)
        # 50 RETURN_VALUE

    def _subs_tree(self, tvars, args):
        # 0 COPY_FREE_VARS           1
        # 1308           2 RESUME                   0
        # 1309           4 LOAD_FAST                0 (self)
        # 6 LOAD_GLOBAL              0 (Annotated)
        # 18 IS_OP                    0
        # 20 POP_JUMP_FORWARD_IF_FALSE     7 (to 36)
        # 1310          22 LOAD_GLOBAL              0 (Annotated)
        # 34 RETURN_VALUE
        # 1311     >>   36 LOAD_GLOBAL              3 (NULL + super)
        # 48 PRECALL                  0
        # 52 CALL                     0
        # 62 LOAD_METHOD              2 (_subs_tree)
        # 84 LOAD_FAST                1 (tvars)
        # 86 LOAD_FAST                2 (args)
        # 88 KW_NAMES                 1
        # 90 PRECALL                  2
        # 94 CALL                     2
        # 104 STORE_FAST               3 (res)
        # 1313         106 LOAD_GLOBAL              7 (NULL + isinstance)
        # 118 LOAD_FAST                3 (res)
        # 120 LOAD_CONST               2 (1)
        # 122 BINARY_SUBSCR
        # 132 LOAD_GLOBAL              8 (tuple)
        # 144 PRECALL                  2
        # 148 CALL                     2
        # 158 POP_JUMP_FORWARD_IF_FALSE    68 (to 296)
        # 160 LOAD_FAST                3 (res)
        # 162 LOAD_CONST               2 (1)
        # 164 BINARY_SUBSCR
        # 174 LOAD_CONST               3 (0)
        # 176 BINARY_SUBSCR
        # 186 LOAD_GLOBAL              0 (Annotated)
        # 198 IS_OP                    0
        # 200 POP_JUMP_FORWARD_IF_FALSE    47 (to 296)
        # 1314         202 LOAD_FAST                3 (res)
        # 204 LOAD_CONST               2 (1)
        # 206 BINARY_SUBSCR
        # 216 LOAD_CONST               2 (1)
        # 218 BINARY_SUBSCR
        # 228 STORE_FAST               4 (sub_tp)
        # 1315         230 LOAD_FAST                3 (res)
        # 232 LOAD_CONST               2 (1)
        # 234 BINARY_SUBSCR
        # 244 LOAD_CONST               4 (2)
        # 246 BINARY_SUBSCR
        # 256 STORE_FAST               5 (sub_annot)
        # 1316         258 LOAD_GLOBAL              0 (Annotated)
        # 270 LOAD_FAST                4 (sub_tp)
        # 272 LOAD_FAST                5 (sub_annot)
        # 274 LOAD_FAST                3 (res)
        # 276 LOAD_CONST               4 (2)
        # 278 BINARY_SUBSCR
        # 288 BINARY_OP                0 (+)
        # 292 BUILD_TUPLE              3
        # 294 RETURN_VALUE
        # 1317     >>  296 LOAD_FAST                3 (res)
        # 298 RETURN_VALUE

    def _get_cons(self):
        """Return the class used to create instance of this type."""
        # 1319           0 RESUME                   0
        # 1321           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (__origin__)
        # 14 POP_JUMP_FORWARD_IF_NOT_NONE    15 (to 46)
        # 1322          16 LOAD_GLOBAL              3 (NULL + TypeError)
        # 28 LOAD_CONST               2 ('Cannot get the underlying type of a non-specialized Annotated type.')
        # 30 PRECALL                  1
        # 34 CALL                     1
        # 44 RAISE_VARARGS            1
        # 1324     >>   46 LOAD_FAST                0 (self)
        # 48 LOAD_METHOD              2 (_subs_tree)
        # 70 PRECALL                  0
        # 74 CALL                     0
        # 84 STORE_FAST               1 (tree)
        # 1325          86 LOAD_GLOBAL              7 (NULL + isinstance)
        # 98 LOAD_FAST                1 (tree)
        # 100 LOAD_GLOBAL              8 (tuple)
        # 112 PRECALL                  2
        # 116 CALL                     2
        # 126 POP_JUMP_FORWARD_IF_FALSE    59 (to 246)
        # 128 LOAD_FAST                1 (tree)
        # 130 LOAD_CONST               3 (0)
        # 132 BINARY_SUBSCR
        # 142 LOAD_GLOBAL             10 (Annotated)
        # 154 IS_OP                    0
        # 156 POP_JUMP_FORWARD_IF_FALSE    44 (to 246)
        # 1326     >>  158 LOAD_FAST                1 (tree)
        # 160 LOAD_CONST               4 (1)
        # 162 BINARY_SUBSCR
        # 172 STORE_FAST               1 (tree)
        # 1325         174 LOAD_GLOBAL              7 (NULL + isinstance)
        # 186 LOAD_FAST                1 (tree)
        # 188 LOAD_GLOBAL              8 (tuple)
        # 200 PRECALL                  2
        # 204 CALL                     2
        # 214 POP_JUMP_FORWARD_IF_FALSE    15 (to 246)
        # 216 LOAD_FAST                1 (tree)
        # 218 LOAD_CONST               3 (0)
        # 220 BINARY_SUBSCR
        # 230 LOAD_GLOBAL             10 (Annotated)
        # 242 IS_OP                    0
        # 244 POP_JUMP_BACKWARD_IF_TRUE    44 (to 158)
        # 1327     >>  246 LOAD_GLOBAL              7 (NULL + isinstance)
        # 258 LOAD_FAST                1 (tree)
        # 260 LOAD_GLOBAL              8 (tuple)
        # 272 PRECALL                  2
        # 276 CALL                     2
        # 286 POP_JUMP_FORWARD_IF_FALSE     8 (to 304)
        # 1328         288 LOAD_FAST                1 (tree)
        # 290 LOAD_CONST               3 (0)
        # 292 BINARY_SUBSCR
        # 302 RETURN_VALUE
        # 1330     >>  304 LOAD_FAST                1 (tree)
        # 306 RETURN_VALUE

    def __getitem__(self, params):
        # 0 COPY_FREE_VARS           1
        # 1332           2 RESUME                   0
        # 1334           4 LOAD_GLOBAL              1 (NULL + isinstance)
        # 16 LOAD_FAST                1 (params)
        # 18 LOAD_GLOBAL              2 (tuple)
        # 30 PRECALL                  2
        # 34 CALL                     2
        # 44 POP_JUMP_FORWARD_IF_TRUE     3 (to 52)
        # 1335          46 LOAD_FAST                1 (params)
        # 48 BUILD_TUPLE              1
        # 50 STORE_FAST               1 (params)
        # 1336     >>   52 LOAD_FAST                0 (self)
        # 54 LOAD_ATTR                2 (__origin__)
        # 64 POP_JUMP_FORWARD_IF_NONE    33 (to 132)
        # 1337          66 LOAD_GLOBAL              7 (NULL + super)
        # 78 PRECALL                  0
        # 82 CALL                     0
        # 92 LOAD_METHOD              4 (__getitem__)
        # 114 LOAD_FAST                1 (params)
        # 116 PRECALL                  1
        # 120 CALL                     1
        # 130 RETURN_VALUE
        # 1338     >>  132 LOAD_GLOBAL              1 (NULL + isinstance)
        # 144 LOAD_FAST                1 (params)
        # 146 LOAD_GLOBAL              2 (tuple)
        # 158 PRECALL                  2
        # 162 CALL                     2
        # 172 POP_JUMP_FORWARD_IF_FALSE    19 (to 212)
        # 174 LOAD_GLOBAL             11 (NULL + len)
        # 186 LOAD_FAST                1 (params)
        # 188 PRECALL                  1
        # 192 CALL                     1
        # 202 LOAD_CONST               1 (2)
        # 204 COMPARE_OP               0 (<)
        # 210 POP_JUMP_FORWARD_IF_FALSE    15 (to 242)
        # 1339     >>  212 LOAD_GLOBAL             13 (NULL + TypeError)
        # 224 LOAD_CONST               2 ('Annotated[...] should be instantiated with at least two arguments (a type and an annotation).')
        # 226 PRECALL                  1
        # 230 CALL                     1
        # 240 RAISE_VARARGS            1
        # 1343     >>  242 LOAD_CONST               3 ('Annotated[t, ...]: t must be a type.')
        # 244 STORE_FAST               2 (msg)
        # 1344         246 LOAD_GLOBAL             15 (NULL + typing)
        # 258 LOAD_ATTR                8 (_type_check)
        # 268 LOAD_FAST                1 (params)
        # 270 LOAD_CONST               4 (0)
        # 272 BINARY_SUBSCR
        # 282 LOAD_FAST                2 (msg)
        # 284 PRECALL                  2
        # 288 CALL                     2
        # 298 STORE_FAST               3 (tp)
        # 1345         300 LOAD_GLOBAL              3 (NULL + tuple)
        # 312 LOAD_FAST                1 (params)
        # 314 LOAD_CONST               5 (1)
        # 316 LOAD_CONST               0 (None)
        # 318 BUILD_SLICE              2
        # 320 BINARY_SUBSCR
        # 330 PRECALL                  1
        # 334 CALL                     1
        # 344 STORE_FAST               4 (metadata)
        # 1346         346 LOAD_FAST                0 (self)
        # 348 LOAD_METHOD              9 (__class__)
        # 1347         370 LOAD_FAST                0 (self)
        # 372 LOAD_ATTR               10 (__name__)
        # 1348         382 LOAD_FAST                0 (self)
        # 384 LOAD_ATTR               11 (__bases__)
        # 1349         394 LOAD_GLOBAL             25 (NULL + _no_slots_copy)
        # 406 LOAD_FAST                0 (self)
        # 408 LOAD_ATTR               13 (__dict__)
        # 418 PRECALL                  1
        # 422 CALL                     1
        # 1350         432 LOAD_GLOBAL             29 (NULL + _type_vars)
        # 444 LOAD_FAST                3 (tp)
        # 446 BUILD_TUPLE              1
        # 448 PRECALL                  1
        # 452 CALL                     1
        # 1352         462 LOAD_FAST                3 (tp)
        # 464 LOAD_FAST                4 (metadata)
        # 466 BUILD_TUPLE              2
        # 1353         468 LOAD_FAST                0 (self)
        # 1346         470 KW_NAMES                 6
        # 472 PRECALL                  6
        # 476 CALL                     6
        # 486 RETURN_VALUE

    def __call__(self):
        # 1356           0 RESUME                   0
        # 1357           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (_get_cons)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 STORE_FAST               3 (cons)
        # 1358          42 PUSH_NULL
        # 44 LOAD_FAST                3 (cons)
        # 46 LOAD_FAST                1 (args)
        # 48 BUILD_MAP                0
        # 50 LOAD_FAST                2 (kwargs)
        # 52 DICT_MERGE               1
        # 54 CALL_FUNCTION_EX         1
        # 56 STORE_FAST               4 (result)
        # 1359          58 NOP
        # 1360          60 LOAD_FAST                0 (self)
        # 62 LOAD_FAST                4 (result)
        # 64 STORE_ATTR               1 (__orig_class__)
        # 74 JUMP_FORWARD            16 (to 108)
        # >>   76 PUSH_EXC_INFO
        # 1361          78 LOAD_GLOBAL              4 (AttributeError)
        # 90 CHECK_EXC_MATCH
        # 92 POP_JUMP_FORWARD_IF_FALSE     3 (to 100)
        # 94 POP_TOP
        # 1362          96 POP_EXCEPT
        # 98 JUMP_FORWARD             4 (to 108)
        # 1361     >>  100 RERAISE                  0
        # >>  102 COPY                     3
        # 104 POP_EXCEPT
        # 106 RERAISE                  1
        # 1363     >>  108 LOAD_FAST                4 (result)
        # 110 RETURN_VALUE
        # ExceptionTable:
        # 60 to 72 -> 76 [0]
        # 76 to 94 -> 102 [1] lasti
        # 100 to 100 -> 102 [1] lasti

    def __getattr__(self, attr):
        # 1365           0 RESUME                   0
        # 1367           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (__origin__)
        # 14 POP_JUMP_FORWARD_IF_NONE    49 (to 114)
        # 16 LOAD_GLOBAL              3 (NULL + _is_dunder)
        # 28 LOAD_FAST                1 (attr)
        # 30 PRECALL                  1
        # 34 CALL                     1
        # 44 POP_JUMP_FORWARD_IF_TRUE    34 (to 114)
        # 1368          46 LOAD_GLOBAL              5 (NULL + getattr)
        # 58 LOAD_FAST                0 (self)
        # 60 LOAD_METHOD              3 (_get_cons)
        # 82 PRECALL                  0
        # 86 CALL                     0
        # 96 LOAD_FAST                1 (attr)
        # 98 PRECALL                  2
        # 102 CALL                     2
        # 112 RETURN_VALUE
        # 1369     >>  114 LOAD_GLOBAL              9 (NULL + AttributeError)
        # 126 LOAD_FAST                1 (attr)
        # 128 PRECALL                  1
        # 132 CALL                     1
        # 142 RAISE_VARARGS            1

    def __setattr__(self, attr, value):
        # 0 COPY_FREE_VARS           1
        # 1371           2 RESUME                   0
        # 1372           4 LOAD_GLOBAL              1 (NULL + _is_dunder)
        # 16 LOAD_FAST                1 (attr)
        # 18 PRECALL                  1
        # 22 CALL                     1
        # 32 POP_JUMP_FORWARD_IF_TRUE    21 (to 76)
        # 34 LOAD_FAST                1 (attr)
        # 36 LOAD_METHOD              1 (startswith)
        # 58 LOAD_CONST               1 ('_abc_')
        # 60 PRECALL                  1
        # 64 CALL                     1
        # 74 POP_JUMP_FORWARD_IF_FALSE    36 (to 148)
        # 1373     >>   76 LOAD_GLOBAL              5 (NULL + super)
        # 88 PRECALL                  0
        # 92 CALL                     0
        # 102 LOAD_METHOD              3 (__setattr__)
        # 124 LOAD_FAST                1 (attr)
        # 126 LOAD_FAST                2 (value)
        # 128 PRECALL                  2
        # 132 CALL                     2
        # 142 POP_TOP
        # 144 LOAD_CONST               0 (None)
        # 146 RETURN_VALUE
        # 1374     >>  148 LOAD_FAST                0 (self)
        # 150 LOAD_ATTR                4 (__origin__)
        # 160 POP_JUMP_FORWARD_IF_NOT_NONE    15 (to 192)
        # 1375         162 LOAD_GLOBAL             11 (NULL + AttributeError)
        # 174 LOAD_FAST                1 (attr)
        # 176 PRECALL                  1
        # 180 CALL                     1
        # 190 RAISE_VARARGS            1
        # 1377     >>  192 LOAD_GLOBAL             13 (NULL + setattr)
        # 204 LOAD_FAST                0 (self)
        # 206 LOAD_METHOD              7 (_get_cons)
        # 228 PRECALL                  0
        # 232 CALL                     0
        # 242 LOAD_FAST                1 (attr)
        # 244 LOAD_FAST                2 (value)
        # 246 PRECALL                  3
        # 250 CALL                     3
        # 260 POP_TOP
        # 262 LOAD_CONST               0 (None)
        # 264 RETURN_VALUE

    def __instancecheck__(self, obj):
        # 1379           0 RESUME                   0
        # 1380           2 LOAD_GLOBAL              1 (NULL + TypeError)
        # 14 LOAD_CONST               1 ('Annotated cannot be used with isinstance().')
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 RAISE_VARARGS            1

    def __subclasscheck__(self, cls):
        # 1382           0 RESUME                   0
        # 1383           2 LOAD_GLOBAL              1 (NULL + TypeError)
        # 14 LOAD_CONST               1 ('Annotated cannot be used with issubclass().')
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 RAISE_VARARGS            1


def get_origin(tp):
    """Get the unsubscripted version of a type.

        This supports generic types, Callable, Tuple, Union, Literal, Final, ClassVar
        and Annotated. Return None for unsupported types. Examples::

            get_origin(Literal[42]) is Literal
            get_origin(int) is None
            get_origin(ClassVar[int]) is ClassVar
            get_origin(Generic) is Generic
            get_origin(Generic[T]) is Generic
            get_origin(Union[T, int]) is Union
            get_origin(List[Tuple[T, T]][int]) == list
            get_origin(P.args) is P
        """
    # 1436           0 RESUME                   0
    # 1451           2 LOAD_GLOBAL              1 (NULL + isinstance)
    # 14 LOAD_FAST                0 (tp)
    # 16 LOAD_GLOBAL              2 (_AnnotatedAlias)
    # 28 PRECALL                  2
    # 32 CALL                     2
    # 42 POP_JUMP_FORWARD_IF_FALSE     7 (to 58)
    # 1452          44 LOAD_GLOBAL              4 (Annotated)
    # 56 RETURN_VALUE
    # 1453     >>   58 LOAD_GLOBAL              1 (NULL + isinstance)
    # 70 LOAD_FAST                0 (tp)
    # 72 LOAD_GLOBAL              6 (typing)
    # 84 LOAD_ATTR                4 (_GenericAlias)
    # 94 LOAD_GLOBAL             10 (GenericAlias)
    # 106 LOAD_GLOBAL             12 (_BaseGenericAlias)
    # 1454         118 LOAD_GLOBAL             14 (ParamSpecArgs)
    # 130 LOAD_GLOBAL             16 (ParamSpecKwargs)
    # 1453         142 BUILD_TUPLE              5
    # 144 PRECALL                  2
    # 148 CALL                     2
    # 158 POP_JUMP_FORWARD_IF_FALSE     7 (to 174)
    # 1455         160 LOAD_FAST                0 (tp)
    # 162 LOAD_ATTR                9 (__origin__)
    # 172 RETURN_VALUE
    # 1456     >>  174 LOAD_FAST                0 (tp)
    # 176 LOAD_GLOBAL              6 (typing)
    # 188 LOAD_ATTR               10 (Generic)
    # 198 IS_OP                    0
    # 200 POP_JUMP_FORWARD_IF_FALSE    12 (to 226)
    # 1457         202 LOAD_GLOBAL              6 (typing)
    # 214 LOAD_ATTR               10 (Generic)
    # 224 RETURN_VALUE
    # 1458     >>  226 LOAD_CONST               1 (None)
    # 228 RETURN_VALUE

def get_args(tp):
    """Get type arguments with all substitutions performed.

        For unions, basic simplifications used by Union constructor are performed.
        Examples::
            get_args(Dict[str, int]) == (str, int)
            get_args(int) == ()
            get_args(Union[int, Union[T, int], str][int]) == (int, str)
            get_args(Union[int, Tuple[T, int]][str]) == (int, Tuple[str, int])
            get_args(Callable[[], T][int]) == ([], int)
        """
    # 1460           0 RESUME                   0
    # 1471           2 LOAD_GLOBAL              1 (NULL + isinstance)
    # 14 LOAD_FAST                0 (tp)
    # 16 LOAD_GLOBAL              2 (_AnnotatedAlias)
    # 28 PRECALL                  2
    # 32 CALL                     2
    # 42 POP_JUMP_FORWARD_IF_FALSE    16 (to 76)
    # 1472          44 LOAD_FAST                0 (tp)
    # 46 LOAD_ATTR                2 (__origin__)
    # 56 BUILD_TUPLE              1
    # 58 LOAD_FAST                0 (tp)
    # 60 LOAD_ATTR                3 (__metadata__)
    # 70 BINARY_OP                0 (+)
    # 74 RETURN_VALUE
    # 1473     >>   76 LOAD_GLOBAL              1 (NULL + isinstance)
    # 88 LOAD_FAST                0 (tp)
    # 90 LOAD_GLOBAL              8 (typing)
    # 102 LOAD_ATTR                5 (_GenericAlias)
    # 112 LOAD_GLOBAL             12 (GenericAlias)
    # 124 BUILD_TUPLE              2
    # 126 PRECALL                  2
    # 130 CALL                     2
    # 140 POP_JUMP_FORWARD_IF_FALSE   106 (to 354)
    # 1474         142 LOAD_GLOBAL             15 (NULL + getattr)
    # 154 LOAD_FAST                0 (tp)
    # 156 LOAD_CONST               1 ('_special')
    # 158 LOAD_CONST               2 (False)
    # 160 PRECALL                  3
    # 164 CALL                     3
    # 174 POP_JUMP_FORWARD_IF_FALSE     2 (to 180)
    # 1475         176 LOAD_CONST               3 (())
    # 178 RETURN_VALUE
    # 1476     >>  180 LOAD_FAST                0 (tp)
    # 182 LOAD_ATTR                8 (__args__)
    # 192 STORE_FAST               1 (res)
    # 1477         194 LOAD_GLOBAL             19 (NULL + get_origin)
    # 206 LOAD_FAST                0 (tp)
    # 208 PRECALL                  1
    # 212 CALL                     1
    # 222 LOAD_GLOBAL             20 (collections)
    # 234 LOAD_ATTR               11 (abc)
    # 244 LOAD_ATTR               12 (Callable)
    # 254 IS_OP                    0
    # 256 POP_JUMP_FORWARD_IF_FALSE    46 (to 350)
    # 258 LOAD_FAST                1 (res)
    # 260 LOAD_CONST               4 (0)
    # 262 BINARY_SUBSCR
    # 272 LOAD_GLOBAL             26 (Ellipsis)
    # 284 IS_OP                    1
    # 286 POP_JUMP_FORWARD_IF_FALSE    31 (to 350)
    # 1478         288 LOAD_GLOBAL             29 (NULL + list)
    # 300 LOAD_FAST                1 (res)
    # 302 LOAD_CONST               5 (None)
    # 304 LOAD_CONST               6 (-1)
    # 306 BUILD_SLICE              2
    # 308 BINARY_SUBSCR
    # 318 PRECALL                  1
    # 322 CALL                     1
    # 332 LOAD_FAST                1 (res)
    # 334 LOAD_CONST               6 (-1)
    # 336 BINARY_SUBSCR
    # 346 BUILD_TUPLE              2
    # 348 STORE_FAST               1 (res)
    # 1479     >>  350 LOAD_FAST                1 (res)
    # 352 RETURN_VALUE
    # 1480     >>  354 LOAD_CONST               3 (())
    # 356 RETURN_VALUE

class _TypeAliasForm:
    """_TypeAliasForm"""
    def __repr__(self):
        # 1489           0 RESUME                   0
        # 1490           2 LOAD_CONST               1 ('typing_extensions.')
        # 4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (_name)
        # 16 BINARY_OP                0 (+)
        # 20 RETURN_VALUE


def TypeAlias(self, parameters):
    """Special marker indicating that an assignment should
        be recognized as a proper type alias definition by type
        checkers.

        For example::

            Predicate: TypeAlias = Callable[..., bool]

        It's invalid when used anywhere except as in the example above.
        """
    # 1492           0 RESUME                   0
    # 1504           2 LOAD_GLOBAL              1 (NULL + TypeError)
    # 14 LOAD_FAST                0 (self)
    # 16 FORMAT_VALUE             0
    # 18 LOAD_CONST               1 (' is not subscriptable')
    # 20 BUILD_STRING             2
    # 22 PRECALL                  1
    # 26 CALL                     1
    # 36 RAISE_VARARGS            1

class _TypeAliasMeta:
    """_TypeAliasMeta"""
    def __repr__(self):
        # 1527           0 RESUME                   0
        # 1528           2 LOAD_CONST               1 ('typing_extensions.TypeAlias')
        # 4 RETURN_VALUE


class _TypeAliasBase:
    """_TypeAliasBase"""
    def __instancecheck__(self, obj):
        # 1543           0 RESUME                   0
        # 1544           2 LOAD_GLOBAL              1 (NULL + TypeError)
        # 14 LOAD_CONST               1 ('TypeAlias cannot be used with isinstance().')
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 RAISE_VARARGS            1

    def __subclasscheck__(self, cls):
        # 1546           0 RESUME                   0
        # 1547           2 LOAD_GLOBAL              1 (NULL + TypeError)
        # 14 LOAD_CONST               1 ('TypeAlias cannot be used with issubclass().')
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 RAISE_VARARGS            1

    def __repr__(self):
        # 1549           0 RESUME                   0
        # 1550           2 LOAD_CONST               1 ('typing_extensions.TypeAlias')
        # 4 RETURN_VALUE


class _Immutable:
    """_Immutable"""
    def __copy__(self):
        # 1565           0 RESUME                   0
        # 1566           2 LOAD_FAST                0 (self)
        # 4 RETURN_VALUE

    def __deepcopy__(self, memo):
        # 1568           0 RESUME                   0
        # 1569           2 LOAD_FAST                0 (self)
        # 4 RETURN_VALUE


class ParamSpecArgs:
    """ParamSpecArgs"""
    def __init__(self, origin):
        # 1583           0 RESUME                   0
        # 1584           2 LOAD_FAST                1 (origin)
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (__origin__)
        # 16 LOAD_CONST               0 (None)
        # 18 RETURN_VALUE

    def __repr__(self):
        # 1586           0 RESUME                   0
        # 1587           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (__origin__)
        # 14 LOAD_ATTR                1 (__name__)
        # 24 FORMAT_VALUE             0
        # 26 LOAD_CONST               1 ('.args')
        # 28 BUILD_STRING             2
        # 30 RETURN_VALUE


class ParamSpecKwargs:
    """ParamSpecKwargs"""
    def __init__(self, origin):
        # 1601           0 RESUME                   0
        # 1602           2 LOAD_FAST                1 (origin)
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (__origin__)
        # 16 LOAD_CONST               0 (None)
        # 18 RETURN_VALUE

    def __repr__(self):
        # 1604           0 RESUME                   0
        # 1605           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (__origin__)
        # 14 LOAD_ATTR                1 (__name__)
        # 24 FORMAT_VALUE             0
        # 26 LOAD_CONST               1 ('.kwargs')
        # 28 BUILD_STRING             2
        # 30 RETURN_VALUE


class ParamSpec:
    """ParamSpec"""
    def args(self):
        # 1664           0 RESUME                   0
        # 1666           2 LOAD_GLOBAL              1 (NULL + ParamSpecArgs)
        # 14 LOAD_FAST                0 (self)
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 RETURN_VALUE

    def kwargs(self):
        # 1668           0 RESUME                   0
        # 1670           2 LOAD_GLOBAL              1 (NULL + ParamSpecKwargs)
        # 14 LOAD_FAST                0 (self)
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 RETURN_VALUE

    def __init__(self, name):
        # 0 COPY_FREE_VARS           1
        # 1672           2 RESUME                   0
        # 1673           4 LOAD_GLOBAL              1 (NULL + super)
        # 16 PRECALL                  0
        # 20 CALL                     0
        # 30 LOAD_METHOD              1 (__init__)
        # 52 LOAD_FAST                0 (self)
        # 54 BUILD_LIST               1
        # 56 PRECALL                  1
        # 60 CALL                     1
        # 70 POP_TOP
        # 1674          72 LOAD_FAST                1 (name)
        # 74 LOAD_FAST                0 (self)
        # 76 STORE_ATTR               2 (__name__)
        # 1675          86 LOAD_GLOBAL              7 (NULL + bool)
        # 98 LOAD_FAST                3 (covariant)
        # 100 PRECALL                  1
        # 104 CALL                     1
        # 114 LOAD_FAST                0 (self)
        # 116 STORE_ATTR               4 (__covariant__)
        # 1676         126 LOAD_GLOBAL              7 (NULL + bool)
        # 138 LOAD_FAST                4 (contravariant)
        # 140 PRECALL                  1
        # 144 CALL                     1
        # 154 LOAD_FAST                0 (self)
        # 156 STORE_ATTR               5 (__contravariant__)
        # 1677         166 LOAD_FAST                2 (bound)
        # 168 POP_JUMP_FORWARD_IF_FALSE    27 (to 224)
        # 1678         170 LOAD_GLOBAL             13 (NULL + typing)
        # 182 LOAD_ATTR                7 (_type_check)
        # 192 LOAD_FAST                2 (bound)
        # 194 LOAD_CONST               1 ('Bound must be a type.')
        # 196 PRECALL                  2
        # 200 CALL                     2
        # 210 LOAD_FAST                0 (self)
        # 212 STORE_ATTR               8 (__bound__)
        # 222 JUMP_FORWARD             7 (to 238)
        # 1680     >>  224 LOAD_CONST               0 (None)
        # 226 LOAD_FAST                0 (self)
        # 228 STORE_ATTR               8 (__bound__)
        # 1683     >>  238 NOP
        # 1684         240 LOAD_GLOBAL             19 (NULL + sys)
        # 252 LOAD_ATTR               10 (_getframe)
        # 262 LOAD_CONST               2 (1)
        # 264 PRECALL                  1
        # 268 CALL                     1
        # 278 LOAD_ATTR               11 (f_globals)
        # 288 LOAD_METHOD             12 (get)
        # 310 LOAD_CONST               3 ('__name__')
        # 312 LOAD_CONST               4 ('__main__')
        # 314 PRECALL                  2
        # 318 CALL                     2
        # 328 STORE_FAST               5 (def_mod)
        # 330 JUMP_FORWARD            25 (to 382)
        # >>  332 PUSH_EXC_INFO
        # 1685         334 LOAD_GLOBAL             26 (AttributeError)
        # 346 LOAD_GLOBAL             28 (ValueError)
        # 358 BUILD_TUPLE              2
        # 360 CHECK_EXC_MATCH
        # 362 POP_JUMP_FORWARD_IF_FALSE     5 (to 374)
        # 364 POP_TOP
        # 1686         366 LOAD_CONST               0 (None)
        # 368 STORE_FAST               5 (def_mod)
        # 370 POP_EXCEPT
        # 372 JUMP_FORWARD             4 (to 382)
        # 1685     >>  374 RERAISE                  0
        # >>  376 COPY                     3
        # 378 POP_EXCEPT
        # 380 RERAISE                  1
        # 1687     >>  382 LOAD_FAST                5 (def_mod)
        # 384 LOAD_CONST               5 ('typing_extensions')
        # 386 COMPARE_OP               3 (!=)
        # 392 POP_JUMP_FORWARD_IF_FALSE     9 (to 412)
        # 1688         394 LOAD_FAST                5 (def_mod)
        # 396 LOAD_FAST                0 (self)
        # 398 STORE_ATTR              15 (__module__)
        # 408 LOAD_CONST               0 (None)
        # 410 RETURN_VALUE
        # 1687     >>  412 LOAD_CONST               0 (None)
        # 414 RETURN_VALUE
        # ExceptionTable:
        # 240 to 328 -> 332 [0]
        # 332 to 368 -> 376 [1] lasti
        # 374 to 374 -> 376 [1] lasti

    def __repr__(self):
        # 1690           0 RESUME                   0
        # 1691           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (__covariant__)
        # 14 POP_JUMP_FORWARD_IF_FALSE     3 (to 22)
        # 1692          16 LOAD_CONST               1 ('+')
        # 18 STORE_FAST               1 (prefix)
        # 20 JUMP_FORWARD            12 (to 46)
        # 1693     >>   22 LOAD_FAST                0 (self)
        # 24 LOAD_ATTR                1 (__contravariant__)
        # 34 POP_JUMP_FORWARD_IF_FALSE     3 (to 42)
        # 1694          36 LOAD_CONST               2 ('-')
        # 38 STORE_FAST               1 (prefix)
        # 40 JUMP_FORWARD             2 (to 46)
        # 1696     >>   42 LOAD_CONST               3 ('~')
        # 44 STORE_FAST               1 (prefix)
        # 1697     >>   46 LOAD_FAST                1 (prefix)
        # 48 LOAD_FAST                0 (self)
        # 50 LOAD_ATTR                2 (__name__)
        # 60 BINARY_OP                0 (+)
        # 64 RETURN_VALUE

    def __hash__(self):
        # 1699           0 RESUME                   0
        # 1700           2 LOAD_GLOBAL              0 (object)
        # 14 LOAD_METHOD              1 (__hash__)
        # 36 LOAD_FAST                0 (self)
        # 38 PRECALL                  1
        # 42 CALL                     1
        # 52 RETURN_VALUE

    def __eq__(self, other):
        # 1702           0 RESUME                   0
        # 1703           2 LOAD_FAST                0 (self)
        # 4 LOAD_FAST                1 (other)
        # 6 IS_OP                    0
        # 8 RETURN_VALUE

    def __reduce__(self):
        # 1705           0 RESUME                   0
        # 1706           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (__name__)
        # 14 RETURN_VALUE

    def __call__(self):
        # 1709           0 RESUME                   0
        # 1710           2 LOAD_CONST               0 (None)
        # 4 RETURN_VALUE

    def _get_type_vars(self, tvars):
        # 1714           0 RESUME                   0
        # 1715           2 LOAD_FAST                0 (self)
        # 4 LOAD_FAST                1 (tvars)
        # 6 CONTAINS_OP              1
        # 8 POP_JUMP_FORWARD_IF_FALSE    23 (to 56)
        # 1716          10 LOAD_FAST                1 (tvars)
        # 12 LOAD_METHOD              0 (append)
        # 34 LOAD_FAST                0 (self)
        # 36 PRECALL                  1
        # 40 CALL                     1
        # 50 POP_TOP
        # 52 LOAD_CONST               0 (None)
        # 54 RETURN_VALUE
        # 1715     >>   56 LOAD_CONST               0 (None)
        # 58 RETURN_VALUE


class _ConcatenateGenericAlias:
    """_ConcatenateGenericAlias"""
    def __init__(self, origin, args):
        # 0 COPY_FREE_VARS           1
        # 1735           2 RESUME                   0
        # 1736           4 LOAD_GLOBAL              1 (NULL + super)
        # 16 PRECALL                  0
        # 20 CALL                     0
        # 30 LOAD_METHOD              1 (__init__)
        # 52 LOAD_FAST                2 (args)
        # 54 PRECALL                  1
        # 58 CALL                     1
        # 68 POP_TOP
        # 1737          70 LOAD_FAST                1 (origin)
        # 72 LOAD_FAST                0 (self)
        # 74 STORE_ATTR               2 (__origin__)
        # 1738          84 LOAD_FAST                2 (args)
        # 86 LOAD_FAST                0 (self)
        # 88 STORE_ATTR               3 (__args__)
        # 98 LOAD_CONST               0 (None)
        # 100 RETURN_VALUE

    def __repr__(self):
        # 0 MAKE_CELL                1 (_type_repr)
        # 1740           2 RESUME                   0
        # 1741           4 LOAD_GLOBAL              0 (typing)
        # 16 LOAD_ATTR                1 (_type_repr)
        # 26 STORE_DEREF              1 (_type_repr)
        # 1742          28 PUSH_NULL
        # 30 LOAD_DEREF               1 (_type_repr)
        # 32 LOAD_FAST                0 (self)
        # 34 LOAD_ATTR                2 (__origin__)
        # 44 PRECALL                  1
        # 48 CALL                     1
        # 58 FORMAT_VALUE             0
        # 60 LOAD_CONST               1 ('[')
        # 1743          62 LOAD_CONST               2 (', ')
        # 64 LOAD_METHOD              3 (join)
        # 86 LOAD_CLOSURE             1 (_type_repr)
        # 88 BUILD_TUPLE              1
        # 90 LOAD_CONST               3 (<code object <genexpr> at 0x000001EBD7EE9D40, file "setuptools\_vendor\typing_extensions.py", line 1743>)
        # 92 MAKE_FUNCTION            8 (closure)
        # 94 LOAD_FAST                0 (self)
        # 96 LOAD_ATTR                4 (__args__)
        # 106 GET_ITER
        # 108 PRECALL                  0
        # 112 CALL                     0
        # 122 PRECALL                  1
        # 126 CALL                     1
        # 1742         136 FORMAT_VALUE             0
        # 138 LOAD_CONST               4 (']')
        # 140 BUILD_STRING             4
        # 142 RETURN_VALUE
        # Disassembly of <code object <genexpr> at 0x000001EBD7EE9D40, file "setuptools\_vendor\typing_extensions.py", line 1743>:
        # 0 COPY_FREE_VARS           1
        # 1743           2 RETURN_GENERATOR
        # 4 POP_TOP
        # 6 RESUME                   0
        # 8 LOAD_FAST                0 (.0)
        # >>   10 FOR_ITER                15 (to 42)
        # 12 STORE_FAST               1 (arg)
        # 14 PUSH_NULL
        # 16 LOAD_DEREF               2 (_type_repr)
        # 18 LOAD_FAST                1 (arg)
        # 20 PRECALL                  1
        # 24 CALL                     1
        # 34 YIELD_VALUE
        # 36 RESUME                   1
        # 38 POP_TOP
        # 40 JUMP_BACKWARD           16 (to 10)
        # >>   42 LOAD_CONST               0 (None)
        # 44 RETURN_VALUE

    def __hash__(self):
        # 1745           0 RESUME                   0
        # 1746           2 LOAD_GLOBAL              1 (NULL + hash)
        # 14 LOAD_FAST                0 (self)
        # 16 LOAD_ATTR                1 (__origin__)
        # 26 LOAD_FAST                0 (self)
        # 28 LOAD_ATTR                2 (__args__)
        # 38 BUILD_TUPLE              2
        # 40 PRECALL                  1
        # 44 CALL                     1
        # 54 RETURN_VALUE

    def __call__(self):
        # 1749           0 RESUME                   0
        # 1750           2 LOAD_CONST               0 (None)
        # 4 RETURN_VALUE

    def __parameters__(self):
        # 1752           0 RESUME                   0
        # 1754           2 LOAD_GLOBAL              1 (NULL + tuple)
        # 14 LOAD_CONST               1 (<code object <genexpr> at 0x000001EBD7E48FF0, file "setuptools\_vendor\typing_extensions.py", line 1754>)
        # 16 MAKE_FUNCTION            0
        # 1755          18 LOAD_FAST                0 (self)
        # 20 LOAD_ATTR                1 (__args__)
        # 1754          30 GET_ITER
        # 32 PRECALL                  0
        # 36 CALL                     0
        # 46 PRECALL                  1
        # 50 CALL                     1
        # 60 RETURN_VALUE
        # Disassembly of <code object <genexpr> at 0x000001EBD7E48FF0, file "setuptools\_vendor\typing_extensions.py", line 1754>:
        # 1754           0 RETURN_GENERATOR
        # 2 POP_TOP
        # 4 RESUME                   0
        # 6 LOAD_FAST                0 (.0)
        # >>    8 FOR_ITER                39 (to 88)
        # 1755          10 STORE_FAST               1 (tp)
        # 12 LOAD_GLOBAL              1 (NULL + isinstance)
        # 24 LOAD_FAST                1 (tp)
        # 26 LOAD_GLOBAL              2 (typing)
        # 38 LOAD_ATTR                2 (TypeVar)
        # 48 LOAD_GLOBAL              6 (ParamSpec)
        # 60 BUILD_TUPLE              2
        # 62 PRECALL                  2
        # 66 CALL                     2
        # 1754          76 POP_JUMP_BACKWARD_IF_FALSE    35 (to 8)
        # 1755          78 LOAD_FAST                1 (tp)
        # 1754          80 YIELD_VALUE
        # 82 RESUME                   1
        # 84 POP_TOP
        # 86 JUMP_BACKWARD           40 (to 8)
        # >>   88 LOAD_CONST               0 (None)
        # 90 RETURN_VALUE

    def _get_type_vars(self, tvars):
        # 1760           0 RESUME                   0
        # 1761           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (__origin__)
        # 14 POP_JUMP_FORWARD_IF_FALSE    35 (to 86)
        # 16 LOAD_FAST                0 (self)
        # 18 LOAD_ATTR                1 (__parameters__)
        # 28 POP_JUMP_FORWARD_IF_FALSE    30 (to 90)
        # 1762          30 LOAD_GLOBAL              5 (NULL + typing)
        # 42 LOAD_ATTR                3 (_get_type_vars)
        # 52 LOAD_FAST                0 (self)
        # 54 LOAD_ATTR                1 (__parameters__)
        # 64 LOAD_FAST                1 (tvars)
        # 66 PRECALL                  2
        # 70 CALL                     2
        # 80 POP_TOP
        # 82 LOAD_CONST               0 (None)
        # 84 RETURN_VALUE
        # 1761     >>   86 LOAD_CONST               0 (None)
        # 88 RETURN_VALUE
        # >>   90 LOAD_CONST               0 (None)
        # 92 RETURN_VALUE


def _concatenate_getitem(self, parameters):
    # 0 MAKE_CELL                2 (msg)
    # 1766           2 RESUME                   0
    # 1768           4 LOAD_FAST                1 (parameters)
    # 6 LOAD_CONST               1 (())
    # 8 COMPARE_OP               2 (==)
    # 14 POP_JUMP_FORWARD_IF_FALSE    15 (to 46)
    # 1769          16 LOAD_GLOBAL              1 (NULL + TypeError)
    # 28 LOAD_CONST               2 ('Cannot take a Concatenate of no types.')
    # 30 PRECALL                  1
    # 34 CALL                     1
    # 44 RAISE_VARARGS            1
    # 1770     >>   46 LOAD_GLOBAL              3 (NULL + isinstance)
    # 58 LOAD_FAST                1 (parameters)
    # 60 LOAD_GLOBAL              4 (tuple)
    # 72 PRECALL                  2
    # 76 CALL                     2
    # 86 POP_JUMP_FORWARD_IF_TRUE     3 (to 94)
    # 1771          88 LOAD_FAST                1 (parameters)
    # 90 BUILD_TUPLE              1
    # 92 STORE_FAST               1 (parameters)
    # 1772     >>   94 LOAD_GLOBAL              3 (NULL + isinstance)
    # 106 LOAD_FAST                1 (parameters)
    # 108 LOAD_CONST               3 (-1)
    # 110 BINARY_SUBSCR
    # 120 LOAD_GLOBAL              6 (ParamSpec)
    # 132 PRECALL                  2
    # 136 CALL                     2
    # 146 POP_JUMP_FORWARD_IF_TRUE    15 (to 178)
    # 1773         148 LOAD_GLOBAL              1 (NULL + TypeError)
    # 160 LOAD_CONST               4 ('The last parameter to Concatenate should be a ParamSpec variable.')
    # 162 PRECALL                  1
    # 166 CALL                     1
    # 176 RAISE_VARARGS            1
    # 1775     >>  178 LOAD_CONST               5 ('Concatenate[arg, ...]: each arg must be a type.')
    # 180 STORE_DEREF              2 (msg)
    # 1776         182 LOAD_GLOBAL              5 (NULL + tuple)
    # 194 LOAD_CLOSURE             2 (msg)
    # 196 BUILD_TUPLE              1
    # 198 LOAD_CONST               6 (<code object <genexpr> at 0x000001EBD7DF3B30, file "setuptools\_vendor\typing_extensions.py", line 1776>)
    # 200 MAKE_FUNCTION            8 (closure)
    # 202 LOAD_FAST                1 (parameters)
    # 204 GET_ITER
    # 206 PRECALL                  0
    # 210 CALL                     0
    # 220 PRECALL                  1
    # 224 CALL                     1
    # 234 STORE_FAST               1 (parameters)
    # 1777         236 LOAD_GLOBAL              9 (NULL + _ConcatenateGenericAlias)
    # 248 LOAD_FAST                0 (self)
    # 250 LOAD_FAST                1 (parameters)
    # 252 PRECALL                  2
    # 256 CALL                     2
    # 266 RETURN_VALUE
    # Disassembly of <code object <genexpr> at 0x000001EBD7DF3B30, file "setuptools\_vendor\typing_extensions.py", line 1776>:
    # 0 COPY_FREE_VARS           1
    # 1776           2 RETURN_GENERATOR
    # 4 POP_TOP
    # 6 RESUME                   0
    # 8 LOAD_FAST                0 (.0)
    # >>   10 FOR_ITER                25 (to 62)
    # 12 STORE_FAST               1 (p)
    # 14 LOAD_GLOBAL              1 (NULL + typing)
    # 26 LOAD_ATTR                1 (_type_check)
    # 36 LOAD_FAST                1 (p)
    # 38 LOAD_DEREF               2 (msg)
    # 40 PRECALL                  2
    # 44 CALL                     2
    # 54 YIELD_VALUE
    # 56 RESUME                   1
    # 58 POP_TOP
    # 60 JUMP_BACKWARD           26 (to 10)
    # >>   62 LOAD_CONST               0 (None)
    # 64 RETURN_VALUE

def Concatenate(self, parameters):
    """Used in conjunction with ``ParamSpec`` and ``Callable`` to represent a
        higher order function which adds, removes or transforms parameters of a
        callable.

        For example::

           Callable[Concatenate[int, P], int]

        See PEP 612 for detailed information.
        """
    # 1786           0 RESUME                   0
    # 1798           2 LOAD_GLOBAL              1 (NULL + _concatenate_getitem)
    # 14 LOAD_FAST                0 (self)
    # 16 LOAD_FAST                1 (parameters)
    # 18 PRECALL                  2
    # 22 CALL                     2
    # 32 RETURN_VALUE

class _ConcatenateForm:
    """_ConcatenateForm"""
    def __repr__(self):
        # 1802           0 RESUME                   0
        # 1803           2 LOAD_CONST               1 ('typing_extensions.')
        # 4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (_name)
        # 16 BINARY_OP                0 (+)
        # 20 RETURN_VALUE

    def __getitem__(self, parameters):
        # 1805           0 RESUME                   0
        # 1806           2 LOAD_GLOBAL              1 (NULL + _concatenate_getitem)
        # 14 LOAD_FAST                0 (self)
        # 16 LOAD_FAST                1 (parameters)
        # 18 PRECALL                  2
        # 22 CALL                     2
        # 32 RETURN_VALUE


class _ConcatenateAliasMeta:
    """_ConcatenateAliasMeta"""
    def __repr__(self):
        # 1825           0 RESUME                   0
        # 1826           2 LOAD_CONST               1 ('typing_extensions.Concatenate')
        # 4 RETURN_VALUE


class _ConcatenateAliasBase:
    """_ConcatenateAliasBase"""
    def __instancecheck__(self, obj):
        # 1843           0 RESUME                   0
        # 1844           2 LOAD_GLOBAL              1 (NULL + TypeError)
        # 14 LOAD_CONST               1 ('Concatenate cannot be used with isinstance().')
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 RAISE_VARARGS            1

    def __subclasscheck__(self, cls):
        # 1846           0 RESUME                   0
        # 1847           2 LOAD_GLOBAL              1 (NULL + TypeError)
        # 14 LOAD_CONST               1 ('Concatenate cannot be used with issubclass().')
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 RAISE_VARARGS            1

    def __repr__(self):
        # 1849           0 RESUME                   0
        # 1850           2 LOAD_CONST               1 ('typing_extensions.Concatenate')
        # 4 RETURN_VALUE

    def __getitem__(self, parameters):
        # 1852           0 RESUME                   0
        # 1853           2 LOAD_GLOBAL              1 (NULL + _concatenate_getitem)
        # 14 LOAD_FAST                0 (self)
        # 16 LOAD_FAST                1 (parameters)
        # 18 PRECALL                  2
        # 22 CALL                     2
        # 32 RETURN_VALUE


class _TypeGuardForm:
    """_TypeGuardForm"""
    def __repr__(self):
        # 1863           0 RESUME                   0
        # 1864           2 LOAD_CONST               1 ('typing_extensions.')
        # 4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (_name)
        # 16 BINARY_OP                0 (+)
        # 20 RETURN_VALUE


def TypeGuard(self, parameters):
    """Special typing form used to annotate the return type of a user-defined
        type guard function.  ``TypeGuard`` only accepts a single type argument.
        At runtime, functions marked this way should return a boolean.

        ``TypeGuard`` aims to benefit *type narrowing* -- a technique used by static
        type checkers to determine a more precise type of an expression within a
        program's code flow.  Usually type narrowing is done by analyzing
        conditional code flow and applying the narrowing to a block of code.  The
        conditional expression here is sometimes referred to as a "type guard".

        Sometimes it would be convenient to use a user-defined boolean function
        as a type guard.  Such a function should use ``TypeGuard[...]`` as its
        return type to alert static type checkers to this intention.

        Using  ``-> TypeGuard`` tells the static type checker that for a given
        function:

        1. The return value is a boolean.
        2. If the return value is ``True``, the type of its argument
        is the type inside ``TypeGuard``.

        For example::

            def is_str(val: Union[str, float]):
                # "isinstance" type guard
                if isinstance(val, str):
                    # Type of ``val`` is narrowed to ``str``
                    ...
                else:
                    # Else, type of ``val`` is narrowed to ``float``.
                    ...

        Strict type narrowing is not enforced -- ``TypeB`` need not be a narrower
        form of ``TypeA`` (it can even be a wider form) and this may lead to
        type-unsafe results.  The main reason is to allow for things like
        narrowing ``List[object]`` to ``List[str]`` even though the latter is not
        a subtype of the former, since ``List`` is invariant.  The responsibility of
        writing type-safe type guards is left to the user.

        ``TypeGuard`` also works with type variables.  For more information, see
        PEP 647 (User-Defined Type Guards).
        """
    # 1866           0 RESUME                   0
    # 1910           2 LOAD_GLOBAL              1 (NULL + typing)
    # 14 LOAD_ATTR                1 (_type_check)
    # 24 LOAD_FAST                1 (parameters)
    # 26 LOAD_FAST                0 (self)
    # 28 FORMAT_VALUE             0
    # 30 LOAD_CONST               1 (' accepts only single type.')
    # 32 BUILD_STRING             2
    # 34 PRECALL                  2
    # 38 CALL                     2
    # 48 STORE_FAST               2 (item)
    # 1911          50 LOAD_GLOBAL              1 (NULL + typing)
    # 62 LOAD_ATTR                2 (_GenericAlias)
    # 72 LOAD_FAST                0 (self)
    # 74 LOAD_FAST                2 (item)
    # 76 BUILD_TUPLE              1
    # 78 PRECALL                  2
    # 82 CALL                     2
    # 92 RETURN_VALUE

class _TypeGuard:
    """_TypeGuard"""
    def __init__(self, tp):
        # 2016           0 RESUME                   0
        # 2017           2 LOAD_FAST                1 (tp)
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (__type__)
        # 16 LOAD_CONST               0 (None)
        # 18 RETURN_VALUE

    def __getitem__(self, item):
        # 2019           0 RESUME                   0
        # 2020           2 LOAD_GLOBAL              1 (NULL + type)
        # 14 LOAD_FAST                0 (self)
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 STORE_FAST               2 (cls)
        # 2021          32 LOAD_FAST                0 (self)
        # 34 LOAD_ATTR                1 (__type__)
        # 44 POP_JUMP_FORWARD_IF_NOT_NONE    48 (to 142)
        # 2022          46 PUSH_NULL
        # 48 LOAD_FAST                2 (cls)
        # 50 LOAD_GLOBAL              5 (NULL + typing)
        # 62 LOAD_ATTR                3 (_type_check)
        # 72 LOAD_FAST                1 (item)
        # 2023          74 LOAD_FAST                2 (cls)
        # 76 LOAD_ATTR                4 (__name__)
        # 86 LOAD_CONST               1 (1)
        # 88 LOAD_CONST               0 (None)
        # 90 BUILD_SLICE              2
        # 92 BINARY_SUBSCR
        # 102 FORMAT_VALUE             0
        # 104 LOAD_CONST               2 (' accepts only a single type.')
        # 106 BUILD_STRING             2
        # 2022         108 PRECALL                  2
        # 112 CALL                     2
        # 2024         122 LOAD_CONST               3 (True)
        # 2022         124 KW_NAMES                 4
        # 126 PRECALL                  2
        # 130 CALL                     2
        # 140 RETURN_VALUE
        # 2025     >>  142 LOAD_GLOBAL             11 (NULL + TypeError)
        # 154 LOAD_FAST                2 (cls)
        # 156 LOAD_ATTR                4 (__name__)
        # 166 LOAD_CONST               1 (1)
        # 168 LOAD_CONST               0 (None)
        # 170 BUILD_SLICE              2
        # 172 BINARY_SUBSCR
        # 182 FORMAT_VALUE             0
        # 184 LOAD_CONST               5 (' cannot be further subscripted')
        # 186 BUILD_STRING             2
        # 188 PRECALL                  1
        # 192 CALL                     1
        # 202 RAISE_VARARGS            1

    def _eval_type(self, globalns, localns):
        # 2027           0 RESUME                   0
        # 2028           2 LOAD_GLOBAL              1 (NULL + typing)
        # 14 LOAD_ATTR                1 (_eval_type)
        # 24 LOAD_FAST                0 (self)
        # 26 LOAD_ATTR                2 (__type__)
        # 36 LOAD_FAST                1 (globalns)
        # 38 LOAD_FAST                2 (localns)
        # 40 PRECALL                  3
        # 44 CALL                     3
        # 54 STORE_FAST               3 (new_tp)
        # 2029          56 LOAD_FAST                3 (new_tp)
        # 58 LOAD_FAST                0 (self)
        # 60 LOAD_ATTR                2 (__type__)
        # 70 COMPARE_OP               2 (==)
        # 76 POP_JUMP_FORWARD_IF_FALSE     2 (to 82)
        # 2030          78 LOAD_FAST                0 (self)
        # 80 RETURN_VALUE
        # 2031     >>   82 PUSH_NULL
        # 84 LOAD_GLOBAL              7 (NULL + type)
        # 96 LOAD_FAST                0 (self)
        # 98 PRECALL                  1
        # 102 CALL                     1
        # 112 LOAD_FAST                3 (new_tp)
        # 114 LOAD_CONST               1 (True)
        # 116 KW_NAMES                 2
        # 118 PRECALL                  2
        # 122 CALL                     2
        # 132 RETURN_VALUE

    def __repr__(self):
        # 0 COPY_FREE_VARS           1
        # 2033           2 RESUME                   0
        # 2034           4 LOAD_GLOBAL              1 (NULL + super)
        # 16 PRECALL                  0
        # 20 CALL                     0
        # 30 LOAD_METHOD              1 (__repr__)
        # 52 PRECALL                  0
        # 56 CALL                     0
        # 66 STORE_FAST               1 (r)
        # 2035          68 LOAD_FAST                0 (self)
        # 70 LOAD_ATTR                2 (__type__)
        # 80 POP_JUMP_FORWARD_IF_NONE    32 (to 146)
        # 2036          82 LOAD_FAST                1 (r)
        # 84 LOAD_CONST               1 ('[')
        # 86 LOAD_GLOBAL              7 (NULL + typing)
        # 98 LOAD_ATTR                4 (_type_repr)
        # 108 LOAD_FAST                0 (self)
        # 110 LOAD_ATTR                2 (__type__)
        # 120 PRECALL                  1
        # 124 CALL                     1
        # 134 FORMAT_VALUE             0
        # 136 LOAD_CONST               2 (']')
        # 138 BUILD_STRING             3
        # 140 BINARY_OP               13 (+=)
        # 144 STORE_FAST               1 (r)
        # 2037     >>  146 LOAD_FAST                1 (r)
        # 148 RETURN_VALUE

    def __hash__(self):
        # 2039           0 RESUME                   0
        # 2040           2 LOAD_GLOBAL              1 (NULL + hash)
        # 14 LOAD_GLOBAL              3 (NULL + type)
        # 26 LOAD_FAST                0 (self)
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 LOAD_ATTR                2 (__name__)
        # 52 LOAD_FAST                0 (self)
        # 54 LOAD_ATTR                3 (__type__)
        # 64 BUILD_TUPLE              2
        # 66 PRECALL                  1
        # 70 CALL                     1
        # 80 RETURN_VALUE

    def __eq__(self, other):
        # 2042           0 RESUME                   0
        # 2043           2 LOAD_GLOBAL              1 (NULL + isinstance)
        # 14 LOAD_FAST                1 (other)
        # 16 LOAD_GLOBAL              2 (_TypeGuard)
        # 28 PRECALL                  2
        # 32 CALL                     2
        # 42 POP_JUMP_FORWARD_IF_TRUE     7 (to 58)
        # 2044          44 LOAD_GLOBAL              4 (NotImplemented)
        # 56 RETURN_VALUE
        # 2045     >>   58 LOAD_FAST                0 (self)
        # 60 LOAD_ATTR                3 (__type__)
        # 70 POP_JUMP_FORWARD_IF_NONE    16 (to 104)
        # 2046          72 LOAD_FAST                0 (self)
        # 74 LOAD_ATTR                3 (__type__)
        # 84 LOAD_FAST                1 (other)
        # 86 LOAD_ATTR                3 (__type__)
        # 96 COMPARE_OP               2 (==)
        # 102 RETURN_VALUE
        # 2047     >>  104 LOAD_FAST                0 (self)
        # 106 LOAD_FAST                1 (other)
        # 108 IS_OP                    0
        # 110 RETURN_VALUE


class _SpecialForm:
    """_SpecialForm"""
    def __init__(self, getitem):
        # 2058           0 RESUME                   0
        # 2059           2 LOAD_FAST                1 (getitem)
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (_getitem)
        # 2060          16 LOAD_FAST                1 (getitem)
        # 18 LOAD_ATTR                1 (__name__)
        # 28 LOAD_FAST                0 (self)
        # 30 STORE_ATTR               2 (_name)
        # 2061          40 LOAD_FAST                1 (getitem)
        # 42 LOAD_ATTR                3 (__doc__)
        # 52 LOAD_FAST                0 (self)
        # 54 STORE_ATTR               3 (__doc__)
        # 64 LOAD_CONST               0 (None)
        # 66 RETURN_VALUE

    def __getattr__(self, item):
        # 2063           0 RESUME                   0
        # 2064           2 LOAD_FAST                1 (item)
        # 4 LOAD_CONST               1 (frozenset({'__qualname__', '__name__'}))
        # 6 CONTAINS_OP              0
        # 8 POP_JUMP_FORWARD_IF_FALSE     7 (to 24)
        # 2065          10 LOAD_FAST                0 (self)
        # 12 LOAD_ATTR                0 (_name)
        # 22 RETURN_VALUE
        # 2067     >>   24 LOAD_GLOBAL              3 (NULL + AttributeError)
        # 36 LOAD_FAST                1 (item)
        # 38 PRECALL                  1
        # 42 CALL                     1
        # 52 RAISE_VARARGS            1

    def __mro_entries__(self, bases):
        # 2069           0 RESUME                   0
        # 2070           2 LOAD_GLOBAL              1 (NULL + TypeError)
        # 14 LOAD_CONST               1 ('Cannot subclass ')
        # 16 LOAD_FAST                0 (self)
        # 18 FORMAT_VALUE             2 (repr)
        # 20 BUILD_STRING             2
        # 22 PRECALL                  1
        # 26 CALL                     1
        # 36 RAISE_VARARGS            1

    def __repr__(self):
        # 2072           0 RESUME                   0
        # 2073           2 LOAD_CONST               1 ('typing_extensions.')
        # 4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (_name)
        # 16 FORMAT_VALUE             0
        # 18 BUILD_STRING             2
        # 20 RETURN_VALUE

    def __reduce__(self):
        # 2075           0 RESUME                   0
        # 2076           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_name)
        # 14 RETURN_VALUE

    def __call__(self):
        # 2078           0 RESUME                   0
        # 2079           2 LOAD_GLOBAL              1 (NULL + TypeError)
        # 14 LOAD_CONST               1 ('Cannot instantiate ')
        # 16 LOAD_FAST                0 (self)
        # 18 FORMAT_VALUE             2 (repr)
        # 20 BUILD_STRING             2
        # 22 PRECALL                  1
        # 26 CALL                     1
        # 36 RAISE_VARARGS            1

    def __or__(self, other):
        # 2081           0 RESUME                   0
        # 2082           2 LOAD_GLOBAL              0 (typing)
        # 14 LOAD_ATTR                1 (Union)
        # 24 LOAD_FAST                0 (self)
        # 26 LOAD_FAST                1 (other)
        # 28 BUILD_TUPLE              2
        # 30 BINARY_SUBSCR
        # 40 RETURN_VALUE

    def __ror__(self, other):
        # 2084           0 RESUME                   0
        # 2085           2 LOAD_GLOBAL              0 (typing)
        # 14 LOAD_ATTR                1 (Union)
        # 24 LOAD_FAST                1 (other)
        # 26 LOAD_FAST                0 (self)
        # 28 BUILD_TUPLE              2
        # 30 BINARY_SUBSCR
        # 40 RETURN_VALUE

    def __instancecheck__(self, obj):
        # 2087           0 RESUME                   0
        # 2088           2 LOAD_GLOBAL              1 (NULL + TypeError)
        # 14 LOAD_FAST                0 (self)
        # 16 FORMAT_VALUE             0
        # 18 LOAD_CONST               1 (' cannot be used with isinstance()')
        # 20 BUILD_STRING             2
        # 22 PRECALL                  1
        # 26 CALL                     1
        # 36 RAISE_VARARGS            1

    def __subclasscheck__(self, cls):
        # 2090           0 RESUME                   0
        # 2091           2 LOAD_GLOBAL              1 (NULL + TypeError)
        # 14 LOAD_FAST                0 (self)
        # 16 FORMAT_VALUE             0
        # 18 LOAD_CONST               1 (' cannot be used with issubclass()')
        # 20 BUILD_STRING             2
        # 22 PRECALL                  1
        # 26 CALL                     1
        # 36 RAISE_VARARGS            1

    def __getitem__(self, parameters):
        # 2093           0 RESUME                   0
        # 2095           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (_getitem)
        # 26 LOAD_FAST                0 (self)
        # 28 LOAD_FAST                1 (parameters)
        # 30 PRECALL                  2
        # 34 CALL                     2
        # 44 RETURN_VALUE


def Self(self, params):
    """Used to spell the type of "self" in classes.

        Example::

          from typing import Self

          class ReturnsSelf:
              def parse(self, data: bytes) -> Self:
                  ...
                  return self

        """
    # 2097           0 RESUME                   0
    # 2112           2 LOAD_GLOBAL              1 (NULL + TypeError)
    # 14 LOAD_FAST                0 (self)
    # 16 FORMAT_VALUE             0
    # 18 LOAD_CONST               1 (' is not subscriptable')
    # 20 BUILD_STRING             2
    # 22 PRECALL                  1
    # 26 CALL                     1
    # 36 RAISE_VARARGS            1

class _Self:
    """_Self"""
    def __instancecheck__(self, obj):
        # 2130           0 RESUME                   0
        # 2131           2 LOAD_GLOBAL              1 (NULL + TypeError)
        # 14 LOAD_FAST                0 (self)
        # 16 FORMAT_VALUE             0
        # 18 LOAD_CONST               1 (' cannot be used with isinstance().')
        # 20 BUILD_STRING             2
        # 22 PRECALL                  1
        # 26 CALL                     1
        # 36 RAISE_VARARGS            1

    def __subclasscheck__(self, cls):
        # 2133           0 RESUME                   0
        # 2134           2 LOAD_GLOBAL              1 (NULL + TypeError)
        # 14 LOAD_FAST                0 (self)
        # 16 FORMAT_VALUE             0
        # 18 LOAD_CONST               1 (' cannot be used with issubclass().')
        # 20 BUILD_STRING             2
        # 22 PRECALL                  1
        # 26 CALL                     1
        # 36 RAISE_VARARGS            1


class _ExtensionsSpecialForm:
    """_ExtensionsSpecialForm"""
    def __repr__(self):
        # 2144           0 RESUME                   0
        # 2145           2 LOAD_CONST               1 ('typing_extensions.')
        # 4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (_name)
        # 16 BINARY_OP                0 (+)
        # 20 RETURN_VALUE


def Required(self, parameters):
    """A special typing construct to mark a key of a total=False TypedDict
        as required. For example:

            class Movie(TypedDict, total=False):
                title: Required[str]
                year: int

            m = Movie(
                title='The Matrix',  # typechecker error if key is omitted
                year=1999,
            )

        There is no runtime checking that a required key is actually provided
        when instantiating a related TypedDict.
        """
    # 2147           0 RESUME                   0
    # 2164           2 LOAD_GLOBAL              1 (NULL + typing)
    # 14 LOAD_ATTR                1 (_type_check)
    # 24 LOAD_FAST                1 (parameters)
    # 26 LOAD_FAST                0 (self)
    # 28 LOAD_ATTR                2 (_name)
    # 38 FORMAT_VALUE             0
    # 40 LOAD_CONST               1 (' accepts only single type')
    # 42 BUILD_STRING             2
    # 44 PRECALL                  2
    # 48 CALL                     2
    # 58 STORE_FAST               2 (item)
    # 2165          60 LOAD_GLOBAL              1 (NULL + typing)
    # 72 LOAD_ATTR                3 (_GenericAlias)
    # 82 LOAD_FAST                0 (self)
    # 84 LOAD_FAST                2 (item)
    # 86 BUILD_TUPLE              1
    # 88 PRECALL                  2
    # 92 CALL                     2
    # 102 RETURN_VALUE

def NotRequired(self, parameters):
    """A special typing construct to mark a key of a TypedDict as
        potentially missing. For example:

            class Movie(TypedDict):
                title: str
                year: NotRequired[int]

            m = Movie(
                title='The Matrix',  # typechecker error if key is omitted
                year=1999,
            )
        """
    # 2167           0 RESUME                   0
    # 2181           2 LOAD_GLOBAL              1 (NULL + typing)
    # 14 LOAD_ATTR                1 (_type_check)
    # 24 LOAD_FAST                1 (parameters)
    # 26 LOAD_FAST                0 (self)
    # 28 LOAD_ATTR                2 (_name)
    # 38 FORMAT_VALUE             0
    # 40 LOAD_CONST               1 (' accepts only single type')
    # 42 BUILD_STRING             2
    # 44 PRECALL                  2
    # 48 CALL                     2
    # 58 STORE_FAST               2 (item)
    # 2182          60 LOAD_GLOBAL              1 (NULL + typing)
    # 72 LOAD_ATTR                3 (_GenericAlias)
    # 82 LOAD_FAST                0 (self)
    # 84 LOAD_FAST                2 (item)
    # 86 BUILD_TUPLE              1
    # 88 PRECALL                  2
    # 92 CALL                     2
    # 102 RETURN_VALUE

class _RequiredForm:
    """_RequiredForm"""
    def __repr__(self):
        # 2186           0 RESUME                   0
        # 2187           2 LOAD_CONST               1 ('typing_extensions.')
        # 4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (_name)
        # 16 BINARY_OP                0 (+)
        # 20 RETURN_VALUE

    def __getitem__(self, parameters):
        # 2189           0 RESUME                   0
        # 2190           2 LOAD_GLOBAL              1 (NULL + typing)
        # 14 LOAD_ATTR                1 (_type_check)
        # 24 LOAD_FAST                1 (parameters)
        # 2191          26 LOAD_CONST               1 ('{} accepts only single type')
        # 28 LOAD_METHOD              2 (format)
        # 50 LOAD_FAST                0 (self)
        # 52 LOAD_ATTR                3 (_name)
        # 62 PRECALL                  1
        # 66 CALL                     1
        # 2190          76 PRECALL                  2
        # 80 CALL                     2
        # 90 STORE_FAST               2 (item)
        # 2192          92 LOAD_GLOBAL              1 (NULL + typing)
        # 104 LOAD_ATTR                4 (_GenericAlias)
        # 114 LOAD_FAST                0 (self)
        # 116 LOAD_FAST                2 (item)
        # 118 BUILD_TUPLE              1
        # 120 PRECALL                  2
        # 124 CALL                     2
        # 134 RETURN_VALUE


class _MaybeRequired:
    """_MaybeRequired"""
    def __init__(self, tp):
        # 2230           0 RESUME                   0
        # 2231           2 LOAD_FAST                1 (tp)
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (__type__)
        # 16 LOAD_CONST               0 (None)
        # 18 RETURN_VALUE

    def __getitem__(self, item):
        # 2233           0 RESUME                   0
        # 2234           2 LOAD_GLOBAL              1 (NULL + type)
        # 14 LOAD_FAST                0 (self)
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 STORE_FAST               2 (cls)
        # 2235          32 LOAD_FAST                0 (self)
        # 34 LOAD_ATTR                1 (__type__)
        # 44 POP_JUMP_FORWARD_IF_NOT_NONE    64 (to 174)
        # 2236          46 PUSH_NULL
        # 48 LOAD_FAST                2 (cls)
        # 50 LOAD_GLOBAL              5 (NULL + typing)
        # 62 LOAD_ATTR                3 (_type_check)
        # 72 LOAD_FAST                1 (item)
        # 2237          74 LOAD_CONST               1 ('{} accepts only single type.')
        # 76 LOAD_METHOD              4 (format)
        # 98 LOAD_FAST                2 (cls)
        # 100 LOAD_ATTR                5 (__name__)
        # 110 LOAD_CONST               2 (1)
        # 112 LOAD_CONST               0 (None)
        # 114 BUILD_SLICE              2
        # 116 BINARY_SUBSCR
        # 126 PRECALL                  1
        # 130 CALL                     1
        # 2236         140 PRECALL                  2
        # 144 CALL                     2
        # 2238         154 LOAD_CONST               3 (True)
        # 2236         156 KW_NAMES                 4
        # 158 PRECALL                  2
        # 162 CALL                     2
        # 172 RETURN_VALUE
        # 2239     >>  174 LOAD_GLOBAL             13 (NULL + TypeError)
        # 186 LOAD_CONST               5 ('{} cannot be further subscripted')
        # 2240         188 LOAD_METHOD              4 (format)
        # 210 LOAD_FAST                2 (cls)
        # 212 LOAD_ATTR                5 (__name__)
        # 222 LOAD_CONST               2 (1)
        # 224 LOAD_CONST               0 (None)
        # 226 BUILD_SLICE              2
        # 228 BINARY_SUBSCR
        # 238 PRECALL                  1
        # 242 CALL                     1
        # 2239         252 PRECALL                  1
        # 256 CALL                     1
        # 266 RAISE_VARARGS            1

    def _eval_type(self, globalns, localns):
        # 2242           0 RESUME                   0
        # 2243           2 LOAD_GLOBAL              1 (NULL + typing)
        # 14 LOAD_ATTR                1 (_eval_type)
        # 24 LOAD_FAST                0 (self)
        # 26 LOAD_ATTR                2 (__type__)
        # 36 LOAD_FAST                1 (globalns)
        # 38 LOAD_FAST                2 (localns)
        # 40 PRECALL                  3
        # 44 CALL                     3
        # 54 STORE_FAST               3 (new_tp)
        # 2244          56 LOAD_FAST                3 (new_tp)
        # 58 LOAD_FAST                0 (self)
        # 60 LOAD_ATTR                2 (__type__)
        # 70 COMPARE_OP               2 (==)
        # 76 POP_JUMP_FORWARD_IF_FALSE     2 (to 82)
        # 2245          78 LOAD_FAST                0 (self)
        # 80 RETURN_VALUE
        # 2246     >>   82 PUSH_NULL
        # 84 LOAD_GLOBAL              7 (NULL + type)
        # 96 LOAD_FAST                0 (self)
        # 98 PRECALL                  1
        # 102 CALL                     1
        # 112 LOAD_FAST                3 (new_tp)
        # 114 LOAD_CONST               1 (True)
        # 116 KW_NAMES                 2
        # 118 PRECALL                  2
        # 122 CALL                     2
        # 132 RETURN_VALUE

    def __repr__(self):
        # 0 COPY_FREE_VARS           1
        # 2248           2 RESUME                   0
        # 2249           4 LOAD_GLOBAL              1 (NULL + super)
        # 16 PRECALL                  0
        # 20 CALL                     0
        # 30 LOAD_METHOD              1 (__repr__)
        # 52 PRECALL                  0
        # 56 CALL                     0
        # 66 STORE_FAST               1 (r)
        # 2250          68 LOAD_FAST                0 (self)
        # 70 LOAD_ATTR                2 (__type__)
        # 80 POP_JUMP_FORWARD_IF_NONE    47 (to 176)
        # 2251          82 LOAD_FAST                1 (r)
        # 84 LOAD_CONST               1 ('[{}]')
        # 86 LOAD_METHOD              3 (format)
        # 108 LOAD_GLOBAL              9 (NULL + typing)
        # 120 LOAD_ATTR                5 (_type_repr)
        # 130 LOAD_FAST                0 (self)
        # 132 LOAD_ATTR                2 (__type__)
        # 142 PRECALL                  1
        # 146 CALL                     1
        # 156 PRECALL                  1
        # 160 CALL                     1
        # 170 BINARY_OP               13 (+=)
        # 174 STORE_FAST               1 (r)
        # 2252     >>  176 LOAD_FAST                1 (r)
        # 178 RETURN_VALUE

    def __hash__(self):
        # 2254           0 RESUME                   0
        # 2255           2 LOAD_GLOBAL              1 (NULL + hash)
        # 14 LOAD_GLOBAL              3 (NULL + type)
        # 26 LOAD_FAST                0 (self)
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 LOAD_ATTR                2 (__name__)
        # 52 LOAD_FAST                0 (self)
        # 54 LOAD_ATTR                3 (__type__)
        # 64 BUILD_TUPLE              2
        # 66 PRECALL                  1
        # 70 CALL                     1
        # 80 RETURN_VALUE

    def __eq__(self, other):
        # 2257           0 RESUME                   0
        # 2258           2 LOAD_GLOBAL              1 (NULL + isinstance)
        # 14 LOAD_FAST                1 (other)
        # 16 LOAD_GLOBAL              3 (NULL + type)
        # 28 LOAD_FAST                0 (self)
        # 30 PRECALL                  1
        # 34 CALL                     1
        # 44 PRECALL                  2
        # 48 CALL                     2
        # 58 POP_JUMP_FORWARD_IF_TRUE     7 (to 74)
        # 2259          60 LOAD_GLOBAL              4 (NotImplemented)
        # 72 RETURN_VALUE
        # 2260     >>   74 LOAD_FAST                0 (self)
        # 76 LOAD_ATTR                3 (__type__)
        # 86 POP_JUMP_FORWARD_IF_NONE    16 (to 120)
        # 2261          88 LOAD_FAST                0 (self)
        # 90 LOAD_ATTR                3 (__type__)
        # 100 LOAD_FAST                1 (other)
        # 102 LOAD_ATTR                3 (__type__)
        # 112 COMPARE_OP               2 (==)
        # 118 RETURN_VALUE
        # 2262     >>  120 LOAD_FAST                0 (self)
        # 122 LOAD_FAST                1 (other)
        # 124 IS_OP                    0
        # 126 RETURN_VALUE


class _Required:
    """_Required"""

class _NotRequired:
    """_NotRequired"""
