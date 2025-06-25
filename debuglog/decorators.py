import inspect

def explore(func):
    def wrapper(*args, **kwargs):
        print(f"🌀 [@explore] Entering {func.__name__}")
        
        frame = inspect.currentframe().f_back
        print("🔍 LOCALS (before call):")
        for k, v in frame.f_locals.items():
            print(f"  {k:20}: {type(v).__name__} = {v}")

        result = func(*args, **kwargs)

        print("🌀 [@explore] Exiting", func.__name__)
        return result
    return wrapper