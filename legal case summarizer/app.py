# 📄 app.py
import streamlit as st
import os
from utils.extractor import extract_text
from utils.summarizer import generate_summary
from io import BytesIO
from reportlab.pdfgen import canvas

st.set_page_config(page_title="⚖️ Legal Case Summarizer")
st.title("⚖️ Legal Case Summarizer")
st.write("Upload a legal case file (PDF, DOCX, or TXT) to generate a structured summary.")

# Create folders
os.makedirs("uploads", exist_ok=True)

uploaded_file = st.file_uploader("Upload Legal Document", type=["pdf", "docx", "txt"])

if uploaded_file:
    file_path = f"uploads/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ File uploaded. Extracting...")

    # Extract text
    raw_text = extract_text(file_path)
    st.text_area("📄 Extracted Raw Text", raw_text[:2000], height=300)

    if raw_text.strip():
        summary = generate_summary(raw_text)
        st.subheader("📄 Legal Summary")
        st.text_area("Generated Summary", summary, height=400)

        # Download as PDF
        if st.button("Download Summary as PDF"):
            buffer = BytesIO()
            c = canvas.Canvas(buffer)
            y = 800
            for line in summary.split('\n'):
                c.drawString(30, y, line[:120])
                y -= 15
                if y < 50:
                    c.showPage()
                    y = 800
            c.save()
            buffer.seek(0)
            st.download_button("Download PDF", buffer, file_name="legal_summary.pdf")
    else:
        st.error("❌ Could not extract any meaningful text from the uploaded document.")
