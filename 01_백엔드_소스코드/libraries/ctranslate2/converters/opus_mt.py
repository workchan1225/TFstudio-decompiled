# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: opus_mt.pyc (Python 3.11)

import argparse
import os
import yaml
from ctranslate2.converters.marian import MarianConverter

class OpusMTConverter(MarianConverter):
    pass
# WARNING: Decompyle incomplete


def main():
    parser = argparse.ArgumentParser(formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--model_dir', required = True, help = 'Path to the OPUS-MT model directory.')
    OpusMTConverter.declare_arguments(parser)
    args = parser.parse_args()
    converter = OpusMTConverter(args.model_dir)
    converter.convert_from_args(args)

if __name__ == '__main__':
    main()
    return None
