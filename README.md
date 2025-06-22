[![🤗 View on Hugging Face](https://img.shields.io/badge/🤗%20Live%20App-HuggingFace-blue)](https://huggingface.co/spaces/jillellajoel/autoae-app)

# 🧠 AutoAE – Adverse Event Extractor for Pharmacovigilance

Created by **Joel Jillella**  
📄 [LinkedIn](https://www.linkedin.com/in/koushal-joel-jillella-b29689338)  
🧪 Pharmacovigilance Automation | Custom NER | NLP for Drug Safety

---

AutoAE is an AI-powered NLP tool that extracts Adverse Events (AEs) from unstructured medical case narratives using a custom-trained spaCy NER model. Built for drug safety workflows, this tool helps automate the detection of critical safety signals faster and more efficiently.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ FEATURES

✅ Custom-trained NER model for AE detection  
✅ Built with Streamlit for instant browser-based use  
✅ Clean UI for entering and analyzing free-text case narratives  
✅ Designed for pharmacovigilance professionals & researchers  
✅ Fully compatible with Hugging Face Spaces deployment  

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 PROJECT STRUCTURE

autoae-app/  
├── app.py                  → Main Streamlit app  
├── models/  
│   └── ae_custom_model/    → Your trained AE NER model  
├── requirements.txt        → App dependencies  
└── README.md               → This documentation file  

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💻 HOW TO RUN LOCALLY

🔹 Step 1: Clone this repository  
    git clone https://github.com/jillellajoel/autoae-pharmacovigilance_.git  
    cd autoae-pharmacovigilance_

🔹 Step 2: (Optional) Set up a virtual environment  
    python -m venv venv  
    source venv/bin/activate  
    (Windows: venv\Scripts\activate)

🔹 Step 3: Install dependencies  
    pip install -r requirements.txt

🔹 Step 4: Launch the app  
    streamlit run app.py

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 DEPLOY ON HUGGING FACE SPACES

1️⃣ Go to https://huggingface.co/spaces  
2️⃣ Click "Create new Space" and choose "Streamlit" as the SDK  
3️⃣ Upload these items:
    • app.py  
    • requirements.txt  
    • models/ae_custom_model/ (your trained NER model)

🎯 After upload, your app will launch automatically.

🔗 Demo (Coming Soon):  
    https://huggingface.co/spaces/jillellajoel/autoae-app

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 REQUIREMENTS

• Python 3.8+  
• spaCy  
• Streamlit  

📥 Optional spaCy model download:  
    python -m spacy download en_core_web_sm

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🛠️ TO-DO ROADMAP

☑ Improve model accuracy with more AE-labeled data  
☑ Add batch input for multi-narrative support  
☑ Enable CSV export for extracted AEs  
☑ Publicly deploy to Hugging Face Spaces  
☑ Add visual confidence score & structured AE output  

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👤 AUTHOR

📛 Kaushal Joel  
🎓 B. Pharm 
📧 jillellakaushal000@gmail.com  

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌟 SUPPORT THIS PROJECT

If you found this useful, give the repo a ⭐ on GitHub and share it with the PV and AI communities!
