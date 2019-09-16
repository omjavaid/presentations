# This is test.py

import lldb

def test(debugger, command, result, internal_dict):
    """ Just a test command to set a breakpoint """
    target = debugger.GetSelectedTarget()
    breakpoint = target.BreakpointCreateByName("fun1")

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f test.test test')
