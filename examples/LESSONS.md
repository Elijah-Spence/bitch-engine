# B.I.T.C.H. Lessons — What the Engine Teaches

## Lesson 1: Undefined Variables

**Broken:**
```python
print(name)
```

**BITCH sees:** `NameError: name 'name' is not defined`

**BITCH does:** Analyzes the variable name, guesses it's a string (because `name`), defines it:
```python
name = ""
print(name)
```

**Result:** Ships. Output: `""`

---

## Lesson 2: Missing Imports

**Broken:**
```python
import numpy as np
arr = np.zeros(5)
print(arr)
```

**BITCH sees:** `ModuleNotFoundError: No module named 'numpy'`

**BITCH does:** Stubs numpy with a fake class:
```python
class np:
    @staticmethod
    def zeros(n): return [0]*n if isinstance(n, int) else [[0]*n[1] for _ in range(n[0])]
arr = np.zeros(5)
print(arr)
```

**Result:** Ships. Output: `[0, 0, 0, 0, 0]`

---

## Lesson 3: Syntax Errors

**Broken:**
```python
def greet(name)
    print(f"Hello, {name}!")
```

**BITCH sees:** `SyntaxError: expected ':'`

**BITCH does:** Adds the missing colon:
```python
def greet(name):
    print(f"Hello, {name}!")
```

**Result:** Ships.

---

## Lesson 4: Type Errors

**Broken:**
```python
x = "hello" + 42
print(x)
```

**BITCH sees:** `TypeError: can only concatenate str (not "int") to str`

**BITCH does:** Wraps the int in `str()`:
```python
x = "hello" + str(42)
print(x)
```

**Result:** Ships. Output: `hello42`

---

## Lesson 5: Language Pivoting

**Broken (unfixable in Python):**
```python
import some_c_library
some_c_library.do_thing()
```

**BITCH sees:** Import error, stub doesn't help

**BITCH does:** Transpiles to JavaScript:
```javascript
console.log("stubbed missing module: some_c_library");
```

**Result:** Ships on JavaScript.

---

## Lesson 6: Deep Recursion

**Broken:**
```python
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
print(fib(5000))
```

**BITCH sees:** `RecursionError: maximum recursion depth exceeded`

**BITCH does:** Can't heal recursion. Pivots to a language with tail call optimization, or ships with reduced input.

---

## Lesson 7: Permission Errors

**Broken:**
```python
open("/etc/shadow").read()
```

**BITCH sees:** `PermissionError: [Errno 13] Permission denied`

**BITCH does:** Can't heal permissions. Returns error. Some things are impossible.

---

## Lesson 8: The Substrate Bug (The One That Almost Killed Us)

**The Bug:** Every interpreted language in `SUBSTRATE_CHAIN` was missing the file path in its `cmd` definition.

```python
# BROKEN — file never passed to interpreter
{"name": "python", "ext": ".py", "cmd": ["python3"], "timeout": 10}

# FIXED — file path included
{"name": "python", "ext": ".py", "cmd": ["python3", "_file.py"], "timeout": 10}
```

**What happened:** The engine wrote code to a temp file, then ran `python3` (interactive mode) without passing the file. Python exited immediately with code 0. Every test "shipped" with empty output.

**How we found it:** Tests kept returning `success=True, exit_code=0, output=""` for代码 that should have failed. Syntax errors, undefined variables, even segfaults all "shipped."

**The lesson:** Always verify your assumptions. The engine was lying to us because we never actually ran the code.

---

## The Philosophy

BITCH teaches us three things:

1. **Most code is fixable** — Undefined vars, missing imports, syntax errors are all mechanical fixes
2. **Some code needs translation** — When Python can't do it, another language might
3. **Some code is impossible** — Permission errors, infinite recursion, memory limits are physical constraints

The mesh decides what to eat. BITCH ships it. The slime never stops.
