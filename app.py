import gradio as gr
import spacy
import os

# Load your trained AE model
MODEL_PATH = "models/ae_custom_model"

try:
    nlp = spacy.load(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"❌ Failed to load model from {MODEL_PATH}. Error: {e}")

# Extract AEs from text
def extract_adverse_events(text):
    doc = nlp(text)
    ae_entities = [ent.text for ent in doc.ents if ent.label_ == "AE"]
    return "\n".join(sorted(set(ae_entities))) if ae_entities else "No Adverse Events detected."

# Gradio interface
demo = gr.Interface(
    fn=extract_adverse_events,
    inputs=gr.Textbox(lines=10, label="Paste Medical Narrative"),
    outputs=gr.Textbox(label="Detected Adverse Events"),
    title="🧠 AutoAE – Adverse Event Extractor",
    description="Custom NLP app to extract Adverse Events (AEs) from unstructured text using a spaCy model trained for pharmacovigilance.",
    theme="compact"
)

if __name__ == "__main__":
    demo.launch()
