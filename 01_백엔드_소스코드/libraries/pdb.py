# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pdb.pyc (Python 3.11)

__doc__ = '\nThe Python Debugger Pdb\n=======================\n\nTo use the debugger in its simplest form:\n\n        >>> import pdb\n        >>> pdb.run(\'<a statement>\')\n\nThe debugger\'s prompt is \'(Pdb) \'.  This will stop in the first\nfunction call in <a statement>.\n\nAlternatively, if a statement terminated with an unhandled exception,\nyou can use pdb\'s post-mortem facility to inspect the contents of the\ntraceback:\n\n        >>> <a statement>\n        <exception traceback>\n        >>> import pdb\n        >>> pdb.pm()\n\nThe commands recognized by the debugger are listed in the next\nsection.  Most can be abbreviated as indicated; e.g., h(elp) means\nthat \'help\' can be typed as \'h\' or \'help\' (but not as \'he\' or \'hel\',\nnor as \'H\' or \'Help\' or \'HELP\').  Optional arguments are enclosed in\nsquare brackets.  Alternatives in the command syntax are separated\nby a vertical bar (|).\n\nA blank line repeats the previous command literally, except for\n\'list\', where it lists the next 11 lines.\n\nCommands that the debugger doesn\'t recognize are assumed to be Python\nstatements and are executed in the context of the program being\ndebugged.  Python statements can also be prefixed with an exclamation\npoint (\'!\').  This is a powerful way to inspect the program being\ndebugged; it is even possible to change variables or call functions.\nWhen an exception occurs in such a statement, the exception name is\nprinted but the debugger\'s state is not changed.\n\nThe debugger supports aliases, which can save typing.  And aliases can\nhave parameters (see the alias help entry) which allows one a certain\nlevel of adaptability to the context under examination.\n\nMultiple commands may be entered on a single line, separated by the\npair \';;\'.  No intelligence is applied to separating the commands; the\ninput is split at the first \';;\', even if it is in the middle of a\nquoted string.\n\nIf a file ".pdbrc" exists in your home directory or in the current\ndirectory, it is read in and executed as if it had been typed at the\ndebugger prompt.  This is particularly useful for aliases.  If both\nfiles exist, the one in the home directory is read first and aliases\ndefined there can be overridden by the local file.  This behavior can be\ndisabled by passing the "readrc=False" argument to the Pdb constructor.\n\nAside from aliases, the debugger is not directly programmable; but it\nis implemented as a class from which you can derive your own debugger\nclass, which you can make as fancy as you like.\n\n\nDebugger commands\n=================\n\n'
import os
import io
import re
import sys
import cmd
import bdb
import dis
import code
import glob
import pprint
import signal
import inspect
import tokenize
import functools
import traceback
import linecache
from typing import Union

class Restart(Exception):
    '''Causes a debugger to be restarted for the debugged python program.'''
    pass

__all__ = [
    'run',
    'pm',
    'Pdb',
    'runeval',
    'runctx',
    'runcall',
    'set_trace',
    'post_mortem',
    'help']

def find_function(funcname, filename):
    cre = re.compile('def\\s+%s\\s*[(]' % re.escape(funcname))
    
    try:
        fp = tokenize.open(filename)
    except OSError:
        return None

    fp
    for lineno, line in enumerate(fp, start = 1):
        if cre.match(line):
            
            None(None, None)
            return 
        None(None, None)
    with None:
        if not None:
            pass


def lasti2lineno(code, lasti):
    linestarts = list(dis.findlinestarts(code))
    linestarts.reverse()
    for i, lineno in linestarts:
        if lasti >= i:
            
            return None, lineno
        return 0


class _rstr(str):
    """String that doesn't quote its repr."""
    
    def __repr__(self):
        return self



class _ScriptTarget(str):
    pass
# WARNING: Decompyle incomplete


class _ModuleTarget(str):
    
    def check(self):
        
        try:
            self._details
            return None
        except ImportError:
            e = None
            print(f'''ImportError: {e}''')
            sys.exit(1)
            e = None
            del e
            return None
            e = None
            del e
            except Exception:
                traceback.print_exc()
                sys.exit(1)
                return None


    _details = (lambda self: import runpyrunpy._get_module_details(self))()
    filename = (lambda self: self.code.co_filename)()
    code = (lambda self: (name, spec, code) = self._detailscode)()
    _spec = (lambda self: (name, spec, code) = self._detailsspec)()
    namespace = (lambda self: dict(__name__ = '__main__', __file__ = os.path.normcase(os.path.abspath(self.filename)), __package__ = self._spec.parent, __loader__ = self._spec.loader, __spec__ = self._spec, __builtins__ = __builtins__))()

line_prefix = '\n-> '

class Pdb(cmd.Cmd, bdb.Bdb):
    _previous_sigint_handler = None
    
    def __init__(self, completekey, stdin, stdout, skip, nosigint, readrc = ('tab', None, None, None, False, True)):
        bdb.Bdb.__init__(self, skip = skip)
        cmd.Cmd.__init__(self, completekey, stdin, stdout)
        sys.audit('pdb.Pdb')
        if stdout:
            self.use_rawinput = 0
        self.prompt = '(Pdb) '
        self.aliases = { }
        self.displaying = { }
        self.mainpyfile = ''
        self._wait_for_mainpyfile = False
        self.tb_lineno = { }
        
        try:
            import readline
            readline.set_completer_delims(' \t\n`@#$%^&*()=+[{]}\\|;:\'",<>?')
        except ImportError:
            pass

        self.allow_kbdint = False
        self.nosigint = nosigint
        self.rcLines = []
        if readrc:
            
            try:
                rcFile = open(os.path.expanduser('~/.pdbrc'), encoding = 'utf-8')
                self.rcLines.extend(rcFile)
                
                try:
                    None(None, None)
                with None:
                    if not None:
                        
                        try:
                            
                            try:
                                pass
                            except OSError:
                                pass

                            
                            try:
                                rcFile = open('.pdbrc', encoding = 'utf-8')
                                self.rcLines.extend(rcFile)
                                
                                try:
                                    None(None, None)
                                with None:
                                    if not None:
                                        
                                        try:
                                            
                                            try:
                                                pass
                                            except OSError:
                                                pass

                                            self.commands = { }
                                            self.commands_doprompt = { }
                                            self.commands_silent = { }
                                            self.commands_defining = False
                                            self.commands_bnum = None
                                            return None







    
    def sigint_handler(self, signum, frame):
        if self.allow_kbdint:
            raise KeyboardInterrupt
        self.message("\nProgram interrupted. (Use 'cont' to resume).")
        self.set_step()
        self.set_trace(frame)

    
    def reset(self):
        bdb.Bdb.reset(self)
        self.forget()

    
    def forget(self):
        self.lineno = None
        self.stack = []
        self.curindex = 0
        self.curframe = None
        self.tb_lineno.clear()

    
    def setup(self, f, tb):
        self.forget()
        (self.stack, self.curindex) = self.get_stack(f, tb)
    # WARNING: Decompyle incomplete

    
    def execRcLines(self):
        if not self.rcLines:
            return None
        rcLines = None.rcLines
        rcLines.reverse()
        self.rcLines = []
    # WARNING: Decompyle incomplete

    
    def user_call(self, frame, argument_list):
        '''This method is called when there is the remote possibility
        that we ever need to stop in this function.'''
        if self._wait_for_mainpyfile:
            return None
        if None.stop_here(frame):
            self.message('--Call--')
            self.interaction(frame, None)
            return None

    
    def user_line(self, frame):
        '''This function is called when we stop or break at this line.'''
        if self._wait_for_mainpyfile:
            if self.mainpyfile != self.canonic(frame.f_code.co_filename) or frame.f_lineno <= 0:
                return None
            self._wait_for_mainpyfile = None
        if self.bp_commands(frame):
            self.interaction(frame, None)
            return None

    
    def bp_commands(self, frame):
        '''Call every command that was set for the current active breakpoint
        (if there is one).

        Returns True if the normal interaction function must be called,
        False otherwise.'''
        if getattr(self, 'currentbp', False) and self.currentbp in self.commands:
            currentbp = self.currentbp
            self.currentbp = 0
            lastcmd_back = self.lastcmd
            self.setup(frame, None)
            for line in self.commands[currentbp]:
                self.onecmd(line)
                self.lastcmd = lastcmd_back
                if not self.commands_silent[currentbp]:
                    self.print_stack_entry(self.stack[self.curindex])
            if self.commands_doprompt[currentbp]:
                self._cmdloop()
            self.forget()
            return None
        return 1

    
    def user_return(self, frame, return_value):
        '''This function is called when a return trap is set here.'''
        if self._wait_for_mainpyfile:
            return None
        frame.f_locals['__return__'] = None
        self.message('--Return--')
        self.interaction(frame, None)

    
    def user_exception(self, frame, exc_info):
        '''This function is called if an exception occurs,
        but only if we are to stop at or just below this level.'''
        if self._wait_for_mainpyfile:
            return None
        (exc_type, exc_value, exc_traceback) = None
        frame.f_locals['__exception__'] = (exc_type, exc_value)
        prefix = 'Internal ' if exc_traceback and exc_type is StopIteration else ''
        self.message(f'''{prefix!s}{traceback.format_exception_only(exc_type, exc_value)[-1].strip()!s}''')
        self.interaction(frame, exc_traceback)

    
    def _cmdloop(self):
        
        try:
            self.allow_kbdint = True
            self.cmdloop()
            self.allow_kbdint = False
            return None
        except KeyboardInterrupt:
            self.message('--KeyboardInterrupt--')

        continue

    
    def preloop(self):
        displaying = self.displaying.get(self.curframe)
        if displaying:
            for expr, oldvalue in displaying.items():
                newvalue = self._getval_except(expr)
                if newvalue is not oldvalue and newvalue != oldvalue:
                    displaying[expr] = newvalue
                    self.message(f'''display {expr!s}: {self._safe_repr(newvalue, expr)!s}  [old: {self._safe_repr(oldvalue, expr)!s}]''')
                return None
                return None

    
    def interaction(self, frame, traceback):
        if Pdb._previous_sigint_handler:
            
            try:
                signal.signal(signal.SIGINT, Pdb._previous_sigint_handler)
                Pdb._previous_sigint_handler = None
            except ValueError:
                pass

            if self.setup(frame, traceback):
                self.forget()
                return None
            None.print_stack_entry(self.stack[self.curindex])
            self._cmdloop()
            self.forget()
            return None

    
    def displayhook(self, obj):
        '''Custom displayhook for the exec in default(), which prevents
        assignment of the _ variable in the builtins.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def default(self, line):
        if line[:1] == '!':
            line = line[1:]
        locals = self.curframe_locals
        globals = self.curframe.f_globals
        
        try:
            code = compile(line + '\n', '<stdin>', 'single')
            save_stdout = sys.stdout
            save_stdin = sys.stdin
            save_displayhook = sys.displayhook
            
            try:
                sys.stdin = self.stdin
                sys.stdout = self.stdout
                sys.displayhook = self.displayhook
                exec(code, globals, locals)
                
                try:
                    sys.stdout = save_stdout
                    sys.stdin = save_stdin
                    sys.displayhook = save_displayhook
                    return None
                    sys.stdout = save_stdout
                    sys.stdin = save_stdin
                    sys.displayhook = save_displayhook
                    
                    try:
                        pass
                    except:
                        self._error_exc()
                        return None





    
    def precmd(self, line):
        """Handle alias expansion and ';;' separator."""
        if not line.strip():
            return line
        args = None.split()
    # WARNING: Decompyle incomplete

    
    def onecmd(self, line):
        '''Interpret the argument as though it had been typed in response
        to the prompt.

        Checks whether this line is typed at the normal prompt or in
        a breakpoint command list definition.
        '''
        if not self.commands_defining:
            return cmd.Cmd.onecmd(self, line)
        return None.handle_command_def(line)

    
    def handle_command_def(self, line):
        '''Handles one command line during command list definition.'''
        (cmd, arg, line) = self.parseline(line)
        if not cmd:
            return None
        if None == 'silent':
            self.commands_silent[self.commands_bnum] = True
            return None
        if None == 'end':
            self.cmdqueue = []
            return 1
        cmdlist = None.commands[self.commands_bnum]
        if arg:
            cmdlist.append(cmd + ' ' + arg)
        else:
            cmdlist.append(cmd)
        
        try:
            func = getattr(self, 'do_' + cmd)
        except AttributeError:
            func = self.default

        if func.__name__ in self.commands_resuming:
            self.commands_doprompt[self.commands_bnum] = False
            self.cmdqueue = []
            return 1

    
    def message(self, msg):
        print(msg, file = self.stdout)

    
    def error(self, msg):
        print('***', msg, file = self.stdout)

    
    def _complete_location(self, text, line, begidx, endidx):
        if line.strip().endswith((':', ',')):
            return []
        
        try:
            ret = self._complete_expression(text, line, begidx, endidx)
        except Exception:
            ret = []

        globs = glob.glob(glob.escape(text) + '*')
        for fn in globs:
            if os.path.isdir(fn):
                ret.append(fn + '/')
                continue
            if os.path.isfile(fn) and fn.lower().endswith(('.py', '.pyw')):
                ret.append(fn + ':')
            return ret

    
    def _complete_bpnumber(self, text, line, begidx, endidx):
        pass
    # WARNING: Decompyle incomplete

    
    def _complete_expression(self, text, line, begidx, endidx):
        pass
    # WARNING: Decompyle incomplete

    
    def do_commands(self, arg):
        """commands [bpnumber]
        (com) ...
        (com) end
        (Pdb)

        Specify a list of commands for breakpoint number bpnumber.
        The commands themselves are entered on the following lines.
        Type a line containing just 'end' to terminate the commands.
        The commands are executed when the breakpoint is hit.

        To remove all commands from a breakpoint, type commands and
        follow it immediately with end; that is, give no commands.

        With no bpnumber argument, commands refers to the last
        breakpoint set.

        You can use breakpoint commands to start your program up
        again.  Simply use the continue command, or step, or any other
        command that resumes execution.

        Specifying any command resuming execution (currently continue,
        step, next, return, jump, quit and their abbreviations)
        terminates the command list (as if that command was
        immediately followed by end).  This is because any time you
        resume execution (even with a simple next or step), you may
        encounter another breakpoint -- which could have its own
        command list, leading to ambiguities about which list to
        execute.

        If you use the 'silent' command in the command list, the usual
        message about stopping at a breakpoint is not printed.  This
        may be desirable for breakpoints that are to print a specific
        message and then continue.  If none of the other commands
        print anything, you will see no sign that the breakpoint was
        reached.
        """
        if not arg:
            bnum = len(bdb.Breakpoint.bpbynumber) - 1
        else:
            
            try:
                bnum = int(arg)
            except:
                self.error('Usage: commands [bnum]\n        ...\n        end')
                return None

            
            try:
                self.get_bpbynumber(bnum)
            except ValueError:
                err = None
                self.error('cannot set commands: %s' % err)
                err = None
                del err
                return None
                err = None
                del err

            self.commands_bnum = bnum
            if bnum in self.commands:
                old_command_defs = (self.commands[bnum], self.commands_doprompt[bnum], self.commands_silent[bnum])
            else:
                old_command_defs = None
        self.commands[bnum] = []
        self.commands_doprompt[bnum] = True
        self.commands_silent[bnum] = False
        prompt_back = self.prompt
        self.prompt = '(com) '
        self.commands_defining = True
        
        try:
            self.cmdloop()
            
            try:
                pass
            except KeyboardInterrupt:
                if old_command_defs:
                    self.commands[bnum] = old_command_defs[0]
                    self.commands_doprompt[bnum] = old_command_defs[1]
                    self.commands_silent[bnum] = old_command_defs[2]
                else:
                    del self.commands[bnum]
                    del self.commands_doprompt[bnum]
                    del self.commands_silent[bnum]
                self.error('command definition aborted, old commands restored')
                
                try:
                    pass
                try:
                    self.commands_defining = False
                    self.prompt = prompt_back
                    return None
                except:
                    self.commands_defining = False
                    self.prompt = prompt_back




    complete_commands = _complete_bpnumber
    
    def do_break(self, arg, temporary = (0,)):
        """b(reak) [ ([filename:]lineno | function) [, condition] ]
        Without argument, list all breaks.

        With a line number argument, set a break at this line in the
        current file.  With a function name, set a break at the first
        executable line of that function.  If a second argument is
        present, it is a string specifying an expression which must
        evaluate to true before the breakpoint is honored.

        The line number may be prefixed with a filename and a colon,
        to specify a breakpoint in another file (probably one that
        hasn't been loaded yet).  The file is searched for on
        sys.path; the .py suffix may be omitted.
        """
        if not arg:
            if self.breaks:
                self.message('Num Type         Disp Enb   Where')
                for bp in bdb.Breakpoint.bpbynumber:
                    if bp:
                        self.message(bp.bpformat())
                    return None
                    filename = None
                    lineno = None
                    cond = None
                    comma = arg.find(',')
                    if comma > 0:
                        cond = arg[comma + 1:].lstrip()
                        arg = arg[:comma].rstrip()
        colon = arg.rfind(':')
        funcname = None
        if not filename:
            filename = self.defaultFile()
        line = self.checkline(filename, lineno)
        if line:
            err = self.set_break(filename, line, temporary, cond, funcname)
            if err:
                self.error(err)
                return None
            bp = None if colon >= 0 else None.get_breaks(filename, line)[-1]
            self.message('Breakpoint %d at %s:%d' % (bp.number, bp.file, bp.line))
            return None
        return None if colon >= 0 else None

    
    def defaultFile(self):
        '''Produce a reasonable default.'''
        filename = self.curframe.f_code.co_filename
        if filename == '<string>' and self.mainpyfile:
            filename = self.mainpyfile
        return filename

    do_b = do_break
    complete_break = _complete_location
    complete_b = _complete_location
    
    def do_tbreak(self, arg):
        '''tbreak [ ([filename:]lineno | function) [, condition] ]
        Same arguments as break, but sets a temporary breakpoint: it
        is automatically deleted when first hit.
        '''
        self.do_break(arg, 1)

    complete_tbreak = _complete_location
    
    def lineinfo(self, identifier):
