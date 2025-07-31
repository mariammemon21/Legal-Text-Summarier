import re
from transformers import pipeline

# Pegasus is powerful but can be fragile with malformed text
summarizer = pipeline("summarization", model="google/pegasus-xsum")

def split_text(text, max_tokens=512):
    sentences = text.split('. ')
    chunks = []
    current_chunk = ""
    current_length = 0

    for sentence in sentences:
        words = sentence.split()
        if current_length + len(words) <= max_tokens:
            current_chunk += sentence + ". "
            current_length += len(words)
        else:
            if current_chunk.strip():
                chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "
            current_length = len(words)

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks

def generate_summary(text):
    input_text = text.strip().replace("\n", " ")
    chunks = split_text(input_text)

    summaries = []
    for chunk in chunks:
        if not chunk.strip():
            continue
        try:
            result = summarizer(chunk, max_length=256, min_length=60, do_sample=False)
            summaries.append(result[0]['summary_text'])
        except Exception as e:
            summaries.append("[Summary failed for one part]")

    full_summary = "\n".join(summaries)

    # Extract case title and date using improved regex
    match = re.search(r"([\w\s]+)\s+v(?:s\.?|ersus)\s+([\w\s]+)\s+on\s+(\d{1,2}\s+\w+\s+\d{4})", text, re.IGNORECASE)
    if match:
        party_1, party_2, date = match.groups()
        parties = f"{party_1.strip()} vs {party_2.strip()}"
    else:
        parties, date = "Not Found", "Not Found"

    # Optional: you can add smarter parsing using SpaCy or pattern matching
    evidence = "\n".join(re.findall(r"(Exhibit\s+\w+.*?)\n", text, re.IGNORECASE)) or "Not explicitly mentioned"
    witnesses = "\n".join(re.findall(r"(Witness\s+\d+:.*?)\n", text, re.IGNORECASE)) or "Not explicitly mentioned"

    summary_output = f"""
🏷️ 1. Case Title and Court Details  
Date of Case: {date}

👤 2. Whose Case Is It?  
Parties: {parties}

⚖️ 3. Actors Involved  
(Mentioned in document summary)

👁️‍🔦 4. Witnesses  
{witnesses}

📌 5. Evidence  
{evidence}

🧾 6. Legal Claims  
(Summarized from input text)

🧠 7. Legal Suggestions (Next Steps)  
(Based on summarization)

📌 **Generated Summary**:
{full_summary}
"""
    return summary_output
