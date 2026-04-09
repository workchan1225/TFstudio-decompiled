# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: httpx\_decoders.py

"""
Handlers for Content-Encoding.

See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Encoding
"""

from __future__ import annotations
import codecs
import io
import typing
import zlib
from _exceptions import DecodingError
import brotli
import brotlicffi
import zstandard

class ContentDecoder:
    """ContentDecoder"""
    def decode(self, data):
        # 37           0 RESUME                   0
        # 38           2 LOAD_GLOBAL              1 (NULL + NotImplementedError)
        # 14 PRECALL                  0
        # 18 CALL                     0
        # 28 RAISE_VARARGS            1

    def flush(self):
        # 40           0 RESUME                   0
        # 41           2 LOAD_GLOBAL              1 (NULL + NotImplementedError)
        # 14 PRECALL                  0
        # 18 CALL                     0
        # 28 RAISE_VARARGS            1


class IdentityDecoder:
    """IdentityDecoder"""
    def decode(self, data):
        # 49           0 RESUME                   0
        # 50           2 LOAD_FAST                1 (data)
        # 4 RETURN_VALUE

    def flush(self):
        # 52           0 RESUME                   0
        # 53           2 LOAD_CONST               1 (b'')
        # 4 RETURN_VALUE


class DeflateDecoder:
    """DeflateDecoder"""
    def __init__(self):
        # 63           0 RESUME                   0
        # 64           2 LOAD_CONST               1 (True)
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (first_attempt)
        # 65          16 LOAD_GLOBAL              3 (NULL + zlib)
        # 28 LOAD_ATTR                2 (decompressobj)
        # 38 PRECALL                  0
        # 42 CALL                     0
        # 52 LOAD_FAST                0 (self)
        # 54 STORE_ATTR               3 (decompressor)
        # 64 LOAD_CONST               0 (None)
        # 66 RETURN_VALUE

    def decode(self, data):
        # 67           0 RESUME                   0
        # 68           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (first_attempt)
        # 14 STORE_FAST               2 (was_first_attempt)
        # 69          16 LOAD_CONST               1 (False)
        # 18 LOAD_FAST                0 (self)
        # 20 STORE_ATTR               0 (first_attempt)
        # 70          30 NOP
        # 71          32 LOAD_FAST                0 (self)
        # 34 LOAD_ATTR                1 (decompressor)
        # 44 LOAD_METHOD              2 (decompress)
        # 66 LOAD_FAST                1 (data)
        # 68 PRECALL                  1
        # 72 CALL                     1
        # 82 RETURN_VALUE
        # >>   84 PUSH_EXC_INFO
        # 72          86 LOAD_GLOBAL              6 (zlib)
        # 98 LOAD_ATTR                4 (error)
        # 108 CHECK_EXC_MATCH
        # 110 POP_JUMP_FORWARD_IF_FALSE    98 (to 308)
        # 112 STORE_FAST               3 (exc)
        # 73         114 LOAD_FAST                2 (was_first_attempt)
        # 116 POP_JUMP_FORWARD_IF_FALSE    62 (to 242)
        # 74         118 LOAD_GLOBAL              7 (NULL + zlib)
        # 130 LOAD_ATTR                5 (decompressobj)
        # 140 LOAD_GLOBAL              6 (zlib)
        # 152 LOAD_ATTR                6 (MAX_WBITS)
        # 162 UNARY_NEGATIVE
        # 164 PRECALL                  1
        # 168 CALL                     1
        # 178 LOAD_FAST                0 (self)
        # 180 STORE_ATTR               1 (decompressor)
        # 75         190 LOAD_FAST                0 (self)
        # 192 LOAD_METHOD              7 (decode)
        # 214 LOAD_FAST                1 (data)
        # 216 PRECALL                  1
        # 220 CALL                     1
        # 230 SWAP                     2
        # 232 POP_EXCEPT
        # 234 LOAD_CONST               0 (None)
        # 236 STORE_FAST               3 (exc)
        # 238 DELETE_FAST              3 (exc)
        # 240 RETURN_VALUE
        # 76     >>  242 LOAD_GLOBAL             17 (NULL + DecodingError)
        # 254 LOAD_GLOBAL             19 (NULL + str)
        # 266 LOAD_FAST                3 (exc)
        # 268 PRECALL                  1
        # 272 CALL                     1
        # 282 PRECALL                  1
        # 286 CALL                     1
        # 296 LOAD_FAST                3 (exc)
        # 298 RAISE_VARARGS            2
        # >>  300 LOAD_CONST               0 (None)
        # 302 STORE_FAST               3 (exc)
        # 304 DELETE_FAST              3 (exc)
        # 306 RERAISE                  1
        # 72     >>  308 RERAISE                  0
        # >>  310 COPY                     3
        # 312 POP_EXCEPT
        # 314 RERAISE                  1
        # ExceptionTable:
        # 32 to 80 -> 84 [0]
        # 84 to 112 -> 310 [1] lasti
        # 114 to 228 -> 300 [1] lasti
        # 230 to 230 -> 310 [1] lasti
        # 242 to 298 -> 300 [1] lasti
        # 300 to 308 -> 310 [1] lasti

    def flush(self):
        # 78           0 RESUME                   0
        # 79           2 NOP
        # 80           4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (decompressor)
        # 16 LOAD_METHOD              1 (flush)
        # 38 PRECALL                  0
        # 42 CALL                     0
        # 52 RETURN_VALUE
        # >>   54 PUSH_EXC_INFO
        # 81          56 LOAD_GLOBAL              4 (zlib)
        # 68 LOAD_ATTR                3 (error)
        # 78 CHECK_EXC_MATCH
        # 80 POP_JUMP_FORWARD_IF_FALSE    34 (to 150)
        # 82 STORE_FAST               1 (exc)
        # 82          84 LOAD_GLOBAL              9 (NULL + DecodingError)
        # 96 LOAD_GLOBAL             11 (NULL + str)
        # 108 LOAD_FAST                1 (exc)
        # 110 PRECALL                  1
        # 114 CALL                     1
        # 124 PRECALL                  1
        # 128 CALL                     1
        # 138 LOAD_FAST                1 (exc)
        # 140 RAISE_VARARGS            2
        # >>  142 LOAD_CONST               0 (None)
        # 144 STORE_FAST               1 (exc)
        # 146 DELETE_FAST              1 (exc)
        # 148 RERAISE                  1
        # 81     >>  150 RERAISE                  0
        # >>  152 COPY                     3
        # 154 POP_EXCEPT
        # 156 RERAISE                  1
        # ExceptionTable:
        # 4 to 50 -> 54 [0]
        # 54 to 82 -> 152 [1] lasti
        # 84 to 140 -> 142 [1] lasti
        # 142 to 150 -> 152 [1] lasti


class GZipDecoder:
    """GZipDecoder"""
    def __init__(self):
        # 92           0 RESUME                   0
        # 93           2 LOAD_GLOBAL              1 (NULL + zlib)
        # 14 LOAD_ATTR                1 (decompressobj)
        # 24 LOAD_GLOBAL              0 (zlib)
        # 36 LOAD_ATTR                2 (MAX_WBITS)
        # 46 LOAD_CONST               1 (16)
        # 48 BINARY_OP                7 (|)
        # 52 PRECALL                  1
        # 56 CALL                     1
        # 66 LOAD_FAST                0 (self)
        # 68 STORE_ATTR               3 (decompressor)
        # 78 LOAD_CONST               0 (None)
        # 80 RETURN_VALUE

    def decode(self, data):
        # 95           0 RESUME                   0
        # 96           2 NOP
        # 97           4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (decompressor)
        # 16 LOAD_METHOD              1 (decompress)
        # 38 LOAD_FAST                1 (data)
        # 40 PRECALL                  1
        # 44 CALL                     1
        # 54 RETURN_VALUE
        # >>   56 PUSH_EXC_INFO
        # 98          58 LOAD_GLOBAL              4 (zlib)
        # 70 LOAD_ATTR                3 (error)
        # 80 CHECK_EXC_MATCH
        # 82 POP_JUMP_FORWARD_IF_FALSE    34 (to 152)
        # 84 STORE_FAST               2 (exc)
        # 99          86 LOAD_GLOBAL              9 (NULL + DecodingError)
        # 98 LOAD_GLOBAL             11 (NULL + str)
        # 110 LOAD_FAST                2 (exc)
        # 112 PRECALL                  1
        # 116 CALL                     1
        # 126 PRECALL                  1
        # 130 CALL                     1
        # 140 LOAD_FAST                2 (exc)
        # 142 RAISE_VARARGS            2
        # >>  144 LOAD_CONST               0 (None)
        # 146 STORE_FAST               2 (exc)
        # 148 DELETE_FAST              2 (exc)
        # 150 RERAISE                  1
        # 98     >>  152 RERAISE                  0
        # >>  154 COPY                     3
        # 156 POP_EXCEPT
        # 158 RERAISE                  1
        # ExceptionTable:
        # 4 to 52 -> 56 [0]
        # 56 to 84 -> 154 [1] lasti
        # 86 to 142 -> 144 [1] lasti
        # 144 to 152 -> 154 [1] lasti

    def flush(self):
        # 101           0 RESUME                   0
        # 102           2 NOP
        # 103           4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (decompressor)
        # 16 LOAD_METHOD              1 (flush)
        # 38 PRECALL                  0
        # 42 CALL                     0
        # 52 RETURN_VALUE
        # >>   54 PUSH_EXC_INFO
        # 104          56 LOAD_GLOBAL              4 (zlib)
        # 68 LOAD_ATTR                3 (error)
        # 78 CHECK_EXC_MATCH
        # 80 POP_JUMP_FORWARD_IF_FALSE    34 (to 150)
        # 82 STORE_FAST               1 (exc)
        # 105          84 LOAD_GLOBAL              9 (NULL + DecodingError)
        # 96 LOAD_GLOBAL             11 (NULL + str)
        # 108 LOAD_FAST                1 (exc)
        # 110 PRECALL                  1
        # 114 CALL                     1
        # 124 PRECALL                  1
        # 128 CALL                     1
        # 138 LOAD_FAST                1 (exc)
        # 140 RAISE_VARARGS            2
        # >>  142 LOAD_CONST               0 (None)
        # 144 STORE_FAST               1 (exc)
        # 146 DELETE_FAST              1 (exc)
        # 148 RERAISE                  1
        # 104     >>  150 RERAISE                  0
        # >>  152 COPY                     3
        # 154 POP_EXCEPT
        # 156 RERAISE                  1
        # ExceptionTable:
        # 4 to 50 -> 54 [0]
        # 54 to 82 -> 152 [1] lasti
        # 84 to 140 -> 142 [1] lasti
        # 142 to 150 -> 152 [1] lasti


class BrotliDecoder:
    """BrotliDecoder"""
    def __init__(self):
        # 118           0 RESUME                   0
        # 119           2 LOAD_GLOBAL              0 (brotli)
        # 14 POP_JUMP_FORWARD_IF_NOT_NONE    16 (to 48)
        # 120          16 LOAD_GLOBAL              3 (NULL + ImportError)
        # 121          28 LOAD_CONST               1 ("Using 'BrotliDecoder', but neither of the 'brotlicffi' or 'brotli' packages have been installed. Make sure to install httpx using `pip install httpx[brotli]`.")
        # 120          30 PRECALL                  1
        # 34 CALL                     1
        # 124          44 LOAD_CONST               0 (None)
        # 120          46 RAISE_VARARGS            2
        # 126     >>   48 LOAD_GLOBAL              1 (NULL + brotli)
        # 60 LOAD_ATTR                2 (Decompressor)
        # 70 PRECALL                  0
        # 74 CALL                     0
        # 84 LOAD_FAST                0 (self)
        # 86 STORE_ATTR               3 (decompressor)
        # 127          96 LOAD_CONST               2 (False)
        # 98 LOAD_FAST                0 (self)
        # 100 STORE_ATTR               4 (seen_data)
        # 128         110 LOAD_FAST                0 (self)
        # 112 POP_TOP
        # 129         114 LOAD_GLOBAL             11 (NULL + hasattr)
        # 126 LOAD_FAST                0 (self)
        # 128 LOAD_ATTR                3 (decompressor)
        # 138 LOAD_CONST               3 ('decompress')
        # 140 PRECALL                  2
        # 144 CALL                     2
        # 154 POP_JUMP_FORWARD_IF_FALSE    19 (to 194)
        # 131         156 LOAD_FAST                0 (self)
        # 158 LOAD_ATTR                3 (decompressor)
        # 168 LOAD_ATTR                6 (decompress)
        # 178 LOAD_FAST                0 (self)
        # 180 STORE_ATTR               7 (_decompress)
        # 190 LOAD_CONST               0 (None)
        # 192 RETURN_VALUE
        # 134     >>  194 LOAD_FAST                0 (self)
        # 196 LOAD_ATTR                3 (decompressor)
        # 206 LOAD_ATTR                8 (process)
        # 216 LOAD_FAST                0 (self)
        # 218 STORE_ATTR               7 (_decompress)
        # 228 LOAD_CONST               0 (None)
        # 230 RETURN_VALUE

    def decode(self, data):
        # 136           0 RESUME                   0
        # 137           2 LOAD_FAST                1 (data)
        # 4 POP_JUMP_FORWARD_IF_TRUE     2 (to 10)
        # 138           6 LOAD_CONST               1 (b'')
        # 8 RETURN_VALUE
        # 139     >>   10 LOAD_CONST               2 (True)
        # 12 LOAD_FAST                0 (self)
        # 14 STORE_ATTR               0 (seen_data)
        # 140          24 NOP
        # 141          26 LOAD_FAST                0 (self)
        # 28 LOAD_METHOD              1 (_decompress)
        # 50 LOAD_FAST                1 (data)
        # 52 PRECALL                  1
        # 56 CALL                     1
        # 66 RETURN_VALUE
        # >>   68 PUSH_EXC_INFO
        # 142          70 LOAD_GLOBAL              4 (brotli)
        # 82 LOAD_ATTR                3 (error)
        # 92 CHECK_EXC_MATCH
        # 94 POP_JUMP_FORWARD_IF_FALSE    34 (to 164)
        # 96 STORE_FAST               2 (exc)
        # 143          98 LOAD_GLOBAL              9 (NULL + DecodingError)
        # 110 LOAD_GLOBAL             11 (NULL + str)
        # 122 LOAD_FAST                2 (exc)
        # 124 PRECALL                  1
        # 128 CALL                     1
        # 138 PRECALL                  1
        # 142 CALL                     1
        # 152 LOAD_FAST                2 (exc)
        # 154 RAISE_VARARGS            2
        # >>  156 LOAD_CONST               0 (None)
        # 158 STORE_FAST               2 (exc)
        # 160 DELETE_FAST              2 (exc)
        # 162 RERAISE                  1
        # 142     >>  164 RERAISE                  0
        # >>  166 COPY                     3
        # 168 POP_EXCEPT
        # 170 RERAISE                  1
        # ExceptionTable:
        # 26 to 64 -> 68 [0]
        # 68 to 96 -> 166 [1] lasti
        # 98 to 154 -> 156 [1] lasti
        # 156 to 164 -> 166 [1] lasti

    def flush(self):
        # 145           0 RESUME                   0
        # 146           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (seen_data)
        # 14 POP_JUMP_FORWARD_IF_TRUE     2 (to 20)
        # 147          16 LOAD_CONST               1 (b'')
        # 18 RETURN_VALUE
        # 148     >>   20 NOP
        # 149          22 LOAD_GLOBAL              3 (NULL + hasattr)
        # 34 LOAD_FAST                0 (self)
        # 36 LOAD_ATTR                2 (decompressor)
        # 46 LOAD_CONST               2 ('finish')
        # 48 PRECALL                  2
        # 52 CALL                     2
        # 62 POP_JUMP_FORWARD_IF_FALSE    25 (to 114)
        # 155          64 LOAD_FAST                0 (self)
        # 66 LOAD_ATTR                2 (decompressor)
        # 76 LOAD_METHOD              3 (finish)
        # 98 PRECALL                  0
        # 102 CALL                     0
        # 112 POP_TOP
        # 156     >>  114 LOAD_CONST               1 (b'')
        # 116 RETURN_VALUE
        # >>  118 PUSH_EXC_INFO
        # 157         120 LOAD_GLOBAL              8 (brotli)
        # 132 LOAD_ATTR                5 (error)
        # 142 CHECK_EXC_MATCH
        # 144 POP_JUMP_FORWARD_IF_FALSE    34 (to 214)
        # 146 STORE_FAST               1 (exc)
        # 158         148 LOAD_GLOBAL             13 (NULL + DecodingError)
        # 160 LOAD_GLOBAL             15 (NULL + str)
        # 172 LOAD_FAST                1 (exc)
        # 174 PRECALL                  1
        # 178 CALL                     1
        # 188 PRECALL                  1
        # 192 CALL                     1
        # 202 LOAD_FAST                1 (exc)
        # 204 RAISE_VARARGS            2
        # >>  206 LOAD_CONST               0 (None)
        # 208 STORE_FAST               1 (exc)
        # 210 DELETE_FAST              1 (exc)
        # 212 RERAISE                  1
        # 157     >>  214 RERAISE                  0
        # >>  216 COPY                     3
        # 218 POP_EXCEPT
        # 220 RERAISE                  1
        # ExceptionTable:
        # 22 to 112 -> 118 [0]
        # 118 to 146 -> 216 [1] lasti
        # 148 to 204 -> 206 [1] lasti
        # 206 to 214 -> 216 [1] lasti


class ZStandardDecoder:
    """ZStandardDecoder"""
    def __init__(self):
        # 170           0 RESUME                   0
        # 171           2 LOAD_GLOBAL              0 (zstandard)
        # 14 POP_JUMP_FORWARD_IF_NOT_NONE    16 (to 48)
        # 172          16 LOAD_GLOBAL              3 (NULL + ImportError)
        # 173          28 LOAD_CONST               1 ("Using 'ZStandardDecoder', ...Make sure to install httpx using `pip install httpx[zstd]`.")
        # 172          30 PRECALL                  1
        # 34 CALL                     1
        # 175          44 LOAD_CONST               0 (None)
        # 172          46 RAISE_VARARGS            2
        # 177     >>   48 LOAD_GLOBAL              1 (NULL + zstandard)
        # 60 LOAD_ATTR                2 (ZstdDecompressor)
        # 70 PRECALL                  0
        # 74 CALL                     0
        # 84 LOAD_METHOD              3 (decompressobj)
        # 106 PRECALL                  0
        # 110 CALL                     0
        # 120 LOAD_FAST                0 (self)
        # 122 STORE_ATTR               4 (decompressor)
        # 178         132 LOAD_CONST               2 (False)
        # 134 LOAD_FAST                0 (self)
        # 136 STORE_ATTR               5 (seen_data)
        # 146 LOAD_CONST               0 (None)
        # 148 RETURN_VALUE

    def decode(self, data):
        # 180           0 RESUME                   0
        # 181           2 LOAD_GLOBAL              0 (zstandard)
        # 14 POP_JUMP_FORWARD_IF_NOT_NONE     2 (to 20)
        # 16 LOAD_ASSERTION_ERROR
        # 18 RAISE_VARARGS            1
        # 182     >>   20 LOAD_CONST               1 (True)
        # 22 LOAD_FAST                0 (self)
        # 24 STORE_ATTR               1 (seen_data)
        # 183          34 LOAD_GLOBAL              5 (NULL + io)
        # 46 LOAD_ATTR                3 (BytesIO)
        # 56 PRECALL                  0
        # 60 CALL                     0
        # 70 STORE_FAST               2 (output)
        # 184          72 NOP
        # 185          74 LOAD_FAST                2 (output)
        # 76 LOAD_METHOD              4 (write)
        # 98 LOAD_FAST                0 (self)
        # 100 LOAD_ATTR                5 (decompressor)
        # 110 LOAD_METHOD              6 (decompress)
        # 132 LOAD_FAST                1 (data)
        # 134 PRECALL                  1
        # 138 CALL                     1
        # 148 PRECALL                  1
        # 152 CALL                     1
        # 162 POP_TOP
        # 186         164 LOAD_FAST                0 (self)
        # 166 LOAD_ATTR                5 (decompressor)
        # 176 LOAD_ATTR                7 (eof)
        # 186 POP_JUMP_FORWARD_IF_FALSE   135 (to 458)
        # 188 LOAD_FAST                0 (self)
        # 190 LOAD_ATTR                5 (decompressor)
        # 200 LOAD_ATTR                8 (unused_data)
        # 210 POP_JUMP_FORWARD_IF_FALSE   123 (to 458)
        # 187     >>  212 LOAD_FAST                0 (self)
        # 214 LOAD_ATTR                5 (decompressor)
        # 224 LOAD_ATTR                8 (unused_data)
        # 234 STORE_FAST               3 (unused_data)
        # 188         236 LOAD_GLOBAL              1 (NULL + zstandard)
        # 248 LOAD_ATTR                9 (ZstdDecompressor)
        # 258 PRECALL                  0
        # 262 CALL                     0
        # 272 LOAD_METHOD             10 (decompressobj)
        # 294 PRECALL                  0
        # 298 CALL                     0
        # 308 LOAD_FAST                0 (self)
        # 310 STORE_ATTR               5 (decompressor)
        # 189         320 LOAD_FAST                2 (output)
        # 322 LOAD_METHOD              4 (write)
        # 344 LOAD_FAST                0 (self)
        # 346 LOAD_ATTR                5 (decompressor)
        # 356 LOAD_METHOD              6 (decompress)
        # 378 LOAD_FAST                3 (unused_data)
        # 380 PRECALL                  1
        # 384 CALL                     1
        # 394 PRECALL                  1
        # 398 CALL                     1
        # 408 POP_TOP
        # 186         410 LOAD_FAST                0 (self)
        # 412 LOAD_ATTR                5 (decompressor)
        # 422 LOAD_ATTR                7 (eof)
        # 432 POP_JUMP_FORWARD_IF_FALSE    12 (to 458)
        # 434 LOAD_FAST                0 (self)
        # 436 LOAD_ATTR                5 (decompressor)
        # 446 LOAD_ATTR                8 (unused_data)
        # 456 POP_JUMP_BACKWARD_IF_TRUE   123 (to 212)
        # >>  458 JUMP_FORWARD            52 (to 564)
        # >>  460 PUSH_EXC_INFO
        # 190         462 LOAD_GLOBAL              0 (zstandard)
        # 474 LOAD_ATTR               11 (ZstdError)
        # 484 CHECK_EXC_MATCH
        # 486 POP_JUMP_FORWARD_IF_FALSE    34 (to 556)
        # 488 STORE_FAST               4 (exc)
        # 191         490 LOAD_GLOBAL             25 (NULL + DecodingError)
        # 502 LOAD_GLOBAL             27 (NULL + str)
        # 514 LOAD_FAST                4 (exc)
        # 516 PRECALL                  1
        # 520 CALL                     1
        # 530 PRECALL                  1
        # 534 CALL                     1
        # 544 LOAD_FAST                4 (exc)
        # 546 RAISE_VARARGS            2
        # >>  548 LOAD_CONST               0 (None)
        # 550 STORE_FAST               4 (exc)
        # 552 DELETE_FAST              4 (exc)
        # 554 RERAISE                  1
        # 190     >>  556 RERAISE                  0
        # >>  558 COPY                     3
        # 560 POP_EXCEPT
        # 562 RERAISE                  1
        # 192     >>  564 LOAD_FAST                2 (output)
        # 566 LOAD_METHOD             14 (getvalue)
        # 588 PRECALL                  0
        # 592 CALL                     0
        # 602 RETURN_VALUE
        # ExceptionTable:
        # 74 to 456 -> 460 [0]
        # 460 to 488 -> 558 [1] lasti
        # 490 to 546 -> 548 [1] lasti
        # 548 to 556 -> 558 [1] lasti

    def flush(self):
        # 194           0 RESUME                   0
        # 195           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (seen_data)
        # 14 POP_JUMP_FORWARD_IF_TRUE     2 (to 20)
        # 196          16 LOAD_CONST               1 (b'')
        # 18 RETURN_VALUE
        # 197     >>   20 LOAD_FAST                0 (self)
        # 22 LOAD_ATTR                1 (decompressor)
        # 32 LOAD_METHOD              2 (flush)
        # 54 PRECALL                  0
        # 58 CALL                     0
        # 68 STORE_FAST               1 (ret)
        # 198          70 LOAD_FAST                0 (self)
        # 72 LOAD_ATTR                1 (decompressor)
        # 82 LOAD_ATTR                3 (eof)
        # 92 POP_JUMP_FORWARD_IF_TRUE    15 (to 124)
        # 199          94 LOAD_GLOBAL              9 (NULL + DecodingError)
        # 106 LOAD_CONST               2 ('Zstandard data is incomplete')
        # 108 PRECALL                  1
        # 112 CALL                     1
        # 122 RAISE_VARARGS            1
        # 200     >>  124 LOAD_GLOBAL             11 (NULL + bytes)
        # 136 LOAD_FAST                1 (ret)
        # 138 PRECALL                  1
        # 142 CALL                     1
        # 152 RETURN_VALUE


class MultiDecoder:
    """MultiDecoder"""
    def __init__(self, children):
        """
        'children' should be a sequence of decoders in the order in which
        each was applied.
        """
        # 208           0 RESUME                   0
        # 214           2 LOAD_GLOBAL              1 (NULL + list)
        # 14 LOAD_GLOBAL              3 (NULL + reversed)
        # 26 LOAD_FAST                1 (children)
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 PRECALL                  1
        # 46 CALL                     1
        # 56 LOAD_FAST                0 (self)
        # 58 STORE_ATTR               2 (children)
        # 68 LOAD_CONST               1 (None)
        # 70 RETURN_VALUE

    def decode(self, data):
        # 216           0 RESUME                   0
        # 217           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (children)
        # 14 GET_ITER
        # >>   16 FOR_ITER                23 (to 64)
        # 18 STORE_FAST               2 (child)
        # 218          20 LOAD_FAST                2 (child)
        # 22 LOAD_METHOD              1 (decode)
        # 44 LOAD_FAST                1 (data)
        # 46 PRECALL                  1
        # 50 CALL                     1
        # 60 STORE_FAST               1 (data)
        # 62 JUMP_BACKWARD           24 (to 16)
        # 219     >>   64 LOAD_FAST                1 (data)
        # 66 RETURN_VALUE

    def flush(self):
        # 221           0 RESUME                   0
        # 222           2 LOAD_CONST               1 (b'')
        # 4 STORE_FAST               1 (data)
        # 223           6 LOAD_FAST                0 (self)
        # 8 LOAD_ATTR                0 (children)
        # 18 GET_ITER
        # >>   20 FOR_ITER                44 (to 110)
        # 22 STORE_FAST               2 (child)
        # 224          24 LOAD_FAST                2 (child)
        # 26 LOAD_METHOD              1 (decode)
        # 48 LOAD_FAST                1 (data)
        # 50 PRECALL                  1
        # 54 CALL                     1
        # 64 LOAD_FAST                2 (child)
        # 66 LOAD_METHOD              2 (flush)
        # 88 PRECALL                  0
        # 92 CALL                     0
        # 102 BINARY_OP                0 (+)
        # 106 STORE_FAST               1 (data)
        # 108 JUMP_BACKWARD           45 (to 20)
        # 225     >>  110 LOAD_FAST                1 (data)
        # 112 RETURN_VALUE


class ByteChunker:
    """ByteChunker"""
    def __init__(self, chunk_size):
        # 233           0 RESUME                   0
        # 234           2 LOAD_GLOBAL              1 (NULL + io)
        # 14 LOAD_ATTR                1 (BytesIO)
        # 24 PRECALL                  0
        # 28 CALL                     0
        # 38 LOAD_FAST                0 (self)
        # 40 STORE_ATTR               2 (_buffer)
        # 235          50 LOAD_FAST                1 (chunk_size)
        # 52 LOAD_FAST                0 (self)
        # 54 STORE_ATTR               3 (_chunk_size)
        # 64 LOAD_CONST               0 (None)
        # 66 RETURN_VALUE

    def decode(self, content):
        # 0 MAKE_CELL                0 (self)
        # 2 MAKE_CELL                3 (value)
        # 237           4 RESUME                   0
        # 238           6 LOAD_DEREF               0 (self)
        # 8 LOAD_ATTR                0 (_chunk_size)
        # 18 POP_JUMP_FORWARD_IF_NOT_NONE     7 (to 34)
        # 239          20 LOAD_FAST                1 (content)
        # 22 POP_JUMP_FORWARD_IF_FALSE     3 (to 30)
        # 24 LOAD_FAST                1 (content)
        # 26 BUILD_LIST               1
        # 28 JUMP_FORWARD             1 (to 32)
        # >>   30 BUILD_LIST               0
        # >>   32 RETURN_VALUE
        # 241     >>   34 LOAD_DEREF               0 (self)
        # 36 LOAD_ATTR                1 (_buffer)
        # 46 LOAD_METHOD              2 (write)
        # 68 LOAD_FAST                1 (content)
        # 70 PRECALL                  1
        # 74 CALL                     1
        # 84 POP_TOP
        # 242          86 LOAD_DEREF               0 (self)
        # 88 LOAD_ATTR                1 (_buffer)
        # 98 LOAD_METHOD              3 (tell)
        # 120 PRECALL                  0
        # 124 CALL                     0
        # 134 LOAD_DEREF               0 (self)
        # 136 LOAD_ATTR                0 (_chunk_size)
        # 146 COMPARE_OP               5 (>=)
        # 152 POP_JUMP_FORWARD_IF_FALSE   249 (to 652)
        # 243         154 LOAD_DEREF               0 (self)
        # 156 LOAD_ATTR                1 (_buffer)
        # 166 LOAD_METHOD              4 (getvalue)
        # 188 PRECALL                  0
        # 192 CALL                     0
        # 202 STORE_DEREF              3 (value)
        # 244         204 LOAD_CLOSURE             0 (self)
        # 206 LOAD_CLOSURE             3 (value)
        # 208 BUILD_TUPLE              2
        # 210 LOAD_CONST               1 (<code object <listcomp> at 0x000001EBD7E225B0, file "httpx\_decoders.py", line 244>)
        # 212 MAKE_FUNCTION            8 (closure)
        # 246         214 LOAD_GLOBAL             11 (NULL + range)
        # 226 LOAD_CONST               2 (0)
        # 228 LOAD_GLOBAL             13 (NULL + len)
        # 240 LOAD_DEREF               3 (value)
        # 242 PRECALL                  1
        # 246 CALL                     1
        # 256 LOAD_DEREF               0 (self)
        # 258 LOAD_ATTR                0 (_chunk_size)
        # 268 PRECALL                  3
        # 272 CALL                     3
        # 244         282 GET_ITER
        # 284 PRECALL                  0
        # 288 CALL                     0
        # 298 STORE_FAST               2 (chunks)
        # 248         300 LOAD_GLOBAL             13 (NULL + len)
        # 312 LOAD_FAST                2 (chunks)
        # 314 LOAD_CONST               3 (-1)
        # 316 BINARY_SUBSCR
        # 326 PRECALL                  1
        # 330 CALL                     1
        # 340 LOAD_DEREF               0 (self)
        # 342 LOAD_ATTR                0 (_chunk_size)
        # 352 COMPARE_OP               2 (==)
        # 358 POP_JUMP_FORWARD_IF_FALSE    53 (to 466)
        # 249         360 LOAD_DEREF               0 (self)
        # 362 LOAD_ATTR                1 (_buffer)
        # 372 LOAD_METHOD              7 (seek)
        # 394 LOAD_CONST               2 (0)
        # 396 PRECALL                  1
        # 400 CALL                     1
        # 410 POP_TOP
        # 250         412 LOAD_DEREF               0 (self)
        # 414 LOAD_ATTR                1 (_buffer)
        # 424 LOAD_METHOD              8 (truncate)
        # 446 PRECALL                  0
        # 450 CALL                     0
        # 460 POP_TOP
        # 251         462 LOAD_FAST                2 (chunks)
        # 464 RETURN_VALUE
        # 253     >>  466 LOAD_DEREF               0 (self)
        # 468 LOAD_ATTR                1 (_buffer)
        # 478 LOAD_METHOD              7 (seek)
        # 500 LOAD_CONST               2 (0)
        # 502 PRECALL                  1
        # 506 CALL                     1
        # 516 POP_TOP
        # 254         518 LOAD_DEREF               0 (self)
        # 520 LOAD_ATTR                1 (_buffer)
        # 530 LOAD_METHOD              2 (write)
        # 552 LOAD_FAST                2 (chunks)
        # 554 LOAD_CONST               3 (-1)
        # 556 BINARY_SUBSCR
        # 566 PRECALL                  1
        # 570 CALL                     1
        # 580 POP_TOP
        # 255         582 LOAD_DEREF               0 (self)
        # 584 LOAD_ATTR                1 (_buffer)
        # 594 LOAD_METHOD              8 (truncate)
        # 616 PRECALL                  0
        # 620 CALL                     0
        # 630 POP_TOP
        # 256         632 LOAD_FAST                2 (chunks)
        # 634 LOAD_CONST               0 (None)
        # 636 LOAD_CONST               3 (-1)
        # 638 BUILD_SLICE              2
        # 640 BINARY_SUBSCR
        # 650 RETURN_VALUE
        # 258     >>  652 BUILD_LIST               0
        # 654 RETURN_VALUE
        # Disassembly of <code object <listcomp> at 0x000001EBD7E225B0, file "httpx\_decoders.py", line 244>:
        # 0 COPY_FREE_VARS           2
        # 244           2 RESUME                   0
        # 4 BUILD_LIST               0
        # 6 LOAD_FAST                0 (.0)
        # >>    8 FOR_ITER                20 (to 50)
        # 246          10 STORE_FAST               1 (i)
        # 245          12 LOAD_DEREF               3 (value)
        # 14 LOAD_FAST                1 (i)
        # 16 LOAD_FAST                1 (i)
        # 18 LOAD_DEREF               2 (self)
        # 20 LOAD_ATTR                0 (_chunk_size)
        # 30 BINARY_OP                0 (+)
        # 34 BUILD_SLICE              2
        # 36 BINARY_SUBSCR
        # 244          46 LIST_APPEND              2
        # 48 JUMP_BACKWARD           21 (to 8)
        # >>   50 RETURN_VALUE

    def flush(self):
        # 260           0 RESUME                   0
        # 261           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_buffer)
        # 14 LOAD_METHOD              1 (getvalue)
        # 36 PRECALL                  0
        # 40 CALL                     0
        # 50 STORE_FAST               1 (value)
        # 262          52 LOAD_FAST                0 (self)
        # 54 LOAD_ATTR                0 (_buffer)
        # 64 LOAD_METHOD              2 (seek)
        # 86 LOAD_CONST               1 (0)
        # 88 PRECALL                  1
        # 92 CALL                     1
        # 102 POP_TOP
        # 263         104 LOAD_FAST                0 (self)
        # 106 LOAD_ATTR                0 (_buffer)
        # 116 LOAD_METHOD              3 (truncate)
        # 138 PRECALL                  0
        # 142 CALL                     0
        # 152 POP_TOP
        # 264         154 LOAD_FAST                1 (value)
        # 156 POP_JUMP_FORWARD_IF_FALSE     3 (to 164)
        # 158 LOAD_FAST                1 (value)
        # 160 BUILD_LIST               1
        # 162 JUMP_FORWARD             1 (to 166)
        # >>  164 BUILD_LIST               0
        # >>  166 RETURN_VALUE


class TextChunker:
    """TextChunker"""
    def __init__(self, chunk_size):
        # 272           0 RESUME                   0
        # 273           2 LOAD_GLOBAL              1 (NULL + io)
        # 14 LOAD_ATTR                1 (StringIO)
        # 24 PRECALL                  0
        # 28 CALL                     0
        # 38 LOAD_FAST                0 (self)
        # 40 STORE_ATTR               2 (_buffer)
        # 274          50 LOAD_FAST                1 (chunk_size)
        # 52 LOAD_FAST                0 (self)
        # 54 STORE_ATTR               3 (_chunk_size)
        # 64 LOAD_CONST               0 (None)
        # 66 RETURN_VALUE

    def decode(self, content):
        # 0 MAKE_CELL                0 (self)
        # 2 MAKE_CELL                3 (value)
        # 276           4 RESUME                   0
        # 277           6 LOAD_DEREF               0 (self)
        # 8 LOAD_ATTR                0 (_chunk_size)
        # 18 POP_JUMP_FORWARD_IF_NOT_NONE     7 (to 34)
        # 278          20 LOAD_FAST                1 (content)
        # 22 POP_JUMP_FORWARD_IF_FALSE     3 (to 30)
        # 24 LOAD_FAST                1 (content)
        # 26 BUILD_LIST               1
        # 28 JUMP_FORWARD             1 (to 32)
        # >>   30 BUILD_LIST               0
        # >>   32 RETURN_VALUE
        # 280     >>   34 LOAD_DEREF               0 (self)
        # 36 LOAD_ATTR                1 (_buffer)
        # 46 LOAD_METHOD              2 (write)
        # 68 LOAD_FAST                1 (content)
        # 70 PRECALL                  1
        # 74 CALL                     1
        # 84 POP_TOP
        # 281          86 LOAD_DEREF               0 (self)
        # 88 LOAD_ATTR                1 (_buffer)
        # 98 LOAD_METHOD              3 (tell)
        # 120 PRECALL                  0
        # 124 CALL                     0
        # 134 LOAD_DEREF               0 (self)
        # 136 LOAD_ATTR                0 (_chunk_size)
        # 146 COMPARE_OP               5 (>=)
        # 152 POP_JUMP_FORWARD_IF_FALSE   249 (to 652)
        # 282         154 LOAD_DEREF               0 (self)
        # 156 LOAD_ATTR                1 (_buffer)
        # 166 LOAD_METHOD              4 (getvalue)
        # 188 PRECALL                  0
        # 192 CALL                     0
        # 202 STORE_DEREF              3 (value)
        # 283         204 LOAD_CLOSURE             0 (self)
        # 206 LOAD_CLOSURE             3 (value)
        # 208 BUILD_TUPLE              2
        # 210 LOAD_CONST               1 (<code object <listcomp> at 0x000001EBD7E22790, file "httpx\_decoders.py", line 283>)
        # 212 MAKE_FUNCTION            8 (closure)
        # 285         214 LOAD_GLOBAL             11 (NULL + range)
        # 226 LOAD_CONST               2 (0)
        # 228 LOAD_GLOBAL             13 (NULL + len)
        # 240 LOAD_DEREF               3 (value)
        # 242 PRECALL                  1
        # 246 CALL                     1
        # 256 LOAD_DEREF               0 (self)
        # 258 LOAD_ATTR                0 (_chunk_size)
        # 268 PRECALL                  3
        # 272 CALL                     3
        # 283         282 GET_ITER
        # 284 PRECALL                  0
        # 288 CALL                     0
        # 298 STORE_FAST               2 (chunks)
        # 287         300 LOAD_GLOBAL             13 (NULL + len)
        # 312 LOAD_FAST                2 (chunks)
        # 314 LOAD_CONST               3 (-1)
        # 316 BINARY_SUBSCR
        # 326 PRECALL                  1
        # 330 CALL                     1
        # 340 LOAD_DEREF               0 (self)
        # 342 LOAD_ATTR                0 (_chunk_size)
        # 352 COMPARE_OP               2 (==)
        # 358 POP_JUMP_FORWARD_IF_FALSE    53 (to 466)
        # 288         360 LOAD_DEREF               0 (self)
        # 362 LOAD_ATTR                1 (_buffer)
        # 372 LOAD_METHOD              7 (seek)
        # 394 LOAD_CONST               2 (0)
        # 396 PRECALL                  1
        # 400 CALL                     1
        # 410 POP_TOP
        # 289         412 LOAD_DEREF               0 (self)
        # 414 LOAD_ATTR                1 (_buffer)
        # 424 LOAD_METHOD              8 (truncate)
        # 446 PRECALL                  0
        # 450 CALL                     0
        # 460 POP_TOP
        # 290         462 LOAD_FAST                2 (chunks)
        # 464 RETURN_VALUE
        # 292     >>  466 LOAD_DEREF               0 (self)
        # 468 LOAD_ATTR                1 (_buffer)
        # 478 LOAD_METHOD              7 (seek)
        # 500 LOAD_CONST               2 (0)
        # 502 PRECALL                  1
        # 506 CALL                     1
        # 516 POP_TOP
        # 293         518 LOAD_DEREF               0 (self)
        # 520 LOAD_ATTR                1 (_buffer)
        # 530 LOAD_METHOD              2 (write)
        # 552 LOAD_FAST                2 (chunks)
        # 554 LOAD_CONST               3 (-1)
        # 556 BINARY_SUBSCR
        # 566 PRECALL                  1
        # 570 CALL                     1
        # 580 POP_TOP
        # 294         582 LOAD_DEREF               0 (self)
        # 584 LOAD_ATTR                1 (_buffer)
        # 594 LOAD_METHOD              8 (truncate)
        # 616 PRECALL                  0
        # 620 CALL                     0
        # 630 POP_TOP
        # 295         632 LOAD_FAST                2 (chunks)
        # 634 LOAD_CONST               0 (None)
        # 636 LOAD_CONST               3 (-1)
        # 638 BUILD_SLICE              2
        # 640 BINARY_SUBSCR
        # 650 RETURN_VALUE
        # 297     >>  652 BUILD_LIST               0
        # 654 RETURN_VALUE
        # Disassembly of <code object <listcomp> at 0x000001EBD7E22790, file "httpx\_decoders.py", line 283>:
        # 0 COPY_FREE_VARS           2
        # 283           2 RESUME                   0
        # 4 BUILD_LIST               0
        # 6 LOAD_FAST                0 (.0)
        # >>    8 FOR_ITER                20 (to 50)
        # 285          10 STORE_FAST               1 (i)
        # 284          12 LOAD_DEREF               3 (value)
        # 14 LOAD_FAST                1 (i)
        # 16 LOAD_FAST                1 (i)
        # 18 LOAD_DEREF               2 (self)
        # 20 LOAD_ATTR                0 (_chunk_size)
        # 30 BINARY_OP                0 (+)
        # 34 BUILD_SLICE              2
        # 36 BINARY_SUBSCR
        # 283          46 LIST_APPEND              2
        # 48 JUMP_BACKWARD           21 (to 8)
        # >>   50 RETURN_VALUE

    def flush(self):
        # 299           0 RESUME                   0
        # 300           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_buffer)
        # 14 LOAD_METHOD              1 (getvalue)
        # 36 PRECALL                  0
        # 40 CALL                     0
        # 50 STORE_FAST               1 (value)
        # 301          52 LOAD_FAST                0 (self)
        # 54 LOAD_ATTR                0 (_buffer)
        # 64 LOAD_METHOD              2 (seek)
        # 86 LOAD_CONST               1 (0)
        # 88 PRECALL                  1
        # 92 CALL                     1
        # 102 POP_TOP
        # 302         104 LOAD_FAST                0 (self)
        # 106 LOAD_ATTR                0 (_buffer)
        # 116 LOAD_METHOD              3 (truncate)
        # 138 PRECALL                  0
        # 142 CALL                     0
        # 152 POP_TOP
        # 303         154 LOAD_FAST                1 (value)
        # 156 POP_JUMP_FORWARD_IF_FALSE     3 (to 164)
        # 158 LOAD_FAST                1 (value)
        # 160 BUILD_LIST               1
        # 162 JUMP_FORWARD             1 (to 166)
        # >>  164 BUILD_LIST               0
        # >>  166 RETURN_VALUE


class TextDecoder:
    """TextDecoder"""
    def __init__(self, encoding):
        # 311           0 RESUME                   0
        # 312           2 PUSH_NULL
        # 4 LOAD_GLOBAL              1 (NULL + codecs)
        # 16 LOAD_ATTR                1 (getincrementaldecoder)
        # 26 LOAD_FAST                1 (encoding)
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 LOAD_CONST               1 ('replace')
        # 44 KW_NAMES                 2
        # 46 PRECALL                  1
        # 50 CALL                     1
        # 60 LOAD_FAST                0 (self)
        # 62 STORE_ATTR               2 (decoder)
        # 72 LOAD_CONST               0 (None)
        # 74 RETURN_VALUE

    def decode(self, data):
        # 314           0 RESUME                   0
        # 315           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (decoder)
        # 14 LOAD_METHOD              1 (decode)
        # 36 LOAD_FAST                1 (data)
        # 38 PRECALL                  1
        # 42 CALL                     1
        # 52 RETURN_VALUE

    def flush(self):
        # 317           0 RESUME                   0
        # 318           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (decoder)
        # 14 LOAD_METHOD              1 (decode)
        # 36 LOAD_CONST               1 (b'')
        # 38 LOAD_CONST               2 (True)
        # 40 PRECALL                  2
        # 44 CALL                     2
        # 54 RETURN_VALUE


class LineDecoder:
    """LineDecoder"""
    def __init__(self):
        # 329           0 RESUME                   0
        # 330           2 BUILD_LIST               0
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (buffer)
        # 331          16 LOAD_CONST               1 (False)
        # 18 LOAD_FAST                0 (self)
        # 20 STORE_ATTR               1 (trailing_cr)
        # 30 LOAD_CONST               0 (None)
        # 32 RETURN_VALUE

    def decode(self, text):
        # 333           0 RESUME                   0
        # 335           2 LOAD_CONST               1 ('\n\r\x0b\x0c\x1c\x1d\x1e\x85\u2028\u2029')
        # 4 STORE_FAST               2 (NEWLINE_CHARS)
        # 338           6 LOAD_FAST                0 (self)
        # 8 LOAD_ATTR                0 (trailing_cr)
        # 18 POP_JUMP_FORWARD_IF_FALSE    12 (to 44)
        # 339          20 LOAD_CONST               2 ('\r')
        # 22 LOAD_FAST                1 (text)
        # 24 BINARY_OP                0 (+)
        # 28 STORE_FAST               1 (text)
        # 340          30 LOAD_CONST               3 (False)
        # 32 LOAD_FAST                0 (self)
        # 34 STORE_ATTR               0 (trailing_cr)
        # 341     >>   44 LOAD_FAST                1 (text)
        # 46 LOAD_METHOD              1 (endswith)
        # 68 LOAD_CONST               2 ('\r')
        # 70 PRECALL                  1
        # 74 CALL                     1
        # 84 POP_JUMP_FORWARD_IF_FALSE    17 (to 120)
        # 342          86 LOAD_CONST               4 (True)
        # 88 LOAD_FAST                0 (self)
        # 90 STORE_ATTR               0 (trailing_cr)
        # 343         100 LOAD_FAST                1 (text)
        # 102 LOAD_CONST               0 (None)
        # 104 LOAD_CONST               5 (-1)
        # 106 BUILD_SLICE              2
        # 108 BINARY_SUBSCR
        # 118 STORE_FAST               1 (text)
        # 345     >>  120 LOAD_FAST                1 (text)
        # 122 POP_JUMP_FORWARD_IF_TRUE     2 (to 128)
        # 348         124 BUILD_LIST               0
        # 126 RETURN_VALUE
        # 350     >>  128 LOAD_FAST                1 (text)
        # 130 LOAD_CONST               5 (-1)
        # 132 BINARY_SUBSCR
        # 142 LOAD_FAST                2 (NEWLINE_CHARS)
        # 144 CONTAINS_OP              0
        # 146 STORE_FAST               3 (trailing_newline)
        # 351         148 LOAD_FAST                1 (text)
        # 150 LOAD_METHOD              2 (splitlines)
        # 172 PRECALL                  0
        # 176 CALL                     0
        # 186 STORE_FAST               4 (lines)
        # 353         188 LOAD_GLOBAL              7 (NULL + len)
        # 200 LOAD_FAST                4 (lines)
        # 202 PRECALL                  1
        # 206 CALL                     1
        # 216 LOAD_CONST               6 (1)
        # 218 COMPARE_OP               2 (==)
        # 224 POP_JUMP_FORWARD_IF_FALSE    36 (to 298)
        # 226 LOAD_FAST                3 (trailing_newline)
        # 228 POP_JUMP_FORWARD_IF_TRUE    34 (to 298)
        # 355         230 LOAD_FAST                0 (self)
        # 232 LOAD_ATTR                4 (buffer)
        # 242 LOAD_METHOD              5 (append)
        # 264 LOAD_FAST                4 (lines)
        # 266 LOAD_CONST               7 (0)
        # 268 BINARY_SUBSCR
        # 278 PRECALL                  1
        # 282 CALL                     1
        # 292 POP_TOP
        # 356         294 BUILD_LIST               0
        # 296 RETURN_VALUE
        # 358     >>  298 LOAD_FAST                0 (self)
        # 300 LOAD_ATTR                4 (buffer)
        # 310 POP_JUMP_FORWARD_IF_FALSE    54 (to 420)
        # 361         312 LOAD_CONST               8 ('')
        # 314 LOAD_METHOD              6 (join)
        # 336 LOAD_FAST                0 (self)
        # 338 LOAD_ATTR                4 (buffer)
        # 348 PRECALL                  1
        # 352 CALL                     1
        # 362 LOAD_FAST                4 (lines)
        # 364 LOAD_CONST               7 (0)
        # 366 BINARY_SUBSCR
        # 376 BINARY_OP                0 (+)
        # 380 BUILD_LIST               1
        # 382 LOAD_FAST                4 (lines)
        # 384 LOAD_CONST               6 (1)
        # 386 LOAD_CONST               0 (None)
        # 388 BUILD_SLICE              2
        # 390 BINARY_SUBSCR
        # 400 BINARY_OP                0 (+)
        # 404 STORE_FAST               4 (lines)
        # 362         406 BUILD_LIST               0
        # 408 LOAD_FAST                0 (self)
        # 410 STORE_ATTR               4 (buffer)
        # 364     >>  420 LOAD_FAST                3 (trailing_newline)
        # 422 POP_JUMP_FORWARD_IF_TRUE    26 (to 476)
        # 367         424 LOAD_FAST                4 (lines)
        # 426 LOAD_METHOD              7 (pop)
        # 448 PRECALL                  0
        # 452 CALL                     0
        # 462 BUILD_LIST               1
        # 464 LOAD_FAST                0 (self)
        # 466 STORE_ATTR               4 (buffer)
        # 369     >>  476 LOAD_FAST                4 (lines)
        # 478 RETURN_VALUE

    def flush(self):
        # 371           0 RESUME                   0
        # 372           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (buffer)
        # 14 POP_JUMP_FORWARD_IF_TRUE     9 (to 34)
        # 16 LOAD_FAST                0 (self)
        # 18 LOAD_ATTR                1 (trailing_cr)
        # 28 POP_JUMP_FORWARD_IF_TRUE     2 (to 34)
        # 373          30 BUILD_LIST               0
        # 32 RETURN_VALUE
        # 375     >>   34 LOAD_CONST               1 ('')
        # 36 LOAD_METHOD              2 (join)
        # 58 LOAD_FAST                0 (self)
        # 60 LOAD_ATTR                0 (buffer)
        # 70 PRECALL                  1
        # 74 CALL                     1
        # 84 BUILD_LIST               1
        # 86 STORE_FAST               1 (lines)
        # 376          88 BUILD_LIST               0
        # 90 LOAD_FAST                0 (self)
        # 92 STORE_ATTR               0 (buffer)
        # 377         102 LOAD_CONST               2 (False)
        # 104 LOAD_FAST                0 (self)
        # 106 STORE_ATTR               1 (trailing_cr)
        # 378         116 LOAD_FAST                1 (lines)
        # 118 RETURN_VALUE

