from easygoogletranslate import EasyGoogleTranslate
from langid.langid import LanguageIdentifier, model
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


translator = EasyGoogleTranslate()

lang_identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)


def detect_language(text):
    lang, _ = lang_identifier.classify(text)
    return lang


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/translate", methods=["POST"])
def translate():
    user_input = request.form['user_input']
    target_language = request.form['target_language']
    translated_text = translator.translate(
        user_input, target_language=target_language)
    return jsonify({"result": translated_text})


if __name__ == "__main__":
    app.run(debug=True)