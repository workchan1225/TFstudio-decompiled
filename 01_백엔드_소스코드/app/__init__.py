# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path
import os
import sys
import io
import time

def _setup_stdio_encoding():
    '''stdout/stderr 인코딩을 UTF-8로 설정하거나 devnull로 리디렉션'''
    pass
# WARNING: Decompyle incomplete

_setup_stdio_encoding()
os.environ['ORT_LOG_LEVEL'] = '3'
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('MKL_NUM_THREADS', '1')
os.environ.setdefault('OMP_NUM_THREADS', '1')

try:
    import numpy as np
    print(f'''[App Init] NumPy {np.__version__} pre-initialized (CPU dispatcher tracer fix)''')
except ImportError:
    print('[App Init] NumPy not found')
except Exception:
    e = None
    print(f'''[App Init] NumPy init warning: {e}''')
    e = None
    del e
except:
    e = None
    del e

_preload_onnxruntime = os.environ.get('TFSTUDIO_PRELOAD_ONNXRUNTIME', '').strip() == '1'
if _preload_onnxruntime:
    
    try:
        import onnxruntime as ort
        print(f'''[App Init] ONNX Runtime {ort.__version__} pre-initialized''')
    except ImportError:
        print('[App Init] ONNX Runtime not found')
    except Exception:
        e = None
        print(f'''[App Init] ONNX Runtime init warning: {e}''')
        e = None
        del e
    except:
        e = None
        del e
        print('[App Init] ONNX Runtime pre-initialization skipped')

    db = SQLAlchemy()
    
    def _setup_external_packages():
        '''외부 패키지 경로 설정 (Qwen TTS용)

    EXE 환경에서 torch/transformers 등 대용량 패키지를
    %LOCALAPPDATA%/TFstudio/packages에서 로드합니다.
    '''
        IS_FROZEN = IS_FROZEN
        import app.config.paths
        if not IS_FROZEN:
            return None
        if not None.environ.get('LOCALAPPDATA'):
            pass
        local_app_data = os.path.join(os.path.expanduser('~'), 'AppData', 'Local')
        packages_path = os.path.join(local_app_data, 'TFstudio', 'packages')
        if not os.path.isdir(packages_path):
            return None
        search_paths = [
            None,
            os.path.join(packages_path, 'qwen_tts_packages')]
        for search_path in search_paths:
            torch_path = os.path.join(search_path, 'torch')
            if os.path.isdir(torch_path):
                sys.path.insert(0, search_path)
                print(f'''[App Init] External packages loaded from: {search_path}''')
                return None
            return None

    
    def create_app():
        pass
    # WARNING: Decompyle incomplete

    return None
