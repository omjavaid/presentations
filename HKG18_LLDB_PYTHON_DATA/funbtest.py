# This is funbtest.py
import lldb
import smtplib
import time

def funbtest(debugger, command, result, internal_dict):
    """ Just a test command to set a breakpoint """
    target = debugger.GetSelectedTarget()

    main_bp = target.BreakpointCreateByName("main")
    main_bp.SetScriptCallbackFunction('funbtest.main_callback')

    func1_bp = target.BreakpointCreateByName("func1")
    func1_bp.SetScriptCallbackFunction('funbtest.func1_callback')

    func2_bp = target.BreakpointCreateByName("func2")
    func2_bp.SetScriptCallbackFunction('funbtest.func2_callback')

def main_callback(frame, bp_loc, dict):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("lldb.python@gmail.com", "lldb@hkg18")

    msg = "LLDB fun has begun !!!"
    server.sendmail("lldb.python@gmail.com", "omair.javaid@linaro.org", msg)
    server.quit()


def func1_callback(frame, bp_loc, dict):
    with open("fun.txt", "a") as myfile:
        msg = "LLDB fun reached its peak at: " + time.ctime() + "\n"
        myfile.write(msg)
        myfile.close

def func2_callback(frame, bp_loc, dict):
    print "LLDB fun is about to end !!!"


def __lldb_init_module(debugger, internal_dict):
   debugger.HandleCommand('command script add -f funbtest.funbtest funbtest')

