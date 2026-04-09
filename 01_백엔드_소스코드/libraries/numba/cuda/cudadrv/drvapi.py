# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: drvapi.pyc (Python 3.11)

from ctypes import c_byte, c_char_p, c_float, c_int, c_size_t, c_uint, c_uint8, c_void_p, py_object, CFUNCTYPE, POINTER
from numba.cuda.cudadrv import _extras
cu_device = c_int
cu_device_attribute = c_int
cu_context = c_void_p
cu_module = c_void_p
cu_jit_option = c_int
cu_jit_input_type = c_int
cu_function = c_void_p
cu_device_ptr = c_size_t
cu_stream = c_void_p
cu_event = c_void_p
cu_link_state = c_void_p
cu_function_attribute = c_int
cu_ipc_mem_handle = c_byte * _extras.CUDA_IPC_HANDLE_SIZE
cu_uuid = c_byte * 16
cu_stream_callback_pyobj = CFUNCTYPE(None, cu_stream, c_int, py_object)
cu_occupancy_b2d_size = CFUNCTYPE(c_size_t, c_int)
CU_STREAM_DEFAULT = 0
CU_STREAM_LEGACY = 1
CU_STREAM_PER_THREAD = 2
# WARNING: Decompyle incomplete
