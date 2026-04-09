# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: register.pyc (Python 3.11)

"""distutils.command.register

Implements the Distutils 'register' command (register with the repository).
"""
import getpass
import io
import urllib.parse as urllib
import urllib.request as urllib
from warnings import warn
from distutils.core import PyPIRCCommand
from distutils import log

class register(PyPIRCCommand):
    description = 'register the distribution with the Python package index'
    user_options = PyPIRCCommand.user_options + [
        ('list-classifiers', None, 'list the valid Trove classifiers'),
        ('strict', None, 'Will stop the registering if the meta-data are not fully compliant')]
    boolean_options = PyPIRCCommand.boolean_options + [
        'verify',
        'list-classifiers',
        'strict']
    sub_commands = [
        ('check', (lambda self: True))]
    
    def initialize_options(self):
        PyPIRCCommand.initialize_options(self)
        self.list_classifiers = 0
        self.strict = 0

    
    def finalize_options(self):
        PyPIRCCommand.finalize_options(self)
        check_options = {
            'strict': ('register', self.strict),
            'restructuredtext': ('register', 1) }
        self.distribution.command_options['check'] = check_options

    
    def run(self):
        self.finalize_options()
        self._set_config()
        for cmd_name in self.get_sub_commands():
            self.run_command(cmd_name)
            if self.dry_run:
                self.verify_metadata()
                return None
            if None.list_classifiers:
                self.classifiers()
                return None
            None.send_metadata()
            return None

    
    def check_metadata(self):
        '''Deprecated API.'''
        warn('distutils.command.register.check_metadata is deprecated; use the check command instead', DeprecationWarning)
        check = self.distribution.get_command_obj('check')
        check.ensure_finalized()
        check.strict = self.strict
        check.restructuredtext = 1
        check.run()

    
    def _set_config(self):
        '''Reads the configuration file and set attributes.'''
        config = self._read_pypirc()
        if config != { }:
            self.username = config['username']
            self.password = config['password']
            self.repository = config['repository']
            self.realm = config['realm']
            self.has_config = True
            return None
        if None.repository not in ('pypi', self.DEFAULT_REPOSITORY):
            raise ValueError('%s not found in .pypirc' % self.repository)
        if self.repository == 'pypi':
            self.repository = self.DEFAULT_REPOSITORY
        self.has_config = False

    
    def classifiers(self):
        '''Fetch the list of classifiers from the server.'''
        url = self.repository + '?:action=list_classifiers'
        response = urllib.request.urlopen(url)
        log.info(self._read_pypi_response(response))

    
    def verify_metadata(self):
        '''Send the metadata to the package index server to be checked.'''
        (code, result) = self.post_to_server(self.build_post_data('verify'))
        log.info('Server response (%s): %s', code, result)

    
    def send_metadata(self):
        """Send the metadata to the package index server.

        Well, do the following:
        1. figure who the user is, and then
        2. send the data as a Basic auth'ed POST.

        First we try to read the username/password from $HOME/.pypirc,
        which is a ConfigParser-formatted file with a section
        [distutils] containing username and password entries (both
        in clear text). Eg:

            [distutils]
            index-servers =
                pypi

            [pypi]
            username: fred
            password: sekrit

        Otherwise, to figure who the user is, we offer the user three
        choices:

         1. use existing login,
         2. register as a new user, or
         3. set the password to a random string and email the user.

        """
        if self.has_config:
            choice = '1'
            username = self.username
            password = self.password
        else:
            choice = 'x'
            username = ''
            password = ''
        choices = '1 2 3 4'.split()
    # WARNING: Decompyle incomplete

    
    def build_post_data(self, action):
        meta = self.distribution.metadata
    # WARNING: Decompyle incomplete

    
    def post_to_server(self, data, auth = (None,)):
        '''Post a query to the server, and return a string response.'''
        if 'name' in data:
            self.announce('Registering {} to {}'.format(data['name'], self.repository), log.INFO)
        boundary = '--------------GHSKFJDLGDS7543FJKLFHRE75642756743254'
        sep_boundary = '\n--' + boundary
        end_boundary = sep_boundary + '--'
        body = io.StringIO()
        for key, value in data.items():
            if type(value) not in (type([]), type(())):
                value = [
                    value]
            for value in value:
                value = str(value)
                body.write(sep_boundary)
                body.write('\nContent-Disposition: form-data; name="%s"' % key)
                body.write('\n\n')
                body.write(value)
                if value and value[-1] == '\r':
                    body.write('\n')
                body.write(end_boundary)
                body.write('\n')
                body = body.getvalue().encode('utf-8')
                headers = {
                    'Content-type': 'multipart/form-data; boundary=%s; charset=utf-8' % boundary,
                    'Content-length': str(len(body)) }
                req = urllib.request.Request(self.repository, body, headers)
                opener = urllib.request.build_opener(urllib.request.HTTPBasicAuthHandler(password_mgr = auth))
                data = ''
                
                try:
                    result = opener.open(req)
                    if self.show_response:
                        data = self._read_pypi_response(result)
                    result = (200, 'OK')
                except urllib.error.HTTPError:
                    e = None
                    if self.show_response:
                        data = e.fp.read()
                    result = (e.code, e.msg)
                    e = None
                    del e
                except urllib.error.URLError:
                    e = None
                    result = (500, str(e))
                    e = None
                    del e
                except:
                    e = None
                    del e

                if self.show_response:
                    msg = '\n'.join(('---------------------------------------------------------------------------', data, '---------------------------------------------------------------------------'))
                    self.announce(msg, log.INFO)
        return result
