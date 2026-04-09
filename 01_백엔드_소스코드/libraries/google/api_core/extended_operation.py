# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: extended_operation.pyc (Python 3.11)

'''Futures for extended long-running operations returned from Google Cloud APIs.

These futures can be used to synchronously wait for the result of a
long-running operations using :meth:`ExtendedOperation.result`:

.. code-block:: python

    extended_operation = my_api_client.long_running_method()

    extended_operation.result()

Or asynchronously using callbacks and :meth:`Operation.add_done_callback`:

.. code-block:: python

    extended_operation = my_api_client.long_running_method()

    def my_callback(ex_op):
        print(f"Operation {ex_op.name} completed")

    extended_operation.add_done_callback(my_callback)

'''
import threading
from google.api_core import exceptions
from google.api_core.future import polling

class ExtendedOperation(polling.PollingFuture):
    pass
# WARNING: Decompyle incomplete
