# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: pydantic\_internal\_known_annotated_metadata.py

from __future__ import annotations
from collections import defaultdict
from collections.abc import Iterable
from copy import copy
from functools import lru_cache
from typing import TYPE_CHECKING
from pydantic_core import CoreSchema
from pydantic_core import core_schema
from _fields import PydanticMetadata
from _import_utils import import_cached_field_info

def as_jsonable_value(v):
    # 100           0 RESUME                   0
    # 101           2 LOAD_GLOBAL              1 (NULL + type)
    # 14 LOAD_FAST                0 (v)
    # 16 PRECALL                  1
    # 20 CALL                     1
    # 30 LOAD_GLOBAL              2 (int)
    # 42 LOAD_GLOBAL              4 (str)
    # 54 LOAD_GLOBAL              6 (float)
    # 66 LOAD_GLOBAL              8 (bytes)
    # 78 LOAD_GLOBAL             10 (bool)
    # 90 LOAD_GLOBAL              1 (NULL + type)
    # 102 LOAD_CONST               0 (None)
    # 104 PRECALL                  1
    # 108 CALL                     1
    # 118 BUILD_TUPLE              6
    # 120 CONTAINS_OP              1
    # 122 POP_JUMP_FORWARD_IF_FALSE    15 (to 154)
    # 102         124 LOAD_GLOBAL             13 (NULL + to_jsonable_python)
    # 136 LOAD_FAST                0 (v)
    # 138 PRECALL                  1
    # 142 CALL                     1
    # 152 RETURN_VALUE
    # 103     >>  154 LOAD_FAST                0 (v)
    # 156 RETURN_VALUE

def expand_grouped_metadata(annotations):
    """Expand the annotations.

    Args:
        annotations: An iterable of annotations.

    Returns:
        An iterable of expanded annotations.

    Example:
        ```python
        from annotated_types import Ge, Len

        from pydantic._internal._known_annotated_metadata import expand_grouped_metadata

        print(list(expand_grouped_metadata([Ge(4), Len(5)])))
        #> [Ge(ge=4), MinLen(min_length=5)]
        ```
    """
    # 106           0 RETURN_GENERATOR
    # 2 POP_TOP
    # 4 RESUME                   0
    # 125           6 LOAD_CONST               1 (0)
    # 8 LOAD_CONST               2 (None)
    # 10 IMPORT_NAME              0 (annotated_types)
    # 12 STORE_FAST               1 (at)
    # 127          14 LOAD_GLOBAL              3 (NULL + import_cached_field_info)
    # 26 PRECALL                  0
    # 30 CALL                     0
    # 40 STORE_FAST               2 (FieldInfo)
    # 129          42 LOAD_FAST                0 (annotations)
    # 44 GET_ITER
    # >>   46 FOR_ITER                92 (to 232)
    # 48 STORE_FAST               3 (annotation)
    # 130          50 LOAD_GLOBAL              5 (NULL + isinstance)
    # 62 LOAD_FAST                3 (annotation)
    # 64 LOAD_FAST                1 (at)
    # 66 LOAD_ATTR                3 (GroupedMetadata)
    # 76 PRECALL                  2
    # 80 CALL                     2
    # 90 POP_JUMP_FORWARD_IF_FALSE     9 (to 110)
    # 131          92 LOAD_FAST                3 (annotation)
    # 94 GET_YIELD_FROM_ITER
    # 96 LOAD_CONST               2 (None)
    # >>   98 SEND                     3 (to 106)
    # 100 YIELD_VALUE
    # 102 RESUME                   2
    # 104 JUMP_BACKWARD_NO_INTERRUPT     4 (to 98)
    # >>  106 POP_TOP
    # 108 JUMP_BACKWARD           32 (to 46)
    # 132     >>  110 LOAD_GLOBAL              5 (NULL + isinstance)
    # 122 LOAD_FAST                3 (annotation)
    # 124 LOAD_FAST                2 (FieldInfo)
    # 126 PRECALL                  2
    # 130 CALL                     2
    # 140 POP_JUMP_FORWARD_IF_FALSE    40 (to 222)
    # 133         142 LOAD_FAST                3 (annotation)
    # 144 LOAD_ATTR                4 (metadata)
    # 154 GET_YIELD_FROM_ITER
    # 156 LOAD_CONST               2 (None)
    # >>  158 SEND                     3 (to 166)
    # 160 YIELD_VALUE
    # 162 RESUME                   2
    # 164 JUMP_BACKWARD_NO_INTERRUPT     4 (to 158)
    # >>  166 POP_TOP
    # 139         168 LOAD_GLOBAL             11 (NULL + copy)
    # 180 LOAD_FAST                3 (annotation)
    # 182 PRECALL                  1
    # 186 CALL                     1
    # 196 STORE_FAST               3 (annotation)
    # 140         198 BUILD_LIST               0
    # 200 LOAD_FAST                3 (annotation)
    # 202 STORE_ATTR               4 (metadata)
    # 141         212 LOAD_FAST                3 (annotation)
    # 214 YIELD_VALUE
    # 216 RESUME                   1
    # 218 POP_TOP
    # 220 JUMP_BACKWARD           88 (to 46)
    # 143     >>  222 LOAD_FAST                3 (annotation)
    # 224 YIELD_VALUE
    # 226 RESUME                   1
    # 228 POP_TOP
    # 230 JUMP_BACKWARD           93 (to 46)
    # 129     >>  232 LOAD_CONST               2 (None)
    # 234 RETURN_VALUE

def _get_at_to_constraint_map():
    """Return a mapping of annotated types to constraints.

    Normally, we would define a mapping like this in the module scope, but we can't do that
    because we don't permit module level imports of `annotated_types`, in an attempt to speed up
    the import time of `pydantic`. We still only want to have this dictionary defined in one place,
    so we use this function to cache the result.
    """
    # 146           0 RESUME                   0
    # 155           2 LOAD_CONST               1 (0)
    # 4 LOAD_CONST               2 (None)
    # 6 IMPORT_NAME              0 (annotated_types)
    # 8 STORE_FAST               0 (at)
    # 158          10 LOAD_FAST                0 (at)
    # 12 LOAD_ATTR                1 (Gt)
    # 22 LOAD_CONST               3 ('gt')
    # 159          24 LOAD_FAST                0 (at)
    # 26 LOAD_ATTR                2 (Ge)
    # 36 LOAD_CONST               4 ('ge')
    # 160          38 LOAD_FAST                0 (at)
    # 40 LOAD_ATTR                3 (Lt)
    # 50 LOAD_CONST               5 ('lt')
    # 161          52 LOAD_FAST                0 (at)
    # 54 LOAD_ATTR                4 (Le)
    # 64 LOAD_CONST               6 ('le')
    # 162          66 LOAD_FAST                0 (at)
    # 68 LOAD_ATTR                5 (MultipleOf)
    # 78 LOAD_CONST               7 ('multiple_of')
    # 163          80 LOAD_FAST                0 (at)
    # 82 LOAD_ATTR                6 (MinLen)
    # 92 LOAD_CONST               8 ('min_length')
    # 164          94 LOAD_FAST                0 (at)
    # 96 LOAD_ATTR                7 (MaxLen)
    # 106 LOAD_CONST               9 ('max_length')
    # 157         108 BUILD_MAP                7
    # 110 RETURN_VALUE

def apply_known_metadata(annotation, schema):
    """Apply `annotation` to `schema` if it is an annotation we know about (Gt, Le, etc.).
    Otherwise return `None`.

    This does not handle all known annotations. If / when it does, it can always
    return a CoreSchema and return the unmodified schema if the annotation should be ignored.

    Assumes that GroupedMetadata has already been expanded via `expand_grouped_metadata`.

    Args:
        annotation: The annotation.
        schema: The schema.

    Returns:
        An updated schema with annotation if it is an annotation we know about, `None` otherwise.

    Raises:
        RuntimeError: If a constraint can't be applied to a specific schema type.
        ValueError: If an unknown constraint is encountered.
    """
    # 0 MAKE_CELL                0 (annotation)
    # 2 MAKE_CELL               21 (constraint)
    # 4 MAKE_CELL               22 (predicate_name)
    # 6 MAKE_CELL               23 (schema_type)
    # 168           8 RESUME                   0
    # 188          10 LOAD_CONST               1 (0)
    # 12 LOAD_CONST               2 (None)
    # 14 IMPORT_NAME              0 (annotated_types)
    # 16 STORE_FAST               2 (at)
    # 190          18 LOAD_CONST               3 (1)
    # 20 LOAD_CONST               4 (('NUMERIC_VALIDATOR_LOOKUP', 'forbid_inf_nan_check'))
    # 22 IMPORT_NAME              1 (_validators)
    # 24 IMPORT_FROM              2 (NUMERIC_VALIDATOR_LOOKUP)
    # 26 STORE_FAST               3 (NUMERIC_VALIDATOR_LOOKUP)
    # 28 IMPORT_FROM              3 (forbid_inf_nan_check)
    # 30 STORE_FAST               4 (forbid_inf_nan_check)
    # 32 POP_TOP
    # 192          34 LOAD_FAST                1 (schema)
    # 36 LOAD_METHOD              4 (copy)
    # 58 PRECALL                  0
    # 62 CALL                     0
    # 72 STORE_FAST               1 (schema)
    # 193          74 LOAD_GLOBAL             11 (NULL + collect_known_metadata)
    # 86 LOAD_DEREF               0 (annotation)
    # 88 BUILD_LIST               1
    # 90 PRECALL                  1
    # 94 CALL                     1
    # 104 UNPACK_SEQUENCE          2
    # 108 STORE_FAST               5 (schema_update)
    # 110 STORE_FAST               6 (other_metadata)
    # 194         112 LOAD_FAST                1 (schema)
    # 114 LOAD_CONST               5 ('type')
    # 116 BINARY_SUBSCR
    # 126 STORE_DEREF             23 (schema_type)
    # 196         128 BUILD_SET                0
    # 130 LOAD_CONST               6 (frozenset({'coerce_numbers_to_str', 'to_upper', 'strip_whitespace', 'pattern', 'to_lower'}))
    # 132 SET_UPDATE               1
    # 134 STORE_FAST               7 (chain_schema_constraints)
    # 203         136 BUILD_LIST               0
    # 138 STORE_FAST               8 (chain_schema_steps)
    # 205         140 LOAD_FAST                5 (schema_update)
    # 142 LOAD_METHOD              6 (items)
    # 164 PRECALL                  0
    # 168 CALL                     0
    # 178 GET_ITER
    # >>  180 EXTENDED_ARG             1
    # 182 FOR_ITER               477 (to 1138)
    # 184 UNPACK_SEQUENCE          2
    # 188 STORE_DEREF             21 (constraint)
    # 190 STORE_FAST               9 (value)
    # 206         192 LOAD_DEREF              21 (constraint)
    # 194 LOAD_GLOBAL             14 (CONSTRAINTS_TO_ALLOWED_SCHEMAS)
    # 206 CONTAINS_OP              1
    # 208 POP_JUMP_FORWARD_IF_FALSE    18 (to 246)
    # 207         210 LOAD_GLOBAL             17 (NULL + ValueError)
    # 222 LOAD_CONST               7 ('Unknown constraint ')
    # 224 LOAD_DEREF              21 (constraint)
    # 226 FORMAT_VALUE             0
    # 228 BUILD_STRING             2
    # 230 PRECALL                  1
    # 234 CALL                     1
    # 244 RAISE_VARARGS            1
    # 208     >>  246 LOAD_GLOBAL             14 (CONSTRAINTS_TO_ALLOWED_SCHEMAS)
    # 258 LOAD_DEREF              21 (constraint)
    # 260 BINARY_SUBSCR
    # 270 STORE_FAST              10 (allowed_schemas)
    # 214         272 LOAD_DEREF              23 (schema_type)
    # 274 LOAD_CONST               8 (frozenset({'function-before', 'function-wrap', 'function-after'}))
    # 276 CONTAINS_OP              0
    # 278 POP_JUMP_FORWARD_IF_FALSE    35 (to 350)
    # 280 LOAD_DEREF              21 (constraint)
    # 282 LOAD_CONST               9 ('strict')
    # 284 COMPARE_OP               2 (==)
    # 290 POP_JUMP_FORWARD_IF_FALSE    29 (to 350)
    # 215         292 LOAD_GLOBAL             19 (NULL + apply_known_metadata)
    # 304 LOAD_DEREF               0 (annotation)
    # 306 LOAD_FAST                1 (schema)
    # 308 LOAD_CONST              10 ('schema')
    # 310 BINARY_SUBSCR
    # 320 PRECALL                  2
    # 324 CALL                     2
    # 334 LOAD_FAST                1 (schema)
    # 336 LOAD_CONST              10 ('schema')
    # 338 STORE_SUBSCR
    # 216         342 LOAD_FAST                1 (schema)
    # 344 SWAP                     2
    # 346 POP_TOP
    # 348 RETURN_VALUE
    # 219     >>  350 LOAD_DEREF              23 (schema_type)
    # 352 LOAD_FAST               10 (allowed_schemas)
    # 354 CONTAINS_OP              0
    # 356 POP_JUMP_FORWARD_IF_FALSE    24 (to 406)
    # 220         358 LOAD_DEREF              21 (constraint)
    # 360 LOAD_CONST              11 ('union_mode')
    # 362 COMPARE_OP               2 (==)
    # 368 POP_JUMP_FORWARD_IF_FALSE    12 (to 394)
    # 370 LOAD_DEREF              23 (schema_type)
    # 372 LOAD_CONST              12 ('union')
    # 374 COMPARE_OP               2 (==)
    # 380 POP_JUMP_FORWARD_IF_FALSE     6 (to 394)
    # 221         382 LOAD_FAST                9 (value)
    # 384 LOAD_FAST                1 (schema)
    # 386 LOAD_CONST              13 ('mode')
    # 388 STORE_SUBSCR
    # 392 JUMP_FORWARD             5 (to 404)
    # 223     >>  394 LOAD_FAST                9 (value)
    # 396 LOAD_FAST                1 (schema)
    # 398 LOAD_DEREF              21 (constraint)
    # 400 STORE_SUBSCR
    # 224     >>  404 JUMP_BACKWARD          113 (to 180)
    # 227     >>  406 LOAD_DEREF              21 (constraint)
    # 408 LOAD_FAST                7 (chain_schema_constraints)
    # 410 CONTAINS_OP              0
    # 412 POP_JUMP_FORWARD_IF_FALSE    65 (to 544)
    # 229         414 LOAD_CONST              41 (('value', 'Any', 'handler', 'cs.ValidatorFunctionWrapHandler', 'return', 'Any'))
    # 416 LOAD_CLOSURE            21 (constraint)
    # 418 LOAD_CLOSURE            23 (schema_type)
    # 420 BUILD_TUPLE              2
    # 422 LOAD_CONST              19 (<code object _apply_constraint_with_incompatibility_info at 0x000001EBD733B030, file "pydantic\_internal\_known_annotated_metadata.py", line 229>)
    # 424 MAKE_FUNCTION           12 (annotations, closure)
    # 426 STORE_FAST              11 (_apply_constraint_with_incompatibility_info)
    # 247         428 LOAD_FAST                8 (chain_schema_steps)
    # 430 LOAD_METHOD             10 (append)
    # 248         452 LOAD_GLOBAL             23 (NULL + cs)
    # 464 LOAD_ATTR               12 (no_info_wrap_validator_function)
    # 249         474 LOAD_FAST               11 (_apply_constraint_with_incompatibility_info)
    # 476 LOAD_GLOBAL             23 (NULL + cs)
    # 488 LOAD_ATTR               13 (str_schema)
    # 498 LOAD_CONST              42 (())
    # 500 BUILD_MAP                0
    # 502 LOAD_DEREF              21 (constraint)
    # 504 LOAD_FAST                9 (value)
    # 506 BUILD_MAP                1
    # 508 DICT_MERGE               1
    # 510 CALL_FUNCTION_EX         1
    # 248         512 PRECALL                  2
    # 516 CALL                     2
    # 247         526 PRECALL                  1
    # 530 CALL                     1
    # 540 POP_TOP
    # 542 JUMP_BACKWARD          182 (to 180)
    # 252     >>  544 LOAD_DEREF              21 (constraint)
    # 546 LOAD_FAST                3 (NUMERIC_VALIDATOR_LOOKUP)
    # 548 CONTAINS_OP              0
    # 550 POP_JUMP_FORWARD_IF_FALSE   238 (to 1028)
    # 253         552 LOAD_DEREF              21 (constraint)
    # 554 LOAD_GLOBAL             28 (LENGTH_CONSTRAINTS)
    # 566 CONTAINS_OP              0
    # 568 POP_JUMP_FORWARD_IF_FALSE    90 (to 750)
    # 254         570 LOAD_FAST                1 (schema)
    # 572 STORE_FAST              12 (inner_schema)
    # 255         574 LOAD_FAST               12 (inner_schema)
    # 576 LOAD_CONST               5 ('type')
    # 578 BINARY_SUBSCR
    # 588 LOAD_CONST               8 (frozenset({'function-before', 'function-wrap', 'function-after'}))
    # 590 CONTAINS_OP              0
    # 592 POP_JUMP_FORWARD_IF_FALSE    18 (to 630)
    # 256     >>  594 LOAD_FAST               12 (inner_schema)
    # 596 LOAD_CONST              10 ('schema')
    # 598 BINARY_SUBSCR
    # 608 STORE_FAST              12 (inner_schema)
    # 255         610 LOAD_FAST               12 (inner_schema)
    # 612 LOAD_CONST               5 ('type')
    # 614 BINARY_SUBSCR
    # 624 LOAD_CONST               8 (frozenset({'function-before', 'function-wrap', 'function-after'}))
    # 626 CONTAINS_OP              0
    # 628 POP_JUMP_BACKWARD_IF_TRUE    18 (to 594)
    # 257     >>  630 LOAD_FAST               12 (inner_schema)
    # 632 LOAD_CONST               5 ('type')
    # 634 BINARY_SUBSCR
    # 644 STORE_FAST              13 (inner_schema_type)
    # 258         646 LOAD_FAST               13 (inner_schema_type)
    # 648 LOAD_CONST              20 ('list')
    # 650 COMPARE_OP               2 (==)
    # 656 POP_JUMP_FORWARD_IF_TRUE    24 (to 706)
    # 259         658 LOAD_FAST               13 (inner_schema_type)
    # 660 LOAD_CONST              21 ('json-or-python')
    # 662 COMPARE_OP               2 (==)
    # 668 POP_JUMP_FORWARD_IF_FALSE    29 (to 728)
    # 670 LOAD_FAST               12 (inner_schema)
    # 672 LOAD_CONST              22 ('json_schema')
    # 674 BINARY_SUBSCR
    # 684 LOAD_CONST               5 ('type')
    # 686 BINARY_SUBSCR
    # 696 LOAD_CONST              20 ('list')
    # 698 COMPARE_OP               2 (==)
    # 704 POP_JUMP_FORWARD_IF_FALSE    11 (to 728)
    # 261     >>  706 LOAD_DEREF              21 (constraint)
    # 708 LOAD_CONST              23 ('min_length')
    # 710 COMPARE_OP               2 (==)
    # 716 POP_JUMP_FORWARD_IF_FALSE     2 (to 722)
    # 718 LOAD_CONST              24 ('minItems')
    # 720 JUMP_FORWARD             1 (to 724)
    # >>  722 LOAD_CONST              25 ('maxItems')
    # >>  724 STORE_FAST              14 (js_constraint_key)
    # 726 JUMP_FORWARD            13 (to 754)
    # 263     >>  728 LOAD_DEREF              21 (constraint)
    # 730 LOAD_CONST              23 ('min_length')
    # 732 COMPARE_OP               2 (==)
    # 738 POP_JUMP_FORWARD_IF_FALSE     2 (to 744)
    # 740 LOAD_CONST              26 ('minLength')
    # 742 JUMP_FORWARD             1 (to 746)
    # >>  744 LOAD_CONST              27 ('maxLength')
    # >>  746 STORE_FAST              14 (js_constraint_key)
    # 748 JUMP_FORWARD             2 (to 754)
    # 265     >>  750 LOAD_DEREF              21 (constraint)
    # 752 STORE_FAST              14 (js_constraint_key)
    # 267     >>  754 LOAD_GLOBAL             23 (NULL + cs)
    # 766 LOAD_ATTR               15 (no_info_after_validator_function)
    # 268         776 LOAD_GLOBAL             33 (NULL + partial)
    # 788 LOAD_FAST                3 (NUMERIC_VALIDATOR_LOOKUP)
    # 790 LOAD_DEREF              21 (constraint)
    # 792 BINARY_SUBSCR
    # 802 BUILD_TUPLE              1
    # 804 BUILD_MAP                0
    # 806 LOAD_DEREF              21 (constraint)
    # 808 LOAD_FAST                9 (value)
    # 810 BUILD_MAP                1
    # 812 DICT_MERGE               1
    # 814 CALL_FUNCTION_EX         1
    # 816 LOAD_FAST                1 (schema)
    # 267         818 PRECALL                  2
    # 822 CALL                     2
    # 832 STORE_FAST               1 (schema)
    # 270         834 LOAD_FAST                1 (schema)
    # 836 LOAD_METHOD             17 (get)
    # 858 LOAD_CONST              28 ('metadata')
    # 860 BUILD_MAP                0
    # 862 PRECALL                  2
    # 866 CALL                     2
    # 876 STORE_FAST              15 (metadata)
    # 271         878 LOAD_FAST               15 (metadata)
    # 880 LOAD_METHOD             17 (get)
    # 902 LOAD_CONST              29 ('pydantic_js_updates')
    # 904 PRECALL                  1
    # 908 CALL                     1
    # 918 COPY                     1
    # 920 STORE_FAST              16 (existing_json_schema_updates)
    # 922 POP_JUMP_FORWARD_IF_NONE    25 (to 974)
    # 272         924 BUILD_MAP                0
    # 273         926 LOAD_FAST               16 (existing_json_schema_updates)
    # 272         928 DICT_UPDATE              1
    # 274         930 LOAD_FAST               14 (js_constraint_key)
    # 932 LOAD_GLOBAL             37 (NULL + as_jsonable_value)
    # 944 LOAD_FAST                9 (value)
    # 946 PRECALL                  1
    # 950 CALL                     1
    # 960 BUILD_MAP                1
    # 272         962 DICT_UPDATE              1
    # 964 LOAD_FAST               15 (metadata)
    # 966 LOAD_CONST              29 ('pydantic_js_updates')
    # 968 STORE_SUBSCR
    # 972 JUMP_FORWARD            20 (to 1014)
    # 277     >>  974 LOAD_FAST               14 (js_constraint_key)
    # 976 LOAD_GLOBAL             37 (NULL + as_jsonable_value)
    # 988 LOAD_FAST                9 (value)
    # 990 PRECALL                  1
    # 994 CALL                     1
    # 1004 BUILD_MAP                1
    # 1006 LOAD_FAST               15 (metadata)
    # 1008 LOAD_CONST              29 ('pydantic_js_updates')
    # 1010 STORE_SUBSCR
    # 278     >> 1014 LOAD_FAST               15 (metadata)
    # 1016 LOAD_FAST                1 (schema)
    # 1018 LOAD_CONST              28 ('metadata')
    # 1020 STORE_SUBSCR
    # 1024 EXTENDED_ARG             1
    # 1026 JUMP_BACKWARD          424 (to 180)
    # 279     >> 1028 LOAD_DEREF              21 (constraint)
    # 1030 LOAD_CONST              30 ('allow_inf_nan')
    # 1032 COMPARE_OP               2 (==)
    # 1038 POP_JUMP_FORWARD_IF_FALSE    27 (to 1094)
    # 1040 LOAD_FAST                9 (value)
    # 1042 LOAD_CONST              31 (False)
    # 1044 IS_OP                    0
    # 1046 POP_JUMP_FORWARD_IF_FALSE    23 (to 1094)
    # 280        1048 LOAD_GLOBAL             23 (NULL + cs)
    # 1060 LOAD_ATTR               15 (no_info_after_validator_function)
    # 281        1070 LOAD_FAST                4 (forbid_inf_nan_check)
    # 282        1072 LOAD_FAST                1 (schema)
    # 280        1074 PRECALL                  2
    # 1078 CALL                     2
    # 1088 STORE_FAST               1 (schema)
    # 1090 EXTENDED_ARG             1
    # 1092 JUMP_BACKWARD          457 (to 180)
    # 287     >> 1094 LOAD_GLOBAL             39 (NULL + RuntimeError)
    # 1106 LOAD_CONST              32 ("Unable to apply constraint '")
    # 1108 LOAD_DEREF              21 (constraint)
    # 1110 FORMAT_VALUE             0
    # 1112 LOAD_CONST              33 ("' to schema of type '")
    # 1114 LOAD_DEREF              23 (schema_type)
    # 1116 FORMAT_VALUE             0
    # 1118 LOAD_CONST              34 ("'")
    # 1120 BUILD_STRING             5
    # 1122 PRECALL                  1
    # 1126 CALL                     1
    # 1136 RAISE_VARARGS            1
    # 289     >> 1138 LOAD_FAST                6 (other_metadata)
    # 1140 GET_ITER
    # >> 1142 EXTENDED_ARG             1
    # 1144 FOR_ITER               263 (to 1672)
    # 1146 STORE_DEREF              0 (annotation)
    # 290        1148 LOAD_GLOBAL             41 (NULL + type)
    # 1160 LOAD_DEREF               0 (annotation)
    # 1162 PRECALL                  1
    # 1166 CALL                     1
    # 1176 COPY                     1
    # 1178 STORE_FAST              17 (annotation_type)
    # 1180 LOAD_GLOBAL             43 (NULL + _get_at_to_constraint_map)
    # 1192 PRECALL                  0
    # 1196 CALL                     0
    # 1206 COPY                     1
    # 1208 STORE_FAST              18 (at_to_constraint_map)
    # 1210 CONTAINS_OP              0
    # 1212 POP_JUMP_FORWARD_IF_FALSE   101 (to 1416)
    # 291        1214 LOAD_FAST               18 (at_to_constraint_map)
    # 1216 LOAD_FAST               17 (annotation_type)
    # 1218 BINARY_SUBSCR
    # 1228 STORE_DEREF             21 (constraint)
    # 292        1230 LOAD_FAST                3 (NUMERIC_VALIDATOR_LOOKUP)
    # 1232 LOAD_METHOD             17 (get)
    # 1254 LOAD_DEREF              21 (constraint)
    # 1256 PRECALL                  1
    # 1260 CALL                     1
    # 1270 STORE_FAST              19 (validator)
    # 293        1272 LOAD_FAST               19 (validator)
    # 1274 POP_JUMP_FORWARD_IF_NOT_NONE    18 (to 1312)
    # 294        1276 LOAD_GLOBAL             17 (NULL + ValueError)
    # 1288 LOAD_CONST               7 ('Unknown constraint ')
    # 1290 LOAD_DEREF              21 (constraint)
    # 1292 FORMAT_VALUE             0
    # 1294 BUILD_STRING             2
    # 1296 PRECALL                  1
    # 1300 CALL                     1
    # 1310 RAISE_VARARGS            1
    # 295     >> 1312 LOAD_GLOBAL             23 (NULL + cs)
    # 1324 LOAD_ATTR               15 (no_info_after_validator_function)
    # 296        1334 LOAD_GLOBAL             33 (NULL + partial)
    # 1346 LOAD_FAST               19 (validator)
    # 1348 LOAD_DEREF              21 (constraint)
    # 1350 LOAD_GLOBAL             45 (NULL + getattr)
    # 1362 LOAD_DEREF               0 (annotation)
    # 1364 LOAD_DEREF              21 (constraint)
    # 1366 PRECALL                  2
    # 1370 CALL                     2
    # 1380 BUILD_MAP                1
    # 1382 PRECALL                  2
    # 1386 CALL                     2
    # 1396 LOAD_FAST                1 (schema)
    # 295        1398 PRECALL                  2
    # 1402 CALL                     2
    # 1412 STORE_FAST               1 (schema)
    # 298        1414 JUMP_BACKWARD          137 (to 1142)
    # 299     >> 1416 LOAD_GLOBAL             47 (NULL + isinstance)
    # 1428 LOAD_DEREF               0 (annotation)
    # 1430 LOAD_FAST                2 (at)
    # 1432 LOAD_ATTR               24 (Predicate)
    # 1442 LOAD_FAST                2 (at)
    # 1444 LOAD_ATTR               25 (Not)
    # 1454 BUILD_TUPLE              2
    # 1456 PRECALL                  2
    # 1460 CALL                     2
    # 1470 POP_JUMP_FORWARD_IF_FALSE    97 (to 1666)
    # 300        1472 LOAD_GLOBAL             53 (NULL + hasattr)
    # 1484 LOAD_DEREF               0 (annotation)
    # 1486 LOAD_ATTR               27 (func)
    # 1496 LOAD_CONST              35 ('__qualname__')
    # 1498 PRECALL                  2
    # 1502 CALL                     2
    # 1512 POP_JUMP_FORWARD_IF_FALSE    15 (to 1544)
    # 1514 LOAD_DEREF               0 (annotation)
    # 1516 LOAD_ATTR               27 (func)
    # 1526 LOAD_ATTR               28 (__qualname__)
    # 1536 FORMAT_VALUE             2 (repr)
    # 1538 LOAD_CONST              36 (' ')
    # 1540 BUILD_STRING             2
    # 1542 JUMP_FORWARD             1 (to 1546)
    # >> 1544 LOAD_CONST              37 ('')
    # >> 1546 STORE_DEREF             22 (predicate_name)
    # 306        1548 LOAD_GLOBAL             47 (NULL + isinstance)
    # 1560 LOAD_DEREF               0 (annotation)
    # 1562 LOAD_FAST                2 (at)
    # 1564 LOAD_ATTR               24 (Predicate)
    # 1574 PRECALL                  2
    # 1578 CALL                     2
    # 1588 POP_JUMP_FORWARD_IF_FALSE     8 (to 1606)
    # 308        1590 LOAD_CONST              43 (('v', 'Any', 'return', 'Any'))
    # 1592 LOAD_CLOSURE             0 (annotation)
    # 1594 LOAD_CLOSURE            22 (predicate_name)
    # 1596 BUILD_TUPLE              2
    # 1598 LOAD_CONST              39 (<code object val_func at 0x000001EBD7E484B0, file "pydantic\_internal\_known_annotated_metadata.py", line 308>)
    # 1600 MAKE_FUNCTION           12 (annotations, closure)
    # 1602 STORE_FAST              20 (val_func)
    # 1604 JUMP_FORWARD             7 (to 1620)
    # 319     >> 1606 LOAD_CONST              43 (('v', 'Any', 'return', 'Any'))
    # 1608 LOAD_CLOSURE             0 (annotation)
    # 1610 LOAD_CLOSURE            22 (predicate_name)
    # 1612 BUILD_TUPLE              2
    # 1614 LOAD_CONST              40 (<code object val_func at 0x000001EBD7E48930, file "pydantic\_internal\_known_annotated_metadata.py", line 319>)
    # 1616 MAKE_FUNCTION           12 (annotations, closure)
    # 1618 STORE_FAST              20 (val_func)
    # 328     >> 1620 LOAD_GLOBAL             23 (NULL + cs)
    # 1632 LOAD_ATTR               15 (no_info_after_validator_function)
    # 1642 LOAD_FAST               20 (val_func)
    # 1644 LOAD_FAST                1 (schema)
    # 1646 PRECALL                  2
    # 1650 CALL                     2
    # 1660 STORE_FAST               1 (schema)
    # 1662 EXTENDED_ARG             1
    # 1664 JUMP_BACKWARD          262 (to 1142)
    # 331     >> 1666 POP_TOP
    # 1668 LOAD_CONST               2 (None)
    # 1670 RETURN_VALUE
    # 333     >> 1672 LOAD_FAST                8 (chain_schema_steps)
    # 1674 POP_JUMP_FORWARD_IF_FALSE    26 (to 1728)
    # 334        1676 LOAD_FAST                1 (schema)
    # 1678 BUILD_LIST               1
    # 1680 LOAD_FAST                8 (chain_schema_steps)
    # 1682 BINARY_OP                0 (+)
    # 1686 STORE_FAST               8 (chain_schema_steps)
    # 335        1688 LOAD_GLOBAL             23 (NULL + cs)
    # 1700 LOAD_ATTR               29 (chain_schema)
    # 1710 LOAD_FAST                8 (chain_schema_steps)
    # 1712 PRECALL                  1
    # 1716 CALL                     1
    # 1726 RETURN_VALUE
    # 337     >> 1728 LOAD_FAST                1 (schema)
    # 1730 RETURN_VALUE
    # Disassembly of <code object _apply_constraint_with_incompatibility_info at 0x000001EBD733B030, file "pydantic\_internal\_known_annotated_metadata.py", line 229>:
    # 0 COPY_FREE_VARS           2
    # 229           2 RESUME                   0
    # 232           4 NOP
    # 233           6 PUSH_NULL
    # 8 LOAD_FAST                1 (handler)
    # 10 LOAD_FAST                0 (value)
    # 12 PRECALL                  1
    # 16 CALL                     1
    # 26 STORE_FAST               2 (x)
    # 28 JUMP_FORWARD            79 (to 188)
    # >>   30 PUSH_EXC_INFO
    # 234          32 LOAD_GLOBAL              0 (ValidationError)
    # 44 CHECK_EXC_MATCH
    # 46 POP_JUMP_FORWARD_IF_FALSE    66 (to 180)
    # 48 STORE_FAST               3 (ve)
    # 240          50 LOAD_CONST               1 ('type')
    # 52 LOAD_FAST                3 (ve)
    # 54 LOAD_METHOD              1 (errors)
    # 76 PRECALL                  0
    # 80 CALL                     0
    # 90 LOAD_CONST               2 (0)
    # 92 BINARY_SUBSCR
    # 102 LOAD_CONST               1 ('type')
    # 104 BINARY_SUBSCR
    # 114 CONTAINS_OP              0
    # 116 POP_JUMP_FORWARD_IF_FALSE    25 (to 168)
    # 241         118 LOAD_GLOBAL              5 (NULL + TypeError)
    # 242         130 LOAD_CONST               3 ("Unable to apply constraint '")
    # 132 LOAD_DEREF               4 (constraint)
    # 134 FORMAT_VALUE             0
    # 136 LOAD_CONST               4 ("' to supplied value ")
    # 138 LOAD_FAST                0 (value)
    # 140 FORMAT_VALUE             0
    # 142 LOAD_CONST               5 (" for schema of type '")
    # 144 LOAD_DEREF               5 (schema_type)
    # 146 FORMAT_VALUE             0
    # 148 LOAD_CONST               6 ("'")
    # 150 BUILD_STRING             7
    # 241         152 PRECALL                  1
    # 156 CALL                     1
    # 166 RAISE_VARARGS            1
    # 244     >>  168 LOAD_FAST                3 (ve)
    # 170 RAISE_VARARGS            1
    # >>  172 LOAD_CONST               0 (None)
    # 174 STORE_FAST               3 (ve)
    # 176 DELETE_FAST              3 (ve)
    # 178 RERAISE                  1
    # 234     >>  180 RERAISE                  0
    # >>  182 COPY                     3
    # 184 POP_EXCEPT
    # 186 RERAISE                  1
    # 245     >>  188 LOAD_FAST                2 (x)
    # 190 RETURN_VALUE
    # ExceptionTable:
    # 6 to 26 -> 30 [0]
    # 30 to 48 -> 182 [1] lasti
    # 50 to 170 -> 172 [1] lasti
    # 172 to 180 -> 182 [1] lasti
    # Disassembly of <code object val_func at 0x000001EBD7E484B0, file "pydantic\_internal\_known_annotated_metadata.py", line 308>:
    # 0 COPY_FREE_VARS           2
    # 308           2 RESUME                   0
    # 309           4 LOAD_DEREF               2 (annotation)
    # 6 LOAD_METHOD              0 (func)
    # 28 LOAD_FAST                0 (v)
    # 30 PRECALL                  1
    # 34 CALL                     1
    # 44 STORE_FAST               1 (predicate_satisfied)
    # 310          46 LOAD_FAST                1 (predicate_satisfied)
    # 48 POP_JUMP_FORWARD_IF_TRUE    20 (to 90)
    # 311          50 LOAD_GLOBAL              3 (NULL + PydanticCustomError)
    # 312          62 LOAD_CONST               1 ('predicate_failed')
    # 313          64 LOAD_CONST               2 ('Predicate ')
    # 66 LOAD_DEREF               3 (predicate_name)
    # 68 FORMAT_VALUE             0
    # 70 LOAD_CONST               3 ('failed')
    # 72 BUILD_STRING             3
    # 311          74 PRECALL                  2
    # 78 CALL                     2
    # 88 RAISE_VARARGS            1
    # 315     >>   90 LOAD_FAST                0 (v)
    # 92 RETURN_VALUE
    # Disassembly of <code object val_func at 0x000001EBD7E48930, file "pydantic\_internal\_known_annotated_metadata.py", line 319>:
    # 0 COPY_FREE_VARS           2
    # 319           2 RESUME                   0
    # 320           4 LOAD_DEREF               2 (annotation)
    # 6 LOAD_METHOD              0 (func)
    # 28 LOAD_FAST                0 (v)
    # 30 PRECALL                  1
    # 34 CALL                     1
    # 44 STORE_FAST               1 (predicate_satisfied)
    # 321          46 LOAD_FAST                1 (predicate_satisfied)
    # 48 POP_JUMP_FORWARD_IF_FALSE    20 (to 90)
    # 322          50 LOAD_GLOBAL              3 (NULL + PydanticCustomError)
    # 323          62 LOAD_CONST               1 ('not_operation_failed')
    # 324          64 LOAD_CONST               2 ('Not of ')
    # 66 LOAD_DEREF               3 (predicate_name)
    # 68 FORMAT_VALUE             0
    # 70 LOAD_CONST               3 ('failed')
    # 72 BUILD_STRING             3
    # 322          74 PRECALL                  2
    # 78 CALL                     2
    # 88 RAISE_VARARGS            1
    # 326     >>   90 LOAD_FAST                0 (v)
    # 92 RETURN_VALUE

def collect_known_metadata(annotations):
    """Split `annotations` into known metadata and unknown annotations.

    Args:
        annotations: An iterable of annotations.

    Returns:
        A tuple contains a dict of known metadata and a list of unknown annotations.

    Example:
        ```python
        from annotated_types import Gt, Len

        from pydantic._internal._known_annotated_metadata import collect_known_metadata

        print(collect_known_metadata([Gt(1), Len(42), ...]))
        #> ({'gt': 1, 'min_length': 42}, [Ellipsis])
        ```
    """
    # 340           0 RESUME                   0
    # 359           2 LOAD_GLOBAL              1 (NULL + expand_grouped_metadata)
    # 14 LOAD_FAST                0 (annotations)
    # 16 PRECALL                  1
    # 20 CALL                     1
    # 30 STORE_FAST               0 (annotations)
    # 361          32 BUILD_MAP                0
    # 34 STORE_FAST               1 (res)
    # 362          36 BUILD_LIST               0
    # 38 STORE_FAST               2 (remaining)
    # 364          40 LOAD_FAST                0 (annotations)
    # 42 GET_ITER
    # >>   44 FOR_ITER               237 (to 520)
    # 46 STORE_FAST               3 (annotation)
    # 366          48 LOAD_GLOBAL              3 (NULL + isinstance)
    # 60 LOAD_FAST                3 (annotation)
    # 62 LOAD_GLOBAL              4 (PydanticMetadata)
    # 74 PRECALL                  2
    # 78 CALL                     2
    # 88 POP_JUMP_FORWARD_IF_FALSE    27 (to 144)
    # 367          90 LOAD_FAST                1 (res)
    # 92 LOAD_METHOD              3 (update)
    # 114 LOAD_FAST                3 (annotation)
    # 116 LOAD_ATTR                4 (__dict__)
    # 126 PRECALL                  1
    # 130 CALL                     1
    # 140 POP_TOP
    # 142 JUMP_BACKWARD           50 (to 44)
    # 369     >>  144 LOAD_GLOBAL             11 (NULL + type)
    # 156 LOAD_FAST                3 (annotation)
    # 158 PRECALL                  1
    # 162 CALL                     1
    # 172 COPY                     1
    # 174 STORE_FAST               4 (annotation_type)
    # 176 LOAD_GLOBAL             13 (NULL + _get_at_to_constraint_map)
    # 188 PRECALL                  0
    # 192 CALL                     0
    # 202 COPY                     1
    # 204 STORE_FAST               5 (at_to_constraint_map)
    # 206 CONTAINS_OP              0
    # 208 POP_JUMP_FORWARD_IF_FALSE    28 (to 266)
    # 370         210 LOAD_FAST                5 (at_to_constraint_map)
    # 212 LOAD_FAST                4 (annotation_type)
    # 214 BINARY_SUBSCR
    # 224 STORE_FAST               6 (constraint)
    # 371         226 LOAD_GLOBAL             15 (NULL + getattr)
    # 238 LOAD_FAST                3 (annotation)
    # 240 LOAD_FAST                6 (constraint)
    # 242 PRECALL                  2
    # 246 CALL                     2
    # 256 LOAD_FAST                1 (res)
    # 258 LOAD_FAST                6 (constraint)
    # 260 STORE_SUBSCR
    # 264 JUMP_BACKWARD          111 (to 44)
    # 372     >>  266 LOAD_GLOBAL              3 (NULL + isinstance)
    # 278 LOAD_FAST                3 (annotation)
    # 280 LOAD_GLOBAL             10 (type)
    # 292 PRECALL                  2
    # 296 CALL                     2
    # 306 POP_JUMP_FORWARD_IF_FALSE    84 (to 476)
    # 308 LOAD_GLOBAL             17 (NULL + issubclass)
    # 320 LOAD_FAST                3 (annotation)
    # 322 LOAD_GLOBAL              4 (PydanticMetadata)
    # 334 PRECALL                  2
    # 338 CALL                     2
    # 348 POP_JUMP_FORWARD_IF_FALSE    63 (to 476)
    # 375         350 LOAD_FAST                1 (res)
    # 352 LOAD_METHOD              3 (update)
    # 374 LOAD_CONST               1 (<code object <dictcomp> at 0x000001EBD7DF0830, file "pydantic\_internal\_known_annotated_metadata.py", line 375>)
    # 376 MAKE_FUNCTION            0
    # 378 LOAD_GLOBAL             19 (NULL + vars)
    # 390 LOAD_FAST                3 (annotation)
    # 392 PRECALL                  1
    # 396 CALL                     1
    # 406 LOAD_METHOD             10 (items)
    # 428 PRECALL                  0
    # 432 CALL                     0
    # 442 GET_ITER
    # 444 PRECALL                  0
    # 448 CALL                     0
    # 458 PRECALL                  1
    # 462 CALL                     1
    # 472 POP_TOP
    # 474 JUMP_BACKWARD          216 (to 44)
    # 377     >>  476 LOAD_FAST                2 (remaining)
    # 478 LOAD_METHOD             11 (append)
    # 500 LOAD_FAST                3 (annotation)
    # 502 PRECALL                  1
    # 506 CALL                     1
    # 516 POP_TOP
    # 518 JUMP_BACKWARD          238 (to 44)
    # 381     >>  520 LOAD_CONST               2 (<code object <dictcomp> at 0x000001EBD7E42950, file "pydantic\_internal\_known_annotated_metadata.py", line 381>)
    # 522 MAKE_FUNCTION            0
    # 524 LOAD_FAST                1 (res)
    # 526 LOAD_METHOD             10 (items)
    # 548 PRECALL                  0
    # 552 CALL                     0
    # 562 GET_ITER
    # 564 PRECALL                  0
    # 568 CALL                     0
    # 578 STORE_FAST               1 (res)
    # 382         580 LOAD_FAST                1 (res)
    # 582 LOAD_FAST                2 (remaining)
    # 584 BUILD_TUPLE              2
    # 586 RETURN_VALUE
    # Disassembly of <code object <dictcomp> at 0x000001EBD7DF0830, file "pydantic\_internal\_known_annotated_metadata.py", line 375>:
    # 375           0 RESUME                   0
    # 2 BUILD_MAP                0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER                29 (to 66)
    # 8 UNPACK_SEQUENCE          2
    # 12 STORE_FAST               1 (k)
    # 14 STORE_FAST               2 (v)
    # 16 LOAD_FAST                1 (k)
    # 18 LOAD_METHOD              0 (startswith)
    # 40 LOAD_CONST               0 ('_')
    # 42 PRECALL                  1
    # 46 CALL                     1
    # 56 POP_JUMP_BACKWARD_IF_TRUE    26 (to 6)
    # 58 LOAD_FAST                1 (k)
    # 60 LOAD_FAST                2 (v)
    # 62 MAP_ADD                  2
    # 64 JUMP_BACKWARD           30 (to 6)
    # >>   66 RETURN_VALUE
    # Disassembly of <code object <dictcomp> at 0x000001EBD7E42950, file "pydantic\_internal\_known_annotated_metadata.py", line 381>:
    # 381           0 RESUME                   0
    # 2 BUILD_MAP                0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER                10 (to 28)
    # 8 UNPACK_SEQUENCE          2
    # 12 STORE_FAST               1 (k)
    # 14 STORE_FAST               2 (v)
    # 16 LOAD_FAST                2 (v)
    # 18 POP_JUMP_BACKWARD_IF_NONE     7 (to 6)
    # 20 LOAD_FAST                1 (k)
    # 22 LOAD_FAST                2 (v)
    # 24 MAP_ADD                  2
    # 26 JUMP_BACKWARD           11 (to 6)
    # >>   28 RETURN_VALUE

def check_metadata(metadata, allowed, source_type):
    """A small utility function to validate that the given metadata can be applied to the target.
    More than saving lines of code, this gives us a consistent error message for all of our internal implementations.

    Args:
        metadata: A dict of metadata.
        allowed: An iterable of allowed metadata.
        source_type: The source type.

    Raises:
        TypeError: If there is metadatas that can't be applied on source type.
    """
    # 385           0 RESUME                   0
    # 397           2 LOAD_FAST                0 (metadata)
    # 4 LOAD_METHOD              0 (keys)
    # 26 PRECALL                  0
    # 30 CALL                     0
    # 40 LOAD_GLOBAL              3 (NULL + set)
    # 52 LOAD_FAST                1 (allowed)
    # 54 PRECALL                  1
    # 58 CALL                     1
    # 68 BINARY_OP               10 (-)
    # 72 STORE_FAST               3 (unknown)
    # 398          74 LOAD_FAST                3 (unknown)
    # 76 POP_JUMP_FORWARD_IF_FALSE    50 (to 178)
    # 399          78 LOAD_GLOBAL              5 (NULL + TypeError)
    # 400          90 LOAD_CONST               1 ('The following constraints cannot be applied to ')
    # 92 LOAD_FAST                2 (source_type)
    # 94 FORMAT_VALUE             2 (repr)
    # 96 LOAD_CONST               2 (': ')
    # 98 LOAD_CONST               3 (', ')
    # 100 LOAD_METHOD              3 (join)
    # 122 LOAD_CONST               4 (<code object <listcomp> at 0x000001EBD7E13B80, file "pydantic\_internal\_known_annotated_metadata.py", line 400>)
    # 124 MAKE_FUNCTION            0
    # 126 LOAD_FAST                3 (unknown)
    # 128 GET_ITER
    # 130 PRECALL                  0
    # 134 CALL                     0
    # 144 PRECALL                  1
    # 148 CALL                     1
    # 158 FORMAT_VALUE             0
    # 160 BUILD_STRING             4
    # 399         162 PRECALL                  1
    # 166 CALL                     1
    # 176 RAISE_VARARGS            1
    # 398     >>  178 LOAD_CONST               5 (None)
    # 180 RETURN_VALUE
    # Disassembly of <code object <listcomp> at 0x000001EBD7E13B80, file "pydantic\_internal\_known_annotated_metadata.py", line 400>:
    # 400           0 RESUME                   0
    # 2 BUILD_LIST               0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER                 5 (to 18)
    # 8 STORE_FAST               1 (k)
    # 10 LOAD_FAST                1 (k)
    # 12 FORMAT_VALUE             2 (repr)
    # 14 LIST_APPEND              2
    # 16 JUMP_BACKWARD            6 (to 6)
    # >>   18 RETURN_VALUE
