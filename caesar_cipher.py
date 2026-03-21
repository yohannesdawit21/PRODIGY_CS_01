"""Caesar Cipher CLI tool.

Supports encryption, decryption, and brute-force exploration.
"""

from __future__ import annotations

import argparse


def _shift_char(char: str, shift: int) -> str:
    """Shift a single alphabetic character by the given amount."""
    if not char.isalpha():
        return char

    # Normalize to [0, 25] so negative and large values work reliably.
    normalized_shift = shift % 26

    if char.isupper():
        base = ord("A")
    else:
        base = ord("a")

    offset = ord(char) - base
    shifted_offset = (offset + normalized_shift) % 26
    return chr(base + shifted_offset)


def encrypt(text: str, shift: int) -> str:
    """Return encrypted text using Caesar Cipher."""
    return "".join(_shift_char(char, shift) for char in text)


def decrypt(text: str, shift: int) -> str:
    """Return decrypted text using Caesar Cipher."""
    return "".join(_shift_char(char, -shift) for char in text)


def brute_force_decryptions(text: str) -> list[tuple[int, str]]:
    """Return all 26 possible decryptions with their shift values."""
    return [(shift, decrypt(text, shift)) for shift in range(26)]


def _read_message(prompt: str = "Enter your message: ") -> str:
    """Read message from user."""
    return input(prompt)


def _read_shift() -> int:
    """Read and validate integer shift value from user."""
    while True:
        raw_value = input("Enter shift value (integer): ").strip()
        try:
            return int(raw_value)
        except ValueError:
            print("Invalid shift value. Please enter a valid integer.")


def _read_mode() -> str:
    """Read and validate operation mode from user."""
    while True:
        print("\nChoose an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Brute-force decrypt (try all shifts)")
        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == "1":
            return "encrypt"
        if choice == "2":
            return "decrypt"
        if choice == "3":
            return "bruteforce"

        print("Invalid choice. Please enter 1, 2, or 3.")


def _parse_shift(value: str) -> int:
    """argparse type parser for shift with clean error reporting."""
    try:
        return int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            f"Invalid shift '{value}'. Shift must be an integer."
        ) from exc


def _build_parser() -> argparse.ArgumentParser:
    """Create command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Encrypt/decrypt text with a Caesar cipher.",
    )
    parser.add_argument(
        "text",
        nargs="?",
        help="Message text to process. If omitted with --interactive, you will be prompted.",
    )
    parser.add_argument(
        "-m",
        "--mode",
        choices=["encrypt", "decrypt", "bruteforce"],
        help="Operation mode.",
    )
    parser.add_argument(
        "-s",
        "--shift",
        type=_parse_shift,
        help="Shift value for encrypt/decrypt (integer, supports negatives and large values).",
    )
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Run in interactive mode.",
    )
    return parser


def _run_interactive() -> None:
    """Run interactive CLI flow."""
    print("=== Caesar Cipher Program (Interactive) ===")
    message = _read_message()
    mode = _read_mode()

    if mode == "bruteforce":
        print("\nAll possible decryptions:")
        for shift, candidate in brute_force_decryptions(message):
            print(f"Shift {shift:2d}: {candidate}")
        return

    shift = _read_shift()
    if mode == "encrypt":
        result = encrypt(message, shift)
        print(f"\nEncrypted text: {result}")
    else:
        result = decrypt(message, shift)
        print(f"\nDecrypted text: {result}")


def _run_non_interactive(
    args: argparse.Namespace, parser: argparse.ArgumentParser
) -> None:
    """Run non-interactive CLI flow using parsed args."""
    if not args.mode:
        parser.error("--mode is required unless --interactive is used.")

    if args.text is None:
        parser.error("text is required unless --interactive is used.")

    if args.mode == "bruteforce":
        print("All possible decryptions:")
        for shift, candidate in brute_force_decryptions(args.text):
            print(f"Shift {shift:2d}: {candidate}")
        return

    if args.shift is None:
        parser.error("--shift is required for encrypt/decrypt modes.")

    if args.mode == "encrypt":
        print(encrypt(args.text, args.shift))
    else:
        print(decrypt(args.text, args.shift))


def main() -> None:
    """Run Caesar Cipher command-line interface."""
    parser = _build_parser()
    args = parser.parse_args()

    if args.interactive:
        _run_interactive()
        return

    _run_non_interactive(args, parser)


if __name__ == "__main__":
    main()
