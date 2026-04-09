# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: libsecret.pyc (Python 3.11)

import logging
from  import backend
from backend import KeyringBackend
from compat import properties
from credentials import SimpleCredential
from errors import KeyringLocked, PasswordDeleteError, PasswordSetError
available = False

try:
    import gi
    from gi.repository import Gio, GLib
    gi.require_version('Secret', '1')
    from gi.repository import Secret
    available = True
except (AttributeError, ImportError, ValueError):
    pass

log = logging.getLogger(__name__)

class Keyring(KeyringBackend, backend.SchemeSelectable):
    '''libsecret Keyring'''
    appid = 'Python keyring library'
    schema = (lambda self: Secret.Schema.new('org.freedesktop.Secret.Generic', Secret.SchemaFlags.NONE, self._query(Secret.SchemaAttributeType.STRING, Secret.SchemaAttributeType.STRING, application = Secret.SchemaAttributeType.STRING)))()
    collection = (lambda self: Secret.COLLECTION_DEFAULT)()
    priority = (lambda cls = property: if not available:
raise RuntimeError('libsecret required')try:
Secret.Service.get_sync(Secret.ServiceFlags.OPEN_SESSION, None)except GLib.Error:
error = Noneraise RuntimeError("Can't open a session to the secret service"), errorerror = Nonedel error4.8)()
    
    def get_password(self, service, username):
        '''Get password of the username for the service'''
        attributes = self._query(service, username, application = self.appid)
        
        try:
            items = Secret.password_search_sync(self.schema, attributes, Secret.SearchFlags.UNLOCK, None)
        except GLib.Error:
            error = None
            quark = GLib.quark_try_string('g-io-error-quark')
            if error.matches(quark, Gio.IOErrorEnum.FAILED):
                raise KeyringLocked('Failed to unlock the item!'), error
            raise 
            error = None
            del error

        for item in items:
            
            return None, item.retrieve_secret_sync().get_text()
            except GLib.Error:
                GLib.quark_try_string('secret-error') = None
                if error.matches(quark, Secret.Error.IS_LOCKED):
                    raise KeyringLocked('Failed to unlock the item!'), error
                raise 
                error = None
                del error
            return None

    
    def set_password(self, service, username, password):
        '''Set password for the username of the service'''
        attributes = self._query(service, username, application = self.appid)
        label = f'''Password for \'{username}\' on \'{service}\''''
        
        try:
            stored = Secret.password_store_sync(self.schema, attributes, self.collection, label, password, None)
        except GLib.Error:
            error = None
            quark = GLib.quark_try_string('secret-error')
            if error.matches(quark, Secret.Error.IS_LOCKED):
                raise KeyringLocked('Failed to unlock the collection!'), error
            quark = GLib.quark_try_string('g-io-error-quark')
            if error.matches(quark, Gio.IOErrorEnum.FAILED):
                raise KeyringLocked('Failed to unlock the collection!'), error
            raise 
            error = None
            del error

        if not stored:
            raise PasswordSetError('Failed to store password!')

    
    def delete_password(self, service, username):
        '''Delete the stored password (only the first one)'''
        attributes = self._query(service, username, application = self.appid)
        
        try:
            items = Secret.password_search_sync(self.schema, attributes, Secret.SearchFlags.UNLOCK, None)
        except GLib.Error:
            error = None
            quark = GLib.quark_try_string('g-io-error-quark')
            if error.matches(quark, Gio.IOErrorEnum.FAILED):
                raise KeyringLocked('Failed to unlock the item!'), error
            raise 
            error = None
            del error

        for item in items:
            removed = Secret.password_clear_sync(self.schema, item.get_attributes(), None)
        except GLib.Error:
            error = None
            quark = GLib.quark_try_string('secret-error')
            if error.matches(quark, Secret.Error.IS_LOCKED):
                raise KeyringLocked('Failed to unlock the item!'), error
            raise 
            error = None
            del error
        
        return None, removed
        raise PasswordDeleteError('No such password!')

    
    def get_credential(self, service, username):
        '''Get the first username and password for a service.
        Return a Credential instance

        The username can be omitted, but if there is one, it will use get_password
        and return a SimpleCredential containing  the username and password
        Otherwise, it will return the first username and password combo that it finds.
        '''
        query = self._query(service, username)
        
        try:
            items = Secret.password_search_sync(self.schema, query, Secret.SearchFlags.UNLOCK, None)
        except GLib.Error:
            error = None
            quark = GLib.quark_try_string('g-io-error-quark')
            if error.matches(quark, Gio.IOErrorEnum.FAILED):
                raise KeyringLocked('Failed to unlock the item!'), error
            raise 
            error = None
            del error

        for item in items:
            username = item.get_attributes().get('username')
            
            return None, SimpleCredential(username, item.retrieve_secret_sync().get_text())
            except GLib.Error:
                GLib.quark_try_string('secret-error') = None
                if error.matches(quark, Secret.Error.IS_LOCKED):
                    raise KeyringLocked('Failed to unlock the item!'), error
                raise 
                error = None
                del error
            return None
