#!/usr/bin/env python3
"""
Example: Basic usage of B.I.T.C.H. v3
"""
from bitch_engine import BITCHEngineV3

engine = BITCHEngineV3()

# Example 1: Simple code that works
print("=" * 60)
print("EXAMPLE 1: Code that ships immediately")
print("=" * 60)

result = engine.bitch_execute("hello_world", """
print("Hello from B.I.T.C.H.!")
""")
print(f"Shipped: {result['shipped']}")
print(f"Language: {result['final_substrate']}")
print(f"Output: {result['final_output']}")
print()

# Example 2: Undefined variable (BITCH will fix it)
print("=" * 60)
print("EXAMPLE 2: Undefined variable (auto-healed)")
print("=" * 60)

result = engine.bitch_execute("undefined_var", """
x = some_undefined_var
print(f"Found: {x}")
""")
print(f"Shipped: {result['shipped']}")
print(f"Language: {result['final_substrate']}")
print(f"Heals: {result['heals']}")
print(f"Output: {result['final_output']}")
print()

# Example 3: Syntax error (BITCH will fix it)
print("=" * 60)
print("EXAMPLE 3: Syntax error (auto-healed)")
print("=" * 60)

result = engine.bitch_execute("syntax_error", """
def greet(name)
    print(f"Hello, {name}!")
""")
print(f"Shipped: {result['shipped']}")
print(f"Language: {result['final_substrate']}")
print(f"Heals: {result['heals']}")
print(f"Output: {result['final_output']}")
print()

# Example 4: Missing import (BITCH will stub it)
print("=" * 60)
print("EXAMPLE 4: Missing import (stubbed)")
print("=" * 60)

result = engine.bitch_execute("missing_import", """
import numpy as np
arr = np.zeros(5)
print(f"Array: {arr}")
""")
print(f"Shipped: {result['shipped']}")
print(f"Language: {result['final_substrate']}")
print(f"Heals: {result['heals']}")
print(f"Output: {result['final_output']}")
print()

# Show stats
print("=" * 60)
print("ENGINE STATS")
print("=" * 60)
print(json.dumps(engine.stats(), indent=2))
