# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

__all__ = ('commonmark', 'default', 'gfm_like', 'js_default', 'zero')
from utils import PresetType
from  import commonmark, default, zero
js_default = default

class gfm_like:
    '''GitHub Flavoured Markdown (GFM) like.

    This adds the linkify, table and strikethrough components to CommmonMark.

    Note, it lacks task-list items and raw HTML filtering,
    to meet the the full GFM specification
    (see https://github.github.com/gfm/#autolinks-extension-).
    '''
    make = (lambda : config = commonmark.make()config['components']['core']['rules'].append('linkify')config['components']['block']['rules'].append('table')config['components']['inline']['rules'].extend([
'strikethrough',
'linkify'])config['components']['inline']['rules2'].append('strikethrough')config['options']['linkify'] = Trueconfig['options']['html'] = Trueconfig)()
