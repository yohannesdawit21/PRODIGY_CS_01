document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("#cipher-form");
    const modeField = document.querySelector("#id_mode");
    const shiftField = document.querySelector("#id_shift");
    const shiftFieldWrapper = document.querySelector("#shift-field");
    const shiftHelp = document.querySelector("#shift-help");
    const runButton = document.querySelector("#run-button");
    const resultPanel = document.querySelector("#result-panel");

    if (!form || !modeField || !shiftField || !shiftFieldWrapper || !runButton || !resultPanel) {
        return;
    }

    const defaultButtonText = runButton.textContent;

    function syncShiftField() {
        const isBruteforce = modeField.value === "bruteforce";

        shiftFieldWrapper.classList.toggle("is-hidden", isBruteforce);
        shiftField.disabled = isBruteforce;

        if (shiftHelp) {
            shiftHelp.textContent = isBruteforce
                ? "Shift is not needed for brute-force mode."
                : "Required for encrypt and decrypt.";
        }
    }

    modeField.addEventListener("change", syncShiftField);

    form.addEventListener("submit", () => {
        runButton.disabled = true;
        runButton.textContent = "Running...";
        window.setTimeout(() => {
            runButton.disabled = false;
            runButton.textContent = defaultButtonText;
        }, 4000);
    });

    syncShiftField();

    if (resultPanel.dataset.hasSubmission === "true") {
        window.requestAnimationFrame(() => {
            resultPanel.scrollIntoView({ behavior: "smooth", block: "start" });
            resultPanel.focus();
        });
    }
});
