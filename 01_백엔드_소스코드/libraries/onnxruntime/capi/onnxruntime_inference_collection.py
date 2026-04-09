# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: onnxruntime_inference_collection.pyc (Python 3.11)

from __future__ import annotations
import collections
import collections.abc as collections
import os
import typing
import warnings
from collections.abc import Callable, Sequence
from typing import Any
from onnxruntime.capi import _pybind_state as C
if typing.TYPE_CHECKING:
    import numpy as np
    from numpy.typing import typing as npt
    import onnxruntime

def get_ort_device_type(device_type = None):
    if device_type == 'cuda':
        return C.OrtDevice.cuda()
    if None == 'cann':
        return C.OrtDevice.cann()
    if None == 'cpu':
        return C.OrtDevice.cpu()
    if None == 'dml':
        return C.OrtDevice.dml()
    if None == 'webgpu':
        return C.OrtDevice.webgpu()
    if None == 'gpu':
        return C.OrtDevice.gpu()
    if None == 'npu':
        return C.OrtDevice.npu()
    raise None('Unsupported device type: ' + device_type)


class AdapterFormat:
    '''
    This class is used to create adapter files from python structures
    '''
    
    def __init__(self = None, adapter = None):
        pass
    # WARNING: Decompyle incomplete

    read_adapter = (lambda file_path = None: AdapterFormat(C.AdapterFormat.read_adapter(file_path)))()
    
    def export_adapter(self = None, file_path = None):
        '''
        This function writes a file at the specified location
        in onnxrunitme adapter format containing Lora parameters.

        :param file_path: absolute path for the adapter
        '''
        self._adapter.export_adapter(file_path)

    
    def get_format_version(self = None):
        return self._adapter.format_version

    
    def set_adapter_version(self = None, adapter_version = None):
        self._adapter.adapter_version = adapter_version

    
    def get_adapter_version(self = None):
        return self._adapter.adapter_version

    
    def set_model_version(self = None, model_version = None):
        self._adapter.model_version = model_version

    
    def get_model_version(self = None):
        return self._adapter.model_version

    
    def set_parameters(self = None, params = None):
        self._adapter.parameters = params.items()()

    
    def get_parameters(self = None):
        return self._adapter.parameters.items()()



def check_and_normalize_provider_args(providers = None, provider_options = None, available_provider_names = None):
    """
    Validates the 'providers' and 'provider_options' arguments and returns a
        normalized version.

    :param providers: Optional sequence of providers in order of decreasing
        precedence. Values can either be provider names or tuples of
        (provider name, options dict).
    :param provider_options: Optional sequence of options dicts corresponding
        to the providers listed in 'providers'.
    :param available_provider_names: The available provider names.

    :return: Tuple of (normalized 'providers' sequence, normalized
        'provider_options' sequence).

    'providers' can contain either names or names and options. When any options
        are given in 'providers', 'provider_options' should not be used.

    The normalized result is a tuple of:
    1. Sequence of provider names in the same order as 'providers'.
    2. Sequence of corresponding provider options dicts with string keys and
        values. Unspecified provider options yield empty dicts.
    """
    pass
# WARNING: Decompyle incomplete


class Session:
    '''
    This is the main class used to run a model.
    '''
    
    def __init__(self = None, enable_fallback = None):
        self._sess = None
        self._enable_fallback = enable_fallback

    
    def get_session_options(self = None):
        '''Return the session options. See :class:`onnxruntime.SessionOptions`.'''
        return self._sess_options

    
    def get_inputs(self = None):
        '''Return the inputs metadata as a list of :class:`onnxruntime.NodeArg`.'''
        return self._inputs_meta

    
    def get_outputs(self = None):
        '''Return the outputs metadata as a list of :class:`onnxruntime.NodeArg`.'''
        return self._outputs_meta

    
    def get_overridable_initializers(self = None):
        '''Return the inputs (including initializers) metadata as a list of :class:`onnxruntime.NodeArg`.'''
        return self._overridable_initializers

    
    def get_modelmeta(self = None):
        '''Return the metadata. See :class:`onnxruntime.ModelMetadata`.'''
        return self._model_meta

    
    def get_input_memory_infos(self = None):
        '''Return the memory info for the inputs.'''
        return self._input_meminfos

    
    def get_output_memory_infos(self = None):
        '''Return the memory info for the outputs.'''
        return self._output_meminfos

    
    def get_input_epdevices(self = None):
        '''Return the execution providers for the inputs.'''
        return self._input_epdevices

    
    def get_providers(self = None):
        '''Return list of registered execution providers.'''
        return self._providers

    
    def get_provider_options(self):
        """Return registered execution providers' configurations."""
        return self._provider_options

    
    def get_provider_graph_assignment_info(self = None):
        '''
        Get information about the subgraphs assigned to each execution provider and the nodes within.

        Application must enable the recording of graph assignment information by setting the session configuration
        for the key "session.record_ep_graph_assignment_info" to "1".
        '''
        return self._sess.get_provider_graph_assignment_info()

    
    def set_providers(self = None, providers = None, provider_options = None):
        """
        Register the input list of execution providers. The underlying session is re-created.

        :param providers: Optional sequence of providers in order of decreasing
            precedence. Values can either be provider names or tuples of
            (provider name, options dict). If not provided, then all available
            providers are used with the default precedence.
        :param provider_options: Optional sequence of options dicts corresponding
            to the providers listed in 'providers'.

        'providers' can contain either names or names and options. When any options
        are given in 'providers', 'provider_options' should not be used.

        The list of providers is ordered by precedence. For example
        `['CUDAExecutionProvider', 'CPUExecutionProvider']`
        means execute a node using CUDAExecutionProvider if capable,
        otherwise execute using CPUExecutionProvider.
        """
        self._reset_session(providers, provider_options)

    
    def disable_fallback(self = None):
        '''
        Disable session.run() fallback mechanism.
        '''
        self._enable_fallback = False

    
    def enable_fallback(self = None):
        '''
        Enable session.Run() fallback mechanism. If session.Run() fails due to an internal Execution Provider failure,
        reset the Execution Providers enabled for this session.
        If GPU is enabled, fall back to CUDAExecutionProvider.
        otherwise fall back to CPUExecutionProvider.
        '''
        self._enable_fallback = True

    
    def _validate_input(self, feed_input_names):
        missing_input_names = []
        for input in self._inputs_meta:
            if not input.name not in feed_input_names and input.type.startswith('optional'):
                missing_input_names.append(input.name)
            if missing_input_names:
                raise ValueError(f'''Required inputs ({missing_input_names}) are missing from input feed ({feed_input_names}).''')
            return None

    
    def run(self = None, output_names = None, input_feed = None, run_options = (None,)):
        '''
        Compute the predictions.

        :param output_names: name of the outputs
        :param input_feed: dictionary ``{ input_name: input_value }``
        :param run_options: See :class:`onnxruntime.RunOptions`.
        :return: list of results, every result is either a numpy array,
            a sparse tensor, a list or a dictionary.

        ::

            sess.run([output_name], {input_name: x})
        '''
        self._validate_input(list(input_feed.keys()))
        if not output_names:
            output_names = self._outputs_meta()
        
        try:
            return self._sess.run(output_names, input_feed, run_options)
        except C.EPFail:
            err = None
            if self._enable_fallback:
                print(f'''EP Error: {err!s} using {self._providers}''')
                print(f'''Falling back to {self._fallback_providers} and retrying.''')
                self.set_providers(self._fallback_providers)
                self.disable_fallback()
                del err
                return None
            None = None
            del err


    
    def run_async(self, output_names, input_feed, callback, user_data, run_options = (None,)):
        '''
        Compute the predictions asynchronously in a separate cxx thread from ort intra-op threadpool.

        :param output_names: name of the outputs
        :param input_feed: dictionary ``{ input_name: input_value }``
        :param callback: python function that accept array of results, and a status string on error.
            The callback will be invoked by a cxx thread from ort intra-op threadpool.
        :param run_options: See :class:`onnxruntime.RunOptions`.

        ::
            class MyData:
                def __init__(self):
                    # ...
                def save_results(self, results):
                    # ...

            def callback(results: np.ndarray, user_data: MyData, err: str) -> None:
              if err:
                 print (err)
              else:
                # save results to user_data

            sess.run_async([output_name], {input_name: x}, callback)
        '''
        self._validate_input(list(input_feed.keys()))
        if not output_names:
            output_names = self._outputs_meta()
        return self._sess.run_async(output_names, input_feed, callback, user_data, run_options)

    
    def run_with_ort_values(self = None, output_names = None, input_dict_ort_values = None, run_options = (None,)):
        '''
        Compute the predictions.

        :param output_names: name of the outputs
        :param input_dict_ort_values: dictionary ``{ input_name: input_ort_value }``
            See ``OrtValue`` class how to create `OrtValue`
            from numpy array or `SparseTensor`
        :param run_options: See :class:`onnxruntime.RunOptions`.
        :return: an array of `OrtValue`

        ::

            sess.run([output_name], {input_name: x})
        '''
        
        def invoke(sess, output_names, input_dict_ort_values, run_options):
            input_dict = { }
            for n, v in input_dict_ort_values.items():
                input_dict[n] = v._get_c_value()
                result = sess.run_with_ort_values(input_dict, output_names, run_options)
                if not isinstance(result, C.OrtValueVector):
                    raise TypeError("run_with_ort_values() must return a instance of type 'OrtValueVector'.")
                ort_values = result()
                return ort_values

        self._validate_input(list(input_dict_ort_values.keys()))
        if not output_names:
            output_names = self._outputs_meta()
        
        try:
            return invoke(self._sess, output_names, input_dict_ort_values, run_options)
        except C.EPFail:
            err = None
            if self._enable_fallback:
                print(f'''EP Error: {err!s} using {self._providers}''')
                print(f'''Falling back to {self._fallback_providers} and retrying.''')
                self.set_providers(self._fallback_providers)
                self.disable_fallback()
                del err
                return None
            None = None
            del err


    
    def end_profiling(self):
        '''
        End profiling and return results in a file.

        The results are stored in a filename if the option
        :meth:`onnxruntime.SessionOptions.enable_profiling`.
        '''
        return self._sess.end_profiling()

    
    def get_profiling_start_time_ns(self):
        """
        Return the nanoseconds of profiling's start time
        Comparable to time.monotonic_ns() after Python 3.3
        On some platforms, this timer may not be as precise as nanoseconds
        For instance, on Windows and MacOS, the precision will be ~100ns
        """
        return self._sess.get_profiling_start_time_ns

    
    def io_binding(self = None):
        '''Return an onnxruntime.IOBinding object`.'''
        return IOBinding(self)

    
    def run_with_iobinding(self, iobinding, run_options = (None,)):
        '''
        Compute the predictions.

        :param iobinding: the iobinding object that has graph inputs/outputs bind.
        :param run_options: See :class:`onnxruntime.RunOptions`.
        '''
        self._sess.run_with_iobinding(iobinding._iobinding, run_options)

    
    def set_ep_dynamic_options(self = None, options = None):
        '''
        Set dynamic options for execution providers.

        :param options: Dictionary of key-value pairs where both keys and values are strings.
                        These options will be passed to the execution providers to modify
                        their runtime behavior.
        '''
        self._sess.set_ep_dynamic_options(options)

    
    def get_tuning_results(self):
        return self._sess.get_tuning_results()

    
    def set_tuning_results(self = None, results = {
        'error_on_invalid': False }, *, error_on_invalid):
        return self._sess.set_tuning_results(results, error_on_invalid)

    
    def run_with_ortvaluevector(self, run_options, feed_names, feeds, fetch_names, fetches, fetch_devices):
        '''
        Compute the predictions similar to other run_*() methods but with minimal C++/Python conversion overhead.

        :param run_options: See :class:`onnxruntime.RunOptions`.
        :param feed_names: list of input names.
        :param feeds: list of input OrtValue.
        :param fetch_names: list of output names.
        :param fetches: list of output OrtValue.
        :param fetch_devices: list of output devices.
        '''
        self._sess.run_with_ortvaluevector(run_options, feed_names, feeds, fetch_names, fetches, fetch_devices)



class InferenceSession(Session):
    pass
# WARNING: Decompyle incomplete


def make_get_initializer_location_func_wrapper(get_initializer_location_func = None):
    '''
    Wraps a user\'s "get initializer location" function. The returned wrapper function adheres to the
    signature expected by ORT.

    Need this wrapper to:
      - Convert the `initializer_value` parameter from `C.OrtValue` to `onnxruntime.OrtValue`, which is more
        convenient for the user\'s function to use.
      - Allow the user\'s function to return the original `external_info` parameter (this wrapper makes a copy)
    '''
    pass
# WARNING: Decompyle incomplete


class ModelCompiler:
    '''
    This class is used to compile an ONNX model. A compiled ONNX model has EPContext nodes that each
    encapsulates a subgraph compiled/optimized for a specific execution provider.

    Refer to the EPContext design document for more information about EPContext models:
    https://onnxruntime.ai/docs/execution-providers/EP-Context-Design.html

        ::

            sess_options = onnxruntime.SessionOptions()
            sess_options.add_provider("SomeExecutionProvider", {"option1": "value1"})
            # Alternatively, allow ONNX Runtime to select the provider automatically given a policy:
            # sess_options.set_provider_selection_policy(onnxrt.OrtExecutionProviderDevicePolicy.PREFER_NPU)

            model_compiler = onnxruntime.ModelCompiler(sess_options, "input_model.onnx")
            model_compiler.compile_to_file("output_model.onnx")
    '''
    
    def __init__(self, sess_options, input_model_path_or_bytes, embed_compiled_data_into_model, external_initializers_file_path = None, external_initializers_size_threshold = None, flags = None, graph_optimization_level = (False, None, 1024, C.OrtCompileApiFlags.NONE, C.GraphOptimizationLevel.ORT_DISABLE_ALL, None), get_initializer_location_func = ('sess_options', 'onnxruntime.SessionOptions', 'input_model_path_or_bytes', 'str | os.PathLike | bytes', 'embed_compiled_data_into_model', 'bool', 'external_initializers_file_path', 'str | os.PathLike | None', 'external_initializers_size_threshold', 'int', 'flags', 'int', 'graph_optimization_level', 'C.GraphOptimizationLevel', 'get_initializer_location_func', 'GetInitializerLocationFunc | None')):
        '''
        Creates a ModelCompiler instance.

        :param sess_options: Session options containing the providers for which the model will be compiled.
            Refer to SessionOptions.add_provider() and SessionOptions.set_provider_selection_policy().
        :param input_model_path_or_bytes: The path to the input model file or bytes representing a serialized
            ONNX model.
        :param embed_compiled_data_into_model: Defaults to False. Set to True to embed compiled binary data into
            EPContext nodes in the compiled model.
        :param external_initializers_file_path: Defaults to None. Set to a path for a file that will store the
            initializers for non-compiled nodes.
        :param external_initializers_size_threshold: Defaults to 1024. Ignored if `external_initializers_file_path`
            is None or empty. Initializers larger than this threshold are stored in the external initializers file.
        :param flags: Additional boolean options to enable. Set this parameter to a bitwise OR of
            flags in onnxruntime.OrtCompileApiFlags.
        :param graph_optimization_level: The graph optimization level.
            Defaults to onnxruntime.GraphOptimizationLevel.ORT_DISABLE_ALL.
        :param get_initializer_location_func: Optional function called for every initializer to allow user to specify
            whether an initializer should be stored within the model or externally. Example:
            ```
                def get_initializer_location(
                    initializer_name: str,
                    initializer_value: onnxrt.OrtValue,
                    external_info: onnxrt.OrtExternalInitializerInfo | None,
                ) -> onnxrt.OrtExternalInitializerInfo | None:
                    byte_size = initializer_value.tensor_size_in_bytes()

                    if byte_size < 64:
                        return None  # Store small initializer within compiled model.

                    # Else, write initializer to new external file.
                    value_np = initializer_value.numpy()
                    file_offset = ext_init_file.tell()
                    ext_init_file.write(value_np.tobytes())
                    return onnxrt.OrtExternalInitializerInfo(initializer_file_path, file_offset, byte_size)
            ```
        '''
        input_model_path = None
        input_model_bytes = None
        if isinstance(input_model_path_or_bytes, (str, os.PathLike)):
            if not input_model_path_or_bytes:
                raise ValueError('Input model path is empty')
            input_model_path = os.fspath(input_model_path_or_bytes)
        elif isinstance(input_model_path_or_bytes, bytes):
            if len(input_model_path_or_bytes) == 0:
                raise ValueError('Input model bytes array is empty')
            input_model_bytes = input_model_path_or_bytes
        else:
            raise TypeError(f'''Unable to load from type \'{type(input_model_path_or_bytes)}\'''')
        if external_initializers_file_path:
            if not isinstance(external_initializers_file_path, (str, os.PathLike)):
                arg_type = type(external_initializers_file_path)
                raise TypeError(f'''Output external initializer filepath is of unexpected type \'{arg_type}\'''')
            external_initializers_file_path = os.fspath(external_initializers_file_path)
        else:
            external_initializers_file_path = ''
    # WARNING: Decompyle incomplete

    
    def compile_to_file(self = None, output_model_path = None):
        """
        Compiles to an output file. If an output file path is not provided,
        the output file path is generated based on the input model path by replacing
        '.onnx' with '_ctx.onnx'. Ex: The generated output file is 'model_ctx.onnx' for
        an input model with path 'model.onnx'.

        Raises an 'InvalidArgument' exception if the compilation options are invalid.

        :param output_model_path: Defaults to None. The path for the output/compiled model.
        """
        if output_model_path:
            if not isinstance(output_model_path, (str, os.PathLike)):
                raise TypeError(f'''Output model\'s filepath is of unexpected type \'{type(output_model_path)}\'''')
            output_model_path = os.fspath(output_model_path)
        self._model_compiler.compile_to_file(output_model_path)

    
    def compile_to_bytes(self = None):
        """
        Compiles to bytes representing the serialized compiled ONNX model.

        Raises an 'InvalidArgument' exception if the compilation options are invalid.

        :return: A bytes object representing the compiled ONNX model.
        """
        return self._model_compiler.compile_to_bytes()

    
    def compile_to_stream(self = None, write_function = None):
        """
        Compiles the input model and writes the serialized ONNX bytes to a stream using the provided write function.
        Raises an 'InvalidArgument' exception if the compilation options are invalid.
        :param write_function: A callable that accepts a bytes buffer to write.
        """
        self._model_compiler.compile_to_stream(write_function)



class IOBinding:
    '''
    This class provides API to bind input/output to a specified device, e.g. GPU.
    '''
    
    def __init__(self = None, session = None):
        self._iobinding = C.SessionIOBinding(session._sess)
        self._numpy_obj_references = { }

    
    def bind_cpu_input(self, name, arr_on_cpu):
        '''
        bind an input to array on CPU
        :param name: input name
        :param arr_on_cpu: input values as a python array on CPU
        '''
        self._numpy_obj_references[name] = arr_on_cpu
        self._iobinding.bind_input(name, arr_on_cpu)

    
    def bind_input(self, name, device_type, device_id, element_type, shape, buffer_ptr):
        '''
        :param name: input name
        :param device_type: e.g. cpu, cuda, cann
        :param device_id: device id, e.g. 0
        :param element_type: input element type. It can be either numpy type (like numpy.float32) or an integer for onnx type (like onnx.TensorProto.BFLOAT16)
        :param shape: input shape
        :param buffer_ptr: memory pointer to input data
        '''
        self._iobinding.bind_input(name, C.OrtDevice(get_ort_device_type(device_type), C.OrtDevice.default_memory(), device_id), element_type, shape, buffer_ptr)

    
    def bind_ortvalue_input(self, name, ortvalue):
        '''
        :param name: input name
        :param ortvalue: OrtValue instance to bind
        '''
        self._iobinding.bind_ortvalue_input(name, ortvalue._ortvalue)

    
    def synchronize_inputs(self):
        self._iobinding.synchronize_inputs()

    
    def bind_output(self, name, device_type, device_id, element_type, shape, buffer_ptr = ('cpu', 0, None, None, None)):
        '''
        :param name: output name
        :param device_type: e.g. cpu, cuda, cann, cpu by default
        :param device_id: device id, e.g. 0
        :param element_type: output element type. It can be either numpy type (like numpy.float32) or an integer for onnx type (like onnx.TensorProto.BFLOAT16)
        :param shape: output shape
        :param buffer_ptr: memory pointer to output data
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def bind_ortvalue_output(self, name, ortvalue):
        '''
        :param name: output name
        :param ortvalue: OrtValue instance to bind
        '''
        self._iobinding.bind_ortvalue_output(name, ortvalue._ortvalue)

    
    def synchronize_outputs(self):
        self._iobinding.synchronize_outputs()

    
    def get_outputs(self):
        '''
        Returns the output OrtValues from the Run() that preceded the call.
        The data buffer of the obtained OrtValues may not reside on CPU memory
        '''
        outputs = self._iobinding.get_outputs()
        if not isinstance(outputs, C.OrtValueVector):
            raise TypeError("get_outputs() must return an instance of type 'OrtValueVector'.")
        return outputs()

    
    def get_outputs_as_ortvaluevector(self):
        return self._iobinding.get_outputs()

    
    def copy_outputs_to_cpu(self):
        '''Copy output contents to CPU.'''
        return self._iobinding.copy_outputs_to_cpu()

    
    def clear_binding_inputs(self):
        self._iobinding.clear_binding_inputs()

    
    def clear_binding_outputs(self):
        self._iobinding.clear_binding_outputs()



class OrtValue:
    '''
    A data structure that supports all ONNX data formats (tensors and non-tensors) that allows users
    to place the data backing these on a device, for example, on a CUDA supported device.
    This class provides APIs to construct and deal with OrtValues.
    '''
    
    def __init__(self = None, ortvalue = None, numpy_obj = None):
        if isinstance(ortvalue, C.OrtValue):
            self._ortvalue = ortvalue
            self._numpy_obj = numpy_obj
            return None
        raise None('`Provided ortvalue` needs to be of type `onnxruntime.capi.onnxruntime_pybind11_state.OrtValue`')

    
    def _get_c_value(self = None):
        return self._ortvalue

    ortvalue_from_numpy = (lambda cls = None, numpy_obj = None, device_type = classmethod, device_id = ('cpu', 0, -1), vendor_id = ('numpy_obj', 'np.ndarray', 'return', 'OrtValue'): cls(C.OrtValue.ortvalue_from_numpy(numpy_obj, OrtDevice.make(device_type, device_id, vendor_id)._get_c_device()), numpy_obj if device_type.lower() == 'cpu' else None))()
    ortvalue_from_numpy_with_onnx_type = (lambda cls = None, data = None, onnx_element_type = classmethod: cls(C.OrtValue.ortvalue_from_numpy_with_onnx_type(data, onnx_element_type), data))()
    ortvalue_from_shape_and_type = (lambda cls, shape = None, element_type = None, device_type = classmethod, device_id = ('cpu', 0, -1), vendor_id = ('shape', 'Sequence[int]', 'device_type', 'str', 'device_id', 'int', 'vendor_id', 'int', 'return', 'OrtValue'): device = OrtDevice.make(device_type, device_id, vendor_id)._get_c_device()if isinstance(element_type, int):
cls(C.OrtValue.ortvalue_from_shape_and_onnx_type(shape, element_type, device))cls(C.OrtValue.ortvalue_from_shape_and_type(shape, element_type, device)))()
    ort_value_from_sparse_tensor = (lambda cls = None, sparse_tensor = None: cls(C.OrtValue.ort_value_from_sparse_tensor(sparse_tensor._get_c_tensor())))()
    
    def as_sparse_tensor(self = None):
        '''
        The function will return SparseTensor contained in this OrtValue
        '''
        return SparseTensor(self._ortvalue.as_sparse_tensor())

    
    def data_ptr(self = None):
        """
        Returns the address of the first element in the OrtValue's data buffer
        """
        return self._ortvalue.data_ptr()

    
    def device_name(self = None):
        """
        Returns the name of the device where the OrtValue's data buffer resides e.g. cpu, cuda, cann
        """
        return self._ortvalue.device_name().lower()

    
    def shape(self = None):
        '''
        Returns the shape of the data in the OrtValue
        '''
        return self._ortvalue.shape()

    
    def data_type(self = None):
        """
        Returns the data type of the data in the OrtValue. E.g. 'tensor(int64)'
        """
        return self._ortvalue.data_type()

    
    def element_type(self = None):
        '''
        Returns the proto type of the data in the OrtValue
        if the OrtValue is a tensor.
        '''
        return self._ortvalue.element_type()

    
    def tensor_size_in_bytes(self = None):
        '''
        Returns the size of the data in the OrtValue in bytes
        if the OrtValue is a tensor.
        '''
        return self._ortvalue.tensor_size_in_bytes()

    
    def has_value(self = None):
        '''
        Returns True if the OrtValue corresponding to an
        optional type contains data, else returns False
        '''
        return self._ortvalue.has_value()

    
    def is_tensor(self = None):
        '''
        Returns True if the OrtValue contains a Tensor, else returns False
        '''
        return self._ortvalue.is_tensor()

    
    def is_sparse_tensor(self = None):
        '''
        Returns True if the OrtValue contains a SparseTensor, else returns False
        '''
        return self._ortvalue.is_sparse_tensor()

    
    def is_tensor_sequence(self = None):
        '''
        Returns True if the OrtValue contains a Tensor Sequence, else returns False
        '''
        return self._ortvalue.is_tensor_sequence()

    
    def numpy(self = None):
        '''
        Returns a Numpy object from the OrtValue.
        Valid only for OrtValues holding Tensors. Throws for OrtValues holding non-Tensors.
        Use accessors to gain a reference to non-Tensor objects such as SparseTensor
        '''
        return self._ortvalue.numpy()

    
    def update_inplace(self = None, np_arr = None):
        '''
        Update the OrtValue in place with a new Numpy array. The numpy contents
        are copied over to the device memory backing the OrtValue. It can be used
        to update the input valuess for an InferenceSession with CUDA graph
        enabled or other scenarios where the OrtValue needs to be updated while
        the memory address can not be changed.
        '''
        self._ortvalue.update_inplace(np_arr)



def copy_tensors(src = None, dst = None, stream = None):
    '''
    Copy tensor data from source OrtValue sequence to destination OrtValue sequence.
    '''
    c_sources = src()
    c_dsts = dst()
    C.copy_tensors(c_sources, c_dsts, stream)


class OrtDevice:
    '''
    A data structure that exposes the underlying C++ OrtDevice
    '''
    
    def __init__(self, c_ort_device):
        '''
        Internal constructor
        '''
        if isinstance(c_ort_device, C.OrtDevice):
            self._ort_device = c_ort_device
            return None
        raise None('`Provided object` needs to be of type `onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice`')

    
    def _get_c_device(self):
        '''
        Internal accessor to underlying object
        '''
        return self._ort_device

    make = (lambda ort_device_name, device_id, vendor_id = (-1,): if vendor_id < 0:
OrtDevice(C.OrtDevice(get_ort_device_type(ort_device_name), C.OrtDevice.default_memory(), device_id))None(C.OrtDevice(get_ort_device_type(ort_device_name), C.OrtDevice.default_memory(), vendor_id, device_id)))()
    
    def device_id(self):
        return self._ort_device.device_id()

    
    def device_type(self):
        return self._ort_device.device_type()

    
    def device_vendor_id(self):
        return self._ort_device.vendor_id()

    
    def device_mem_type(self):
        return self._ort_device.mem_type()



class SparseTensor:
    '''
    A data structure that project the C++ SparseTensor object
    The class provides API to work with the object.
    Depending on the format, the class will hold more than one buffer
    depending on the format
    '''
    
    def __init__(self = None, sparse_tensor = None):
        '''
        Internal constructor
        '''
        if isinstance(sparse_tensor, C.SparseTensor):
            self._tensor = sparse_tensor
            return None
        raise None('`Provided object` needs to be of type `onnxruntime.capi.onnxruntime_pybind11_state.SparseTensor`')

    
    def _get_c_tensor(self = None):
        return self._tensor

    sparse_coo_from_numpy = (lambda cls, dense_shape = None, values = None, coo_indices = classmethod, ort_device = ('dense_shape', 'npt.NDArray[np.int64]', 'values', 'np.ndarray', 'coo_indices', 'npt.NDArray[np.int64]', 'ort_device', 'OrtDevice', 'return', 'SparseTensor'): cls(C.SparseTensor.sparse_coo_from_numpy(dense_shape, values, coo_indices, ort_device._get_c_device())))()
    sparse_csr_from_numpy = (lambda cls, dense_shape, values = None, inner_indices = None, outer_indices = classmethod, ort_device = ('dense_shape', 'npt.NDArray[np.int64]', 'values', 'np.ndarray', 'inner_indices', 'npt.NDArray[np.int64]', 'outer_indices', 'npt.NDArray[np.int64]', 'ort_device', 'OrtDevice', 'return', 'SparseTensor'): cls(C.SparseTensor.sparse_csr_from_numpy(dense_shape, values, inner_indices, outer_indices, ort_device._get_c_device())))()
    
    def values(self = None):
        '''
        The method returns a numpy array that is backed by the native memory
        if the data type is numeric. Otherwise, the returned numpy array that contains
        copies of the strings.
        '''
        return self._tensor.values()

    
    def as_coo_view(self):
        '''
        The method will return coo representation of the sparse tensor which will enable
        querying COO indices. If the instance did not contain COO format, it would throw.
        You can query coo indices as:

        ::

            coo_indices = sparse_tensor.as_coo_view().indices()

        which will return a numpy array that is backed by the native memory.
        '''
        return self._tensor.get_coo_data()

    
    def as_csrc_view(self):
        '''
        The method will return CSR(C) representation of the sparse tensor which will enable
        querying CRS(C) indices. If the instance dit not contain CSR(C) format, it would throw.
        You can query indices as:

        ::

            inner_ndices = sparse_tensor.as_csrc_view().inner()
            outer_ndices = sparse_tensor.as_csrc_view().outer()

        returning numpy arrays backed by the native memory.
        '''
        return self._tensor.get_csrc_data()

    
    def as_blocksparse_view(self):
        '''
        The method will return coo representation of the sparse tensor which will enable
        querying BlockSparse indices. If the instance did not contain BlockSparse format, it would throw.
        You can query coo indices as:

        ::

            block_sparse_indices = sparse_tensor.as_blocksparse_view().indices()

        which will return a numpy array that is backed by the native memory
        '''
        return self._tensor.get_blocksparse_data()

    
    def to_cuda(self, ort_device):
        """
        Returns a copy of this instance on the specified cuda device

        :param ort_device: with name 'cuda' and valid gpu device id

        The method will throw if:

        - this instance contains strings
        - this instance is already on GPU. Cross GPU copy is not supported
        - CUDA is not present in this build
        - if the specified device is not valid
        """
        return SparseTensor(self._tensor.to_cuda(ort_device._get_c_device()))

    
    def format(self):
        '''
        Returns a OrtSparseFormat enumeration
        '''
        return self._tensor.format

    
    def dense_shape(self = None):
        '''
        Returns a numpy array(int64) containing a dense shape of a sparse tensor
        '''
        return self._tensor.dense_shape()

    
    def data_type(self = None):
        '''
        Returns a string data type of the data in the OrtValue
        '''
        return self._tensor.data_type()

    
    def device_name(self = None):
        '''
        Returns the name of the device where the SparseTensor data buffers reside e.g. cpu, cuda
        '''
        return self._tensor.device_name().lower()


GetInitializerLocationFunc = Callable[([
    str,
    OrtValue,
    C.OrtExternalInitializerInfo | None], C.OrtExternalInitializerInfo | None)]
GetInitializerLocationWrapperFunc = Callable[([
    str,
    C.OrtValue,
    C.OrtExternalInitializerInfo | None], C.OrtExternalInitializerInfo | None)]
