import json
import os

# Load the structured output from Part 1
with open("extracted_content/structured_output.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

# Output list
questions = []

# Loop through pages
for page in pages:
    text = page["text"]
    images = page["images"]

    if len(images) >= 2:  # Assuming we have at least 1 question image and 1 option
        question_data = {
            "question": text.strip().split("\n")[0],  # Use first line of text as question
            "question_image": images[0],
            "option_images": images[1:]  # rest of the images as options
        }
        questions.append(question_data)

# Save to new JSON
output_path = "extracted_content/ai_ready_questions.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=4)

print(f"✅ Questions with image mapping saved to: {output_path}")
