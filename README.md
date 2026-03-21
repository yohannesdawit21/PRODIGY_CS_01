# Caesar Cipher

A Python command-line tool for Caesar cipher encryption, decryption, and brute-force decoding.

## What This Project Does

- Encrypts text with a Caesar shift.
- Decrypts text with a Caesar shift.
- Tries all 26 possible decryptions for quick cryptanalysis.
- Preserves uppercase/lowercase letters.
- Preserves spaces, punctuation, and numbers.
- Supports negative and large shifts with modulo 26 normalization.

## How To Run

Prerequisite: Python 3.10+.

From the project root:

python caesar_cipher.py -h

### Encrypt

python caesar_cipher.py -m encrypt -s 3 "Hello, World!"

Output:

Khoor, Zruog!

### Decrypt

python caesar_cipher.py -m decrypt -s 3 "Khoor, Zruog!"

Output:

Hello, World!

### Brute-force Decrypt (All 26 Shifts)

python caesar_cipher.py -m bruteforce "Khoor, Zruog!"

Output (excerpt):

Shift  0: Khoor, Zruog!
Shift  1: Jgnnq, Yqtnf!
Shift  2: Ifmmp, Xpsme!
Shift  3: Hello, World!
...

### Optional Interactive Mode

python caesar_cipher.py --interactive

The interactive mode prompts for message, operation mode, and shift value when needed.

## Caesar Shift Logic (Short Explanation)

Each alphabetic character is mapped to a number from 0 to 25, shifted by the given value, and wrapped around using modulo 26:

new_index = (old_index + shift) % 26

For decryption, the same operation is applied with the negative shift.

## Testing

Run tests with:

python -m unittest discover -s tests -v

## Project Hygiene

- .gitignore excludes .venv, __pycache__, and .pyc files.
- requirements.txt is intentionally omitted because this project uses only the Python standard library.
