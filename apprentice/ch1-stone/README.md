# Chapter 1: Secret Encoder

Your first real Python project — a simple message encoder using a Caesar cipher!

## What It Does

This program takes any message you type and shifts each letter forward by 3 positions in the alphabet. For example:

- `"hello"` becomes `"khoor"`
- `"ABC"` becomes `"DEF"`

Spaces and punctuation are preserved as-is.

## How to Run

```bash
python encoder.py
```

You'll be prompted to enter a message, and the program will output your encoded secret.

## Concepts Covered

- **Functions** — `def encode_message(message):` creates a reusable block of code
- **Loops** — `for letter in message:` iterates through each character
- **Conditionals** — `if letter.isalpha():` checks if a character is a letter
- **String methods** — `.isalpha()` for checking letter status
- **Built-in functions** — `ord()` converts a character to its ASCII code, `chr()` converts it back
- **User input** — `input()` prompts and captures user text

## Note

This is a basic implementation. Letters near the end of the alphabet (X, Y, Z) will shift to non-letter characters since the code doesn't wrap around. A full Caesar cipher would handle wrapping (e.g., Z → C).
