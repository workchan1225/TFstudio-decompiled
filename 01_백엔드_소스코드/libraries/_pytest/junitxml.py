# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: junitxml.pyc (Python 3.11)

'''Report test results in JUnit-XML format, for use with Jenkins and build
integration servers.

Based on initial code from Ross Lawley.

Output conforms to
https://github.com/jenkinsci/xunit-plugin/blob/master/src/main/resources/org/jenkinsci/plugins/xunit/types/model/xsd/junit-10.xsd
'''
from __future__ import annotations
from collections.abc import Callable
import functools
import os
import platform
import re

ElementTree
from _pytest import nodes
import xml.etree.ElementTree, etree
from _pytest import timing
from _pytest._code.code import ExceptionRepr
from _pytest._code.code import ReprFileLocation
from _pytest.config import Config
from _pytest.config import filename_arg
from _pytest.config.argparsing import Parser
from _pytest.fixtures import FixtureRequest
from _pytest.reports import TestReport
from _pytest.stash import StashKey
from _pytest.terminal import TerminalReporter
import pytest
xml_key = StashKey['LogXML']()

def bin_xml_escape(arg = None):
    """Visually escape invalid XML characters.

    For example, transforms
        'hello\\aworld\\b'
    into
        'hello#x07world#x08'
    Note that the #xABs are *not* XML escapes - missing the ampersand &#xAB.
    The idea is to escape visually for the user rather than for XML itself.
    """
    
    def repl(matchobj = None):
        i = ord(matchobj.group())
        if i <= 255:
            return f'''#x{i:02X}'''
        return f'''{i:04X}'''

    illegal_xml_re = '[^\t\n\r -~-퟿-�က0-ჿff]'
    return re.sub(illegal_xml_re, repl, str(arg))


def merge_family(left = None, right = None):
    result = { }
    for kl, vl in left.items():
        for kr, vr in right.items():
            if not isinstance(vl, list):
                raise TypeError(type(vl))
            result[kl] = vl + vr
            left.update(result)
            return None

families = {
    '_base': {
        'testcase': [
            'classname',
            'name'] },
    '_base_legacy': {
        'testcase': [
            'file',
            'line',
            'url'] } }
families['xunit1'] = families['_base'].copy()
merge_family(families['xunit1'], families['_base_legacy'])
families['xunit2'] = families['_base']

class _NodeReporter:
    
    def __init__(self = None, nodeid = None, xml = None):
        self.id = nodeid
        self.xml = xml
        self.add_stats = self.xml.add_stats
        self.family = self.xml.family
        self.duration = 0
        self.properties = []
        self.nodes = []
        self.attrs = { }

    
    def append(self = None, node = None):
        self.xml.add_stats(node.tag)
        self.nodes.append(node)

    
    def add_property(self = None, name = None, value = None):
        self.properties.append((str(name), bin_xml_escape(value)))

    
    def add_attribute(self = None, name = None, value = None):
        self.attrs[str(name)] = bin_xml_escape(value)

    
    def make_properties_node(self = None):
        '''Return a Junit node containing custom properties, if any.'''
        if self.properties:
            properties = ET.Element('properties')
            for name, value in self.properties:
                properties.append(ET.Element('property', name = name, value = value))
                return properties
                return None

    
    def record_testreport(self = None, testreport = None):
        names = mangle_test_address(testreport.nodeid)
        existing_attrs = self.attrs
        classnames = names[:-1]
        if self.xml.prefix:
            classnames.insert(0, self.xml.prefix)
        attrs = {
            'classname': '.'.join(classnames),
            'name': bin_xml_escape(names[-1]),
            'file': testreport.location[0] }
    # WARNING: Decompyle incomplete

    
    def to_xml(self = None):
        testcase = ET.Element('testcase', self.attrs, time = f'''{self.duration:.3f}''')
        properties = self.make_properties_node()
    # WARNING: Decompyle incomplete

    
    def _add_simple(self = None, tag = None, message = None, data = (None,)):
        node = ET.Element(tag, message = message)
        node.text = bin_xml_escape(data)
        self.append(node)

    
    def write_captured_output(self = None, report = None):
        if self.xml.log_passing_tests and report.passed:
            return None
        content_out = None.capstdout
        content_log = report.caplog
        content_err = report.capstderr
        if self.xml.logging == 'no':
            return None
        content_all = None
        if self.xml.logging in ('log', 'all'):
            content_all = self._prepare_content(content_log, ' Captured Log ')
        if self.xml.logging in ('system-out', 'out-err', 'all'):
            content_all += self._prepare_content(content_out, ' Captured Out ')
            self._write_content(report, content_all, 'system-out')
            content_all = ''
        if self.xml.logging in ('system-err', 'out-err', 'all'):
            content_all += self._prepare_content(content_err, ' Captured Err ')
            self._write_content(report, content_all, 'system-err')
            content_all = ''
        if content_all:
            self._write_content(report, content_all, 'system-out')
            return None

    
    def _prepare_content(self = None, content = None, header = None):
        return '\n'.join([
            header.center(80, '-'),
            content,
            ''])

    
    def _write_content(self = None, report = None, content = None, jheader = ('report', 'TestReport', 'content', 'str', 'jheader', 'str', 'return', 'None')):
        tag = ET.Element(jheader)
        tag.text = bin_xml_escape(content)
        self.append(tag)

    
    def append_pass(self = None, report = None):
        self.add_stats('passed')

    
    def append_failure(self = None, report = None):
        if hasattr(report, 'wasxfail'):
            self._add_simple('skipped', 'xfail-marked test passes unexpectedly')
            return None
    # WARNING: Decompyle incomplete

    
    def append_collect_error(self = None, report = None):
        pass
    # WARNING: Decompyle incomplete

    
    def append_collect_skipped(self = None, report = None):
        self._add_simple('skipped', 'collection skipped', str(report.longrepr))

    
    def append_error(self = None, report = None):
        pass
    # WARNING: Decompyle incomplete

    
    def append_skipped(self = None, report = None):
        if hasattr(report, 'wasxfail'):
            xfailreason = report.wasxfail
            if xfailreason.startswith('reason: '):
                xfailreason = xfailreason[8:]
            xfailreason = bin_xml_escape(xfailreason)
            skipped = ET.Element('skipped', type = 'pytest.xfail', message = xfailreason)
            self.append(skipped)
            return None
    # WARNING: Decompyle incomplete

    
    def finalize(self = None):
        pass
    # WARNING: Decompyle incomplete



def _warn_incompatibility_with_xunit2(request = None, fixture_name = None):
    '''Emit a PytestWarning about the given fixture being incompatible with newer xunit revisions.'''
    PytestWarning = PytestWarning
    import _pytest.warning_types
    xml = request.config.stash.get(xml_key, None)
# WARNING: Decompyle incomplete

record_property = (lambda request = None: pass# WARNING: Decompyle incomplete
)()
record_xml_attribute = (lambda request = None: PytestExperimentalApiWarning = PytestExperimentalApiWarningimport _pytest.warning_typesrequest.node.warn(PytestExperimentalApiWarning('record_xml_attribute is an experimental feature'))_warn_incompatibility_with_xunit2(request, 'record_xml_attribute')
def add_attr_noop(name = None, value = None):
passattr_func = add_attr_noopxml = request.config.stash.get(xml_key, None)# WARNING: Decompyle incomplete
)()

def _check_record_param_type(param = None, v = None):
    '''Used by record_testsuite_property to check that the given parameter name is of the proper
    type.'''
    __tracebackhide__ = True
    if not isinstance(v, str):
        msg = '{param} parameter needs to be a string, but {g} given'
        raise TypeError(msg.format(param = param, g = type(v).__name__))

record_testsuite_property = (lambda request = None: __tracebackhide__ = True
def record_func(name = None, value = None):
'''No-op function in case --junit-xml was not passed in the command-line.'''
__tracebackhide__ = True_check_record_param_type('name', name)xml = request.config.stash.get(xml_key, None)# WARNING: Decompyle incomplete
)()

def pytest_addoption(parser = None):
    group = parser.getgroup('terminal reporting')
    group.addoption('--junitxml', '--junit-xml', action = 'store', dest = 'xmlpath', metavar = 'path', type = functools.partial(filename_arg, optname = '--junitxml'), default = None, help = 'Create junit-xml style report file at given path')
    group.addoption('--junitprefix', '--junit-prefix', action = 'store', metavar = 'str', default = None, help = 'Prepend prefix to classnames in junit-xml output')
    parser.addini('junit_suite_name', 'Test suite name for JUnit report', default = 'pytest')
    parser.addini('junit_logging', 'Write captured log messages to JUnit report: one of no|log|system-out|system-err|out-err|all', default = 'no')
    parser.addini('junit_log_passing_tests', 'Capture log information for passing tests to JUnit report: ', type = 'bool', default = True)
    parser.addini('junit_duration_report', 'Duration time to report: one of total|call', default = 'total')
    parser.addini('junit_family', 'Emit XML for schema: one of legacy|xunit1|xunit2', default = 'xunit2')


def pytest_configure(config = None):
    xmlpath = config.option.xmlpath
    if not xmlpath or hasattr(config, 'workerinput'):
        junit_family = config.getini('junit_family')
        config.stash[xml_key] = LogXML(xmlpath, config.option.junitprefix, config.getini('junit_suite_name'), config.getini('junit_logging'), config.getini('junit_duration_report'), junit_family, config.getini('junit_log_passing_tests'))
        config.pluginmanager.register(config.stash[xml_key])
        return None
    return None


def pytest_unconfigure(config = None):
    xml = config.stash.get(xml_key, None)
    if xml:
        del config.stash[xml_key]
        config.pluginmanager.unregister(xml)
        return None


def mangle_test_address(address = None):
    (path, possible_open_bracket, params) = address.partition('[')
    names = path.split('::')
    names[0] = names[0].replace(nodes.SEP, '.')
    names[0] = re.sub('\\.py$', '', names[0])
    return names


class LogXML:
    
    def __init__(self, logfile, prefix, suite_name = None, logging = None, report_duration = None, family = ('pytest', 'no', 'total', 'xunit1', True), log_passing_tests = ('prefix', 'str | None', 'suite_name', 'str', 'logging', 'str', 'report_duration', 'str', 'log_passing_tests', 'bool', 'return', 'None')):
        logfile = os.path.expanduser(os.path.expandvars(logfile))
        self.logfile = os.path.normpath(os.path.abspath(logfile))
        self.prefix = prefix
        self.suite_name = suite_name
        self.logging = logging
        self.log_passing_tests = log_passing_tests
        self.report_duration = report_duration
        self.family = family
        self.stats = dict.fromkeys([
            'error',
            'passed',
            'failure',
            'skipped'], 0)
        self.node_reporters = { }
        self.node_reporters_ordered = []
        self.global_properties = []
        self.open_reports = []
        self.cnt_double_fail_tests = 0
        if self.family == 'legacy':
            self.family = 'xunit1'
            return None

    
    def finalize(self = None, report = None):
        nodeid = getattr(report, 'nodeid', report)
        workernode = getattr(report, 'node', None)
        reporter = self.node_reporters.pop((nodeid, workernode))
    # WARNING: Decompyle incomplete

    
    def node_reporter(self = None, report = None):
        nodeid = getattr(report, 'nodeid', report)
        workernode = getattr(report, 'node', None)
        key = (nodeid, workernode)
        if key in self.node_reporters:
            return self.node_reporters[key]
        reporter = None(nodeid, self)
        self.node_reporters[key] = reporter
        self.node_reporters_ordered.append(reporter)
        return reporter

    
    def add_stats(self = None, key = None):
        if key in self.stats:
            return None

    
    def _opentestcase(self = None, report = None):
        reporter = self.node_reporter(report)
        reporter.record_testreport(report)
        return reporter

    
    def pytest_runtest_logreport(self = None, report = None):
        '''Handle a setup/call/teardown report, generating the appropriate
        XML tags as necessary.

        Note: due to plugins like xdist, this hook may be called in interlaced
        order with reports from other nodes. For example:

        Usual call order:
            -> setup node1
            -> call node1
            -> teardown node1
            -> setup node2
            -> call node2
            -> teardown node2

        Possible call order in xdist:
            -> setup node1
            -> call node1
            -> setup node2
            -> call node2
            -> teardown node2
            -> teardown node1
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def update_testcase_duration(self = None, report = None):
        '''Accumulate total duration for nodeid from given report and update
        the Junit.testcase with the new total if already created.'''
        if self.report_duration in {
            'total',
            report.when}:
            reporter = self.node_reporter(report)
            return None

    
    def pytest_collectreport(self = None, report = None):
        if not report.passed:
            reporter = self._opentestcase(report)
            if report.failed:
                reporter.append_collect_error(report)
                return None
            None.append_collect_skipped(report)
            return None

    
    def pytest_internalerror(self = None, excrepr = None):
        reporter = self.node_reporter('internal')
        reporter.attrs.update(classname = 'pytest', name = 'internal')
        reporter._add_simple('error', 'internal error', str(excrepr))

    
    def pytest_sessionstart(self = None):
        self.suite_start = timing.Instant()

    
    def pytest_sessionfinish(self = None):
        dirname = os.path.dirname(os.path.abspath(self.logfile))
        os.makedirs(dirname, exist_ok = True)
        logfile = open(self.logfile, 'w', encoding = 'utf-8')
        duration = self.suite_start.elapsed()
        numtests = self.stats['passed'] + self.stats['failure'] + self.stats['skipped'] + self.stats['error'] - self.cnt_double_fail_tests
        logfile.write('<?xml version="1.0" encoding="utf-8"?>')
        suite_node = ET.Element('testsuite', name = self.suite_name, errors = str(self.stats['error']), failures = str(self.stats['failure']), skipped = str(self.stats['skipped']), tests = str(numtests), time = f'''{duration.seconds:.3f}''', timestamp = self.suite_start.as_utc().astimezone().isoformat(), hostname = platform.node())
        global_properties = self._get_global_properties_node()
    # WARNING: Decompyle incomplete

    
    def pytest_terminal_summary(self = None, terminalreporter = None, config = None):
        if config.get_verbosity() >= 0:
            terminalreporter.write_sep('-', f'''generated xml file: {self.logfile}''')
            return None

    
    def add_global_property(self = None, name = None, value = None):
        __tracebackhide__ = True
        _check_record_param_type('name', name)
        self.global_properties.append((name, bin_xml_escape(value)))

    
    def _get_global_properties_node(self = None):
        '''Return a Junit node containing custom properties, if any.'''
        if self.global_properties:
            properties = ET.Element('properties')
            for name, value in self.global_properties:
                properties.append(ET.Element('property', name = name, value = value))
                return properties
                return None
