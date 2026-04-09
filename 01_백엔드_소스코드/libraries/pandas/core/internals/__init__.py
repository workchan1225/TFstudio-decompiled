# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from pandas.core.internals.api import make_block
from pandas.core.internals.concat import concatenate_managers
from pandas.core.internals.managers import BlockManager, SingleBlockManager
__all__ = [
    'Block',
    'BlockManager',
    'DatetimeTZBlock',
    'ExtensionBlock',
    'SingleBlockManager',
    'concatenate_managers',
    'make_block']

def __getattr__(name = None):
    import warnings
    Pandas4Warning = Pandas4Warning
    import pandas.errors
    if name == 'create_block_manager_from_blocks':
        warnings.warn(f'''{name} is deprecated and will be removed in a future version. Use public APIs instead.''', Pandas4Warning, stacklevel = 2)
        create_block_manager_from_blocks = create_block_manager_from_blocks
        import pandas.core.internals.managers
        return create_block_manager_from_blocks
    if None in ('Block', 'ExtensionBlock', 'DatetimeTZBlock'):
        warnings.warn(f'''{name} is deprecated and will be removed in a future version. Use public APIs instead.''', Pandas4Warning, stacklevel = 2)
        if name == 'DatetimeTZBlock':
            DatetimeTZBlock = _DatetimeTZBlock
            import pandas.core.internals.api
            return DatetimeTZBlock
        if None == 'ExtensionBlock':
            ExtensionBlock = ExtensionBlock
            import pandas.core.internals.blocks
            return ExtensionBlock
        Block = Block
        import pandas.core.internals.blocks
        return Block
    raise None(f'''module \'pandas.core.internals\' has no attribute \'{name}\'''')
