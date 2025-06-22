import spacy
import os

def get_spacy_model():
    model_path = os.path.join("models", "en_core_web_sm")
    if os.path.exists(model_path):
        return spacy.load(model_path)
    else:
        return spacy.load("en_core_web_sm")

nlp = get_spacy_model()
