# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: guilib.pyc (Python 3.11)

from __future__ import annotations
import logging
import os
import platform
import sys
from types import ModuleType
from typing import Any, Callable, cast, get_args
from typing_extensions import Literal, TypeAlias
from webview import WebViewException
GUIType: 'TypeAlias' = Literal[('qt', 'gtk', 'cef', 'mshtml', 'edgechromium', 'android', 'cocoa')]
GUI_TYPES = list(get_args(GUIType))
logger = logging.getLogger('pywebview')
guilib: 'ModuleType | None' = None
forced_gui_: 'GUIType | None' = None

def initialize(forced_gui = None):
    global forced_gui_
    
    def import_android():
        global guilib
        
        try:
            
            android
            logger.debug('Using Kivy')
            return True
        except (ImportError, ValueError):
            logger.exception('Kivy cannot be loaded')
            return False


    
    def import_gtk():
        global guilib
        
        try:
            
            gtk
            logger.debug('Using GTK')
            return True
        except (ImportError, ValueError):
            logger.exception('GTK cannot be loaded')
            return False


    
    def import_qt():
        global guilib
        
        try:
            
            qt
            return True
        except ImportError:
            logger.exception('QT cannot be loaded')
            return False


    
    def import_cocoa():
        global guilib
        
        try:
            
            cocoa
            return True
        except ImportError:
            logger.exception('PyObjC cannot be loaded')
            return False


    
    def import_winforms():
        global guilib
        
        try:
            
            winforms
            return True
        except ImportError:
            logger.exception('pythonnet cannot be loaded')
            return False


    
    def try_import(guis = None):
        pass
    # WARNING: Decompyle incomplete

    if not forced_gui:
        forced_gui = 'qt' if 'KDE_FULL_SESSION' in os.environ else None
        forced_gui = cast(GUIType, os.environ['PYWEBVIEW_GUI'].lower() if 'PYWEBVIEW_GUI' in os.environ and os.environ['PYWEBVIEW_GUI'].lower() in GUI_TYPES else forced_gui)
    forced_gui_ = forced_gui
    if platform.system() == 'Darwin':
        if forced_gui == 'qt':
            guis = [
                import_qt,
                import_cocoa]
        else:
            guis = [
                import_cocoa,
                import_qt]
        if not try_import(guis):
            raise WebViewException('You must have either PyObjC (for Cocoa support) or Qt with Python bindings installed in order to use pywebview.')
    elif hasattr(sys, 'getandroidapilevel'):
        try_import([
            import_android])
    elif platform.system() == 'Linux' or platform.system() == 'OpenBSD':
        if forced_gui == 'qt':
            guis = [
                import_qt,
                import_gtk]
        else:
            guis = [
                import_gtk,
                import_qt]
        if not try_import(guis):
            raise WebViewException('You must have either QT or GTK with Python extensions installed in order to use pywebview.')
    elif platform.system() == 'Windows':
        if forced_gui == 'qt':
            guis = [
                import_qt,
                import_winforms]
        else:
            guis = [
                import_winforms]
        if not try_import(guis):
            raise WebViewException('You must have pythonnet installed in order to use pywebview.')
    else:
        raise WebViewException('Unsupported platform. Only Windows, Linux, OS X, OpenBSD are supported.')
    guilib.setup_app()
    return guilib
