# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: winforms.pyc (Python 3.11)

import ctypes
import logging
import os
import sys
import tempfile
import threading
import winreg
from ctypes import windll, wintypes
from platform import machine
from threading import Event, Semaphore
import clr
from webview import FileDialog, _state, settings, windows
from webview.guilib import forced_gui_
from webview.menu import Menu, MenuAction, MenuSeparator
from webview.screen import Screen
from webview.util import inject_base_uri, parse_file_type
from webview.window import FixPoint
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Collections')
clr.AddReference('System.Threading')
clr.AddReference('System.Reflection')

Forms
from Microsoft.Win32 import SystemEvents
import System.Windows.Forms, Windows
from System import Array, Environment, Func, Int32, IntPtr, Object, Type, UInt32
from System.Drawing import Color, ColorTranslator, Icon, Point, Size, SizeF
from System.Reflection import Assembly, BindingFlags
from System.Threading import ApartmentState, Thread, ThreadStart
kernel32 = ctypes.WinDLL('kernel32', use_last_error = True)
logger = logging.getLogger('pywebview')
cache_dir = None

def _is_new_version(current_version = None, new_version = None):
    new_range = new_version.split('.')
    cur_range = current_version.split('.')
    for index, _ in enumerate(new_range):
        if len(cur_range) > index:
            
            return None, int(new_range[index]) >= int(cur_range[index])
        return False


def _is_chromium():
    if settings['WEBVIEW2_RUNTIME_PATH']:
        return True
    
    def edge_build(key_type, key, description = None):
        
        try:
            windows_key = None
            if machine() == 'x86' or key_type == 'HKEY_CURRENT_USER':
                path = f'''Microsoft\\EdgeUpdate\\Clients\\{key}'''
            else:
                path = f'''WOW6432Node\\Microsoft\\EdgeUpdate\\Clients\\{key}'''
            windows_key = winreg.OpenKey(getattr(winreg, key_type), f'''SOFTWARE\\{path}''')
            (build, _) = winreg.QueryValueEx(windows_key, 'pv')
            
            try:
                None(None, None)
                return 
                with None:
                    if not None, str(build):
                        
                        try:
                            
                            try:
                                pass
                            except Exception:
                                pass

                            return '0'




    
    try:
        net_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\NET Framework Setup\\NDP\\v4\\Full')
        (version, _) = winreg.QueryValueEx(net_key, 'Release')
        if version < 394802:
            winreg.CloseKey(net_key)
            return False
        build_versions = [
            {
                'key': None,
                'description': 'Microsoft Edge WebView2 Runtime' },
            {
                'key': '{2CD8A007-E189-409D-A2C8-9AF4EF3C72AA}',
                'description': 'Microsoft Edge WebView2 Beta' },
            {
                'key': '{0D50BFEC-CD6A-4F9A-964C-C7416E3ACB10}',
                'description': 'Microsoft Edge WebView2 Developer' },
            {
                'key': '{65C35B14-6C1D-4122-AC46-7148CC9D6497}',
                'description': 'Microsoft Edge WebView2 Canary' }]
        for item in build_versions:
            for key_type in ('HKEY_CURRENT_USER', 'HKEY_LOCAL_MACHINE'):
                build = edge_build(key_type, item['key'], item['description'])
                if _is_new_version('86.0.622.0', build):
                    winreg.CloseKey(net_key)
                    return True
                
                try:
                    pass
                except Exception:
                    e = None
                    logger.exception(e)
                    
                    try:
                        e = None
                        del e
                    e = None
                    del e
                    try:
                        winreg.CloseKey(net_key)
                    except:
                        winreg.CloseKey(net_key)

                    return False



is_cef = forced_gui_ == 'cef'
if not is_cef:
    if _is_chromium():
        is_chromium = forced_gui_ != 'mshtml'
        if is_cef:
            from  import cef as CEF
            IWebBrowserInterop = object
            logger.debug('Using WinForms / CEF')
            renderer = 'cef'
        elif is_chromium:
            from  import edgechromium as Chromium
            IWebBrowserInterop = object
            logger.debug('Using WinForms / Chromium')
            renderer = 'edgechromium'
        else:
            from  import mshtml as IE
            logger.warning('MSHTML is deprecated. See https://pywebview.flowrl.com/guide/web_engine.html on details how to use Edge Chromium')
            logger.debug('Using WinForms / MSHTML')
            IE._set_ie_mode()
            renderer = 'mshtml'

def DwmSetWindowAttribute(hwnd, attr, value, size = (4,)):
    DwmSetWindowAttribute = ctypes.windll.dwmapi.DwmSetWindowAttribute
    DwmSetWindowAttribute.argtypes = [
        wintypes.HWND,
        wintypes.DWORD,
        ctypes.c_void_p,
        wintypes.DWORD]
    return DwmSetWindowAttribute(hwnd, attr, ctypes.byref(ctypes.c_int(value)), size)


def ExtendFrameIntoClientArea(hwnd):
    
    class _MARGINS(ctypes.Structure):
        _fields_ = [
            ('cxLeftWidth', ctypes.c_int),
            ('cxRightWidth', ctypes.c_int),
            ('cyTopHeight', ctypes.c_int),
            ('cyBottomHeight', ctypes.c_int)]

    DwmExtendFrameIntoClientArea = ctypes.windll.dwmapi.DwmExtendFrameIntoClientArea
    m = _MARGINS()
    m.cxLeftWidth = 1
    m.cxRightWidth = 1
    m.cyTopHeight = 1
    m.cyBottomHeight = 1
    return DwmExtendFrameIntoClientArea(hwnd, ctypes.byref(m))


class BrowserView:
    instances = { }
    
    class BrowserForm(WinForms.Form):
        pass
    # WARNING: Decompyle incomplete

    alert = (lambda message: WinForms.MessageBox.Show(str(message)))()


class OpenFolderDialog:
    foldersFilter = 'Folders|\n'
    flags = BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic
    windowsFormsAssembly = Assembly.LoadWithPartialName('System.Windows.Forms')
    iFileDialogType = windowsFormsAssembly.GetType('System.Windows.Forms.FileDialogNative+IFileDialog')
    OpenFileDialogType = windowsFormsAssembly.GetType('System.Windows.Forms.OpenFileDialog')
    FileDialogType = windowsFormsAssembly.GetType('System.Windows.Forms.FileDialog')
    createVistaDialogMethodInfo = OpenFileDialogType.GetMethod('CreateVistaDialog', flags)
    onBeforeVistaDialogMethodInfo = OpenFileDialogType.GetMethod('OnBeforeVistaDialog', flags)
    getOptionsMethodInfo = FileDialogType.GetMethod('GetOptions', flags)
    setOptionsMethodInfo = iFileDialogType.GetMethod('SetOptions', flags)
    fosPickFoldersBitFlag = windowsFormsAssembly.GetType('System.Windows.Forms.FileDialogNative+FOS').GetField('FOS_PICKFOLDERS').GetValue(None)
    vistaDialogEventsConstructorInfo = windowsFormsAssembly.GetType('System.Windows.Forms.FileDialog+VistaDialogEvents').GetConstructor(flags, None, [
        FileDialogType], [])
    adviseMethodInfo = iFileDialogType.GetMethod('Advise')
    unadviseMethodInfo = iFileDialogType.GetMethod('Unadvise')
    showMethodInfo = iFileDialogType.GetMethod('Show')
    show = (lambda cls, parent, initialDirectory, allow_multiple, title = (None, None, False, None): openFileDialog = WinForms.OpenFileDialog()openFileDialog.InitialDirectory = initialDirectoryopenFileDialog.Title = titleopenFileDialog.Filter = OpenFolderDialog.foldersFilteropenFileDialog.AddExtension = FalseopenFileDialog.CheckFileExists = FalseopenFileDialog.DereferenceLinks = TrueopenFileDialog.Multiselect = allow_multipleopenFileDialog.RestoreDirectory = TrueiFileDialog = OpenFolderDialog.createVistaDialogMethodInfo.Invoke(openFileDialog, [])OpenFolderDialog.onBeforeVistaDialogMethodInfo.Invoke(openFileDialog, [
iFileDialog])options = OpenFolderDialog.getOptionsMethodInfo.Invoke(openFileDialog, [])options = options.op_BitwiseOr(OpenFolderDialog.fosPickFoldersBitFlag)OpenFolderDialog.setOptionsMethodInfo.Invoke(iFileDialog, [
options])adviseParametersWithOutputConnectionToken = Array[Object]([
OpenFolderDialog.vistaDialogEventsConstructorInfo.Invoke([
openFileDialog]),
UInt32(0)])OpenFolderDialog.adviseMethodInfo.Invoke(iFileDialog, adviseParametersWithOutputConnectionToken)dwCookie = adviseParametersWithOutputConnectionToken.GetValue(1)try:
result = OpenFolderDialog.showMethodInfo.Invoke(iFileDialog, [
parent.Handle if parent else None])if result == 0:
OpenFolderDialog.unadviseMethodInfo.Invoke(iFileDialog, [
UInt32(dwCookie)])tuple(openFileDialog.FileNames)OpenFolderDialog.unadviseMethodInfo.Invoke(iFileDialog, [
UInt32(dwCookie)])Noneexcept:
OpenFolderDialog.unadviseMethodInfo.Invoke(iFileDialog, [
UInt32(dwCookie)]))()

_main_window_created = Event()
_main_window_created.clear()
_already_set_up_app = False

def init_storage():
    global cache_dir, cache_dir
    if _state['private_mode'] or _state['storage_path']:
        
        try:
            data_folder = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData)
            if not os.access(data_folder, os.W_OK):
                data_folder = Environment.GetFolderPath(Environment.SpecialFolder.UserProfile)
            if not _state['storage_path']:
                cache_dir = os.path.join(data_folder, 'pywebview')
                if not os.path.exists(cache_dir):
                    os.makedirs(cache_dir)
                    return None
                return None
            except Exception:
                logger.exception(f'''Cache directory {cache_dir} creation failed''')
                return None
            cache_dir = tempfile.TemporaryDirectory().name
            return None



def setup_app():
    global _already_set_up_app
    if _already_set_up_app:
        return None
    None.Application.EnableVisualStyles()
    WinForms.Application.SetCompatibleTextRenderingDefault(False)
    _already_set_up_app = True


def create_window(window):
    pass
# WARNING: Decompyle incomplete


def set_title(title, uid):
    pass
# WARNING: Decompyle incomplete


def create_confirmation_dialog(title, message, uid):
    i = BrowserView.instances.get(uid)
    if not i:
        return None
    result = None.MessageBox.Show(message, title, WinForms.MessageBoxButtons.OKCancel)
    return result == WinForms.DialogResult.OK


def create_file_dialog(dialog_type, directory, allow_multiple, save_filename, file_types, uid):
    i = BrowserView.instances.get(uid)
    if not i:
        return None
    if not None:
        directory = os.environ['HOMEPATH']
    
    try:
        if dialog_type == FileDialog.FOLDER:
            file_path = OpenFolderDialog.show(i, directory, allow_multiple)
        elif dialog_type == FileDialog.OPEN:
            dialog = WinForms.OpenFileDialog()
            dialog.Multiselect = allow_multiple
            dialog.InitialDirectory = directory
            dialog.RestoreDirectory = True
            result = dialog.ShowDialog(i)
            if result == WinForms.DialogResult.OK:
                file_path = tuple(dialog.FileNames)
            else:
                file_path = None
        elif dialog_type == FileDialog.SAVE:
            dialog = WinForms.SaveFileDialog()
            dialog.InitialDirectory = directory
            dialog.RestoreDirectory = True
            dialog.FileName = save_filename
            result = dialog.ShowDialog(i)
        return file_path
    except:
        logger.exception('Error invoking %s dialog', dialog_type)
        return None



def clear_cookies(uid):
    if is_cef:
        CEF.clear_cookies(uid)
    i = BrowserView.instances.get(uid)
    if i:
        i.clear_cookies()
        return None


def get_cookies(uid):
    if is_cef:
        return CEF.get_cookies(uid)
    i = None.instances.get(uid)
    if i:
        return i.get_cookies()


def get_current_url(uid):
    if is_cef:
        return CEF.get_current_url(uid)
    i = None.instances.get(uid)
    if i:
        return i.browser.url


def load_url(url, uid):
    i = BrowserView.instances.get(uid)
    if not i:
        return None
    if None:
        CEF.load_url(url, uid)
        return None
    None.load_url(url)


def load_html(content, base_uri, uid):
    i = BrowserView.instances.get(uid)
    if is_cef:
        CEF.load_html(inject_base_uri(content, base_uri), uid)
        return None
    if None:
        i.load_html(content, base_uri)
        return None


def get_active_window():
    active_window = None
    
    try:
        active_window = WinForms.Form.ActiveForm
    except:
        return None

    if active_window:
        for uid, browser_view_instance in BrowserView.instances.items():
            if browser_view_instance.Handle == active_window.Handle:
                
                return None, browser_view_instance.pywebview_window
            return None


def show(uid):
    i = BrowserView.instances.get(uid)
    if i:
        i.show()
        return None


def hide(uid):
    i = BrowserView.instances.get(uid)
    if i:
        i.hide()
        return None


def toggle_fullscreen(uid):
    i = BrowserView.instances.get(uid)
    if i:
        i.toggle_fullscreen()
        return None


def set_on_top(uid, on_top):
    i = BrowserView.instances.get(uid)
    if i:
        i.TopMost = on_top
        return None


def resize(width, height, uid, fix_point):
    i = BrowserView.instances.get(uid)
    if i:
        i.resize(width, height, fix_point)
        return None


def move(x, y, uid):
    i = BrowserView.instances.get(uid)
    if i:
        i.move(x, y)
        return None


def maximize(uid):
    i = BrowserView.instances.get(uid)
    if i:
        i.maximize()
        return None


def minimize(uid):
    i = BrowserView.instances.get(uid)
    if i:
        i.minimize()
        return None


def restore(uid):
    i = BrowserView.instances.get(uid)
    if i:
        i.restore()
        return None


def destroy_window(uid):
    pass
# WARNING: Decompyle incomplete


def evaluate_js(script, uid, parse_json, result_id = (None,)):
    if is_cef:
        return CEF.evaluate_js(script, result_id, parse_json, uid)
    i = None.instances.get(uid)
    if i:
        return i.evaluate_js(script, parse_json)


def get_position(uid):
    i = BrowserView.instances.get(uid)
    if i:
        return (i.Left, i.Top)


def get_size(uid):
    i = BrowserView.instances.get(uid)
    if i:
        size = i.Size
        return (size.Width, size.Height)


def get_screens():
    screens = WinForms.Screen.AllScreens()
    return screens


def add_tls_cert(_):
    pass
