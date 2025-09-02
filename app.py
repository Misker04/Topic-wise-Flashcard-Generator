from flask import Flask, request, render_template, redirect
from werkzeug.utils import secure_filename
import os
from io import BytesIO

from text_extraction import extract_text_from_pdf, extract_text_from_txt
from topic_segmentation import segment_into_chunks, cluster_chunks
from summarization import generate_summary
from question_generation import generate_questions

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    flashcards = []
    error = ""
    
    if request.method == 'POST':
        text = ""
        uploaded_file = request.files.get('file')
        raw_text = request.form.get('raw_text', '')

        try:
            # 1. Handle uploaded file or pasted text
            if uploaded_file and uploaded_file.filename:
                filename = secure_filename(uploaded_file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                uploaded_file.save(file_path)
                with open(file_path, "rb") as f:
                    if filename.endswith(".pdf"):
                        text = extract_text_from_pdf(BytesIO(f.read()))
                    elif filename.endswith(".txt"):
                        text = extract_text_from_txt(BytesIO(f.read()))
            elif raw_text.strip():
                text = raw_text.strip()

            # 2. Process the extracted or entered text
            if text:
                chunks = segment_into_chunks(text)
                topic_map = cluster_chunks(chunks)

                for topic_idx, topic_chunks in topic_map.items():
                    topic_text = " ".join(topic_chunks).strip()
                    
                    if len(topic_text.split()) < 5:
                        flashcards.append((f"Topic {topic_idx+1}", [("Skipped", "Not enough content for summarization.")]))
                        continue
                    
                    try:
                        summary = generate_summary(topic_text)
                        if summary.strip():
                            try:
                                qa_pairs = generate_questions(summary)
                                flashcards.append((f"Topic {topic_idx+1}", qa_pairs))
                            except Exception as qe:
                                flashcards.append((f"Topic {topic_idx+1}", [("QG Error", f"Question generation failed: {qe}")]))
                        else:
                            flashcards.append((f"Topic {topic_idx+1}", [("Summary Error", "Summary was empty.")]))
                    except Exception as se:
                        flashcards.append((f"Topic {topic_idx+1}", [("Summary Error", f"Summarization failed: {se}")]))
            else:
                error = "No input text provided."

        except Exception as e:
            error = f"Unexpected error: {e}"

    return render_template('index.html', flashcards=flashcards, error=error)

if __name__ == '__main__':
    app.run(debug=True)
