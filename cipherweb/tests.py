"""Tests for the Caesar Cipher web UI."""

from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    def test_home_page_loads(self) -> None:
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Caesar Cipher")

    def test_encrypt_submission_renders_result(self) -> None:
        response = self.client.post(
            reverse("home"),
            {
                "message": "Hello",
                "mode": "encrypt",
                "shift": 3,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Khoor")

    def test_decrypt_submission_renders_result(self) -> None:
        response = self.client.post(
            reverse("home"),
            {
                "message": "Khoor",
                "mode": "decrypt",
                "shift": 3,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello")

    def test_bruteforce_submission_renders_all_candidates(self) -> None:
        response = self.client.post(
            reverse("home"),
            {
                "message": "Khoor",
                "mode": "bruteforce",
                "shift": "",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Shift 3")
        self.assertContains(response, "Hello")
