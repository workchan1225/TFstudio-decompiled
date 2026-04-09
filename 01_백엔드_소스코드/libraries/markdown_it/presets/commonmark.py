# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: commonmark.pyc (Python 3.11)

'''Commonmark default options.

This differs to presets.default,
primarily in that it allows HTML and does not enable components:

- block: table
- inline: strikethrough
'''
from utils import PresetType

def make():
    return {
        'options': {
            'maxNesting': 20,
            'html': True,
            'linkify': False,
            'typographer': False,
            'quotes': '“”‘’',
            'xhtmlOut': True,
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
                    'blockquote',
                    'code',
                    'fence',
                    'heading',
                    'hr',
                    'html_block',
                    'lheading',
                    'list',
                    'reference',
                    'paragraph'] },
            'inline': {
                'rules': [
                    'autolink',
                    'backticks',
                    'emphasis',
                    'entity',
                    'escape',
                    'html_inline',
                    'image',
                    'link',
                    'newline',
                    'text'],
                'rules2': [
                    'balance_pairs',
                    'emphasis',
                    'fragments_join'] } } }
