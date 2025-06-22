# 🧠 AutoAE – Adverse Event Extractor for Pharmacovigilance

AutoAE is an AI-powered NLP tool that extracts **Adverse Events (AEs)** from medical case narratives using a custom-trained spaCy NER model. Designed specifically for pharmacovigilance workflows, it helps automate and accelerate the identification of key safety signals.

---

## 🚀 Features

- 🧠 Custom Named Entity Recognition (NER) model trained on AE-labeled data  
- ⚡️ Interactive and lightweight web interface built with Streamlit  
- 📂 Accepts free-text input for real-time AE extraction  
- 🧪 Built for pharmacovigilance professionals and case processors  
- 🌐 Ready for local or Hugging Face Spaces deployment  

---

## 🗂 Project Structure

autoae-app/
├── app.py ← Main Streamlit interface
├── models/
│ └── ae_custom_model/ ← Custom trained spaCy AE model
├── requirements.txt ← Dependencies file
└── README.md ← Project documentation


---

## 💻 How to Run the App Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/jillellajoel/autoae-pharmacovigilance_.git
   cd autoae-pharmacovigilance_
   
2. Create a virtual environment (optional but recommended)
     python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

3. Install the required packages
  pip install -r requirements.txt

4. Launch the app
    streamlit run app.py


   🌐 Deployment
This app is designed for deployment on Hugging Face Spaces using the Streamlit SDK. Just upload this project folder to a new Space and it will auto-run.

Demo coming soon: huggingface.co/spaces/jillellajoel/autoae-app

📦 Requirements
Python 3.8+

spaCy

Streamlit

✅ To-Do (Roadmap)
 Add export option for AE output

 Batch input for multi-case AE extraction

 Model training UI for uploading new AE-labeled datasets

 Public Hugging Face Space deployment

🙋‍♂️ Author
Kaushal Joel
📧 jillellakaushal000@gmail.com
🎓 B. Pharm | Passionate about Pharmacovigilance + NLP

⭐️ Show your support
If you found this useful, consider giving the repo a ⭐ on GitHub!

---





