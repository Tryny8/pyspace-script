import builtins
import inspect

def explore_namespaces():
    print("\n🔍 GLOBALS:")
    for k, v in globals().items():
        print(f"  {k:20} => {type(v).__name__}")

    print("\n🔍 LOCALS (from caller):")
    current_locals = inspect.currentframe().f_back.f_locals
    for k, v in current_locals.items():
        print(f"  {k:20} => {type(v).__name__}")

    print("\n🔍 BUILTINS:")
    for name in dir(builtins):
        if not name.startswith("__"):
            print(f"  {name:20} => {type(getattr(builtins, name)).__name__}")

def debug_context(only=None):
    print("\n🧪 [debug_context]")

    frame = inspect.currentframe().f_back
    local_vars = frame.f_locals

    if only:
        for name in only:
            if name in local_vars:
                print(f"{name} = {repr(local_vars[name])}")
            else:
                print(f"{name} is not defined in local context.")
    else:
        for name, val in local_vars.items():
            print(f"{name} ({type(val).__name__}) = {repr(val)}")