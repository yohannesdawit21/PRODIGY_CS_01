"""Forms for the Caesar Cipher web UI."""

from django import forms


MODE_CHOICES = [
    ("encrypt", "Encrypt"),
    ("decrypt", "Decrypt"),
    ("bruteforce", "Brute-force"),
]


class CaesarCipherForm(forms.Form):
    """Collect message, mode, and shift for the cipher UI."""

    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(
            attrs={
                "rows": 6,
                "placeholder": "Type your message here...",
            }
        ),
    )
    mode = forms.ChoiceField(label="Mode", choices=MODE_CHOICES, initial="encrypt")
    shift = forms.IntegerField(
        label="Shift",
        initial=3,
        required=False,
        help_text="Required for encrypt and decrypt.",
    )

    def clean(self) -> dict[str, object]:
        """Require shift only when the selected mode needs it."""
        cleaned_data = super().clean()
        mode = cleaned_data.get("mode")
        shift = cleaned_data.get("shift")

        if mode in {"encrypt", "decrypt"} and shift is None:
            self.add_error("shift", "Shift is required for encrypt and decrypt.")

        return cleaned_data
