# Python Behind the Scenes — Interview Notes

## How Python Runs

Python source code is not executed directly by the CPU.

A simplified CPython execution flow is:

```text
.py Source Code
      ↓
Lexing / Parsing
      ↓
AST (Abstract Syntax Tree)
      ↓
Compilation
      ↓
Python Bytecode
      ↓
CPython Runtime / Virtual Machine
      ↓
Operating System
      ↓
CPU
```

### 1. Source Code

You write code such as:

```python
x = 10
print(x)
```

The CPU does not understand Python syntax.

### 2. Parsing

Python checks the source code's syntax and builds an internal representation, including an **AST**.

### 3. Bytecode

The code is compiled into **Python bytecode**.

Bytecode is an intermediate representation. It is **not CPU machine code**.

Cached bytecode can appear in:

```text
__pycache__/
```

as `.pyc` files.

### 4. Runtime Execution

The CPython runtime executes the bytecode and handles:

- Objects and types
- Function calls
- Variables and namespaces
- Exceptions
- Memory management
- Interaction with the operating system

### 5. Variables and Objects

Python variables are best understood as **names bound to objects**.

```python
x = 10
y = x
```

Conceptually:

```text
x ─────┐
       ├──→ Integer object: 10
y ─────┘
```

### 6. Memory Management

CPython primarily uses **reference counting** and also has a **cyclic garbage collector**.

This allows Python to automatically manage most memory instead of requiring manual allocation and deallocation.

## Key Mental Model

```text
You write Python
      ↓
Python parses it
      ↓
Python compiles it to bytecode
      ↓
CPython runtime executes bytecode
      ↓
OS provides system services
      ↓
CPU executes low-level instructions
```

---

# Important Interview Questions & Answers

## 1. Is Python compiled or interpreted?

**Answer: Both, depending on what you mean.**

In CPython, source code is first **compiled into bytecode**, and that bytecode is then executed by the Python runtime/virtual machine.

So saying simply "Python is interpreted" is an oversimplification.

---

## 2. What is Python bytecode?

**Answer:**

Python bytecode is an intermediate representation of Python code produced by the compiler. The Python runtime executes this bytecode.

It is different from native machine code because it is designed for the Python runtime rather than directly for a CPU.

---

## 3. Does the CPU execute Python code directly?

**Answer: No.**

The CPU does not directly understand Python syntax. The Python implementation processes the code, executes its bytecode, and ultimately relies on native instructions and operating-system services.

---

## 4. What happens when `x = 10` executes?

**Answer:**

Python creates or obtains an integer object representing `10` and binds the name `x` to that object.

```text
x ──→ 10
```

Python variables are therefore better understood as **names/references to objects**, rather than fixed memory boxes.

---

## 5. How does Python manage memory?

**Answer:**

In CPython, memory management primarily uses **reference counting**. When objects are no longer referenced, their memory can be reclaimed. CPython also has a cyclic garbage collector to detect reference cycles that reference counting alone cannot reclaim.

---

## 6. What is the difference between bytecode and machine code?

**Answer:**

- **Bytecode:** instructions for the Python runtime.
- **Machine code:** CPU-specific instructions executed natively by a processor.

Bytecode provides an intermediate layer between Python source code and low-level execution.

---

## 7. What is `__pycache__`?

**Answer:**

`__pycache__` is commonly used by Python to store cached compiled bytecode (`.pyc` files) for modules. This can avoid repeating some compilation work when modules are imported again.

---

## 8. Explain the complete execution flow of a Python program.

**Answer:**

A strong interview answer is:

> "In CPython, Python source code is parsed and compiled into bytecode. The CPython runtime executes that bytecode, manages Python objects, memory, function calls and exceptions, and uses the operating system for system-level operations. Eventually, the underlying native instructions are executed by the CPU."

