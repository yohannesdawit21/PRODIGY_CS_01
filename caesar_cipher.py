"""Caesar Cipher CLI tool.

Supports encryption and decryption with case preservation,
non-alphabetic pass-through, and robust shift handling.
"""


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


def _read_message() -> str:
    """Read message from user."""
    return input("Enter your message: ")


def _read_shift() -> int:
    """Read and validate integer shift value from user."""
    while True:
        raw_value = input("Enter shift value (integer): ").strip()
        try:
            return int(raw_value)
        except ValueError:
            print("Invalid shift value. Please enter a valid integer.")


def _read_choice() -> str:
    """Read and validate operation choice from user."""
    while True:
        print("\nChoose an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice in {"1", "2"}:
            return choice

        print("Invalid choice. Please enter 1 or 2.")


def main() -> None:
    """Run Caesar Cipher command-line interface."""
    print("=== Caesar Cipher Program ===")

    message = _read_message()
    shift = _read_shift()
    choice = _read_choice()

    if choice == "1":
        result = encrypt(message, shift)
        print(f"\nEncrypted text: {result}")
    else:
        result = decrypt(message, shift)
        print(f"\nDecrypted text: {result}")


if __name__ == "__main__":
    main()
