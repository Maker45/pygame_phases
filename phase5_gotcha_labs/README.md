# Phase 5: The "Gotcha" Labs (PCEP Exam Prep)

**Lesson 5.1: PCEP Syntax & "Dry" Topics**

Pygame is great for logic (loops, lists, if-statements), but the PCEP exam also tests things games rarely use. These labs cover the "gotchas" — the trick questions the exam uses to see if you truly understand how Python reads code.

**No Pygame in this phase.** Every file is a plain Python script that prints to the VS Code terminal. Do **not** `import pygame`.

---

## 01_bitwise_gotchas.py

### Binary Basics

Humans count in Base-10 (0–9). Computers use Base-2 (0 and 1). Each 1 or 0 is a **bit**.

```
0000 0001 = 1
0000 0010 = 2
0000 0011 = 3
```

### Bitwise Operators (Math with Bits)

| Operator | Name | What it does |
|---|---|---|
| `<<` | Shift Left | Multiplies the number by 2 |
| `>>` | Shift Right | Divides the number by 2 (integer division) |
| `&` | AND | Compares the binary 1s and 0s |
| `\|` | OR | Compares the binary 1s and 0s |
| `^` | XOR | Compares the binary 1s and 0s |
| `~` | NOT | Flips the binary 1s and 0s |

**Practice:** Use `print()` to try each operator on small numbers and check the results.

---

## 02_slicing_gotchas.py

### String Slicing `[start : stop : step]`

- Strings are like lists of characters!
- **The trap:** The `stop` index is **exclusive** — it does not include that letter.
- Example: `text = "Hello World"` then `print(text[::-1])`

### String Quirks (Immutability)

- **Immutable:** Once a string is created, you cannot change its individual letters. To change it, build a brand new string.
- Use `+` to glue strings together (concatenation) and `*` to repeat them (`"A" * 3` is `"AAA"`).

**Practice:** Use `print()` to try different start, stop, and step values on a string.

---

## 03_casting_gotchas.py

### Type Casting (Constructors)

`"10"` is text. `10` is a number. They are **not** the same!

- `int()` turns text or floats into integers.
- `str()` turns numbers into text.
- `float()` turns integers or text into decimals.

**Practice:** Compare `int("10")` and `str(10)`. Use `print()` and `type()` to see what you get.

---

## 04_terminal_mini_test.py

### Lab Challenge: "Terminal Hacker" (The PCEP Mini-Test)

Open this blank Python file in VS Code (no Pygame imports). Solve these 4 challenges and **print** the answers:

1. What is the output of `8 >> 2`?
2. Create the variable `secret = "PCEP EXAM"`. Use slicing to print only `"EXAM"`.
3. Print the word `"BANANA"` backwards using slicing.
4. Fix this code so it prints `15` instead of `510`:
   ```python
   num1 = "5"
   num2 = "10"
   print(num1 + num2)
   ```
