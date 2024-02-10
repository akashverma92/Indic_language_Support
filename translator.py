from easygoogletranslate import EasyGoogleTranslate
from langid.langid import LanguageIdentifier, model


translator = EasyGoogleTranslate()

lang_identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)


def detect_language(text):
    lang, _ = lang_identifier.classify(text)
    return lang


user_input = input("Enter any indic language to translate : ")
translated_text = translator.translate(
    user_input, target_language="en")


print("Translated text : ", translated_text)