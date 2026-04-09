# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: debughelpers.pyc (Python 3.11)

from __future__ import annotations
import typing as t
from blueprints import Blueprint
from globals import request_ctx
from sansio.app import App

class UnexpectedUnicodeError(UnicodeError, AssertionError):
    '''Raised in places where we want some better error reporting for
    unexpected unicode or binary data.
    '''
    pass


class DebugFilesKeyError(AssertionError, KeyError):
    '''Raised from request.files during debugging.  The idea is that it can
    provide a better error message than just a generic KeyError/BadRequest.
    '''
    
    def __init__(self, request, key):
        form_matches = request.form.getlist(key)
        buf = [
            f'''You tried to access the file {key!r} in the request.files dictionary but it does not exist. The mimetype for the request is {request.mimetype!r} instead of \'multipart/form-data\' which means that no file contents were transmitted. To fix this error you should provide enctype="multipart/form-data" in your form.''']
        if form_matches:
            names = (lambda .0: pass# WARNING: Decompyle incomplete
)(form_matches())
            buf.append(f'''\n\nThe browser instead transmitted some file names. This was submitted: {names}''')
        self.msg = ''.join(buf)

    
    def __str__(self):
        return self.msg



class FormDataRoutingRedirect(AssertionError):
    pass
# WARNING: Decompyle incomplete


def attach_enctype_error_multidict(request):
    '''Patch ``request.files.__getitem__`` to raise a descriptive error
    about ``enctype=multipart/form-data``.

    :param request: The request to patch.
    :meta private:
    '''
    pass
# WARNING: Decompyle incomplete


def _dump_loader_info(loader = None):
    pass
# WARNING: Decompyle incomplete


def explain_template_loading_attempts(app = None, template = None, attempts = None):
    '''This should help developers understand what failed'''
    info = [
        f'''Locating template {template!r}:''']
    total_found = 0
    blueprint = None
# WARNING: Decompyle incomplete
