# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: whisper_spec.pyc (Python 3.11)

from typing import List, Optional, Tuple
import numpy as np
from ctranslate2.specs import common_spec, model_spec, transformer_spec

class WhisperConfig(model_spec.ModelConfig):
    pass
# WARNING: Decompyle incomplete


class WhisperSpec(model_spec.LanguageModelSpec):
    pass
# WARNING: Decompyle incomplete


class WhisperEncoderSpec(model_spec.LayerSpec):
    
    def __init__(self, num_layers, num_heads):
        self.num_heads = np.dtype('int16').type(num_heads)
        self.conv1 = common_spec.Conv1DSpec()
        self.conv2 = common_spec.Conv1DSpec()
        self.position_encodings = transformer_spec.PositionEncoderSpec()
        self.layer_norm = common_spec.LayerNormSpec()
        self.layer = range(num_layers)()
