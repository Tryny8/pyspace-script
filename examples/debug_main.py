import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from debuglog import explore, debug_context

@explore
def main():
    x = 10
    y = 20
    msg = "Coucou"
    debug_context(only=["x", "msg"])
    return x + y

if __name__ == "__main__":
    print("Résultat:", main())