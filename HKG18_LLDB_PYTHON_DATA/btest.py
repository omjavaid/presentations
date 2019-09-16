# This is test.py
import lldb
def btest(debugger, command, result, internal_dict):
   """ Just a test command to set a breakpoint """
   target = debugger.GetSelectedTarget()
   main_bp = target.BreakpointCreateByName("main")
   func1_bp = target.BreakpointCreateByName("func1")
   func2_bp = target.BreakpointCreateByName("func2")

def __lldb_init_module(debugger, internal_dict):
   debugger.HandleCommand('command script add -f btest.btest btest')

