from simplet5 import SimpleT5

# Load the small model locally
summarizer = SimpleT5()
summarizer.load_model("t5", "t5-small", use_gpu=False)

def generate_summary(text):
    if len(text.strip().split()) < 10:
        return text
    text = "summarize: " + text.strip().replace("\n", " ")
    try:
        summary = summarizer.predict(text[:512])[0]
        return summary
    except Exception as e:
        return f"Summarization failed: {e}"
