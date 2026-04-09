# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fetch.pyc (Python 3.11)

"""
Support for streaming http requests in emscripten.

A few caveats -

If your browser (or Node.js) has WebAssembly JavaScript Promise Integration enabled
https://github.com/WebAssembly/js-promise-integration/blob/main/proposals/js-promise-integration/Overview.md
*and* you launch pyodide using `pyodide.runPythonAsync`, this will fetch data using the
JavaScript asynchronous fetch api (wrapped via `pyodide.ffi.call_sync`). In this case
timeouts and streaming should just work.

Otherwise, it uses a combination of XMLHttpRequest and a web-worker for streaming.

This approach has several caveats:

Firstly, you can't do streaming http in the main UI thread, because atomics.wait isn't allowed.
Streaming only works if you're running pyodide in a web worker.

Secondly, this uses an extra web worker and SharedArrayBuffer to do the asynchronous fetch
operation, so it requires that you have crossOriginIsolation enabled, by serving over https
(or from localhost) with the two headers below set:

    Cross-Origin-Opener-Policy: same-origin
    Cross-Origin-Embedder-Policy: require-corp

You can tell if cross origin isolation is successfully enabled by looking at the global crossOriginIsolated variable in
JavaScript console. If it isn't, streaming requests will fallback to XMLHttpRequest, i.e. getting the whole
request into a buffer and then returning it. it shows a warning in the JavaScript console in this case.

Finally, the webworker which does the streaming fetch is created on initial import, but will only be started once
control is returned to javascript. Call `await wait_for_streaming_ready()` to wait for streaming fetch.

NB: in this code, there are a lot of JavaScript objects. They are named js_*
to make it clear what type of object they are.
"""
from __future__ import annotations
import io
import json
from email.parser import Parser
from importlib.resources import files
from typing import TYPE_CHECKING, Any
import js
from pyodide.ffi import JsArray, JsException, JsProxy, to_js
if TYPE_CHECKING:
    from typing_extensions import Buffer
from request import EmscriptenRequest
from response import EmscriptenResponse
HEADERS_TO_IGNORE = ('user-agent',)
SUCCESS_HEADER = -1
SUCCESS_EOF = -2
ERROR_TIMEOUT = -3
ERROR_EXCEPTION = -4

class _RequestError(Exception):
    pass
# WARNING: Decompyle incomplete


class _StreamingError(_RequestError):
    pass


class _TimeoutError(_RequestError):
    pass


def _obj_from_dict(dict_val = None):
    return to_js(dict_val, dict_converter = js.Object.fromEntries)


class _ReadStream(io.RawIOBase):
    pass
# WARNING: Decompyle incomplete


class _StreamingFetcher:
    
    def __init__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def send(self = None, request = None):
        headers = request.headers.items()()
        body = request.body
        fetch_data = {
            'headers': headers,
            'body': to_js(body),
            'method': request.method }
        timeout = int(1000 * request.timeout) if request.timeout > 0 else None
        js_shared_buffer = js.SharedArrayBuffer.new(1048576)
        js_int_buffer = js.Int32Array.new(js_shared_buffer)
        js_byte_buffer = js.Uint8Array.new(js_shared_buffer, 8)
        js.Atomics.store(js_int_buffer, 0, ERROR_TIMEOUT)
        js.Atomics.notify(js_int_buffer, 0)
        js_absolute_url = js.URL.new(request.url, js.location).href
        self.js_worker.postMessage(_obj_from_dict({
            'buffer': js_shared_buffer,
            'url': js_absolute_url,
            'fetchParams': fetch_data }))
        js.Atomics.wait(js_int_buffer, 0, ERROR_TIMEOUT, timeout)
        if js_int_buffer[0] == ERROR_TIMEOUT:
            raise _TimeoutError('Timeout connecting to streaming request', request = request, response = None)
        if js_int_buffer[0] == SUCCESS_HEADER:
            string_len = js_int_buffer[1]
            js_decoder = js.TextDecoder.new()
            json_str = js_decoder.decode(js_byte_buffer.slice(0, string_len))
            response_obj = json.loads(json_str)
            return EmscriptenResponse(request = request, status_code = response_obj['status'], headers = response_obj['headers'], body = _ReadStream(js_int_buffer, js_byte_buffer, request.timeout, self.js_worker, response_obj['connectionID'], request))
        if (lambda .0: pass# WARNING: Decompyle incomplete
)[0] == ERROR_EXCEPTION:
            string_len = js_int_buffer[1]
            js_decoder = js.TextDecoder.new()
            json_str = js_decoder.decode(js_byte_buffer.slice(0, string_len))
            raise _StreamingError(f'''Exception thrown in fetch: {json_str}''', request = request, response = None)
        raise _StreamingError(f'''Unknown status from worker in fetch: {js_int_buffer[0]}''', request = request, response = None)



class _JSPIReadStream(io.RawIOBase):
    pass
# WARNING: Decompyle incomplete


def is_in_browser_main_thread():
