# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: zero.pyc (Python 3.11)

'''
"Zero" preset, with nothing enabled. Useful for manual configuring of simple
modes. For example, to parse bold/italic only.
'''
from utils import PresetType

def make():
    return {
        'options': {
            'maxNesting': 20,
            'html': False,
            'linkify': False,
            'typographer': False,
            'quotes': '“”‘’',
            'xhtmlOut': False,
            'breaks': False,
            'langPrefix': 'language-',
            'highlight': None },
        'components': {
            'core': {
                'rules': [
                    'normalize',
                    'block',
                    'inline',
                    'text_join'] },
            'block': {
                'rules': [
                    'paragraph'] },
            'inline': {
                'rules': [
                    'text'],
                'rules2': [
                    'balance_pairs',
                    'fragments_join'] } } }
