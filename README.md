# Topic-wise Flashcard Generator

Transform long academic text into clean, study-ready flashcards—organized by topic with concise summaries and question–answer pairs.

This project segments input documents into coherent topics, summarizes each topic, and generates flashcard-friendly Q&A for rapid review. Built with Python (app + NLP pipeline) and an HTML front-end.

## Features

- **Topic segmentation** — splits long documents into logical sections for focused studying.  
- **Auto-summarization** — produces brief, skimmable topic synopses.  
- **Question generation** — creates Q&A pairs you can export to your flashcard tool.  
- **Web UI** — upload a file, review topics, copy/export generated cards.  
- **Sample inputs** — try it quickly with files in `samples/`.

## Project Structure

```
Topic-wise-Flashcard-Generator/
├─ app.py                    # Flask app / web server
├─ requirements.txt          # Python dependencies
├─ topic_segmentation.py     # Topic boundary detection
├─ summarization.py          # Topic-level summarization
├─ question_generation.py    # Q&A card generation
├─ text_extraction.py        # Ingest PDF/TXT and clean text
├─ templates/                # HTML templates for the UI
├─ uploads/                  # (runtime) uploaded files
└─ samples/                  # Example documents
```

> Languages (per GitHub): Python (~87%) and HTML (~13%).

## Quickstart

### 1) Prerequisites
- Python 3.9+ recommended
- macOS/Linux/Windows

### 2) Clone & install
```bash
git clone https://github.com/Misker04/Topic-wise-Flashcard-Generator.git
cd Topic-wise-Flashcard-Generator
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

### 3) Run the app
```bash
python app.py
```

Then open your browser to:
```
http://localhost:5000
```

## How to Use

1. **Launch** the web app (`python app.py`) and open the local URL.  
2. **Upload** a document (PDF/TXT) or use one from the `samples/` folder.  
3. **Process** the file to:
   - view **detected topics**,
   - read each **topic summary**,
   - review **generated Q&A** flashcards.  
4. **Export**: copy the flashcards or save them as CSV/TSV from the UI (if provided), then import into your preferred tool (e.g., Anki/RemNote).


## Configuration

Most setups work out-of-the-box. If you plug in external models or APIs later (e.g., OpenAI/HF), add environment variables here and document them:

```bash
# examples (uncomment/adapt if you wire these in)
# export OPENAI_API_KEY=...
# export HF_HOME=...
# export MODEL_NAME=...
```

## Modules Overview

- `text_extraction.py` — reads PDFs/TXT and normalizes text for downstream tasks.  
- `topic_segmentation.py` — finds topic boundaries for chunked processing.  
- `summarization.py` — creates concise summaries per topic.  
- `question_generation.py` — turns content into question–answer pairs for flashcards.  
- `app.py` — Flask app wiring the pipeline to a simple web UI (`templates/`).


## Sample Workflow (CLI-style)

If you prefer scripting (or later add a CLI), a typical flow is:

1. Extract and clean text →  
2. Segment into topics →  
3. Summarize each topic →  
4. Generate Q&A cards →  
5. Save as CSV/JSON.


## Try with Sample Files

Place or select a file from `samples/`, then process it via the UI to see topic blocks, summaries, and generated cards.

## Output Format

- **Per topic**:
  - `topic_title`
  - `summary`
  - `cards`: list of `{question, answer}`

For CSV export (Anki-ready), use two columns: `Question,Answer`.


## Notes & Tips

- Quality improves when inputs are **clean** (remove headers/footers, OCR noise).
- Long documents work best when **segmented** before summarization and QG.
- You can tune question styles (definitions, cloze, why/how, MCQ stems) inside `question_generation.py`.


## Development

Run in debug mode:

```bash
# inside app.py, if using Flask:
# app.run(debug=True)
python app.py
```

Lint/format (suggested):
```bash
pip install ruff black
ruff check .
black .
```


## Troubleshooting

- **App runs but UI is blank**: ensure `templates/` files are present and Flask is pointing to them.  
- **Large PDFs fail**: try splitting the PDF or increasing request limits/timeouts.  
- **Encoding errors**: convert inputs to UTF-8 text first.

## Acknowledgments

This repository was created to streamline studying by converting dense academic materials into topic-organized flashcards with minimal manual effort.

