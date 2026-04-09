# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: zstandard\__init__.py

"""Python interface to the Zstandard (zstd) compression library."""

from __future__ import absolute_import
import builtins
import io
import os
import platform
import sys
from collections.abc import Buffer
from typing import ByteString
import backend_c
import backend_cffi
import backend_rust

def open(filename, mode, cctx, dctx, encoding, errors, newline, closefd):
    """Create a file object with zstd (de)compression.

    The object returned from this function will be a
    :py:class:`ZstdDecompressionReader` if opened for reading in binary mode,
    a :py:class:`ZstdCompressionWriter` if opened for writing in binary mode,
    or an ``io.TextIOWrapper`` if opened for reading or writing in text mode.

    :param filename:
       ``bytes``, ``str``, or ``os.PathLike`` defining a file to open or a
       file object (with a ``read()`` or ``write()`` method).
    :param mode:
       ``str`` File open mode. Accepts any of the open modes recognized by
       ``open()``.
    :param cctx:
       ``ZstdCompressor`` to use for compression. If not specified and file
       is opened for writing, the default ``ZstdCompressor`` will be used.
    :param dctx:
       ``ZstdDecompressor`` to use for decompression. If not specified and file
       is opened for reading, the default ``ZstdDecompressor`` will be used.
    :param encoding:
        ``str`` that defines text encoding to use when file is opened in text
        mode.
    :param errors:
       ``str`` defining text encoding error handling mode.
    :param newline:
       ``str`` defining newline to use in text mode.
    :param closefd:
       ``bool`` whether to close the file when the returned object is closed.
        Only used if a file object is passed. If a filename is specified, the
        opened file is always closed when the returned object is closed.
    """
    # 97           0 RESUME                   0
    # 138           2 LOAD_FAST                1 (mode)
    # 4 LOAD_METHOD              0 (replace)
    # 26 LOAD_CONST               1 ('t')
    # 28 LOAD_CONST               2 ('')
    # 30 PRECALL                  2
    # 34 CALL                     2
    # 44 STORE_FAST               8 (normalized_mode)
    # 140          46 LOAD_FAST                8 (normalized_mode)
    # 48 LOAD_CONST               3 (('r', 'rb'))
    # 50 CONTAINS_OP              0
    # 52 POP_JUMP_FORWARD_IF_FALSE    21 (to 96)
    # 141          54 LOAD_FAST                3 (dctx)
    # 56 JUMP_IF_TRUE_OR_POP     13 (to 84)
    # 58 LOAD_GLOBAL              3 (NULL + ZstdDecompressor)
    # 70 PRECALL                  0
    # 74 CALL                     0
    # >>   84 STORE_FAST               3 (dctx)
    # 142          86 LOAD_CONST               4 ('r')
    # 88 STORE_FAST               9 (open_mode)
    # 143          90 LOAD_CONST               5 ('rb')
    # 92 STORE_FAST              10 (raw_open_mode)
    # 94 JUMP_FORWARD            85 (to 266)
    # 144     >>   96 LOAD_FAST                8 (normalized_mode)
    # 98 LOAD_CONST               6 (('w', 'wb', 'a', 'ab', 'x', 'xb'))
    # 100 CONTAINS_OP              0
    # 102 POP_JUMP_FORWARD_IF_FALSE    47 (to 198)
    # 145         104 LOAD_FAST                2 (cctx)
    # 106 JUMP_IF_TRUE_OR_POP     13 (to 134)
    # 108 LOAD_GLOBAL              5 (NULL + ZstdCompressor)
    # 120 PRECALL                  0
    # 124 CALL                     0
    # >>  134 STORE_FAST               2 (cctx)
    # 146         136 LOAD_CONST               7 ('w')
    # 138 STORE_FAST               9 (open_mode)
    # 147         140 LOAD_FAST                8 (normalized_mode)
    # 142 STORE_FAST              10 (raw_open_mode)
    # 148         144 LOAD_FAST               10 (raw_open_mode)
    # 146 LOAD_METHOD              3 (endswith)
    # 168 LOAD_CONST               8 ('b')
    # 170 PRECALL                  1
    # 174 CALL                     1
    # 184 POP_JUMP_FORWARD_IF_TRUE     5 (to 196)
    # 149         186 LOAD_FAST               10 (raw_open_mode)
    # 188 LOAD_CONST               8 ('b')
    # 190 BINARY_OP                0 (+)
    # 194 STORE_FAST              10 (raw_open_mode)
    # >>  196 JUMP_FORWARD            34 (to 266)
    # 151     >>  198 LOAD_GLOBAL              9 (NULL + ValueError)
    # 210 LOAD_CONST               9 ('Invalid mode: {!r}')
    # 212 LOAD_METHOD              5 (format)
    # 234 LOAD_FAST                1 (mode)
    # 236 PRECALL                  1
    # 240 CALL                     1
    # 250 PRECALL                  1
    # 254 CALL                     1
    # 264 RAISE_VARARGS            1
    # 153     >>  266 LOAD_GLOBAL             13 (NULL + hasattr)
    # 278 LOAD_GLOBAL             14 (os)
    # 290 LOAD_CONST              10 ('PathLike')
    # 292 PRECALL                  2
    # 296 CALL                     2
    # 306 POP_JUMP_FORWARD_IF_FALSE    26 (to 360)
    # 154         308 LOAD_GLOBAL             16 (str)
    # 320 LOAD_GLOBAL             18 (bytes)
    # 332 LOAD_GLOBAL             14 (os)
    # 344 LOAD_ATTR               10 (PathLike)
    # 354 BUILD_TUPLE              3
    # 356 STORE_FAST              11 (types)
    # 358 JUMP_FORWARD            14 (to 388)
    # 156     >>  360 LOAD_GLOBAL             16 (str)
    # 372 LOAD_GLOBAL             18 (bytes)
    # 384 BUILD_TUPLE              2
    # 386 STORE_FAST              11 (types)
    # 158     >>  388 LOAD_GLOBAL             23 (NULL + isinstance)
    # 400 LOAD_FAST                0 (filename)
    # 402 LOAD_FAST               11 (types)
    # 404 PRECALL                  2
    # 408 CALL                     2
    # 418 POP_JUMP_FORWARD_IF_FALSE    24 (to 468)
    # 159         420 LOAD_GLOBAL             25 (NULL + builtins)
    # 432 LOAD_ATTR               13 (open)
    # 442 LOAD_FAST                0 (filename)
    # 444 LOAD_FAST               10 (raw_open_mode)
    # 446 PRECALL                  2
    # 450 CALL                     2
    # 460 STORE_FAST              12 (inner_fh)
    # 160         462 LOAD_CONST              11 (True)
    # 464 STORE_FAST               7 (closefd)
    # 466 JUMP_FORWARD            65 (to 598)
    # 161     >>  468 LOAD_GLOBAL             13 (NULL + hasattr)
    # 480 LOAD_FAST                0 (filename)
    # 482 LOAD_CONST              12 ('read')
    # 484 PRECALL                  2
    # 488 CALL                     2
    # 498 POP_JUMP_FORWARD_IF_TRUE    16 (to 532)
    # 500 LOAD_GLOBAL             13 (NULL + hasattr)
    # 512 LOAD_FAST                0 (filename)
    # 514 LOAD_CONST              13 ('write')
    # 516 PRECALL                  2
    # 520 CALL                     2
    # 530 POP_JUMP_FORWARD_IF_FALSE    18 (to 568)
    # 162     >>  532 LOAD_FAST                0 (filename)
    # 534 STORE_FAST              12 (inner_fh)
    # 163         536 LOAD_GLOBAL             29 (NULL + bool)
    # 548 LOAD_FAST                7 (closefd)
    # 550 PRECALL                  1
    # 554 CALL                     1
    # 564 STORE_FAST               7 (closefd)
    # 566 JUMP_FORWARD            15 (to 598)
    # 165     >>  568 LOAD_GLOBAL             31 (NULL + TypeError)
    # 166         580 LOAD_CONST              14 ('filename must be a str, bytes, file or PathLike object')
    # 165         582 PRECALL                  1
    # 586 CALL                     1
    # 596 RAISE_VARARGS            1
    # 169     >>  598 LOAD_FAST                9 (open_mode)
    # 600 LOAD_CONST               4 ('r')
    # 602 COMPARE_OP               2 (==)
    # 608 POP_JUMP_FORWARD_IF_FALSE    24 (to 658)
    # 170         610 LOAD_FAST                3 (dctx)
    # 612 LOAD_METHOD             16 (stream_reader)
    # 634 LOAD_FAST               12 (inner_fh)
    # 636 LOAD_FAST                7 (closefd)
    # 638 KW_NAMES                15
    # 640 PRECALL                  2
    # 644 CALL                     2
    # 654 STORE_FAST              13 (fh)
    # 656 JUMP_FORWARD            45 (to 748)
    # 171     >>  658 LOAD_FAST                9 (open_mode)
    # 660 LOAD_CONST               7 ('w')
    # 662 COMPARE_OP               2 (==)
    # 668 POP_JUMP_FORWARD_IF_FALSE    24 (to 718)
    # 172         670 LOAD_FAST                2 (cctx)
    # 672 LOAD_METHOD             17 (stream_writer)
    # 694 LOAD_FAST               12 (inner_fh)
    # 696 LOAD_FAST                7 (closefd)
    # 698 KW_NAMES                15
    # 700 PRECALL                  2
    # 704 CALL                     2
    # 714 STORE_FAST              13 (fh)
    # 716 JUMP_FORWARD            15 (to 748)
    # 174     >>  718 LOAD_GLOBAL             37 (NULL + RuntimeError)
    # 730 LOAD_CONST              16 ('logic error in zstandard.open() handling open mode')
    # 732 PRECALL                  1
    # 736 CALL                     1
    # 746 RAISE_VARARGS            1
    # 176     >>  748 LOAD_CONST               8 ('b')
    # 750 LOAD_FAST                8 (normalized_mode)
    # 752 CONTAINS_OP              1
    # 754 POP_JUMP_FORWARD_IF_FALSE    24 (to 804)
    # 177         756 LOAD_GLOBAL             39 (NULL + io)
    # 768 LOAD_ATTR               20 (TextIOWrapper)
    # 178         778 LOAD_FAST               13 (fh)
    # 780 LOAD_FAST                4 (encoding)
    # 782 LOAD_FAST                5 (errors)
    # 784 LOAD_FAST                6 (newline)
    # 177         786 KW_NAMES                17
    # 788 PRECALL                  4
    # 792 CALL                     4
    # 802 RETURN_VALUE
    # 181     >>  804 LOAD_FAST               13 (fh)
    # 806 RETURN_VALUE

def compress(data, level):
    """Compress source data using the zstd compression format.

    This performs one-shot compression using basic/default compression
    settings.

    This method is provided for convenience and is equivalent to calling
    ``ZstdCompressor(level=level).compress(data)``.

    If you find yourself calling this function in a tight loop,
    performance will be greater if you construct a single ``ZstdCompressor``
    and repeatedly call ``compress()`` on it.
    """
    # 184           0 RESUME                   0
    # 197           2 LOAD_GLOBAL              1 (NULL + ZstdCompressor)
    # 14 LOAD_FAST                1 (level)
    # 16 KW_NAMES                 1
    # 18 PRECALL                  1
    # 22 CALL                     1
    # 32 STORE_FAST               2 (cctx)
    # 199          34 LOAD_FAST                2 (cctx)
    # 36 LOAD_METHOD              1 (compress)
    # 58 LOAD_FAST                0 (data)
    # 60 PRECALL                  1
    # 64 CALL                     1
    # 74 RETURN_VALUE

def decompress(data, max_output_size):
    """Decompress a zstd frame into its original data.

    This performs one-shot decompression using basic/default compression
    settings.

    This method is provided for convenience and is equivalent to calling
    ``ZstdDecompressor().decompress(data, max_output_size=max_output_size)``.

    If you find yourself calling this function in a tight loop, performance
    will be greater if you construct a single ``ZstdDecompressor`` and
    repeatedly call ``decompress()`` on it.
    """
    # 202           0 RESUME                   0
    # 215           2 LOAD_GLOBAL              1 (NULL + ZstdDecompressor)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 STORE_FAST               2 (dctx)
    # 217          30 LOAD_FAST                2 (dctx)
    # 32 LOAD_METHOD              1 (decompress)
    # 54 LOAD_FAST                0 (data)
    # 56 LOAD_FAST                1 (max_output_size)
    # 58 KW_NAMES                 1
    # 60 PRECALL                  2
    # 64 CALL                     2
    # 74 RETURN_VALUE
