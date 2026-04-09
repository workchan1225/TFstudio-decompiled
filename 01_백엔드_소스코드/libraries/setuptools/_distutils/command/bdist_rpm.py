# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bdist_rpm.pyc (Python 3.11)

"""distutils.command.bdist_rpm

Implements the Distutils 'bdist_rpm' command (create RPM source and binary
distributions)."""
import subprocess
import sys
import os
from distutils.core import Command
from distutils.debug import DEBUG
from distutils.file_util import write_file
from distutils.errors import DistutilsOptionError, DistutilsPlatformError, DistutilsFileError, DistutilsExecError
from distutils.sysconfig import get_python_version
from distutils import log

class bdist_rpm(Command):
    description = 'create an RPM distribution'
    user_options = [
        ('bdist-base=', None, 'base directory for creating built distributions'),
        ('rpm-base=', None, 'base directory for creating RPMs (defaults to "rpm" under --bdist-base; must be specified for RPM 2)'),
        ('dist-dir=', 'd', 'directory to put final RPM files in (and .spec files if --spec-only)'),
        ('python=', None, 'path to Python interpreter to hard-code in the .spec file (default: "python")'),
        ('fix-python', None, 'hard-code the exact path to the current Python interpreter in the .spec file'),
        ('spec-only', None, 'only regenerate spec file'),
        ('source-only', None, 'only generate source RPM'),
        ('binary-only', None, 'only generate binary RPM'),
        ('use-bzip2', None, 'use bzip2 instead of gzip to create source distribution'),
        ('distribution-name=', None, 'name of the (Linux) distribution to which this RPM applies (*not* the name of the module distribution!)'),
        ('group=', None, 'package classification [default: "Development/Libraries"]'),
        ('release=', None, 'RPM release number'),
        ('serial=', None, 'RPM serial number'),
        ('vendor=', None, 'RPM "vendor" (eg. "Joe Blow <joe@example.com>") [default: maintainer or author from setup script]'),
        ('packager=', None, 'RPM packager (eg. "Jane Doe <jane@example.net>") [default: vendor]'),
        ('doc-files=', None, 'list of documentation files (space or comma-separated)'),
        ('changelog=', None, 'RPM changelog'),
        ('icon=', None, 'name of icon file'),
        ('provides=', None, 'capabilities provided by this package'),
        ('requires=', None, 'capabilities required by this package'),
        ('conflicts=', None, 'capabilities which conflict with this package'),
        ('build-requires=', None, 'capabilities required to build this package'),
        ('obsoletes=', None, 'capabilities made obsolete by this package'),
        ('no-autoreq', None, 'do not automatically calculate dependencies'),
        ('keep-temp', 'k', "don't clean up RPM build directory"),
        ('no-keep-temp', None, 'clean up RPM build directory [default]'),
        ('use-rpm-opt-flags', None, 'compile with RPM_OPT_FLAGS when building from source RPM'),
        ('no-rpm-opt-flags', None, 'do not pass any RPM CFLAGS to compiler'),
        ('rpm3-mode', None, 'RPM 3 compatibility mode (default)'),
        ('rpm2-mode', None, 'RPM 2 compatibility mode'),
        ('prep-script=', None, 'Specify a script for the PREP phase of RPM building'),
        ('build-script=', None, 'Specify a script for the BUILD phase of RPM building'),
        ('pre-install=', None, 'Specify a script for the pre-INSTALL phase of RPM building'),
        ('install-script=', None, 'Specify a script for the INSTALL phase of RPM building'),
        ('post-install=', None, 'Specify a script for the post-INSTALL phase of RPM building'),
        ('pre-uninstall=', None, 'Specify a script for the pre-UNINSTALL phase of RPM building'),
        ('post-uninstall=', None, 'Specify a script for the post-UNINSTALL phase of RPM building'),
        ('clean-script=', None, 'Specify a script for the CLEAN phase of RPM building'),
        ('verify-script=', None, 'Specify a script for the VERIFY phase of the RPM build'),
        ('force-arch=', None, 'Force an architecture onto the RPM build process'),
        ('quiet', 'q', 'Run the INSTALL phase of RPM building in quiet mode')]
    boolean_options = [
        'keep-temp',
        'use-rpm-opt-flags',
        'rpm3-mode',
        'no-autoreq',
        'quiet']
    negative_opt = {
        'no-keep-temp': 'keep-temp',
        'no-rpm-opt-flags': 'use-rpm-opt-flags',
        'rpm2-mode': 'rpm3-mode' }
    
    def initialize_options(self):
        self.bdist_base = None
        self.rpm_base = None
        self.dist_dir = None
        self.python = None
        self.fix_python = None
        self.spec_only = None
        self.binary_only = None
        self.source_only = None
        self.use_bzip2 = None
        self.distribution_name = None
        self.group = None
        self.release = None
        self.serial = None
        self.vendor = None
        self.packager = None
        self.doc_files = None
        self.changelog = None
        self.icon = None
        self.prep_script = None
        self.build_script = None
        self.install_script = None
        self.clean_script = None
        self.verify_script = None
        self.pre_install = None
        self.post_install = None
        self.pre_uninstall = None
        self.post_uninstall = None
        self.prep = None
        self.provides = None
        self.requires = None
        self.conflicts = None
        self.build_requires = None
        self.obsoletes = None
        self.keep_temp = 0
        self.use_rpm_opt_flags = 1
        self.rpm3_mode = 1
        self.no_autoreq = 0
        self.force_arch = None
        self.quiet = 0

    
    def finalize_options(self):
        self.set_undefined_options('bdist', ('bdist_base', 'bdist_base'))
    # WARNING: Decompyle incomplete

    
    def finalize_package_data(self):
        self.ensure_string('group', 'Development/Libraries')
        self.ensure_string('vendor', f'''{self.distribution.get_contact()!s} <{self.distribution.get_contact_email()!s}>''')
        self.ensure_string('packager')
        self.ensure_string_list('doc_files')
        if isinstance(self.doc_files, list):
            for readme in ('README', 'README.txt'):
                if os.path.exists(readme) and readme not in self.doc_files:
                    self.doc_files.append(readme)
                self.ensure_string('release', '1')
                self.ensure_string('serial')
                self.ensure_string('distribution_name')
                self.ensure_string('changelog')
                self.changelog = self._format_changelog(self.changelog)
                self.ensure_filename('icon')
                self.ensure_filename('prep_script')
                self.ensure_filename('build_script')
                self.ensure_filename('install_script')
                self.ensure_filename('clean_script')
                self.ensure_filename('verify_script')
                self.ensure_filename('pre_install')
                self.ensure_filename('post_install')
                self.ensure_filename('pre_uninstall')
                self.ensure_filename('post_uninstall')
                self.ensure_string_list('provides')
                self.ensure_string_list('requires')
                self.ensure_string_list('conflicts')
                self.ensure_string_list('build_requires')
                self.ensure_string_list('obsoletes')
                self.ensure_string('force_arch')
                return None

    
    def run(self):
        if DEBUG:
            print('before _get_package_data():')
            print('vendor =', self.vendor)
            print('packager =', self.packager)
            print('doc_files =', self.doc_files)
            print('changelog =', self.changelog)
        if self.spec_only:
            spec_dir = self.dist_dir
            self.mkpath(spec_dir)
        else:
            rpm_dir = { }
            for d in ('SOURCES', 'SPECS', 'BUILD', 'RPMS', 'SRPMS'):
                rpm_dir[d] = os.path.join(self.rpm_base, d)
                self.mkpath(rpm_dir[d])
                spec_dir = rpm_dir['SPECS']
                spec_path = os.path.join(spec_dir, '%s.spec' % self.distribution.get_name())
                self.execute(write_file, (spec_path, self._make_spec_file()), "writing '%s'" % spec_path)
                if self.spec_only:
                    return None
                saved_dist_files = None.distribution.dist_files[:]
                sdist = self.reinitialize_command('sdist')
                if self.use_bzip2:
                    sdist.formats = [
                        'bztar']
                else:
                    sdist.formats = [
                        'gztar']
        self.run_command('sdist')
        self.distribution.dist_files = saved_dist_files
        source = sdist.get_archive_files()[0]
        source_dir = rpm_dir['SOURCES']
        self.copy_file(source, source_dir)
        if self.icon:
            if os.path.exists(self.icon):
                self.copy_file(self.icon, source_dir)
            else:
                raise DistutilsFileError("icon file '%s' does not exist" % self.icon)
        log.info('building RPMs')
        rpm_cmd = [
            'rpmbuild']
        if self.source_only:
            rpm_cmd.append('-bs')
        elif self.binary_only:
            rpm_cmd.append('-bb')
        else:
            rpm_cmd.append('-ba')
        rpm_cmd.extend([
            '--define',
            '__python %s' % self.python])
        if self.rpm3_mode:
            rpm_cmd.extend([
                '--define',
                '_topdir %s' % os.path.abspath(self.rpm_base)])
        if not self.keep_temp:
            rpm_cmd.append('--clean')
        if self.quiet:
            rpm_cmd.append('--quiet')
        rpm_cmd.append(spec_path)
        nvr_string = '%{name}-%{version}-%{release}'
        src_rpm = nvr_string + '.src.rpm'
        non_src_rpm = '%{arch}/' + nvr_string + '.%{arch}.rpm'
        q_cmd = "rpm -q --qf '{} {}\\n' --specfile '{}'".format(src_rpm, non_src_rpm, spec_path)
        out = os.popen(q_cmd)
    # WARNING: Decompyle incomplete

    
    def _dist_path(self, path):
        return os.path.join(self.dist_dir, os.path.basename(path))

    
    def _make_spec_file(self):
        '''Generate the text of an RPM spec file and return it as a
        list of strings (one per line).
        '''
        if not self.distribution.get_description():
            spec_file = [
                '%define name ' + self.distribution.get_name(),
                '%define version ' + self.distribution.get_version().replace('-', '_'),
                '%define unmangled_version ' + self.distribution.get_version(),
                '%define release ' + self.release.replace('-', '_'),
                '',
                'Summary: ' + 'UNKNOWN']
            vendor_hook = subprocess.getoutput('rpm --eval %{__os_install_post}')
            vendor_hook = (lambda .0: [ '  %s \\' % line.strip() for line in .0 ])(vendor_hook.splitlines()())
            problem = 'brp-python-bytecompile \\\n'
            fixed = 'brp-python-bytecompile %{__python} \\\n'
            fixed_hook = vendor_hook.replace(problem, fixed)
            if fixed_hook != vendor_hook:
                spec_file.append('# Workaround for http://bugs.python.org/issue14443')
                spec_file.append('%define __os_install_post ' + fixed_hook + '\n')
        spec_file.extend([
            'Name: %{name}',
            'Version: %{version}',
            'Release: %{release}'])
        if not self.distribution.get_license():
            spec_file.extend([
                'License: ' + 'UNKNOWN',
                'Group: ' + self.group,
                'BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot',
                'Prefix: %{_prefix}'])
            if not self.force_arch:
                pass
    # WARNING: Decompyle incomplete

    
    def _format_changelog(self, changelog):
        '''Format the changelog correctly and convert it to a list of strings'''
        if not changelog:
            return changelog
        new_changelog = None
        for line in changelog.strip().split('\n'):
            line = line.strip()
            if line[0] == '*':
                new_changelog.extend([
                    '',
                    line])
                continue
            if line[0] == '-':
                new_changelog.append(line)
                continue
            new_changelog.append('  ' + line)
            if not new_changelog[0]:
                del new_changelog[0]
        return new_changelog
