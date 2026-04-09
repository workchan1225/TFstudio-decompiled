# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: app\config\paths.py

"""
Centralized path configuration for TFstudio
Handles both development and frozen (Nuitka/PyInstaller) modes

Data path resolution priority:
1. TFSTUDIO_DATA_PATH_OVERRIDE env var (debug/testing)
2. runtime_config.json configured path
3. Default %LOCALAPPDATA%/TFstudio/data
"""

import os
import sys
import logging
import shutil
from pathlib import Path

def get_base_path():
    """
    Get application base path (where exe/main.py is located)
    Result is cached for performance.

    Returns:
        Path: Root directory of the application
    """
    # 37           0 RESUME                   0
    # 46           2 LOAD_GLOBAL              0 (_cached_base_path)
    # 14 POP_JUMP_FORWARD_IF_NONE     7 (to 30)
    # 47          16 LOAD_GLOBAL              0 (_cached_base_path)
    # 28 RETURN_VALUE
    # 49     >>   30 LOAD_GLOBAL              2 (IS_FROZEN)
    # 42 POP_JUMP_FORWARD_IF_FALSE    85 (to 214)
    # 51          44 LOAD_GLOBAL              5 (NULL + Path)
    # 56 LOAD_GLOBAL              6 (sys)
    # 68 LOAD_ATTR                4 (executable)
    # 78 PRECALL                  1
    # 82 CALL                     1
    # 92 LOAD_METHOD              5 (resolve)
    # 114 PRECALL                  0
    # 118 CALL                     0
    # 128 STORE_FAST               0 (exe_path)
    # 52         130 LOAD_FAST                0 (exe_path)
    # 132 LOAD_ATTR                6 (parent)
    # 142 STORE_GLOBAL             0 (_cached_base_path)
    # 53         144 LOAD_GLOBAL             14 (_paths_logger)
    # 156 LOAD_METHOD              8 (info)
    # 178 LOAD_CONST               2 ('[Paths] EXE base_path (resolved): ')
    # 180 LOAD_GLOBAL              0 (_cached_base_path)
    # 192 FORMAT_VALUE             0
    # 194 BUILD_STRING             2
    # 196 PRECALL                  1
    # 200 CALL                     1
    # 210 POP_TOP
    # 212 JUMP_FORWARD            92 (to 398)
    # 57     >>  214 LOAD_GLOBAL              5 (NULL + Path)
    # 226 LOAD_GLOBAL             18 (__file__)
    # 238 PRECALL                  1
    # 242 CALL                     1
    # 252 LOAD_METHOD              5 (resolve)
    # 274 PRECALL                  0
    # 278 CALL                     0
    # 288 LOAD_ATTR                6 (parent)
    # 298 LOAD_ATTR                6 (parent)
    # 308 LOAD_ATTR                6 (parent)
    # 318 LOAD_ATTR                6 (parent)
    # 328 STORE_GLOBAL             0 (_cached_base_path)
    # 58         330 LOAD_GLOBAL             14 (_paths_logger)
    # 342 LOAD_METHOD             10 (debug)
    # 364 LOAD_CONST               3 ('[Paths] DEV base_path: ')
    # 366 LOAD_GLOBAL              0 (_cached_base_path)
    # 378 FORMAT_VALUE             0
    # 380 BUILD_STRING             2
    # 382 PRECALL                  1
    # 386 CALL                     1
    # 396 POP_TOP
    # 60     >>  398 LOAD_GLOBAL              0 (_cached_base_path)
    # 410 RETURN_VALUE

def get_backend_path():
    """
    Get backend directory path

    Returns:
        Path: Backend directory
    """
    # 63           0 RESUME                   0
    # 70           2 LOAD_GLOBAL              0 (IS_FROZEN)
    # 14 POP_JUMP_FORWARD_IF_FALSE    14 (to 44)
    # 72          16 LOAD_GLOBAL              3 (NULL + get_base_path)
    # 28 PRECALL                  0
    # 32 CALL                     0
    # 42 RETURN_VALUE
    # 73     >>   44 LOAD_GLOBAL              3 (NULL + get_base_path)
    # 56 PRECALL                  0
    # 60 CALL                     0
    # 70 LOAD_CONST               1 ('backend')
    # 72 BINARY_OP               11 (/)
    # 76 RETURN_VALUE

def get_static_path():
    """
    Get static files directory path

    Returns:
        Path: Static directory (fonts, etc.)
    """
    # 76           0 RESUME                   0
    # 83           2 LOAD_GLOBAL              0 (IS_FROZEN)
    # 14 POP_JUMP_FORWARD_IF_FALSE    17 (to 50)
    # 84          16 LOAD_GLOBAL              3 (NULL + get_base_path)
    # 28 PRECALL                  0
    # 32 CALL                     0
    # 42 LOAD_CONST               1 ('static')
    # 44 BINARY_OP               11 (/)
    # 48 RETURN_VALUE
    # 85     >>   50 LOAD_GLOBAL              5 (NULL + get_backend_path)
    # 62 PRECALL                  0
    # 66 CALL                     0
    # 76 LOAD_CONST               1 ('static')
    # 78 BINARY_OP               11 (/)
    # 82 RETURN_VALUE

def _dedupe_paths(paths):
    # 88           0 RESUME                   0
    # 89           2 BUILD_LIST               0
    # 4 STORE_FAST               1 (unique_paths)
    # 90           6 LOAD_GLOBAL              1 (NULL + set)
    # 18 PRECALL                  0
    # 22 CALL                     0
    # 32 STORE_FAST               2 (seen)
    # 91          34 LOAD_FAST                0 (paths)
    # 36 GET_ITER
    # >>   38 FOR_ITER                64 (to 168)
    # 40 STORE_FAST               3 (path)
    # 92          42 LOAD_GLOBAL              3 (NULL + str)
    # 54 LOAD_FAST                3 (path)
    # 56 PRECALL                  1
    # 60 CALL                     1
    # 70 STORE_FAST               4 (key)
    # 93          72 LOAD_FAST                4 (key)
    # 74 LOAD_FAST                2 (seen)
    # 76 CONTAINS_OP              0
    # 78 POP_JUMP_FORWARD_IF_FALSE     1 (to 82)
    # 94          80 JUMP_BACKWARD           22 (to 38)
    # 95     >>   82 LOAD_FAST                2 (seen)
    # 84 LOAD_METHOD              2 (add)
    # 106 LOAD_FAST                4 (key)
    # 108 PRECALL                  1
    # 112 CALL                     1
    # 122 POP_TOP
    # 96         124 LOAD_FAST                1 (unique_paths)
    # 126 LOAD_METHOD              3 (append)
    # 148 LOAD_FAST                3 (path)
    # 150 PRECALL                  1
    # 154 CALL                     1
    # 164 POP_TOP
    # 166 JUMP_BACKWARD           65 (to 38)
    # 97     >>  168 LOAD_FAST                1 (unique_paths)
    # 170 RETURN_VALUE

def _pick_existing_path(candidates):
    # 100           0 RESUME                   0
    # 101           2 LOAD_GLOBAL              1 (NULL + _dedupe_paths)
    # 14 LOAD_FAST                0 (candidates)
    # 16 PRECALL                  1
    # 20 CALL                     1
    # 30 STORE_FAST               1 (deduped)
    # 102          32 LOAD_FAST                1 (deduped)
    # 34 GET_ITER
    # >>   36 FOR_ITER                26 (to 90)
    # 38 STORE_FAST               2 (candidate)
    # 103          40 LOAD_FAST                2 (candidate)
    # 42 LOAD_METHOD              1 (exists)
    # 64 PRECALL                  0
    # 68 CALL                     0
    # 78 POP_JUMP_FORWARD_IF_FALSE     4 (to 88)
    # 104          80 LOAD_FAST                2 (candidate)
    # 82 SWAP                     2
    # 84 POP_TOP
    # 86 RETURN_VALUE
    # 103     >>   88 JUMP_BACKWARD           27 (to 36)
    # 105     >>   90 LOAD_FAST                1 (deduped)
    # 92 LOAD_CONST               1 (0)
    # 94 BINARY_SUBSCR
    # 104 RETURN_VALUE

def _resource_candidates():
    # 108           0 RESUME                   0
    # 109           2 LOAD_GLOBAL              1 (NULL + Path)
    # 14 LOAD_FAST                0 (relative_parts)
    # 16 CALL_FUNCTION_EX         0
    # 18 STORE_FAST               1 (relative_path)
    # 111          20 LOAD_GLOBAL              3 (NULL + get_backend_path)
    # 32 PRECALL                  0
    # 36 CALL                     0
    # 46 LOAD_FAST                1 (relative_path)
    # 48 BINARY_OP               11 (/)
    # 112          52 LOAD_GLOBAL              5 (NULL + get_base_path)
    # 64 PRECALL                  0
    # 68 CALL                     0
    # 78 LOAD_FAST                1 (relative_path)
    # 80 BINARY_OP               11 (/)
    # 110          84 BUILD_LIST               2
    # 86 STORE_FAST               2 (candidates)
    # 114          88 LOAD_GLOBAL              6 (IS_FROZEN)
    # 100 POP_JUMP_FORWARD_IF_FALSE    39 (to 180)
    # 115         102 LOAD_FAST                2 (candidates)
    # 104 LOAD_METHOD              4 (append)
    # 126 LOAD_GLOBAL              5 (NULL + get_base_path)
    # 138 PRECALL                  0
    # 142 CALL                     0
    # 152 LOAD_CONST               1 ('_internal')
    # 154 BINARY_OP               11 (/)
    # 158 LOAD_FAST                1 (relative_path)
    # 160 BINARY_OP               11 (/)
    # 164 PRECALL                  1
    # 168 CALL                     1
    # 178 POP_TOP
    # 116     >>  180 LOAD_GLOBAL             11 (NULL + _dedupe_paths)
    # 192 LOAD_FAST                2 (candidates)
    # 194 PRECALL                  1
    # 198 CALL                     1
    # 208 RETURN_VALUE

def get_default_appdata_path():
    """
    Get default AppData base path (always %LOCALAPPDATA%/TFstudio)

    This returns the default AppData path regardless of runtime_config settings.
    Used by components that should always use AppData (logs, chrome_profile, etc.)

    Returns:
        Path: Default AppData directory (%LOCALAPPDATA%/TFstudio or ~/.tfstudio)
    """
    # 119           0 RESUME                   0
    # 129           2 LOAD_GLOBAL              0 (os)
    # 14 LOAD_ATTR                1 (name)
    # 24 LOAD_CONST               1 ('nt')
    # 26 COMPARE_OP               2 (==)
    # 32 POP_JUMP_FORWARD_IF_FALSE    69 (to 172)
    # 130          34 LOAD_GLOBAL              1 (NULL + os)
    # 46 LOAD_ATTR                2 (getenv)
    # 56 LOAD_CONST               2 ('LOCALAPPDATA')
    # 58 LOAD_GLOBAL              0 (os)
    # 70 LOAD_ATTR                3 (path)
    # 80 LOAD_METHOD              4 (expanduser)
    # 102 LOAD_CONST               3 ('~')
    # 104 PRECALL                  1
    # 108 CALL                     1
    # 118 PRECALL                  2
    # 122 CALL                     2
    # 132 STORE_FAST               0 (localappdata)
    # 131         134 LOAD_GLOBAL             11 (NULL + Path)
    # 146 LOAD_FAST                0 (localappdata)
    # 148 PRECALL                  1
    # 152 CALL                     1
    # 162 LOAD_CONST               4 ('TFstudio')
    # 164 BINARY_OP               11 (/)
    # 168 STORE_FAST               1 (appdata_path)
    # 170 JUMP_FORWARD            22 (to 216)
    # 133     >>  172 LOAD_GLOBAL             11 (NULL + Path)
    # 184 LOAD_ATTR                6 (home)
    # 194 PRECALL                  0
    # 198 CALL                     0
    # 208 LOAD_CONST               5 ('.tfstudio')
    # 210 BINARY_OP               11 (/)
    # 214 STORE_FAST               1 (appdata_path)
    # 135     >>  216 LOAD_FAST                1 (appdata_path)
    # 218 LOAD_METHOD              7 (mkdir)
    # 240 LOAD_CONST               6 (True)
    # 242 LOAD_CONST               6 (True)
    # 244 KW_NAMES                 7
    # 246 PRECALL                  2
    # 250 CALL                     2
    # 260 POP_TOP
    # 136         262 LOAD_FAST                1 (appdata_path)
    # 264 RETURN_VALUE

def get_frontend_dist_path():
    """Get the packaged frontend dist directory."""
    # 139           0 RESUME                   0
    # 141           2 LOAD_GLOBAL              1 (NULL + get_base_path)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 ('frontend')
    # 30 BINARY_OP               11 (/)
    # 34 LOAD_CONST               2 ('dist')
    # 36 BINARY_OP               11 (/)
    # 40 RETURN_VALUE

def get_default_style_samples_path():
    """Get the read-only bundled default style samples directory."""
    # 144           0 RESUME                   0
    # 146           2 LOAD_GLOBAL              1 (NULL + get_static_path)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 ('default_style_samples')
    # 30 BINARY_OP               11 (/)
    # 34 RETURN_VALUE

def get_thumbnail_references_path():
    """Get the read-only bundled thumbnail references directory."""
    # 149           0 RESUME                   0
    # 151           2 LOAD_GLOBAL              1 (NULL + get_static_path)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 ('thumbnail_references')
    # 30 BINARY_OP               11 (/)
    # 34 RETURN_VALUE

def get_overlay_assets_path():
    """Get the read-only bundled overlay assets directory."""
    # 154           0 RESUME                   0
    # 156           2 LOAD_GLOBAL              1 (NULL + get_static_path)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 ('overlays')
    # 30 BINARY_OP               11 (/)
    # 34 RETURN_VALUE

def get_scene_data_path():
    """Get the bundled scene rules/data directory."""
    # 159           0 RESUME                   0
    # 161           2 LOAD_GLOBAL              1 (NULL + _pick_existing_path)
    # 14 LOAD_GLOBAL              3 (NULL + _resource_candidates)
    # 26 LOAD_CONST               1 ('app')
    # 28 LOAD_CONST               2 ('services')
    # 30 LOAD_CONST               3 ('scene')
    # 32 LOAD_CONST               4 ('data')
    # 34 PRECALL                  4
    # 38 CALL                     4
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 RETURN_VALUE

def get_assistant_data_path():
    """Get the bundled assistant data directory."""
    # 164           0 RESUME                   0
    # 166           2 LOAD_GLOBAL              1 (NULL + _pick_existing_path)
    # 14 LOAD_GLOBAL              3 (NULL + _resource_candidates)
    # 26 LOAD_CONST               1 ('app')
    # 28 LOAD_CONST               2 ('services')
    # 30 LOAD_CONST               3 ('assistant')
    # 32 LOAD_CONST               4 ('data')
    # 34 PRECALL                  4
    # 38 CALL                     4
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 RETURN_VALUE

def get_voice_metadata_path():
    """Get the bundled voice metadata JSON path."""
    # 169           0 RESUME                   0
    # 171           2 LOAD_GLOBAL              1 (NULL + _pick_existing_path)
    # 14 LOAD_GLOBAL              3 (NULL + _resource_candidates)
    # 26 LOAD_CONST               1 ('data')
    # 28 LOAD_CONST               2 ('voice_metadata.json')
    # 30 PRECALL                  2
    # 34 CALL                     2
    # 44 PRECALL                  1
    # 48 CALL                     1
    # 58 RETURN_VALUE

def get_supertonic_helper_path():
    """Get the bundled Supertonic helper.py path."""
    # 174           0 RESUME                   0
    # 176           2 LOAD_GLOBAL              1 (NULL + _pick_existing_path)
    # 177          14 LOAD_GLOBAL              3 (NULL + _resource_candidates)
    # 26 LOAD_CONST               1 ('supertonic-main')
    # 28 LOAD_CONST               1 ('supertonic-main')
    # 30 LOAD_CONST               1 ('supertonic-main')
    # 32 LOAD_CONST               2 ('py')
    # 34 LOAD_CONST               3 ('helper.py')
    # 36 PRECALL                  5
    # 40 CALL                     5
    # 178          50 LOAD_GLOBAL              3 (NULL + _resource_candidates)
    # 62 LOAD_CONST               1 ('supertonic-main')
    # 64 LOAD_CONST               2 ('py')
    # 66 LOAD_CONST               3 ('helper.py')
    # 68 PRECALL                  3
    # 72 CALL                     3
    # 177          82 BINARY_OP                0 (+)
    # 176          86 PRECALL                  1
    # 90 CALL                     1
    # 100 RETURN_VALUE

def get_supertonic_onnx_path():
    """Get the bundled Supertonic ONNX directory."""
    # 182           0 RESUME                   0
    # 184           2 LOAD_GLOBAL              1 (NULL + _pick_existing_path)
    # 185          14 LOAD_GLOBAL              3 (NULL + _resource_candidates)
    # 26 LOAD_CONST               1 ('supertonic-2')
    # 28 LOAD_CONST               2 ('onnx')
    # 30 PRECALL                  2
    # 34 CALL                     2
    # 186          44 LOAD_GLOBAL              3 (NULL + _resource_candidates)
    # 56 LOAD_CONST               3 ('Supertonic2TTS')
    # 58 LOAD_CONST               2 ('onnx')
    # 60 PRECALL                  2
    # 64 CALL                     2
    # 185          74 BINARY_OP                0 (+)
    # 184          78 PRECALL                  1
    # 82 CALL                     1
    # 92 RETURN_VALUE

def get_supertonic_voice_styles_path():
    """Get the bundled Supertonic voice styles directory."""
    # 190           0 RESUME                   0
    # 192           2 LOAD_GLOBAL              1 (NULL + _pick_existing_path)
    # 193          14 LOAD_GLOBAL              3 (NULL + _resource_candidates)
    # 26 LOAD_CONST               1 ('supertonic-2')
    # 28 LOAD_CONST               2 ('voice_styles')
    # 30 PRECALL                  2
    # 34 CALL                     2
    # 194          44 LOAD_GLOBAL              3 (NULL + _resource_candidates)
    # 56 LOAD_CONST               3 ('Supertonic2TTS')
    # 58 LOAD_CONST               2 ('voice_styles')
    # 60 PRECALL                  2
    # 64 CALL                     2
    # 193          74 BINARY_OP                0 (+)
    # 192          78 PRECALL                  1
    # 82 CALL                     1
    # 92 RETURN_VALUE

def get_data_path():
    """
    Get user data directory path

    Resolution priority:
    1. TFSTUDIO_DATA_PATH_OVERRIDE env var (debug/testing)
    2. runtime_config.json configured path
    3. Default %LOCALAPPDATA%/TFstudio/data

    This ensures consistency between development and EXE builds.
    Result is cached for performance.

    Returns:
        Path: User data directory
    """
    # 198           0 RESUME                   0
    # 216           2 LOAD_GLOBAL              0 (os)
    # 14 LOAD_ATTR                1 (environ)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_CONST               1 ('TFSTUDIO_DATA_PATH_OVERRIDE')
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               0 (data_path_env)
    # 217          64 LOAD_FAST                0 (data_path_env)
    # 66 POP_JUMP_FORWARD_IF_FALSE    71 (to 210)
    # 219          68 LOAD_GLOBAL              6 (_paths_logger)
    # 80 LOAD_METHOD              4 (warning)
    # 102 LOAD_CONST               2 ('[Paths] Using override path: ')
    # 104 LOAD_FAST                0 (data_path_env)
    # 106 FORMAT_VALUE             0
    # 108 BUILD_STRING             2
    # 110 PRECALL                  1
    # 114 CALL                     1
    # 124 POP_TOP
    # 220         126 LOAD_CONST               3 ('override')
    # 128 STORE_GLOBAL             5 (_data_path_source)
    # 221         130 LOAD_GLOBAL             13 (NULL + Path)
    # 142 LOAD_FAST                0 (data_path_env)
    # 144 PRECALL                  1
    # 148 CALL                     1
    # 158 STORE_FAST               1 (data_path)
    # 222         160 LOAD_FAST                1 (data_path)
    # 162 LOAD_METHOD              7 (mkdir)
    # 184 LOAD_CONST               4 (True)
    # 186 LOAD_CONST               4 (True)
    # 188 KW_NAMES                 5
    # 190 PRECALL                  2
    # 194 CALL                     2
    # 204 POP_TOP
    # 223         206 LOAD_FAST                1 (data_path)
    # 208 RETURN_VALUE
    # 226     >>  210 LOAD_GLOBAL             16 (_cached_data_path)
    # 222 POP_JUMP_FORWARD_IF_NONE     7 (to 238)
    # 227         224 LOAD_GLOBAL             16 (_cached_data_path)
    # 236 RETURN_VALUE
    # 230     >>  238 NOP
    # 231         240 LOAD_CONST               7 (0)
    # 242 LOAD_CONST               8 (('get_configured_data_path',))
    # 244 IMPORT_NAME              9 (app.config.runtime_config)
    # 246 IMPORT_FROM             10 (get_configured_data_path)
    # 248 STORE_FAST               2 (get_configured_data_path)
    # 250 POP_TOP
    # 232         252 PUSH_NULL
    # 254 LOAD_FAST                2 (get_configured_data_path)
    # 256 PRECALL                  0
    # 260 CALL                     0
    # 270 STORE_FAST               3 (configured_path)
    # 233         272 LOAD_FAST                3 (configured_path)
    # 274 POP_JUMP_FORWARD_IF_FALSE    68 (to 412)
    # 234         276 LOAD_FAST                3 (configured_path)
    # 278 STORE_GLOBAL             8 (_cached_data_path)
    # 235         280 LOAD_CONST               9 ('config')
    # 282 STORE_GLOBAL             5 (_data_path_source)
    # 236         284 LOAD_GLOBAL              6 (_paths_logger)
    # 296 LOAD_METHOD             11 (info)
    # 318 LOAD_CONST              10 ('[Paths] Using configured path: ')
    # 320 LOAD_FAST                3 (configured_path)
    # 322 FORMAT_VALUE             0
    # 324 BUILD_STRING             2
    # 326 PRECALL                  1
    # 330 CALL                     1
    # 340 POP_TOP
    # 237         342 LOAD_GLOBAL             16 (_cached_data_path)
    # 354 LOAD_METHOD              7 (mkdir)
    # 376 LOAD_CONST               4 (True)
    # 378 LOAD_CONST               4 (True)
    # 380 KW_NAMES                 5
    # 382 PRECALL                  2
    # 386 CALL                     2
    # 396 POP_TOP
    # 238         398 LOAD_GLOBAL             16 (_cached_data_path)
    # 410 RETURN_VALUE
    # 233     >>  412 JUMP_FORWARD            42 (to 498)
    # >>  414 PUSH_EXC_INFO
    # 239         416 LOAD_GLOBAL             24 (ImportError)
    # 428 CHECK_EXC_MATCH
    # 430 POP_JUMP_FORWARD_IF_FALSE    29 (to 490)
    # 432 POP_TOP
    # 240         434 LOAD_GLOBAL              6 (_paths_logger)
    # 446 LOAD_METHOD             13 (debug)
    # 468 LOAD_CONST              11 ('[Paths] runtime_config not available, using default')
    # 470 PRECALL                  1
    # 474 CALL                     1
    # 484 POP_TOP
    # 486 POP_EXCEPT
    # 488 JUMP_FORWARD             4 (to 498)
    # 239     >>  490 RERAISE                  0
    # >>  492 COPY                     3
    # 494 POP_EXCEPT
    # 496 RERAISE                  1
    # 245     >>  498 LOAD_GLOBAL              0 (os)
    # 510 LOAD_ATTR               14 (name)
    # 520 LOAD_CONST              12 ('nt')
    # 522 COMPARE_OP               2 (==)
    # 528 POP_JUMP_FORWARD_IF_FALSE    72 (to 674)
    # 246         530 LOAD_GLOBAL              1 (NULL + os)
    # 542 LOAD_ATTR               15 (getenv)
    # 552 LOAD_CONST              13 ('LOCALAPPDATA')
    # 554 LOAD_GLOBAL              0 (os)
    # 566 LOAD_ATTR               16 (path)
    # 576 LOAD_METHOD             17 (expanduser)
    # 598 LOAD_CONST              14 ('~')
    # 600 PRECALL                  1
    # 604 CALL                     1
    # 614 PRECALL                  2
    # 618 CALL                     2
    # 628 STORE_FAST               4 (localappdata)
    # 247         630 LOAD_GLOBAL             13 (NULL + Path)
    # 642 LOAD_FAST                4 (localappdata)
    # 644 PRECALL                  1
    # 648 CALL                     1
    # 658 LOAD_CONST              15 ('TFstudio')
    # 660 BINARY_OP               11 (/)
    # 664 LOAD_CONST              16 ('data')
    # 666 BINARY_OP               11 (/)
    # 670 STORE_GLOBAL             8 (_cached_data_path)
    # 672 JUMP_FORWARD            25 (to 724)
    # 249     >>  674 LOAD_GLOBAL             13 (NULL + Path)
    # 686 LOAD_ATTR               18 (home)
    # 696 PRECALL                  0
    # 700 CALL                     0
    # 710 LOAD_CONST              17 ('.tfstudio')
    # 712 BINARY_OP               11 (/)
    # 716 LOAD_CONST              16 ('data')
    # 718 BINARY_OP               11 (/)
    # 722 STORE_GLOBAL             8 (_cached_data_path)
    # 251     >>  724 LOAD_CONST              18 ('default')
    # 726 STORE_GLOBAL             5 (_data_path_source)
    # 252         728 LOAD_GLOBAL              6 (_paths_logger)
    # 740 LOAD_METHOD             11 (info)
    # 762 LOAD_CONST              19 ('[Paths] Using default path: ')
    # 764 LOAD_GLOBAL             16 (_cached_data_path)
    # 776 FORMAT_VALUE             0
    # 778 BUILD_STRING             2
    # 780 PRECALL                  1
    # 784 CALL                     1
    # 794 POP_TOP
    # 255         796 LOAD_GLOBAL             16 (_cached_data_path)
    # 808 LOAD_METHOD              7 (mkdir)
    # 830 LOAD_CONST               4 (True)
    # 832 LOAD_CONST               4 (True)
    # 834 KW_NAMES                 5
    # 836 PRECALL                  2
    # 840 CALL                     2
    # 850 POP_TOP
    # 256         852 LOAD_GLOBAL             16 (_cached_data_path)
    # 864 RETURN_VALUE
    # ExceptionTable:
    # 240 to 408 -> 414 [0]
    # 414 to 484 -> 492 [1] lasti
    # 490 to 490 -> 492 [1] lasti

def reset_data_path_cache():
    """
    Reset the cached data path.
    Call this when the data path configuration changes and a restart is pending.
    """
    # 259           0 RESUME                   0
    # 265           2 LOAD_CONST               1 (None)
    # 4 STORE_GLOBAL             0 (_cached_data_path)
    # 266           6 LOAD_CONST               2 ('default')
    # 8 STORE_GLOBAL             1 (_data_path_source)
    # 267          10 LOAD_GLOBAL              4 (_paths_logger)
    # 22 LOAD_METHOD              3 (info)
    # 44 LOAD_CONST               3 ('[Paths] Data path cache reset')
    # 46 PRECALL                  1
    # 50 CALL                     1
    # 60 POP_TOP
    # 62 LOAD_CONST               1 (None)
    # 64 RETURN_VALUE

def get_data_path_source():
    """
    Get the source of the current data path configuration

    Returns:
        str: 'override', 'config', or 'default'
    """
    # 270           0 RESUME                   0
    # 277           2 LOAD_GLOBAL              0 (_data_path_source)
    # 14 RETURN_VALUE

def get_database_path():
    """
    Get SQLite database absolute path

    Returns:
        Path: Database file path
    """
    # 280           0 RESUME                   0
    # 288           2 LOAD_GLOBAL              1 (NULL + get_data_path)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 ('database')
    # 30 BINARY_OP               11 (/)
    # 34 STORE_FAST               0 (db_dir)
    # 289          36 LOAD_FAST                0 (db_dir)
    # 38 LOAD_METHOD              1 (mkdir)
    # 60 LOAD_CONST               2 (True)
    # 62 LOAD_CONST               2 (True)
    # 64 KW_NAMES                 3
    # 66 PRECALL                  2
    # 70 CALL                     2
    # 80 POP_TOP
    # 290          82 LOAD_FAST                0 (db_dir)
    # 84 LOAD_CONST               4 ('tfstudio.db')
    # 86 BINARY_OP               11 (/)
    # 90 RETURN_VALUE

def get_database_url():
    """
    Get SQLAlchemy database URL with absolute path

    Returns:
        str: SQLAlchemy-compatible database URL
    """
    # 293           0 RESUME                   0
    # 300           2 LOAD_GLOBAL              1 (NULL + get_database_path)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 STORE_FAST               0 (db_path)
    # 303          30 LOAD_GLOBAL              3 (NULL + str)
    # 42 LOAD_FAST                0 (db_path)
    # 44 PRECALL                  1
    # 48 CALL                     1
    # 58 LOAD_METHOD              2 (replace)
    # 80 LOAD_CONST               1 ('\\')
    # 82 LOAD_CONST               2 ('/')
    # 84 PRECALL                  2
    # 88 CALL                     2
    # 98 STORE_FAST               1 (path_str)
    # 304         100 LOAD_CONST               3 ('sqlite:///')
    # 102 LOAD_FAST                1 (path_str)
    # 104 FORMAT_VALUE             0
    # 106 BUILD_STRING             2
    # 108 RETURN_VALUE

def get_projects_path():
    """
    Get projects directory path

    Returns:
        Path: Projects directory
    """
    # 307           0 RESUME                   0
    # 314           2 LOAD_GLOBAL              1 (NULL + get_data_path)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 ('projects')
    # 30 BINARY_OP               11 (/)
    # 34 STORE_FAST               0 (projects_path)
    # 315          36 LOAD_FAST                0 (projects_path)
    # 38 LOAD_METHOD              1 (mkdir)
    # 60 LOAD_CONST               2 (True)
    # 62 LOAD_CONST               2 (True)
    # 64 KW_NAMES                 3
    # 66 PRECALL                  2
    # 70 CALL                     2
    # 80 POP_TOP
    # 316          82 LOAD_FAST                0 (projects_path)
    # 84 RETURN_VALUE

def get_outputs_path():
    """
    Get outputs directory path

    Returns:
        Path: Outputs directory for rendered videos
    """
    # 319           0 RESUME                   0
    # 326           2 LOAD_GLOBAL              1 (NULL + get_data_path)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 ('outputs')
    # 30 BINARY_OP               11 (/)
    # 34 STORE_FAST               0 (outputs_path)
    # 327          36 LOAD_FAST                0 (outputs_path)
    # 38 LOAD_METHOD              1 (mkdir)
    # 60 LOAD_CONST               2 (True)
    # 62 LOAD_CONST               2 (True)
    # 64 KW_NAMES                 3
    # 66 PRECALL                  2
    # 70 CALL                     2
    # 80 POP_TOP
    # 328          82 LOAD_FAST                0 (outputs_path)
    # 84 RETURN_VALUE

def get_temp_path():
    """
    Get temporary files directory path

    Returns:
        Path: Temp directory
    """
    # 331           0 RESUME                   0
    # 338           2 LOAD_GLOBAL              1 (NULL + get_data_path)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 ('temp')
    # 30 BINARY_OP               11 (/)
    # 34 STORE_FAST               0 (temp_path)
    # 339          36 LOAD_FAST                0 (temp_path)
    # 38 LOAD_METHOD              1 (mkdir)
    # 60 LOAD_CONST               2 (True)
    # 62 LOAD_CONST               2 (True)
    # 64 KW_NAMES                 3
    # 66 PRECALL                  2
    # 70 CALL                     2
    # 80 POP_TOP
    # 340          82 LOAD_FAST                0 (temp_path)
    # 84 RETURN_VALUE

def get_fonts_path():
    """
    Get fonts directory path

    Returns:
        Path: Fonts directory
    """
    # 343           0 RESUME                   0
    # 350           2 LOAD_GLOBAL              1 (NULL + get_static_path)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 ('fonts')
    # 30 BINARY_OP               11 (/)
    # 34 RETURN_VALUE

def get_bundled_ffmpeg_path():
    """Get the bundled FFmpeg executable path."""
    # 353           0 RESUME                   0
    # 355           2 LOAD_GLOBAL              1 (NULL + get_base_path)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 ('bin')
    # 30 BINARY_OP               11 (/)
    # 34 LOAD_CONST               2 ('ffmpeg')
    # 36 BINARY_OP               11 (/)
    # 40 LOAD_CONST               3 ('ffmpeg.exe')
    # 42 BINARY_OP               11 (/)
    # 46 RETURN_VALUE

def get_bundled_ffprobe_path():
    """Get the bundled FFprobe executable path."""
    # 358           0 RESUME                   0
    # 360           2 LOAD_GLOBAL              1 (NULL + get_base_path)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 ('bin')
    # 30 BINARY_OP               11 (/)
    # 34 LOAD_CONST               2 ('ffmpeg')
    # 36 BINARY_OP               11 (/)
    # 40 LOAD_CONST               3 ('ffprobe.exe')
    # 42 BINARY_OP               11 (/)
    # 46 RETURN_VALUE

def resolve_runtime_binary_path(binary_name, bundled_path):
    """
    Resolve a runtime binary path with EXE-safe rules.

    Returns:
        tuple[Path, str]: (resolved path, source) where source is bundled or system
    """
    # 363           0 RESUME                   0
    # 370           2 LOAD_FAST                1 (bundled_path)
    # 4 LOAD_METHOD              0 (exists)
    # 26 PRECALL                  0
    # 30 CALL                     0
    # 40 POP_JUMP_FORWARD_IF_FALSE     4 (to 50)
    # 371          42 LOAD_FAST                1 (bundled_path)
    # 44 LOAD_CONST               1 ('bundled')
    # 46 BUILD_TUPLE              2
    # 48 RETURN_VALUE
    # 373     >>   50 LOAD_GLOBAL              2 (IS_FROZEN)
    # 62 POP_JUMP_FORWARD_IF_TRUE    39 (to 142)
    # 374          64 LOAD_GLOBAL              5 (NULL + shutil)
    # 76 LOAD_ATTR                3 (which)
    # 86 LOAD_FAST                0 (binary_name)
    # 88 PRECALL                  1
    # 92 CALL                     1
    # 102 STORE_FAST               2 (system_path)
    # 375         104 LOAD_FAST                2 (system_path)
    # 106 POP_JUMP_FORWARD_IF_FALSE    17 (to 142)
    # 376         108 LOAD_GLOBAL              9 (NULL + Path)
    # 120 LOAD_FAST                2 (system_path)
    # 122 PRECALL                  1
    # 126 CALL                     1
    # 136 LOAD_CONST               2 ('system')
    # 138 BUILD_TUPLE              2
    # 140 RETURN_VALUE
    # 378     >>  142 LOAD_GLOBAL             11 (NULL + str)
    # 154 LOAD_FAST                1 (bundled_path)
    # 156 PRECALL                  1
    # 160 CALL                     1
    # 170 LOAD_METHOD              6 (replace)
    # 192 LOAD_CONST               3 ('\\')
    # 194 LOAD_CONST               4 ('/')
    # 196 PRECALL                  2
    # 200 CALL                     2
    # 210 STORE_FAST               3 (normalized_bundled)
    # 379         212 LOAD_GLOBAL              2 (IS_FROZEN)
    # 224 POP_JUMP_FORWARD_IF_FALSE    21 (to 268)
    # 380         226 LOAD_GLOBAL             15 (NULL + FileNotFoundError)
    # 381         238 LOAD_CONST               5 ('Bundled ')
    # 240 LOAD_FAST                0 (binary_name)
    # 242 FORMAT_VALUE             0
    # 244 LOAD_CONST               6 (' is missing at ')
    # 246 LOAD_FAST                3 (normalized_bundled)
    # 248 FORMAT_VALUE             0
    # 250 BUILD_STRING             4
    # 380         252 PRECALL                  1
    # 256 CALL                     1
    # 266 RAISE_VARARGS            1
    # 384     >>  268 LOAD_GLOBAL             15 (NULL + FileNotFoundError)
    # 385         280 LOAD_FAST                0 (binary_name)
    # 282 FORMAT_VALUE             0
    # 284 LOAD_CONST               7 (' executable not found. Expected bundled binary at ')
    # 386         286 LOAD_FAST                3 (normalized_bundled)
    # 385         288 FORMAT_VALUE             0
    # 290 LOAD_CONST               8 (' or a system PATH entry.')
    # 292 BUILD_STRING             4
    # 384         294 PRECALL                  1
    # 298 CALL                     1
    # 308 RAISE_VARARGS            1

def get_ffmpeg_path():
    """
    Get the resolved FFmpeg executable path.

    Returns:
        Path: FFmpeg executable path
    """
    # 390           0 RESUME                   0
    # 397           2 LOAD_GLOBAL              1 (NULL + resolve_runtime_binary_path)
    # 14 LOAD_CONST               1 ('ffmpeg')
    # 16 LOAD_GLOBAL              3 (NULL + get_bundled_ffmpeg_path)
    # 28 PRECALL                  0
    # 32 CALL                     0
    # 42 PRECALL                  2
    # 46 CALL                     2
    # 56 UNPACK_SEQUENCE          2
    # 60 STORE_FAST               0 (resolved_path)
    # 62 STORE_FAST               1 (_)
    # 398          64 LOAD_FAST                0 (resolved_path)
    # 66 RETURN_VALUE

def get_ffprobe_path():
    """
    Get the resolved FFprobe executable path.

    Returns:
        Path: FFprobe executable path
    """
    # 401           0 RESUME                   0
    # 408           2 LOAD_GLOBAL              1 (NULL + resolve_runtime_binary_path)
    # 14 LOAD_CONST               1 ('ffprobe')
    # 16 LOAD_GLOBAL              3 (NULL + get_bundled_ffprobe_path)
    # 28 PRECALL                  0
    # 32 CALL                     0
    # 42 PRECALL                  2
    # 46 CALL                     2
    # 56 UNPACK_SEQUENCE          2
    # 60 STORE_FAST               0 (resolved_path)
    # 62 STORE_FAST               1 (_)
    # 409          64 LOAD_FAST                0 (resolved_path)
    # 66 RETURN_VALUE

def get_user_style_samples_path():
    """
    Get style samples directory path (for all style template images)
    Both default and user-generated images are stored here.

    Location: %LOCALAPPDATA%/TFstudio/data/style_samples/

    Returns:
        Path: Style samples directory
    """
    # 412           0 RESUME                   0
    # 422           2 LOAD_GLOBAL              1 (NULL + get_data_path)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 ('style_samples')
    # 30 BINARY_OP               11 (/)
    # 34 STORE_FAST               0 (samples_path)
    # 423          36 LOAD_FAST                0 (samples_path)
    # 38 LOAD_METHOD              1 (mkdir)
    # 60 LOAD_CONST               2 (True)
    # 62 LOAD_CONST               2 (True)
    # 64 KW_NAMES                 3
    # 66 PRECALL                  2
    # 70 CALL                     2
    # 80 POP_TOP
    # 424          82 LOAD_FAST                0 (samples_path)
    # 84 RETURN_VALUE

def get_custom_style_templates_dir():
    """
    Get custom style templates directory path.

    Location: %LOCALAPPDATA%/TFstudio/data/style_templates/custom/

    Returns:
        Path: Custom style templates directory
    """
    # 427           0 RESUME                   0
    # 436           2 LOAD_GLOBAL              1 (NULL + get_data_path)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 ('style_templates')
    # 30 BINARY_OP               11 (/)
    # 34 LOAD_CONST               2 ('custom')
    # 36 BINARY_OP               11 (/)
    # 40 STORE_FAST               0 (templates_dir)
    # 437          42 LOAD_FAST                0 (templates_dir)
    # 44 LOAD_METHOD              1 (mkdir)
    # 66 LOAD_CONST               3 (True)
    # 68 LOAD_CONST               3 (True)
    # 70 KW_NAMES                 4
    # 72 PRECALL                  2
    # 76 CALL                     2
    # 86 POP_TOP
    # 438          88 LOAD_FAST                0 (templates_dir)
    # 90 RETURN_VALUE

def get_custom_style_templates_manifest_path():
    """
    Get custom style templates manifest file path.

    Returns:
        Path: JSON manifest path for custom style templates
    """
    # 441           0 RESUME                   0
    # 448           2 LOAD_GLOBAL              1 (NULL + get_custom_style_templates_dir)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 ('custom_style_templates.json')
    # 30 BINARY_OP               11 (/)
    # 34 RETURN_VALUE

def get_custom_thumbnail_references_dir():
    """
    Get custom thumbnail references directory path.
    User-added YouTube thumbnail references are stored here.

    Location: %LOCALAPPDATA%/TFstudio/data/thumbnail_references/custom/

    Returns:
        Path: Custom thumbnail references directory
    """
    # 451           0 RESUME                   0
    # 461           2 LOAD_GLOBAL              1 (NULL + get_data_path)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 ('thumbnail_references')
    # 30 BINARY_OP               11 (/)
    # 34 LOAD_CONST               2 ('custom')
    # 36 BINARY_OP               11 (/)
    # 40 STORE_FAST               0 (refs_dir)
    # 462          42 LOAD_FAST                0 (refs_dir)
    # 44 LOAD_METHOD              1 (mkdir)
    # 66 LOAD_CONST               3 (True)
    # 68 LOAD_CONST               3 (True)
    # 70 KW_NAMES                 4
    # 72 PRECALL                  2
    # 76 CALL                     2
    # 86 POP_TOP
    # 463          88 LOAD_FAST                0 (refs_dir)
    # 90 RETURN_VALUE

def get_custom_thumbnail_references_manifest_path():
    """
    Get custom thumbnail references manifest file path.

    Returns:
        Path: JSON manifest path for custom thumbnail references
    """
    # 466           0 RESUME                   0
    # 473           2 LOAD_GLOBAL              1 (NULL + get_custom_thumbnail_references_dir)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 ('custom_references.json')
    # 30 BINARY_OP               11 (/)
    # 34 RETURN_VALUE

def get_sfx_library_path():
    """
    Get SFX library directory path (공통 효과음 라이브러리)
    업로드된 효과음이 저장되어 모든 프로젝트에서 재사용 가능

    Location: %LOCALAPPDATA%/TFstudio/data/sfx_library/

    Returns:
        Path: SFX library directory
    """
    # 476           0 RESUME                   0
    # 486           2 LOAD_GLOBAL              1 (NULL + get_data_path)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 ('sfx_library')
    # 30 BINARY_OP               11 (/)
    # 34 STORE_FAST               0 (sfx_path)
    # 487          36 LOAD_FAST                0 (sfx_path)
    # 38 LOAD_METHOD              1 (mkdir)
    # 60 LOAD_CONST               2 (True)
    # 62 LOAD_CONST               2 (True)
    # 64 KW_NAMES                 3
    # 66 PRECALL                  2
    # 70 CALL                     2
    # 80 POP_TOP
    # 488          82 LOAD_FAST                0 (sfx_path)
    # 84 RETURN_VALUE

def get_overlay_library_path():
    """
    Get overlay library directory path (오버레이 에셋 라이브러리)
    빌트인 및 사용자 업로드 오버레이 저장

    Location: %LOCALAPPDATA%/TFstudio/data/overlay_library/

    Returns:
        Path: Overlay library directory
    """
    # 491           0 RESUME                   0
    # 501           2 LOAD_GLOBAL              1 (NULL + get_data_path)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 ('overlay_library')
    # 30 BINARY_OP               11 (/)
    # 34 STORE_FAST               0 (overlay_path)
    # 502          36 LOAD_FAST                0 (overlay_path)
    # 38 LOAD_METHOD              1 (mkdir)
    # 60 LOAD_CONST               2 (True)
    # 62 LOAD_CONST               2 (True)
    # 64 KW_NAMES                 3
    # 66 PRECALL                  2
    # 70 CALL                     2
    # 80 POP_TOP
    # 503          82 LOAD_FAST                0 (overlay_path)
    # 84 RETURN_VALUE

def normalize_path(path):
    """
    Normalize path for cross-platform compatibility
    Always uses forward slashes for consistency

    Args:
        path: Path string to normalize

    Returns:
        str: Normalized path with forward slashes
    """
    # 506           0 RESUME                   0
    # 517           2 LOAD_FAST                0 (path)
    # 4 LOAD_METHOD              0 (replace)
    # 26 LOAD_CONST               1 ('\\')
    # 28 LOAD_CONST               2 ('/')
    # 30 PRECALL                  2
    # 34 CALL                     2
    # 44 RETURN_VALUE

def get_env_path():
    """
    Get .env file path

    - Development: backend/.env
    - EXE (Frozen): %LOCALAPPDATA%/TFstudio/.env (권한 문제 방지)

    Note: EXE 환경에서는 Program Files 대신 LocalAppData를 사용하여
    관리자 권한 없이도 .env 파일을 읽고 쓸 수 있습니다.

    Returns:
        Path: .env file path
    """
    # 520           0 RESUME                   0
    # 533           2 LOAD_GLOBAL              0 (IS_FROZEN)
    # 14 POP_JUMP_FORWARD_IF_FALSE   135 (to 286)
    # 535          16 LOAD_GLOBAL              2 (os)
    # 28 LOAD_ATTR                2 (name)
    # 38 LOAD_CONST               1 ('nt')
    # 40 COMPARE_OP               2 (==)
    # 46 POP_JUMP_FORWARD_IF_FALSE    69 (to 186)
    # 536          48 LOAD_GLOBAL              3 (NULL + os)
    # 60 LOAD_ATTR                3 (getenv)
    # 70 LOAD_CONST               2 ('LOCALAPPDATA')
    # 72 LOAD_GLOBAL              2 (os)
    # 84 LOAD_ATTR                4 (path)
    # 94 LOAD_METHOD              5 (expanduser)
    # 116 LOAD_CONST               3 ('~')
    # 118 PRECALL                  1
    # 122 CALL                     1
    # 132 PRECALL                  2
    # 136 CALL                     2
    # 146 STORE_FAST               0 (localappdata)
    # 537         148 LOAD_GLOBAL             13 (NULL + Path)
    # 160 LOAD_FAST                0 (localappdata)
    # 162 PRECALL                  1
    # 166 CALL                     1
    # 176 LOAD_CONST               4 ('TFstudio')
    # 178 BINARY_OP               11 (/)
    # 182 STORE_FAST               1 (env_dir)
    # 184 JUMP_FORWARD            22 (to 230)
    # 539     >>  186 LOAD_GLOBAL             13 (NULL + Path)
    # 198 LOAD_ATTR                7 (home)
    # 208 PRECALL                  0
    # 212 CALL                     0
    # 222 LOAD_CONST               5 ('.tfstudio')
    # 224 BINARY_OP               11 (/)
    # 228 STORE_FAST               1 (env_dir)
    # 540     >>  230 LOAD_FAST                1 (env_dir)
    # 232 LOAD_METHOD              8 (mkdir)
    # 254 LOAD_CONST               6 (True)
    # 256 LOAD_CONST               6 (True)
    # 258 KW_NAMES                 7
    # 260 PRECALL                  2
    # 264 CALL                     2
    # 274 POP_TOP
    # 541         276 LOAD_FAST                1 (env_dir)
    # 278 LOAD_CONST               8 ('.env')
    # 280 BINARY_OP               11 (/)
    # 284 RETURN_VALUE
    # 544     >>  286 LOAD_GLOBAL             19 (NULL + get_backend_path)
    # 298 PRECALL                  0
    # 302 CALL                     0
    # 312 LOAD_CONST               8 ('.env')
    # 314 BINARY_OP               11 (/)
    # 318 RETURN_VALUE

def get_relative_data_path(absolute_path):
    """
    Convert absolute path to relative path from data directory

    Args:
        absolute_path: Absolute file path

    Returns:
        str: Relative path from data directory
    """
    # 547           0 RESUME                   0
    # 557           2 LOAD_GLOBAL              1 (NULL + str)
    # 14 LOAD_GLOBAL              3 (NULL + get_data_path)
    # 26 PRECALL                  0
    # 30 CALL                     0
    # 40 PRECALL                  1
    # 44 CALL                     1
    # 54 LOAD_METHOD              2 (replace)
    # 76 LOAD_CONST               1 ('\\')
    # 78 LOAD_CONST               2 ('/')
    # 80 PRECALL                  2
    # 84 CALL                     2
    # 94 STORE_FAST               1 (data_path)
    # 558          96 LOAD_FAST                0 (absolute_path)
    # 98 LOAD_METHOD              2 (replace)
    # 120 LOAD_CONST               1 ('\\')
    # 122 LOAD_CONST               2 ('/')
    # 124 PRECALL                  2
    # 128 CALL                     2
    # 138 STORE_FAST               2 (abs_path)
    # 560         140 LOAD_FAST                2 (abs_path)
    # 142 LOAD_METHOD              3 (startswith)
    # 164 LOAD_FAST                1 (data_path)
    # 166 PRECALL                  1
    # 170 CALL                     1
    # 180 POP_JUMP_FORWARD_IF_FALSE    42 (to 266)
    # 561         182 LOAD_FAST                2 (abs_path)
    # 184 LOAD_GLOBAL              9 (NULL + len)
    # 196 LOAD_FAST                1 (data_path)
    # 198 PRECALL                  1
    # 202 CALL                     1
    # 212 LOAD_CONST               3 (None)
    # 214 BUILD_SLICE              2
    # 216 BINARY_SUBSCR
    # 226 LOAD_METHOD              5 (lstrip)
    # 248 LOAD_CONST               2 ('/')
    # 250 PRECALL                  1
    # 254 CALL                     1
    # 264 RETURN_VALUE
    # 562     >>  266 LOAD_FAST                2 (abs_path)
    # 268 RETURN_VALUE
