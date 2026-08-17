# B.I.T.C.H. v3 — Never Fails

**"bitch until it ships."**

A self-healing, multi-language code execution engine that tries every language until your code works. 49 substrates. Auto-pivoting. Self-healing. Never gives up.

## What it does

1. **You give it code** (Python, JS, shell, whatever)
2. **It tries to run it**
3. **If it fails**, it classifies the error and heals the code
4. **If it still fails**, it translates to another language and tries again
5. **It NEVER gives up** until it ships or exhausts all 49 languages

## Quick Start

```python
from bitch_engine import BITCHEngineV3

engine = BITCHEngineV3()

# This code has an undefined variable — BITCH will fix it
result = engine.bitch_execute("my_task", """
print(undefined_variable_123)
""")

print(f"Shipped: {result['shipped']}")
print(f"Language: {result['final_substrate']}")
print(f"Output: {result['final_output']}")
```

## Languages

49 substrates across every paradigm:

| Category | Languages |
|----------|-----------|
| **Scripting** | Python, Ruby, Perl, Lua, PHP |
| **Web** | JavaScript, TypeScript, Clojure |
| **Systems** | C, C++, Rust, Go, Zig, V, Odin, Nim |
| **JVM** | Java, Kotlin, Scala, Groovy |
| **Functional** | Haskell, OCaml, F#, Scheme, Racket, Elixir, Erlang |
| **Academic** | R, Julia, Prolog, Ada, Pascal, Fortran, COBOL |
| **Shell** | Bash, PowerShell, AWK, Sed |
| **Esoteric** | Brainfuck, Forth |
| **Build** | Makefile, CMake |
| **Legacy** | Assembly, COBOL, Fortran |

## Self-Healing

BITCH automatically fixes common errors:

- **Undefined variables** → Defines them with smart defaults
- **Import errors** → Stubs missing modules (numpy, requests, datetime, etc.)
- **Syntax errors** → Adds missing colons, fixes indentation
- **Type errors** → Wraps in `str()` conversions

```python
# This code is broken — BITCH will fix it
result = engine.bitch_execute("broken", """
x = "hello" + 42  # TypeError
print(x)
""")
# BITCH wraps 42 in str() → ships on Python
```

## Error Classification

BITCH classifies errors into 10 categories:

- `recursion` — Maximum call stack exceeded
- `syntax` — SyntaxError, IndentationError
- `type_coercion` — TypeError, incompatible types
- `undefined` — NameError, ReferenceError
- `division_zero` — ZeroDivisionError
- `import` — ModuleNotFoundError, ImportError
- `permission` — PermissionError
- `timeout` — Execution timed out
- `memory` — MemoryError
- `unknown` — Unclassified errors

## CLI

```bash
# Run tests
python -m bitch_engine test

# Show language stats
python -m bitch_engine stats

# List all languages
python -m bitch_engine langs
```

## Configuration

```python
engine = BITCHEngineV3()
engine.MAX_RETRIES = 5    # Retries per language before pivoting
engine.MAX_PIVOTS = 3     # Max language pivots
```

## Optional Dependencies

```bash
# For faster execution via sandbox
pip install bitch-engine[polyglot]

# For code obfuscation
pip install bitch-engine[polymorphic]

# For better translations
pip install bitch-engine[universal]

# Everything
pip install bitch-engine[all]
```

## How it works

```
┌─────────────────────────────────────────────────────────────┐
│                    B.I.T.C.H. v3                            │
├─────────────────────────────────────────────────────────────┤
│  INPUT: Python code                                         │
│    │                                                        │
│    ▼                                                        │
│  ┌──────────────────────────────────────────┐              │
│  │ 1. EXECUTE in Python                     │              │
│  │    ├─ SUCCESS → SHIP IT                  │              │
│  │    └─ FAIL → CLASSIFY ERROR              │              │
│  └──────────────────────────────────────────┘              │
│    │                                                        │
│    ▼                                                        │
│  ┌──────────────────────────────────────────┐              │
│  │ 2. HEAL (if Python)                      │              │
│  │    ├─ Undefined var → Define it          │              │
│  │    ├─ Import error → Stub module         │              │
│  │    ├─ Syntax error → Fix code            │              │
│  │    └─ Type error → Add conversions       │              │
│  └──────────────────────────────────────────┘              │
│    │                                                        │
│    ▼                                                        │
│  ┌──────────────────────────────────────────┐              │
│  │ 3. PIVOT to next language                │              │
│  │    ├─ Translate Python → JavaScript      │              │
│  │    ├─ Translate Python → Shell           │              │
│  │    └─ Try 49 languages total             │              │
│  └──────────────────────────────────────────┘              │
│    │                                                        │
│    ▼                                                        │
│  OUTPUT: {shipped: true, substrate: "python", ...}         │
└─────────────────────────────────────────────────────────────┘
```

## License

MIT — go break things.

## Credits

Built by VINCULA / GARY. "The slime never stops."
