"""Views for the Caesar Cipher web UI."""

from django.shortcuts import render

from caesar_cipher import brute_force_decryptions, decrypt, encrypt

from .forms import CaesarCipherForm


def home(request):
    """Render the single-page Caesar Cipher interface."""
    form = CaesarCipherForm(request.POST or None)
    context = {
        "form": form,
        "result_title": "Ready",
        "result_text": "Choose a mode, enter a message, and run the cipher.",
        "bruteforce_results": None,
        "has_submission": request.method == "POST",
    }

    if request.method == "POST" and form.is_valid():
        message = form.cleaned_data["message"]
        mode = form.cleaned_data["mode"]
        shift = form.cleaned_data.get("shift")

        if mode == "encrypt":
            context["result_title"] = "Encrypted Text"
            context["result_text"] = encrypt(message, shift)
        elif mode == "decrypt":
            context["result_title"] = "Decrypted Text"
            context["result_text"] = decrypt(message, shift)
        else:
            context["result_title"] = "All 26 Decryptions"
            context["result_text"] = None
            context["bruteforce_results"] = brute_force_decryptions(message)

    return render(request, "cipherweb/index.html", context)
