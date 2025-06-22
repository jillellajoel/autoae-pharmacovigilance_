import spacy
import pandas as pd
import os

# ✅ Load model from local folder
def get_spacy_model():
    try:
        return spacy.load("models/en_core_web_sm")
    except Exception as e:
        raise RuntimeError(f"Failed to load spaCy model: {e}")

nlp = get_spacy_model()
