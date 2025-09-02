from transformers import T5ForConditionalGeneration, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("valhalla/t5-base-qg-hl")
model = T5ForConditionalGeneration.from_pretrained("valhalla/t5-base-qg-hl")

def generate_questions(passage):
    if not passage.strip() or len(passage.split()) < 5:
        return [("What is the summary of this topic?", passage.strip())]

    # Pick the middle sentence as the answer span to highlight
    sentences = passage.strip().split(". ")
    if len(sentences) < 3:
        highlight = sentences[0]
    else:
        highlight = sentences[len(sentences) // 2]
    
    input_text = passage.replace(highlight, f"<hl> {highlight.strip()} <hl>")
    input_text = "generate question: " + input_text.strip()

    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    try:
        output = model.generate(
            input_ids,
            max_length=64,
            do_sample=True,
            top_k=50,
            temperature=0.8
        )
        question = tokenizer.decode(output[0], skip_special_tokens=True)
        return [(question.strip(), highlight.strip())]
    except Exception as e:
        return [("Error generating question", f"Model exception: {e}")]
