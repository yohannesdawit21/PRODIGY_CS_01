# Caesar Cipher

A Python Caesar cipher project with both a command-line interface and a simple Django web UI.

## What This Project Does

- Encrypts text with a Caesar shift.
- Decrypts text with a Caesar shift.
- Tries all 26 possible decryptions for quick cryptanalysis.
- Preserves uppercase/lowercase letters.
- Preserves spaces, punctuation, and numbers.
- Supports negative and large shifts with modulo 26 normalization.
- Includes a clean Django UI that reuses the same Python cipher logic.

## Host It Free On Render

This Django app is ready to deploy on Render's free tier.

1. Push this repository to GitHub.
2. Sign in to [Render](https://render.com/) and create a new `Blueprint`.
3. Select your GitHub repository.
4. Render will detect `render.yaml` and set up the web service automatically.
5. Wait for the first deploy to finish, then open the generated Render URL.

The deployment config already:

- installs dependencies from `requirements.txt`
- runs `collectstatic`
- runs `migrate`
- starts the app with `gunicorn`
- generates a `SECRET_KEY`
- sets `DEBUG=False`

If you deploy manually instead of using the blueprint flow, use:

- Build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
- Start command: `gunicorn ciphersite.wsgi:application`

## Install Dependencies

Prerequisite: Python 3.10+.

From the project root:

If you do not already have a virtual environment:

python3 -m venv .venv

Activate it:

source .venv/bin/activate

Then install dependencies:

pip install -r requirements.txt

If your Linux distribution blocks system-wide `pip` installs, always use the
virtual environment commands above or run:

.venv/bin/pip install -r requirements.txt

## Run The Django UI

Start the development server:

python manage.py runserver

Or, without activating the environment:

.venv/bin/python manage.py runserver

Then open:

http://127.0.0.1:8000/

## Run The Python CLI

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

To run the Django UI tests:

python manage.py test

Or, without activating the environment:

.venv/bin/python manage.py test

## Project Hygiene

- .gitignore excludes `.venv`, `__pycache__`, `.pyc`, and `db.sqlite3`.
- The Django UI imports and reuses the logic from `caesar_cipher.py` instead of duplicating the cipher behavior.
- `render.yaml` is included so the project can be deployed quickly on Render.
