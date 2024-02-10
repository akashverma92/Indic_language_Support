function translateStuff() {
    var userInput = document.getElementById("userInput").value;
    var selectedLanguage = document.getElementById("languageSelect").value;

    fetch("/translate", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams({
                "user_input": userInput,
                "target_language": selectedLanguage
            })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("translationResult").innerText = "Translated to " + selectedLanguage + ": " + data.result;
        });
}

function translateFile() {
    var fileInput = document.getElementById("fileInput");
    var file = fileInput.files[0];

    if (file) {
        var formData = new FormData();
        formData.append("file", file);

        fetch("/translate-file", {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById("fileTranslationResult").innerText = "Translated File Content: " + data.result;
            });
    } else {
        alert("Please select a file.");
    }
}