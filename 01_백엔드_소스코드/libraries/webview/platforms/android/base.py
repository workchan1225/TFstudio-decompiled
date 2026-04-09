# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

from threading import Semaphore
from android.activity import register_activity_lifecycle_callbacks
from android.runnable import run_on_ui_thread
from webview.platforms.android.event import EventDispatcher
from webview.platforms.android.jclass.view import Choreographer
from webview.platforms.android.jinterface.view import FrameCallback

class EventLoop(EventDispatcher):
    pass
# WARNING: Decompyle incomplete
