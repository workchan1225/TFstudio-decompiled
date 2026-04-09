# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: data_classes.pyc (Python 3.11)

'''Data models for edge-tts.'''
import argparse
import re
from dataclasses import dataclass
from typing_extensions import Literal
TTSConfig = <NODE:12>()

class UtilArgs(argparse.Namespace):
    proxy: str = 'CLI arguments.'
