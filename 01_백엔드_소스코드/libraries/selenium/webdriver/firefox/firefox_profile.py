# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: firefox_profile.pyc (Python 3.11)

import base64
import copy
import json
import os
import re
import shutil
import sys
import tempfile
import warnings
import zipfile
from io import BytesIO
from xml.dom import minidom
from typing_extensions import deprecated
from selenium.common.exceptions import WebDriverException
WEBDRIVER_PREFERENCES = 'webdriver_prefs.json'
AddonFormatError = <NODE:12>()

class FirefoxProfile:
    DEFAULT_PREFERENCES = None
    
    def __init__(self, profile_directory = (None,)):
        '''Initialises a new instance of a Firefox Profile.

        Args:
            profile_directory: Directory of profile that you want to use. If a
                directory is passed in it will be cloned and the cloned directory
                will be used by the driver when instantiated.
                This defaults to None and will create a new
                directory when object is created.
        '''
        self._desired_preferences = { }
        if profile_directory:
            newprof = os.path.join(tempfile.mkdtemp(), 'webdriver-py-profilecopy')
            shutil.copytree(profile_directory, newprof, ignore = shutil.ignore_patterns('parent.lock', 'lock', '.parentlock'))
            self._profile_dir = newprof
            os.chmod(self._profile_dir, 493)
            return None
        self._profile_dir = None.mkdtemp()
        if not FirefoxProfile.DEFAULT_PREFERENCES:
            default_prefs = open(os.path.join(os.path.dirname(__file__), WEBDRIVER_PREFERENCES), encoding = 'utf-8')
            FirefoxProfile.DEFAULT_PREFERENCES = json.load(default_prefs)
            None(None, None)
        else:
            with None:
                if not None:
                    pass
        self._desired_preferences = copy.deepcopy(FirefoxProfile.DEFAULT_PREFERENCES['mutable'])
        for key, value in FirefoxProfile.DEFAULT_PREFERENCES['frozen'].items():
            self._desired_preferences[key] = value
            return None

    
    def set_preference(self, key, value):
        '''Sets the preference that we want in the profile.'''
        self._desired_preferences[key] = value

    add_extension = (lambda self, extension = (None,): self._install_extension(extension))()
    
    def update_preferences(self):
        '''Writes the desired user prefs to disk.'''
        user_prefs = os.path.join(self._profile_dir, 'user.js')
        if os.path.isfile(user_prefs):
            os.chmod(user_prefs, 420)
            self._read_existing_userjs(user_prefs)
        f = open(user_prefs, 'w', encoding = 'utf-8')
        for key, value in self._desired_preferences.items():
            f.write(f'''user_pref("{key}", {json.dumps(value)});\n''')
            None(None, None)
            return None
            with None:
                if not None:
                    pass

    path = (lambda self: self._profile_dir)()
    port = (lambda self: self._port)()()
    port = (lambda self = deprecated('The port is stored in the Service class'), port = port.setter: if not isinstance(port, int):
raise WebDriverException('Port needs to be an integer')try:
port = int(port)if port < 1 or port > 65535:
raise WebDriverException('Port number must be in the range 1..65535')except (ValueError, TypeError):
raise WebDriverException('Port needs to be an integer')self._port = portself.set_preference('webdriver_firefox_port', self._port))()()
    accept_untrusted_certs = (lambda self: self._desired_preferences['webdriver_accept_untrusted_certs'])()()
    accept_untrusted_certs = (lambda self = deprecated('Allowing untrusted certs is toggled in the Options class'), value = accept_untrusted_certs.setter: if not isinstance(value, bool):
raise WebDriverException('Please pass in a Boolean to this call')self.set_preference('webdriver_accept_untrusted_certs', value))()()
    assume_untrusted_cert_issuer = (lambda self: self._desired_preferences['webdriver_assume_untrusted_issuer'])()()
    assume_untrusted_cert_issuer = (lambda self = deprecated('Allowing untrusted certs is toggled in the Options class'), value = assume_untrusted_cert_issuer.setter: if not isinstance(value, bool):
raise WebDriverException('Please pass in a Boolean to this call')self.set_preference('webdriver_assume_untrusted_issuer', value))()()
    encoded = (lambda self = property: if self._desired_preferences:
self.update_preferences()fp = BytesIO()zipped = zipfile.ZipFile(fp, 'w', zipfile.ZIP_DEFLATED, strict_timestamps = False)path_root = len(self.path) + 1for base, _, files in os.walk(self.path):
for fyle in files:
filename = os.path.join(base, fyle)zipped.write(filename, filename[path_root:])None(None, None)with None:
if not None:
passbase64.b64encode(fp.getvalue()).decode('UTF-8'))()
    
    def _read_existing_userjs(self, userjs):
        '''Read existing preferences and add them to the desired preference dictionary.'''
        pref_pattern = re.compile('user_pref\\("(.*)",\\s(.*)\\)')
        f = open(userjs, encoding = 'utf-8')
        for usr in f:
            matches = pref_pattern.search(usr)
            self._desired_preferences[matches.group(1)] = json.loads(matches.group(2))
            except Exception:
                warnings.warn(f'''(skipping) failed to json.loads existing preference: {matches.group(1) + matches.group(2)}''')
                continue
            None(None, None)
            return None
            with None:
                if not None:
                    pass

    _install_extension = (lambda self, addon, unpack = (True,): tmpdir = Nonexpifile = Noneif addon.endswith('.xpi'):
tmpdir = tempfile.mkdtemp(suffix = '.' + os.path.split(addon)[-1])compressed_file = zipfile.ZipFile(addon, 'r')for name in compressed_file.namelist():
if name.endswith('/'):
if not os.path.isdir(os.path.join(tmpdir, name)):
os.makedirs(os.path.join(tmpdir, name))continueif not os.path.isdir(os.path.dirname(os.path.join(tmpdir, name))):
os.makedirs(os.path.dirname(os.path.join(tmpdir, name)))data = compressed_file.read(name)f = open(os.path.join(tmpdir, name), 'wb')f.write(data)None(None, None)with None:
if not None:
passcontinuexpifile = addonaddon = tmpdiraddon_details = self._addon_details(addon)addon_id = addon_details.get('id')# WARNING: Decompyle incomplete
)()
    _addon_details = (lambda self, addon_path: details = {
'id': None,
'unpack': False,
'name': None,
'version': None }
def get_namespace_id(doc, url):
attributes = doc.documentElement.attributesnamespace = ''for i in range(attributes.length):
if attributes.item(i).value == url and ':' in attributes.item(i).name:
namespace = attributes.item(i).name.split(':')[1] + ':'namespace
def get_text(element):
'''Retrieve the text value of a given node.'''
rc = []for node in element.childNodes:
if node.nodeType == node.TEXT_NODE:
rc.append(node.data)''.join(rc).strip()
def parse_manifest_json(content):
'''Extract details from the contents of a WebExtensions manifest.json file.'''
manifest = json.loads(content)try:
id = manifest['applications']['gecko']['id']except KeyError:
id = manifest['name'].replace(' ', '') + '@' + manifest['version']{
'id': id,
'version': manifest['version'],
'name': manifest['version'],
'unpack': False }if not os.path.exists(addon_path):
raise OSError(f'''Add-on path does not exist: {addon_path}''')try:
if zipfile.is_zipfile(addon_path):
compressed_file = zipfile.ZipFile(addon_path, 'r')if 'manifest.json' in compressed_file.namelist():
try:
None(None, None)try:
None(None, None)with None:
if not compressed_file.read('install.rdf'):
try:
try:
None, parse_manifest_json(compressed_file.read('manifest.json'))if os.path.isdir(addon_path):
os.path.join(addon_path, 'manifest.json') = None, parse_manifest_json(compressed_file.read('manifest.json'))if os.path.exists(manifest_json_filename):
f = open(manifest_json_filename, encoding = 'utf-8')try:
None(None, None)with None:
if not None, parse_manifest_json(f.read()):
try:
try:
f.read() = open(os.path.join(addon_path, 'install.rdf'), encoding = 'utf-8')try:
None(None, None)with None:
if not None:
try:
try:
passraise OSError(f'''Add-on path is neither an XPI nor a directory: {addon_path}''')except (OSError, KeyError):
e = Noneraise AddonFormatError(str(e), sys.exc_info()[2])e = Nonedel etry:
doc = minidom.parseString(manifest)em = get_namespace_id(doc, 'http://www.mozilla.org/2004/em-rdf#')rdf = get_namespace_id(doc, 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')description = doc.getElementsByTagName(rdf + 'Description').item(0)if not description:
description = doc.getElementsByTagName('Description').item(0)for node in description.childNodes:
entry = node.nodeName.replace(em, '')if entry in details:
details.update({
entry: get_text(node) })if not details.get('id'):
for i in range(description.attributes.length):
attribute = description.attributes.item(i)if attribute.name == em + 'id':
details.update({
'id': attribute.value })except Exception:
e = Noneraise AddonFormatError(str(e), sys.exc_info()[2])e = Nonedel eif isinstance(details['unpack'], str):
details['unpack'] = details['unpack'].lower() == 'true'if not details.get('id'):
raise AddonFormatError('Add-on id could not be found.')details)()
