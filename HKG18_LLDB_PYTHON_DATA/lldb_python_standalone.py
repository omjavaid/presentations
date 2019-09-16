#!/usr/bin/python
# export PYTHONPATH=/home/omair/work/HKG18_LLDB_PYTHON/lldb-build/build/host/lib/python2.7/site-packages
# Creating a target for './app'
# SBBreakpoint: id = 1, name = 'main', module = app, locations = 1
# SBProcess: pid = 10439, state = stopped, threads = 1, executable = app
# thread #1: tid = 10439, 0x000000000040057f app`main at app.c:15, name = 'app', stop reason = breakpoint 1.1
# frame #0: 0x000000000040057f app`main at app.c:15
# SBFunction: id = 0xffffffff00000054, name = main, type = main
# app[0x400570]: pushq  %rbp
# app[0x400571]: movq   %rsp, %rbp
# app[0x400574]: subq   $0x10, %rsp
# app[0x400578]: movl   $0x0, -0x4(%rbp)
# app[0x40057f]: callq  0x400510
# app[0x400584]: callq  0x400540
# app[0x400589]: xorl   %eax, %eax
# app[0x40058b]: addq   $0x10, %rsp
# app[0x40058f]: popq   %rbp
# app[0x400590]: retq 

import lldb
import os

def disassemble_instructions(insts):
    for i in insts:
        print i

# Set the path to the executable to debug
exe = "./app"

# Create a new debugger instance
debugger = lldb.SBDebugger.Create()

# When we step or continue, don't return from the function until the process 
# stops. Otherwise we would have to handle the process events ourselves which, while doable is
#a little tricky.  We do this by setting the async mode to false.
debugger.SetAsync (False)

# Create a target from a file and arch
print "Creating a target for '%s'" % exe

target = debugger.CreateTargetWithFileAndArch (exe, "x86_64")

if target:
    # If the target is valid set a breakpoint at main
    main_bp = target.BreakpointCreateByName ("main", target.GetExecutable().GetFilename());

    print main_bp

    # Launch the process. Since we specified synchronous mode, we won't return
    # from this function until we hit the breakpoint at main
    process = target.LaunchSimple (None, None, os.getcwd())
    
    # Make sure the launch went ok
    if process:
        # Print some simple process info
        state = process.GetState ()
        print process
        if state == lldb.eStateStopped:
            # Get the first thread
            thread = process.GetThreadAtIndex (0)
            if thread:
                # Print some simple thread info
                print thread
                # Get the first frame
                frame = thread.GetFrameAtIndex (0)
                if frame:
                    # Print some simple frame info
                    print frame
                    function = frame.GetFunction()
                    # See if we have debug info (a function)
                    if function:
                        # We do have a function, print some info for the function
                        print function
                        # Now get all instructions for this function and print them
                        insts = function.GetInstructions(target)
                        disassemble_instructions (insts)
                    else:
                        # See if we have a symbol in the symbol table for where we stopped
                        symbol = frame.GetSymbol();
                        if symbol:
                            # We do have a symbol, print some info for the symbol
                            print symbol
