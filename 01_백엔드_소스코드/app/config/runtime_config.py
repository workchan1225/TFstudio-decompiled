# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: runtime_config.pyc (Python 3.11)

'''
Runtime configuration for TFstudio
Manages settings that need to persist outside the database (e.g., data path)
because the database location itself depends on these settings.

Config file location:
- Windows: %LOCALAPPDATA%/TFstudio/runtime_config.json
- Linux/Mac: ~/.tfstudio/runtime_config.json
'''
import json
import os
import logging
from pathlib import Path
from datetime import datetime
from typing import TypedDict
logger = logging.getLogger(__name__)

def MigrationStatus():
    '''MigrationStatus'''
    bytes_copied: int = 'Migration status structure'

MigrationStatus = <NODE:27>(MigrationStatus, 'MigrationStatus', TypedDict, total = False)

def RuntimeConfig():
    '''RuntimeConfig'''
    path_history: list[str] = 'Runtime configuration structure'

RuntimeConfig = <NODE:27>(RuntimeConfig, 'RuntimeConfig', TypedDict, total = False)

def get_runtime_config_dir():
    '''
    Get runtime config directory path

    Returns:
        Path: Config directory
    '''
    if os.name == 'nt':
        localappdata = os.getenv('LOCALAPPDATA', os.path.expanduser('~'))
        config_dir = Path(localappdata) / 'TFstudio'
    else:
        config_dir = Path.home() / '.tfstudio'
    config_dir.mkdir(parents = True, exist_ok = True)
    return config_dir


def get_runtime_config_path():
    '''
    Get runtime config file path

    Returns:
        Path: Config file path
    '''
    return get_runtime_config_dir() / 'runtime_config.json'


def load_runtime_config():
    """
    Load runtime configuration from file

    Returns:
        RuntimeConfig: Configuration dict (empty if file doesn't exist)
    """
    config_path = get_runtime_config_path()
    if not config_path.exists():
        return { }
    
    try:
        f = open(config_path, 'r', encoding = 'utf-8')
        config = json.load(f)
        logger.debug(f'''Loaded runtime config: {config}''')
        
        try:
            None(None, None)
            return 
            with None:
                if not None, config:
                    
                    try:
                        
                        try:
                            return None
                        except (json.JSONDecodeError, IOError):
                            logger.error(f'''Failed to load runtime config: {e}''')
                            del e
                            return None
                            None = 
                            del e






def save_runtime_config(config = None):
    '''
    Save runtime configuration to file

    Args:
        config: Configuration dict to save

    Returns:
        bool: True if successful
    '''
    config_path = get_runtime_config_path()
    
    try:
        f = open(config_path, 'w', encoding = 'utf-8')
        json.dump(config, f, indent = 2, ensure_ascii = False)
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        logger.info(f'''Saved runtime config to {config_path}''')
                        return True
                    except IOError:
                        e = None
                        logger.error(f'''Failed to save runtime config: {e}''')
                        e = None
                        del e
                        return False
                        e = None
                        del e






def get_configured_data_path():
    '''
    Get the configured data path from runtime config

    Returns:
        Path | None: Configured path or None if using default
    '''
    config = load_runtime_config()
    data_path = config.get('data_path')
    if data_path:
        path = Path(data_path)
        if path.exists() and path.is_dir():
            return path
        None.warning(f'''Configured data path does not exist: {data_path}''')


def set_data_path(path = None):
    '''
    Set the configured data path (applied immediately)

    Args:
        path: New data path to use

    Returns:
        bool: True if successful
    '''
    config = load_runtime_config()
    config['data_path'] = path
    if config.get('pending_data_path') == path:
        config.pop('pending_data_path', None)
    return save_runtime_config(config)


def set_pending_data_path(path = None):
    '''
    Set a pending data path that will be applied after restart

    Args:
        path: New data path to apply after restart

    Returns:
        bool: True if successful
    '''
    config = load_runtime_config()
    config['pending_data_path'] = path
    return save_runtime_config(config)


def get_pending_data_path():
    '''
    Get the pending data path waiting to be applied

    Returns:
        str | None: Pending path or None
    '''
    config = load_runtime_config()
    return config.get('pending_data_path')


def clear_pending_data_path():
    '''
    Clear the pending data path

    Returns:
        bool: True if successful
    '''
    config = load_runtime_config()
    if 'pending_data_path' in config:
        del config['pending_data_path']
        return save_runtime_config(config)


def apply_pending_data_path():
    '''
    Apply pending data path as the active path
    Called during startup to finalize path change

    Returns:
        bool: True if path was applied, False if no pending path
    '''
    config = load_runtime_config()
    pending = config.get('pending_data_path')
    if not pending:
        return False
    path = None(pending)
    if not path.exists():
        logger.error(f'''Pending data path does not exist: {pending}''')
        return False
    config['data_path'] = None
    del config['pending_data_path']
    migration = config.get('migration', { })
    if migration.get('status') == 'completed':
        del config['migration']
    if save_runtime_config(config):
        logger.info(f'''Applied pending data path: {pending}''')
        return True


def get_migration_status():
    '''
    Get current migration status

    Returns:
        MigrationStatus | None: Migration status or None
    '''
    config = load_runtime_config()
    return config.get('migration')


def set_migration_status(status = None):
    '''
    Set migration status

    Args:
        status: Migration status to set

    Returns:
        bool: True if successful
    '''
    config = load_runtime_config()
    config['migration'] = status
    return save_runtime_config(config)


def clear_migration_status():
    '''
    Clear migration status

    Returns:
        bool: True if successful
    '''
    config = load_runtime_config()
    if 'migration' in config:
        del config['migration']
        return save_runtime_config(config)


def clear_data_path():
    '''
    Clear configured data path (revert to default)

    Returns:
        bool: True if successful
    '''
    config = load_runtime_config()
    changed = False
    if 'data_path' in config:
        del config['data_path']
        changed = True
    if 'pending_data_path' in config:
        del config['pending_data_path']
        changed = True
    if changed:
        return save_runtime_config(config)


def add_to_path_history(path = None):
    '''
    Add a path to the history list

    Args:
        path: Path to add to history

    Returns:
        bool: True if successful
    '''
    config = load_runtime_config()
    history = config.get('path_history', [])
    normalized_path = path.replace('\\', '/')
    if normalized_path in history:
        history.remove(normalized_path)
    history.insert(0, normalized_path)
    history = history[:10]
    config['path_history'] = history
    return save_runtime_config(config)


def get_path_history():
    '''
    Get the list of previously used paths

    Returns:
        list[str]: List of paths (most recent first)
    '''
    config = load_runtime_config()
    return config.get('path_history', [])


def remove_from_path_history(path = None):
    '''
    Remove a path from history

    Args:
        path: Path to remove

    Returns:
        bool: True if successful
    '''
    config = load_runtime_config()
    history = config.get('path_history', [])
    normalized_path = path.replace('\\', '/')
    if normalized_path in history:
        history.remove(normalized_path)
        config['path_history'] = history
        return save_runtime_config(config)


def get_default_data_path():
    '''
    Get the default data path (without any configuration)

    Returns:
        Path: Default data path
    '''
    if os.name == 'nt':
        localappdata = os.getenv('LOCALAPPDATA', os.path.expanduser('~'))
        return Path(localappdata) / 'TFstudio' / 'data'
    return None.home() / '.tfstudio' / 'data'


def validate_data_path(path = None):
