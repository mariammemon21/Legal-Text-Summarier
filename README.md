# ⚖️ Legal Case Summarizer

A Streamlit-powered web app to **automatically extract and summarize legal case documents** (PDF, DOCX, TXT). This tool is ideal for lawyers, legal researchers, and law students who want to quickly grasp the essential elements of a case.

---

## 🚀 Features

- ✅ Upload legal documents in `.pdf`, `.docx`, or `.txt`
- 🧠 Extracts key sections:
  - Case title and court details
  - Involved parties and actors
  - Evidence and witnesses (if present)
  - Legal claims and suggestions
- 📄 View raw text and structured summary
- 📥 Download summary as PDF
- 💬 Based on NLP + custom logic tailored for Indian legal documents

---

## 🧰 Tech Stack

- [Streamlit](https://streamlit.io/) – UI
- [PyMuPDF](https://pymupdf.readthedocs.io/) – PDF text extraction
- [python-docx](https://python-docx.readthedocs.io/) – DOCX reader
- [transformers](https://huggingface.co/transformers/) – Summarization (fallback)
- [ReportLab](https://www.reportlab.com/) – PDF summary generation
- [Torch](https://pytorch.org/) – backend for summarization models

---

## 🛠 Installation

### ✅ Python 3.10+ recommended

```bash
# Clone this repository
git clone https://github.com/your-username/legal-case-summarizer.git
cd legal-case-summarizer

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
