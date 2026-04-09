# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: werkzeug\security.py

from __future__ import annotations
import hashlib
import hmac
import os
import posixpath
import secrets

def <genexpr>(.0):
    # 12           0 RETURN_GENERATOR
    # 2 POP_TOP
    # 4 RESUME                   0
    # 6 LOAD_FAST                0 (.0)
    # >>    8 FOR_ITER                14 (to 38)
    # 13          10 STORE_FAST               1 (sep)
    # 12 LOAD_FAST                1 (sep)
    # 14 POP_JUMP_BACKWARD_IF_NONE     4 (to 8)
    # 16 LOAD_FAST                1 (sep)
    # 18 LOAD_CONST               1 ('/')
    # 20 COMPARE_OP               3 (!=)
    # 26 POP_JUMP_BACKWARD_IF_FALSE    10 (to 8)
    # 28 LOAD_FAST                1 (sep)
    # 30 YIELD_VALUE
    # 32 RESUME                   1
    # 34 POP_TOP
    # 36 JUMP_BACKWARD           15 (to 8)
    # 12     >>   38 LOAD_CONST               0 (None)
    # 40 RETURN_VALUE

def gen_salt(length):
    """Generate a random string of SALT_CHARS with specified ``length``."""
    # 25           0 RESUME                   0
    # 27           2 LOAD_FAST                0 (length)
    # 4 LOAD_CONST               1 (0)
    # 6 COMPARE_OP               1 (<=)
    # 12 POP_JUMP_FORWARD_IF_FALSE    15 (to 44)
    # 28          14 LOAD_GLOBAL              1 (NULL + ValueError)
    # 26 LOAD_CONST               2 ('Salt length must be at least 1.')
    # 28 PRECALL                  1
    # 32 CALL                     1
    # 42 RAISE_VARARGS            1
    # 30     >>   44 LOAD_CONST               3 ('')
    # 46 LOAD_METHOD              1 (join)
    # 68 LOAD_CONST               4 (<code object <genexpr> at 0x000001EBD7DF2F30, file "werkzeug\security.py", line 30>)
    # 70 MAKE_FUNCTION            0
    # 72 LOAD_GLOBAL              5 (NULL + range)
    # 84 LOAD_FAST                0 (length)
    # 86 PRECALL                  1
    # 90 CALL                     1
    # 100 GET_ITER
    # 102 PRECALL                  0
    # 106 CALL                     0
    # 116 PRECALL                  1
    # 120 CALL                     1
    # 130 RETURN_VALUE
    # Disassembly of <code object <genexpr> at 0x000001EBD7DF2F30, file "werkzeug\security.py", line 30>:
    # 30           0 RETURN_GENERATOR
    # 2 POP_TOP
    # 4 RESUME                   0
    # 6 LOAD_FAST                0 (.0)
    # >>    8 FOR_ITER                29 (to 68)
    # 10 STORE_FAST               1 (_)
    # 12 LOAD_GLOBAL              1 (NULL + secrets)
    # 24 LOAD_ATTR                1 (choice)
    # 34 LOAD_GLOBAL              4 (SALT_CHARS)
    # 46 PRECALL                  1
    # 50 CALL                     1
    # 60 YIELD_VALUE
    # 62 RESUME                   1
    # 64 POP_TOP
    # 66 JUMP_BACKWARD           30 (to 8)
    # >>   68 LOAD_CONST               0 (None)
    # 70 RETURN_VALUE

def _hash_internal(method, salt, password):
    # 33           0 RESUME                   0
    # 34           2 LOAD_FAST                0 (method)
    # 4 LOAD_METHOD              0 (split)
    # 26 LOAD_CONST               1 (':')
    # 28 PRECALL                  1
    # 32 CALL                     1
    # 42 UNPACK_EX                1
    # 44 STORE_FAST               0 (method)
    # 46 STORE_FAST               3 (args)
    # 35          48 LOAD_FAST                1 (salt)
    # 50 LOAD_METHOD              1 (encode)
    # 72 PRECALL                  0
    # 76 CALL                     0
    # 86 STORE_FAST               4 (salt_bytes)
    # 36          88 LOAD_FAST                2 (password)
    # 90 LOAD_METHOD              1 (encode)
    # 112 PRECALL                  0
    # 116 CALL                     0
    # 126 STORE_FAST               5 (password_bytes)
    # 38         128 LOAD_FAST                0 (method)
    # 130 LOAD_CONST               2 ('scrypt')
    # 132 COMPARE_OP               2 (==)
    # 138 POP_JUMP_FORWARD_IF_FALSE   132 (to 404)
    # 39         140 LOAD_FAST                3 (args)
    # 142 POP_JUMP_FORWARD_IF_TRUE     7 (to 158)
    # 40         144 LOAD_CONST               3 (32768)
    # 146 STORE_FAST               6 (n)
    # 41         148 LOAD_CONST               4 (8)
    # 150 STORE_FAST               7 (r)
    # 42         152 LOAD_CONST               5 (1)
    # 154 STORE_FAST               8 (p)
    # 156 JUMP_FORWARD            57 (to 272)
    # 44     >>  158 NOP
    # 45         160 LOAD_GLOBAL              5 (NULL + map)
    # 172 LOAD_GLOBAL              6 (int)
    # 184 LOAD_FAST                3 (args)
    # 186 PRECALL                  2
    # 190 CALL                     2
    # 200 UNPACK_SEQUENCE          3
    # 204 STORE_FAST               6 (n)
    # 206 STORE_FAST               7 (r)
    # 208 STORE_FAST               8 (p)
    # 210 JUMP_FORWARD            30 (to 272)
    # >>  212 PUSH_EXC_INFO
    # 46         214 LOAD_GLOBAL              8 (ValueError)
    # 226 CHECK_EXC_MATCH
    # 228 POP_JUMP_FORWARD_IF_FALSE    17 (to 264)
    # 230 POP_TOP
    # 47         232 LOAD_GLOBAL              9 (NULL + ValueError)
    # 244 LOAD_CONST               6 ("'scrypt' takes 3 arguments.")
    # 246 PRECALL                  1
    # 250 CALL                     1
    # 260 LOAD_CONST               0 (None)
    # 262 RAISE_VARARGS            2
    # 46     >>  264 RERAISE                  0
    # >>  266 COPY                     3
    # 268 POP_EXCEPT
    # 270 RERAISE                  1
    # 49     >>  272 LOAD_CONST               7 (132)
    # 274 LOAD_FAST                6 (n)
    # 276 BINARY_OP                5 (*)
    # 280 LOAD_FAST                7 (r)
    # 282 BINARY_OP                5 (*)
    # 286 LOAD_FAST                8 (p)
    # 288 BINARY_OP                5 (*)
    # 292 STORE_FAST               9 (maxmem)
    # 51         294 LOAD_GLOBAL             11 (NULL + hashlib)
    # 306 LOAD_ATTR                6 (scrypt)
    # 52         316 LOAD_FAST                5 (password_bytes)
    # 318 LOAD_FAST                4 (salt_bytes)
    # 320 LOAD_FAST                6 (n)
    # 322 LOAD_FAST                7 (r)
    # 324 LOAD_FAST                8 (p)
    # 326 LOAD_FAST                9 (maxmem)
    # 51         328 KW_NAMES                 8
    # 330 PRECALL                  6
    # 334 CALL                     6
    # 53         344 LOAD_METHOD              7 (hex)
    # 366 PRECALL                  0
    # 370 CALL                     0
    # 54         380 LOAD_CONST               9 ('scrypt:')
    # 382 LOAD_FAST                6 (n)
    # 384 FORMAT_VALUE             0
    # 386 LOAD_CONST               1 (':')
    # 388 LOAD_FAST                7 (r)
    # 390 FORMAT_VALUE             0
    # 392 LOAD_CONST               1 (':')
    # 394 LOAD_FAST                8 (p)
    # 396 FORMAT_VALUE             0
    # 398 BUILD_STRING             6
    # 50         400 BUILD_TUPLE              2
    # 402 RETURN_VALUE
    # 56     >>  404 LOAD_FAST                0 (method)
    # 406 LOAD_CONST              10 ('pbkdf2')
    # 408 COMPARE_OP               2 (==)
    # 414 POP_JUMP_FORWARD_IF_FALSE   153 (to 722)
    # 57         416 LOAD_GLOBAL             17 (NULL + len)
    # 428 LOAD_FAST                3 (args)
    # 430 PRECALL                  1
    # 434 CALL                     1
    # 444 STORE_FAST              10 (len_args)
    # 59         446 LOAD_FAST               10 (len_args)
    # 448 LOAD_CONST              11 (0)
    # 450 COMPARE_OP               2 (==)
    # 456 POP_JUMP_FORWARD_IF_FALSE    10 (to 478)
    # 60         458 LOAD_CONST              12 ('sha256')
    # 460 STORE_FAST              11 (hash_name)
    # 61         462 LOAD_GLOBAL             18 (DEFAULT_PBKDF2_ITERATIONS)
    # 474 STORE_FAST              12 (iterations)
    # 476 JUMP_FORWARD            73 (to 624)
    # 62     >>  478 LOAD_FAST               10 (len_args)
    # 480 LOAD_CONST               5 (1)
    # 482 COMPARE_OP               2 (==)
    # 488 POP_JUMP_FORWARD_IF_FALSE    16 (to 522)
    # 63         490 LOAD_FAST                3 (args)
    # 492 LOAD_CONST              11 (0)
    # 494 BINARY_SUBSCR
    # 504 STORE_FAST              11 (hash_name)
    # 64         506 LOAD_GLOBAL             18 (DEFAULT_PBKDF2_ITERATIONS)
    # 518 STORE_FAST              12 (iterations)
    # 520 JUMP_FORWARD            51 (to 624)
    # 65     >>  522 LOAD_FAST               10 (len_args)
    # 524 LOAD_CONST              13 (2)
    # 526 COMPARE_OP               2 (==)
    # 532 POP_JUMP_FORWARD_IF_FALSE    30 (to 594)
    # 66         534 LOAD_FAST                3 (args)
    # 536 LOAD_CONST              11 (0)
    # 538 BINARY_SUBSCR
    # 548 STORE_FAST              11 (hash_name)
    # 67         550 LOAD_GLOBAL              7 (NULL + int)
    # 562 LOAD_FAST                3 (args)
    # 564 LOAD_CONST               5 (1)
    # 566 BINARY_SUBSCR
    # 576 PRECALL                  1
    # 580 CALL                     1
    # 590 STORE_FAST              12 (iterations)
    # 592 JUMP_FORWARD            15 (to 624)
    # 69     >>  594 LOAD_GLOBAL              9 (NULL + ValueError)
    # 606 LOAD_CONST              14 ("'pbkdf2' takes 2 arguments.")
    # 608 PRECALL                  1
    # 612 CALL                     1
    # 622 RAISE_VARARGS            1
    # 72     >>  624 LOAD_GLOBAL             11 (NULL + hashlib)
    # 636 LOAD_ATTR               10 (pbkdf2_hmac)
    # 73         646 LOAD_FAST               11 (hash_name)
    # 648 LOAD_FAST                5 (password_bytes)
    # 650 LOAD_FAST                4 (salt_bytes)
    # 652 LOAD_FAST               12 (iterations)
    # 72         654 PRECALL                  4
    # 658 CALL                     4
    # 74         668 LOAD_METHOD              7 (hex)
    # 690 PRECALL                  0
    # 694 CALL                     0
    # 75         704 LOAD_CONST              15 ('pbkdf2:')
    # 706 LOAD_FAST               11 (hash_name)
    # 708 FORMAT_VALUE             0
    # 710 LOAD_CONST               1 (':')
    # 712 LOAD_FAST               12 (iterations)
    # 714 FORMAT_VALUE             0
    # 716 BUILD_STRING             4
    # 71         718 BUILD_TUPLE              2
    # 720 RETURN_VALUE
    # 78     >>  722 LOAD_GLOBAL              9 (NULL + ValueError)
    # 734 LOAD_CONST              16 ("Invalid hash method '")
    # 736 LOAD_FAST                0 (method)
    # 738 FORMAT_VALUE             0
    # 740 LOAD_CONST              17 ("'.")
    # 742 BUILD_STRING             3
    # 744 PRECALL                  1
    # 748 CALL                     1
    # 758 RAISE_VARARGS            1
    # ExceptionTable:
    # 160 to 208 -> 212 [0]
    # 212 to 264 -> 266 [1] lasti

def generate_password_hash(password, method, salt_length):
    """Securely hash a password for storage. A password can be compared to a stored hash
    using :func:`check_password_hash`.

    The following methods are supported:

    -   ``scrypt``, the default. The parameters are ``n``, ``r``, and ``p``, the default
        is ``scrypt:32768:8:1``. See :func:`hashlib.scrypt`.
    -   ``pbkdf2``, less secure. The parameters are ``hash_method`` and ``iterations``,
        the default is ``pbkdf2:sha256:600000``. See :func:`hashlib.pbkdf2_hmac`.

    Default parameters may be updated to reflect current guidelines, and methods may be
    deprecated and removed if they are no longer considered secure. To migrate old
    hashes, you may generate a new hash when checking an old hash, or you may contact
    users with a link to reset their password.

    :param password: The plaintext password.
    :param method: The key derivation function and parameters.
    :param salt_length: The number of characters to generate for the salt.

    .. versionchanged:: 3.1
        The default iterations for pbkdf2 was increased to 1,000,000.

    .. versionchanged:: 2.3
        Scrypt support was added.

    .. versionchanged:: 2.3
        The default iterations for pbkdf2 was increased to 600,000.

    .. versionchanged:: 2.3
        All plain hashes are deprecated and will not be supported in Werkzeug 3.0.
    """
    # 81           0 RESUME                   0
    # 115           2 LOAD_GLOBAL              1 (NULL + gen_salt)
    # 14 LOAD_FAST                2 (salt_length)
    # 16 PRECALL                  1
    # 20 CALL                     1
    # 30 STORE_FAST               3 (salt)
    # 116          32 LOAD_GLOBAL              3 (NULL + _hash_internal)
    # 44 LOAD_FAST                1 (method)
    # 46 LOAD_FAST                3 (salt)
    # 48 LOAD_FAST                0 (password)
    # 50 PRECALL                  3
    # 54 CALL                     3
    # 64 UNPACK_SEQUENCE          2
    # 68 STORE_FAST               4 (h)
    # 70 STORE_FAST               5 (actual_method)
    # 117          72 LOAD_FAST                5 (actual_method)
    # 74 FORMAT_VALUE             0
    # 76 LOAD_CONST               1 ('$')
    # 78 LOAD_FAST                3 (salt)
    # 80 FORMAT_VALUE             0
    # 82 LOAD_CONST               1 ('$')
    # 84 LOAD_FAST                4 (h)
    # 86 FORMAT_VALUE             0
    # 88 BUILD_STRING             5
    # 90 RETURN_VALUE

def check_password_hash(pwhash, password):
    """Securely check that the given stored password hash, previously generated using
    :func:`generate_password_hash`, matches the given password.

    Methods may be deprecated and removed if they are no longer considered secure. To
    migrate old hashes, you may generate a new hash when checking an old hash, or you
    may contact users with a link to reset their password.

    :param pwhash: The hashed password.
    :param password: The plaintext password.

    .. versionchanged:: 2.3
        All plain hashes are deprecated and will not be supported in Werkzeug 3.0.
    """
    # 120           0 RESUME                   0
    # 134           2 NOP
    # 135           4 LOAD_FAST                0 (pwhash)
    # 6 LOAD_METHOD              0 (split)
    # 28 LOAD_CONST               1 ('$')
    # 30 LOAD_CONST               2 (2)
    # 32 PRECALL                  2
    # 36 CALL                     2
    # 46 UNPACK_SEQUENCE          3
    # 50 STORE_FAST               2 (method)
    # 52 STORE_FAST               3 (salt)
    # 54 STORE_FAST               4 (hashval)
    # 56 JUMP_FORWARD            17 (to 92)
    # >>   58 PUSH_EXC_INFO
    # 136          60 LOAD_GLOBAL              2 (ValueError)
    # 72 CHECK_EXC_MATCH
    # 74 POP_JUMP_FORWARD_IF_FALSE     4 (to 84)
    # 76 POP_TOP
    # 137          78 POP_EXCEPT
    # 80 LOAD_CONST               3 (False)
    # 82 RETURN_VALUE
    # 136     >>   84 RERAISE                  0
    # >>   86 COPY                     3
    # 88 POP_EXCEPT
    # 90 RERAISE                  1
    # 139     >>   92 LOAD_GLOBAL              5 (NULL + hmac)
    # 104 LOAD_ATTR                3 (compare_digest)
    # 114 LOAD_GLOBAL              9 (NULL + _hash_internal)
    # 126 LOAD_FAST                2 (method)
    # 128 LOAD_FAST                3 (salt)
    # 130 LOAD_FAST                1 (password)
    # 132 PRECALL                  3
    # 136 CALL                     3
    # 146 LOAD_CONST               4 (0)
    # 148 BINARY_SUBSCR
    # 158 LOAD_FAST                4 (hashval)
    # 160 PRECALL                  2
    # 164 CALL                     2
    # 174 RETURN_VALUE
    # ExceptionTable:
    # 4 to 54 -> 58 [0]
    # 58 to 76 -> 86 [1] lasti
    # 84 to 84 -> 86 [1] lasti

def safe_join(directory):
    """Safely join zero or more untrusted path components to a base
    directory to avoid escaping the base directory.

    :param directory: The trusted base directory.
    :param pathnames: The untrusted path components relative to the
        base directory.
    :return: A safe path, otherwise ``None``.

    .. versionchanged:: 3.1.4
        Special device names are disallowed on Windows.
    """
    # 0 MAKE_CELL                3 (filename)
    # 142           2 RESUME                   0
    # 154           4 LOAD_FAST                0 (directory)
    # 6 POP_JUMP_FORWARD_IF_TRUE     2 (to 12)
    # 157           8 LOAD_CONST               1 ('.')
    # 10 STORE_FAST               0 (directory)
    # 159     >>   12 LOAD_FAST                0 (directory)
    # 14 BUILD_LIST               1
    # 16 STORE_FAST               2 (parts)
    # 161          18 LOAD_FAST                1 (pathnames)
    # 20 GET_ITER
    # >>   22 FOR_ITER               241 (to 506)
    # 24 STORE_DEREF              3 (filename)
    # 162          26 LOAD_DEREF               3 (filename)
    # 28 LOAD_CONST               2 ('')
    # 30 COMPARE_OP               3 (!=)
    # 36 POP_JUMP_FORWARD_IF_FALSE    20 (to 78)
    # 163          38 LOAD_GLOBAL              1 (NULL + posixpath)
    # 50 LOAD_ATTR                1 (normpath)
    # 60 LOAD_DEREF               3 (filename)
    # 62 PRECALL                  1
    # 66 CALL                     1
    # 76 STORE_DEREF              3 (filename)
    # 166     >>   78 LOAD_GLOBAL              5 (NULL + any)
    # 90 LOAD_CLOSURE             3 (filename)
    # 92 BUILD_TUPLE              1
    # 94 LOAD_CONST               3 (<code object <genexpr> at 0x000001EBD7F391B0, file "werkzeug\security.py", line 166>)
    # 96 MAKE_FUNCTION            8 (closure)
    # 98 LOAD_GLOBAL              6 (_os_alt_seps)
    # 110 GET_ITER
    # 112 PRECALL                  0
    # 116 CALL                     0
    # 126 PRECALL                  1
    # 130 CALL                     1
    # 165         140 POP_JUMP_FORWARD_IF_TRUE   157 (to 456)
    # 168         142 LOAD_GLOBAL              8 (os)
    # 154 LOAD_ATTR                5 (name)
    # 164 LOAD_CONST               4 ('nt')
    # 166 COMPARE_OP               2 (==)
    # 172 POP_JUMP_FORWARD_IF_FALSE    62 (to 298)
    # 169         174 LOAD_GLOBAL              8 (os)
    # 186 LOAD_ATTR                6 (path)
    # 196 LOAD_METHOD              7 (splitext)
    # 218 LOAD_DEREF               3 (filename)
    # 220 PRECALL                  1
    # 224 CALL                     1
    # 234 LOAD_CONST               5 (0)
    # 236 BINARY_SUBSCR
    # 246 LOAD_METHOD              8 (upper)
    # 268 PRECALL                  0
    # 272 CALL                     0
    # 282 LOAD_GLOBAL             18 (_windows_device_files)
    # 294 CONTAINS_OP              0
    # 296 POP_JUMP_FORWARD_IF_TRUE    79 (to 456)
    # 171     >>  298 LOAD_GLOBAL              8 (os)
    # 310 LOAD_ATTR                6 (path)
    # 320 LOAD_METHOD             10 (isabs)
    # 342 LOAD_DEREF               3 (filename)
    # 344 PRECALL                  1
    # 348 CALL                     1
    # 169         358 POP_JUMP_FORWARD_IF_TRUE    48 (to 456)
    # 173         360 LOAD_DEREF               3 (filename)
    # 362 LOAD_METHOD             11 (startswith)
    # 384 LOAD_CONST               6 ('/')
    # 386 PRECALL                  1
    # 390 CALL                     1
    # 169         400 POP_JUMP_FORWARD_IF_TRUE    27 (to 456)
    # 174         402 LOAD_DEREF               3 (filename)
    # 404 LOAD_CONST               7 ('..')
    # 406 COMPARE_OP               2 (==)
    # 412 POP_JUMP_FORWARD_IF_TRUE    21 (to 456)
    # 175         414 LOAD_DEREF               3 (filename)
    # 416 LOAD_METHOD             11 (startswith)
    # 438 LOAD_CONST               8 ('../')
    # 440 PRECALL                  1
    # 444 CALL                     1
    # 174         454 POP_JUMP_FORWARD_IF_FALSE     3 (to 462)
    # 177     >>  456 POP_TOP
    # 458 LOAD_CONST               9 (None)
    # 460 RETURN_VALUE
    # 179     >>  462 LOAD_FAST                2 (parts)
    # 464 LOAD_METHOD             12 (append)
    # 486 LOAD_DEREF               3 (filename)
    # 488 PRECALL                  1
    # 492 CALL                     1
    # 502 POP_TOP
    # 504 JUMP_BACKWARD          242 (to 22)
    # 181     >>  506 LOAD_GLOBAL              1 (NULL + posixpath)
    # 518 LOAD_ATTR               13 (join)
    # 528 LOAD_FAST                2 (parts)
    # 530 CALL_FUNCTION_EX         0
    # 532 RETURN_VALUE
    # Disassembly of <code object <genexpr> at 0x000001EBD7F391B0, file "werkzeug\security.py", line 166>:
    # 0 COPY_FREE_VARS           1
    # 166           2 RETURN_GENERATOR
    # 4 POP_TOP
    # 6 RESUME                   0
    # 8 LOAD_FAST                0 (.0)
    # >>   10 FOR_ITER                 8 (to 28)
    # 12 STORE_FAST               1 (sep)
    # 14 LOAD_FAST                1 (sep)
    # 16 LOAD_DEREF               2 (filename)
    # 18 CONTAINS_OP              0
    # 20 YIELD_VALUE
    # 22 RESUME                   1
    # 24 POP_TOP
    # 26 JUMP_BACKWARD            9 (to 10)
    # >>   28 LOAD_CONST               0 (None)
    # 30 RETURN_VALUE
