# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_stop_reason.pyc (Python 3.11)

from typing_extensions import Literal, TypeAlias
__all__ = [
    'BetaStopReason']
BetaStopReason: TypeAlias = Literal[('end_turn', 'max_tokens', 'stop_sequence', 'tool_use', 'pause_turn', 'refusal', 'model_context_window_exceeded')]
