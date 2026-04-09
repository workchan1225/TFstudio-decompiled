# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: webextension.pyc (Python 3.11)

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.bidi.common import command_builder

class WebExtension:
    '''BiDi implementation of the webExtension module.'''
    
    def __init__(self, conn):
        self.conn = conn

    
    def install(self = None, path = None, archive_path = None, base64_value = (None, None, None)):
        '''Installs a web extension in the remote end.

        You must provide exactly one of the parameters.

        Args:
            path: Path to an extension directory.
            archive_path: Path to an extension archive file.
            base64_value: Base64 encoded string of the extension archive.

        Returns:
            A dictionary containing the extension ID.
        '''
        if (lambda .0: pass# WARNING: Decompyle incomplete
)((path, archive_path, base64_value)()) != 1:
            raise ValueError('Exactly one of path, archive_path, or base64_value must be provided')
    # WARNING: Decompyle incomplete

    
    def uninstall(self = None, extension_id_or_result = None):
        '''Uninstalls a web extension from the remote end.

        Args:
            extension_id_or_result: Either the extension ID as a string or the result dictionary
              from a previous install() call containing the extension ID.
        '''
        if isinstance(extension_id_or_result, dict):
            extension_id = extension_id_or_result.get('extension')
        else:
            extension_id = extension_id_or_result
        params = {
            'extension': extension_id }
        self.conn.execute(command_builder('webExtension.uninstall', params))
