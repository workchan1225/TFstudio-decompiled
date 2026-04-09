# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: view.pyc (Python 3.11)

__all__ = ('View', 'KeyEvent', 'Choreographer')
from jnius import JavaClass, JavaMethod, JavaStaticField, JavaStaticMethod, MetaJavaClass

def View():
    '''View'''
    __doc__ = "\n    Represents an Android view class with constants for system UI visibility flags.\n\n    Provides direct references to various system UI visibility constants, which\n    are used to control the appearance of the system user interface elements\n    such as the status bar, navigation bar, and fullscreen modes. This class\n    serves as a bridge to work with Java's Android View API in Python through\n    a metaclass-based approach.\n\n    Attributes\n    ----------\n    __javaclass__ : str\n        The name of the corresponding Java class used for this bridge.\n    SYSTEM_UI_FLAG_FULLSCREEN : JavaStaticField\n        Constant for enabling fullscreen mode in the system UI.\n    SYSTEM_UI_FLAG_HIDE_NAVIGATION : JavaStaticField\n        Constant for hiding the navigation bar in the system UI.\n    SYSTEM_UI_FLAG_IMMERSIVE : JavaStaticField\n        Constant for enabling immersive mode.\n    SYSTEM_UI_FLAG_IMMERSIVE_STICKY : JavaStaticField\n        Constant for enabling sticky immersive mode.\n    SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN : JavaStaticField\n        Constant for making the layout occupy the fullscreen area.\n    SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION : JavaStaticField\n        Constant for making the layout extend under the navigation bar.\n    SYSTEM_UI_FLAG_LAYOUT_STABLE : JavaStaticField\n        Constant for preventing layout changes when the system UI\n        visibility changes.\n    SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR : JavaStaticField\n        Constant for enabling light navigation bar mode.\n    SYSTEM_UI_FLAG_LIGHT_STATUS_BAR : JavaStaticField\n        Constant for enabling light status bar mode.\n    SYSTEM_UI_FLAG_LOW_PROFILE : JavaStaticField\n        Constant for enabling low-profile mode for system UI.\n    SYSTEM_UI_FLAG_VISIBLE : JavaStaticField\n        Constant for ensuring the system UI is visible.\n    SYSTEM_UI_LAYOUT_FLAGS : JavaStaticField\n        Combined constant for specifying multiple layout-related flags.\n    "
    __javaclass__ = 'android/view/View'
    SYSTEM_UI_FLAG_FULLSCREEN = JavaStaticField('I')
    SYSTEM_UI_FLAG_HIDE_NAVIGATION = JavaStaticField('I')
    SYSTEM_UI_FLAG_IMMERSIVE = JavaStaticField('I')
    SYSTEM_UI_FLAG_IMMERSIVE_STICKY = JavaStaticField('I')
    SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN = JavaStaticField('I')
    SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION = JavaStaticField('I')
    SYSTEM_UI_FLAG_LAYOUT_STABLE = JavaStaticField('I')
    SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR = JavaStaticField('I')
    SYSTEM_UI_FLAG_LIGHT_STATUS_BAR = JavaStaticField('I')
    SYSTEM_UI_FLAG_LOW_PROFILE = JavaStaticField('I')
    SYSTEM_UI_FLAG_VISIBLE = JavaStaticField('I')
    SYSTEM_UI_LAYOUT_FLAGS = JavaStaticField('I')

View = <NODE:27>(View, 'View', JavaClass, metaclass = MetaJavaClass)

def KeyEvent():
    '''KeyEvent'''
    __doc__ = '\n    Represents a wrapper for the Android KeyEvent class.\n\n    This class serves as a Python representation of the Android KeyEvent Java class, providing access\n    to Java static fields, and facilitating interaction with Android key event constants and properties.\n\n    Attributes:\n    KEYCODE_BACK : int\n        Static field representing the key code for the "Back" button in Android.\n    '
    __javaclass__ = 'android/view/KeyEvent'
    KEYCODE_BACK = JavaStaticField('I')
    ACTION_DOWN = JavaStaticField('I')
    getAction = JavaMethod('()I')

KeyEvent = <NODE:27>(KeyEvent, 'KeyEvent', JavaClass, metaclass = MetaJavaClass)

def Choreographer():
    '''Choreographer'''
    __javaclass__ = 'android/view/Choreographer'
    getInstance = JavaStaticMethod('()Landroid/view/Choreographer;')
    postFrameCallback = JavaMethod('(Landroid/view/Choreographer$FrameCallback;)V')
    removeFrameCallback = JavaMethod('(Landroid/view/Choreographer$FrameCallback;)V')

Choreographer = <NODE:27>(Choreographer, 'Choreographer', JavaClass, metaclass = MetaJavaClass)
