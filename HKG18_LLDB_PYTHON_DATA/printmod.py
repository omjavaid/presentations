import lldb
import shlex

def printmod(debugger, command, result, dict):
    target = debugger.GetSelectedTarget()

    process = target.GetProcess()

    thread = process.GetSelectedThread()

    frame = thread.GetSelectedFrame()

    count = int(frame.FindVariable("index").GetValueAsUnsigned()) -1
    indices = range(count)
    va = frame.FindVariable("m")
    for i in indices:
        var = va.GetChildAtIndex(i)
        print var.GetChildMemberWithName("name").GetSummary().strip('\"')

def __lldb_init_module(debugger, internal_dict):
   debugger.HandleCommand('command script add -f printmod.printmod printmod')
