# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: machine_info.pyc (Python 3.11)

import argparse
import importlib.metadata as importlib
import json
import logging
import platform
from os import environ
import cpuinfo
import psutil
from py3nvml.py3nvml import NVMLError, nvmlDeviceGetCount, nvmlDeviceGetHandleByIndex, nvmlDeviceGetMemoryInfo, nvmlDeviceGetName, nvmlInit, nvmlShutdown, nvmlSystemGetDriverVersion

class MachineInfo:
    '''Class encapsulating Machine Info logic.'''
    
    def __init__(self, silent, logger = (False, None)):
        self.silent = silent
    # WARNING: Decompyle incomplete

    
    def get_machine_info(self):
        '''Get machine info in metric format'''
        gpu_info = self.get_gpu_info_by_nvml()
        cpu_info = cpuinfo.get_cpu_info()
        machine_info = {
            'gpu': gpu_info,
            'cpu': self.get_cpu_info(),
            'memory': self.get_memory_info(),
            'os': platform.platform(),
            'python': self._try_get(cpu_info, [
                'python_version']),
            'packages': self.get_related_packages(),
            'onnxruntime': self.get_onnxruntime_info(),
            'pytorch': self.get_pytorch_info(),
            'tensorflow': self.get_tensorflow_info() }
        return machine_info

    
    def get_memory_info(self = None):
        '''Get memory info'''
        mem = psutil.virtual_memory()
        return {
            'total': mem.total,
            'available': mem.available }

    
    def _try_get(self = None, cpu_info = None, names = None):
        for name in names:
            if name in cpu_info:
                value = cpu_info[name]
                if isinstance(value, (list, tuple)):
                    
                    return ','.join, (lambda .0: [ str(i) for i in .0 ])(value())
                
                return None, None
            return ''

    
    def get_cpu_info(self = None):
        '''Get CPU info'''
        cpu_info = cpuinfo.get_cpu_info()
        return {
            'brand': self._try_get(cpu_info, [
                'brand',
                'brand_raw']),
            'cores': psutil.cpu_count(logical = False),
            'logical_cores': psutil.cpu_count(logical = True),
            'hz': self._try_get(cpu_info, [
                'hz_actual']),
            'l2_cache': self._try_get(cpu_info, [
                'l2_cache_size']),
            'flags': self._try_get(cpu_info, [
                'flags']),
            'processor': platform.uname().processor }

    
    def get_gpu_info_by_nvml(self = None):
        '''Get GPU info using nvml'''
        gpu_info_list = []
        driver_version = None
        
        try:
            nvmlInit()
            driver_version = nvmlSystemGetDriverVersion()
            deviceCount = nvmlDeviceGetCount()
            for i in range(deviceCount):
                handle = nvmlDeviceGetHandleByIndex(i)
                info = nvmlDeviceGetMemoryInfo(handle)
                gpu_info = { }
                gpu_info['memory_total'] = info.total
                gpu_info['memory_available'] = info.free
                gpu_info['name'] = nvmlDeviceGetName(handle)
                gpu_info_list.append(gpu_info)
                nvmlShutdown()
        except NVMLError:
            error = None
            if not self.silent:
                self.logger.error('Error fetching GPU information using nvml: %s', error)
            error = None
            del error
            return None
            error = None
            del error
            result = {
                'driver_version': driver_version,
                'devices': gpu_info_list }
            if 'CUDA_VISIBLE_DEVICES' in environ:
                result['cuda_visible'] = environ['CUDA_VISIBLE_DEVICES']
            return result


    
    def get_related_packages(self = None):
        related_packages = {
            'onnxruntime-gpu',
            'onnxconverter-common',
            'onnx',
            'numpy',
            'sympy',
            'torch',
            'protobuf',
            'tensorflow',
            'flatbuffers',
            'onnxruntime',
            'transformers'}
        related_packages_list = { }
        for dist in importlib.metadata.distributions():
            if dist.metadata['Name'].lower() in related_packages:
                related_packages_list[dist.metadata['Name'].lower()] = dist.version
            return related_packages_list

    
    def get_onnxruntime_info(self = None):
        
        try:
            import onnxruntime
            return {
                'version': onnxruntime.__version__,
                'support_gpu': 'CUDAExecutionProvider' in onnxruntime.get_available_providers() }
        except ImportError:
            error = None
            if not self.silent:
                self.logger.exception(error)
            error = None
            del error
            return None
            error = None
            del error
            except Exception:
                exception = None
                if not self.silent:
                    self.logger.exception(exception, False)
                exception = None
                del exception
                return None
                exception = None
                del exception


    
    def get_pytorch_info(self = None):
        
        try:
            import torch
            return {
                'version': torch.__version__,
                'support_gpu': torch.cuda.is_available(),
                'cuda': torch.version.cuda }
        except ImportError:
            error = None
            if not self.silent:
                self.logger.exception(error)
            error = None
            del error
            return None
            error = None
            del error
            except Exception:
                exception = None
                if not self.silent:
                    self.logger.exception(exception, False)
                exception = None
                del exception
                return None
                exception = None
                del exception


    
    def get_tensorflow_info(self = None):
        
        try:
            import tensorflow as tf
            return {
                'version': tf.version.VERSION,
                'git_version': tf.version.GIT_VERSION,
                'support_gpu': tf.test.is_built_with_cuda() }
        except ImportError:
            error = None
            if not self.silent:
                self.logger.exception(error)
            error = None
            del error
            return None
            error = None
            del error
            except ModuleNotFoundError:
                error = None
                if not self.silent:
                    self.logger.exception(error)
                error = None
                del error
                return None
                error = None
                del error




def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--silent', required = False, action = 'store_true', help = 'Do not print error message')
    parser.set_defaults(silent = False)
    args = parser.parse_args()
    return args


def get_machine_info(silent = None):
    machine = MachineInfo(silent)
    return json.dumps(machine.machine_info, indent = 2)


def get_device_info(silent = None):
    machine = MachineInfo(silent)
    info = machine.machine_info
    if info:
        info = info.items()()
    return json.dumps(info, indent = 2)

if __name__ == '__main__':
    args = parse_arguments()
    print(get_machine_info(args.silent))
    return None
