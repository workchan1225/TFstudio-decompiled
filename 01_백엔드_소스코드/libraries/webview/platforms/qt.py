# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: webview\platforms\qt.py

import json
import logging
import os
import platform
import signal
import socket
import sys
import webbrowser
from copy import copy
from functools import partial
from threading import Event
from uuid import uuid1
from webview import FileDialog
from webview.dom import _dnd_state
from webview.menu import Menu
from webview.models import Request
from webview.screen import Screen
from webview.util import DEFAULT_HTML
from webview.window import FixPoint
from qtpy import QtCore
from qtpy import PYQT6
from qtpy.QtCore import QByteArray
from qtpy.QtGui import QColor
from qtpy.QtWidgets import QAction
from qtpy.QtNetwork import QSslCertificate
from qtpy.QtWebChannel import QWebChannel
from qtpy.QtWebEngineCore import QWebEngineUrlRequestInterceptor
from qtpy.QtWebEngineWidgets import QWebEnginePage
from qtpy.QtWebEngineWidgets import QWebEngineProfile
from qtpy.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtNetwork import QSslCertificate
from PyQt5.QtWebKitWidgets import QWebPage

def _sigint_handler(signum, frame):
    """
    Handler for SIGINT signal (Ctrl+C).

    Qt applications don't handle SIGINT by default because Python signal handlers
    can only be called when the Python interpreter is running. Since the Qt event
    loop runs in C++, signals are noted but handlers aren't called until Python
    code executes. The timer in create_window() ensures the Python interpreter
    runs periodically to process pending signals.

    See: https://stackoverflow.com/a/4939113
    """
    # 79           0 RESUME                   0
    # 92           2 LOAD_GLOBAL              0 (_app)
    # 14 POP_JUMP_FORWARD_IF_FALSE    27 (to 70)
    # 93          16 LOAD_GLOBAL              0 (_app)
    # 28 LOAD_METHOD              1 (quit)
    # 50 PRECALL                  0
    # 54 CALL                     0
    # 64 POP_TOP
    # 66 LOAD_CONST               1 (None)
    # 68 RETURN_VALUE
    # 92     >>   70 LOAD_CONST               1 (None)
    # 72 RETURN_VALUE

class BrowserView:
    """BrowserView"""
    def JSBridge():
        """BrowserView.JSBridge"""
        # 0 MAKE_CELL                0 (__class__)
        # 122           2 RESUME                   0
        # 4 LOAD_NAME                0 (__name__)
        # 6 STORE_NAME               1 (__module__)
        # 8 LOAD_CONST               0 ('BrowserView.JSBridge')
        # 10 STORE_NAME               2 (__qualname__)
        # 123          12 LOAD_NAME                3 (is_webengine)
        # 14 POP_JUMP_FORWARD_IF_FALSE     7 (to 30)
        # 16 LOAD_NAME                4 (QtCore)
        # 18 LOAD_ATTR                5 (QJsonValue)
        # 28 JUMP_FORWARD             1 (to 32)
        # >>   30 LOAD_NAME                6 (str)
        # >>   32 STORE_NAME               7 (qtype)
        # 125          34 LOAD_CLOSURE             0 (__class__)
        # 36 BUILD_TUPLE              1
        # 38 LOAD_CONST               1 (<code object __init__ at 0x000001EBD77ECF30, file "webview\platforms\qt.py", line 125>)
        # 40 MAKE_FUNCTION            8 (closure)
        # 42 STORE_NAME               8 (__init__)
        # 130          44 PUSH_NULL
        # 46 LOAD_NAME                4 (QtCore)
        # 48 LOAD_ATTR                9 (Slot)
        # 58 LOAD_NAME                6 (str)
        # 60 LOAD_NAME                7 (qtype)
        # 62 LOAD_NAME                6 (str)
        # 64 LOAD_NAME                6 (str)
        # 66 KW_NAMES                 2
        # 68 PRECALL                  4
        # 72 CALL                     4
        # 131          82 LOAD_CONST               3 (<code object call at 0x000001EBD70D2790, file "webview\platforms\qt.py", line 130>)
        # 84 MAKE_FUNCTION            0
        # 130          86 PRECALL                  0
        # 90 CALL                     0
        # 131         100 STORE_NAME              10 (call)
        # 102 LOAD_CLOSURE             0 (__class__)
        # 104 COPY                     1
        # 106 STORE_NAME              11 (__classcell__)
        # 108 RETURN_VALUE
        # Disassembly of <code object __init__ at 0x000001EBD77ECF30, file "webview\platforms\qt.py", line 125>:
        # 0 COPY_FREE_VARS           1
        # 125           2 RESUME                   0
        # 126           4 LOAD_GLOBAL              1 (NULL + super)
        # 16 LOAD_GLOBAL              2 (BrowserView)
        # 28 LOAD_ATTR                2 (JSBridge)
        # 38 LOAD_FAST                0 (self)
        # 40 PRECALL                  2
        # 44 CALL                     2
        # 54 LOAD_METHOD              3 (__init__)
        # 76 PRECALL                  0
        # 80 CALL                     0
        # 90 POP_TOP
        # 127          92 LOAD_FAST                1 (parent)
        # 94 LOAD_FAST                0 (self)
        # 96 STORE_ATTR               4 (parent)
        # 128         106 LOAD_FAST                1 (parent)
        # 108 LOAD_ATTR                5 (pywebview_window)
        # 118 LOAD_FAST                0 (self)
        # 120 STORE_ATTR               6 (window)
        # 130 LOAD_CONST               0 (None)
        # 132 RETURN_VALUE
        # Disassembly of <code object call at 0x000001EBD70D2790, file "webview\platforms\qt.py", line 130>:
        # 130           0 RESUME                   0
        # 132           2 LOAD_GLOBAL              0 (BrowserView)
        # 14 LOAD_METHOD              1 (_convert_string)
        # 36 LOAD_FAST                1 (func_name)
        # 38 PRECALL                  1
        # 42 CALL                     1
        # 52 STORE_FAST               1 (func_name)
        # 133          54 LOAD_GLOBAL              0 (BrowserView)
        # 66 LOAD_METHOD              1 (_convert_string)
        # 88 LOAD_FAST                2 (param)
        # 90 PRECALL                  1
        # 94 CALL                     1
        # 104 STORE_FAST               2 (param)
        # 135         106 LOAD_FAST                1 (func_name)
        # 108 LOAD_CONST               1 ('_pywebviewAlert')
        # 110 COMPARE_OP               2 (==)
        # 116 POP_JUMP_FORWARD_IF_FALSE    42 (to 202)
        # 136         118 LOAD_GLOBAL              5 (NULL + QMessageBox)
        # 130 LOAD_ATTR                3 (information)
        # 140 LOAD_FAST                0 (self)
        # 142 LOAD_ATTR                4 (parent)
        # 152 LOAD_CONST               2 ('Message')
        # 154 LOAD_GLOBAL             11 (NULL + str)
        # 166 LOAD_FAST                2 (param)
        # 168 PRECALL                  1
        # 172 CALL                     1
        # 182 PRECALL                  3
        # 186 CALL                     3
        # 196 POP_TOP
        # 198 LOAD_CONST               0 (None)
        # 200 RETURN_VALUE
        # 138     >>  202 LOAD_GLOBAL             13 (NULL + js_bridge_call)
        # 214 LOAD_FAST                0 (self)
        # 216 LOAD_ATTR                7 (window)
        # 226 LOAD_FAST                1 (func_name)
        # 228 LOAD_GLOBAL             17 (NULL + json)
        # 240 LOAD_ATTR                9 (loads)
        # 250 LOAD_FAST                2 (param)
        # 252 PRECALL                  1
        # 256 CALL                     1
        # 266 LOAD_FAST                3 (value_id)
        # 268 PRECALL                  4
        # 272 CALL                     4
        # 282 RETURN_VALUE

    def WebView():
        """BrowserView.WebView"""
        # 0 MAKE_CELL                0 (__class__)
        # 140           2 RESUME                   0
        # 4 LOAD_NAME                0 (__name__)
        # 6 STORE_NAME               1 (__module__)
        # 8 LOAD_CONST               0 ('BrowserView.WebView')
        # 10 STORE_NAME               2 (__qualname__)
        # 141          12 LOAD_CONST              11 ((None,))
        # 14 LOAD_CLOSURE             0 (__class__)
        # 16 BUILD_TUPLE              1
        # 18 LOAD_CONST               2 (<code object __init__ at 0x000001EBD777ED20, file "webview\platforms\qt.py", line 141>)
        # 20 MAKE_FUNCTION            9 (defaults, closure)
        # 22 STORE_NAME               3 (__init__)
        # 154          24 LOAD_CONST               3 (<code object contextMenuEvent at 0x000001EBD6FDC900, file "webview\platforms\qt.py", line 154>)
        # 26 MAKE_FUNCTION            0
        # 28 STORE_NAME               4 (contextMenuEvent)
        # 174          30 LOAD_CLOSURE             0 (__class__)
        # 32 BUILD_TUPLE              1
        # 34 LOAD_CONST               4 (<code object dragEnterEvent at 0x000001EBD733B030, file "webview\platforms\qt.py", line 174>)
        # 36 MAKE_FUNCTION            8 (closure)
        # 38 STORE_NAME               5 (dragEnterEvent)
        # 180          40 LOAD_CLOSURE             0 (__class__)
        # 42 BUILD_TUPLE              1
        # 44 LOAD_CONST               5 (<code object dragMoveEvent at 0x000001EBD733B930, file "webview\platforms\qt.py", line 180>)
        # 46 MAKE_FUNCTION            8 (closure)
        # 48 STORE_NAME               6 (dragMoveEvent)
        # 186          50 LOAD_CLOSURE             0 (__class__)
        # 52 BUILD_TUPLE              1
        # 54 LOAD_CONST               6 (<code object dropEvent at 0x000001EBD70D21F0, file "webview\platforms\qt.py", line 186>)
        # 56 MAKE_FUNCTION            8 (closure)
        # 58 STORE_NAME               7 (dropEvent)
        # 198          60 LOAD_CONST               7 (<code object show_inspector at 0x000001EBD7628DE0, file "webview\platforms\qt.py", line 198>)
        # 62 MAKE_FUNCTION            0
        # 64 STORE_NAME               8 (show_inspector)
        # 213          66 LOAD_CONST               8 (<code object mousePressEvent at 0x000001EBD70D25B0, file "webview\platforms\qt.py", line 213>)
        # 68 MAKE_FUNCTION            0
        # 70 STORE_NAME               9 (mousePressEvent)
        # 219          72 LOAD_CONST               9 (<code object mouseMoveEvent at 0x000001EBD7102DC0, file "webview\platforms\qt.py", line 219>)
        # 74 MAKE_FUNCTION            0
        # 76 STORE_NAME              10 (mouseMoveEvent)
        # 226          78 LOAD_CONST              10 (<code object eventFilter at 0x000001EBD70D2970, file "webview\platforms\qt.py", line 226>)
        # 80 MAKE_FUNCTION            0
        # 82 STORE_NAME              11 (eventFilter)
        # 84 LOAD_CLOSURE             0 (__class__)
        # 86 COPY                     1
        # 88 STORE_NAME              12 (__classcell__)
        # 90 RETURN_VALUE
        # Disassembly of <code object __init__ at 0x000001EBD777ED20, file "webview\platforms\qt.py", line 141>:
        # 0 COPY_FREE_VARS           1
        # 141           2 RESUME                   0
        # 142           4 LOAD_GLOBAL              1 (NULL + super)
        # 16 LOAD_GLOBAL              2 (BrowserView)
        # 28 LOAD_ATTR                2 (WebView)
        # 38 LOAD_FAST                0 (self)
        # 40 PRECALL                  2
        # 44 CALL                     2
        # 54 LOAD_METHOD              3 (__init__)
        # 76 LOAD_FAST                1 (parent)
        # 78 PRECALL                  1
        # 82 CALL                     1
        # 92 POP_TOP
        # 144          94 LOAD_FAST                1 (parent)
        # 96 LOAD_ATTR                4 (frameless)
        # 106 POP_JUMP_FORWARD_IF_FALSE    66 (to 240)
        # 108 LOAD_FAST                1 (parent)
        # 110 LOAD_ATTR                5 (easy_drag)
        # 120 POP_JUMP_FORWARD_IF_FALSE    59 (to 240)
        # 145         122 LOAD_GLOBAL             13 (NULL + QApplication)
        # 134 LOAD_ATTR                7 (instance)
        # 144 PRECALL                  0
        # 148 CALL                     0
        # 158 LOAD_METHOD              8 (installEventFilter)
        # 180 LOAD_FAST                0 (self)
        # 182 PRECALL                  1
        # 186 CALL                     1
        # 196 POP_TOP
        # 146         198 LOAD_FAST                0 (self)
        # 200 LOAD_METHOD              9 (setMouseTracking)
        # 222 LOAD_CONST               1 (True)
        # 224 PRECALL                  1
        # 228 CALL                     1
        # 238 POP_TOP
        # 148     >>  240 LOAD_FAST                1 (parent)
        # 242 LOAD_ATTR               10 (transparent)
        # 252 LOAD_FAST                0 (self)
        # 254 STORE_ATTR              10 (transparent)
        # 149         264 LOAD_FAST                1 (parent)
        # 266 LOAD_ATTR               10 (transparent)
        # 276 POP_JUMP_FORWARD_IF_FALSE    96 (to 470)
        # 150         278 LOAD_FAST                0 (self)
        # 280 LOAD_METHOD             11 (setAttribute)
        # 302 LOAD_GLOBAL             24 (QtCore)
        # 314 LOAD_ATTR               13 (Qt)
        # 324 LOAD_ATTR               14 (WA_TranslucentBackground)
        # 334 PRECALL                  1
        # 338 CALL                     1
        # 348 POP_TOP
        # 151         350 LOAD_FAST                0 (self)
        # 352 LOAD_METHOD             11 (setAttribute)
        # 374 LOAD_GLOBAL             24 (QtCore)
        # 386 LOAD_ATTR               13 (Qt)
        # 396 LOAD_ATTR               15 (WA_OpaquePaintEvent)
        # 406 LOAD_CONST               2 (False)
        # 408 PRECALL                  2
        # 412 CALL                     2
        # 422 POP_TOP
        # 152         424 LOAD_FAST                0 (self)
        # 426 LOAD_METHOD             16 (setStyleSheet)
        # 448 LOAD_CONST               3 ('background: transparent;')
        # 450 PRECALL                  1
        # 454 CALL                     1
        # 464 POP_TOP
        # 466 LOAD_CONST               0 (None)
        # 468 RETURN_VALUE
        # 149     >>  470 LOAD_CONST               0 (None)
        # 472 RETURN_VALUE
        # Disassembly of <code object contextMenuEvent at 0x000001EBD6FDC900, file "webview\platforms\qt.py", line 154>:
        # 154           0 RESUME                   0
        # 155           2 LOAD_GLOBAL              0 (_qt6)
        # 14 POP_JUMP_FORWARD_IF_FALSE    21 (to 58)
        # 156          16 LOAD_FAST                0 (self)
        # 18 LOAD_METHOD              1 (createStandardContextMenu)
        # 40 PRECALL                  0
        # 44 CALL                     0
        # 54 STORE_FAST               2 (menu)
        # 56 JUMP_FORWARD            38 (to 134)
        # 158     >>   58 LOAD_FAST                0 (self)
        # 60 LOAD_METHOD              2 (page)
        # 82 PRECALL                  0
        # 86 CALL                     0
        # 96 LOAD_METHOD              1 (createStandardContextMenu)
        # 118 PRECALL                  0
        # 122 CALL                     0
        # 132 STORE_FAST               2 (menu)
        # 162     >>  134 LOAD_FAST                2 (menu)
        # 136 LOAD_METHOD              3 (actions)
        # 158 PRECALL                  0
        # 162 CALL                     0
        # 172 GET_ITER
        # >>  174 FOR_ITER                28 (to 232)
        # 176 STORE_FAST               3 (i)
        # 163         178 LOAD_FAST                3 (i)
        # 180 LOAD_METHOD              4 (text)
        # 202 PRECALL                  0
        # 206 CALL                     0
        # 216 LOAD_CONST               1 ('Inspect Element')
        # 218 COMPARE_OP               2 (==)
        # 224 POP_JUMP_FORWARD_IF_FALSE     2 (to 230)
        # 164         226 POP_TOP
        # 228 JUMP_FORWARD            69 (to 368)
        # 163     >>  230 JUMP_BACKWARD           29 (to 174)
        # 168     >>  232 LOAD_GLOBAL             11 (NULL + QAction)
        # 244 LOAD_CONST               1 ('Inspect Element')
        # 246 LOAD_FAST                2 (menu)
        # 248 PRECALL                  2
        # 252 CALL                     2
        # 262 STORE_FAST               4 (inspect_element)
        # 169         264 LOAD_FAST                4 (inspect_element)
        # 266 LOAD_ATTR                6 (triggered)
        # 276 LOAD_METHOD              7 (connect)
        # 298 LOAD_FAST                0 (self)
        # 300 LOAD_ATTR                8 (show_inspector)
        # 310 PRECALL                  1
        # 314 CALL                     1
        # 324 POP_TOP
        # 170         326 LOAD_FAST                2 (menu)
        # 328 LOAD_METHOD              9 (addAction)
        # 350 LOAD_FAST                4 (inspect_element)
        # 352 PRECALL                  1
        # 356 CALL                     1
        # 366 POP_TOP
        # 172     >>  368 LOAD_FAST                2 (menu)
        # 370 LOAD_METHOD             10 (exec_)
        # 392 LOAD_FAST                1 (event)
        # 394 LOAD_METHOD             11 (globalPos)
        # 416 PRECALL                  0
        # 420 CALL                     0
        # 430 PRECALL                  1
        # 434 CALL                     1
        # 444 POP_TOP
        # 446 LOAD_CONST               0 (None)
        # 448 RETURN_VALUE
        # Disassembly of <code object dragEnterEvent at 0x000001EBD733B030, file "webview\platforms\qt.py", line 174>:
        # 0 COPY_FREE_VARS           1
        # 174           2 RESUME                   0
        # 175           4 LOAD_FAST                1 (e)
        # 6 LOAD_METHOD              0 (mimeData)
        # 28 PRECALL                  0
        # 32 CALL                     0
        # 42 LOAD_ATTR                1 (hasUrls)
        # 52 POP_JUMP_FORWARD_IF_FALSE    37 (to 128)
        # 54 LOAD_GLOBAL              4 (_dnd_state)
        # 66 LOAD_CONST               1 ('num_listeners')
        # 68 BINARY_SUBSCR
        # 78 LOAD_CONST               2 (0)
        # 80 COMPARE_OP               4 (>)
        # 86 POP_JUMP_FORWARD_IF_FALSE    20 (to 128)
        # 176          88 LOAD_FAST                1 (e)
        # 90 LOAD_METHOD              3 (acceptProposedAction)
        # 112 PRECALL                  0
        # 116 CALL                     0
        # 126 POP_TOP
        # 178     >>  128 LOAD_GLOBAL              9 (NULL + super)
        # 140 PRECALL                  0
        # 144 CALL                     0
        # 154 LOAD_METHOD              5 (dragEnterEvent)
        # 176 LOAD_FAST                1 (e)
        # 178 PRECALL                  1
        # 182 CALL                     1
        # 192 RETURN_VALUE
        # Disassembly of <code object dragMoveEvent at 0x000001EBD733B930, file "webview\platforms\qt.py", line 180>:
        # 0 COPY_FREE_VARS           1
        # 180           2 RESUME                   0
        # 181           4 LOAD_FAST                1 (e)
        # 6 LOAD_METHOD              0 (mimeData)
        # 28 PRECALL                  0
        # 32 CALL                     0
        # 42 LOAD_ATTR                1 (hasUrls)
        # 52 POP_JUMP_FORWARD_IF_FALSE    37 (to 128)
        # 54 LOAD_GLOBAL              4 (_dnd_state)
        # 66 LOAD_CONST               1 ('num_listeners')
        # 68 BINARY_SUBSCR
        # 78 LOAD_CONST               2 (0)
        # 80 COMPARE_OP               4 (>)
        # 86 POP_JUMP_FORWARD_IF_FALSE    20 (to 128)
        # 182          88 LOAD_FAST                1 (e)
        # 90 LOAD_METHOD              3 (acceptProposedAction)
        # 112 PRECALL                  0
        # 116 CALL                     0
        # 126 POP_TOP
        # 184     >>  128 LOAD_GLOBAL              9 (NULL + super)
        # 140 PRECALL                  0
        # 144 CALL                     0
        # 154 LOAD_METHOD              5 (dragMoveEvent)
        # 176 LOAD_FAST                1 (e)
        # 178 PRECALL                  1
        # 182 CALL                     1
        # 192 RETURN_VALUE
        # Disassembly of <code object dropEvent at 0x000001EBD70D21F0, file "webview\platforms\qt.py", line 186>:
        # 0 COPY_FREE_VARS           1
        # 186           2 RESUME                   0
        # 187           4 LOAD_FAST                1 (e)
        # 6 LOAD_METHOD              0 (mimeData)
        # 28 PRECALL                  0
        # 32 CALL                     0
        # 42 LOAD_ATTR                1 (hasUrls)
        # 52 POP_JUMP_FORWARD_IF_FALSE    86 (to 226)
        # 54 LOAD_GLOBAL              4 (_dnd_state)
        # 66 LOAD_CONST               1 ('num_listeners')
        # 68 BINARY_SUBSCR
        # 78 LOAD_CONST               2 (0)
        # 80 COMPARE_OP               4 (>)
        # 86 POP_JUMP_FORWARD_IF_FALSE    69 (to 226)
        # 188          88 LOAD_CONST               3 (<code object <listcomp> at 0x000001EBD73260D0, file "webview\platforms\qt.py", line 188>)
        # 90 MAKE_FUNCTION            0
        # 190          92 LOAD_FAST                1 (e)
        # 94 LOAD_METHOD              0 (mimeData)
        # 116 PRECALL                  0
        # 120 CALL                     0
        # 130 LOAD_METHOD              3 (urls)
        # 152 PRECALL                  0
        # 156 CALL                     0
        # 188         166 GET_ITER
        # 168 PRECALL                  0
        # 172 CALL                     0
        # 182 STORE_FAST               2 (files)
        # 193         184 LOAD_GLOBAL              4 (_dnd_state)
        # 196 LOAD_CONST               4 ('paths')
        # 198 COPY                     2
        # 200 COPY                     2
        # 202 BINARY_SUBSCR
        # 212 LOAD_FAST                2 (files)
        # 214 BINARY_OP               13 (+=)
        # 218 SWAP                     3
        # 220 SWAP                     2
        # 222 STORE_SUBSCR
        # 195     >>  226 LOAD_GLOBAL              9 (NULL + super)
        # 238 PRECALL                  0
        # 242 CALL                     0
        # 252 LOAD_METHOD              5 (dropEvent)
        # 274 LOAD_FAST                1 (e)
        # 276 PRECALL                  1
        # 280 CALL                     1
        # 290 RETURN_VALUE
        # Disassembly of <code object <listcomp> at 0x000001EBD73260D0, file "webview\platforms\qt.py", line 188>:
        # 188           0 RESUME                   0
        # 2 BUILD_LIST               0
        # 4 LOAD_FAST                0 (.0)
        # >>    6 FOR_ITER               130 (to 268)
        # 190           8 STORE_FAST               1 (value)
        # 191          10 LOAD_FAST                1 (value)
        # 12 LOAD_METHOD              0 (toString)
        # 34 PRECALL                  0
        # 38 CALL                     0
        # 48 LOAD_METHOD              1 (startswith)
        # 70 LOAD_CONST               0 ('file://')
        # 72 PRECALL                  1
        # 76 CALL                     1
        # 188          86 POP_JUMP_BACKWARD_IF_FALSE    41 (to 6)
        # 189          88 LOAD_GLOBAL              4 (os)
        # 100 LOAD_ATTR                3 (path)
        # 110 LOAD_METHOD              4 (basename)
        # 132 LOAD_FAST                1 (value)
        # 134 LOAD_METHOD              0 (toString)
        # 156 PRECALL                  0
        # 160 CALL                     0
        # 170 PRECALL                  1
        # 174 CALL                     1
        # 184 LOAD_FAST                1 (value)
        # 186 LOAD_METHOD              0 (toString)
        # 208 PRECALL                  0
        # 212 CALL                     0
        # 222 LOAD_METHOD              5 (replace)
        # 244 LOAD_CONST               0 ('file://')
        # 246 LOAD_CONST               1 ('')
        # 248 PRECALL                  2
        # 252 CALL                     2
        # 262 BUILD_TUPLE              2
        # 188         264 LIST_APPEND              2
        # 266 JUMP_BACKWARD          131 (to 6)
        # >>  268 RETURN_VALUE
        # Disassembly of <code object show_inspector at 0x000001EBD7628DE0, file "webview\platforms\qt.py", line 198>:
        # 198           0 RESUME                   0
        # 199           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (parent)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 LOAD_ATTR                1 (uid)
        # 50 LOAD_CONST               1 ('-inspector')
        # 52 BINARY_OP                0 (+)
        # 56 STORE_FAST               1 (uid)
        # 200          58 NOP
        # 202          60 LOAD_GLOBAL              4 (BrowserView)
        # 72 LOAD_ATTR                3 (instances)
        # 82 LOAD_FAST                1 (uid)
        # 84 BINARY_SUBSCR
        # 94 LOAD_METHOD              4 (raise_)
        # 116 PRECALL                  0
        # 120 CALL                     0
        # 130 POP_TOP
        # 203         132 LOAD_GLOBAL              4 (BrowserView)
        # 144 LOAD_ATTR                3 (instances)
        # 154 LOAD_FAST                1 (uid)
        # 156 BINARY_SUBSCR
        # 166 LOAD_METHOD              5 (activateWindow)
        # 188 PRECALL                  0
        # 192 CALL                     0
        # 202 POP_TOP
        # 204 LOAD_CONST               0 (None)
        # 206 RETURN_VALUE
        # >>  208 PUSH_EXC_INFO
        # 204         210 LOAD_GLOBAL             12 (KeyError)
        # 222 CHECK_EXC_MATCH
        # 224 POP_JUMP_FORWARD_IF_FALSE   132 (to 490)
        # 226 POP_TOP
        # 205         228 LOAD_CONST               2 ('Web Inspector - ')
        # 230 LOAD_FAST                0 (self)
        # 232 LOAD_METHOD              0 (parent)
        # 254 PRECALL                  0
        # 258 CALL                     0
        # 268 LOAD_ATTR                7 (title)
        # 278 FORMAT_VALUE             0
        # 280 BUILD_STRING             2
        # 282 STORE_FAST               2 (title)
        # 206         284 LOAD_CONST               3 ('http://localhost:')
        # 286 LOAD_GLOBAL              4 (BrowserView)
        # 298 LOAD_ATTR                8 (inspector_port)
        # 308 FORMAT_VALUE             0
        # 310 BUILD_STRING             2
        # 312 STORE_FAST               3 (url)
        # 207         314 LOAD_GLOBAL             19 (NULL + Window)
        # 326 LOAD_CONST               4 ('web_inspector')
        # 328 LOAD_FAST                2 (title)
        # 330 LOAD_FAST                3 (url)
        # 332 LOAD_CONST               5 ('')
        # 334 LOAD_CONST               6 (700)
        # 336 LOAD_CONST               7 (500)
        # 338 PRECALL                  6
        # 342 CALL                     6
        # 352 STORE_FAST               4 (window)
        # 208         354 LOAD_FAST                0 (self)
        # 356 LOAD_METHOD              0 (parent)
        # 378 PRECALL                  0
        # 382 CALL                     0
        # 392 LOAD_ATTR               10 (localization)
        # 402 LOAD_FAST                4 (window)
        # 404 STORE_ATTR              10 (localization)
        # 210         414 LOAD_GLOBAL              5 (NULL + BrowserView)
        # 426 LOAD_FAST                4 (window)
        # 428 PRECALL                  1
        # 432 CALL                     1
        # 442 STORE_FAST               5 (inspector)
        # 211         444 LOAD_FAST                5 (inspector)
        # 446 LOAD_METHOD             11 (show)
        # 468 PRECALL                  0
        # 472 CALL                     0
        # 482 POP_TOP
        # 484 POP_EXCEPT
        # 486 LOAD_CONST               0 (None)
        # 488 RETURN_VALUE
        # 204     >>  490 RERAISE                  0
        # >>  492 COPY                     3
        # 494 POP_EXCEPT
        # 496 RERAISE                  1
        # ExceptionTable:
        # 60 to 202 -> 208 [0]
        # 208 to 482 -> 492 [1] lasti
        # 490 to 490 -> 492 [1] lasti
        # Disassembly of <code object mousePressEvent at 0x000001EBD70D25B0, file "webview\platforms\qt.py", line 213>:
        # 213           0 RESUME                   0
        # 214           2 LOAD_FAST                1 (event)
        # 4 LOAD_METHOD              0 (button)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 LOAD_GLOBAL              2 (QtCore)
        # 52 LOAD_ATTR                2 (Qt)
        # 62 LOAD_ATTR                3 (LeftButton)
        # 72 COMPARE_OP               2 (==)
        # 78 POP_JUMP_FORWARD_IF_FALSE    82 (to 244)
        # 215          80 LOAD_FAST                1 (event)
        # 82 LOAD_METHOD              4 (globalPos)
        # 104 PRECALL                  0
        # 108 CALL                     0
        # 118 LOAD_FAST                0 (self)
        # 120 LOAD_METHOD              5 (parent)
        # 142 PRECALL                  0
        # 146 CALL                     0
        # 156 LOAD_METHOD              6 (frameGeometry)
        # 178 PRECALL                  0
        # 182 CALL                     0
        # 192 LOAD_METHOD              7 (topLeft)
        # 214 PRECALL                  0
        # 218 CALL                     0
        # 228 BINARY_OP               10 (-)
        # 232 LOAD_FAST                0 (self)
        # 234 STORE_ATTR               8 (drag_pos)
        # 217     >>  244 LOAD_FAST                1 (event)
        # 246 LOAD_METHOD              9 (accept)
        # 268 PRECALL                  0
        # 272 CALL                     0
        # 282 POP_TOP
        # 284 LOAD_CONST               0 (None)
        # 286 RETURN_VALUE
        # Disassembly of <code object mouseMoveEvent at 0x000001EBD7102DC0, file "webview\platforms\qt.py", line 219>:
        # 219           0 RESUME                   0
        # 220           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (parent)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 STORE_FAST               2 (parent)
        # 222          42 LOAD_FAST                2 (parent)
        # 44 LOAD_ATTR                1 (frameless)
        # 221          54 POP_JUMP_FORWARD_IF_FALSE    85 (to 226)
        # 222          56 LOAD_FAST                2 (parent)
        # 58 LOAD_ATTR                2 (easy_drag)
        # 221          68 POP_JUMP_FORWARD_IF_FALSE    80 (to 230)
        # 222          70 LOAD_FAST                1 (event)
        # 72 LOAD_METHOD              3 (buttons)
        # 94 PRECALL                  0
        # 98 CALL                     0
        # 108 LOAD_ATTR                4 (value)
        # 118 LOAD_CONST               1 (1)
        # 120 COMPARE_OP               2 (==)
        # 126 POP_JUMP_FORWARD_IF_FALSE    53 (to 234)
        # 224         128 LOAD_FAST                2 (parent)
        # 130 LOAD_METHOD              5 (move)
        # 152 LOAD_FAST                1 (event)
        # 154 LOAD_METHOD              6 (globalPos)
        # 176 PRECALL                  0
        # 180 CALL                     0
        # 190 LOAD_FAST                0 (self)
        # 192 LOAD_ATTR                7 (drag_pos)
        # 202 BINARY_OP               10 (-)
        # 206 PRECALL                  1
        # 210 CALL                     1
        # 220 POP_TOP
        # 222 LOAD_CONST               0 (None)
        # 224 RETURN_VALUE
        # 221     >>  226 LOAD_CONST               0 (None)
        # 228 RETURN_VALUE
        # >>  230 LOAD_CONST               0 (None)
        # 232 RETURN_VALUE
        # 222     >>  234 LOAD_CONST               0 (None)
        # 236 RETURN_VALUE
        # Disassembly of <code object eventFilter at 0x000001EBD70D2970, file "webview\platforms\qt.py", line 226>:
        # 226           0 RESUME                   0
        # 227           2 LOAD_FAST                1 (object)
        # 4 LOAD_METHOD              0 (parent)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 LOAD_FAST                0 (self)
        # 42 COMPARE_OP               2 (==)
        # 48 POP_JUMP_FORWARD_IF_FALSE   121 (to 292)
        # 228          50 LOAD_FAST                2 (event)
        # 52 LOAD_METHOD              1 (type)
        # 74 PRECALL                  0
        # 78 CALL                     0
        # 88 LOAD_GLOBAL              4 (QtCore)
        # 100 LOAD_ATTR                3 (QEvent)
        # 110 LOAD_ATTR                4 (MouseMove)
        # 120 COMPARE_OP               2 (==)
        # 126 POP_JUMP_FORWARD_IF_FALSE    22 (to 172)
        # 229         128 LOAD_FAST                0 (self)
        # 130 LOAD_METHOD              5 (mouseMoveEvent)
        # 152 LOAD_FAST                2 (event)
        # 154 PRECALL                  1
        # 158 CALL                     1
        # 168 POP_TOP
        # 170 JUMP_FORWARD            60 (to 292)
        # 230     >>  172 LOAD_FAST                2 (event)
        # 174 LOAD_METHOD              1 (type)
        # 196 PRECALL                  0
        # 200 CALL                     0
        # 210 LOAD_GLOBAL              4 (QtCore)
        # 222 LOAD_ATTR                3 (QEvent)
        # 232 LOAD_ATTR                6 (MouseButtonPress)
        # 242 COMPARE_OP               2 (==)
        # 248 POP_JUMP_FORWARD_IF_FALSE    21 (to 292)
        # 231         250 LOAD_FAST                0 (self)
        # 252 LOAD_METHOD              7 (mousePressEvent)
        # 274 LOAD_FAST                2 (event)
        # 276 PRECALL                  1
        # 280 CALL                     1
        # 290 POP_TOP
        # 233     >>  292 LOAD_CONST               1 (False)
        # 294 RETURN_VALUE

    def RequestInterceptor():
        """BrowserView.RequestInterceptor"""
        # 0 MAKE_CELL                0 (__class__)
        # 235           2 RESUME                   0
        # 4 LOAD_NAME                0 (__name__)
        # 6 STORE_NAME               1 (__module__)
        # 8 LOAD_CONST               0 ('BrowserView.RequestInterceptor')
        # 10 STORE_NAME               2 (__qualname__)
        # 236          12 LOAD_CLOSURE             0 (__class__)
        # 14 BUILD_TUPLE              1
        # 16 LOAD_CONST               1 (<code object __init__ at 0x000001EBD7E45CE0, file "webview\platforms\qt.py", line 236>)
        # 18 MAKE_FUNCTION            8 (closure)
        # 20 STORE_NAME               3 (__init__)
        # 240          22 LOAD_CONST               2 (<code object interceptRequest at 0x000001EBD75B56E0, file "webview\platforms\qt.py", line 240>)
        # 24 MAKE_FUNCTION            0
        # 26 STORE_NAME               4 (interceptRequest)
        # 28 LOAD_CLOSURE             0 (__class__)
        # 30 COPY                     1
        # 32 STORE_NAME               5 (__classcell__)
        # 34 RETURN_VALUE
        # Disassembly of <code object __init__ at 0x000001EBD7E45CE0, file "webview\platforms\qt.py", line 236>:
        # 0 COPY_FREE_VARS           1
        # 236           2 RESUME                   0
        # 237           4 LOAD_GLOBAL              1 (NULL + super)
        # 16 PRECALL                  0
        # 20 CALL                     0
        # 30 LOAD_METHOD              1 (__init__)
        # 52 PRECALL                  0
        # 56 CALL                     0
        # 66 POP_TOP
        # 238          68 LOAD_FAST                1 (window)
        # 70 LOAD_FAST                0 (self)
        # 72 STORE_ATTR               2 (window)
        # 82 LOAD_CONST               0 (None)
        # 84 RETURN_VALUE
        # Disassembly of <code object interceptRequest at 0x000001EBD75B56E0, file "webview\platforms\qt.py", line 240>:
        # 240           0 RESUME                   0
        # 241           2 LOAD_GLOBAL              1 (NULL + len)
        # 14 LOAD_FAST                0 (self)
        # 16 LOAD_ATTR                1 (window)
        # 26 LOAD_ATTR                2 (events)
        # 36 LOAD_ATTR                3 (request_sent)
        # 46 PRECALL                  1
        # 50 CALL                     1
        # 60 LOAD_CONST               1 (0)
        # 62 COMPARE_OP               2 (==)
        # 68 POP_JUMP_FORWARD_IF_FALSE     2 (to 74)
        # 242          70 LOAD_CONST               0 (None)
        # 72 RETURN_VALUE
        # 244     >>   74 LOAD_FAST                1 (info)
        # 76 LOAD_METHOD              4 (requestUrl)
        # 98 PRECALL                  0
        # 102 CALL                     0
        # 112 LOAD_METHOD              5 (toString)
        # 134 PRECALL                  0
        # 138 CALL                     0
        # 148 STORE_FAST               2 (url)
        # 245         150 LOAD_FAST                1 (info)
        # 152 LOAD_METHOD              6 (requestMethod)
        # 174 PRECALL                  0
        # 178 CALL                     0
        # 188 STORE_FAST               3 (method)
        # 247         190 LOAD_CONST               2 ('httpHeaders')
        # 192 LOAD_GLOBAL             15 (NULL + dir)
        # 204 LOAD_FAST                1 (info)
        # 206 PRECALL                  1
        # 210 CALL                     1
        # 220 CONTAINS_OP              0
        # 222 POP_JUMP_FORWARD_IF_FALSE    49 (to 322)
        # 248         224 LOAD_CONST               3 (<code object <dictcomp> at 0x000001EBD7107280, file "webview\platforms\qt.py", line 248>)
        # 226 MAKE_FUNCTION            0
        # 250         228 LOAD_FAST                1 (info)
        # 230 LOAD_METHOD              8 (httpHeaders)
        # 252 PRECALL                  0
        # 256 CALL                     0
        # 266 LOAD_METHOD              9 (items)
        # 288 PRECALL                  0
        # 292 CALL                     0
        # 248         302 GET_ITER
        # 304 PRECALL                  0
        # 308 CALL                     0
        # 318 STORE_FAST               4 (headers)
        # 320 JUMP_FORWARD             2 (to 326)
        # 253     >>  322 BUILD_MAP                0
        # 324 STORE_FAST               4 (headers)
        # 255     >>  326 LOAD_GLOBAL             21 (NULL + Request)
        # 338 LOAD_FAST                2 (url)
        # 340 LOAD_FAST                3 (method)
        # 342 LOAD_FAST                4 (headers)
        # 344 PRECALL                  3
        # 348 CALL                     3
        # 358 STORE_FAST               5 (request)
        # 256         360 LOAD_FAST                0 (self)
        # 362 LOAD_ATTR                1 (window)
        # 372 LOAD_ATTR                2 (events)
        # 382 LOAD_ATTR                3 (request_sent)
        # 392 LOAD_METHOD             11 (set)
        # 414 LOAD_FAST                5 (request)
        # 416 PRECALL                  1
        # 420 CALL                     1
        # 430 POP_TOP
        # 258         432 LOAD_FAST                5 (request)
        # 434 LOAD_ATTR               12 (headers)
        # 444 LOAD_FAST                4 (headers)
        # 446 COMPARE_OP               3 (!=)
        # 452 POP_JUMP_FORWARD_IF_FALSE   117 (to 688)
        # 259         454 LOAD_FAST                5 (request)
        # 456 LOAD_ATTR               12 (headers)
        # 466 LOAD_METHOD              9 (items)
        # 488 PRECALL                  0
        # 492 CALL                     0
        # 502 GET_ITER
        # >>  504 FOR_ITER                93 (to 692)
        # 506 UNPACK_SEQUENCE          2
        # 510 STORE_FAST               6 (key)
        # 512 STORE_FAST               7 (value)
        # 260         514 LOAD_FAST                1 (info)
        # 516 LOAD_METHOD             13 (setHttpHeader)
        # 261         538 LOAD_GLOBAL             29 (NULL + QByteArray)
        # 550 LOAD_FAST                6 (key)
        # 552 LOAD_METHOD             15 (encode)
        # 574 LOAD_CONST               4 ('utf-8')
        # 576 PRECALL                  1
        # 580 CALL                     1
        # 590 PRECALL                  1
        # 594 CALL                     1
        # 604 LOAD_GLOBAL             29 (NULL + QByteArray)
        # 616 LOAD_FAST                7 (value)
        # 618 LOAD_METHOD             15 (encode)
        # 640 LOAD_CONST               4 ('utf-8')
        # 642 PRECALL                  1
        # 646 CALL                     1
        # 656 PRECALL                  1
        # 660 CALL                     1
        # 260         670 PRECALL                  2
        # 674 CALL                     2
        # 684 POP_TOP
        # 686 JUMP_BACKWARD           92 (to 504)
        # 258     >>  688 LOAD_CONST               0 (None)
        # 690 RETURN_VALUE
        # 259     >>  692 LOAD_CONST               0 (None)
        # 694 RETURN_VALUE
        # Disassembly of <code object <dictcomp> at 0x000001EBD7107280, file "webview\platforms\qt.py", line 248>:
        # 248           0 RESUME                   0
        # 2 BUILD_MAP                0
        # 4 LOAD_FAST                0 (.0)
        # >>    6 FOR_ITER                82 (to 172)
        # 250           8 UNPACK_SEQUENCE          2
        # 12 STORE_FAST               1 (k)
        # 14 STORE_FAST               2 (v)
        # 249          16 LOAD_FAST                1 (k)
        # 18 LOAD_METHOD              0 (data)
        # 40 PRECALL                  0
        # 44 CALL                     0
        # 54 LOAD_METHOD              1 (decode)
        # 76 LOAD_CONST               0 ('utf-8')
        # 78 PRECALL                  1
        # 82 CALL                     1
        # 92 LOAD_FAST                1 (k)
        # 94 LOAD_METHOD              0 (data)
        # 116 PRECALL                  0
        # 120 CALL                     0
        # 130 LOAD_METHOD              1 (decode)
        # 152 LOAD_CONST               0 ('utf-8')
        # 154 PRECALL                  1
        # 158 CALL                     1
        # 248         168 MAP_ADD                  2
        # 170 JUMP_BACKWARD           83 (to 6)
        # >>  172 RETURN_VALUE

    def NavigationHandler():
        """BrowserView.NavigationHandler"""
        # 0 MAKE_CELL                0 (__class__)
        # 265           2 RESUME                   0
        # 4 LOAD_NAME                0 (__name__)
        # 6 STORE_NAME               1 (__module__)
        # 8 LOAD_CONST               0 ('BrowserView.NavigationHandler')
        # 10 STORE_NAME               2 (__qualname__)
        # 266          12 LOAD_CLOSURE             0 (__class__)
        # 14 BUILD_TUPLE              1
        # 16 LOAD_CONST               1 (<code object __init__ at 0x000001EBD77ED2F0, file "webview\platforms\qt.py", line 266>)
        # 18 MAKE_FUNCTION            8 (closure)
        # 20 STORE_NAME               3 (__init__)
        # 270          22 LOAD_CONST               2 (<code object acceptNavigationRequest at 0x000001EBD716FB90, file "webview\platforms\qt.py", line 270>)
        # 24 MAKE_FUNCTION            0
        # 26 STORE_NAME               4 (acceptNavigationRequest)
        # 28 LOAD_CLOSURE             0 (__class__)
        # 30 COPY                     1
        # 32 STORE_NAME               5 (__classcell__)
        # 34 RETURN_VALUE
        # Disassembly of <code object __init__ at 0x000001EBD77ED2F0, file "webview\platforms\qt.py", line 266>:
        # 0 COPY_FREE_VARS           1
        # 266           2 RESUME                   0
        # 267           4 LOAD_GLOBAL              1 (NULL + super)
        # 16 PRECALL                  0
        # 20 CALL                     0
        # 30 LOAD_METHOD              1 (__init__)
        # 52 LOAD_FAST                1 (page)
        # 54 LOAD_METHOD              2 (profile)
        # 76 PRECALL                  0
        # 80 CALL                     0
        # 90 PRECALL                  1
        # 94 CALL                     1
        # 104 POP_TOP
        # 268         106 LOAD_FAST                1 (page)
        # 108 LOAD_ATTR                3 (parent)
        # 118 LOAD_FAST                0 (self)
        # 120 STORE_ATTR               4 (_parent)
        # 130 LOAD_CONST               0 (None)
        # 132 RETURN_VALUE
        # Disassembly of <code object acceptNavigationRequest at 0x000001EBD716FB90, file "webview\platforms\qt.py", line 270>:
        # 270           0 RESUME                   0
        # 271           2 LOAD_GLOBAL              0 (settings)
        # 14 LOAD_CONST               1 ('OPEN_EXTERNAL_LINKS_IN_BROWSER')
        # 16 BINARY_SUBSCR
        # 26 POP_JUMP_FORWARD_IF_FALSE    42 (to 112)
        # 272          28 LOAD_GLOBAL              3 (NULL + webbrowser)
        # 40 LOAD_ATTR                2 (open)
        # 50 LOAD_FAST                1 (url)
        # 52 LOAD_METHOD              3 (toString)
        # 74 PRECALL                  0
        # 78 CALL                     0
        # 88 LOAD_CONST               2 (2)
        # 90 LOAD_CONST               3 (True)
        # 92 PRECALL                  3
        # 96 CALL                     3
        # 106 POP_TOP
        # 273         108 LOAD_CONST               4 (False)
        # 110 RETURN_VALUE
        # 275     >>  112 LOAD_FAST                0 (self)
        # 114 LOAD_ATTR                4 (_parent)
        # 124 LOAD_METHOD              5 (load_url)
        # 146 LOAD_FAST                1 (url)
        # 148 LOAD_METHOD              3 (toString)
        # 170 PRECALL                  0
        # 174 CALL                     0
        # 184 PRECALL                  1
        # 188 CALL                     1
        # 198 POP_TOP
        # 276         200 LOAD_CONST               3 (True)
        # 202 RETURN_VALUE

    def WebPage():
        """BrowserView.WebPage"""
        # 0 MAKE_CELL                0 (__class__)
        # 278           2 RESUME                   0
        # 4 LOAD_NAME                0 (__name__)
        # 6 STORE_NAME               1 (__module__)
        # 8 LOAD_CONST               0 ('BrowserView.WebPage')
        # 10 STORE_NAME               2 (__qualname__)
        # 279          12 LOAD_CONST               7 ((None, None))
        # 14 LOAD_CLOSURE             0 (__class__)
        # 16 BUILD_TUPLE              1
        # 18 LOAD_CONST               2 (<code object __init__ at 0x000001EBD75961B0, file "webview\platforms\qt.py", line 279>)
        # 20 MAKE_FUNCTION            9 (defaults, closure)
        # 22 STORE_NAME               3 (__init__)
        # 294          24 LOAD_NAME                4 (is_webengine)
        # 26 POP_JUMP_FORWARD_IF_FALSE     4 (to 36)
        # 296          28 LOAD_CONST               3 (<code object onFeaturePermissionRequested at 0x000001EBD77CAD80, file "webview\platforms\qt.py", line 296>)
        # 30 MAKE_FUNCTION            0
        # 32 STORE_NAME               5 (onFeaturePermissionRequested)
        # 34 JUMP_FORWARD             3 (to 42)
        # 307     >>   36 LOAD_CONST               4 (<code object acceptNavigationRequest at 0x000001EBD77ED430, file "webview\platforms\qt.py", line 307>)
        # 38 MAKE_FUNCTION            0
        # 40 STORE_NAME               6 (acceptNavigationRequest)
        # 313     >>   42 LOAD_CLOSURE             0 (__class__)
        # 44 BUILD_TUPLE              1
        # 46 LOAD_CONST               5 (<code object userAgentForUrl at 0x000001EBD7E48A50, file "webview\platforms\qt.py", line 313>)
        # 48 MAKE_FUNCTION            8 (closure)
        # 50 STORE_NAME               7 (userAgentForUrl)
        # 320          52 LOAD_CONST               6 (<code object createWindow at 0x000001EBD7F1CFA0, file "webview\platforms\qt.py", line 320>)
        # 54 MAKE_FUNCTION            0
        # 56 STORE_NAME               8 (createWindow)
        # 58 LOAD_CLOSURE             0 (__class__)
        # 60 COPY                     1
        # 62 STORE_NAME               9 (__classcell__)
        # 64 RETURN_VALUE
        # Disassembly of <code object __init__ at 0x000001EBD75961B0, file "webview\platforms\qt.py", line 279>:
        # 0 COPY_FREE_VARS           1
        # 279           2 RESUME                   0
        # 280           4 LOAD_GLOBAL              0 (is_webengine)
        # 16 POP_JUMP_FORWARD_IF_FALSE    54 (to 126)
        # 18 LOAD_FAST                2 (profile)
        # 20 POP_JUMP_FORWARD_IF_FALSE    52 (to 126)
        # 281          22 LOAD_GLOBAL              3 (NULL + super)
        # 34 LOAD_GLOBAL              4 (BrowserView)
        # 46 LOAD_ATTR                3 (WebPage)
        # 56 LOAD_FAST                0 (self)
        # 58 PRECALL                  2
        # 62 CALL                     2
        # 72 LOAD_METHOD              4 (__init__)
        # 94 LOAD_FAST                2 (profile)
        # 96 LOAD_FAST                1 (parent)
        # 98 LOAD_ATTR                5 (webview)
        # 108 PRECALL                  2
        # 112 CALL                     2
        # 122 POP_TOP
        # 124 JUMP_FORWARD            50 (to 226)
        # 283     >>  126 LOAD_GLOBAL              3 (NULL + super)
        # 138 LOAD_GLOBAL              4 (BrowserView)
        # 150 LOAD_ATTR                3 (WebPage)
        # 160 LOAD_FAST                0 (self)
        # 162 PRECALL                  2
        # 166 CALL                     2
        # 176 LOAD_METHOD              4 (__init__)
        # 198 LOAD_FAST                1 (parent)
        # 200 LOAD_ATTR                5 (webview)
        # 210 PRECALL                  1
        # 214 CALL                     1
        # 224 POP_TOP
        # 285     >>  226 LOAD_GLOBAL              0 (is_webengine)
        # 238 POP_JUMP_FORWARD_IF_FALSE    63 (to 366)
        # 286         240 LOAD_FAST                0 (self)
        # 242 LOAD_ATTR                6 (featurePermissionRequested)
        # 252 LOAD_METHOD              7 (connect)
        # 274 LOAD_FAST                0 (self)
        # 276 LOAD_ATTR                8 (onFeaturePermissionRequested)
        # 286 PRECALL                  1
        # 290 CALL                     1
        # 300 POP_TOP
        # 287         302 LOAD_GLOBAL              4 (BrowserView)
        # 314 LOAD_METHOD              9 (NavigationHandler)
        # 336 LOAD_FAST                0 (self)
        # 338 PRECALL                  1
        # 342 CALL                     1
        # 352 LOAD_FAST                0 (self)
        # 354 STORE_ATTR              10 (nav_handler)
        # 364 JUMP_FORWARD             7 (to 380)
        # 289     >>  366 LOAD_CONST               0 (None)
        # 368 LOAD_FAST                0 (self)
        # 370 STORE_ATTR              10 (nav_handler)
        # 291     >>  380 LOAD_FAST                1 (parent)
        # 382 LOAD_ATTR               11 (transparent)
        # 392 POP_JUMP_FORWARD_IF_FALSE    38 (to 470)
        # 292         394 LOAD_FAST                0 (self)
        # 396 LOAD_METHOD             12 (setBackgroundColor)
        # 418 LOAD_GLOBAL             26 (QtCore)
        # 430 LOAD_ATTR               14 (Qt)
        # 440 LOAD_ATTR               11 (transparent)
        # 450 PRECALL                  1
        # 454 CALL                     1
        # 464 POP_TOP
        # 466 LOAD_CONST               0 (None)
        # 468 RETURN_VALUE
        # 291     >>  470 LOAD_CONST               0 (None)
        # 472 RETURN_VALUE
        # Disassembly of <code object onFeaturePermissionRequested at 0x000001EBD77CAD80, file "webview\platforms\qt.py", line 296>:
        # 296           0 RESUME                   0
        # 297           2 LOAD_FAST                2 (feature)
        # 298           4 LOAD_GLOBAL              0 (QWebPage)
        # 16 LOAD_ATTR                1 (Feature)
        # 26 LOAD_ATTR                2 (MediaAudioCapture)
        # 299          36 LOAD_GLOBAL              0 (QWebPage)
        # 48 LOAD_ATTR                1 (Feature)
        # 58 LOAD_ATTR                3 (MediaVideoCapture)
        # 300          68 LOAD_GLOBAL              0 (QWebPage)
        # 80 LOAD_ATTR                1 (Feature)
        # 90 LOAD_ATTR                4 (MediaAudioVideoCapture)
        # 297         100 BUILD_TUPLE              3
        # 102 CONTAINS_OP              0
        # 104 POP_JUMP_FORWARD_IF_FALSE    25 (to 156)
        # 302         106 LOAD_FAST                0 (self)
        # 108 LOAD_METHOD              5 (setFeaturePermission)
        # 130 LOAD_FAST                1 (url)
        # 132 LOAD_FAST                2 (feature)
        # 134 LOAD_CONST               1 (1)
        # 136 PRECALL                  3
        # 140 CALL                     3
        # 150 POP_TOP
        # 152 LOAD_CONST               0 (None)
        # 154 RETURN_VALUE
        # 304     >>  156 LOAD_FAST                0 (self)
        # 158 LOAD_METHOD              5 (setFeaturePermission)
        # 180 LOAD_FAST                1 (url)
        # 182 LOAD_FAST                2 (feature)
        # 184 LOAD_CONST               2 (2)
        # 186 PRECALL                  3
        # 190 CALL                     3
        # 200 POP_TOP
        # 202 LOAD_CONST               0 (None)
        # 204 RETURN_VALUE
        # Disassembly of <code object acceptNavigationRequest at 0x000001EBD77ED430, file "webview\platforms\qt.py", line 307>:
        # 307           0 RESUME                   0
        # 308           2 LOAD_FAST                1 (frame)
        # 4 POP_JUMP_FORWARD_IF_NOT_NONE    60 (to 126)
        # 309           6 LOAD_GLOBAL              1 (NULL + webbrowser)
        # 18 LOAD_ATTR                1 (open)
        # 28 LOAD_FAST                2 (request)
        # 30 LOAD_METHOD              2 (url)
        # 52 PRECALL                  0
        # 56 CALL                     0
        # 66 LOAD_METHOD              3 (toString)
        # 88 PRECALL                  0
        # 92 CALL                     0
        # 102 LOAD_CONST               1 (2)
        # 104 LOAD_CONST               2 (True)
        # 106 PRECALL                  3
        # 110 CALL                     3
        # 120 POP_TOP
        # 310         122 LOAD_CONST               3 (False)
        # 124 RETURN_VALUE
        # 311     >>  126 LOAD_CONST               2 (True)
        # 128 RETURN_VALUE
        # Disassembly of <code object userAgentForUrl at 0x000001EBD7E48A50, file "webview\platforms\qt.py", line 313>:
        # 0 COPY_FREE_VARS           1
        # 313           2 RESUME                   0
        # 314           4 LOAD_GLOBAL              0 (_state)
        # 16 LOAD_CONST               1 ('user_agent')
        # 18 BINARY_SUBSCR
        # 28 STORE_FAST               2 (user_agent)
        # 315          30 LOAD_FAST                2 (user_agent)
        # 32 POP_JUMP_FORWARD_IF_FALSE     2 (to 38)
        # 316          34 LOAD_FAST                2 (user_agent)
        # 36 RETURN_VALUE
        # 318     >>   38 LOAD_GLOBAL              3 (NULL + super)
        # 50 PRECALL                  0
        # 54 CALL                     0
        # 64 LOAD_METHOD              2 (userAgentForUrl)
        # 86 LOAD_FAST                1 (url)
        # 88 PRECALL                  1
        # 92 CALL                     1
        # 102 RETURN_VALUE
        # Disassembly of <code object createWindow at 0x000001EBD7F1CFA0, file "webview\platforms\qt.py", line 320>:
        # 320           0 RESUME                   0
        # 321           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (nav_handler)
        # 14 RETURN_VALUE

    def __init__(self, window):
        # 0 COPY_FREE_VARS           1
        # 323           2 RESUME                   0
        # 324           4 LOAD_GLOBAL              1 (NULL + super)
        # 16 LOAD_GLOBAL              2 (BrowserView)
        # 28 LOAD_FAST                0 (self)
        # 30 PRECALL                  2
        # 34 CALL                     2
        # 44 LOAD_METHOD              2 (__init__)
        # 66 PRECALL                  0
        # 70 CALL                     0
        # 80 POP_TOP
        # 325          82 LOAD_FAST                0 (self)
        # 84 LOAD_GLOBAL              2 (BrowserView)
        # 96 LOAD_ATTR                3 (instances)
        # 106 LOAD_FAST                1 (window)
        # 108 LOAD_ATTR                4 (uid)
        # 118 STORE_SUBSCR
        # 326         122 LOAD_FAST                1 (window)
        # 124 LOAD_ATTR                4 (uid)
        # 134 LOAD_FAST                0 (self)
        # 136 STORE_ATTR               4 (uid)
        # 327         146 LOAD_FAST                1 (window)
        # 148 LOAD_FAST                0 (self)
        # 150 STORE_ATTR               5 (pywebview_window)
        # 328         160 LOAD_FAST                0 (self)
        # 162 LOAD_FAST                0 (self)
        # 164 LOAD_ATTR                5 (pywebview_window)
        # 174 STORE_ATTR               6 (native)
        # 330         184 LOAD_GLOBAL              2 (BrowserView)
        # 196 LOAD_METHOD              7 (JSBridge)
        # 218 LOAD_FAST                0 (self)
        # 220 PRECALL                  1
        # 224 CALL                     1
        # 234 LOAD_FAST                0 (self)
        # 236 STORE_ATTR               8 (js_bridge)
        # 332         246 LOAD_CONST               1 (False)
        # 248 LOAD_FAST                0 (self)
        # 250 STORE_ATTR               9 (is_fullscreen)
        # 334         260 LOAD_GLOBAL             21 (NULL + Semaphore)
        # 272 LOAD_CONST               2 (0)
        # 274 PRECALL                  1
        # 278 CALL                     1
        # 288 LOAD_FAST                0 (self)
        # 290 STORE_ATTR              11 (_file_name_semaphore)
        # 335         300 LOAD_GLOBAL             21 (NULL + Semaphore)
        # 312 LOAD_CONST               2 (0)
        # 314 PRECALL                  1
        # 318 CALL                     1
        # 328 LOAD_FAST                0 (self)
        # 330 STORE_ATTR              12 (_current_url_semaphore)
        # 337         340 LOAD_FAST                1 (window)
        # 342 LOAD_ATTR               13 (localization)
        # 352 LOAD_FAST                0 (self)
        # 354 STORE_ATTR              13 (localization)
        # 339         364 LOAD_FAST                1 (window)
        # 366 LOAD_ATTR               14 (screen)
        # 376 POP_JUMP_FORWARD_IF_FALSE    79 (to 536)
        # 340         378 LOAD_GLOBAL             30 (_qt6)
        # 390 POP_JUMP_FORWARD_IF_FALSE    36 (to 464)
        # 341         392 LOAD_GLOBAL             33 (NULL + QScreen)
        # 404 LOAD_ATTR               17 (geometry)
        # 414 LOAD_FAST                1 (window)
        # 416 LOAD_ATTR               14 (screen)
        # 426 LOAD_ATTR               18 (frame)
        # 436 PRECALL                  1
        # 440 CALL                     1
        # 450 LOAD_FAST                0 (self)
        # 452 STORE_ATTR              14 (screen)
        # 462 JUMP_FORWARD           128 (to 720)
        # 343     >>  464 LOAD_FAST                1 (window)
        # 466 LOAD_ATTR               14 (screen)
        # 476 LOAD_ATTR               18 (frame)
        # 486 LOAD_METHOD             17 (geometry)
        # 508 PRECALL                  0
        # 512 CALL                     0
        # 522 LOAD_FAST                0 (self)
        # 524 STORE_ATTR              14 (screen)
        # 534 JUMP_FORWARD            92 (to 720)
        # 345     >>  536 LOAD_GLOBAL             30 (_qt6)
        # 548 POP_JUMP_FORWARD_IF_FALSE    43 (to 636)
        # 346         550 LOAD_GLOBAL             33 (NULL + QScreen)
        # 562 LOAD_ATTR               17 (geometry)
        # 572 LOAD_GLOBAL             39 (NULL + QApplication)
        # 584 LOAD_ATTR               20 (primaryScreen)
        # 594 PRECALL                  0
        # 598 CALL                     0
        # 608 PRECALL                  1
        # 612 CALL                     1
        # 622 LOAD_FAST                0 (self)
        # 624 STORE_ATTR              14 (screen)
        # 634 JUMP_FORWARD            42 (to 720)
        # 348     >>  636 LOAD_GLOBAL             39 (NULL + QApplication)
        # 648 LOAD_ATTR               20 (primaryScreen)
        # 658 PRECALL                  0
        # 662 CALL                     0
        # 672 LOAD_METHOD             17 (geometry)
        # 694 PRECALL                  0
        # 698 CALL                     0
        # 708 LOAD_FAST                0 (self)
        # 710 STORE_ATTR              14 (screen)
        # 350     >>  720 BUILD_MAP                0
        # 722 LOAD_FAST                0 (self)
        # 724 STORE_ATTR              21 (_js_results)
        # 351         734 LOAD_CONST               0 (None)
        # 736 LOAD_FAST                0 (self)
        # 738 STORE_ATTR              22 (_current_url)
        # 352         748 LOAD_CONST               0 (None)
        # 750 LOAD_FAST                0 (self)
        # 752 STORE_ATTR              23 (_file_name)
        # 353         762 BUILD_MAP                0
        # 764 LOAD_FAST                0 (self)
        # 766 STORE_ATTR              24 (_confirmation_dialog_results)
        # 355         776 LOAD_FAST                0 (self)
        # 778 LOAD_METHOD             25 (resize)
        # 800 LOAD_FAST                1 (window)
        # 802 LOAD_ATTR               26 (initial_width)
        # 812 LOAD_FAST                1 (window)
        # 814 LOAD_ATTR               27 (initial_height)
        # 824 PRECALL                  2
        # 828 CALL                     2
        # 838 POP_TOP
        # 356         840 LOAD_FAST                1 (window)
        # 842 LOAD_ATTR               28 (title)
        # 852 LOAD_FAST                0 (self)
        # 854 STORE_ATTR              28 (title)
        # 357         864 LOAD_FAST                0 (self)
        # 866 LOAD_METHOD             29 (setWindowTitle)
        # 888 LOAD_FAST                1 (window)
        # 890 LOAD_ATTR               28 (title)
        # 900 PRECALL                  1
        # 904 CALL                     1
        # 914 POP_TOP
        # 360         916 LOAD_GLOBAL             61 (NULL + QColor)
        # 928 PRECALL                  0
        # 932 CALL                     0
        # 942 LOAD_FAST                0 (self)
        # 944 STORE_ATTR              31 (background_color)
        # 361         954 LOAD_FAST                0 (self)
        # 956 LOAD_ATTR               31 (background_color)
        # 966 LOAD_METHOD             32 (setNamedColor)
        # 988 LOAD_FAST                1 (window)
        # 990 LOAD_ATTR               31 (background_color)
        # 1000 PRECALL                  1
        # 1004 CALL                     1
        # 1014 POP_TOP
        # 362        1016 LOAD_FAST                0 (self)
        # 1018 LOAD_METHOD             33 (palette)
        # 1040 PRECALL                  0
        # 1044 CALL                     0
        # 1054 STORE_FAST               2 (palette)
        # 363        1056 LOAD_FAST                2 (palette)
        # 1058 LOAD_METHOD             34 (setColor)
        # 1080 LOAD_FAST                0 (self)
        # 1082 LOAD_METHOD             35 (backgroundRole)
        # 1104 PRECALL                  0
        # 1108 CALL                     0
        # 1118 LOAD_FAST                0 (self)
        # 1120 LOAD_ATTR               31 (background_color)
        # 1130 PRECALL                  2
        # 1134 CALL                     2
        # 1144 POP_TOP
        # 364        1146 LOAD_FAST                0 (self)
        # 1148 LOAD_METHOD             36 (setPalette)
        # 1170 LOAD_FAST                2 (palette)
        # 1172 PRECALL                  1
        # 1176 CALL                     1
        # 1186 POP_TOP
        # 366        1188 LOAD_FAST                1 (window)
        # 1190 LOAD_ATTR               37 (resizable)
        # 1200 POP_JUMP_FORWARD_IF_TRUE    32 (to 1266)
        # 367        1202 LOAD_FAST                0 (self)
        # 1204 LOAD_METHOD             38 (setFixedSize)
        # 1226 LOAD_FAST                1 (window)
        # 1228 LOAD_ATTR               26 (initial_width)
        # 1238 LOAD_FAST                1 (window)
        # 1240 LOAD_ATTR               27 (initial_height)
        # 1250 PRECALL                  2
        # 1254 CALL                     2
        # 1264 POP_TOP
        # 369     >> 1266 LOAD_FAST                0 (self)
        # 1268 LOAD_METHOD             39 (setMinimumSize)
        # 1290 LOAD_FAST                1 (window)
        # 1292 LOAD_ATTR               40 (min_size)
        # 1302 LOAD_CONST               2 (0)
        # 1304 BINARY_SUBSCR
        # 1314 LOAD_FAST                1 (window)
        # 1316 LOAD_ATTR               40 (min_size)
        # 1326 LOAD_CONST               3 (1)
        # 1328 BINARY_SUBSCR
        # 1338 PRECALL                  2
        # 1342 CALL                     2
        # 1352 POP_TOP
        # 371        1354 LOAD_FAST                1 (window)
        # 1356 LOAD_ATTR               41 (frameless)
        # 1366 LOAD_FAST                0 (self)
        # 1368 STORE_ATTR              41 (frameless)
        # 372        1378 LOAD_FAST                1 (window)
        # 1380 LOAD_ATTR               42 (easy_drag)
        # 1390 LOAD_FAST                0 (self)
        # 1392 STORE_ATTR              42 (easy_drag)
        # 373        1402 LOAD_FAST                0 (self)
        # 1404 LOAD_METHOD             43 (windowFlags)
        # 1426 PRECALL                  0
        # 1430 CALL                     0
        # 1440 STORE_FAST               3 (flags)
        # 374        1442 LOAD_FAST                0 (self)
        # 1444 LOAD_ATTR               41 (frameless)
        # 1454 POP_JUMP_FORWARD_IF_FALSE    20 (to 1496)
        # 375        1456 LOAD_FAST                3 (flags)
        # 1458 LOAD_GLOBAL             88 (QtCore)
        # 1470 LOAD_ATTR               45 (Qt)
        # 1480 LOAD_ATTR               46 (FramelessWindowHint)
        # 1490 BINARY_OP                7 (|)
        # 1494 STORE_FAST               3 (flags)
        # 377     >> 1496 LOAD_FAST                1 (window)
        # 1498 LOAD_ATTR               47 (on_top)
        # 1508 POP_JUMP_FORWARD_IF_FALSE    20 (to 1550)
        # 378        1510 LOAD_FAST                3 (flags)
        # 1512 LOAD_GLOBAL             88 (QtCore)
        # 1524 LOAD_ATTR               45 (Qt)
        # 1534 LOAD_ATTR               48 (WindowStaysOnTopHint)
        # 1544 BINARY_OP                7 (|)
        # 1548 STORE_FAST               3 (flags)
        # 380     >> 1550 LOAD_FAST                1 (window)
        # 1552 LOAD_ATTR               49 (focus)
        # 1562 POP_JUMP_FORWARD_IF_TRUE    56 (to 1676)
        # 381        1564 LOAD_FAST                0 (self)
        # 1566 LOAD_METHOD             50 (setAttribute)
        # 1588 LOAD_GLOBAL             88 (QtCore)
        # 1600 LOAD_ATTR               45 (Qt)
        # 1610 LOAD_ATTR               51 (WA_ShowWithoutActivating)
        # 1620 PRECALL                  1
        # 1624 CALL                     1
        # 1634 POP_TOP
        # 382        1636 LOAD_FAST                3 (flags)
        # 1638 LOAD_GLOBAL             88 (QtCore)
        # 1650 LOAD_ATTR               45 (Qt)
        # 1660 LOAD_ATTR               52 (WindowDoesNotAcceptFocus)
        # 1670 BINARY_OP                7 (|)
        # 1674 STORE_FAST               3 (flags)
        # 384     >> 1676 LOAD_FAST                0 (self)
        # 1678 LOAD_METHOD             53 (setWindowFlags)
        # 1700 LOAD_FAST                3 (flags)
        # 1702 PRECALL                  1
        # 1706 CALL                     1
        # 1716 POP_TOP
        # 385        1718 LOAD_FAST                0 (self)
        # 1720 LOAD_METHOD             54 (setAcceptDrops)
        # 1742 LOAD_CONST               4 (True)
        # 1744 PRECALL                  1
        # 1748 CALL                     1
        # 1758 POP_TOP
        # 387        1760 LOAD_FAST                1 (window)
        # 1762 LOAD_ATTR               55 (transparent)
        # 1772 LOAD_FAST                0 (self)
        # 1774 STORE_ATTR              55 (transparent)
        # 388        1784 LOAD_FAST                0 (self)
        # 1786 LOAD_ATTR               55 (transparent)
        # 1796 POP_JUMP_FORWARD_IF_FALSE   142 (to 2082)
        # 390        1798 LOAD_GLOBAL             61 (NULL + QColor)
        # 1810 LOAD_CONST               5 ('transparent')
        # 1812 PRECALL                  1
        # 1816 CALL                     1
        # 1826 LOAD_FAST                0 (self)
        # 1828 STORE_ATTR              31 (background_color)
        # 391        1838 LOAD_FAST                0 (self)
        # 1840 LOAD_METHOD             33 (palette)
        # 1862 PRECALL                  0
        # 1866 CALL                     0
        # 1876 STORE_FAST               2 (palette)
        # 392        1878 LOAD_FAST                2 (palette)
        # 1880 LOAD_METHOD             34 (setColor)
        # 1902 LOAD_FAST                0 (self)
        # 1904 LOAD_METHOD             35 (backgroundRole)
        # 1926 PRECALL                  0
        # 1930 CALL                     0
        # 1940 LOAD_FAST                0 (self)
        # 1942 LOAD_ATTR               31 (background_color)
        # 1952 PRECALL                  2
        # 1956 CALL                     2
        # 1966 POP_TOP
        # 393        1968 LOAD_FAST                0 (self)
        # 1970 LOAD_METHOD             36 (setPalette)
        # 1992 LOAD_FAST                2 (palette)
        # 1994 PRECALL                  1
        # 1998 CALL                     1
        # 2008 POP_TOP
        # 395        2010 LOAD_FAST                0 (self)
        # 2012 LOAD_METHOD             50 (setAttribute)
        # 2034 LOAD_GLOBAL             88 (QtCore)
        # 2046 LOAD_ATTR               45 (Qt)
        # 2056 LOAD_ATTR               56 (WA_TranslucentBackground)
        # 2066 PRECALL                  1
        # 2070 CALL                     1
        # 2080 POP_TOP
        # 397     >> 2082 LOAD_GLOBAL              2 (BrowserView)
        # 2094 LOAD_METHOD             57 (WebView)
        # 2116 LOAD_FAST                0 (self)
        # 2118 PRECALL                  1
        # 2122 CALL                     1
        # 2132 LOAD_FAST                0 (self)
        # 2134 STORE_ATTR              58 (webview)
        # 399        2144 LOAD_GLOBAL            118 (is_webengine)
        # 2156 POP_JUMP_FORWARD_IF_FALSE    17 (to 2192)
        # 400        2158 LOAD_GLOBAL            121 (NULL + environ_append)
        # 401        2170 LOAD_CONST               6 ('QTWEBENGINE_CHROMIUM_FLAGS')
        # 402        2172 LOAD_CONST               7 ('--use-fake-ui-for-media-stream')
        # 403        2174 LOAD_CONST               8 ('--enable-features=AutoplayIgnoreWebAudio')
        # 400        2176 PRECALL                  3
        # 2180 CALL                     3
        # 2190 POP_TOP
        # 406     >> 2192 LOAD_GLOBAL            122 (_state)
        # 2204 LOAD_CONST               9 ('debug')
        # 2206 BINARY_SUBSCR
        # 2216 POP_JUMP_FORWARD_IF_FALSE    80 (to 2378)
        # 2218 LOAD_GLOBAL            118 (is_webengine)
        # 2230 POP_JUMP_FORWARD_IF_FALSE    73 (to 2378)
        # 408        2232 LOAD_GLOBAL              2 (BrowserView)
        # 2244 LOAD_ATTR               62 (inspector_port)
        # 2254 POP_JUMP_FORWARD_IF_TRUE    60 (to 2376)
        # 409        2256 LOAD_GLOBAL              2 (BrowserView)
        # 2268 LOAD_METHOD             63 (_get_debug_port)
        # 2290 PRECALL                  0
        # 2294 CALL                     0
        # 2304 LOAD_GLOBAL              2 (BrowserView)
        # 2316 STORE_ATTR              62 (inspector_port)
        # 410        2326 LOAD_GLOBAL              2 (BrowserView)
        # 2338 LOAD_ATTR               62 (inspector_port)
        # 2348 LOAD_GLOBAL            128 (os)
        # 2360 LOAD_ATTR               65 (environ)
        # 2370 LOAD_CONST              10 ('QTWEBENGINE_REMOTE_DEBUGGING')
        # 2372 STORE_SUBSCR
        # >> 2376 JUMP_FORWARD            41 (to 2460)
        # 412     >> 2378 LOAD_FAST                0 (self)
        # 2380 LOAD_ATTR               58 (webview)
        # 2390 LOAD_METHOD             66 (setContextMenuPolicy)
        # 413        2412 LOAD_GLOBAL             88 (QtCore)
        # 2424 LOAD_ATTR               45 (Qt)
        # 2434 LOAD_ATTR               67 (NoContextMenu)
        # 412        2444 PRECALL                  1
        # 2448 CALL                     1
        # 2458 POP_TOP
        # 416     >> 2460 BUILD_MAP                0
        # 2462 LOAD_FAST                0 (self)
        # 2464 STORE_ATTR              68 (cookies)
        # 418        2474 LOAD_GLOBAL            118 (is_webengine)
        # 2486 EXTENDED_ARG             1
        # 2488 POP_JUMP_FORWARD_IF_FALSE   337 (to 3164)
        # 419        2490 LOAD_GLOBAL              2 (BrowserView)
        # 2502 LOAD_METHOD             69 (RequestInterceptor)
        # 2524 LOAD_FAST                0 (self)
        # 2526 LOAD_ATTR                5 (pywebview_window)
        # 2536 PRECALL                  1
        # 2540 CALL                     1
        # 2550 LOAD_FAST                0 (self)
        # 2552 STORE_ATTR              70 (request_interceptor)
        # 421        2562 LOAD_GLOBAL            122 (_state)
        # 2574 LOAD_CONST              11 ('private_mode')
        # 2576 BINARY_SUBSCR
        # 2586 POP_JUMP_FORWARD_IF_FALSE    20 (to 2628)
        # 422        2588 LOAD_GLOBAL            143 (NULL + QWebEngineProfile)
        # 2600 PRECALL                  0
        # 2604 CALL                     0
        # 2614 LOAD_FAST                0 (self)
        # 2616 STORE_ATTR              72 (profile)
        # 2626 JUMP_FORWARD            51 (to 2730)
        # 424     >> 2628 LOAD_GLOBAL            143 (NULL + QWebEngineProfile)
        # 2640 LOAD_CONST              12 ('pywebview')
        # 2642 PRECALL                  1
        # 2646 CALL                     1
        # 2656 LOAD_FAST                0 (self)
        # 2658 STORE_ATTR              72 (profile)
        # 425        2668 LOAD_FAST                0 (self)
        # 2670 LOAD_ATTR               72 (profile)
        # 2680 LOAD_METHOD             73 (setPersistentStoragePath)
        # 2702 LOAD_GLOBAL            148 (_profile_storage_path)
        # 2714 PRECALL                  1
        # 2718 CALL                     1
        # 2728 POP_TOP
        # 427     >> 2730 LOAD_GLOBAL            122 (_state)
        # 2742 LOAD_CONST              13 ('user_agent')
        # 2744 BINARY_SUBSCR
        # 2754 STORE_FAST               4 (user_agent)
        # 428        2756 LOAD_FAST                4 (user_agent)
        # 2758 POP_JUMP_FORWARD_IF_FALSE    26 (to 2812)
        # 429        2760 LOAD_FAST                0 (self)
        # 2762 LOAD_ATTR               72 (profile)
        # 2772 LOAD_METHOD             75 (setHttpUserAgent)
        # 2794 LOAD_FAST                4 (user_agent)
        # 2796 PRECALL                  1
        # 2800 CALL                     1
        # 2810 POP_TOP
        # 431     >> 2812 LOAD_FAST                0 (self)
        # 2814 LOAD_ATTR               72 (profile)
        # 2824 LOAD_METHOD             76 (cookieStore)
        # 2846 PRECALL                  0
        # 2850 CALL                     0
        # 2860 STORE_FAST               5 (cookie_store)
        # 432        2862 LOAD_FAST                5 (cookie_store)
        # 2864 LOAD_ATTR               77 (cookieAdded)
        # 2874 LOAD_METHOD             78 (connect)
        # 2896 LOAD_FAST                0 (self)
        # 2898 LOAD_ATTR               79 (on_cookie_added)
        # 2908 PRECALL                  1
        # 2912 CALL                     1
        # 2922 POP_TOP
        # 433        2924 LOAD_FAST                5 (cookie_store)
        # 2926 LOAD_ATTR               80 (cookieRemoved)
        # 2936 LOAD_METHOD             78 (connect)
        # 2958 LOAD_FAST                0 (self)
        # 2960 LOAD_ATTR               81 (on_cookie_removed)
        # 2970 PRECALL                  1
        # 2974 CALL                     1
        # 2984 POP_TOP
        # 435        2986 LOAD_FAST                0 (self)
        # 2988 LOAD_ATTR               72 (profile)
        # 2998 LOAD_METHOD             82 (setUrlRequestInterceptor)
        # 3020 LOAD_FAST                0 (self)
        # 3022 LOAD_ATTR               70 (request_interceptor)
        # 3032 PRECALL                  1
        # 3036 CALL                     1
        # 3046 POP_TOP
        # 436        3048 LOAD_FAST                0 (self)
        # 3050 LOAD_ATTR               58 (webview)
        # 3060 LOAD_METHOD             83 (setPage)
        # 3082 LOAD_GLOBAL              2 (BrowserView)
        # 3094 LOAD_METHOD             84 (WebPage)
        # 3116 LOAD_FAST                0 (self)
        # 3118 LOAD_FAST                0 (self)
        # 3120 LOAD_ATTR               72 (profile)
        # 3130 KW_NAMES                14
        # 3132 PRECALL                  2
        # 3136 CALL                     2
        # 3146 PRECALL                  1
        # 3150 CALL                     1
        # 3160 POP_TOP
        # 3162 JUMP_FORWARD            46 (to 3256)
        # 437     >> 3164 LOAD_GLOBAL            118 (is_webengine)
        # 3176 POP_JUMP_FORWARD_IF_TRUE    39 (to 3256)
        # 3178 LOAD_GLOBAL            122 (_state)
        # 3190 LOAD_CONST              11 ('private_mode')
        # 3192 BINARY_SUBSCR
        # 3202 POP_JUMP_FORWARD_IF_TRUE    26 (to 3256)
        # 438        3204 LOAD_GLOBAL            170 (logger)
        # 3216 LOAD_METHOD             86 (warning)
        # 3238 LOAD_CONST              15 ('qtwebkit does not support private_mode')
        # 3240 PRECALL                  1
        # 3244 CALL                     1
        # 3254 POP_TOP
        # 440     >> 3256 LOAD_GLOBAL            122 (_state)
        # 3268 LOAD_CONST              13 ('user_agent')
        # 3270 BINARY_SUBSCR
        # 3280 STORE_FAST               4 (user_agent)
        # 444        3282 LOAD_GLOBAL            118 (is_webengine)
        # 3294 POP_JUMP_FORWARD_IF_FALSE    71 (to 3438)
        # 445        3296 LOAD_FAST                0 (self)
        # 3298 LOAD_ATTR               72 (profile)
        # 3308 LOAD_METHOD             87 (settings)
        # 3330 PRECALL                  0
        # 3334 CALL                     0
        # 3344 LOAD_METHOD             50 (setAttribute)
        # 446        3366 LOAD_GLOBAL            176 (QWebEngineSettings)
        # 3378 LOAD_ATTR               89 (WebAttribute)
        # 3388 LOAD_ATTR               90 (LocalContentCanAccessFileUrls)
        # 447        3398 LOAD_GLOBAL            174 (settings)
        # 3410 LOAD_CONST              16 ('ALLOW_FILE_URLS')
        # 3412 BINARY_SUBSCR
        # 445        3422 PRECALL                  2
        # 3426 CALL                     2
        # 3436 POP_TOP
        # 450     >> 3438 LOAD_FAST                0 (self)
        # 3440 LOAD_ATTR               58 (webview)
        # 3450 LOAD_METHOD             91 (page)
        # 3472 PRECALL                  0
        # 3476 CALL                     0
        # 3486 LOAD_ATTR               92 (loadFinished)
        # 3496 LOAD_METHOD             78 (connect)
        # 3518 LOAD_FAST                0 (self)
        # 3520 LOAD_ATTR               93 (on_load_finished)
        # 3530 PRECALL                  1
        # 3534 CALL                     1
        # 3544 POP_TOP
        # 452        3546 LOAD_GLOBAL            174 (settings)
        # 3558 LOAD_CONST              17 ('ALLOW_DOWNLOADS')
        # 3560 BINARY_SUBSCR
        # 3570 POP_JUMP_FORWARD_IF_FALSE    72 (to 3716)
        # 453        3572 LOAD_FAST                0 (self)
        # 3574 LOAD_ATTR               58 (webview)
        # 3584 LOAD_METHOD             91 (page)
        # 3606 PRECALL                  0
        # 3610 CALL                     0
        # 3620 LOAD_METHOD             72 (profile)
        # 3642 PRECALL                  0
        # 3646 CALL                     0
        # 3656 LOAD_ATTR               94 (downloadRequested)
        # 3666 LOAD_METHOD             78 (connect)
        # 3688 LOAD_FAST                0 (self)
        # 3690 LOAD_ATTR               95 (on_download_requested)
        # 3700 PRECALL                  1
        # 3704 CALL                     1
        # 3714 POP_TOP
        # 455     >> 3716 LOAD_FAST                0 (self)
        # 3718 LOAD_METHOD             96 (setCentralWidget)
        # 3740 LOAD_FAST                0 (self)
        # 3742 LOAD_ATTR               58 (webview)
        # 3752 PRECALL                  1
        # 3756 CALL                     1
        # 3766 POP_TOP
        # 457        3768 LOAD_FAST                0 (self)
        # 3770 LOAD_ATTR               97 (create_window_trigger)
        # 3780 LOAD_METHOD             78 (connect)
        # 3802 LOAD_GLOBAL              2 (BrowserView)
        # 3814 LOAD_ATTR               98 (on_create_window)
        # 3824 PRECALL                  1
        # 3828 CALL                     1
        # 3838 POP_TOP
        # 458        3840 LOAD_FAST                0 (self)
        # 3842 LOAD_ATTR               99 (load_url_trigger)
        # 3852 LOAD_METHOD             78 (connect)
        # 3874 LOAD_FAST                0 (self)
        # 3876 LOAD_ATTR              100 (on_load_url)
        # 3886 PRECALL                  1
        # 3890 CALL                     1
        # 3900 POP_TOP
        # 459        3902 LOAD_FAST                0 (self)
        # 3904 LOAD_ATTR              101 (html_trigger)
        # 3914 LOAD_METHOD             78 (connect)
        # 3936 LOAD_FAST                0 (self)
        # 3938 LOAD_ATTR              102 (on_load_html)
        # 3948 PRECALL                  1
        # 3952 CALL                     1
        # 3962 POP_TOP
        # 460        3964 LOAD_FAST                0 (self)
        # 3966 LOAD_ATTR              103 (confirmation_dialog_trigger)
        # 3976 LOAD_METHOD             78 (connect)
        # 3998 LOAD_FAST                0 (self)
        # 4000 LOAD_ATTR              104 (on_confirmation_dialog)
        # 4010 PRECALL                  1
        # 4014 CALL                     1
        # 4024 POP_TOP
        # 461        4026 LOAD_FAST                0 (self)
        # 4028 LOAD_ATTR              105 (file_dialog_trigger)
        # 4038 LOAD_METHOD             78 (connect)
        # 4060 LOAD_FAST                0 (self)
        # 4062 LOAD_ATTR              106 (on_file_dialog)
        # 4072 PRECALL                  1
        # 4076 CALL                     1
        # 4086 POP_TOP
        # 462        4088 LOAD_FAST                0 (self)
        # 4090 LOAD_ATTR              107 (destroy_trigger)
        # 4100 LOAD_METHOD             78 (connect)
        # 4122 LOAD_FAST                0 (self)
        # 4124 LOAD_ATTR              108 (on_destroy_window)
        # 4134 PRECALL                  1
        # 4138 CALL                     1
        # 4148 POP_TOP
        # 463        4150 LOAD_FAST                0 (self)
        # 4152 LOAD_ATTR              109 (show_trigger)
        # 4162 LOAD_METHOD             78 (connect)
        # 4184 LOAD_FAST                0 (self)
        # 4186 LOAD_ATTR              110 (on_show_window)
        # 4196 PRECALL                  1
        # 4200 CALL                     1
        # 4210 POP_TOP
        # 464        4212 LOAD_FAST                0 (self)
        # 4214 LOAD_ATTR              111 (hide_trigger)
        # 4224 LOAD_METHOD             78 (connect)
        # 4246 LOAD_FAST                0 (self)
        # 4248 LOAD_ATTR              112 (on_hide_window)
        # 4258 PRECALL                  1
        # 4262 CALL                     1
        # 4272 POP_TOP
        # 465        4274 LOAD_FAST                0 (self)
        # 4276 LOAD_ATTR              113 (fullscreen_trigger)
        # 4286 LOAD_METHOD             78 (connect)
        # 4308 LOAD_FAST                0 (self)
        # 4310 LOAD_ATTR              114 (on_fullscreen)
        # 4320 PRECALL                  1
        # 4324 CALL                     1
        # 4334 POP_TOP
        # 466        4336 LOAD_FAST                0 (self)
        # 4338 LOAD_ATTR              115 (window_size_trigger)
        # 4348 LOAD_METHOD             78 (connect)
        # 4370 LOAD_FAST                0 (self)
        # 4372 LOAD_ATTR              116 (on_window_size)
        # 4382 PRECALL                  1
        # 4386 CALL                     1
        # 4396 POP_TOP
        # 467        4398 LOAD_FAST                0 (self)
        # 4400 LOAD_ATTR              117 (window_move_trigger)
        # 4410 LOAD_METHOD             78 (connect)
        # 4432 LOAD_FAST                0 (self)
        # 4434 LOAD_ATTR              118 (on_window_move)
        # 4444 PRECALL                  1
        # 4448 CALL                     1
        # 4458 POP_TOP
        # 468        4460 LOAD_FAST                0 (self)
        # 4462 LOAD_ATTR              119 (window_maximize_trigger)
        # 4472 LOAD_METHOD             78 (connect)
        # 4494 LOAD_FAST                0 (self)
        # 4496 LOAD_ATTR              120 (on_window_maximize)
        # 4506 PRECALL                  1
        # 4510 CALL                     1
        # 4520 POP_TOP
        # 469        4522 LOAD_FAST                0 (self)
        # 4524 LOAD_ATTR              121 (window_minimize_trigger)
        # 4534 LOAD_METHOD             78 (connect)
        # 4556 LOAD_FAST                0 (self)
        # 4558 LOAD_ATTR              122 (on_window_minimize)
        # 4568 PRECALL                  1
        # 4572 CALL                     1
        # 4582 POP_TOP
        # 470        4584 LOAD_FAST                0 (self)
        # 4586 LOAD_ATTR              123 (window_restore_trigger)
        # 4596 LOAD_METHOD             78 (connect)
        # 4618 LOAD_FAST                0 (self)
        # 4620 LOAD_ATTR              124 (on_window_restore)
        # 4630 PRECALL                  1
        # 4634 CALL                     1
        # 4644 POP_TOP
        # 471        4646 LOAD_FAST                0 (self)
        # 4648 LOAD_ATTR              125 (current_url_trigger)
        # 4658 LOAD_METHOD             78 (connect)
        # 4680 LOAD_FAST                0 (self)
        # 4682 LOAD_ATTR              126 (on_current_url)
        # 4692 PRECALL                  1
        # 4696 CALL                     1
        # 4706 POP_TOP
        # 472        4708 LOAD_FAST                0 (self)
        # 4710 LOAD_ATTR              127 (evaluate_js_trigger)
        # 4720 LOAD_METHOD             78 (connect)
        # 4742 LOAD_FAST                0 (self)
        # 4744 LOAD_ATTR              128 (on_evaluate_js)
        # 4754 PRECALL                  1
        # 4758 CALL                     1
        # 4768 POP_TOP
        # 473        4770 LOAD_FAST                0 (self)
        # 4772 LOAD_ATTR              129 (set_title_trigger)
        # 4782 LOAD_METHOD             78 (connect)
        # 4804 LOAD_FAST                0 (self)
        # 4806 LOAD_ATTR              130 (on_set_title)
        # 4816 PRECALL                  1
        # 4820 CALL                     1
        # 4830 POP_TOP
        # 474        4832 LOAD_FAST                0 (self)
        # 4834 LOAD_ATTR              131 (on_top_trigger)
        # 4844 LOAD_METHOD             78 (connect)
        # 4866 LOAD_FAST                0 (self)
        # 4868 LOAD_ATTR              132 (on_set_on_top)
        # 4878 PRECALL                  1
        # 4882 CALL                     1
        # 4892 POP_TOP
        # 476        4894 LOAD_GLOBAL            118 (is_webengine)
        # 4906 POP_JUMP_FORWARD_IF_FALSE   117 (to 5142)
        # 4908 EXTENDED_ARG             1
        # 4910 LOAD_GLOBAL            267 (NULL + platform)
        # 4922 LOAD_ATTR              134 (system)
        # 4932 PRECALL                  0
        # 4936 CALL                     0
        # 4946 LOAD_CONST              18 ('OpenBSD')
        # 4948 COMPARE_OP               3 (!=)
        # 4954 POP_JUMP_FORWARD_IF_FALSE    93 (to 5142)
        # 477        4956 EXTENDED_ARG             1
        # 4958 LOAD_GLOBAL            271 (NULL + QWebChannel)
        # 4970 LOAD_FAST                0 (self)
        # 4972 LOAD_ATTR               58 (webview)
        # 4982 LOAD_METHOD             91 (page)
        # 5004 PRECALL                  0
        # 5008 CALL                     0
        # 5018 PRECALL                  1
        # 5022 CALL                     1
        # 5032 LOAD_FAST                0 (self)
        # 5034 STORE_ATTR             136 (channel)
        # 478        5044 LOAD_FAST                0 (self)
        # 5046 LOAD_ATTR               58 (webview)
        # 5056 LOAD_METHOD             91 (page)
        # 5078 PRECALL                  0
        # 5082 CALL                     0
        # 5092 LOAD_METHOD            137 (setWebChannel)
        # 5114 LOAD_FAST                0 (self)
        # 5116 LOAD_ATTR              136 (channel)
        # 5126 PRECALL                  1
        # 5130 CALL                     1
        # 5140 POP_TOP
        # 480     >> 5142 LOAD_FAST                1 (window)
        # 5144 LOAD_ATTR              138 (fullscreen)
        # 5154 POP_JUMP_FORWARD_IF_FALSE    20 (to 5196)
        # 481        5156 LOAD_FAST                0 (self)
        # 5158 LOAD_METHOD            139 (toggle_fullscreen)
        # 5180 PRECALL                  0
        # 5184 CALL                     0
        # 5194 POP_TOP
        # 483     >> 5196 LOAD_FAST                1 (window)
        # 5198 LOAD_ATTR              140 (real_url)
        # 5208 POP_JUMP_FORWARD_IF_NONE    50 (to 5310)
        # 484        5210 LOAD_FAST                0 (self)
        # 5212 LOAD_ATTR               58 (webview)
        # 5222 LOAD_METHOD            141 (setUrl)
        # 5244 LOAD_GLOBAL             89 (NULL + QtCore)
        # 5256 LOAD_ATTR              142 (QUrl)
        # 5266 LOAD_FAST                1 (window)
        # 5268 LOAD_ATTR              140 (real_url)
        # 5278 PRECALL                  1
        # 5282 CALL                     1
        # 5292 PRECALL                  1
        # 5296 CALL                     1
        # 5306 POP_TOP
        # 5308 JUMP_FORWARD           170 (to 5650)
        # 485     >> 5310 LOAD_FAST                1 (window)
        # 5312 LOAD_ATTR                4 (uid)
        # 5322 LOAD_CONST              19 ('web_inspector')
        # 5324 COMPARE_OP               2 (==)
        # 5330 POP_JUMP_FORWARD_IF_FALSE    50 (to 5432)
        # 486        5332 LOAD_FAST                0 (self)
        # 5334 LOAD_ATTR               58 (webview)
        # 5344 LOAD_METHOD            141 (setUrl)
        # 5366 LOAD_GLOBAL             89 (NULL + QtCore)
        # 5378 LOAD_ATTR              142 (QUrl)
        # 5388 LOAD_FAST                1 (window)
        # 5390 LOAD_ATTR              143 (original_url)
        # 5400 PRECALL                  1
        # 5404 CALL                     1
        # 5414 PRECALL                  1
        # 5418 CALL                     1
        # 5428 POP_TOP
        # 5430 JUMP_FORWARD           109 (to 5650)
        # 487     >> 5432 LOAD_FAST                1 (window)
        # 5434 LOAD_ATTR              144 (html)
        # 5444 POP_JUMP_FORWARD_IF_FALSE    51 (to 5548)
        # 488        5446 LOAD_FAST                0 (self)
        # 5448 LOAD_ATTR               58 (webview)
        # 5458 LOAD_METHOD            145 (setHtml)
        # 5480 LOAD_FAST                1 (window)
        # 5482 LOAD_ATTR              144 (html)
        # 5492 LOAD_GLOBAL             89 (NULL + QtCore)
        # 5504 LOAD_ATTR              142 (QUrl)
        # 5514 LOAD_CONST              20 ('')
        # 5516 PRECALL                  1
        # 5520 CALL                     1
        # 5530 PRECALL                  2
        # 5534 CALL                     2
        # 5544 POP_TOP
        # 5546 JUMP_FORWARD            51 (to 5650)
        # 490     >> 5548 LOAD_FAST                0 (self)
        # 5550 LOAD_ATTR               58 (webview)
        # 5560 LOAD_METHOD            145 (setHtml)
        # 5582 EXTENDED_ARG             1
        # 5584 LOAD_GLOBAL            292 (DEFAULT_HTML)
        # 5596 LOAD_GLOBAL             89 (NULL + QtCore)
        # 5608 LOAD_ATTR              142 (QUrl)
        # 5618 LOAD_CONST              20 ('')
        # 5620 PRECALL                  1
        # 5624 CALL                     1
        # 5634 PRECALL                  2
        # 5638 CALL                     2
        # 5648 POP_TOP
        # 492     >> 5650 LOAD_FAST                1 (window)
        # 5652 LOAD_ATTR              147 (initial_x)
        # 5662 POP_JUMP_FORWARD_IF_NONE    92 (to 5848)
        # 5664 LOAD_FAST                1 (window)
        # 5666 LOAD_ATTR              148 (initial_y)
        # 5676 POP_JUMP_FORWARD_IF_NONE    85 (to 5848)
        # 493        5678 LOAD_FAST                0 (self)
        # 5680 LOAD_METHOD            149 (move)
        # 5702 LOAD_FAST                0 (self)
        # 5704 LOAD_ATTR               14 (screen)
        # 5714 LOAD_METHOD            150 (x)
        # 5736 PRECALL                  0
        # 5740 CALL                     0
        # 5750 LOAD_FAST                1 (window)
        # 5752 LOAD_ATTR              147 (initial_x)
        # 5762 BINARY_OP                0 (+)
        # 5766 LOAD_FAST                0 (self)
        # 5768 LOAD_ATTR               14 (screen)
        # 5778 LOAD_METHOD            151 (y)
        # 5800 PRECALL                  0
        # 5804 CALL                     0
        # 5814 LOAD_FAST                1 (window)
        # 5816 LOAD_ATTR              148 (initial_y)
        # 5826 BINARY_OP                0 (+)
        # 5830 PRECALL                  2
        # 5834 CALL                     2
        # 5844 POP_TOP
        # 5846 JUMP_FORWARD           136 (to 6120)
        # 495     >> 5848 LOAD_GLOBAL             30 (_qt6)
        # 5860 POP_JUMP_FORWARD_IF_FALSE     2 (to 5866)
        # 5862 LOAD_CONST              21 (-16)
        # 5864 JUMP_FORWARD             1 (to 5868)
        # >> 5866 LOAD_CONST               2 (0)
        # >> 5868 STORE_FAST               6 (offset)
        # 496        5870 LOAD_FAST                0 (self)
        # 5872 LOAD_ATTR               14 (screen)
        # 5882 LOAD_METHOD            152 (center)
        # 5904 PRECALL                  0
        # 5908 CALL                     0
        # 5918 LOAD_FAST                0 (self)
        # 5920 LOAD_METHOD            153 (rect)
        # 5942 PRECALL                  0
        # 5946 CALL                     0
        # 5956 LOAD_METHOD            152 (center)
        # 5978 PRECALL                  0
        # 5982 CALL                     0
        # 5992 BINARY_OP               10 (-)
        # 5996 STORE_FAST               7 (center)
        # 497        5998 LOAD_FAST                0 (self)
        # 6000 LOAD_METHOD            149 (move)
        # 6022 LOAD_FAST                7 (center)
        # 6024 LOAD_METHOD            150 (x)
        # 6046 PRECALL                  0
        # 6050 CALL                     0
        # 6060 LOAD_FAST                7 (center)
        # 6062 LOAD_METHOD            151 (y)
        # 6084 PRECALL                  0
        # 6088 CALL                     0
        # 6098 LOAD_FAST                6 (offset)
        # 6100 BINARY_OP                0 (+)
        # 6104 PRECALL                  2
        # 6108 CALL                     2
        # 6118 POP_TOP
        # 499     >> 6120 LOAD_FAST                1 (window)
        # 6122 LOAD_ATTR              154 (minimized)
        # 6132 POP_JUMP_FORWARD_IF_TRUE    40 (to 6214)
        # 500        6134 LOAD_FAST                0 (self)
        # 6136 LOAD_METHOD            155 (activateWindow)
        # 6158 PRECALL                  0
        # 6162 CALL                     0
        # 6172 POP_TOP
        # 501        6174 LOAD_FAST                0 (self)
        # 6176 LOAD_METHOD            156 (raise_)
        # 6198 PRECALL                  0
        # 6202 CALL                     0
        # 6212 POP_TOP
        # 503     >> 6214 LOAD_GLOBAL            122 (_state)
        # 6226 LOAD_CONST              22 ('icon')
        # 6228 BINARY_SUBSCR
        # 6238 POP_JUMP_FORWARD_IF_FALSE    48 (to 6336)
        # 504        6240 EXTENDED_ARG             1
        # 6242 LOAD_GLOBAL            315 (NULL + QIcon)
        # 6254 LOAD_GLOBAL            122 (_state)
        # 6266 LOAD_CONST              22 ('icon')
        # 6268 BINARY_SUBSCR
        # 6278 PRECALL                  1
        # 6282 CALL                     1
        # 6292 STORE_FAST               8 (icon)
        # 505        6294 LOAD_FAST                0 (self)
        # 6296 LOAD_METHOD            158 (setWindowIcon)
        # 6318 LOAD_FAST                8 (icon)
        # 6320 PRECALL                  1
        # 6324 CALL                     1
        # 6334 POP_TOP
        # 507     >> 6336 LOAD_FAST                0 (self)
        # 6338 LOAD_ATTR                5 (pywebview_window)
        # 6348 LOAD_ATTR              159 (events)
        # 6358 LOAD_ATTR              160 (before_show)
        # 6368 LOAD_METHOD            161 (set)
        # 6390 PRECALL                  0
        # 6394 CALL                     0
        # 6404 POP_TOP
        # 6406 LOAD_CONST               0 (None)
        # 6408 RETURN_VALUE

    def on_set_title(self, title):
        # 509           0 RESUME                   0
        # 510           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (setWindowTitle)
        # 26 LOAD_FAST                1 (title)
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 POP_TOP
        # 44 LOAD_CONST               0 (None)
        # 46 RETURN_VALUE

    def on_confirmation_dialog(self, title, message, uuid):
        # 512           0 RESUME                   0
        # 513           2 LOAD_GLOBAL              0 (BrowserView)
        # 14 LOAD_METHOD              1 (_convert_string)
        # 36 LOAD_FAST                3 (uuid)
        # 38 PRECALL                  1
        # 42 CALL                     1
        # 52 STORE_FAST               4 (uuid_)
        # 514          54 LOAD_GLOBAL              5 (NULL + QMessageBox)
        # 66 LOAD_ATTR                3 (question)
        # 76 LOAD_FAST                0 (self)
        # 78 LOAD_FAST                1 (title)
        # 80 LOAD_FAST                2 (message)
        # 82 LOAD_GLOBAL              4 (QMessageBox)
        # 94 LOAD_ATTR                4 (Cancel)
        # 104 LOAD_GLOBAL              4 (QMessageBox)
        # 116 LOAD_ATTR                5 (Ok)
        # 126 PRECALL                  5
        # 130 CALL                     5
        # 140 STORE_FAST               5 (reply)
        # 516         142 LOAD_FAST                0 (self)
        # 144 LOAD_ATTR                6 (_confirmation_dialog_results)
        # 154 LOAD_FAST                4 (uuid_)
        # 156 BINARY_SUBSCR
        # 166 STORE_FAST               6 (confirmation_dialog_result)
        # 518         168 LOAD_CONST               1 (False)
        # 170 STORE_FAST               7 (result)
        # 519         172 LOAD_FAST                5 (reply)
        # 174 LOAD_GLOBAL              4 (QMessageBox)
        # 186 LOAD_ATTR                5 (Ok)
        # 196 COMPARE_OP               2 (==)
        # 202 POP_JUMP_FORWARD_IF_FALSE     2 (to 208)
        # 520         204 LOAD_CONST               2 (True)
        # 206 STORE_FAST               7 (result)
        # 521     >>  208 LOAD_FAST                7 (result)
        # 210 LOAD_FAST                6 (confirmation_dialog_result)
        # 212 LOAD_CONST               3 ('result')
        # 214 STORE_SUBSCR
        # 522         218 LOAD_FAST                6 (confirmation_dialog_result)
        # 220 LOAD_CONST               4 ('semaphore')
        # 222 BINARY_SUBSCR
        # 232 LOAD_METHOD              7 (release)
        # 254 PRECALL                  0
        # 258 CALL                     0
        # 268 POP_TOP
        # 270 LOAD_CONST               0 (None)
        # 272 RETURN_VALUE

    def on_file_dialog(self, dialog_type, directory, allow_multiple, save_filename, file_filter):
        # 524           0 RESUME                   0
        # 525           2 LOAD_FAST                1 (dialog_type)
        # 4 LOAD_GLOBAL              0 (FileDialog)
        # 16 LOAD_ATTR                1 (FOLDER)
        # 26 COMPARE_OP               2 (==)
        # 32 POP_JUMP_FORWARD_IF_FALSE    51 (to 136)
        # 526          34 LOAD_GLOBAL              5 (NULL + QFileDialog)
        # 46 LOAD_ATTR                3 (getExistingDirectory)
        # 527          56 LOAD_FAST                0 (self)
        # 528          58 LOAD_FAST                0 (self)
        # 60 LOAD_ATTR                4 (localization)
        # 70 LOAD_CONST               1 ('linux.openFolder')
        # 72 BINARY_SUBSCR
        # 529          82 LOAD_FAST                2 (directory)
        # 530          84 LOAD_GLOBAL              4 (QFileDialog)
        # 96 LOAD_ATTR                5 (ShowDirsOnly)
        # 526         106 KW_NAMES                 2
        # 108 PRECALL                  4
        # 112 CALL                     4
        # 122 LOAD_FAST                0 (self)
        # 124 STORE_ATTR               6 (_file_name)
        # 134 JUMP_FORWARD           212 (to 560)
        # 532     >>  136 LOAD_FAST                1 (dialog_type)
        # 138 LOAD_GLOBAL              0 (FileDialog)
        # 150 LOAD_ATTR                7 (OPEN)
        # 160 COMPARE_OP               2 (==)
        # 166 POP_JUMP_FORWARD_IF_FALSE    82 (to 332)
        # 533         168 LOAD_FAST                3 (allow_multiple)
        # 170 POP_JUMP_FORWARD_IF_FALSE    40 (to 252)
        # 534         172 LOAD_GLOBAL              5 (NULL + QFileDialog)
        # 184 LOAD_ATTR                8 (getOpenFileNames)
        # 535         194 LOAD_FAST                0 (self)
        # 196 LOAD_FAST                0 (self)
        # 198 LOAD_ATTR                4 (localization)
        # 208 LOAD_CONST               3 ('linux.openFiles')
        # 210 BINARY_SUBSCR
        # 220 LOAD_FAST                2 (directory)
        # 222 LOAD_FAST                5 (file_filter)
        # 534         224 PRECALL                  4
        # 228 CALL                     4
        # 238 LOAD_FAST                0 (self)
        # 240 STORE_ATTR               6 (_file_name)
        # 250 JUMP_FORWARD           154 (to 560)
        # 538     >>  252 LOAD_GLOBAL              5 (NULL + QFileDialog)
        # 264 LOAD_ATTR                9 (getOpenFileName)
        # 539         274 LOAD_FAST                0 (self)
        # 276 LOAD_FAST                0 (self)
        # 278 LOAD_ATTR                4 (localization)
        # 288 LOAD_CONST               4 ('linux.openFile')
        # 290 BINARY_SUBSCR
        # 300 LOAD_FAST                2 (directory)
        # 302 LOAD_FAST                5 (file_filter)
        # 538         304 PRECALL                  4
        # 308 CALL                     4
        # 318 LOAD_FAST                0 (self)
        # 320 STORE_ATTR               6 (_file_name)
        # 330 JUMP_FORWARD           114 (to 560)
        # 541     >>  332 LOAD_FAST                1 (dialog_type)
        # 334 LOAD_GLOBAL              0 (FileDialog)
        # 346 LOAD_ATTR               10 (SAVE)
        # 356 COMPARE_OP               2 (==)
        # 362 POP_JUMP_FORWARD_IF_FALSE    98 (to 560)
        # 542         364 LOAD_FAST                2 (directory)
        # 366 POP_JUMP_FORWARD_IF_FALSE    58 (to 484)
        # 543         368 LOAD_GLOBAL             22 (os)
        # 380 LOAD_ATTR               12 (path)
        # 390 LOAD_METHOD             13 (join)
        # 412 LOAD_GLOBAL             29 (NULL + str)
        # 424 LOAD_FAST                2 (directory)
        # 426 PRECALL                  1
        # 430 CALL                     1
        # 440 LOAD_GLOBAL             29 (NULL + str)
        # 452 LOAD_FAST                4 (save_filename)
        # 454 PRECALL                  1
        # 458 CALL                     1
        # 468 PRECALL                  2
        # 472 CALL                     2
        # 482 STORE_FAST               4 (save_filename)
        # 545     >>  484 LOAD_GLOBAL              5 (NULL + QFileDialog)
        # 496 LOAD_ATTR               15 (getSaveFileName)
        # 546         506 LOAD_FAST                0 (self)
        # 508 LOAD_FAST                0 (self)
        # 510 LOAD_ATTR                4 (localization)
        # 520 LOAD_CONST               5 ('global.saveFile')
        # 522 BINARY_SUBSCR
        # 532 LOAD_FAST                4 (save_filename)
        # 545         534 PRECALL                  3
        # 538 CALL                     3
        # 548 LOAD_FAST                0 (self)
        # 550 STORE_ATTR               6 (_file_name)
        # 549     >>  560 LOAD_FAST                0 (self)
        # 562 LOAD_ATTR               16 (_file_name_semaphore)
        # 572 LOAD_METHOD             17 (release)
        # 594 PRECALL                  0
        # 598 CALL                     0
        # 608 POP_TOP
        # 610 LOAD_CONST               0 (None)
        # 612 RETURN_VALUE

    def on_cookie_added(self, cookie):
        # 551           0 RESUME                   0
        # 552           2 LOAD_GLOBAL              1 (NULL + str)
        # 14 LOAD_FAST                1 (cookie)
        # 16 LOAD_METHOD              1 (toRawForm)
        # 38 PRECALL                  0
        # 42 CALL                     0
        # 52 LOAD_CONST               1 ('utf-8')
        # 54 PRECALL                  2
        # 58 CALL                     2
        # 68 STORE_FAST               2 (raw)
        # 553          70 LOAD_GLOBAL              5 (NULL + create_cookie)
        # 82 LOAD_FAST                2 (raw)
        # 84 PRECALL                  1
        # 88 CALL                     1
        # 98 STORE_FAST               1 (cookie)
        # 555         100 LOAD_FAST                2 (raw)
        # 102 LOAD_FAST                0 (self)
        # 104 LOAD_ATTR                3 (cookies)
        # 114 CONTAINS_OP              1
        # 116 POP_JUMP_FORWARD_IF_FALSE    12 (to 142)
        # 556         118 LOAD_FAST                1 (cookie)
        # 120 LOAD_FAST                0 (self)
        # 122 LOAD_ATTR                3 (cookies)
        # 132 LOAD_FAST                2 (raw)
        # 134 STORE_SUBSCR
        # 138 LOAD_CONST               0 (None)
        # 140 RETURN_VALUE
        # 555     >>  142 LOAD_CONST               0 (None)
        # 144 RETURN_VALUE

    def on_cookie_removed(self, cookie):
        # 558           0 RESUME                   0
        # 559           2 LOAD_GLOBAL              1 (NULL + str)
        # 14 LOAD_FAST                1 (cookie)
        # 16 LOAD_METHOD              1 (toRawForm)
        # 38 PRECALL                  0
        # 42 CALL                     0
        # 52 LOAD_CONST               1 ('utf-8')
        # 54 PRECALL                  2
        # 58 CALL                     2
        # 68 STORE_FAST               2 (raw)
        # 561          70 LOAD_FAST                2 (raw)
        # 72 LOAD_FAST                0 (self)
        # 74 LOAD_ATTR                2 (cookies)
        # 84 CONTAINS_OP              0
        # 86 POP_JUMP_FORWARD_IF_FALSE    10 (to 108)
        # 562          88 LOAD_FAST                0 (self)
        # 90 LOAD_ATTR                2 (cookies)
        # 100 LOAD_FAST                2 (raw)
        # 102 DELETE_SUBSCR
        # 104 LOAD_CONST               0 (None)
        # 106 RETURN_VALUE
        # 561     >>  108 LOAD_CONST               0 (None)
        # 110 RETURN_VALUE

    def on_current_url(self):
        # 564           0 RESUME                   0
        # 565           2 LOAD_GLOBAL              0 (BrowserView)
        # 14 LOAD_METHOD              1 (_convert_string)
        # 36 LOAD_FAST                0 (self)
        # 38 LOAD_ATTR                2 (webview)
        # 48 LOAD_METHOD              3 (url)
        # 70 PRECALL                  0
        # 74 CALL                     0
        # 84 LOAD_METHOD              4 (toString)
        # 106 PRECALL                  0
        # 110 CALL                     0
        # 120 PRECALL                  1
        # 124 CALL                     1
        # 134 STORE_FAST               1 (url)
        # 566         136 LOAD_FAST                1 (url)
        # 138 LOAD_CONST               1 ('')
        # 140 COMPARE_OP               2 (==)
        # 146 POP_JUMP_FORWARD_IF_TRUE    21 (to 190)
        # 148 LOAD_FAST                1 (url)
        # 150 LOAD_METHOD              5 (startswith)
        # 172 LOAD_CONST               2 ('data:text/html')
        # 174 PRECALL                  1
        # 178 CALL                     1
        # 188 POP_JUMP_FORWARD_IF_FALSE     2 (to 194)
        # >>  190 LOAD_CONST               0 (None)
        # 192 JUMP_FORWARD             1 (to 196)
        # >>  194 LOAD_FAST                1 (url)
        # >>  196 LOAD_FAST                0 (self)
        # 198 STORE_ATTR               6 (_current_url)
        # 567         208 LOAD_FAST                0 (self)
        # 210 LOAD_ATTR                7 (_current_url_semaphore)
        # 220 LOAD_METHOD              8 (release)
        # 242 PRECALL                  0
        # 246 CALL                     0
        # 256 POP_TOP
        # 258 LOAD_CONST               0 (None)
        # 260 RETURN_VALUE

    def on_load_url(self, url):
        # 569           0 RESUME                   0
        # 570           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (webview)
        # 14 LOAD_METHOD              1 (setUrl)
        # 36 LOAD_GLOBAL              5 (NULL + QtCore)
        # 48 LOAD_ATTR                3 (QUrl)
        # 58 LOAD_FAST                1 (url)
        # 60 PRECALL                  1
        # 64 CALL                     1
        # 74 PRECALL                  1
        # 78 CALL                     1
        # 88 POP_TOP
        # 90 LOAD_CONST               0 (None)
        # 92 RETURN_VALUE

    def on_load_html(self, content, base_uri):
        # 572           0 RESUME                   0
        # 573           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (webview)
        # 14 LOAD_METHOD              1 (setHtml)
        # 36 LOAD_FAST                1 (content)
        # 38 LOAD_GLOBAL              5 (NULL + QtCore)
        # 50 LOAD_ATTR                3 (QUrl)
        # 60 LOAD_FAST                2 (base_uri)
        # 62 PRECALL                  1
        # 66 CALL                     1
        # 76 PRECALL                  2
        # 80 CALL                     2
        # 90 POP_TOP
        # 92 LOAD_CONST               0 (None)
        # 94 RETURN_VALUE

    def on_set_on_top(self, top):
        # 575           0 RESUME                   0
        # 576           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (windowFlags)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 STORE_FAST               2 (flags)
        # 577          42 LOAD_FAST                1 (top)
        # 44 POP_JUMP_FORWARD_IF_FALSE    40 (to 126)
        # 578          46 LOAD_FAST                0 (self)
        # 48 LOAD_METHOD              1 (setWindowFlags)
        # 70 LOAD_FAST                2 (flags)
        # 72 LOAD_GLOBAL              4 (QtCore)
        # 84 LOAD_ATTR                3 (Qt)
        # 94 LOAD_ATTR                4 (WindowStaysOnTopHint)
        # 104 BINARY_OP                7 (|)
        # 108 PRECALL                  1
        # 112 CALL                     1
        # 122 POP_TOP
        # 124 JUMP_FORWARD            40 (to 206)
        # 580     >>  126 LOAD_FAST                0 (self)
        # 128 LOAD_METHOD              1 (setWindowFlags)
        # 150 LOAD_FAST                2 (flags)
        # 152 LOAD_GLOBAL              4 (QtCore)
        # 164 LOAD_ATTR                3 (Qt)
        # 174 LOAD_ATTR                4 (WindowStaysOnTopHint)
        # 184 UNARY_INVERT
        # 186 BINARY_OP                1 (&)
        # 190 PRECALL                  1
        # 194 CALL                     1
        # 204 POP_TOP
        # 582     >>  206 LOAD_FAST                0 (self)
        # 208 LOAD_METHOD              5 (show)
        # 230 PRECALL                  0
        # 234 CALL                     0
        # 244 POP_TOP
        # 246 LOAD_CONST               0 (None)
        # 248 RETURN_VALUE

    def showEvent(self, event):
        # 584           0 RESUME                   0
        # 585           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (pywebview_window)
        # 14 LOAD_ATTR                1 (events)
        # 24 LOAD_ATTR                2 (shown)
        # 34 LOAD_METHOD              3 (set)
        # 56 PRECALL                  0
        # 60 CALL                     0
        # 70 POP_TOP
        # 72 LOAD_CONST               0 (None)
        # 74 RETURN_VALUE

    def closeEvent(self, event):
        # 587           0 RESUME                   0
        # 588           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (pywebview_window)
        # 14 LOAD_ATTR                1 (events)
        # 24 LOAD_ATTR                2 (closing)
        # 34 LOAD_METHOD              3 (set)
        # 56 PRECALL                  0
        # 60 CALL                     0
        # 70 STORE_FAST               2 (should_cancel)
        # 590          72 LOAD_FAST                2 (should_cancel)
        # 74 POP_JUMP_FORWARD_IF_FALSE    22 (to 120)
        # 591          76 LOAD_FAST                1 (event)
        # 78 LOAD_METHOD              4 (ignore)
        # 100 PRECALL                  0
        # 104 CALL                     0
        # 114 POP_TOP
        # 592         116 LOAD_CONST               0 (None)
        # 118 RETURN_VALUE
        # 594     >>  120 LOAD_FAST                0 (self)
        # 122 LOAD_ATTR                0 (pywebview_window)
        # 132 LOAD_ATTR                5 (confirm_close)
        # 142 POP_JUMP_FORWARD_IF_FALSE    98 (to 340)
        # 595         144 LOAD_GLOBAL             13 (NULL + QMessageBox)
        # 156 LOAD_ATTR                7 (question)
        # 596         166 LOAD_FAST                0 (self)
        # 597         168 LOAD_FAST                0 (self)
        # 170 LOAD_ATTR                8 (title)
        # 598         180 LOAD_FAST                0 (self)
        # 182 LOAD_ATTR                9 (localization)
        # 192 LOAD_CONST               1 ('global.quitConfirmation')
        # 194 BINARY_SUBSCR
        # 599         204 LOAD_GLOBAL             12 (QMessageBox)
        # 216 LOAD_ATTR               10 (Yes)
        # 600         226 LOAD_GLOBAL             12 (QMessageBox)
        # 238 LOAD_ATTR               11 (No)
        # 595         248 PRECALL                  5
        # 252 CALL                     5
        # 262 STORE_FAST               3 (reply)
        # 603         264 LOAD_FAST                3 (reply)
        # 266 LOAD_GLOBAL             12 (QMessageBox)
        # 278 LOAD_ATTR               11 (No)
        # 288 COMPARE_OP               2 (==)
        # 294 POP_JUMP_FORWARD_IF_FALSE    22 (to 340)
        # 604         296 LOAD_FAST                1 (event)
        # 298 LOAD_METHOD              4 (ignore)
        # 320 PRECALL                  0
        # 324 CALL                     0
        # 334 POP_TOP
        # 605         336 LOAD_CONST               0 (None)
        # 338 RETURN_VALUE
        # 607     >>  340 LOAD_FAST                1 (event)
        # 342 LOAD_METHOD             12 (accept)
        # 364 PRECALL                  0
        # 368 CALL                     0
        # 378 POP_TOP
        # 609         380 LOAD_GLOBAL             26 (BrowserView)
        # 392 LOAD_ATTR               14 (instances)
        # 402 LOAD_FAST                0 (self)
        # 404 LOAD_ATTR               15 (uid)
        # 414 DELETE_SUBSCR
        # 610         416 LOAD_FAST                0 (self)
        # 418 LOAD_METHOD             16 (close)
        # 440 PRECALL                  0
        # 444 CALL                     0
        # 454 POP_TOP
        # 612         456 LOAD_FAST                0 (self)
        # 458 LOAD_ATTR                0 (pywebview_window)
        # 468 LOAD_GLOBAL             34 (windows)
        # 480 CONTAINS_OP              0
        # 482 POP_JUMP_FORWARD_IF_FALSE    25 (to 534)
        # 613         484 LOAD_GLOBAL             35 (NULL + windows)
        # 496 LOAD_ATTR               18 (remove)
        # 506 LOAD_FAST                0 (self)
        # 508 LOAD_ATTR                0 (pywebview_window)
        # 518 PRECALL                  1
        # 522 CALL                     1
        # 532 POP_TOP
        # 615     >>  534 LOAD_FAST                0 (self)
        # 536 LOAD_ATTR                0 (pywebview_window)
        # 546 LOAD_ATTR                1 (events)
        # 556 LOAD_ATTR               19 (closed)
        # 566 LOAD_METHOD              3 (set)
        # 588 PRECALL                  0
        # 592 CALL                     0
        # 602 POP_TOP
        # 617         604 LOAD_FAST                0 (self)
        # 606 LOAD_ATTR               20 (webview)
        # 616 LOAD_METHOD             21 (page)
        # 638 PRECALL                  0
        # 642 CALL                     0
        # 652 POP_JUMP_FORWARD_IF_FALSE    43 (to 740)
        # 618         654 LOAD_FAST                0 (self)
        # 656 LOAD_ATTR               20 (webview)
        # 666 LOAD_METHOD             21 (page)
        # 688 PRECALL                  0
        # 692 CALL                     0
        # 702 LOAD_METHOD             22 (deleteLater)
        # 724 PRECALL                  0
        # 728 CALL                     0
        # 738 POP_TOP
        # 620     >>  740 LOAD_GLOBAL             47 (NULL + len)
        # 752 LOAD_GLOBAL             26 (BrowserView)
        # 764 LOAD_ATTR               14 (instances)
        # 774 PRECALL                  1
        # 778 CALL                     1
        # 788 LOAD_CONST               2 (0)
        # 790 COMPARE_OP               2 (==)
        # 796 POP_JUMP_FORWARD_IF_FALSE    47 (to 892)
        # 621         798 LOAD_FAST                0 (self)
        # 800 LOAD_METHOD             24 (hide)
        # 822 PRECALL                  0
        # 826 CALL                     0
        # 836 POP_TOP
        # 622         838 LOAD_GLOBAL             50 (_app)
        # 850 LOAD_METHOD             26 (exit)
        # 872 PRECALL                  0
        # 876 CALL                     0
        # 886 POP_TOP
        # 888 LOAD_CONST               0 (None)
        # 890 RETURN_VALUE
        # 620     >>  892 LOAD_CONST               0 (None)
        # 894 RETURN_VALUE

    def changeEvent(self, e):
        # 624           0 RESUME                   0
        # 625           2 LOAD_FAST                1 (e)
        # 4 LOAD_METHOD              0 (type)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 LOAD_GLOBAL              2 (QtCore)
        # 52 LOAD_ATTR                2 (QEvent)
        # 62 LOAD_ATTR                3 (WindowStateChange)
        # 72 COMPARE_OP               3 (!=)
        # 78 POP_JUMP_FORWARD_IF_FALSE     2 (to 84)
        # 626          80 LOAD_CONST               0 (None)
        # 82 RETURN_VALUE
        # 628     >>   84 LOAD_FAST                0 (self)
        # 86 LOAD_METHOD              4 (windowState)
        # 108 PRECALL                  0
        # 112 CALL                     0
        # 122 LOAD_GLOBAL              2 (QtCore)
        # 134 LOAD_ATTR                5 (Qt)
        # 144 LOAD_ATTR                6 (WindowMinimized)
        # 154 COMPARE_OP               2 (==)
        # 160 POP_JUMP_FORWARD_IF_FALSE    35 (to 232)
        # 629         162 LOAD_FAST                0 (self)
        # 164 LOAD_ATTR                7 (pywebview_window)
        # 174 LOAD_ATTR                8 (events)
        # 184 LOAD_ATTR                9 (minimized)
        # 194 LOAD_METHOD             10 (set)
        # 216 PRECALL                  0
        # 220 CALL                     0
        # 230 POP_TOP
        # 631     >>  232 LOAD_FAST                0 (self)
        # 234 LOAD_METHOD              4 (windowState)
        # 256 PRECALL                  0
        # 260 CALL                     0
        # 270 LOAD_GLOBAL              2 (QtCore)
        # 282 LOAD_ATTR                5 (Qt)
        # 292 LOAD_ATTR               11 (WindowMaximized)
        # 302 COMPARE_OP               2 (==)
        # 308 POP_JUMP_FORWARD_IF_FALSE    35 (to 380)
        # 632         310 LOAD_FAST                0 (self)
        # 312 LOAD_ATTR                7 (pywebview_window)
        # 322 LOAD_ATTR                8 (events)
        # 332 LOAD_ATTR               12 (maximized)
        # 342 LOAD_METHOD             10 (set)
        # 364 PRECALL                  0
        # 368 CALL                     0
        # 378 POP_TOP
        # 634     >>  380 LOAD_FAST                0 (self)
        # 382 LOAD_METHOD              4 (windowState)
        # 404 PRECALL                  0
        # 408 CALL                     0
        # 418 LOAD_GLOBAL              2 (QtCore)
        # 430 LOAD_ATTR                5 (Qt)
        # 440 LOAD_ATTR               13 (WindowNoState)
        # 450 COMPARE_OP               2 (==)
        # 456 POP_JUMP_FORWARD_IF_FALSE    91 (to 640)
        # 458 LOAD_FAST                1 (e)
        # 460 LOAD_METHOD             14 (oldState)
        # 482 PRECALL                  0
        # 486 CALL                     0
        # 635         496 LOAD_GLOBAL              2 (QtCore)
        # 508 LOAD_ATTR                5 (Qt)
        # 518 LOAD_ATTR                6 (WindowMinimized)
        # 636         528 LOAD_GLOBAL              2 (QtCore)
        # 540 LOAD_ATTR                5 (Qt)
        # 550 LOAD_ATTR               11 (WindowMaximized)
        # 634         560 BUILD_TUPLE              2
        # 562 CONTAINS_OP              0
        # 564 POP_JUMP_FORWARD_IF_FALSE    39 (to 644)
        # 638         566 LOAD_FAST                0 (self)
        # 568 LOAD_ATTR                7 (pywebview_window)
        # 578 LOAD_ATTR                8 (events)
        # 588 LOAD_ATTR               15 (restored)
        # 598 LOAD_METHOD             10 (set)
        # 620 PRECALL                  0
        # 624 CALL                     0
        # 634 POP_TOP
        # 636 LOAD_CONST               0 (None)
        # 638 RETURN_VALUE
        # 634     >>  640 LOAD_CONST               0 (None)
        # 642 RETURN_VALUE
        # >>  644 LOAD_CONST               0 (None)
        # 646 RETURN_VALUE

    def resizeEvent(self, e):
        # 640           0 RESUME                   0
        # 642           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (pywebview_window)
        # 14 LOAD_ATTR                1 (initial_width)
        # 24 LOAD_FAST                0 (self)
        # 26 LOAD_METHOD              2 (width)
        # 48 PRECALL                  0
        # 52 CALL                     0
        # 62 COMPARE_OP               3 (!=)
        # 68 POP_JUMP_FORWARD_IF_TRUE    34 (to 138)
        # 643          70 LOAD_FAST                0 (self)
        # 72 LOAD_ATTR                0 (pywebview_window)
        # 82 LOAD_ATTR                3 (initial_height)
        # 92 LOAD_FAST                0 (self)
        # 94 LOAD_METHOD              4 (height)
        # 116 PRECALL                  0
        # 120 CALL                     0
        # 130 COMPARE_OP               3 (!=)
        # 136 POP_JUMP_FORWARD_IF_FALSE    75 (to 288)
        # 645     >>  138 LOAD_FAST                0 (self)
        # 140 LOAD_ATTR                0 (pywebview_window)
        # 150 LOAD_ATTR                5 (events)
        # 160 LOAD_ATTR                6 (resized)
        # 170 LOAD_METHOD              7 (set)
        # 192 LOAD_FAST                0 (self)
        # 194 LOAD_METHOD              2 (width)
        # 216 PRECALL                  0
        # 220 CALL                     0
        # 230 LOAD_FAST                0 (self)
        # 232 LOAD_METHOD              4 (height)
        # 254 PRECALL                  0
        # 258 CALL                     0
        # 268 PRECALL                  2
        # 272 CALL                     2
        # 282 POP_TOP
        # 284 LOAD_CONST               0 (None)
        # 286 RETURN_VALUE
        # 643     >>  288 LOAD_CONST               0 (None)
        # 290 RETURN_VALUE

    def eventFilter(self, object, event):
        # 0 COPY_FREE_VARS           1
        # 647           2 RESUME                   0
        # 648           4 LOAD_FAST                2 (event)
        # 6 LOAD_METHOD              0 (type)
        # 28 PRECALL                  0
        # 32 CALL                     0
        # 42 LOAD_GLOBAL              2 (QtCore)
        # 54 LOAD_ATTR                2 (QEvent)
        # 64 LOAD_ATTR                3 (Move)
        # 74 COMPARE_OP               2 (==)
        # 80 POP_JUMP_FORWARD_IF_FALSE    73 (to 228)
        # 649          82 LOAD_FAST                0 (self)
        # 84 LOAD_ATTR                4 (pywebview_window)
        # 94 LOAD_ATTR                5 (events)
        # 104 LOAD_ATTR                6 (moved)
        # 114 LOAD_METHOD              7 (set)
        # 136 LOAD_FAST                0 (self)
        # 138 LOAD_METHOD              8 (x)
        # 160 PRECALL                  0
        # 164 CALL                     0
        # 174 LOAD_FAST                0 (self)
        # 176 LOAD_METHOD              9 (y)
        # 198 PRECALL                  0
        # 202 CALL                     0
        # 212 PRECALL                  2
        # 216 CALL                     2
        # 226 POP_TOP
        # 651     >>  228 LOAD_GLOBAL             21 (NULL + super)
        # 240 PRECALL                  0
        # 244 CALL                     0
        # 254 LOAD_METHOD             11 (eventFilter)
        # 276 LOAD_FAST                1 (object)
        # 278 LOAD_FAST                2 (event)
        # 280 PRECALL                  2
        # 284 CALL                     2
        # 294 RETURN_VALUE

    def on_show_window(self):
        # 653           0 RESUME                   0
        # 654           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (show)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 POP_TOP
        # 42 LOAD_CONST               0 (None)
        # 44 RETURN_VALUE

    def on_hide_window(self):
        # 656           0 RESUME                   0
        # 657           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (hide)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 POP_TOP
        # 42 LOAD_CONST               0 (None)
        # 44 RETURN_VALUE

    def on_destroy_window(self):
        # 659           0 RESUME                   0
        # 660           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (close)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 POP_TOP
        # 42 LOAD_CONST               0 (None)
        # 44 RETURN_VALUE

    def on_fullscreen(self):
        # 662           0 RESUME                   0
        # 663           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (is_fullscreen)
        # 14 POP_JUMP_FORWARD_IF_FALSE    21 (to 58)
        # 664          16 LOAD_FAST                0 (self)
        # 18 LOAD_METHOD              1 (showNormal)
        # 40 PRECALL                  0
        # 44 CALL                     0
        # 54 POP_TOP
        # 56 JUMP_FORWARD            20 (to 98)
        # 666     >>   58 LOAD_FAST                0 (self)
        # 60 LOAD_METHOD              2 (showFullScreen)
        # 82 PRECALL                  0
        # 86 CALL                     0
        # 96 POP_TOP
        # 668     >>   98 LOAD_FAST                0 (self)
        # 100 LOAD_ATTR                0 (is_fullscreen)
        # 110 UNARY_NOT
        # 112 LOAD_FAST                0 (self)
        # 114 STORE_ATTR               0 (is_fullscreen)
        # 124 LOAD_CONST               0 (None)
        # 126 RETURN_VALUE

    def on_window_size(self, width, height, fix_point):
        # 670           0 RESUME                   0
        # 671           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (geometry)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 STORE_FAST               4 (geo)
        # 673          42 LOAD_FAST                3 (fix_point)
        # 44 LOAD_GLOBAL              2 (FixPoint)
        # 56 LOAD_ATTR                2 (EAST)
        # 66 BINARY_OP                1 (&)
        # 70 POP_JUMP_FORWARD_IF_FALSE    63 (to 198)
        # 675          72 LOAD_FAST                4 (geo)
        # 74 LOAD_METHOD              3 (setX)
        # 96 LOAD_FAST                4 (geo)
        # 98 LOAD_METHOD              4 (x)
        # 120 PRECALL                  0
        # 124 CALL                     0
        # 134 LOAD_FAST                4 (geo)
        # 136 LOAD_METHOD              5 (width)
        # 158 PRECALL                  0
        # 162 CALL                     0
        # 172 BINARY_OP                0 (+)
        # 176 LOAD_FAST                1 (width)
        # 178 BINARY_OP               10 (-)
        # 182 PRECALL                  1
        # 186 CALL                     1
        # 196 POP_TOP
        # 677     >>  198 LOAD_FAST                3 (fix_point)
        # 200 LOAD_GLOBAL              2 (FixPoint)
        # 212 LOAD_ATTR                6 (SOUTH)
        # 222 BINARY_OP                1 (&)
        # 226 POP_JUMP_FORWARD_IF_FALSE    63 (to 354)
        # 679         228 LOAD_FAST                4 (geo)
        # 230 LOAD_METHOD              7 (setY)
        # 252 LOAD_FAST                4 (geo)
        # 254 LOAD_METHOD              8 (y)
        # 276 PRECALL                  0
        # 280 CALL                     0
        # 290 LOAD_FAST                4 (geo)
        # 292 LOAD_METHOD              9 (height)
        # 314 PRECALL                  0
        # 318 CALL                     0
        # 328 BINARY_OP                0 (+)
        # 332 LOAD_FAST                2 (height)
        # 334 BINARY_OP               10 (-)
        # 338 PRECALL                  1
        # 342 CALL                     1
        # 352 POP_TOP
        # 681     >>  354 LOAD_FAST                0 (self)
        # 356 LOAD_METHOD             10 (setGeometry)
        # 378 LOAD_FAST                4 (geo)
        # 380 PRECALL                  1
        # 384 CALL                     1
        # 394 POP_TOP
        # 682         396 LOAD_FAST                0 (self)
        # 398 LOAD_METHOD             11 (setFixedSize)
        # 420 LOAD_FAST                1 (width)
        # 422 LOAD_FAST                2 (height)
        # 424 PRECALL                  2
        # 428 CALL                     2
        # 438 POP_TOP
        # 440 LOAD_CONST               0 (None)
        # 442 RETURN_VALUE

    def on_window_move(self, x, y):
        # 684           0 RESUME                   0
        # 685           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (move)
        # 26 LOAD_FAST                1 (x)
        # 28 LOAD_FAST                2 (y)
        # 30 PRECALL                  2
        # 34 CALL                     2
        # 44 POP_TOP
        # 46 LOAD_CONST               0 (None)
        # 48 RETURN_VALUE

    def on_window_maximize(self):
        # 687           0 RESUME                   0
        # 688           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (setWindowState)
        # 26 LOAD_GLOBAL              2 (QtCore)
        # 38 LOAD_ATTR                2 (Qt)
        # 48 LOAD_ATTR                3 (WindowMaximized)
        # 58 PRECALL                  1
        # 62 CALL                     1
        # 72 POP_TOP
        # 74 LOAD_CONST               0 (None)
        # 76 RETURN_VALUE

    def on_window_minimize(self):
        # 690           0 RESUME                   0
        # 691           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (setWindowState)
        # 26 LOAD_GLOBAL              2 (QtCore)
        # 38 LOAD_ATTR                2 (Qt)
        # 48 LOAD_ATTR                3 (WindowMinimized)
        # 58 PRECALL                  1
        # 62 CALL                     1
        # 72 POP_TOP
        # 74 LOAD_CONST               0 (None)
        # 76 RETURN_VALUE

    def on_window_restore(self):
        # 693           0 RESUME                   0
        # 694           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (setWindowState)
        # 26 LOAD_GLOBAL              2 (QtCore)
        # 38 LOAD_ATTR                2 (Qt)
        # 48 LOAD_ATTR                3 (WindowNoState)
        # 58 PRECALL                  1
        # 62 CALL                     1
        # 72 POP_TOP
        # 695          74 LOAD_FAST                0 (self)
        # 76 LOAD_METHOD              4 (raise_)
        # 98 PRECALL                  0
        # 102 CALL                     0
        # 112 POP_TOP
        # 696         114 LOAD_FAST                0 (self)
        # 116 LOAD_METHOD              5 (activateWindow)
        # 138 PRECALL                  0
        # 142 CALL                     0
        # 152 POP_TOP
        # 154 LOAD_CONST               0 (None)
        # 156 RETURN_VALUE

    def on_evaluate_js(self, script, uuid):
        # 0 MAKE_CELL                0 (self)
        # 2 MAKE_CELL                2 (uuid)
        # 698           4 RESUME                   0
        # 699           6 LOAD_CLOSURE             0 (self)
        # 8 LOAD_CLOSURE             2 (uuid)
        # 10 BUILD_TUPLE              2
        # 12 LOAD_CONST               1 (<code object return_result at 0x000001EBD75B23E0, file "webview\platforms\qt.py", line 699>)
        # 14 MAKE_FUNCTION            8 (closure)
        # 16 STORE_FAST               3 (return_result)
        # 716          18 NOP
        # 717          20 LOAD_GLOBAL              0 (_qt6)
        # 32 POP_JUMP_FORWARD_IF_FALSE    48 (to 130)
        # 718          34 LOAD_DEREF               0 (self)
        # 36 LOAD_ATTR                1 (webview)
        # 46 LOAD_METHOD              2 (page)
        # 68 PRECALL                  0
        # 72 CALL                     0
        # 82 LOAD_METHOD              3 (runJavaScript)
        # 104 LOAD_FAST                1 (script)
        # 106 LOAD_CONST               2 (0)
        # 108 LOAD_FAST                3 (return_result)
        # 110 PRECALL                  3
        # 114 CALL                     3
        # 124 POP_TOP
        # 126 LOAD_CONST               0 (None)
        # 128 RETURN_VALUE
        # 720     >>  130 LOAD_DEREF               0 (self)
        # 132 LOAD_ATTR                1 (webview)
        # 142 LOAD_METHOD              2 (page)
        # 164 PRECALL                  0
        # 168 CALL                     0
        # 178 LOAD_METHOD              3 (runJavaScript)
        # 200 LOAD_FAST                1 (script)
        # 202 LOAD_FAST                3 (return_result)
        # 204 PRECALL                  2
        # 208 CALL                     2
        # 218 POP_TOP
        # 220 LOAD_CONST               0 (None)
        # 222 RETURN_VALUE
        # >>  224 PUSH_EXC_INFO
        # 721         226 LOAD_GLOBAL              8 (TypeError)
        # 238 CHECK_EXC_MATCH
        # 240 POP_JUMP_FORWARD_IF_FALSE    48 (to 338)
        # 242 POP_TOP
        # 722         244 LOAD_DEREF               0 (self)
        # 246 LOAD_ATTR                1 (webview)
        # 256 LOAD_METHOD              2 (page)
        # 278 PRECALL                  0
        # 282 CALL                     0
        # 292 LOAD_METHOD              3 (runJavaScript)
        # 314 LOAD_FAST                1 (script)
        # 316 PRECALL                  1
        # 320 CALL                     1
        # 330 POP_TOP
        # 332 POP_EXCEPT
        # 334 LOAD_CONST               0 (None)
        # 336 RETURN_VALUE
        # 723     >>  338 LOAD_GLOBAL             10 (AttributeError)
        # 350 CHECK_EXC_MATCH
        # 352 POP_JUMP_FORWARD_IF_FALSE    77 (to 508)
        # 354 POP_TOP
        # 724         356 LOAD_DEREF               0 (self)
        # 358 LOAD_ATTR                1 (webview)
        # 368 LOAD_METHOD              2 (page)
        # 390 PRECALL                  0
        # 394 CALL                     0
        # 404 LOAD_METHOD              6 (mainFrame)
        # 426 PRECALL                  0
        # 430 CALL                     0
        # 440 LOAD_METHOD              7 (evaluateJavaScript)
        # 462 LOAD_FAST                1 (script)
        # 464 PRECALL                  1
        # 468 CALL                     1
        # 478 STORE_FAST               4 (result)
        # 725         480 PUSH_NULL
        # 482 LOAD_FAST                3 (return_result)
        # 484 LOAD_FAST                4 (result)
        # 486 PRECALL                  1
        # 490 CALL                     1
        # 500 POP_TOP
        # 502 POP_EXCEPT
        # 504 LOAD_CONST               0 (None)
        # 506 RETURN_VALUE
        # 726     >>  508 LOAD_GLOBAL             16 (Exception)
        # 520 CHECK_EXC_MATCH
        # 522 POP_JUMP_FORWARD_IF_FALSE    37 (to 598)
        # 524 STORE_FAST               5 (e)
        # 727         526 LOAD_GLOBAL             18 (logger)
        # 538 LOAD_METHOD             10 (exception)
        # 560 LOAD_FAST                5 (e)
        # 562 PRECALL                  1
        # 566 CALL                     1
        # 576 POP_TOP
        # 578 POP_EXCEPT
        # 580 LOAD_CONST               0 (None)
        # 582 STORE_FAST               5 (e)
        # 584 DELETE_FAST              5 (e)
        # 586 LOAD_CONST               0 (None)
        # 588 RETURN_VALUE
        # >>  590 LOAD_CONST               0 (None)
        # 592 STORE_FAST               5 (e)
        # 594 DELETE_FAST              5 (e)
        # 596 RERAISE                  1
        # 726     >>  598 RERAISE                  0
        # >>  600 COPY                     3
        # 602 POP_EXCEPT
        # 604 RERAISE                  1
        # ExceptionTable:
        # 20 to 124 -> 224 [0]
        # 130 to 218 -> 224 [0]
        # 224 to 330 -> 600 [1] lasti
        # 338 to 500 -> 600 [1] lasti
        # 508 to 524 -> 600 [1] lasti
        # 526 to 576 -> 590 [1] lasti
        # 590 to 598 -> 600 [1] lasti
        # Disassembly of <code object return_result at 0x000001EBD75B23E0, file "webview\platforms\qt.py", line 699>:
        # 0 COPY_FREE_VARS           2
        # 699           2 RESUME                   0
        # 700           4 LOAD_GLOBAL              0 (BrowserView)
        # 16 LOAD_METHOD              1 (_convert_string)
        # 38 LOAD_FAST                0 (result_)
        # 40 PRECALL                  1
        # 44 CALL                     1
        # 54 STORE_FAST               1 (result)
        # 701          56 LOAD_GLOBAL              0 (BrowserView)
        # 68 LOAD_METHOD              1 (_convert_string)
        # 90 LOAD_DEREF               5 (uuid)
        # 92 PRECALL                  1
        # 96 CALL                     1
        # 106 STORE_FAST               2 (uuid_)
        # 703         108 LOAD_DEREF               4 (self)
        # 110 LOAD_ATTR                2 (_js_results)
        # 120 LOAD_FAST                2 (uuid_)
        # 122 BINARY_SUBSCR
        # 132 STORE_FAST               3 (js_result)
        # 705         134 LOAD_FAST                3 (js_result)
        # 136 LOAD_CONST               1 ('parse_json')
        # 138 BINARY_SUBSCR
        # 148 POP_JUMP_FORWARD_IF_FALSE    75 (to 300)
        # 150 LOAD_FAST                1 (result)
        # 152 POP_JUMP_FORWARD_IF_FALSE    73 (to 300)
        # 706         154 NOP
        # 707         156 LOAD_GLOBAL              7 (NULL + json)
        # 168 LOAD_ATTR                4 (loads)
        # 178 LOAD_FAST                1 (result)
        # 180 PRECALL                  1
        # 184 CALL                     1
        # 194 LOAD_FAST                3 (js_result)
        # 196 LOAD_CONST               2 ('result')
        # 198 STORE_SUBSCR
        # 202 JUMP_FORWARD            53 (to 310)
        # >>  204 PUSH_EXC_INFO
        # 708         206 LOAD_GLOBAL             10 (Exception)
        # 218 CHECK_EXC_MATCH
        # 220 POP_JUMP_FORWARD_IF_FALSE    35 (to 292)
        # 222 POP_TOP
        # 709         224 LOAD_GLOBAL             12 (logger)
        # 236 LOAD_METHOD              7 (exception)
        # 258 LOAD_CONST               3 ('Failed to parse JSON: %s')
        # 260 LOAD_FAST                1 (result)
        # 262 PRECALL                  2
        # 266 CALL                     2
        # 276 POP_TOP
        # 710         278 LOAD_FAST                1 (result)
        # 280 LOAD_FAST                3 (js_result)
        # 282 LOAD_CONST               2 ('result')
        # 284 STORE_SUBSCR
        # 288 POP_EXCEPT
        # 290 JUMP_FORWARD             9 (to 310)
        # 708     >>  292 RERAISE                  0
        # >>  294 COPY                     3
        # 296 POP_EXCEPT
        # 298 RERAISE                  1
        # 712     >>  300 LOAD_FAST                1 (result)
        # 302 LOAD_FAST                3 (js_result)
        # 304 LOAD_CONST               2 ('result')
        # 306 STORE_SUBSCR
        # 714     >>  310 LOAD_FAST                3 (js_result)
        # 312 LOAD_CONST               4 ('semaphore')
        # 314 BINARY_SUBSCR
        # 324 LOAD_METHOD              8 (release)
        # 346 PRECALL                  0
        # 350 CALL                     0
        # 360 POP_TOP
        # 362 LOAD_CONST               0 (None)
        # 364 RETURN_VALUE
        # ExceptionTable:
        # 156 to 200 -> 204 [0]
        # 204 to 286 -> 294 [1] lasti
        # 292 to 292 -> 294 [1] lasti

    def on_load_finished(self):
        # 729           0 RESUME                   0
        # 730           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (uid)
        # 14 LOAD_CONST               1 ('web_inspector')
        # 16 COMPARE_OP               2 (==)
        # 22 POP_JUMP_FORWARD_IF_FALSE     2 (to 28)
        # 731          24 LOAD_CONST               0 (None)
        # 26 RETURN_VALUE
        # 733     >>   28 LOAD_FAST                0 (self)
        # 30 LOAD_METHOD              1 (_set_js_api)
        # 52 PRECALL                  0
        # 56 CALL                     0
        # 66 POP_TOP
        # 735          68 LOAD_GLOBAL              4 (_state)
        # 80 LOAD_CONST               2 ('debug')
        # 82 BINARY_SUBSCR
        # 92 POP_JUMP_FORWARD_IF_FALSE    40 (to 174)
        # 94 LOAD_GLOBAL              6 (settings)
        # 106 LOAD_CONST               3 ('OPEN_DEVTOOLS_IN_DEBUG')
        # 108 BINARY_SUBSCR
        # 118 POP_JUMP_FORWARD_IF_FALSE    29 (to 178)
        # 736         120 LOAD_FAST                0 (self)
        # 122 LOAD_ATTR                4 (webview)
        # 132 LOAD_METHOD              5 (show_inspector)
        # 154 PRECALL                  0
        # 158 CALL                     0
        # 168 POP_TOP
        # 170 LOAD_CONST               0 (None)
        # 172 RETURN_VALUE
        # 735     >>  174 LOAD_CONST               0 (None)
        # 176 RETURN_VALUE
        # >>  178 LOAD_CONST               0 (None)
        # 180 RETURN_VALUE

    def on_download_requested(self, download):
        # 738           0 RESUME                   0
        # 739           2 LOAD_FAST                1 (download)
        # 4 LOAD_METHOD              0 (url)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 LOAD_METHOD              1 (path)
        # 62 PRECALL                  0
        # 66 CALL                     0
        # 76 STORE_FAST               2 (old_path)
        # 740          78 LOAD_GLOBAL              5 (NULL + QtCore)
        # 90 LOAD_ATTR                3 (QFileInfo)
        # 100 LOAD_FAST                2 (old_path)
        # 102 PRECALL                  1
        # 106 CALL                     1
        # 116 LOAD_METHOD              4 (suffix)
        # 138 PRECALL                  0
        # 142 CALL                     0
        # 152 STORE_FAST               3 (suffix)
        # 741         154 LOAD_GLOBAL             11 (NULL + QFileDialog)
        # 166 LOAD_ATTR                6 (getSaveFileName)
        # 742         176 LOAD_FAST                0 (self)
        # 178 LOAD_FAST                0 (self)
        # 180 LOAD_ATTR                7 (localization)
        # 190 LOAD_CONST               1 ('global.saveFile')
        # 192 BINARY_SUBSCR
        # 202 LOAD_FAST                2 (old_path)
        # 204 LOAD_CONST               2 ('*.')
        # 206 LOAD_FAST                3 (suffix)
        # 208 BINARY_OP                0 (+)
        # 741         212 PRECALL                  4
        # 216 CALL                     4
        # 226 UNPACK_SEQUENCE          2
        # 230 STORE_FAST               4 (path)
        # 232 STORE_FAST               5 (_)
        # 744         234 LOAD_FAST                4 (path)
        # 236 POP_JUMP_FORWARD_IF_FALSE    43 (to 324)
        # 745         238 LOAD_FAST                1 (download)
        # 240 LOAD_METHOD              8 (setPath)
        # 262 LOAD_FAST                4 (path)
        # 264 PRECALL                  1
        # 268 CALL                     1
        # 278 POP_TOP
        # 746         280 LOAD_FAST                1 (download)
        # 282 LOAD_METHOD              9 (accept)
        # 304 PRECALL                  0
        # 308 CALL                     0
        # 318 POP_TOP
        # 320 LOAD_CONST               0 (None)
        # 322 RETURN_VALUE
        # 744     >>  324 LOAD_CONST               0 (None)
        # 326 RETURN_VALUE

    def set_title(self, title):
        # 748           0 RESUME                   0
        # 749           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (set_title_trigger)
        # 14 LOAD_METHOD              1 (emit)
        # 36 LOAD_FAST                1 (title)
        # 38 PRECALL                  1
        # 42 CALL                     1
        # 52 POP_TOP
        # 54 LOAD_CONST               0 (None)
        # 56 RETURN_VALUE

    def get_cookies(self):
        # 751           0 RESUME                   0
        # 752           2 LOAD_GLOBAL              1 (NULL + list)
        # 14 LOAD_FAST                0 (self)
        # 16 LOAD_ATTR                1 (cookies)
        # 26 LOAD_METHOD              2 (values)
        # 48 PRECALL                  0
        # 52 CALL                     0
        # 62 PRECALL                  1
        # 66 CALL                     1
        # 76 RETURN_VALUE

    def clear_cookies(self):
        # 754           0 RESUME                   0
        # 755           2 BUILD_MAP                0
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (cookies)
        # 756          16 LOAD_FAST                0 (self)
        # 18 LOAD_ATTR                1 (profile)
        # 28 LOAD_METHOD              2 (cookieStore)
        # 50 PRECALL                  0
        # 54 CALL                     0
        # 64 LOAD_METHOD              3 (deleteAllCookies)
        # 86 PRECALL                  0
        # 90 CALL                     0
        # 100 POP_TOP
        # 102 LOAD_CONST               0 (None)
        # 104 RETURN_VALUE

    def get_current_url(self):
        # 758           0 RESUME                   0
        # 759           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (current_url_trigger)
        # 14 LOAD_METHOD              1 (emit)
        # 36 PRECALL                  0
        # 40 CALL                     0
        # 50 POP_TOP
        # 760          52 LOAD_FAST                0 (self)
        # 54 LOAD_ATTR                2 (_current_url_semaphore)
        # 64 LOAD_METHOD              3 (acquire)
        # 86 PRECALL                  0
        # 90 CALL                     0
        # 100 POP_TOP
        # 762         102 LOAD_FAST                0 (self)
        # 104 LOAD_ATTR                4 (_current_url)
        # 114 RETURN_VALUE

    def load_url(self, url):
        # 764           0 RESUME                   0
        # 765           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (load_url_trigger)
        # 14 LOAD_METHOD              1 (emit)
        # 36 LOAD_FAST                1 (url)
        # 38 PRECALL                  1
        # 42 CALL                     1
        # 52 POP_TOP
        # 54 LOAD_CONST               0 (None)
        # 56 RETURN_VALUE

    def load_html(self, content, base_uri):
        # 767           0 RESUME                   0
        # 768           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (html_trigger)
        # 14 LOAD_METHOD              1 (emit)
        # 36 LOAD_FAST                1 (content)
        # 38 LOAD_FAST                2 (base_uri)
        # 40 PRECALL                  2
        # 44 CALL                     2
        # 54 POP_TOP
        # 56 LOAD_CONST               0 (None)
        # 58 RETURN_VALUE

    def create_confirmation_dialog(self, title, message):
        # 770           0 RESUME                   0
        # 771           2 LOAD_GLOBAL              1 (NULL + Semaphore)
        # 14 LOAD_CONST               1 (0)
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 STORE_FAST               3 (result_semaphore)
        # 772          32 LOAD_GLOBAL              3 (NULL + uuid1)
        # 44 PRECALL                  0
        # 48 CALL                     0
        # 58 LOAD_ATTR                2 (hex)
        # 68 STORE_FAST               4 (unique_id)
        # 774          70 LOAD_FAST                3 (result_semaphore)
        # 775          72 LOAD_CONST               0 (None)
        # 773          74 LOAD_CONST               2 (('semaphore', 'result'))
        # 76 BUILD_CONST_KEY_MAP      2
        # 78 LOAD_FAST                0 (self)
        # 80 LOAD_ATTR                3 (_confirmation_dialog_results)
        # 90 LOAD_FAST                4 (unique_id)
        # 92 STORE_SUBSCR
        # 778          96 LOAD_FAST                0 (self)
        # 98 LOAD_ATTR                4 (confirmation_dialog_trigger)
        # 108 LOAD_METHOD              5 (emit)
        # 130 LOAD_FAST                1 (title)
        # 132 LOAD_FAST                2 (message)
        # 134 LOAD_FAST                4 (unique_id)
        # 136 PRECALL                  3
        # 140 CALL                     3
        # 150 POP_TOP
        # 779         152 LOAD_FAST                3 (result_semaphore)
        # 154 LOAD_METHOD              6 (acquire)
        # 176 PRECALL                  0
        # 180 CALL                     0
        # 190 POP_TOP
        # 781         192 LOAD_FAST                0 (self)
        # 194 LOAD_ATTR                3 (_confirmation_dialog_results)
        # 204 LOAD_FAST                4 (unique_id)
        # 206 BINARY_SUBSCR
        # 216 LOAD_CONST               3 ('result')
        # 218 BINARY_SUBSCR
        # 228 STORE_FAST               5 (result)
        # 782         230 LOAD_FAST                0 (self)
        # 232 LOAD_ATTR                3 (_confirmation_dialog_results)
        # 242 LOAD_FAST                4 (unique_id)
        # 244 DELETE_SUBSCR
        # 784         246 LOAD_FAST                5 (result)
        # 248 RETURN_VALUE

    def create_file_dialog(self, dialog_type, directory, allow_multiple, save_filename, file_filter):
        # 786           0 RESUME                   0
        # 789           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (file_dialog_trigger)
        # 14 LOAD_METHOD              1 (emit)
        # 790          36 LOAD_FAST                1 (dialog_type)
        # 38 LOAD_FAST                2 (directory)
        # 40 LOAD_FAST                3 (allow_multiple)
        # 42 LOAD_FAST                4 (save_filename)
        # 44 LOAD_FAST                5 (file_filter)
        # 789          46 PRECALL                  5
        # 50 CALL                     5
        # 60 POP_TOP
        # 792          62 LOAD_FAST                0 (self)
        # 64 LOAD_ATTR                2 (_file_name_semaphore)
        # 74 LOAD_METHOD              3 (acquire)
        # 96 PRECALL                  0
        # 100 CALL                     0
        # 110 POP_TOP
        # 794         112 LOAD_FAST                1 (dialog_type)
        # 114 LOAD_GLOBAL              8 (FileDialog)
        # 126 LOAD_ATTR                5 (FOLDER)
        # 136 COMPARE_OP               2 (==)
        # 142 POP_JUMP_FORWARD_IF_FALSE     9 (to 162)
        # 795         144 LOAD_FAST                0 (self)
        # 146 LOAD_ATTR                6 (_file_name)
        # 156 BUILD_TUPLE              1
        # 158 STORE_FAST               6 (file_names)
        # 160 JUMP_FORWARD            59 (to 280)
        # 796     >>  162 LOAD_FAST                1 (dialog_type)
        # 164 LOAD_GLOBAL              8 (FileDialog)
        # 176 LOAD_ATTR                7 (SAVE)
        # 186 COMPARE_OP               2 (==)
        # 192 POP_JUMP_FORWARD_IF_TRUE     2 (to 198)
        # 194 LOAD_FAST                3 (allow_multiple)
        # 196 POP_JUMP_FORWARD_IF_TRUE    15 (to 228)
        # 797     >>  198 LOAD_FAST                0 (self)
        # 200 LOAD_ATTR                6 (_file_name)
        # 210 LOAD_CONST               1 (0)
        # 212 BINARY_SUBSCR
        # 222 BUILD_TUPLE              1
        # 224 STORE_FAST               6 (file_names)
        # 226 JUMP_FORWARD            26 (to 280)
        # 799     >>  228 LOAD_GLOBAL             17 (NULL + tuple)
        # 240 LOAD_FAST                0 (self)
        # 242 LOAD_ATTR                6 (_file_name)
        # 252 LOAD_CONST               1 (0)
        # 254 BINARY_SUBSCR
        # 264 PRECALL                  1
        # 268 CALL                     1
        # 278 STORE_FAST               6 (file_names)
        # 802     >>  280 LOAD_GLOBAL             19 (NULL + len)
        # 292 LOAD_FAST                6 (file_names)
        # 294 PRECALL                  1
        # 298 CALL                     1
        # 308 LOAD_CONST               1 (0)
        # 310 COMPARE_OP               2 (==)
        # 316 POP_JUMP_FORWARD_IF_TRUE    25 (to 368)
        # 318 LOAD_GLOBAL             19 (NULL + len)
        # 330 LOAD_FAST                6 (file_names)
        # 332 LOAD_CONST               1 (0)
        # 334 BINARY_SUBSCR
        # 344 PRECALL                  1
        # 348 CALL                     1
        # 358 LOAD_CONST               1 (0)
        # 360 COMPARE_OP               2 (==)
        # 366 POP_JUMP_FORWARD_IF_FALSE     2 (to 372)
        # 803     >>  368 LOAD_CONST               0 (None)
        # 370 RETURN_VALUE
        # 805     >>  372 LOAD_FAST                6 (file_names)
        # 374 RETURN_VALUE

    def hide_(self):
        # 807           0 RESUME                   0
        # 808           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (hide_trigger)
        # 14 LOAD_METHOD              1 (emit)
        # 36 PRECALL                  0
        # 40 CALL                     0
        # 50 POP_TOP
        # 52 LOAD_CONST               0 (None)
        # 54 RETURN_VALUE

    def show_(self):
        # 810           0 RESUME                   0
        # 811           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (show_trigger)
        # 14 LOAD_METHOD              1 (emit)
        # 36 PRECALL                  0
        # 40 CALL                     0
        # 50 POP_TOP
        # 52 LOAD_CONST               0 (None)
        # 54 RETURN_VALUE

    def destroy_(self):
        # 813           0 RESUME                   0
        # 814           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (destroy_trigger)
        # 14 LOAD_METHOD              1 (emit)
        # 36 PRECALL                  0
        # 40 CALL                     0
        # 50 POP_TOP
        # 52 LOAD_CONST               0 (None)
        # 54 RETURN_VALUE

    def toggle_fullscreen(self):
        # 816           0 RESUME                   0
        # 817           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (fullscreen_trigger)
        # 14 LOAD_METHOD              1 (emit)
        # 36 PRECALL                  0
        # 40 CALL                     0
        # 50 POP_TOP
        # 52 LOAD_CONST               0 (None)
        # 54 RETURN_VALUE

    def resize_(self, width, height, fix_point):
        # 819           0 RESUME                   0
        # 820           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (window_size_trigger)
        # 14 LOAD_METHOD              1 (emit)
        # 36 LOAD_FAST                1 (width)
        # 38 LOAD_FAST                2 (height)
        # 40 LOAD_FAST                3 (fix_point)
        # 42 PRECALL                  3
        # 46 CALL                     3
        # 56 POP_TOP
        # 58 LOAD_CONST               0 (None)
        # 60 RETURN_VALUE

    def move_window(self, x, y):
        # 822           0 RESUME                   0
        # 823           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (window_move_trigger)
        # 14 LOAD_METHOD              1 (emit)
        # 36 LOAD_FAST                1 (x)
        # 38 LOAD_FAST                2 (y)
        # 40 PRECALL                  2
        # 44 CALL                     2
        # 54 POP_TOP
        # 56 LOAD_CONST               0 (None)
        # 58 RETURN_VALUE

    def maximize(self):
        # 825           0 RESUME                   0
        # 826           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (window_maximize_trigger)
        # 14 LOAD_METHOD              1 (emit)
        # 36 PRECALL                  0
        # 40 CALL                     0
        # 50 POP_TOP
        # 52 LOAD_CONST               0 (None)
        # 54 RETURN_VALUE

    def minimize(self):
        # 828           0 RESUME                   0
        # 829           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (window_minimize_trigger)
        # 14 LOAD_METHOD              1 (emit)
        # 36 PRECALL                  0
        # 40 CALL                     0
        # 50 POP_TOP
        # 52 LOAD_CONST               0 (None)
        # 54 RETURN_VALUE

    def restore(self):
        # 831           0 RESUME                   0
        # 832           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (window_restore_trigger)
        # 14 LOAD_METHOD              1 (emit)
        # 36 PRECALL                  0
        # 40 CALL                     0
        # 50 POP_TOP
        # 52 LOAD_CONST               0 (None)
        # 54 RETURN_VALUE

    def set_on_top(self, top):
        # 834           0 RESUME                   0
        # 835           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (on_top_trigger)
        # 14 LOAD_METHOD              1 (emit)
        # 36 LOAD_FAST                1 (top)
        # 38 PRECALL                  1
        # 42 CALL                     1
        # 52 POP_TOP
        # 54 LOAD_CONST               0 (None)
        # 56 RETURN_VALUE

    def evaluate_js(self, script, parse_json):
        # 837           0 RESUME                   0
        # 838           2 LOAD_GLOBAL              1 (NULL + Semaphore)
        # 14 LOAD_CONST               1 (0)
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 STORE_FAST               3 (result_semaphore)
        # 839          32 LOAD_GLOBAL              3 (NULL + uuid1)
        # 44 PRECALL                  0
        # 48 CALL                     0
        # 58 LOAD_ATTR                2 (hex)
        # 68 STORE_FAST               4 (unique_id)
        # 841          70 LOAD_FAST                3 (result_semaphore)
        # 842          72 LOAD_CONST               2 ('')
        # 843          74 LOAD_FAST                2 (parse_json)
        # 840          76 LOAD_CONST               3 (('semaphore', 'result', 'parse_json'))
        # 78 BUILD_CONST_KEY_MAP      3
        # 80 LOAD_FAST                0 (self)
        # 82 LOAD_ATTR                3 (_js_results)
        # 92 LOAD_FAST                4 (unique_id)
        # 94 STORE_SUBSCR
        # 846          98 LOAD_FAST                0 (self)
        # 100 LOAD_ATTR                4 (evaluate_js_trigger)
        # 110 LOAD_METHOD              5 (emit)
        # 132 LOAD_FAST                1 (script)
        # 134 LOAD_FAST                4 (unique_id)
        # 136 PRECALL                  2
        # 140 CALL                     2
        # 150 POP_TOP
        # 847         152 LOAD_FAST                3 (result_semaphore)
        # 154 LOAD_METHOD              6 (acquire)
        # 176 PRECALL                  0
        # 180 CALL                     0
        # 190 POP_TOP
        # 849         192 LOAD_GLOBAL             15 (NULL + deepcopy)
        # 204 LOAD_FAST                0 (self)
        # 206 LOAD_ATTR                3 (_js_results)
        # 216 LOAD_FAST                4 (unique_id)
        # 218 BINARY_SUBSCR
        # 228 LOAD_CONST               4 ('result')
        # 230 BINARY_SUBSCR
        # 240 PRECALL                  1
        # 244 CALL                     1
        # 254 STORE_FAST               5 (result)
        # 850         256 LOAD_FAST                0 (self)
        # 258 LOAD_ATTR                3 (_js_results)
        # 268 LOAD_FAST                4 (unique_id)
        # 270 DELETE_SUBSCR
        # 852         272 LOAD_FAST                5 (result)
        # 274 RETURN_VALUE

    def _set_js_api(self):
        # 0 MAKE_CELL                0 (self)
        # 2 MAKE_CELL                4 (frame)
        # 854           4 RESUME                   0
        # 855           6 LOAD_CLOSURE             4 (frame)
        # 8 LOAD_CLOSURE             0 (self)
        # 10 BUILD_TUPLE              2
        # 12 LOAD_CONST               1 (<code object _register_window_object at 0x000001EBD7EF0030, file "webview\platforms\qt.py", line 855>)
        # 14 MAKE_FUNCTION            8 (closure)
        # 16 STORE_FAST               1 (_register_window_object)
        # 858          18 LOAD_GLOBAL              0 (is_webengine)
        # 30 POP_JUMP_FORWARD_IF_FALSE   205 (to 442)
        # 859          32 LOAD_GLOBAL              3 (NULL + QtCore)
        # 44 LOAD_ATTR                2 (QFile)
        # 54 LOAD_CONST               2 ('://qtwebchannel/qwebchannel.js')
        # 56 PRECALL                  1
        # 60 CALL                     1
        # 70 STORE_FAST               2 (qwebchannel_js)
        # 860          72 LOAD_FAST                2 (qwebchannel_js)
        # 74 LOAD_METHOD              3 (open)
        # 96 LOAD_GLOBAL              2 (QtCore)
        # 108 LOAD_ATTR                2 (QFile)
        # 118 LOAD_ATTR                4 (ReadOnly)
        # 128 PRECALL                  1
        # 132 CALL                     1
        # 142 POP_JUMP_FORWARD_IF_FALSE   148 (to 440)
        # 861         144 LOAD_GLOBAL             11 (NULL + bytes)
        # 156 LOAD_FAST                2 (qwebchannel_js)
        # 158 LOAD_METHOD              6 (readAll)
        # 180 PRECALL                  0
        # 184 CALL                     0
        # 194 PRECALL                  1
        # 198 CALL                     1
        # 208 LOAD_METHOD              7 (decode)
        # 230 LOAD_CONST               3 ('utf-8')
        # 232 PRECALL                  1
        # 236 CALL                     1
        # 246 STORE_FAST               3 (source)
        # 862         248 LOAD_DEREF               0 (self)
        # 250 LOAD_ATTR                8 (webview)
        # 260 LOAD_METHOD              9 (page)
        # 282 PRECALL                  0
        # 286 CALL                     0
        # 296 LOAD_METHOD             10 (runJavaScript)
        # 318 LOAD_FAST                3 (source)
        # 320 PRECALL                  1
        # 324 CALL                     1
        # 334 POP_TOP
        # 863         336 LOAD_DEREF               0 (self)
        # 338 LOAD_ATTR               11 (channel)
        # 348 LOAD_METHOD             12 (registerObject)
        # 370 LOAD_CONST               4 ('external')
        # 372 LOAD_DEREF               0 (self)
        # 374 LOAD_ATTR               13 (js_bridge)
        # 384 PRECALL                  2
        # 388 CALL                     2
        # 398 POP_TOP
        # 864         400 LOAD_FAST                2 (qwebchannel_js)
        # 402 LOAD_METHOD             14 (close)
        # 424 PRECALL                  0
        # 428 CALL                     0
        # 438 POP_TOP
        # >>  440 JUMP_FORWARD            53 (to 548)
        # 866     >>  442 LOAD_DEREF               0 (self)
        # 444 LOAD_ATTR                8 (webview)
        # 454 LOAD_METHOD              9 (page)
        # 476 PRECALL                  0
        # 480 CALL                     0
        # 490 LOAD_METHOD             15 (mainFrame)
        # 512 PRECALL                  0
        # 516 CALL                     0
        # 526 STORE_DEREF              4 (frame)
        # 867         528 PUSH_NULL
        # 530 LOAD_FAST                1 (_register_window_object)
        # 532 PRECALL                  0
        # 536 CALL                     0
        # 546 POP_TOP
        # 869     >>  548 LOAD_GLOBAL             33 (NULL + inject_pywebview)
        # 560 LOAD_GLOBAL             34 (renderer)
        # 572 LOAD_DEREF               0 (self)
        # 574 LOAD_ATTR               13 (js_bridge)
        # 584 LOAD_ATTR               18 (window)
        # 594 PRECALL                  2
        # 598 CALL                     2
        # 608 POP_TOP
        # 610 LOAD_CONST               0 (None)
        # 612 RETURN_VALUE
        # Disassembly of <code object _register_window_object at 0x000001EBD7EF0030, file "webview\platforms\qt.py", line 855>:
        # 0 COPY_FREE_VARS           2
        # 855           2 RESUME                   0
        # 856           4 LOAD_DEREF               0 (frame)
        # 6 LOAD_METHOD              0 (addToJavaScriptWindowObject)
        # 28 LOAD_CONST               1 ('external')
        # 30 LOAD_DEREF               1 (self)
        # 32 LOAD_ATTR                1 (js_bridge)
        # 42 PRECALL                  2
        # 46 CALL                     2
        # 56 POP_TOP
        # 58 LOAD_CONST               0 (None)
        # 60 RETURN_VALUE

    def _convert_string(result):
        # 871           0 RESUME                   0
        # 873           2 LOAD_GLOBAL              1 (NULL + isinstance)
        # 14 LOAD_FAST                0 (result)
        # 16 LOAD_GLOBAL              2 (QJsonValue)
        # 28 PRECALL                  2
        # 32 CALL                     2
        # 42 POP_JUMP_FORWARD_IF_FALSE    42 (to 128)
        # 874          44 LOAD_FAST                0 (result)
        # 46 LOAD_METHOD              2 (isNull)
        # 68 PRECALL                  0
        # 72 CALL                     0
        # 82 POP_JUMP_FORWARD_IF_FALSE     2 (to 88)
        # 84 LOAD_CONST               0 (None)
        # 86 JUMP_FORWARD            19 (to 126)
        # >>   88 LOAD_FAST                0 (result)
        # 90 LOAD_METHOD              3 (toString)
        # 112 PRECALL                  0
        # 116 CALL                     0
        # >>  126 RETURN_VALUE
        # 876     >>  128 LOAD_FAST                0 (result)
        # 130 RETURN_VALUE

    def _get_debug_port():
        """
        Check if default debug port 8228 is available,
        increment it by 1 until a port is available.
        :return: port: str
        """
        # 878           0 RESUME                   0
        # 885           2 LOAD_CONST               1 (False)
        # 4 STORE_FAST               0 (port_available)
        # 886           6 LOAD_CONST               2 (8228)
        # 8 STORE_FAST               1 (port)
        # 888          10 LOAD_FAST                0 (port_available)
        # 12 POP_JUMP_FORWARD_IF_TRUE   159 (to 332)
        # 889     >>   14 NOP
        # 890          16 LOAD_GLOBAL              1 (NULL + socket)
        # 28 LOAD_ATTR                0 (socket)
        # 38 LOAD_GLOBAL              0 (socket)
        # 50 LOAD_ATTR                1 (AF_INET)
        # 60 LOAD_GLOBAL              0 (socket)
        # 72 LOAD_ATTR                2 (SOCK_STREAM)
        # 82 PRECALL                  2
        # 86 CALL                     2
        # 96 STORE_FAST               2 (sock)
        # 891          98 LOAD_FAST                2 (sock)
        # 100 LOAD_METHOD              3 (bind)
        # 122 LOAD_CONST               3 ('localhost')
        # 124 LOAD_FAST                1 (port)
        # 126 BUILD_TUPLE              2
        # 128 PRECALL                  1
        # 132 CALL                     1
        # 142 POP_TOP
        # 892         144 LOAD_CONST               4 (True)
        # 146 STORE_FAST               0 (port_available)
        # 148 JUMP_FORWARD            43 (to 236)
        # >>  150 PUSH_EXC_INFO
        # 893         152 POP_TOP
        # 894         154 LOAD_CONST               1 (False)
        # 156 STORE_FAST               0 (port_available)
        # 895         158 LOAD_GLOBAL              8 (logger)
        # 170 LOAD_METHOD              5 (warning)
        # 192 LOAD_CONST               5 ('Port %s is in use')
        # 194 LOAD_FAST                1 (port)
        # 196 BINARY_OP                6 (%)
        # 200 PRECALL                  1
        # 204 CALL                     1
        # 214 POP_TOP
        # 896         216 LOAD_FAST                1 (port)
        # 218 LOAD_CONST               6 (1)
        # 220 BINARY_OP               13 (+=)
        # 224 STORE_FAST               1 (port)
        # 226 POP_EXCEPT
        # 228 JUMP_FORWARD             3 (to 236)
        # >>  230 COPY                     3
        # 232 POP_EXCEPT
        # 234 RERAISE                  1
        # 898     >>  236 LOAD_FAST                2 (sock)
        # 238 LOAD_METHOD              6 (close)
        # 260 PRECALL                  0
        # 264 CALL                     0
        # 274 POP_TOP
        # 276 JUMP_FORWARD            25 (to 328)
        # >>  278 PUSH_EXC_INFO
        # 280 LOAD_FAST                2 (sock)
        # 282 LOAD_METHOD              6 (close)
        # 304 PRECALL                  0
        # 308 CALL                     0
        # 318 POP_TOP
        # 320 RERAISE                  0
        # >>  322 COPY                     3
        # 324 POP_EXCEPT
        # 326 RERAISE                  1
        # 888     >>  328 LOAD_FAST                0 (port_available)
        # 330 POP_JUMP_BACKWARD_IF_FALSE   159 (to 14)
        # 900     >>  332 LOAD_GLOBAL             15 (NULL + str)
        # 344 LOAD_FAST                1 (port)
        # 346 PRECALL                  1
        # 350 CALL                     1
        # 360 RETURN_VALUE
        # ExceptionTable:
        # 16 to 146 -> 150 [0]
        # 148 to 148 -> 278 [0]
        # 150 to 224 -> 230 [1] lasti
        # 226 to 234 -> 278 [0]
        # 278 to 320 -> 322 [1] lasti

    def on_create_window(func):
        # 902           0 RESUME                   0
        # 905           2 PUSH_NULL
        # 4 LOAD_FAST                0 (func)
        # 6 PRECALL                  0
        # 10 CALL                     0
        # 20 POP_TOP
        # 22 LOAD_CONST               0 (None)
        # 24 RETURN_VALUE


def setup_app():
    # 908           0 RESUME                   0
    # 910           2 LOAD_GLOBAL              0 (settings)
    # 14 LOAD_CONST               1 ('IGNORE_SSL_ERRORS')
    # 16 BINARY_SUBSCR
    # 26 POP_JUMP_FORWARD_IF_FALSE    16 (to 60)
    # 911          28 LOAD_GLOBAL              3 (NULL + environ_append)
    # 40 LOAD_CONST               2 ('QTWEBENGINE_CHROMIUM_FLAGS')
    # 42 LOAD_CONST               3 ('--ignore-certificate-errors')
    # 44 PRECALL                  2
    # 48 CALL                     2
    # 58 POP_TOP
    # 912     >>   60 LOAD_GLOBAL              5 (NULL + QApplication)
    # 72 LOAD_ATTR                3 (instance)
    # 82 PRECALL                  0
    # 86 CALL                     0
    # 96 JUMP_IF_TRUE_OR_POP     24 (to 146)
    # 98 LOAD_GLOBAL              5 (NULL + QApplication)
    # 110 LOAD_GLOBAL              8 (sys)
    # 122 LOAD_ATTR                5 (argv)
    # 132 PRECALL                  1
    # 136 CALL                     1
    # >>  146 STORE_GLOBAL             6 (_app)
    # 148 LOAD_CONST               0 (None)
    # 150 RETURN_VALUE

def create_window(window):
    # 0 MAKE_CELL                0 (window)
    # 915           2 RESUME                   0
    # 916           4 LOAD_CLOSURE             0 (window)
    # 6 BUILD_TUPLE              1
    # 8 LOAD_CONST               1 (<code object _create at 0x000001EBD7582150, file "webview\platforms\qt.py", line 916>)
    # 10 MAKE_FUNCTION            8 (closure)
    # 12 STORE_FAST               1 (_create)
    # 939          14 LOAD_DEREF               0 (window)
    # 16 LOAD_ATTR                0 (uid)
    # 26 LOAD_CONST               2 ('master')
    # 28 COMPARE_OP               2 (==)
    # 34 EXTENDED_ARG             1
    # 36 POP_JUMP_FORWARD_IF_FALSE   272 (to 582)
    # 941          38 LOAD_GLOBAL              2 (_state)
    # 50 LOAD_CONST               3 ('menu')
    # 52 BINARY_SUBSCR
    # 62 POP_JUMP_FORWARD_IF_FALSE    73 (to 210)
    # 942          64 LOAD_GLOBAL              5 (NULL + QMenuBar)
    # 76 PRECALL                  0
    # 80 CALL                     0
    # 90 STORE_GLOBAL             3 (_app_menu)
    # 943          92 LOAD_GLOBAL              6 (_app_menu)
    # 104 LOAD_METHOD              4 (setNativeMenuBar)
    # 126 LOAD_CONST               4 (False)
    # 128 PRECALL                  1
    # 132 CALL                     1
    # 142 POP_TOP
    # 944         144 LOAD_GLOBAL             11 (NULL + create_menu)
    # 156 LOAD_GLOBAL              2 (_state)
    # 168 LOAD_CONST               3 ('menu')
    # 170 BINARY_SUBSCR
    # 180 LOAD_GLOBAL              6 (_app_menu)
    # 192 PRECALL                  2
    # 196 CALL                     2
    # 206 POP_TOP
    # 208 JUMP_FORWARD             2 (to 214)
    # 946     >>  210 LOAD_CONST               0 (None)
    # 212 STORE_GLOBAL             3 (_app_menu)
    # 948     >>  214 LOAD_GLOBAL             13 (NULL + QApplication)
    # 226 LOAD_ATTR                7 (instance)
    # 236 PRECALL                  0
    # 240 CALL                     0
    # 250 JUMP_IF_TRUE_OR_POP     24 (to 300)
    # 252 LOAD_GLOBAL             13 (NULL + QApplication)
    # 264 LOAD_GLOBAL             16 (sys)
    # 276 LOAD_ATTR                9 (argv)
    # 286 PRECALL                  1
    # 290 CALL                     1
    # >>  300 STORE_GLOBAL            10 (_app)
    # 950         302 LOAD_GLOBAL             23 (NULL + signal)
    # 314 LOAD_ATTR               11 (signal)
    # 324 LOAD_GLOBAL             22 (signal)
    # 336 LOAD_ATTR               12 (SIGINT)
    # 346 LOAD_GLOBAL             26 (_sigint_handler)
    # 358 PRECALL                  2
    # 362 CALL                     2
    # 372 POP_TOP
    # 955         374 LOAD_GLOBAL             29 (NULL + QtCore)
    # 386 LOAD_ATTR               15 (QTimer)
    # 396 PRECALL                  0
    # 400 CALL                     0
    # 410 STORE_FAST               2 (timer)
    # 956         412 LOAD_FAST                2 (timer)
    # 414 LOAD_METHOD             16 (start)
    # 436 LOAD_CONST               5 (500)
    # 438 PRECALL                  1
    # 442 CALL                     1
    # 452 POP_TOP
    # 957         454 LOAD_FAST                2 (timer)
    # 456 LOAD_ATTR               17 (timeout)
    # 466 LOAD_METHOD             18 (connect)
    # 488 LOAD_CONST               6 (<code object <lambda> at 0x000001EBD7F1BE70, file "webview\platforms\qt.py", line 957>)
    # 490 MAKE_FUNCTION            0
    # 492 PRECALL                  1
    # 496 CALL                     1
    # 506 POP_TOP
    # 959         508 PUSH_NULL
    # 510 LOAD_FAST                1 (_create)
    # 512 PRECALL                  0
    # 516 CALL                     0
    # 526 POP_TOP
    # 960         528 LOAD_GLOBAL             20 (_app)
    # 540 LOAD_METHOD             19 (exec_)
    # 562 PRECALL                  0
    # 566 CALL                     0
    # 576 POP_TOP
    # 578 LOAD_CONST               0 (None)
    # 580 RETURN_VALUE
    # 962     >>  582 LOAD_GLOBAL             40 (_main_window_created)
    # 594 LOAD_METHOD             21 (wait)
    # 616 PRECALL                  0
    # 620 CALL                     0
    # 630 POP_TOP
    # 963         632 LOAD_GLOBAL             45 (NULL + list)
    # 644 LOAD_GLOBAL             46 (BrowserView)
    # 656 LOAD_ATTR               24 (instances)
    # 666 LOAD_METHOD             25 (values)
    # 688 PRECALL                  0
    # 692 CALL                     0
    # 702 PRECALL                  1
    # 706 CALL                     1
    # 716 LOAD_CONST               7 (0)
    # 718 BINARY_SUBSCR
    # 728 STORE_FAST               3 (i)
    # 964         730 LOAD_FAST                3 (i)
    # 732 LOAD_ATTR               26 (create_window_trigger)
    # 742 LOAD_METHOD             27 (emit)
    # 764 LOAD_FAST                1 (_create)
    # 766 PRECALL                  1
    # 770 CALL                     1
    # 780 POP_TOP
    # 782 LOAD_CONST               0 (None)
    # 784 RETURN_VALUE
    # Disassembly of <code object _create at 0x000001EBD7582150, file "webview\platforms\qt.py", line 916>:
    # 0 COPY_FREE_VARS           1
    # 916           2 RESUME                   0
    # 917           4 LOAD_GLOBAL              1 (NULL + BrowserView)
    # 16 LOAD_DEREF               3 (window)
    # 18 PRECALL                  1
    # 22 CALL                     1
    # 32 STORE_FAST               0 (browser)
    # 918          34 LOAD_FAST                0 (browser)
    # 36 LOAD_METHOD              1 (installEventFilter)
    # 58 LOAD_FAST                0 (browser)
    # 60 PRECALL                  1
    # 64 CALL                     1
    # 74 POP_TOP
    # 920          76 LOAD_DEREF               3 (window)
    # 78 LOAD_ATTR                2 (menu)
    # 88 POP_JUMP_FORWARD_IF_TRUE     7 (to 104)
    # 90 LOAD_GLOBAL              6 (_app_menu)
    # 102 POP_JUMP_FORWARD_IF_FALSE    56 (to 216)
    # 921     >>  104 LOAD_DEREF               3 (window)
    # 106 LOAD_ATTR                2 (menu)
    # 116 JUMP_IF_TRUE_OR_POP     12 (to 142)
    # 118 LOAD_GLOBAL              8 (_state)
    # 130 LOAD_CONST               1 ('menu')
    # 132 BINARY_SUBSCR
    # >>  142 STORE_FAST               1 (menu)
    # 922         144 LOAD_FAST                0 (browser)
    # 146 LOAD_METHOD              5 (menuBar)
    # 168 PRECALL                  0
    # 172 CALL                     0
    # 182 STORE_FAST               2 (window_menubar)
    # 923         184 LOAD_GLOBAL             13 (NULL + create_menu)
    # 196 LOAD_FAST                1 (menu)
    # 198 LOAD_FAST                2 (window_menubar)
    # 200 PRECALL                  2
    # 204 CALL                     2
    # 214 POP_TOP
    # 925     >>  216 LOAD_GLOBAL             14 (_main_window_created)
    # 228 LOAD_METHOD              8 (set)
    # 250 PRECALL                  0
    # 254 CALL                     0
    # 264 POP_TOP
    # 927         266 LOAD_DEREF               3 (window)
    # 268 LOAD_ATTR                9 (maximized)
    # 278 POP_JUMP_FORWARD_IF_FALSE    22 (to 324)
    # 928         280 LOAD_FAST                0 (browser)
    # 282 LOAD_METHOD             10 (showMaximized)
    # 304 PRECALL                  0
    # 308 CALL                     0
    # 318 POP_TOP
    # 320 LOAD_CONST               0 (None)
    # 322 RETURN_VALUE
    # 929     >>  324 LOAD_DEREF               3 (window)
    # 326 LOAD_ATTR               11 (minimized)
    # 336 POP_JUMP_FORWARD_IF_FALSE    42 (to 422)
    # 932         338 LOAD_FAST                0 (browser)
    # 340 LOAD_METHOD             12 (showNormal)
    # 362 PRECALL                  0
    # 366 CALL                     0
    # 376 POP_TOP
    # 933         378 LOAD_FAST                0 (browser)
    # 380 LOAD_METHOD             13 (showMinimized)
    # 402 PRECALL                  0
    # 406 CALL                     0
    # 416 POP_TOP
    # 418 LOAD_CONST               0 (None)
    # 420 RETURN_VALUE
    # 934     >>  422 LOAD_DEREF               3 (window)
    # 424 LOAD_ATTR               14 (hidden)
    # 434 POP_JUMP_FORWARD_IF_TRUE    22 (to 480)
    # 935         436 LOAD_FAST                0 (browser)
    # 438 LOAD_METHOD             15 (show)
    # 460 PRECALL                  0
    # 464 CALL                     0
    # 474 POP_TOP
    # 476 LOAD_CONST               0 (None)
    # 478 RETURN_VALUE
    # 936     >>  480 LOAD_DEREF               3 (window)
    # 482 LOAD_ATTR               14 (hidden)
    # 492 POP_JUMP_FORWARD_IF_FALSE    37 (to 568)
    # 937         494 LOAD_FAST                0 (browser)
    # 496 LOAD_ATTR               16 (pywebview_window)
    # 506 LOAD_ATTR               17 (events)
    # 516 LOAD_ATTR               18 (shown)
    # 526 LOAD_METHOD              8 (set)
    # 548 PRECALL                  0
    # 552 CALL                     0
    # 562 POP_TOP
    # 564 LOAD_CONST               0 (None)
    # 566 RETURN_VALUE
    # 936     >>  568 LOAD_CONST               0 (None)
    # 570 RETURN_VALUE
    # Disassembly of <code object <lambda> at 0x000001EBD7F1BE70, file "webview\platforms\qt.py", line 957>:
    # 957           0 RESUME                   0
    # 2 LOAD_CONST               0 (None)
    # 4 RETURN_VALUE

def set_title(title, uid):
    # 967           0 RESUME                   0
    # 968           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                1 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               2 (i)
    # 969          64 LOAD_FAST                2 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    23 (to 114)
    # 970          68 LOAD_FAST                2 (i)
    # 70 LOAD_METHOD              3 (set_title)
    # 92 LOAD_FAST                0 (title)
    # 94 PRECALL                  1
    # 98 CALL                     1
    # 108 POP_TOP
    # 110 LOAD_CONST               0 (None)
    # 112 RETURN_VALUE
    # 969     >>  114 LOAD_CONST               0 (None)
    # 116 RETURN_VALUE

def clear_cookies(uid):
    # 973           0 RESUME                   0
    # 974           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                0 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               1 (i)
    # 975          64 LOAD_FAST                1 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    22 (to 112)
    # 976          68 LOAD_FAST                1 (i)
    # 70 LOAD_METHOD              3 (clear_cookies)
    # 92 PRECALL                  0
    # 96 CALL                     0
    # 106 POP_TOP
    # 108 LOAD_CONST               0 (None)
    # 110 RETURN_VALUE
    # 975     >>  112 LOAD_CONST               0 (None)
    # 114 RETURN_VALUE

def get_cookies(uid):
    # 979           0 RESUME                   0
    # 980           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                0 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               1 (i)
    # 981          64 LOAD_FAST                1 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    20 (to 108)
    # 982          68 LOAD_FAST                1 (i)
    # 70 LOAD_METHOD              3 (get_cookies)
    # 92 PRECALL                  0
    # 96 CALL                     0
    # 106 RETURN_VALUE
    # 981     >>  108 LOAD_CONST               0 (None)
    # 110 RETURN_VALUE

def get_current_url(uid):
    # 985           0 RESUME                   0
    # 986           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                0 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               1 (i)
    # 987          64 LOAD_FAST                1 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    20 (to 108)
    # 988          68 LOAD_FAST                1 (i)
    # 70 LOAD_METHOD              3 (get_current_url)
    # 92 PRECALL                  0
    # 96 CALL                     0
    # 106 RETURN_VALUE
    # 987     >>  108 LOAD_CONST               0 (None)
    # 110 RETURN_VALUE

def load_url(url, uid):
    # 991           0 RESUME                   0
    # 992           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                1 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               2 (i)
    # 993          64 LOAD_FAST                2 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    23 (to 114)
    # 994          68 LOAD_FAST                2 (i)
    # 70 LOAD_METHOD              3 (load_url)
    # 92 LOAD_FAST                0 (url)
    # 94 PRECALL                  1
    # 98 CALL                     1
    # 108 POP_TOP
    # 110 LOAD_CONST               0 (None)
    # 112 RETURN_VALUE
    # 993     >>  114 LOAD_CONST               0 (None)
    # 116 RETURN_VALUE

def load_html(content, base_uri, uid):
    # 997           0 RESUME                   0
    # 998           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                2 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               3 (i)
    # 999          64 LOAD_FAST                3 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    24 (to 116)
    # 1000          68 LOAD_FAST                3 (i)
    # 70 LOAD_METHOD              3 (load_html)
    # 92 LOAD_FAST                0 (content)
    # 94 LOAD_FAST                1 (base_uri)
    # 96 PRECALL                  2
    # 100 CALL                     2
    # 110 POP_TOP
    # 112 LOAD_CONST               0 (None)
    # 114 RETURN_VALUE
    # 999     >>  116 LOAD_CONST               0 (None)
    # 118 RETURN_VALUE

def create_menu(app_menu_list, menubar):
    """
    Create the menu bar for the application for the provided QMenuBar object. Menu can be either a global
    application menu or a window-specific menu.

    Args:
        app_menu_list ([webview.menu.Menu])
        menubar (QMenuBar)
    """
    # 0 MAKE_CELL                4 (create_submenu)
    # 2 MAKE_CELL                5 (run_action)
    # 1003           4 RESUME                   0
    # 1013           6 LOAD_CONST               1 (<code object run_action at 0x000001EBD7E46560, file "webview\platforms\qt.py", line 1013>)
    # 8 MAKE_FUNCTION            0
    # 10 STORE_DEREF              5 (run_action)
    # 1016          12 LOAD_CLOSURE             4 (create_submenu)
    # 14 LOAD_CLOSURE             5 (run_action)
    # 16 BUILD_TUPLE              2
    # 18 LOAD_CONST               2 (<code object create_submenu at 0x000001EBD7756380, file "webview\platforms\qt.py", line 1016>)
    # 20 MAKE_FUNCTION            8 (closure)
    # 22 STORE_DEREF              4 (create_submenu)
    # 1033          24 LOAD_FAST                0 (app_menu_list)
    # 26 GET_ITER
    # >>   28 FOR_ITER                58 (to 146)
    # 30 STORE_FAST               2 (app_menu)
    # 1035          32 LOAD_FAST                2 (app_menu)
    # 34 LOAD_ATTR                0 (title)
    # 44 LOAD_CONST               3 ('__app__')
    # 46 COMPARE_OP               2 (==)
    # 52 POP_JUMP_FORWARD_IF_FALSE     1 (to 56)
    # 1036          54 JUMP_BACKWARD           14 (to 28)
    # 1037     >>   56 PUSH_NULL
    # 58 LOAD_DEREF               4 (create_submenu)
    # 60 LOAD_FAST                2 (app_menu)
    # 62 LOAD_ATTR                0 (title)
    # 72 LOAD_FAST                2 (app_menu)
    # 74 LOAD_ATTR                1 (items)
    # 84 LOAD_FAST                1 (menubar)
    # 86 PRECALL                  3
    # 90 CALL                     3
    # 100 STORE_FAST               3 (menu)
    # 1038         102 LOAD_FAST                1 (menubar)
    # 104 LOAD_METHOD              2 (addMenu)
    # 126 LOAD_FAST                3 (menu)
    # 128 PRECALL                  1
    # 132 CALL                     1
    # 142 POP_TOP
    # 144 JUMP_BACKWARD           59 (to 28)
    # 1033     >>  146 LOAD_CONST               4 (None)
    # 148 RETURN_VALUE
    # Disassembly of <code object run_action at 0x000001EBD7E46560, file "webview\platforms\qt.py", line 1013>:
    # 1013           0 RESUME                   0
    # 1014           2 LOAD_GLOBAL              1 (NULL + Thread)
    # 14 LOAD_FAST                0 (func)
    # 16 KW_NAMES                 1
    # 18 PRECALL                  1
    # 22 CALL                     1
    # 32 LOAD_METHOD              1 (start)
    # 54 PRECALL                  0
    # 58 CALL                     0
    # 68 POP_TOP
    # 70 LOAD_CONST               0 (None)
    # 72 RETURN_VALUE
    # Disassembly of <code object create_submenu at 0x000001EBD7756380, file "webview\platforms\qt.py", line 1016>:
    # 0 COPY_FREE_VARS           2
    # 1016           2 RESUME                   0
    # 1017           4 LOAD_FAST                2 (supermenu)
    # 6 LOAD_METHOD              0 (addMenu)
    # 28 LOAD_FAST                0 (title)
    # 30 PRECALL                  1
    # 34 CALL                     1
    # 44 STORE_FAST               3 (m)
    # 1018          46 LOAD_GLOBAL              2 (BrowserView)
    # 58 LOAD_ATTR                2 (global_menubar_other_objects)
    # 68 LOAD_METHOD              3 (append)
    # 90 LOAD_FAST                3 (m)
    # 92 PRECALL                  1
    # 96 CALL                     1
    # 106 POP_TOP
    # 1019         108 LOAD_FAST                1 (line_items)
    # 110 GET_ITER
    # >>  112 FOR_ITER               242 (to 598)
    # 114 STORE_FAST               4 (menu_line_item)
    # 1020         116 LOAD_GLOBAL              9 (NULL + isinstance)
    # 128 LOAD_FAST                4 (menu_line_item)
    # 130 LOAD_GLOBAL             10 (MenuSeparator)
    # 142 PRECALL                  2
    # 146 CALL                     2
    # 156 POP_JUMP_FORWARD_IF_FALSE    21 (to 200)
    # 1021         158 LOAD_FAST                3 (m)
    # 160 LOAD_METHOD              6 (addSeparator)
    # 182 PRECALL                  0
    # 186 CALL                     0
    # 196 POP_TOP
    # 198 JUMP_BACKWARD           44 (to 112)
    # 1022     >>  200 LOAD_GLOBAL              9 (NULL + isinstance)
    # 212 LOAD_FAST                4 (menu_line_item)
    # 214 LOAD_GLOBAL             14 (MenuAction)
    # 226 PRECALL                  2
    # 230 CALL                     2
    # 240 POP_JUMP_FORWARD_IF_FALSE   133 (to 508)
    # 1023         242 LOAD_GLOBAL             17 (NULL + QAction)
    # 254 LOAD_FAST                4 (menu_line_item)
    # 256 LOAD_ATTR                9 (title)
    # 266 PRECALL                  1
    # 270 CALL                     1
    # 280 STORE_FAST               5 (new_action)
    # 1024         282 LOAD_GLOBAL             21 (NULL + copy)
    # 294 LOAD_FAST                4 (menu_line_item)
    # 296 LOAD_ATTR               11 (function)
    # 306 PRECALL                  1
    # 310 CALL                     1
    # 320 STORE_FAST               6 (func)
    # 1025         322 LOAD_FAST                5 (new_action)
    # 324 LOAD_ATTR               12 (triggered)
    # 334 LOAD_METHOD             13 (connect)
    # 356 LOAD_GLOBAL             29 (NULL + partial)
    # 368 LOAD_DEREF               8 (run_action)
    # 370 LOAD_FAST                6 (func)
    # 372 PRECALL                  2
    # 376 CALL                     2
    # 386 PRECALL                  1
    # 390 CALL                     1
    # 400 POP_TOP
    # 1026         402 LOAD_FAST                3 (m)
    # 404 LOAD_METHOD             15 (addAction)
    # 426 LOAD_FAST                5 (new_action)
    # 428 PRECALL                  1
    # 432 CALL                     1
    # 442 POP_TOP
    # 1027         444 LOAD_GLOBAL              2 (BrowserView)
    # 456 LOAD_ATTR                2 (global_menubar_other_objects)
    # 466 LOAD_METHOD              3 (append)
    # 488 LOAD_FAST                5 (new_action)
    # 490 PRECALL                  1
    # 494 CALL                     1
    # 504 POP_TOP
    # 506 JUMP_BACKWARD          198 (to 112)
    # 1028     >>  508 LOAD_GLOBAL              9 (NULL + isinstance)
    # 520 LOAD_FAST                4 (menu_line_item)
    # 522 LOAD_GLOBAL             32 (Menu)
    # 534 PRECALL                  2
    # 538 CALL                     2
    # 548 POP_JUMP_FORWARD_IF_FALSE    23 (to 596)
    # 1029         550 PUSH_NULL
    # 552 LOAD_DEREF               7 (create_submenu)
    # 554 LOAD_FAST                4 (menu_line_item)
    # 556 LOAD_ATTR                9 (title)
    # 566 LOAD_FAST                4 (menu_line_item)
    # 568 LOAD_ATTR               17 (items)
    # 578 LOAD_FAST                3 (m)
    # 580 PRECALL                  3
    # 584 CALL                     3
    # 594 POP_TOP
    # >>  596 JUMP_BACKWARD          243 (to 112)
    # 1031     >>  598 LOAD_FAST                3 (m)
    # 600 RETURN_VALUE

def get_active_window():
    # 1041           0 RESUME                   0
    # 1042           2 LOAD_CONST               0 (None)
    # 4 STORE_FAST               0 (active_window)
    # 1043           6 NOP
    # 1044           8 LOAD_GLOBAL              0 (_app)
    # 20 LOAD_METHOD              1 (activeWindow)
    # 42 PRECALL                  0
    # 46 CALL                     0
    # 56 STORE_FAST               0 (active_window)
    # 58 JUMP_FORWARD             8 (to 76)
    # >>   60 PUSH_EXC_INFO
    # 1045          62 POP_TOP
    # 1046          64 POP_EXCEPT
    # 66 LOAD_CONST               0 (None)
    # 68 RETURN_VALUE
    # >>   70 COPY                     3
    # 72 POP_EXCEPT
    # 74 RERAISE                  1
    # 1048     >>   76 LOAD_FAST                0 (active_window)
    # 78 POP_JUMP_FORWARD_IF_FALSE     7 (to 94)
    # 1049          80 LOAD_FAST                0 (active_window)
    # 82 LOAD_ATTR                2 (pywebview_window)
    # 92 RETURN_VALUE
    # 1051     >>   94 LOAD_CONST               0 (None)
    # 96 RETURN_VALUE
    # ExceptionTable:
    # 8 to 56 -> 60 [0]
    # 60 to 62 -> 70 [1] lasti

def destroy_window(uid):
    # 1054           0 RESUME                   0
    # 1055           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                0 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               1 (i)
    # 1056          64 LOAD_FAST                1 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    22 (to 112)
    # 1057          68 LOAD_FAST                1 (i)
    # 70 LOAD_METHOD              3 (destroy_)
    # 92 PRECALL                  0
    # 96 CALL                     0
    # 106 POP_TOP
    # 108 LOAD_CONST               0 (None)
    # 110 RETURN_VALUE
    # 1056     >>  112 LOAD_CONST               0 (None)
    # 114 RETURN_VALUE

def hide(uid):
    # 1060           0 RESUME                   0
    # 1061           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                0 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               1 (i)
    # 1062          64 LOAD_FAST                1 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    22 (to 112)
    # 1063          68 LOAD_FAST                1 (i)
    # 70 LOAD_METHOD              3 (hide_)
    # 92 PRECALL                  0
    # 96 CALL                     0
    # 106 POP_TOP
    # 108 LOAD_CONST               0 (None)
    # 110 RETURN_VALUE
    # 1062     >>  112 LOAD_CONST               0 (None)
    # 114 RETURN_VALUE

def show(uid):
    # 1066           0 RESUME                   0
    # 1067           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                0 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               1 (i)
    # 1068          64 LOAD_FAST                1 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    22 (to 112)
    # 1069          68 LOAD_FAST                1 (i)
    # 70 LOAD_METHOD              3 (show_)
    # 92 PRECALL                  0
    # 96 CALL                     0
    # 106 POP_TOP
    # 108 LOAD_CONST               0 (None)
    # 110 RETURN_VALUE
    # 1068     >>  112 LOAD_CONST               0 (None)
    # 114 RETURN_VALUE

def maximize(uid):
    # 1072           0 RESUME                   0
    # 1073           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                0 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               1 (i)
    # 1074          64 LOAD_FAST                1 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    22 (to 112)
    # 1075          68 LOAD_FAST                1 (i)
    # 70 LOAD_METHOD              3 (maximize)
    # 92 PRECALL                  0
    # 96 CALL                     0
    # 106 POP_TOP
    # 108 LOAD_CONST               0 (None)
    # 110 RETURN_VALUE
    # 1074     >>  112 LOAD_CONST               0 (None)
    # 114 RETURN_VALUE

def minimize(uid):
    # 1078           0 RESUME                   0
    # 1079           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                0 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               1 (i)
    # 1080          64 LOAD_FAST                1 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    22 (to 112)
    # 1081          68 LOAD_FAST                1 (i)
    # 70 LOAD_METHOD              3 (minimize)
    # 92 PRECALL                  0
    # 96 CALL                     0
    # 106 POP_TOP
    # 108 LOAD_CONST               0 (None)
    # 110 RETURN_VALUE
    # 1080     >>  112 LOAD_CONST               0 (None)
    # 114 RETURN_VALUE

def restore(uid):
    # 1084           0 RESUME                   0
    # 1085           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                0 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               1 (i)
    # 1086          64 LOAD_FAST                1 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    22 (to 112)
    # 1087          68 LOAD_FAST                1 (i)
    # 70 LOAD_METHOD              3 (restore)
    # 92 PRECALL                  0
    # 96 CALL                     0
    # 106 POP_TOP
    # 108 LOAD_CONST               0 (None)
    # 110 RETURN_VALUE
    # 1086     >>  112 LOAD_CONST               0 (None)
    # 114 RETURN_VALUE

def toggle_fullscreen(uid):
    # 1090           0 RESUME                   0
    # 1091           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                0 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               1 (i)
    # 1092          64 LOAD_FAST                1 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    22 (to 112)
    # 1093          68 LOAD_FAST                1 (i)
    # 70 LOAD_METHOD              3 (toggle_fullscreen)
    # 92 PRECALL                  0
    # 96 CALL                     0
    # 106 POP_TOP
    # 108 LOAD_CONST               0 (None)
    # 110 RETURN_VALUE
    # 1092     >>  112 LOAD_CONST               0 (None)
    # 114 RETURN_VALUE

def set_on_top(uid, top):
    # 1096           0 RESUME                   0
    # 1097           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                0 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               2 (i)
    # 1098          64 LOAD_FAST                2 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    23 (to 114)
    # 1099          68 LOAD_FAST                2 (i)
    # 70 LOAD_METHOD              3 (set_on_top)
    # 92 LOAD_FAST                1 (top)
    # 94 PRECALL                  1
    # 98 CALL                     1
    # 108 POP_TOP
    # 110 LOAD_CONST               0 (None)
    # 112 RETURN_VALUE
    # 1098     >>  114 LOAD_CONST               0 (None)
    # 116 RETURN_VALUE

def resize(width, height, uid, fix_point):
    # 1102           0 RESUME                   0
    # 1103           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                2 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               4 (i)
    # 1104          64 LOAD_FAST                4 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    25 (to 118)
    # 1105          68 LOAD_FAST                4 (i)
    # 70 LOAD_METHOD              3 (resize_)
    # 92 LOAD_FAST                0 (width)
    # 94 LOAD_FAST                1 (height)
    # 96 LOAD_FAST                3 (fix_point)
    # 98 PRECALL                  3
    # 102 CALL                     3
    # 112 POP_TOP
    # 114 LOAD_CONST               0 (None)
    # 116 RETURN_VALUE
    # 1104     >>  118 LOAD_CONST               0 (None)
    # 120 RETURN_VALUE

def move(x, y, uid):
    # 1108           0 RESUME                   0
    # 1109           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                2 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               3 (i)
    # 1110          64 LOAD_FAST                3 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    24 (to 116)
    # 1111          68 LOAD_FAST                3 (i)
    # 70 LOAD_METHOD              3 (move_window)
    # 92 LOAD_FAST                0 (x)
    # 94 LOAD_FAST                1 (y)
    # 96 PRECALL                  2
    # 100 CALL                     2
    # 110 POP_TOP
    # 112 LOAD_CONST               0 (None)
    # 114 RETURN_VALUE
    # 1110     >>  116 LOAD_CONST               0 (None)
    # 118 RETURN_VALUE

def create_confirmation_dialog(title, message, uid):
    # 1114           0 RESUME                   0
    # 1115           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                2 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               3 (i)
    # 1116          64 LOAD_FAST                3 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    22 (to 112)
    # 1117          68 LOAD_FAST                3 (i)
    # 70 LOAD_METHOD              3 (create_confirmation_dialog)
    # 92 LOAD_FAST                0 (title)
    # 94 LOAD_FAST                1 (message)
    # 96 PRECALL                  2
    # 100 CALL                     2
    # 110 RETURN_VALUE
    # 1116     >>  112 LOAD_CONST               0 (None)
    # 114 RETURN_VALUE

def create_file_dialog(dialog_type, directory, allow_multiple, save_filename, file_types, uid):
    # 1120           0 RESUME                   0
    # 1122           2 LOAD_CONST               1 (<code object <listcomp> at 0x000001EBD7EF0130, file "webview\platforms\qt.py", line 1122>)
    # 4 MAKE_FUNCTION            0
    # 6 LOAD_FAST                4 (file_types)
    # 8 GET_ITER
    # 10 PRECALL                  0
    # 14 CALL                     0
    # 24 STORE_FAST               4 (file_types)
    # 1123          26 LOAD_CONST               2 (';;')
    # 28 LOAD_METHOD              0 (join)
    # 50 LOAD_FAST                4 (file_types)
    # 52 PRECALL                  1
    # 56 CALL                     1
    # 66 STORE_FAST               6 (file_filter)
    # 1125          68 LOAD_GLOBAL              2 (BrowserView)
    # 80 LOAD_ATTR                2 (instances)
    # 90 LOAD_METHOD              3 (get)
    # 112 LOAD_FAST                5 (uid)
    # 114 PRECALL                  1
    # 118 CALL                     1
    # 128 STORE_FAST               7 (i)
    # 1126         130 LOAD_FAST                7 (i)
    # 132 POP_JUMP_FORWARD_IF_FALSE    25 (to 184)
    # 1127         134 LOAD_FAST                7 (i)
    # 136 LOAD_METHOD              4 (create_file_dialog)
    # 1128         158 LOAD_FAST                0 (dialog_type)
    # 160 LOAD_FAST                1 (directory)
    # 162 LOAD_FAST                2 (allow_multiple)
    # 164 LOAD_FAST                3 (save_filename)
    # 166 LOAD_FAST                6 (file_filter)
    # 1127         168 PRECALL                  5
    # 172 CALL                     5
    # 182 RETURN_VALUE
    # 1126     >>  184 LOAD_CONST               0 (None)
    # 186 RETURN_VALUE
    # Disassembly of <code object <listcomp> at 0x000001EBD7EF0130, file "webview\platforms\qt.py", line 1122>:
    # 1122           0 RESUME                   0
    # 2 BUILD_LIST               0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER                24 (to 56)
    # 8 STORE_FAST               1 (s)
    # 10 LOAD_FAST                1 (s)
    # 12 LOAD_METHOD              0 (replace)
    # 34 LOAD_CONST               0 (';')
    # 36 LOAD_CONST               1 (' ')
    # 38 PRECALL                  2
    # 42 CALL                     2
    # 52 LIST_APPEND              2
    # 54 JUMP_BACKWARD           25 (to 6)
    # >>   56 RETURN_VALUE

def evaluate_js(script, uid, parse_json):
    # 1132           0 RESUME                   0
    # 1133           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                1 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               3 (i)
    # 1134          64 LOAD_FAST                3 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    22 (to 112)
    # 1135          68 LOAD_FAST                3 (i)
    # 70 LOAD_METHOD              3 (evaluate_js)
    # 92 LOAD_FAST                0 (script)
    # 94 LOAD_FAST                2 (parse_json)
    # 96 PRECALL                  2
    # 100 CALL                     2
    # 110 RETURN_VALUE
    # 1134     >>  112 LOAD_CONST               0 (None)
    # 114 RETURN_VALUE

def get_position(uid):
    # 1138           0 RESUME                   0
    # 1139           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                0 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               1 (i)
    # 1140          64 LOAD_FAST                1 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    60 (to 188)
    # 1141          68 LOAD_FAST                1 (i)
    # 70 LOAD_METHOD              3 (geometry)
    # 92 PRECALL                  0
    # 96 CALL                     0
    # 106 STORE_FAST               2 (position)
    # 1142         108 LOAD_FAST                2 (position)
    # 110 LOAD_METHOD              4 (x)
    # 132 PRECALL                  0
    # 136 CALL                     0
    # 146 LOAD_FAST                2 (position)
    # 148 LOAD_METHOD              5 (y)
    # 170 PRECALL                  0
    # 174 CALL                     0
    # 184 BUILD_TUPLE              2
    # 186 RETURN_VALUE
    # 1144     >>  188 LOAD_CONST               1 ((None, None))
    # 190 RETURN_VALUE

def get_size(uid):
    # 1147           0 RESUME                   0
    # 1148           2 LOAD_GLOBAL              0 (BrowserView)
    # 14 LOAD_ATTR                1 (instances)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_FAST                0 (uid)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               1 (i)
    # 1149          64 LOAD_FAST                1 (i)
    # 66 POP_JUMP_FORWARD_IF_FALSE    40 (to 148)
    # 1150          68 LOAD_FAST                1 (i)
    # 70 LOAD_METHOD              3 (width)
    # 92 PRECALL                  0
    # 96 CALL                     0
    # 106 LOAD_FAST                1 (i)
    # 108 LOAD_METHOD              4 (height)
    # 130 PRECALL                  0
    # 134 CALL                     0
    # 144 BUILD_TUPLE              2
    # 146 RETURN_VALUE
    # 1152     >>  148 LOAD_CONST               1 ((None, None))
    # 150 RETURN_VALUE

def get_screens():
    # 1155           0 RESUME                   0
    # 1157           2 LOAD_GLOBAL              1 (NULL + QApplication)
    # 14 LOAD_ATTR                1 (instance)
    # 24 PRECALL                  0
    # 28 CALL                     0
    # 38 JUMP_IF_TRUE_OR_POP     24 (to 88)
    # 40 LOAD_GLOBAL              1 (NULL + QApplication)
    # 52 LOAD_GLOBAL              4 (sys)
    # 64 LOAD_ATTR                3 (argv)
    # 74 PRECALL                  1
    # 78 CALL                     1
    # >>   88 STORE_GLOBAL             4 (_app)
    # 1158          90 LOAD_CONST               1 (<code object <listcomp> at 0x000001EBD777B0B0, file "webview\platforms\qt.py", line 1158>)
    # 92 MAKE_FUNCTION            0
    # 1160          94 LOAD_GLOBAL              8 (_app)
    # 106 LOAD_METHOD              5 (screens)
    # 128 PRECALL                  0
    # 132 CALL                     0
    # 1158         142 GET_ITER
    # 144 PRECALL                  0
    # 148 CALL                     0
    # 158 STORE_FAST               0 (screens)
    # 1163         160 LOAD_FAST                0 (screens)
    # 162 RETURN_VALUE
    # Disassembly of <code object <listcomp> at 0x000001EBD777B0B0, file "webview\platforms\qt.py", line 1158>:
    # 1158           0 RESUME                   0
    # 2 BUILD_LIST               0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER               165 (to 338)
    # 1160           8 STORE_FAST               1 (s)
    # 1159          10 LOAD_GLOBAL              1 (NULL + Screen)
    # 22 LOAD_FAST                1 (s)
    # 24 LOAD_METHOD              1 (geometry)
    # 46 PRECALL                  0
    # 50 CALL                     0
    # 60 LOAD_METHOD              2 (x)
    # 82 PRECALL                  0
    # 86 CALL                     0
    # 96 LOAD_FAST                1 (s)
    # 98 LOAD_METHOD              1 (geometry)
    # 120 PRECALL                  0
    # 124 CALL                     0
    # 134 LOAD_METHOD              3 (y)
    # 156 PRECALL                  0
    # 160 CALL                     0
    # 170 LOAD_FAST                1 (s)
    # 172 LOAD_METHOD              1 (geometry)
    # 194 PRECALL                  0
    # 198 CALL                     0
    # 208 LOAD_METHOD              4 (width)
    # 230 PRECALL                  0
    # 234 CALL                     0
    # 244 LOAD_FAST                1 (s)
    # 246 LOAD_METHOD              1 (geometry)
    # 268 PRECALL                  0
    # 272 CALL                     0
    # 282 LOAD_METHOD              5 (height)
    # 304 PRECALL                  0
    # 308 CALL                     0
    # 318 LOAD_FAST                1 (s)
    # 320 PRECALL                  5
    # 324 CALL                     5
    # 1158         334 LIST_APPEND              2
    # 336 JUMP_BACKWARD          166 (to 6)
    # >>  338 RETURN_VALUE

def add_tls_cert(certfile):
    # 1166           0 RESUME                   0
    # 1167           2 LOAD_GLOBAL              1 (NULL + QSslConfiguration)
    # 14 LOAD_ATTR                1 (defaultConfiguration)
    # 24 PRECALL                  0
    # 28 CALL                     0
    # 38 STORE_FAST               1 (config)
    # 1168          40 LOAD_FAST                1 (config)
    # 42 LOAD_METHOD              2 (caCertificates)
    # 64 PRECALL                  0
    # 68 CALL                     0
    # 78 STORE_FAST               2 (certs)
    # 1169          80 LOAD_GLOBAL              7 (NULL + QSslCertificate)
    # 92 LOAD_ATTR                4 (fromPath)
    # 102 LOAD_FAST                0 (certfile)
    # 104 PRECALL                  1
    # 108 CALL                     1
    # 118 LOAD_CONST               1 (0)
    # 120 BINARY_SUBSCR
    # 130 STORE_FAST               3 (cert)
    # 1170         132 LOAD_FAST                2 (certs)
    # 134 LOAD_METHOD              5 (append)
    # 156 LOAD_FAST                3 (cert)
    # 158 PRECALL                  1
    # 162 CALL                     1
    # 172 POP_TOP
    # 1171         174 LOAD_FAST                1 (config)
    # 176 LOAD_METHOD              6 (setCaCertificates)
    # 198 LOAD_FAST                2 (certs)
    # 200 PRECALL                  1
    # 204 CALL                     1
    # 214 POP_TOP
    # 1172         216 LOAD_GLOBAL              1 (NULL + QSslConfiguration)
    # 228 LOAD_ATTR                7 (setDefaultConfiguration)
    # 238 LOAD_FAST                1 (config)
    # 240 PRECALL                  1
    # 244 CALL                     1
    # 254 POP_TOP
    # 256 LOAD_CONST               0 (None)
    # 258 RETURN_VALUE
