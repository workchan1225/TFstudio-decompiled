# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: json\encoder.py

"""Implementation of JSONEncoder
"""

import re
from _json import encode_basestring_ascii
from _json import encode_basestring
from _json import make_encoder

def py_encode_basestring(s):
    """Return a JSON representation of a Python string

    """
    # 37           0 RESUME                   0
    # 41           2 LOAD_CONST               1 (<code object replace at 0x000001EBD7DDF830, file "json\encoder.py", line 41>)
    # 4 MAKE_FUNCTION            0
    # 6 STORE_FAST               1 (replace)
    # 43           8 LOAD_CONST               2 ('"')
    # 10 LOAD_GLOBAL              0 (ESCAPE)
    # 22 LOAD_METHOD              1 (sub)
    # 44 LOAD_FAST                1 (replace)
    # 46 LOAD_FAST                0 (s)
    # 48 PRECALL                  2
    # 52 CALL                     2
    # 62 BINARY_OP                0 (+)
    # 66 LOAD_CONST               2 ('"')
    # 68 BINARY_OP                0 (+)
    # 72 RETURN_VALUE
    # Disassembly of <code object replace at 0x000001EBD7DDF830, file "json\encoder.py", line 41>:
    # 41           0 RESUME                   0
    # 42           2 LOAD_GLOBAL              0 (ESCAPE_DCT)
    # 14 LOAD_FAST                0 (match)
    # 16 LOAD_METHOD              1 (group)
    # 38 LOAD_CONST               1 (0)
    # 40 PRECALL                  1
    # 44 CALL                     1
    # 54 BINARY_SUBSCR
    # 64 RETURN_VALUE

def py_encode_basestring_ascii(s):
    """Return an ASCII-only JSON representation of a Python string

    """
    # 49           0 RESUME                   0
    # 53           2 LOAD_CONST               1 (<code object replace at 0x000001EBD70D21F0, file "json\encoder.py", line 53>)
    # 4 MAKE_FUNCTION            0
    # 6 STORE_FAST               1 (replace)
    # 68           8 LOAD_CONST               2 ('"')
    # 10 LOAD_GLOBAL              0 (ESCAPE_ASCII)
    # 22 LOAD_METHOD              1 (sub)
    # 44 LOAD_FAST                1 (replace)
    # 46 LOAD_FAST                0 (s)
    # 48 PRECALL                  2
    # 52 CALL                     2
    # 62 BINARY_OP                0 (+)
    # 66 LOAD_CONST               2 ('"')
    # 68 BINARY_OP                0 (+)
    # 72 RETURN_VALUE
    # Disassembly of <code object replace at 0x000001EBD70D21F0, file "json\encoder.py", line 53>:
    # 53           0 RESUME                   0
    # 54           2 LOAD_FAST                0 (match)
    # 4 LOAD_METHOD              0 (group)
    # 26 LOAD_CONST               1 (0)
    # 28 PRECALL                  1
    # 32 CALL                     1
    # 42 STORE_FAST               1 (s)
    # 55          44 NOP
    # 56          46 LOAD_GLOBAL              2 (ESCAPE_DCT)
    # 58 LOAD_FAST                1 (s)
    # 60 BINARY_SUBSCR
    # 70 RETURN_VALUE
    # >>   72 PUSH_EXC_INFO
    # 57          74 LOAD_GLOBAL              4 (KeyError)
    # 86 CHECK_EXC_MATCH
    # 88 POP_JUMP_FORWARD_IF_FALSE    93 (to 276)
    # 90 POP_TOP
    # 58          92 LOAD_GLOBAL              7 (NULL + ord)
    # 104 LOAD_FAST                1 (s)
    # 106 PRECALL                  1
    # 110 CALL                     1
    # 120 STORE_FAST               2 (n)
    # 59         122 LOAD_FAST                2 (n)
    # 124 LOAD_CONST               2 (65536)
    # 126 COMPARE_OP               0 (<)
    # 132 POP_JUMP_FORWARD_IF_FALSE    23 (to 180)
    # 60         134 LOAD_CONST               3 ('\\u{0:04x}')
    # 136 LOAD_METHOD              4 (format)
    # 158 LOAD_FAST                2 (n)
    # 160 PRECALL                  1
    # 164 CALL                     1
    # 174 SWAP                     2
    # 176 POP_EXCEPT
    # 178 RETURN_VALUE
    # 64     >>  180 LOAD_FAST                2 (n)
    # 182 LOAD_CONST               2 (65536)
    # 184 BINARY_OP               23 (-=)
    # 188 STORE_FAST               2 (n)
    # 65         190 LOAD_CONST               4 (55296)
    # 192 LOAD_FAST                2 (n)
    # 194 LOAD_CONST               5 (10)
    # 196 BINARY_OP                9 (>>)
    # 200 LOAD_CONST               6 (1023)
    # 202 BINARY_OP                1 (&)
    # 206 BINARY_OP                7 (|)
    # 210 STORE_FAST               3 (s1)
    # 66         212 LOAD_CONST               7 (56320)
    # 214 LOAD_FAST                2 (n)
    # 216 LOAD_CONST               6 (1023)
    # 218 BINARY_OP                1 (&)
    # 222 BINARY_OP                7 (|)
    # 226 STORE_FAST               4 (s2)
    # 67         228 LOAD_CONST               8 ('\\u{0:04x}\\u{1:04x}')
    # 230 LOAD_METHOD              4 (format)
    # 252 LOAD_FAST                3 (s1)
    # 254 LOAD_FAST                4 (s2)
    # 256 PRECALL                  2
    # 260 CALL                     2
    # 270 SWAP                     2
    # 272 POP_EXCEPT
    # 274 RETURN_VALUE
    # 57     >>  276 RERAISE                  0
    # >>  278 COPY                     3
    # 280 POP_EXCEPT
    # 282 RERAISE                  1
    # ExceptionTable:
    # 46 to 68 -> 72 [0]
    # 72 to 174 -> 278 [1] lasti
    # 180 to 270 -> 278 [1] lasti
    # 276 to 276 -> 278 [1] lasti

class JSONEncoder:
    """JSONEncoder"""
    def __init__(self):
        """Constructor for JSONEncoder, with sensible defaults.

        If skipkeys is false, then it is a TypeError to attempt
        encoding of keys that are not str, int, float or None.  If
        skipkeys is True, such items are simply skipped.

        If ensure_ascii is true, the output is guaranteed to be str
        objects with all incoming non-ASCII characters escaped.  If
        ensure_ascii is false, the output can contain non-ASCII characters.

        If check_circular is true, then lists, dicts, and custom encoded
        objects will be checked for circular references during encoding to
        prevent an infinite recursion (which would cause an RecursionError).
        Otherwise, no such check takes place.

        If allow_nan is true, then NaN, Infinity, and -Infinity will be
        encoded as such.  This behavior is not JSON specification compliant,
        but is consistent with most JavaScript based encoders and decoders.
        Otherwise, it will be a ValueError to encode such floats.

        If sort_keys is true, then the output of dictionaries will be
        sorted by key; this is useful for regression tests to ensure
        that JSON serializations can be compared on a day-to-day basis.

        If indent is a non-negative integer, then JSON array
        elements and object members will be pretty-printed with that
        indent level.  An indent level of 0 will only insert newlines.
        None is the most compact representation.

        If specified, separators should be an (item_separator, key_separator)
        tuple.  The default is (', ', ': ') if *indent* is ``None`` and
        (',', ': ') otherwise.  To get the most compact JSON representation,
        you should specify (',', ':') to eliminate whitespace.

        If specified, default is a function that gets called for objects
        that can't otherwise be serialized.  It should return a JSON encodable
        version of the object or raise a ``TypeError``.

        """
        # 105           0 RESUME                   0
        # 148           2 LOAD_FAST                1 (skipkeys)
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (skipkeys)
        # 149          16 LOAD_FAST                2 (ensure_ascii)
        # 18 LOAD_FAST                0 (self)
        # 20 STORE_ATTR               1 (ensure_ascii)
        # 150          30 LOAD_FAST                3 (check_circular)
        # 32 LOAD_FAST                0 (self)
        # 34 STORE_ATTR               2 (check_circular)
        # 151          44 LOAD_FAST                4 (allow_nan)
        # 46 LOAD_FAST                0 (self)
        # 48 STORE_ATTR               3 (allow_nan)
        # 152          58 LOAD_FAST                5 (sort_keys)
        # 60 LOAD_FAST                0 (self)
        # 62 STORE_ATTR               4 (sort_keys)
        # 153          72 LOAD_FAST                6 (indent)
        # 74 LOAD_FAST                0 (self)
        # 76 STORE_ATTR               5 (indent)
        # 154          86 LOAD_FAST                7 (separators)
        # 88 POP_JUMP_FORWARD_IF_NONE    16 (to 122)
        # 155          90 LOAD_FAST                7 (separators)
        # 92 UNPACK_SEQUENCE          2
        # 96 LOAD_FAST                0 (self)
        # 98 STORE_ATTR               6 (item_separator)
        # 108 LOAD_FAST                0 (self)
        # 110 STORE_ATTR               7 (key_separator)
        # 120 JUMP_FORWARD             9 (to 140)
        # 156     >>  122 LOAD_FAST                6 (indent)
        # 124 POP_JUMP_FORWARD_IF_NONE     7 (to 140)
        # 157         126 LOAD_CONST               2 (',')
        # 128 LOAD_FAST                0 (self)
        # 130 STORE_ATTR               6 (item_separator)
        # 158     >>  140 LOAD_FAST                8 (default)
        # 142 POP_JUMP_FORWARD_IF_NONE     9 (to 162)
        # 159         144 LOAD_FAST                8 (default)
        # 146 LOAD_FAST                0 (self)
        # 148 STORE_ATTR               8 (default)
        # 158 LOAD_CONST               1 (None)
        # 160 RETURN_VALUE
        # 158     >>  162 LOAD_CONST               1 (None)
        # 164 RETURN_VALUE

    def default(self, o):
        """Implement this method in a subclass such that it returns
        a serializable object for ``o``, or calls the base implementation
        (to raise a ``TypeError``).

        For example, to support arbitrary iterators, you could
        implement default like this::

            def default(self, o):
                try:
                    iterable = iter(o)
                except TypeError:
                    pass
                else:
                    return list(iterable)
                # Let the base class default method raise the TypeError
                return JSONEncoder.default(self, o)

        """
        # 161           0 RESUME                   0
        # 180           2 LOAD_GLOBAL              1 (NULL + TypeError)
        # 14 LOAD_CONST               1 ('Object of type ')
        # 16 LOAD_FAST                1 (o)
        # 18 LOAD_ATTR                1 (__class__)
        # 28 LOAD_ATTR                2 (__name__)
        # 38 FORMAT_VALUE             0
        # 40 LOAD_CONST               2 (' is not JSON serializable')
        # 42 BUILD_STRING             3
        # 44 PRECALL                  1
        # 48 CALL                     1
        # 58 RAISE_VARARGS            1

    def encode(self, o):
        """Return a JSON string representation of a Python data structure.

        >>> from json.encoder import JSONEncoder
        >>> JSONEncoder().encode({"foo": ["bar", "baz"]})
        '{"foo": ["bar", "baz"]}'

        """
        # 183           0 RESUME                   0
        # 192           2 LOAD_GLOBAL              1 (NULL + isinstance)
        # 14 LOAD_FAST                1 (o)
        # 16 LOAD_GLOBAL              2 (str)
        # 28 PRECALL                  2
        # 32 CALL                     2
        # 42 POP_JUMP_FORWARD_IF_FALSE    37 (to 118)
        # 193          44 LOAD_FAST                0 (self)
        # 46 LOAD_ATTR                2 (ensure_ascii)
        # 56 POP_JUMP_FORWARD_IF_FALSE    15 (to 88)
        # 194          58 LOAD_GLOBAL              7 (NULL + encode_basestring_ascii)
        # 70 LOAD_FAST                1 (o)
        # 72 PRECALL                  1
        # 76 CALL                     1
        # 86 RETURN_VALUE
        # 196     >>   88 LOAD_GLOBAL              9 (NULL + encode_basestring)
        # 100 LOAD_FAST                1 (o)
        # 102 PRECALL                  1
        # 106 CALL                     1
        # 116 RETURN_VALUE
        # 200     >>  118 LOAD_FAST                0 (self)
        # 120 LOAD_METHOD              5 (iterencode)
        # 142 LOAD_FAST                1 (o)
        # 144 LOAD_CONST               1 (True)
        # 146 KW_NAMES                 2
        # 148 PRECALL                  2
        # 152 CALL                     2
        # 162 STORE_FAST               2 (chunks)
        # 201         164 LOAD_GLOBAL              1 (NULL + isinstance)
        # 176 LOAD_FAST                2 (chunks)
        # 178 LOAD_GLOBAL             12 (list)
        # 190 LOAD_GLOBAL             14 (tuple)
        # 202 BUILD_TUPLE              2
        # 204 PRECALL                  2
        # 208 CALL                     2
        # 218 POP_JUMP_FORWARD_IF_TRUE    15 (to 250)
        # 202         220 LOAD_GLOBAL             13 (NULL + list)
        # 232 LOAD_FAST                2 (chunks)
        # 234 PRECALL                  1
        # 238 CALL                     1
        # 248 STORE_FAST               2 (chunks)
        # 203     >>  250 LOAD_CONST               3 ('')
        # 252 LOAD_METHOD              8 (join)
        # 274 LOAD_FAST                2 (chunks)
        # 276 PRECALL                  1
        # 280 CALL                     1
        # 290 RETURN_VALUE

    def iterencode(self, o, _one_shot):
        """Encode the given object and yield each string
        representation as available.

        For example::

            for chunk in JSONEncoder().iterencode(bigobject):
                mysocket.write(chunk)

        """
        # 205           0 RESUME                   0
        # 215           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (check_circular)
        # 14 POP_JUMP_FORWARD_IF_FALSE     3 (to 22)
        # 216          16 BUILD_MAP                0
        # 18 STORE_FAST               3 (markers)
        # 20 JUMP_FORWARD             2 (to 26)
        # 218     >>   22 LOAD_CONST               1 (None)
        # 24 STORE_FAST               3 (markers)
        # 219     >>   26 LOAD_FAST                0 (self)
        # 28 LOAD_ATTR                1 (ensure_ascii)
        # 38 POP_JUMP_FORWARD_IF_FALSE     8 (to 56)
        # 220          40 LOAD_GLOBAL              4 (encode_basestring_ascii)
        # 52 STORE_FAST               4 (_encoder)
        # 54 JUMP_FORWARD             7 (to 70)
        # 222     >>   56 LOAD_GLOBAL              6 (encode_basestring)
        # 68 STORE_FAST               4 (_encoder)
        # 224     >>   70 LOAD_FAST                0 (self)
        # 72 LOAD_ATTR                4 (allow_nan)
        # 225          82 LOAD_GLOBAL             10 (float)
        # 94 LOAD_ATTR                6 (__repr__)
        # 104 LOAD_GLOBAL             14 (INFINITY)
        # 116 LOAD_GLOBAL             14 (INFINITY)
        # 128 UNARY_NEGATIVE
        # 224         130 BUILD_TUPLE              4
        # 132 LOAD_CONST               2 (<code object floatstr at 0x000001EBD7183DE0, file "json\encoder.py", line 224>)
        # 134 MAKE_FUNCTION            1 (defaults)
        # 136 STORE_FAST               5 (floatstr)
        # 247         138 LOAD_FAST                2 (_one_shot)
        # 140 POP_JUMP_FORWARD_IF_FALSE    73 (to 288)
        # 142 LOAD_GLOBAL             16 (c_make_encoder)
        # 154 POP_JUMP_FORWARD_IF_NONE    66 (to 288)
        # 248         156 LOAD_FAST                0 (self)
        # 158 LOAD_ATTR                9 (indent)
        # 168 POP_JUMP_FORWARD_IF_NOT_NONE    59 (to 288)
        # 249         170 LOAD_GLOBAL             17 (NULL + c_make_encoder)
        # 250         182 LOAD_FAST                3 (markers)
        # 184 LOAD_FAST                0 (self)
        # 186 LOAD_ATTR               10 (default)
        # 196 LOAD_FAST                4 (_encoder)
        # 198 LOAD_FAST                0 (self)
        # 200 LOAD_ATTR                9 (indent)
        # 251         210 LOAD_FAST                0 (self)
        # 212 LOAD_ATTR               11 (key_separator)
        # 222 LOAD_FAST                0 (self)
        # 224 LOAD_ATTR               12 (item_separator)
        # 234 LOAD_FAST                0 (self)
        # 236 LOAD_ATTR               13 (sort_keys)
        # 252         246 LOAD_FAST                0 (self)
        # 248 LOAD_ATTR               14 (skipkeys)
        # 258 LOAD_FAST                0 (self)
        # 260 LOAD_ATTR                4 (allow_nan)
        # 249         270 PRECALL                  9
        # 274 CALL                     9
        # 284 STORE_FAST               6 (_iterencode)
        # 286 JUMP_FORWARD            54 (to 396)
        # 254     >>  288 LOAD_GLOBAL             31 (NULL + _make_iterencode)
        # 255         300 LOAD_FAST                3 (markers)
        # 302 LOAD_FAST                0 (self)
        # 304 LOAD_ATTR               10 (default)
        # 314 LOAD_FAST                4 (_encoder)
        # 316 LOAD_FAST                0 (self)
        # 318 LOAD_ATTR                9 (indent)
        # 328 LOAD_FAST                5 (floatstr)
        # 256         330 LOAD_FAST                0 (self)
        # 332 LOAD_ATTR               11 (key_separator)
        # 342 LOAD_FAST                0 (self)
        # 344 LOAD_ATTR               12 (item_separator)
        # 354 LOAD_FAST                0 (self)
        # 356 LOAD_ATTR               13 (sort_keys)
        # 257         366 LOAD_FAST                0 (self)
        # 368 LOAD_ATTR               14 (skipkeys)
        # 378 LOAD_FAST                2 (_one_shot)
        # 254         380 PRECALL                 10
        # 384 CALL                    10
        # 394 STORE_FAST               6 (_iterencode)
        # 258     >>  396 PUSH_NULL
        # 398 LOAD_FAST                6 (_iterencode)
        # 400 LOAD_FAST                1 (o)
        # 402 LOAD_CONST               3 (0)
        # 404 PRECALL                  2
        # 408 CALL                     2
        # 418 RETURN_VALUE
        # Disassembly of <code object floatstr at 0x000001EBD7183DE0, file "json\encoder.py", line 224>:
        # 224           0 RESUME                   0
        # 230           2 LOAD_FAST                0 (o)
        # 4 LOAD_FAST                0 (o)
        # 6 COMPARE_OP               3 (!=)
        # 12 POP_JUMP_FORWARD_IF_FALSE     3 (to 20)
        # 231          14 LOAD_CONST               1 ('NaN')
        # 16 STORE_FAST               5 (text)
        # 18 JUMP_FORWARD            29 (to 78)
        # 232     >>   20 LOAD_FAST                0 (o)
        # 22 LOAD_FAST                3 (_inf)
        # 24 COMPARE_OP               2 (==)
        # 30 POP_JUMP_FORWARD_IF_FALSE     3 (to 38)
        # 233          32 LOAD_CONST               2 ('Infinity')
        # 34 STORE_FAST               5 (text)
        # 36 JUMP_FORWARD            20 (to 78)
        # 234     >>   38 LOAD_FAST                0 (o)
        # 40 LOAD_FAST                4 (_neginf)
        # 42 COMPARE_OP               2 (==)
        # 48 POP_JUMP_FORWARD_IF_FALSE     3 (to 56)
        # 235          50 LOAD_CONST               3 ('-Infinity')
        # 52 STORE_FAST               5 (text)
        # 54 JUMP_FORWARD            11 (to 78)
        # 237     >>   56 PUSH_NULL
        # 58 LOAD_FAST                2 (_repr)
        # 60 LOAD_FAST                0 (o)
        # 62 PRECALL                  1
        # 66 CALL                     1
        # 76 RETURN_VALUE
        # 239     >>   78 LOAD_FAST                1 (allow_nan)
        # 80 POP_JUMP_FORWARD_IF_TRUE    31 (to 144)
        # 240          82 LOAD_GLOBAL              1 (NULL + ValueError)
        # 241          94 LOAD_CONST               4 ('Out of range float values are not JSON compliant: ')
        # 242          96 LOAD_GLOBAL              3 (NULL + repr)
        # 108 LOAD_FAST                0 (o)
        # 110 PRECALL                  1
        # 114 CALL                     1
        # 241         124 BINARY_OP                0 (+)
        # 240         128 PRECALL                  1
        # 132 CALL                     1
        # 142 RAISE_VARARGS            1
        # 244     >>  144 LOAD_FAST                5 (text)
        # 146 RETURN_VALUE


def _make_iterencode(markers, _default, _encoder, _indent, _floatstr, _key_separator, _item_separator, _sort_keys, _skipkeys, _one_shot, ValueError, dict, float, id, int, isinstance, list, str, tuple, _intstr):
    # 0 MAKE_CELL                0 (markers)
    # 2 MAKE_CELL                1 (_default)
    # 4 MAKE_CELL                2 (_encoder)
    # 6 MAKE_CELL                3 (_indent)
    # 8 MAKE_CELL                4 (_floatstr)
    # 10 MAKE_CELL                5 (_key_separator)
    # 12 MAKE_CELL                6 (_item_separator)
    # 14 MAKE_CELL                7 (_sort_keys)
    # 16 MAKE_CELL                8 (_skipkeys)
    # 18 MAKE_CELL               10 (ValueError)
    # 20 MAKE_CELL               11 (dict)
    # 22 MAKE_CELL               12 (float)
    # 24 MAKE_CELL               13 (id)
    # 26 MAKE_CELL               14 (int)
    # 28 MAKE_CELL               15 (isinstance)
    # 30 MAKE_CELL               16 (list)
    # 32 MAKE_CELL               17 (str)
    # 34 MAKE_CELL               18 (tuple)
    # 36 MAKE_CELL               19 (_intstr)
    # 38 MAKE_CELL               20 (_iterencode)
    # 40 MAKE_CELL               21 (_iterencode_dict)
    # 42 MAKE_CELL               22 (_iterencode_list)
    # 260          44 RESUME                   0
    # 275          46 LOAD_DEREF               3 (_indent)
    # 48 POP_JUMP_FORWARD_IF_NONE    17 (to 84)
    # 50 PUSH_NULL
    # 52 LOAD_DEREF              15 (isinstance)
    # 54 LOAD_DEREF               3 (_indent)
    # 56 LOAD_DEREF              17 (str)
    # 58 PRECALL                  2
    # 62 CALL                     2
    # 72 POP_JUMP_FORWARD_IF_TRUE     5 (to 84)
    # 276          74 LOAD_CONST               1 (' ')
    # 76 LOAD_DEREF               3 (_indent)
    # 78 BINARY_OP                5 (*)
    # 82 STORE_DEREF              3 (_indent)
    # 278     >>   84 LOAD_CLOSURE            10 (ValueError)
    # 86 LOAD_CLOSURE             2 (_encoder)
    # 88 LOAD_CLOSURE             4 (_floatstr)
    # 90 LOAD_CLOSURE             3 (_indent)
    # 92 LOAD_CLOSURE            19 (_intstr)
    # 94 LOAD_CLOSURE             6 (_item_separator)
    # 96 LOAD_CLOSURE            20 (_iterencode)
    # 98 LOAD_CLOSURE            21 (_iterencode_dict)
    # 100 LOAD_CLOSURE            22 (_iterencode_list)
    # 102 LOAD_CLOSURE            11 (dict)
    # 104 LOAD_CLOSURE            12 (float)
    # 106 LOAD_CLOSURE            13 (id)
    # 108 LOAD_CLOSURE            14 (int)
    # 110 LOAD_CLOSURE            15 (isinstance)
    # 112 LOAD_CLOSURE            16 (list)
    # 114 LOAD_CLOSURE             0 (markers)
    # 116 LOAD_CLOSURE            17 (str)
    # 118 LOAD_CLOSURE            18 (tuple)
    # 120 BUILD_TUPLE             18
    # 122 LOAD_CONST               2 (<code object _iterencode_list at 0x000001EBD7635350, file "json\encoder.py", line 278>)
    # 124 MAKE_FUNCTION            8 (closure)
    # 126 STORE_DEREF             22 (_iterencode_list)
    # 334         128 LOAD_CLOSURE            10 (ValueError)
    # 130 LOAD_CLOSURE             2 (_encoder)
    # 132 LOAD_CLOSURE             4 (_floatstr)
    # 134 LOAD_CLOSURE             3 (_indent)
    # 136 LOAD_CLOSURE            19 (_intstr)
    # 138 LOAD_CLOSURE             6 (_item_separator)
    # 140 LOAD_CLOSURE            20 (_iterencode)
    # 142 LOAD_CLOSURE            21 (_iterencode_dict)
    # 144 LOAD_CLOSURE            22 (_iterencode_list)
    # 146 LOAD_CLOSURE             5 (_key_separator)
    # 148 LOAD_CLOSURE             8 (_skipkeys)
    # 150 LOAD_CLOSURE             7 (_sort_keys)
    # 152 LOAD_CLOSURE            11 (dict)
    # 154 LOAD_CLOSURE            12 (float)
    # 156 LOAD_CLOSURE            13 (id)
    # 158 LOAD_CLOSURE            14 (int)
    # 160 LOAD_CLOSURE            15 (isinstance)
    # 162 LOAD_CLOSURE            16 (list)
    # 164 LOAD_CLOSURE             0 (markers)
    # 166 LOAD_CLOSURE            17 (str)
    # 168 LOAD_CLOSURE            18 (tuple)
    # 170 BUILD_TUPLE             21
    # 172 LOAD_CONST               3 (<code object _iterencode_dict at 0x000001EBD6FC0800, file "json\encoder.py", line 334>)
    # 174 MAKE_FUNCTION            8 (closure)
    # 176 STORE_DEREF             21 (_iterencode_dict)
    # 414         178 LOAD_CLOSURE            10 (ValueError)
    # 180 LOAD_CLOSURE             1 (_default)
    # 182 LOAD_CLOSURE             2 (_encoder)
    # 184 LOAD_CLOSURE             4 (_floatstr)
    # 186 LOAD_CLOSURE            19 (_intstr)
    # 188 LOAD_CLOSURE            20 (_iterencode)
    # 190 LOAD_CLOSURE            21 (_iterencode_dict)
    # 192 LOAD_CLOSURE            22 (_iterencode_list)
    # 194 LOAD_CLOSURE            11 (dict)
    # 196 LOAD_CLOSURE            12 (float)
    # 198 LOAD_CLOSURE            13 (id)
    # 200 LOAD_CLOSURE            14 (int)
    # 202 LOAD_CLOSURE            15 (isinstance)
    # 204 LOAD_CLOSURE            16 (list)
    # 206 LOAD_CLOSURE             0 (markers)
    # 208 LOAD_CLOSURE            17 (str)
    # 210 LOAD_CLOSURE            18 (tuple)
    # 212 BUILD_TUPLE             17
    # 214 LOAD_CONST               4 (<code object _iterencode at 0x000001EBD7526850, file "json\encoder.py", line 414>)
    # 216 MAKE_FUNCTION            8 (closure)
    # 218 STORE_DEREF             20 (_iterencode)
    # 443         220 LOAD_DEREF              20 (_iterencode)
    # 222 RETURN_VALUE
    # Disassembly of <code object _iterencode_list at 0x000001EBD7635350, file "json\encoder.py", line 278>:
    # 0 COPY_FREE_VARS          18
    # 278           2 RETURN_GENERATOR
    # 4 POP_TOP
    # 6 RESUME                   0
    # 279           8 LOAD_FAST                0 (lst)
    # 10 POP_JUMP_FORWARD_IF_TRUE     6 (to 24)
    # 280          12 LOAD_CONST               1 ('[]')
    # 14 YIELD_VALUE
    # 16 RESUME                   1
    # 18 POP_TOP
    # 281          20 LOAD_CONST               0 (None)
    # 22 RETURN_VALUE
    # 282     >>   24 LOAD_DEREF              24 (markers)
    # 26 POP_JUMP_FORWARD_IF_NONE    31 (to 90)
    # 283          28 PUSH_NULL
    # 30 LOAD_DEREF              20 (id)
    # 32 LOAD_FAST                0 (lst)
    # 34 PRECALL                  1
    # 38 CALL                     1
    # 48 STORE_FAST               2 (markerid)
    # 284          50 LOAD_FAST                2 (markerid)
    # 52 LOAD_DEREF              24 (markers)
    # 54 CONTAINS_OP              0
    # 56 POP_JUMP_FORWARD_IF_FALSE    11 (to 80)
    # 285          58 PUSH_NULL
    # 60 LOAD_DEREF               9 (ValueError)
    # 62 LOAD_CONST               2 ('Circular reference detected')
    # 64 PRECALL                  1
    # 68 CALL                     1
    # 78 RAISE_VARARGS            1
    # 286     >>   80 LOAD_FAST                0 (lst)
    # 82 LOAD_DEREF              24 (markers)
    # 84 LOAD_FAST                2 (markerid)
    # 86 STORE_SUBSCR
    # 287     >>   90 LOAD_CONST               3 ('[')
    # 92 STORE_FAST               3 (buf)
    # 288          94 LOAD_DEREF              12 (_indent)
    # 96 POP_JUMP_FORWARD_IF_NONE    24 (to 146)
    # 289          98 LOAD_FAST                1 (_current_indent_level)
    # 100 LOAD_CONST               4 (1)
    # 102 BINARY_OP               13 (+=)
    # 106 STORE_FAST               1 (_current_indent_level)
    # 290         108 LOAD_CONST               5 ('\n')
    # 110 LOAD_DEREF              12 (_indent)
    # 112 LOAD_FAST                1 (_current_indent_level)
    # 114 BINARY_OP                5 (*)
    # 118 BINARY_OP                0 (+)
    # 122 STORE_FAST               4 (newline_indent)
    # 291         124 LOAD_DEREF              14 (_item_separator)
    # 126 LOAD_FAST                4 (newline_indent)
    # 128 BINARY_OP                0 (+)
    # 132 STORE_FAST               5 (separator)
    # 292         134 LOAD_FAST                3 (buf)
    # 136 LOAD_FAST                4 (newline_indent)
    # 138 BINARY_OP               13 (+=)
    # 142 STORE_FAST               3 (buf)
    # 144 JUMP_FORWARD             4 (to 154)
    # 294     >>  146 LOAD_CONST               0 (None)
    # 148 STORE_FAST               4 (newline_indent)
    # 295         150 LOAD_DEREF              14 (_item_separator)
    # 152 STORE_FAST               5 (separator)
    # 296     >>  154 LOAD_CONST               6 (True)
    # 156 STORE_FAST               6 (first)
    # 297         158 LOAD_FAST                0 (lst)
    # 160 GET_ITER
    # >>  162 FOR_ITER               206 (to 576)
    # 164 STORE_FAST               7 (value)
    # 298         166 LOAD_FAST                6 (first)
    # 168 POP_JUMP_FORWARD_IF_FALSE     3 (to 176)
    # 299         170 LOAD_CONST               7 (False)
    # 172 STORE_FAST               6 (first)
    # 174 JUMP_FORWARD             2 (to 180)
    # 301     >>  176 LOAD_FAST                5 (separator)
    # 178 STORE_FAST               3 (buf)
    # 302     >>  180 PUSH_NULL
    # 182 LOAD_DEREF              22 (isinstance)
    # 184 LOAD_FAST                7 (value)
    # 186 LOAD_DEREF              25 (str)
    # 188 PRECALL                  2
    # 192 CALL                     2
    # 202 POP_JUMP_FORWARD_IF_FALSE    17 (to 238)
    # 303         204 LOAD_FAST                3 (buf)
    # 206 PUSH_NULL
    # 208 LOAD_DEREF              10 (_encoder)
    # 210 LOAD_FAST                7 (value)
    # 212 PRECALL                  1
    # 216 CALL                     1
    # 226 BINARY_OP                0 (+)
    # 230 YIELD_VALUE
    # 232 RESUME                   1
    # 234 POP_TOP
    # 236 JUMP_BACKWARD           38 (to 162)
    # 304     >>  238 LOAD_FAST                7 (value)
    # 240 POP_JUMP_FORWARD_IF_NOT_NONE     8 (to 258)
    # 305         242 LOAD_FAST                3 (buf)
    # 244 LOAD_CONST               8 ('null')
    # 246 BINARY_OP                0 (+)
    # 250 YIELD_VALUE
    # 252 RESUME                   1
    # 254 POP_TOP
    # 256 JUMP_BACKWARD           48 (to 162)
    # 306     >>  258 LOAD_FAST                7 (value)
    # 260 LOAD_CONST               6 (True)
    # 262 IS_OP                    0
    # 264 POP_JUMP_FORWARD_IF_FALSE     8 (to 282)
    # 307         266 LOAD_FAST                3 (buf)
    # 268 LOAD_CONST               9 ('true')
    # 270 BINARY_OP                0 (+)
    # 274 YIELD_VALUE
    # 276 RESUME                   1
    # 278 POP_TOP
    # 280 JUMP_BACKWARD           60 (to 162)
    # 308     >>  282 LOAD_FAST                7 (value)
    # 284 LOAD_CONST               7 (False)
    # 286 IS_OP                    0
    # 288 POP_JUMP_FORWARD_IF_FALSE     8 (to 306)
    # 309         290 LOAD_FAST                3 (buf)
    # 292 LOAD_CONST              10 ('false')
    # 294 BINARY_OP                0 (+)
    # 298 YIELD_VALUE
    # 300 RESUME                   1
    # 302 POP_TOP
    # 304 JUMP_BACKWARD           72 (to 162)
    # 310     >>  306 PUSH_NULL
    # 308 LOAD_DEREF              22 (isinstance)
    # 310 LOAD_FAST                7 (value)
    # 312 LOAD_DEREF              21 (int)
    # 314 PRECALL                  2
    # 318 CALL                     2
    # 328 POP_JUMP_FORWARD_IF_FALSE    17 (to 364)
    # 314         330 LOAD_FAST                3 (buf)
    # 332 PUSH_NULL
    # 334 LOAD_DEREF              13 (_intstr)
    # 336 LOAD_FAST                7 (value)
    # 338 PRECALL                  1
    # 342 CALL                     1
    # 352 BINARY_OP                0 (+)
    # 356 YIELD_VALUE
    # 358 RESUME                   1
    # 360 POP_TOP
    # 362 JUMP_BACKWARD          101 (to 162)
    # 315     >>  364 PUSH_NULL
    # 366 LOAD_DEREF              22 (isinstance)
    # 368 LOAD_FAST                7 (value)
    # 370 LOAD_DEREF              19 (float)
    # 372 PRECALL                  2
    # 376 CALL                     2
    # 386 POP_JUMP_FORWARD_IF_FALSE    17 (to 422)
    # 317         388 LOAD_FAST                3 (buf)
    # 390 PUSH_NULL
    # 392 LOAD_DEREF              11 (_floatstr)
    # 394 LOAD_FAST                7 (value)
    # 396 PRECALL                  1
    # 400 CALL                     1
    # 410 BINARY_OP                0 (+)
    # 414 YIELD_VALUE
    # 416 RESUME                   1
    # 418 POP_TOP
    # 420 JUMP_BACKWARD          130 (to 162)
    # 319     >>  422 LOAD_FAST                3 (buf)
    # 424 YIELD_VALUE
    # 426 RESUME                   1
    # 428 POP_TOP
    # 320         430 PUSH_NULL
    # 432 LOAD_DEREF              22 (isinstance)
    # 434 LOAD_FAST                7 (value)
    # 436 LOAD_DEREF              23 (list)
    # 438 LOAD_DEREF              26 (tuple)
    # 440 BUILD_TUPLE              2
    # 442 PRECALL                  2
    # 446 CALL                     2
    # 456 POP_JUMP_FORWARD_IF_FALSE    13 (to 484)
    # 321         458 PUSH_NULL
    # 460 LOAD_DEREF              17 (_iterencode_list)
    # 462 LOAD_FAST                7 (value)
    # 464 LOAD_FAST                1 (_current_indent_level)
    # 466 PRECALL                  2
    # 470 CALL                     2
    # 480 STORE_FAST               8 (chunks)
    # 482 JUMP_FORWARD            37 (to 558)
    # 322     >>  484 PUSH_NULL
    # 486 LOAD_DEREF              22 (isinstance)
    # 488 LOAD_FAST                7 (value)
    # 490 LOAD_DEREF              18 (dict)
    # 492 PRECALL                  2
    # 496 CALL                     2
    # 506 POP_JUMP_FORWARD_IF_FALSE    13 (to 534)
    # 323         508 PUSH_NULL
    # 510 LOAD_DEREF              16 (_iterencode_dict)
    # 512 LOAD_FAST                7 (value)
    # 514 LOAD_FAST                1 (_current_indent_level)
    # 516 PRECALL                  2
    # 520 CALL                     2
    # 530 STORE_FAST               8 (chunks)
    # 532 JUMP_FORWARD            12 (to 558)
    # 325     >>  534 PUSH_NULL
    # 536 LOAD_DEREF              15 (_iterencode)
    # 538 LOAD_FAST                7 (value)
    # 540 LOAD_FAST                1 (_current_indent_level)
    # 542 PRECALL                  2
    # 546 CALL                     2
    # 556 STORE_FAST               8 (chunks)
    # 326     >>  558 LOAD_FAST                8 (chunks)
    # 560 GET_YIELD_FROM_ITER
    # 562 LOAD_CONST               0 (None)
    # >>  564 SEND                     3 (to 572)
    # 566 YIELD_VALUE
    # 568 RESUME                   2
    # 570 JUMP_BACKWARD_NO_INTERRUPT     4 (to 564)
    # >>  572 POP_TOP
    # 574 JUMP_BACKWARD          207 (to 162)
    # 327     >>  576 LOAD_FAST                4 (newline_indent)
    # 578 POP_JUMP_FORWARD_IF_NONE    15 (to 610)
    # 328         580 LOAD_FAST                1 (_current_indent_level)
    # 582 LOAD_CONST               4 (1)
    # 584 BINARY_OP               23 (-=)
    # 588 STORE_FAST               1 (_current_indent_level)
    # 329         590 LOAD_CONST               5 ('\n')
    # 592 LOAD_DEREF              12 (_indent)
    # 594 LOAD_FAST                1 (_current_indent_level)
    # 596 BINARY_OP                5 (*)
    # 600 BINARY_OP                0 (+)
    # 604 YIELD_VALUE
    # 606 RESUME                   1
    # 608 POP_TOP
    # 330     >>  610 LOAD_CONST              11 (']')
    # 612 YIELD_VALUE
    # 614 RESUME                   1
    # 616 POP_TOP
    # 331         618 LOAD_DEREF              24 (markers)
    # 620 POP_JUMP_FORWARD_IF_NONE     5 (to 632)
    # 332         622 LOAD_DEREF              24 (markers)
    # 624 LOAD_FAST                2 (markerid)
    # 626 DELETE_SUBSCR
    # 628 LOAD_CONST               0 (None)
    # 630 RETURN_VALUE
    # 331     >>  632 LOAD_CONST               0 (None)
    # 634 RETURN_VALUE
    # Disassembly of <code object _iterencode_dict at 0x000001EBD6FC0800, file "json\encoder.py", line 334>:
    # 0 COPY_FREE_VARS          21
    # 334           2 RETURN_GENERATOR
    # 4 POP_TOP
    # 6 RESUME                   0
    # 335           8 LOAD_FAST                0 (dct)
    # 10 POP_JUMP_FORWARD_IF_TRUE     6 (to 24)
    # 336          12 LOAD_CONST               1 ('{}')
    # 14 YIELD_VALUE
    # 16 RESUME                   1
    # 18 POP_TOP
    # 337          20 LOAD_CONST               0 (None)
    # 22 RETURN_VALUE
    # 338     >>   24 LOAD_DEREF              28 (markers)
    # 26 POP_JUMP_FORWARD_IF_NONE    31 (to 90)
    # 339          28 PUSH_NULL
    # 30 LOAD_DEREF              24 (id)
    # 32 LOAD_FAST                0 (dct)
    # 34 PRECALL                  1
    # 38 CALL                     1
    # 48 STORE_FAST               2 (markerid)
    # 340          50 LOAD_FAST                2 (markerid)
    # 52 LOAD_DEREF              28 (markers)
    # 54 CONTAINS_OP              0
    # 56 POP_JUMP_FORWARD_IF_FALSE    11 (to 80)
    # 341          58 PUSH_NULL
    # 60 LOAD_DEREF              10 (ValueError)
    # 62 LOAD_CONST               2 ('Circular reference detected')
    # 64 PRECALL                  1
    # 68 CALL                     1
    # 78 RAISE_VARARGS            1
    # 342     >>   80 LOAD_FAST                0 (dct)
    # 82 LOAD_DEREF              28 (markers)
    # 84 LOAD_FAST                2 (markerid)
    # 86 STORE_SUBSCR
    # 343     >>   90 LOAD_CONST               3 ('{')
    # 92 YIELD_VALUE
    # 94 RESUME                   1
    # 96 POP_TOP
    # 344          98 LOAD_DEREF              13 (_indent)
    # 100 POP_JUMP_FORWARD_IF_NONE    23 (to 148)
    # 345         102 LOAD_FAST                1 (_current_indent_level)
    # 104 LOAD_CONST               4 (1)
    # 106 BINARY_OP               13 (+=)
    # 110 STORE_FAST               1 (_current_indent_level)
    # 346         112 LOAD_CONST               5 ('\n')
    # 114 LOAD_DEREF              13 (_indent)
    # 116 LOAD_FAST                1 (_current_indent_level)
    # 118 BINARY_OP                5 (*)
    # 122 BINARY_OP                0 (+)
    # 126 STORE_FAST               3 (newline_indent)
    # 347         128 LOAD_DEREF              15 (_item_separator)
    # 130 LOAD_FAST                3 (newline_indent)
    # 132 BINARY_OP                0 (+)
    # 136 STORE_FAST               4 (item_separator)
    # 348         138 LOAD_FAST                3 (newline_indent)
    # 140 YIELD_VALUE
    # 142 RESUME                   1
    # 144 POP_TOP
    # 146 JUMP_FORWARD             4 (to 156)
    # 350     >>  148 LOAD_CONST               0 (None)
    # 150 STORE_FAST               3 (newline_indent)
    # 351         152 LOAD_DEREF              15 (_item_separator)
    # 154 STORE_FAST               4 (item_separator)
    # 352     >>  156 LOAD_CONST               6 (True)
    # 158 STORE_FAST               5 (first)
    # 353         160 LOAD_DEREF              21 (_sort_keys)
    # 162 POP_JUMP_FORWARD_IF_FALSE    34 (to 232)
    # 354         164 LOAD_GLOBAL              1 (NULL + sorted)
    # 176 LOAD_FAST                0 (dct)
    # 178 LOAD_METHOD              1 (items)
    # 200 PRECALL                  0
    # 204 CALL                     0
    # 214 PRECALL                  1
    # 218 CALL                     1
    # 228 STORE_FAST               6 (items)
    # 230 JUMP_FORWARD            20 (to 272)
    # 356     >>  232 LOAD_FAST                0 (dct)
    # 234 LOAD_METHOD              1 (items)
    # 256 PRECALL                  0
    # 260 CALL                     0
    # 270 STORE_FAST               6 (items)
    # 357     >>  272 LOAD_FAST                6 (items)
    # 274 GET_ITER
    # >>  276 EXTENDED_ARG             1
    # 278 FOR_ITER               318 (to 916)
    # 280 UNPACK_SEQUENCE          2
    # 284 STORE_FAST               7 (key)
    # 286 STORE_FAST               8 (value)
    # 358         288 PUSH_NULL
    # 290 LOAD_DEREF              26 (isinstance)
    # 292 LOAD_FAST                7 (key)
    # 294 LOAD_DEREF              29 (str)
    # 296 PRECALL                  2
    # 300 CALL                     2
    # 310 POP_JUMP_FORWARD_IF_FALSE     1 (to 314)
    # 359         312 JUMP_FORWARD            98 (to 510)
    # 362     >>  314 PUSH_NULL
    # 316 LOAD_DEREF              26 (isinstance)
    # 318 LOAD_FAST                7 (key)
    # 320 LOAD_DEREF              23 (float)
    # 322 PRECALL                  2
    # 326 CALL                     2
    # 336 POP_JUMP_FORWARD_IF_FALSE    12 (to 362)
    # 364         338 PUSH_NULL
    # 340 LOAD_DEREF              12 (_floatstr)
    # 342 LOAD_FAST                7 (key)
    # 344 PRECALL                  1
    # 348 CALL                     1
    # 358 STORE_FAST               7 (key)
    # 360 JUMP_FORWARD            74 (to 510)
    # 365     >>  362 LOAD_FAST                7 (key)
    # 364 LOAD_CONST               6 (True)
    # 366 IS_OP                    0
    # 368 POP_JUMP_FORWARD_IF_FALSE     3 (to 376)
    # 366         370 LOAD_CONST               7 ('true')
    # 372 STORE_FAST               7 (key)
    # 374 JUMP_FORWARD            67 (to 510)
    # 367     >>  376 LOAD_FAST                7 (key)
    # 378 LOAD_CONST               8 (False)
    # 380 IS_OP                    0
    # 382 POP_JUMP_FORWARD_IF_FALSE     3 (to 390)
    # 368         384 LOAD_CONST               9 ('false')
    # 386 STORE_FAST               7 (key)
    # 388 JUMP_FORWARD            60 (to 510)
    # 369     >>  390 LOAD_FAST                7 (key)
    # 392 POP_JUMP_FORWARD_IF_NOT_NONE     3 (to 400)
    # 370         394 LOAD_CONST              10 ('null')
    # 396 STORE_FAST               7 (key)
    # 398 JUMP_FORWARD            55 (to 510)
    # 371     >>  400 PUSH_NULL
    # 402 LOAD_DEREF              26 (isinstance)
    # 404 LOAD_FAST                7 (key)
    # 406 LOAD_DEREF              25 (int)
    # 408 PRECALL                  2
    # 412 CALL                     2
    # 422 POP_JUMP_FORWARD_IF_FALSE    12 (to 448)
    # 373         424 PUSH_NULL
    # 426 LOAD_DEREF              14 (_intstr)
    # 428 LOAD_FAST                7 (key)
    # 430 PRECALL                  1
    # 434 CALL                     1
    # 444 STORE_FAST               7 (key)
    # 446 JUMP_FORWARD            31 (to 510)
    # 374     >>  448 LOAD_DEREF              20 (_skipkeys)
    # 450 POP_JUMP_FORWARD_IF_FALSE     1 (to 454)
    # 375         452 JUMP_BACKWARD           89 (to 276)
    # 377     >>  454 LOAD_GLOBAL              5 (NULL + TypeError)
    # 466 LOAD_CONST              11 ('keys must be str, int, float, bool or None, not ')
    # 378         468 LOAD_FAST                7 (key)
    # 470 LOAD_ATTR                3 (__class__)
    # 480 LOAD_ATTR                4 (__name__)
    # 377         490 FORMAT_VALUE             0
    # 492 BUILD_STRING             2
    # 494 PRECALL                  1
    # 498 CALL                     1
    # 508 RAISE_VARARGS            1
    # 379     >>  510 LOAD_FAST                5 (first)
    # 512 POP_JUMP_FORWARD_IF_FALSE     3 (to 520)
    # 380         514 LOAD_CONST               8 (False)
    # 516 STORE_FAST               5 (first)
    # 518 JUMP_FORWARD             4 (to 528)
    # 382     >>  520 LOAD_FAST                4 (item_separator)
    # 522 YIELD_VALUE
    # 524 RESUME                   1
    # 526 POP_TOP
    # 383     >>  528 PUSH_NULL
    # 530 LOAD_DEREF              11 (_encoder)
    # 532 LOAD_FAST                7 (key)
    # 534 PRECALL                  1
    # 538 CALL                     1
    # 548 YIELD_VALUE
    # 550 RESUME                   1
    # 552 POP_TOP
    # 384         554 LOAD_DEREF              19 (_key_separator)
    # 556 YIELD_VALUE
    # 558 RESUME                   1
    # 560 POP_TOP
    # 385         562 PUSH_NULL
    # 564 LOAD_DEREF              26 (isinstance)
    # 566 LOAD_FAST                8 (value)
    # 568 LOAD_DEREF              29 (str)
    # 570 PRECALL                  2
    # 574 CALL                     2
    # 584 POP_JUMP_FORWARD_IF_FALSE    14 (to 614)
    # 386         586 PUSH_NULL
    # 588 LOAD_DEREF              11 (_encoder)
    # 590 LOAD_FAST                8 (value)
    # 592 PRECALL                  1
    # 596 CALL                     1
    # 606 YIELD_VALUE
    # 608 RESUME                   1
    # 610 POP_TOP
    # 612 JUMP_BACKWARD          169 (to 276)
    # 387     >>  614 LOAD_FAST                8 (value)
    # 616 POP_JUMP_FORWARD_IF_NOT_NONE     5 (to 628)
    # 388         618 LOAD_CONST              10 ('null')
    # 620 YIELD_VALUE
    # 622 RESUME                   1
    # 624 POP_TOP
    # 626 JUMP_BACKWARD          176 (to 276)
    # 389     >>  628 LOAD_FAST                8 (value)
    # 630 LOAD_CONST               6 (True)
    # 632 IS_OP                    0
    # 634 POP_JUMP_FORWARD_IF_FALSE     5 (to 646)
    # 390         636 LOAD_CONST               7 ('true')
    # 638 YIELD_VALUE
    # 640 RESUME                   1
    # 642 POP_TOP
    # 644 JUMP_BACKWARD          185 (to 276)
    # 391     >>  646 LOAD_FAST                8 (value)
    # 648 LOAD_CONST               8 (False)
    # 650 IS_OP                    0
    # 652 POP_JUMP_FORWARD_IF_FALSE     5 (to 664)
    # 392         654 LOAD_CONST               9 ('false')
    # 656 YIELD_VALUE
    # 658 RESUME                   1
    # 660 POP_TOP
    # 662 JUMP_BACKWARD          194 (to 276)
    # 393     >>  664 PUSH_NULL
    # 666 LOAD_DEREF              26 (isinstance)
    # 668 LOAD_FAST                8 (value)
    # 670 LOAD_DEREF              25 (int)
    # 672 PRECALL                  2
    # 676 CALL                     2
    # 686 POP_JUMP_FORWARD_IF_FALSE    14 (to 716)
    # 395         688 PUSH_NULL
    # 690 LOAD_DEREF              14 (_intstr)
    # 692 LOAD_FAST                8 (value)
    # 694 PRECALL                  1
    # 698 CALL                     1
    # 708 YIELD_VALUE
    # 710 RESUME                   1
    # 712 POP_TOP
    # 714 JUMP_BACKWARD          220 (to 276)
    # 396     >>  716 PUSH_NULL
    # 718 LOAD_DEREF              26 (isinstance)
    # 720 LOAD_FAST                8 (value)
    # 722 LOAD_DEREF              23 (float)
    # 724 PRECALL                  2
    # 728 CALL                     2
    # 738 POP_JUMP_FORWARD_IF_FALSE    14 (to 768)
    # 398         740 PUSH_NULL
    # 742 LOAD_DEREF              12 (_floatstr)
    # 744 LOAD_FAST                8 (value)
    # 746 PRECALL                  1
    # 750 CALL                     1
    # 760 YIELD_VALUE
    # 762 RESUME                   1
    # 764 POP_TOP
    # 766 JUMP_BACKWARD          246 (to 276)
    # 400     >>  768 PUSH_NULL
    # 770 LOAD_DEREF              26 (isinstance)
    # 772 LOAD_FAST                8 (value)
    # 774 LOAD_DEREF              27 (list)
    # 776 LOAD_DEREF              30 (tuple)
    # 778 BUILD_TUPLE              2
    # 780 PRECALL                  2
    # 784 CALL                     2
    # 794 POP_JUMP_FORWARD_IF_FALSE    13 (to 822)
    # 401         796 PUSH_NULL
    # 798 LOAD_DEREF              18 (_iterencode_list)
    # 800 LOAD_FAST                8 (value)
    # 802 LOAD_FAST                1 (_current_indent_level)
    # 804 PRECALL                  2
    # 808 CALL                     2
    # 818 STORE_FAST               9 (chunks)
    # 820 JUMP_FORWARD            37 (to 896)
    # 402     >>  822 PUSH_NULL
    # 824 LOAD_DEREF              26 (isinstance)
    # 826 LOAD_FAST                8 (value)
    # 828 LOAD_DEREF              22 (dict)
    # 830 PRECALL                  2
    # 834 CALL                     2
    # 844 POP_JUMP_FORWARD_IF_FALSE    13 (to 872)
    # 403         846 PUSH_NULL
    # 848 LOAD_DEREF              17 (_iterencode_dict)
    # 850 LOAD_FAST                8 (value)
    # 852 LOAD_FAST                1 (_current_indent_level)
    # 854 PRECALL                  2
    # 858 CALL                     2
    # 868 STORE_FAST               9 (chunks)
    # 870 JUMP_FORWARD            12 (to 896)
    # 405     >>  872 PUSH_NULL
    # 874 LOAD_DEREF              16 (_iterencode)
    # 876 LOAD_FAST                8 (value)
    # 878 LOAD_FAST                1 (_current_indent_level)
    # 880 PRECALL                  2
    # 884 CALL                     2
    # 894 STORE_FAST               9 (chunks)
    # 406     >>  896 LOAD_FAST                9 (chunks)
    # 898 GET_YIELD_FROM_ITER
    # 900 LOAD_CONST               0 (None)
    # >>  902 SEND                     3 (to 910)
    # 904 YIELD_VALUE
    # 906 RESUME                   2
    # 908 JUMP_BACKWARD_NO_INTERRUPT     4 (to 902)
    # >>  910 POP_TOP
    # 912 EXTENDED_ARG             1
    # 914 JUMP_BACKWARD          320 (to 276)
    # 407     >>  916 LOAD_FAST                3 (newline_indent)
    # 918 POP_JUMP_FORWARD_IF_NONE    15 (to 950)
    # 408         920 LOAD_FAST                1 (_current_indent_level)
    # 922 LOAD_CONST               4 (1)
    # 924 BINARY_OP               23 (-=)
    # 928 STORE_FAST               1 (_current_indent_level)
    # 409         930 LOAD_CONST               5 ('\n')
    # 932 LOAD_DEREF              13 (_indent)
    # 934 LOAD_FAST                1 (_current_indent_level)
    # 936 BINARY_OP                5 (*)
    # 940 BINARY_OP                0 (+)
    # 944 YIELD_VALUE
    # 946 RESUME                   1
    # 948 POP_TOP
    # 410     >>  950 LOAD_CONST              12 ('}')
    # 952 YIELD_VALUE
    # 954 RESUME                   1
    # 956 POP_TOP
    # 411         958 LOAD_DEREF              28 (markers)
    # 960 POP_JUMP_FORWARD_IF_NONE     5 (to 972)
    # 412         962 LOAD_DEREF              28 (markers)
    # 964 LOAD_FAST                2 (markerid)
    # 966 DELETE_SUBSCR
    # 968 LOAD_CONST               0 (None)
    # 970 RETURN_VALUE
    # 411     >>  972 LOAD_CONST               0 (None)
    # 974 RETURN_VALUE
    # Disassembly of <code object _iterencode at 0x000001EBD7526850, file "json\encoder.py", line 414>:
    # 0 COPY_FREE_VARS          17
    # 414           2 RETURN_GENERATOR
    # 4 POP_TOP
    # 6 RESUME                   0
    # 415           8 PUSH_NULL
    # 10 LOAD_DEREF              15 (isinstance)
    # 12 LOAD_FAST                0 (o)
    # 14 LOAD_DEREF              18 (str)
    # 16 PRECALL                  2
    # 20 CALL                     2
    # 30 POP_JUMP_FORWARD_IF_FALSE    15 (to 62)
    # 416          32 PUSH_NULL
    # 34 LOAD_DEREF               5 (_encoder)
    # 36 LOAD_FAST                0 (o)
    # 38 PRECALL                  1
    # 42 CALL                     1
    # 52 YIELD_VALUE
    # 54 RESUME                   1
    # 56 POP_TOP
    # 58 LOAD_CONST               0 (None)
    # 60 RETURN_VALUE
    # 417     >>   62 LOAD_FAST                0 (o)
    # 64 POP_JUMP_FORWARD_IF_NOT_NONE     6 (to 78)
    # 418          66 LOAD_CONST               1 ('null')
    # 68 YIELD_VALUE
    # 70 RESUME                   1
    # 72 POP_TOP
    # 74 LOAD_CONST               0 (None)
    # 76 RETURN_VALUE
    # 419     >>   78 LOAD_FAST                0 (o)
    # 80 LOAD_CONST               2 (True)
    # 82 IS_OP                    0
    # 84 POP_JUMP_FORWARD_IF_FALSE     6 (to 98)
    # 420          86 LOAD_CONST               3 ('true')
    # 88 YIELD_VALUE
    # 90 RESUME                   1
    # 92 POP_TOP
    # 94 LOAD_CONST               0 (None)
    # 96 RETURN_VALUE
    # 421     >>   98 LOAD_FAST                0 (o)
    # 100 LOAD_CONST               4 (False)
    # 102 IS_OP                    0
    # 104 POP_JUMP_FORWARD_IF_FALSE     6 (to 118)
    # 422         106 LOAD_CONST               5 ('false')
    # 108 YIELD_VALUE
    # 110 RESUME                   1
    # 112 POP_TOP
    # 114 LOAD_CONST               0 (None)
    # 116 RETURN_VALUE
    # 423     >>  118 PUSH_NULL
    # 120 LOAD_DEREF              15 (isinstance)
    # 122 LOAD_FAST                0 (o)
    # 124 LOAD_DEREF              14 (int)
    # 126 PRECALL                  2
    # 130 CALL                     2
    # 140 POP_JUMP_FORWARD_IF_FALSE    15 (to 172)
    # 425         142 PUSH_NULL
    # 144 LOAD_DEREF               7 (_intstr)
    # 146 LOAD_FAST                0 (o)
    # 148 PRECALL                  1
    # 152 CALL                     1
    # 162 YIELD_VALUE
    # 164 RESUME                   1
    # 166 POP_TOP
    # 168 LOAD_CONST               0 (None)
    # 170 RETURN_VALUE
    # 426     >>  172 PUSH_NULL
    # 174 LOAD_DEREF              15 (isinstance)
    # 176 LOAD_FAST                0 (o)
    # 178 LOAD_DEREF              12 (float)
    # 180 PRECALL                  2
    # 184 CALL                     2
    # 194 POP_JUMP_FORWARD_IF_FALSE    15 (to 226)
    # 428         196 PUSH_NULL
    # 198 LOAD_DEREF               6 (_floatstr)
    # 200 LOAD_FAST                0 (o)
    # 202 PRECALL                  1
    # 206 CALL                     1
    # 216 YIELD_VALUE
    # 218 RESUME                   1
    # 220 POP_TOP
    # 222 LOAD_CONST               0 (None)
    # 224 RETURN_VALUE
    # 429     >>  226 PUSH_NULL
    # 228 LOAD_DEREF              15 (isinstance)
    # 230 LOAD_FAST                0 (o)
    # 232 LOAD_DEREF              16 (list)
    # 234 LOAD_DEREF              19 (tuple)
    # 236 BUILD_TUPLE              2
    # 238 PRECALL                  2
    # 242 CALL                     2
    # 252 POP_JUMP_FORWARD_IF_FALSE    20 (to 294)
    # 430         254 PUSH_NULL
    # 256 LOAD_DEREF              10 (_iterencode_list)
    # 258 LOAD_FAST                0 (o)
    # 260 LOAD_FAST                1 (_current_indent_level)
    # 262 PRECALL                  2
    # 266 CALL                     2
    # 276 GET_YIELD_FROM_ITER
    # 278 LOAD_CONST               0 (None)
    # >>  280 SEND                     3 (to 288)
    # 282 YIELD_VALUE
    # 284 RESUME                   2
    # 286 JUMP_BACKWARD_NO_INTERRUPT     4 (to 280)
    # >>  288 POP_TOP
    # 290 LOAD_CONST               0 (None)
    # 292 RETURN_VALUE
    # 431     >>  294 PUSH_NULL
    # 296 LOAD_DEREF              15 (isinstance)
    # 298 LOAD_FAST                0 (o)
    # 300 LOAD_DEREF              11 (dict)
    # 302 PRECALL                  2
    # 306 CALL                     2
    # 316 POP_JUMP_FORWARD_IF_FALSE    20 (to 358)
    # 432         318 PUSH_NULL
    # 320 LOAD_DEREF               9 (_iterencode_dict)
    # 322 LOAD_FAST                0 (o)
    # 324 LOAD_FAST                1 (_current_indent_level)
    # 326 PRECALL                  2
    # 330 CALL                     2
    # 340 GET_YIELD_FROM_ITER
    # 342 LOAD_CONST               0 (None)
    # >>  344 SEND                     3 (to 352)
    # 346 YIELD_VALUE
    # 348 RESUME                   2
    # 350 JUMP_BACKWARD_NO_INTERRUPT     4 (to 344)
    # >>  352 POP_TOP
    # 354 LOAD_CONST               0 (None)
    # 356 RETURN_VALUE
    # 434     >>  358 LOAD_DEREF              17 (markers)
    # 360 POP_JUMP_FORWARD_IF_NONE    31 (to 424)
    # 435         362 PUSH_NULL
    # 364 LOAD_DEREF              13 (id)
    # 366 LOAD_FAST                0 (o)
    # 368 PRECALL                  1
    # 372 CALL                     1
    # 382 STORE_FAST               2 (markerid)
    # 436         384 LOAD_FAST                2 (markerid)
    # 386 LOAD_DEREF              17 (markers)
    # 388 CONTAINS_OP              0
    # 390 POP_JUMP_FORWARD_IF_FALSE    11 (to 414)
    # 437         392 PUSH_NULL
    # 394 LOAD_DEREF               3 (ValueError)
    # 396 LOAD_CONST               6 ('Circular reference detected')
    # 398 PRECALL                  1
    # 402 CALL                     1
    # 412 RAISE_VARARGS            1
    # 438     >>  414 LOAD_FAST                0 (o)
    # 416 LOAD_DEREF              17 (markers)
    # 418 LOAD_FAST                2 (markerid)
    # 420 STORE_SUBSCR
    # 439     >>  424 PUSH_NULL
    # 426 LOAD_DEREF               4 (_default)
    # 428 LOAD_FAST                0 (o)
    # 430 PRECALL                  1
    # 434 CALL                     1
    # 444 STORE_FAST               0 (o)
    # 440         446 PUSH_NULL
    # 448 LOAD_DEREF               8 (_iterencode)
    # 450 LOAD_FAST                0 (o)
    # 452 LOAD_FAST                1 (_current_indent_level)
    # 454 PRECALL                  2
    # 458 CALL                     2
    # 468 GET_YIELD_FROM_ITER
    # 470 LOAD_CONST               0 (None)
    # >>  472 SEND                     3 (to 480)
    # 474 YIELD_VALUE
    # 476 RESUME                   2
    # 478 JUMP_BACKWARD_NO_INTERRUPT     4 (to 472)
    # >>  480 POP_TOP
    # 441         482 LOAD_DEREF              17 (markers)
    # 484 POP_JUMP_FORWARD_IF_NONE     5 (to 496)
    # 442         486 LOAD_DEREF              17 (markers)
    # 488 LOAD_FAST                2 (markerid)
    # 490 DELETE_SUBSCR
    # 492 LOAD_CONST               0 (None)
    # 494 RETURN_VALUE
    # 441     >>  496 LOAD_CONST               0 (None)
    # 498 RETURN_VALUE
