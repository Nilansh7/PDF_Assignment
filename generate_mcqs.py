import json
import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import os

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-vqa-base").to(device)

# Load questions with image mapping
with open("extracted_content/ai_ready_questions.json", "r") as f:
    questions_data = json.load(f)

mcqs = []

for item in questions_data:
    question = item.get("question")
    image_path = item.get("image")

    if not question or not image_path or not os.path.exists(image_path):
        continue  # Skip invalid entries

    try:
        image = Image.open(image_path).convert("RGB")
        inputs = processor(question, image, return_tensors="pt").to(device)
        out = model.generate(**inputs)
        answer = processor.decode(out[0], skip_special_tokens=True)

        mcqs.append({
            "question": question,
            "image_path": image_path,
            "correct_answer": answer
        })
    except Exception as e:
        print(f"Error processing: {question} -> {e}")

# Save the MCQs to JSON file
with open("generated_mcqs.json", "w") as f:
    json.dump(mcqs, f, indent=4)

print("✅ MCQs with answers saved to: generated_mcqs.json")
