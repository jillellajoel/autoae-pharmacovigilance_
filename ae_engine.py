import spacy
import os

# Function to load the custom NER model
def get_spacy_model():
    # Load the trained AE detection model from the models directory
    return spacy.load(os.path.join("models", "ae_custom_model"))

# Function to extract Adverse Events using the loaded model
def extract_adverse_events(text):
    nlp = get_spacy_model()
    doc = nlp(text)

    # Extract named entities labeled as AE (Adverse Event)
    adverse_events = [ent.text for ent in doc.ents if ent.label_ == "AE"]

    return adverse_events
