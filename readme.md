# Vitual Environment (01_basics) 

A virtual environment (venv) is like a separate box for a Python project.

Each project can have its own Python version

Each project can have its own libraries & versions

Prevents dependency conflicts

👉 Example problem without venv:
Project A needs Django 3.2
Project B needs Django 4.2
Both will clash if installed globally ❌

- `python -m venv .venv(name)`
- `.venv\Scripts\activate`

Under main folder You can create `requirements.txt`
- `pip install -r requirements.txt`
everything inside this will be installed.

# DataTypess

- (/) --> gives exact answer of division
- (//) --> without decimal but floor value
- power --> 2^3 is euivalent to 2 ** 3 in python
total_leaves = 1_000_000_000 a special feature of python, still it will be counted as without underscore

### Upcasting

```
is_boiling = True

stri_count = 5

total = is_boiling + stri_count # upcasting

print(total)
```

- for boolean 0 represents false
- for anything present represent as true

# Python Data Types: Mutable vs Immutable

| 🔓 Mutable Data Types | 🔒 Immutable Data Types |
|----------------------|------------------------|
| `list` | `int` |
| `dict` | `float` |
| `set` | `complex` |
| `bytearray` | `bool` |
| `memoryview` | `str` |
| `array` | `tuple` |
| `deque` | `frozenset` |
| `defaultdict` | `bytes` |
| `Counter` | `range` |
|  | `NoneType` |

---

### Example

#### Mutable
```python
lst = [1, 2, 3]
lst.append(4)
