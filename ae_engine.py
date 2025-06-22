import spacy, os

def get_spacy_model():
    path = os.path.join("models", "en_core_web_sm")
    if os.path.exists(path):
        return spacy.load(path)
    return spacy.load("en_core_web_sm")

nlp = get_spacy_model()
