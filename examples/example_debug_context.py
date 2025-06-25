import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pyspacelog.core import debug_context

def main_test():
    print("[Lancememt programme]")
    x = 42
    msg = "hello"
    print(x, msg)
    debug_context(only=["x", "msg", "not_set"])

if __name__ == "__main__":
    main_test()