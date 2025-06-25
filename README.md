# Pyspace-script

> A lightweight and modular namespace and context debugger for Python

**Pyspace-script** is a Python debugging tool that helps you explore local and global contexts, inspect object state, and understand execution flow — without modifying your production code.

## Features

- Print globals, locals, builtins
- Decorate any function with `@explore` for instant introspection
- Debug selected variables with `debug_context(only=[...])`
- Designed for learning, debugging, and optimizing Python code

## Installation

```bash
pip install git+https://github.com/Tryny8/pyspace-script.git
```

## Usage
```python
from debuglog import explore

@explore
def main():
    x = 42
    print("Doing something")
```

## 🔭 Roadmap & Features

See [FEATURES.md](./FEATURES.md) for upcoming features and development roadmap.