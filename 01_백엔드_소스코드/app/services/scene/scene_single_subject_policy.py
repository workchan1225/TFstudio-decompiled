# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: app\services\scene\scene_single_subject_policy.py

import re
from typing import Any
from utils.character_name_matcher import normalize_character_name

def <genexpr>(.0):
    # 80           0 RETURN_GENERATOR
    # 2 POP_TOP
    # 4 RESUME                   0
    # 6 LOAD_FAST                0 (.0)
    # >>    8 FOR_ITER                24 (to 58)
    # 10 STORE_FAST               1 (token)
    # 12 LOAD_GLOBAL              1 (NULL + re)
    # 24 LOAD_ATTR                1 (escape)
    # 34 LOAD_FAST                1 (token)
    # 36 PRECALL                  1
    # 40 CALL                     1
    # 50 YIELD_VALUE
    # 52 RESUME                   1
    # 54 POP_TOP
    # 56 JUMP_BACKWARD           25 (to 8)
    # >>   58 LOAD_CONST               0 (None)
    # 60 RETURN_VALUE

def should_apply_single_subject_lock(*, scene_text, detected_names, scene_actors, scene_actor_profile):
    # 0 MAKE_CELL                9 (profile)
    # 198           2 RESUME                   0
    # 205           4 LOAD_GLOBAL              1 (NULL + _normalize_name_list)
    # 16 LOAD_FAST                1 (detected_names)
    # 18 PRECALL                  1
    # 22 CALL                     1
    # 32 STORE_FAST               4 (detected_name_list)
    # 206          34 LOAD_GLOBAL              3 (NULL + len)
    # 46 LOAD_FAST                4 (detected_name_list)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 LOAD_CONST               1 (1)
    # 64 COMPARE_OP               4 (>)
    # 70 POP_JUMP_FORWARD_IF_FALSE     2 (to 76)
    # 207          72 LOAD_CONST               2 (False)
    # 74 RETURN_VALUE
    # 209     >>   76 LOAD_FAST                3 (scene_actor_profile)
    # 78 JUMP_IF_TRUE_OR_POP      1 (to 82)
    # 80 BUILD_MAP                0
    # >>   82 STORE_DEREF              9 (profile)
    # 210          84 LOAD_GLOBAL              5 (NULL + int)
    # 96 LOAD_DEREF               9 (profile)
    # 98 LOAD_METHOD              3 (get)
    # 120 LOAD_CONST               3 ('visibleActorCount')
    # 122 PRECALL                  1
    # 126 CALL                     1
    # 136 JUMP_IF_TRUE_OR_POP      1 (to 140)
    # 138 LOAD_CONST               4 (0)
    # >>  140 PRECALL                  1
    # 144 CALL                     1
    # 154 STORE_FAST               5 (visible_actor_count)
    # 211         156 LOAD_FAST                5 (visible_actor_count)
    # 158 LOAD_CONST               1 (1)
    # 160 COMPARE_OP               4 (>)
    # 166 POP_JUMP_FORWARD_IF_FALSE     2 (to 172)
    # 212         168 LOAD_CONST               2 (False)
    # 170 RETURN_VALUE
    # 213     >>  172 LOAD_GLOBAL              9 (NULL + any)
    # 184 LOAD_CLOSURE             9 (profile)
    # 186 BUILD_TUPLE              1
    # 188 LOAD_CONST               5 (<code object <genexpr> at 0x000001EBD778B2D0, file "app\services\scene\scene_single_subject_policy.py", line 213>)
    # 190 MAKE_FUNCTION            8 (closure)
    # 215         192 LOAD_CONST               6 (('hasRelationalActor', 'hasNonRegisteredActor', 'hasGroupActor', 'hasCrowdActor', 'hasBackgroundActor'))
    # 213         194 GET_ITER
    # 196 PRECALL                  0
    # 200 CALL                     0
    # 210 PRECALL                  1
    # 214 CALL                     1
    # 224 POP_JUMP_FORWARD_IF_FALSE     2 (to 230)
    # 223         226 LOAD_CONST               2 (False)
    # 228 RETURN_VALUE
    # 225     >>  230 LOAD_FAST                2 (scene_actors)
    # 232 JUMP_IF_TRUE_OR_POP      1 (to 236)
    # 234 BUILD_LIST               0
    # >>  236 GET_ITER
    # >>  238 FOR_ITER               201 (to 642)
    # 240 STORE_FAST               6 (actor)
    # 226         242 LOAD_GLOBAL             11 (NULL + isinstance)
    # 254 LOAD_FAST                6 (actor)
    # 256 LOAD_GLOBAL             12 (dict)
    # 268 PRECALL                  2
    # 272 CALL                     2
    # 282 POP_JUMP_FORWARD_IF_TRUE     1 (to 286)
    # 227         284 JUMP_BACKWARD           24 (to 238)
    # 228     >>  286 LOAD_GLOBAL             15 (NULL + str)
    # 298 LOAD_FAST                6 (actor)
    # 300 LOAD_METHOD              3 (get)
    # 322 LOAD_CONST               7 ('actorType')
    # 324 PRECALL                  1
    # 328 CALL                     1
    # 338 JUMP_IF_TRUE_OR_POP      1 (to 342)
    # 340 LOAD_CONST               8 ('')
    # >>  342 PRECALL                  1
    # 346 CALL                     1
    # 356 LOAD_METHOD              8 (strip)
    # 378 PRECALL                  0
    # 382 CALL                     0
    # 392 LOAD_CONST               9 ('registered_character')
    # 394 COMPARE_OP               3 (!=)
    # 400 POP_JUMP_FORWARD_IF_FALSE     3 (to 408)
    # 229         402 POP_TOP
    # 404 LOAD_CONST               2 (False)
    # 406 RETURN_VALUE
    # 230     >>  408 LOAD_GLOBAL             15 (NULL + str)
    # 420 LOAD_FAST                6 (actor)
    # 422 LOAD_METHOD              3 (get)
    # 444 LOAD_CONST              10 ('interactionTarget')
    # 446 PRECALL                  1
    # 450 CALL                     1
    # 460 JUMP_IF_TRUE_OR_POP      1 (to 464)
    # 462 LOAD_CONST               8 ('')
    # >>  464 PRECALL                  1
    # 468 CALL                     1
    # 478 LOAD_METHOD              8 (strip)
    # 500 PRECALL                  0
    # 504 CALL                     0
    # 514 POP_JUMP_FORWARD_IF_FALSE     3 (to 522)
    # 231         516 POP_TOP
    # 518 LOAD_CONST               2 (False)
    # 520 RETURN_VALUE
    # 232     >>  522 LOAD_GLOBAL             15 (NULL + str)
    # 534 LOAD_FAST                6 (actor)
    # 536 LOAD_METHOD              3 (get)
    # 558 LOAD_CONST              11 ('placementHint')
    # 560 PRECALL                  1
    # 564 CALL                     1
    # 574 JUMP_IF_TRUE_OR_POP      1 (to 578)
    # 576 LOAD_CONST               8 ('')
    # >>  578 PRECALL                  1
    # 582 CALL                     1
    # 592 LOAD_METHOD              8 (strip)
    # 614 PRECALL                  0
    # 618 CALL                     0
    # 628 LOAD_CONST              12 (frozenset({'foreground', 'layered_depth', 'background', 'dispersed'}))
    # 630 CONTAINS_OP              0
    # 632 POP_JUMP_FORWARD_IF_FALSE     3 (to 640)
    # 233         634 POP_TOP
    # 636 LOAD_CONST               2 (False)
    # 638 RETURN_VALUE
    # 232     >>  640 JUMP_BACKWARD          202 (to 238)
    # 235     >>  642 LOAD_GLOBAL             19 (NULL + re)
    # 654 LOAD_ATTR               10 (sub)
    # 664 LOAD_CONST              13 ('\\s+')
    # 666 LOAD_CONST              14 (' ')
    # 668 LOAD_GLOBAL             15 (NULL + str)
    # 680 LOAD_FAST                0 (scene_text)
    # 682 JUMP_IF_TRUE_OR_POP      1 (to 686)
    # 684 LOAD_CONST               8 ('')
    # >>  686 PRECALL                  1
    # 690 CALL                     1
    # 700 PRECALL                  3
    # 704 CALL                     3
    # 714 LOAD_METHOD              8 (strip)
    # 736 PRECALL                  0
    # 740 CALL                     0
    # 750 STORE_FAST               7 (normalized_scene_text)
    # 236         752 LOAD_FAST                7 (normalized_scene_text)
    # 754 POP_JUMP_FORWARD_IF_TRUE     6 (to 768)
    # 237         756 LOAD_FAST                5 (visible_actor_count)
    # 758 LOAD_CONST               1 (1)
    # 760 COMPARE_OP               1 (<=)
    # 766 RETURN_VALUE
    # 239     >>  768 LOAD_GLOBAL             22 (_MULTI_PERSON_SCENE_PATTERNS)
    # 780 GET_ITER
    # >>  782 FOR_ITER                26 (to 836)
    # 784 STORE_FAST               8 (pattern)
    # 240         786 LOAD_FAST                8 (pattern)
    # 788 LOAD_METHOD             12 (search)
    # 810 LOAD_FAST                7 (normalized_scene_text)
    # 812 PRECALL                  1
    # 816 CALL                     1
    # 826 POP_JUMP_FORWARD_IF_FALSE     3 (to 834)
    # 241         828 POP_TOP
    # 830 LOAD_CONST               2 (False)
    # 832 RETURN_VALUE
    # 240     >>  834 JUMP_BACKWARD           27 (to 782)
    # 243     >>  836 LOAD_CONST              15 (True)
    # 838 RETURN_VALUE
    # Disassembly of <code object <genexpr> at 0x000001EBD778B2D0, file "app\services\scene\scene_single_subject_policy.py", line 213>:
    # 0 COPY_FREE_VARS           1
    # 213           2 RETURN_GENERATOR
    # 4 POP_TOP
    # 6 RESUME                   0
    # 8 LOAD_FAST                0 (.0)
    # >>   10 FOR_ITER                38 (to 88)
    # 215          12 STORE_FAST               1 (flag)
    # 214          14 LOAD_GLOBAL              1 (NULL + bool)
    # 26 LOAD_DEREF               2 (profile)
    # 28 LOAD_METHOD              1 (get)
    # 50 LOAD_FAST                1 (flag)
    # 52 PRECALL                  1
    # 56 CALL                     1
    # 66 PRECALL                  1
    # 70 CALL                     1
    # 213          80 YIELD_VALUE
    # 82 RESUME                   1
    # 84 POP_TOP
    # 86 JUMP_BACKWARD           39 (to 10)
    # >>   88 LOAD_CONST               0 (None)
    # 90 RETURN_VALUE

def resolve_single_registered_subject_character(*, characters, detected_names, scene_text, scene_actors, scene_actor_profile):
    # 246           0 RESUME                   0
    # 254           2 LOAD_GLOBAL              1 (NULL + _normalize_name_list)
    # 14 LOAD_FAST                1 (detected_names)
    # 16 PRECALL                  1
    # 20 CALL                     1
    # 30 STORE_FAST               5 (detected_name_list)
    # 255          32 LOAD_GLOBAL              3 (NULL + should_apply_single_subject_lock)
    # 256          44 LOAD_FAST                2 (scene_text)
    # 257          46 LOAD_FAST                5 (detected_name_list)
    # 258          48 LOAD_FAST                3 (scene_actors)
    # 259          50 LOAD_FAST                4 (scene_actor_profile)
    # 255          52 KW_NAMES                 1
    # 54 PRECALL                  4
    # 58 CALL                     4
    # 68 POP_JUMP_FORWARD_IF_TRUE     2 (to 74)
    # 261          70 LOAD_CONST               0 (None)
    # 72 RETURN_VALUE
    # 262     >>   74 LOAD_GLOBAL              5 (NULL + len)
    # 86 LOAD_FAST                5 (detected_name_list)
    # 88 PRECALL                  1
    # 92 CALL                     1
    # 102 LOAD_CONST               2 (1)
    # 104 COMPARE_OP               4 (>)
    # 110 POP_JUMP_FORWARD_IF_FALSE     2 (to 116)
    # 263         112 LOAD_CONST               0 (None)
    # 114 RETURN_VALUE
    # 265     >>  116 LOAD_GLOBAL              7 (NULL + _filter_matching_characters)
    # 128 LOAD_FAST                0 (characters)
    # 130 LOAD_FAST                5 (detected_name_list)
    # 132 PRECALL                  2
    # 136 CALL                     2
    # 146 STORE_FAST               6 (matched_characters)
    # 266         148 LOAD_FAST                6 (matched_characters)
    # 150 POP_JUMP_FORWARD_IF_FALSE     3 (to 158)
    # 267         152 LOAD_FAST                6 (matched_characters)
    # 154 STORE_FAST               7 (candidate_pool)
    # 156 JUMP_FORWARD            71 (to 300)
    # 268     >>  158 LOAD_GLOBAL              5 (NULL + len)
    # 170 LOAD_FAST                0 (characters)
    # 172 JUMP_IF_TRUE_OR_POP      1 (to 176)
    # 174 BUILD_LIST               0
    # >>  176 PRECALL                  1
    # 180 CALL                     1
    # 190 LOAD_CONST               2 (1)
    # 192 COMPARE_OP               2 (==)
    # 198 POP_JUMP_FORWARD_IF_FALSE    48 (to 296)
    # 200 LOAD_GLOBAL              5 (NULL + len)
    # 212 LOAD_FAST                5 (detected_name_list)
    # 214 PRECALL                  1
    # 218 CALL                     1
    # 228 LOAD_CONST               2 (1)
    # 230 COMPARE_OP               1 (<=)
    # 236 POP_JUMP_FORWARD_IF_FALSE    29 (to 296)
    # 269         238 LOAD_GLOBAL              9 (NULL + _has_strong_registered_fallback_signal)
    # 270         250 LOAD_FAST                2 (scene_text)
    # 271         252 LOAD_FAST                5 (detected_name_list)
    # 269         254 KW_NAMES                 3
    # 256 PRECALL                  2
    # 260 CALL                     2
    # 270 POP_JUMP_FORWARD_IF_TRUE     2 (to 276)
    # 273         272 LOAD_CONST               0 (None)
    # 274 RETURN_VALUE
    # 274     >>  276 LOAD_FAST                0 (characters)
    # 278 LOAD_CONST               4 (0)
    # 280 BINARY_SUBSCR
    # 290 BUILD_LIST               1
    # 292 STORE_FAST               7 (candidate_pool)
    # 294 JUMP_FORWARD             2 (to 300)
    # 276     >>  296 LOAD_CONST               0 (None)
    # 298 RETURN_VALUE
    # 278     >>  300 LOAD_GLOBAL              5 (NULL + len)
    # 312 LOAD_FAST                7 (candidate_pool)
    # 314 PRECALL                  1
    # 318 CALL                     1
    # 328 LOAD_CONST               2 (1)
    # 330 COMPARE_OP               3 (!=)
    # 336 POP_JUMP_FORWARD_IF_FALSE     2 (to 342)
    # 279         338 LOAD_CONST               0 (None)
    # 340 RETURN_VALUE
    # 281     >>  342 LOAD_FAST                7 (candidate_pool)
    # 344 LOAD_CONST               4 (0)
    # 346 BINARY_SUBSCR
    # 356 STORE_FAST               8 (candidate)
    # 282         358 LOAD_GLOBAL             11 (NULL + _has_reference_image)
    # 370 LOAD_FAST                8 (candidate)
    # 372 PRECALL                  1
    # 376 CALL                     1
    # 386 POP_JUMP_FORWARD_IF_TRUE     2 (to 392)
    # 283         388 LOAD_CONST               0 (None)
    # 390 RETURN_VALUE
    # 284     >>  392 LOAD_FAST                8 (candidate)
    # 394 RETURN_VALUE

def build_single_registered_subject_lock(*, subject_name, identity_hint):
    # 287           0 RESUME                   0
    # 292           2 LOAD_GLOBAL              1 (NULL + str)
    # 14 LOAD_FAST                0 (subject_name)
    # 16 JUMP_IF_TRUE_OR_POP      1 (to 20)
    # 18 LOAD_CONST               1 ('')
    # >>   20 PRECALL                  1
    # 24 CALL                     1
    # 34 LOAD_METHOD              1 (strip)
    # 56 PRECALL                  0
    # 60 CALL                     0
    # 70 STORE_FAST               2 (clean_name)
    # 293          72 LOAD_FAST                2 (clean_name)
    # 74 POP_JUMP_FORWARD_IF_TRUE     2 (to 80)
    # 294          76 LOAD_CONST               1 ('')
    # 78 RETURN_VALUE
    # 297     >>   80 LOAD_CONST               2 ('[SINGLE REGISTERED SUBJECT LOCK - HIGHEST PRIORITY]')
    # 298          82 LOAD_CONST               3 ('- The ONLY visible character subject in this scene is ')
    # 84 LOAD_FAST                2 (clean_name)
    # 86 FORMAT_VALUE             0
    # 88 LOAD_CONST               4 ('.')
    # 90 BUILD_STRING             3
    # 300          92 LOAD_CONST               5 ('- Any generic role noun or placeholder in narration/scene text (expert, presenter, analyst, narrator, speaker, guide, host, reporter, teacher, doctor, official, worker, man, woman, person, character, figure, subject, protagonist; 전문가, 발표자, 해설자, 화자, 진행자, 기자, 선생, 의사, 남성, 여성, 사람, 인물, 주인공) refers to ')
    # 304          94 LOAD_FAST                2 (clean_name)
    # 300          96 FORMAT_VALUE             0
    # 98 LOAD_CONST               6 (', NOT to a separate extra person.')
    # 100 BUILD_STRING             3
    # 306         102 LOAD_CONST               7 ('- Keep unnamed bystanders and extras minimal and subordinate — they may appear as secondary figures but must not compete with the focal subject.')
    # 307         104 LOAD_CONST               8 ('- Keep ')
    # 106 LOAD_FAST                2 (clean_name)
    # 108 FORMAT_VALUE             0
    # 110 LOAD_CONST               9 (' as the primary visual focus and main narrative subject.')
    # 112 BUILD_STRING             3
    # 296         114 BUILD_LIST               5
    # 116 STORE_FAST               3 (instruction_lines)
    # 309         118 LOAD_GLOBAL              5 (NULL + re)
    # 130 LOAD_ATTR                3 (sub)
    # 140 LOAD_CONST              10 ('\\s+')
    # 142 LOAD_CONST              11 (' ')
    # 144 LOAD_GLOBAL              1 (NULL + str)
    # 156 LOAD_FAST                1 (identity_hint)
    # 158 JUMP_IF_TRUE_OR_POP      1 (to 162)
    # 160 LOAD_CONST               1 ('')
    # >>  162 PRECALL                  1
    # 166 CALL                     1
    # 176 PRECALL                  3
    # 180 CALL                     3
    # 190 LOAD_METHOD              1 (strip)
    # 212 PRECALL                  0
    # 216 CALL                     0
    # 226 STORE_FAST               4 (normalized_identity_hint)
    # 310         228 LOAD_FAST                4 (normalized_identity_hint)
    # 230 POP_JUMP_FORWARD_IF_FALSE    24 (to 280)
    # 311         232 LOAD_FAST                3 (instruction_lines)
    # 234 LOAD_METHOD              4 (append)
    # 256 LOAD_CONST              12 ('- Registered identity anchor: ')
    # 258 LOAD_FAST                4 (normalized_identity_hint)
    # 260 FORMAT_VALUE             0
    # 262 BUILD_STRING             2
    # 264 PRECALL                  1
    # 268 CALL                     1
    # 278 POP_TOP
    # 312     >>  280 LOAD_CONST              13 ('\n')
    # 282 LOAD_METHOD              5 (join)
    # 304 LOAD_FAST                3 (instruction_lines)
    # 306 PRECALL                  1
    # 310 CALL                     1
    # 320 RETURN_VALUE

def rewrite_single_subject_role_aliases(text, subject_name):
    # 315           0 RESUME                   0
    # 316           2 LOAD_FAST                0 (text)
    # 4 POP_JUMP_FORWARD_IF_FALSE     2 (to 10)
    # 6 LOAD_FAST                1 (subject_name)
    # 8 POP_JUMP_FORWARD_IF_TRUE     2 (to 14)
    # 317     >>   10 LOAD_FAST                0 (text)
    # 12 RETURN_VALUE
    # 319     >>   14 LOAD_GLOBAL              1 (NULL + str)
    # 26 LOAD_FAST                0 (text)
    # 28 PRECALL                  1
    # 32 CALL                     1
    # 42 STORE_FAST               2 (rewritten)
    # 320          44 LOAD_GLOBAL              2 (_TAGGED_ROLE_PATTERN)
    # 56 LOAD_METHOD              2 (sub)
    # 78 LOAD_CONST               1 ('@')
    # 80 LOAD_FAST                1 (subject_name)
    # 82 FORMAT_VALUE             0
    # 84 BUILD_STRING             2
    # 86 LOAD_FAST                2 (rewritten)
    # 88 PRECALL                  2
    # 92 CALL                     2
    # 102 STORE_FAST               2 (rewritten)
    # 321         104 LOAD_GLOBAL              6 (_ENGLISH_ARTICLE_ROLE_PATTERN)
    # 116 LOAD_METHOD              2 (sub)
    # 138 LOAD_FAST                1 (subject_name)
    # 140 LOAD_FAST                2 (rewritten)
    # 142 PRECALL                  2
    # 146 CALL                     2
    # 156 STORE_FAST               2 (rewritten)
    # 322         158 LOAD_GLOBAL              8 (_KOREAN_ROLE_PATTERN)
    # 170 LOAD_METHOD              2 (sub)
    # 192 LOAD_FAST                1 (subject_name)
    # 194 LOAD_FAST                2 (rewritten)
    # 196 PRECALL                  2
    # 200 CALL                     2
    # 210 STORE_FAST               2 (rewritten)
    # 323         212 LOAD_GLOBAL             11 (NULL + re)
    # 224 LOAD_ATTR                2 (sub)
    # 234 LOAD_CONST               2 ('\\s+')
    # 236 LOAD_CONST               3 (' ')
    # 238 LOAD_FAST                2 (rewritten)
    # 240 PRECALL                  3
    # 244 CALL                     3
    # 254 LOAD_METHOD              6 (strip)
    # 276 PRECALL                  0
    # 280 CALL                     0
    # 290 STORE_FAST               2 (rewritten)
    # 324         292 LOAD_FAST                2 (rewritten)
    # 294 RETURN_VALUE

def collapse_generic_human_subject_description(scene_text, subject_name):
    # 327           0 RESUME                   0
    # 328           2 LOAD_FAST                0 (scene_text)
    # 4 POP_JUMP_FORWARD_IF_FALSE     2 (to 10)
    # 6 LOAD_FAST                1 (subject_name)
    # 8 POP_JUMP_FORWARD_IF_TRUE     2 (to 14)
    # 329     >>   10 LOAD_FAST                0 (scene_text)
    # 12 RETURN_VALUE
    # 331     >>   14 LOAD_GLOBAL              1 (NULL + rewrite_single_subject_role_aliases)
    # 26 LOAD_FAST                0 (scene_text)
    # 28 LOAD_FAST                1 (subject_name)
    # 30 PRECALL                  2
    # 34 CALL                     2
    # 44 STORE_FAST               2 (collapsed)
    # 332          46 LOAD_GLOBAL              2 (_GENERIC_HUMAN_SUBJECT_PATTERNS)
    # 58 GET_ITER
    # >>   60 FOR_ITER                33 (to 128)
    # 62 STORE_FAST               3 (pattern)
    # 333          64 LOAD_FAST                3 (pattern)
    # 66 LOAD_METHOD              2 (subn)
    # 88 LOAD_FAST                1 (subject_name)
    # 90 LOAD_FAST                2 (collapsed)
    # 92 LOAD_CONST               1 (1)
    # 94 KW_NAMES                 2
    # 96 PRECALL                  3
    # 100 CALL                     3
    # 110 UNPACK_SEQUENCE          2
    # 114 STORE_FAST               2 (collapsed)
    # 116 STORE_FAST               4 (count)
    # 334         118 LOAD_FAST                4 (count)
    # 120 POP_JUMP_FORWARD_IF_FALSE     2 (to 126)
    # 335         122 POP_TOP
    # 124 JUMP_FORWARD             1 (to 128)
    # 334     >>  126 JUMP_BACKWARD           34 (to 60)
    # 336     >>  128 LOAD_GLOBAL              7 (NULL + re)
    # 140 LOAD_ATTR                4 (sub)
    # 150 LOAD_CONST               3 ('\\s+')
    # 152 LOAD_CONST               4 (' ')
    # 154 LOAD_FAST                2 (collapsed)
    # 156 PRECALL                  3
    # 160 CALL                     3
    # 170 LOAD_METHOD              5 (strip)
    # 192 PRECALL                  0
    # 196 CALL                     0
    # 206 STORE_FAST               2 (collapsed)
    # 337         208 LOAD_FAST                2 (collapsed)
    # 210 RETURN_VALUE

def resolve_subject_display_name(character):
    # 340           0 RESUME                   0
    # 341           2 LOAD_GLOBAL              1 (NULL + isinstance)
    # 14 LOAD_FAST                0 (character)
    # 16 LOAD_GLOBAL              2 (dict)
    # 28 PRECALL                  2
    # 32 CALL                     2
    # 42 POP_JUMP_FORWARD_IF_TRUE     2 (to 48)
    # 342          44 LOAD_CONST               1 ('')
    # 46 RETURN_VALUE
    # 343     >>   48 LOAD_CONST               2 (('name', 'nameKo', 'characterName', 'uniqueId'))
    # 50 GET_ITER
    # >>   52 FOR_ITER                82 (to 218)
    # 54 STORE_FAST               1 (key)
    # 344          56 LOAD_GLOBAL              5 (NULL + str)
    # 68 LOAD_FAST                0 (character)
    # 70 LOAD_METHOD              3 (get)
    # 92 LOAD_FAST                1 (key)
    # 94 PRECALL                  1
    # 98 CALL                     1
    # 108 JUMP_IF_TRUE_OR_POP      1 (to 112)
    # 110 LOAD_CONST               1 ('')
    # >>  112 PRECALL                  1
    # 116 CALL                     1
    # 126 LOAD_METHOD              4 (replace)
    # 148 LOAD_CONST               3 ('@')
    # 150 LOAD_CONST               1 ('')
    # 152 PRECALL                  2
    # 156 CALL                     2
    # 166 LOAD_METHOD              5 (strip)
    # 188 PRECALL                  0
    # 192 CALL                     0
    # 202 STORE_FAST               2 (value)
    # 345         204 LOAD_FAST                2 (value)
    # 206 POP_JUMP_FORWARD_IF_FALSE     4 (to 216)
    # 346         208 LOAD_FAST                2 (value)
    # 210 SWAP                     2
    # 212 POP_TOP
    # 214 RETURN_VALUE
    # 345     >>  216 JUMP_BACKWARD           83 (to 52)
    # 347     >>  218 LOAD_CONST               1 ('')
    # 220 RETURN_VALUE

def _has_strong_registered_fallback_signal(*, scene_text, detected_names):
    # 350           0 RESUME                   0
    # 355           2 LOAD_CONST               1 (<code object <setcomp> at 0x000001EBD732A590, file "app\services\scene\scene_single_subject_policy.py", line 355>)
    # 4 MAKE_FUNCTION            0
    # 357           6 LOAD_FAST                1 (detected_names)
    # 355           8 GET_ITER
    # 10 PRECALL                  0
    # 14 CALL                     0
    # 24 STORE_FAST               2 (normalized_detected_names)
    # 360          26 LOAD_FAST                2 (normalized_detected_names)
    # 28 LOAD_METHOD              0 (intersection)
    # 361          50 BUILD_SET                0
    # 362          52 LOAD_CONST               2 (<code object <listcomp> at 0x000001EBD783A1F0, file "app\services\scene\scene_single_subject_policy.py", line 362>)
    # 54 MAKE_FUNCTION            0
    # 56 LOAD_GLOBAL              2 (_STRONG_REGISTERED_FALLBACK_ENGLISH_ALIASES)
    # 68 GET_ITER
    # 70 PRECALL                  0
    # 74 CALL                     0
    # 361          84 SET_UPDATE               1
    # 363          86 LOAD_CONST               3 (<code object <listcomp> at 0x000001EBD783A2E0, file "app\services\scene\scene_single_subject_policy.py", line 363>)
    # 88 MAKE_FUNCTION            0
    # 90 LOAD_GLOBAL              4 (_STRONG_REGISTERED_FALLBACK_KOREAN_ALIASES)
    # 102 GET_ITER
    # 104 PRECALL                  0
    # 108 CALL                     0
    # 361         118 SET_UPDATE               1
    # 360         120 PRECALL                  1
    # 124 CALL                     1
    # 134 POP_JUMP_FORWARD_IF_FALSE     2 (to 140)
    # 366         136 LOAD_CONST               4 (True)
    # 138 RETURN_VALUE
    # 368     >>  140 LOAD_GLOBAL              7 (NULL + re)
    # 152 LOAD_ATTR                4 (sub)
    # 162 LOAD_CONST               5 ('\\s+')
    # 164 LOAD_CONST               6 (' ')
    # 166 LOAD_GLOBAL             11 (NULL + str)
    # 178 LOAD_FAST                0 (scene_text)
    # 180 JUMP_IF_TRUE_OR_POP      1 (to 184)
    # 182 LOAD_CONST               7 ('')
    # >>  184 PRECALL                  1
    # 188 CALL                     1
    # 198 PRECALL                  3
    # 202 CALL                     3
    # 212 LOAD_METHOD              6 (strip)
    # 234 PRECALL                  0
    # 238 CALL                     0
    # 248 STORE_FAST               3 (normalized_scene_text)
    # 369         250 LOAD_FAST                3 (normalized_scene_text)
    # 252 POP_JUMP_FORWARD_IF_TRUE     2 (to 258)
    # 370         254 LOAD_CONST               8 (False)
    # 256 RETURN_VALUE
    # 372     >>  258 LOAD_GLOBAL             15 (NULL + bool)
    # 373         270 LOAD_GLOBAL             16 (_STRONG_TAGGED_ROLE_PATTERN)
    # 282 LOAD_METHOD              9 (search)
    # 304 LOAD_FAST                3 (normalized_scene_text)
    # 306 PRECALL                  1
    # 310 CALL                     1
    # 320 JUMP_IF_TRUE_OR_POP     51 (to 424)
    # 374         322 LOAD_GLOBAL             20 (_STRONG_ENGLISH_ARTICLE_ROLE_PATTERN)
    # 334 LOAD_METHOD              9 (search)
    # 356 LOAD_FAST                3 (normalized_scene_text)
    # 358 PRECALL                  1
    # 362 CALL                     1
    # 373         372 JUMP_IF_TRUE_OR_POP     25 (to 424)
    # 375         374 LOAD_GLOBAL             22 (_STRONG_KOREAN_ROLE_PATTERN)
    # 386 LOAD_METHOD              9 (search)
    # 408 LOAD_FAST                3 (normalized_scene_text)
    # 410 PRECALL                  1
    # 414 CALL                     1
    # 372     >>  424 PRECALL                  1
    # 428 CALL                     1
    # 438 RETURN_VALUE
    # Disassembly of <code object <setcomp> at 0x000001EBD732A590, file "app\services\scene\scene_single_subject_policy.py", line 355>:
    # 355           0 RESUME                   0
    # 2 BUILD_SET                0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER               110 (to 228)
    # 357           8 STORE_FAST               1 (name)
    # 358          10 LOAD_GLOBAL              1 (NULL + str)
    # 22 LOAD_FAST                1 (name)
    # 24 JUMP_IF_TRUE_OR_POP      1 (to 28)
    # 26 LOAD_CONST               0 ('')
    # >>   28 PRECALL                  1
    # 32 CALL                     1
    # 42 LOAD_METHOD              1 (strip)
    # 64 PRECALL                  0
    # 68 CALL                     0
    # 355          78 POP_JUMP_BACKWARD_IF_FALSE    37 (to 6)
    # 356          80 LOAD_GLOBAL              1 (NULL + str)
    # 92 LOAD_FAST                1 (name)
    # 94 JUMP_IF_TRUE_OR_POP      1 (to 98)
    # 96 LOAD_CONST               0 ('')
    # >>   98 PRECALL                  1
    # 102 CALL                     1
    # 112 LOAD_METHOD              2 (replace)
    # 134 LOAD_CONST               1 ('@')
    # 136 LOAD_CONST               0 ('')
    # 138 PRECALL                  2
    # 142 CALL                     2
    # 152 LOAD_METHOD              1 (strip)
    # 174 PRECALL                  0
    # 178 CALL                     0
    # 188 LOAD_METHOD              3 (lower)
    # 210 PRECALL                  0
    # 214 CALL                     0
    # 355         224 SET_ADD                  2
    # 226 JUMP_BACKWARD          111 (to 6)
    # >>  228 RETURN_VALUE
    # Disassembly of <code object <listcomp> at 0x000001EBD783A1F0, file "app\services\scene\scene_single_subject_policy.py", line 362>:
    # 362           0 RESUME                   0
    # 2 BUILD_LIST               0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER                22 (to 52)
    # 8 STORE_FAST               1 (token)
    # 10 LOAD_FAST                1 (token)
    # 12 LOAD_METHOD              0 (lower)
    # 34 PRECALL                  0
    # 38 CALL                     0
    # 48 LIST_APPEND              2
    # 50 JUMP_BACKWARD           23 (to 6)
    # >>   52 RETURN_VALUE
    # Disassembly of <code object <listcomp> at 0x000001EBD783A2E0, file "app\services\scene\scene_single_subject_policy.py", line 363>:
    # 363           0 RESUME                   0
    # 2 BUILD_LIST               0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER                22 (to 52)
    # 8 STORE_FAST               1 (token)
    # 10 LOAD_FAST                1 (token)
    # 12 LOAD_METHOD              0 (lower)
    # 34 PRECALL                  0
    # 38 CALL                     0
    # 48 LIST_APPEND              2
    # 50 JUMP_BACKWARD           23 (to 6)
    # >>   52 RETURN_VALUE

def _filter_matching_characters(characters, detected_names):
    # 379           0 RESUME                   0
    # 383           2 LOAD_FAST                1 (detected_names)
    # 4 POP_JUMP_FORWARD_IF_TRUE     2 (to 10)
    # 384           6 BUILD_LIST               0
    # 8 RETURN_VALUE
    # 386     >>   10 LOAD_CONST               1 (<code object <setcomp> at 0x000001EBD732A730, file "app\services\scene\scene_single_subject_policy.py", line 386>)
    # 12 MAKE_FUNCTION            0
    # 388          14 LOAD_FAST                1 (detected_names)
    # 386          16 GET_ITER
    # 18 PRECALL                  0
    # 22 CALL                     0
    # 32 STORE_FAST               2 (detected_set)
    # 391          34 LOAD_FAST                2 (detected_set)
    # 36 POP_JUMP_FORWARD_IF_TRUE     2 (to 42)
    # 392          38 BUILD_LIST               0
    # 40 RETURN_VALUE
    # 394     >>   42 BUILD_LIST               0
    # 44 STORE_FAST               3 (matched)
    # 395          46 LOAD_FAST                0 (characters)
    # 48 JUMP_IF_TRUE_OR_POP      1 (to 52)
    # 50 BUILD_LIST               0
    # >>   52 GET_ITER
    # >>   54 FOR_ITER               107 (to 270)
    # 56 STORE_FAST               4 (character)
    # 396          58 LOAD_GLOBAL              1 (NULL + isinstance)
    # 70 LOAD_FAST                4 (character)
    # 72 LOAD_GLOBAL              2 (dict)
    # 84 PRECALL                  2
    # 88 CALL                     2
    # 98 POP_JUMP_FORWARD_IF_TRUE     1 (to 102)
    # 397         100 JUMP_BACKWARD           24 (to 54)
    # 398     >>  102 LOAD_CONST               2 (('name', 'nameKo', 'characterName', 'uniqueId'))
    # 104 GET_ITER
    # >>  106 FOR_ITER                80 (to 268)
    # 108 STORE_FAST               5 (key)
    # 399         110 LOAD_GLOBAL              5 (NULL + normalize_character_name)
    # 122 LOAD_GLOBAL              7 (NULL + str)
    # 134 LOAD_FAST                4 (character)
    # 136 LOAD_METHOD              4 (get)
    # 158 LOAD_FAST                5 (key)
    # 160 PRECALL                  1
    # 164 CALL                     1
    # 174 JUMP_IF_TRUE_OR_POP      1 (to 178)
    # 176 LOAD_CONST               3 ('')
    # >>  178 PRECALL                  1
    # 182 CALL                     1
    # 192 PRECALL                  1
    # 196 CALL                     1
    # 206 STORE_FAST               6 (normalized_value)
    # 400         208 LOAD_FAST                6 (normalized_value)
    # 210 POP_JUMP_FORWARD_IF_FALSE    27 (to 266)
    # 212 LOAD_FAST                6 (normalized_value)
    # 214 LOAD_FAST                2 (detected_set)
    # 216 CONTAINS_OP              0
    # 218 POP_JUMP_FORWARD_IF_FALSE    23 (to 266)
    # 401         220 LOAD_FAST                3 (matched)
    # 222 LOAD_METHOD              5 (append)
    # 244 LOAD_FAST                4 (character)
    # 246 PRECALL                  1
    # 250 CALL                     1
    # 260 POP_TOP
    # 402         262 POP_TOP
    # 264 JUMP_FORWARD             1 (to 268)
    # >>  266 JUMP_BACKWARD           81 (to 106)
    # >>  268 JUMP_BACKWARD          108 (to 54)
    # 403     >>  270 LOAD_FAST                3 (matched)
    # 272 RETURN_VALUE
    # Disassembly of <code object <setcomp> at 0x000001EBD732A730, file "app\services\scene\scene_single_subject_policy.py", line 386>:
    # 386           0 RESUME                   0
    # 2 BUILD_SET                0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER               105 (to 218)
    # 388           8 STORE_FAST               1 (name)
    # 389          10 LOAD_GLOBAL              1 (NULL + str)
    # 22 LOAD_FAST                1 (name)
    # 24 JUMP_IF_TRUE_OR_POP      1 (to 28)
    # 26 LOAD_CONST               0 ('')
    # >>   28 PRECALL                  1
    # 32 CALL                     1
    # 42 LOAD_METHOD              1 (strip)
    # 64 PRECALL                  0
    # 68 CALL                     0
    # 386          78 POP_JUMP_BACKWARD_IF_FALSE    37 (to 6)
    # 387          80 LOAD_GLOBAL              5 (NULL + normalize_character_name)
    # 92 LOAD_GLOBAL              1 (NULL + str)
    # 104 LOAD_FAST                1 (name)
    # 106 JUMP_IF_TRUE_OR_POP      1 (to 110)
    # 108 LOAD_CONST               0 ('')
    # >>  110 PRECALL                  1
    # 114 CALL                     1
    # 124 LOAD_METHOD              3 (replace)
    # 146 LOAD_CONST               1 ('@')
    # 148 LOAD_CONST               0 ('')
    # 150 PRECALL                  2
    # 154 CALL                     2
    # 164 LOAD_METHOD              1 (strip)
    # 186 PRECALL                  0
    # 190 CALL                     0
    # 200 PRECALL                  1
    # 204 CALL                     1
    # 386         214 SET_ADD                  2
    # 216 JUMP_BACKWARD          106 (to 6)
    # >>  218 RETURN_VALUE

def _normalize_name_list(names):
    # 406           0 RESUME                   0
    # 407           2 BUILD_LIST               0
    # 4 STORE_FAST               1 (normalized_names)
    # 408           6 LOAD_FAST                0 (names)
    # 8 JUMP_IF_TRUE_OR_POP      1 (to 12)
    # 10 BUILD_LIST               0
    # >>   12 GET_ITER
    # >>   14 FOR_ITER                80 (to 176)
    # 16 STORE_FAST               2 (raw_name)
    # 409          18 LOAD_GLOBAL              1 (NULL + str)
    # 30 LOAD_FAST                2 (raw_name)
    # 32 JUMP_IF_TRUE_OR_POP      1 (to 36)
    # 34 LOAD_CONST               1 ('')
    # >>   36 PRECALL                  1
    # 40 CALL                     1
    # 50 LOAD_METHOD              1 (replace)
    # 72 LOAD_CONST               2 ('@')
    # 74 LOAD_CONST               1 ('')
    # 76 PRECALL                  2
    # 80 CALL                     2
    # 90 LOAD_METHOD              2 (strip)
    # 112 PRECALL                  0
    # 116 CALL                     0
    # 126 STORE_FAST               3 (cleaned)
    # 410         128 LOAD_FAST                3 (cleaned)
    # 130 POP_JUMP_FORWARD_IF_FALSE    21 (to 174)
    # 411         132 LOAD_FAST                1 (normalized_names)
    # 134 LOAD_METHOD              3 (append)
    # 156 LOAD_FAST                3 (cleaned)
    # 158 PRECALL                  1
    # 162 CALL                     1
    # 172 POP_TOP
    # >>  174 JUMP_BACKWARD           81 (to 14)
    # 412     >>  176 LOAD_FAST                1 (normalized_names)
    # 178 RETURN_VALUE

def _has_reference_image(character):
    # 415           0 RESUME                   0
    # 416           2 LOAD_GLOBAL              1 (NULL + bool)
    # 417          14 LOAD_FAST                0 (character)
    # 16 LOAD_METHOD              1 (get)
    # 38 LOAD_CONST               1 ('imageDataUrl')
    # 40 PRECALL                  1
    # 44 CALL                     1
    # 54 JUMP_IF_TRUE_OR_POP     62 (to 180)
    # 418          56 LOAD_FAST                0 (character)
    # 58 LOAD_METHOD              1 (get)
    # 80 LOAD_CONST               2 ('imagePath')
    # 82 PRECALL                  1
    # 86 CALL                     1
    # 417          96 JUMP_IF_TRUE_OR_POP     41 (to 180)
    # 419          98 LOAD_FAST                0 (character)
    # 100 LOAD_METHOD              1 (get)
    # 122 LOAD_CONST               3 ('referenceImage')
    # 124 PRECALL                  1
    # 128 CALL                     1
    # 417         138 JUMP_IF_TRUE_OR_POP     20 (to 180)
    # 420         140 LOAD_FAST                0 (character)
    # 142 LOAD_METHOD              1 (get)
    # 164 LOAD_CONST               4 ('characterImage')
    # 166 PRECALL                  1
    # 170 CALL                     1
    # 416     >>  180 PRECALL                  1
    # 184 CALL                     1
    # 194 RETURN_VALUE
