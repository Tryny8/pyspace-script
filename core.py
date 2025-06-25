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