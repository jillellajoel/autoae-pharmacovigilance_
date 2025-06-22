def extract_adverse_events(text):
    nlp = get_spacy_model()
    doc = nlp(text)

    # Debug: Print all entities
    print("Detected entities:")
    for ent in doc.ents:
        print(f"{ent.text} → {ent.label_}")

    # Return structured output
    output = {
        "Adverse Events": [ent.text for ent in doc.ents if ent.label_ == "AE"],
        "Drugs": [ent.text for ent in doc.ents if ent.label_ == "DRUG"],
        "Seriousness": [ent.text for ent in doc.ents if ent.label_ == "SERIOUS"]
    }

    return output
