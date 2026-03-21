import unittest

from caesar_cipher import brute_force_decryptions, decrypt, encrypt


class CaesarCipherTests(unittest.TestCase):
    def test_encrypt_decrypt_roundtrip(self) -> None:
        original = "Attack at Dawn! 123"
        shift = 7
        encrypted = encrypt(original, shift)
        decrypted = decrypt(encrypted, shift)
        self.assertEqual(decrypted, original)

    def test_shift_zero_and_twenty_six(self) -> None:
        text = "Hello, World!"
        self.assertEqual(encrypt(text, 0), text)
        self.assertEqual(encrypt(text, 26), text)

    def test_negative_shift(self) -> None:
        self.assertEqual(encrypt("abc", -1), "zab")

    def test_large_shift(self) -> None:
        self.assertEqual(encrypt("abc", 52), "abc")
        self.assertEqual(encrypt("abc", 53), "bcd")

    def test_case_preservation(self) -> None:
        self.assertEqual(encrypt("AbCz", 2), "CdEb")

    def test_non_letters_are_preserved(self) -> None:
        text = "Meet me @ 9:00 PM."
        encrypted = encrypt(text, 5)
        self.assertIn("@ 9:00 ", encrypted)
        self.assertTrue(encrypted.endswith("."))

    def test_bruteforce_returns_26_candidates(self) -> None:
        candidates = brute_force_decryptions("khoor")
        self.assertEqual(len(candidates), 26)
        self.assertEqual(candidates[3], (3, "hello"))


if __name__ == "__main__":
    unittest.main()
