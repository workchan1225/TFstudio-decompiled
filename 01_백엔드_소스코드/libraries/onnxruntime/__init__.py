# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
ONNX Runtime is a performance-focused scoring engine for Open Neural Network Exchange (ONNX) models.
For more information on ONNX Runtime, please see `aka.ms/onnxruntime <https://aka.ms/onnxruntime/>`_
or the `Github project <https://github.com/microsoft/onnxruntime/>`_.
'''
import contextlib
__version__ = '1.24.2'
__author__ = 'Microsoft'

try:
    from onnxruntime.capi._pybind_state import ExecutionMode, ExecutionOrder, GraphOptimizationLevel, LoraAdapter, ModelMetadata, NodeArg, OrtAllocatorType, OrtArenaCfg, OrtCompileApiFlags, OrtDeviceMemoryType, OrtEpAssignedNode, OrtEpAssignedSubgraph, OrtEpDevice, OrtExecutionProviderDevicePolicy, OrtExternalInitializerInfo, OrtHardwareDevice, OrtHardwareDeviceType, OrtMemoryInfo, OrtMemoryInfoDeviceType, OrtMemType, OrtSparseFormat, OrtSyncStream, RunOptions, SessionIOBinding, SessionOptions, create_and_register_allocator, create_and_register_allocator_v2, disable_telemetry_events, enable_telemetry_events, get_all_providers, get_available_providers, get_build_info, get_device, get_ep_devices, get_version_string, has_collective_ops, register_execution_provider_library, set_default_logger_severity, set_default_logger_verbosity, set_global_thread_pool_sizes, set_seed, unregister_execution_provider_library
    import_capi_exception = None
except Exception:
    e = None
    import_capi_exception = e
    e = None
    del e
except:
    e = None
    del e

from onnxruntime.capi import onnxruntime_validation
if import_capi_exception:
    raise import_capi_exception
from onnxruntime.capi.onnxruntime_inference_collection import AdapterFormat, InferenceSession, IOBinding, ModelCompiler, OrtDevice, OrtValue, SparseTensor, copy_tensors

try:
    from  import experimental
except ImportError:
    pass

(package_name, version, cuda_version) = onnxruntime_validation.get_package_name_and_version_info()
if version:
    __version__ = version
onnxruntime_validation.check_distro_info()

def _get_package_version(package_name = None):
    PackageNotFoundError = PackageNotFoundError
    version = version
    import importlib.metadata
    
    try:
        package_version = version(package_name)
    except PackageNotFoundError:
        package_version = None

    return package_version


def _get_package_root(package_name = None, directory_name = None):
