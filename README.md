# AutoAE – Adverse Event Extractor for Pharmacovigilance

AutoAE is an AI-powered NLP tool that extracts Adverse Events (AEs) from medical case narratives using a custom-trained spaCy NER model. Designed specifically for pharmacovigilance workflows, it helps automate and accelerate the identification of key safety signals.

------------------------------------------------------------

FEATURES

- Custom Named Entity Recognition (NER) model trained on AE-labeled data
- Interactive and lightweight web interface built with Streamlit
- Accepts free-text input for real-time AE extraction
- Built for pharmacovigilance professionals and case processors
- Ready for local or Hugging Face Spaces deployment

------------------------------------------------------------

PROJECT STRUCTURE

autoae-app/
├── app.py                  <- Main Streamlit interface
├── models/
│   └── ae_custom_model/    <- Custom trained spaCy AE model
├── requirements.txt        <- Dependencies file
└── README.md               <- Project documentation

------------------------------------------------------------

HOW TO RUN THE APP LOCALLY

Step 1: Clone the repository  
        git clone https://github.com/jillellajoel/autoae-pharmacovigilance_.git  
        cd autoae-pharmacovigilance_

Step 2: (Optional) Create a virtual environment  
        python -m venv venv  
        source venv/bin/activate  
        (On Windows: venv\Scripts\activate)

Step 3: Install dependencies  
        pip install -r requirements.txt

Step 4: Run the Streamlit app  
        streamlit run app.py

------------------------------------------------------------

DEPLOYMENT ON HUGGING FACE SPACES

To deploy this app on Hugging Face Spaces:

1. Go to huggingface.co/spaces
2. Click "Create new Space" and select "Streamlit" as SDK
3. Upload the following files:
   - app.py
   - requirements.txt
   - models/ae_custom_model/ folder

Once pushed, Hugging Face will automatically launch your app.

Live demo (coming soon):  
https://huggingface.co/spaces/jillellajoel/autoae-app

------------------------------------------------------------

REQUIREMENTS

- Python 3.8+
- streamlit
- spacy

If needed, run:  
python -m spacy download en_core_web_sm

------------------------------------------------------------

TO-DO ROADMAP

- Add export to CSV
- Add batch processing support
- Improve model with more AE-labeled data
- Deploy final version publicly
- Add UI enhancements (confidence score, structured output)

------------------------------------------------------------

AUTHOR

Kaushal Joel  
Final Year B. Pharmacy Student  
Email: jillellakaushal000@gmail.com

------------------------------------------------------------

SHOW YOUR SUPPORT

If you find this project useful, please give it a ⭐ on GitHub and share it with others in the PV and NLP community.
