import fitz  # PyMuPDF
import os
import json

# Set file and folder names
PDF_FILE = "sample.pdf"
OUTPUT_DIR = "extracted_content"
IMAGES_DIR = os.path.join(OUTPUT_DIR, "images")
JSON_OUTPUT_PATH = os.path.join(OUTPUT_DIR, "structured_output.json")

# Create output folders
os.makedirs(IMAGES_DIR, exist_ok=True)

# Open the PDF file
doc = fitz.open(PDF_FILE)
output_data = []

# Loop through pages
for page_number, page in enumerate(doc, start=1):
    print(f"Processing page {page_number}...")
    page_data = {
        "page": page_number,
        "text": page.get_text(),
        "images": []
    }

    # Extract images
    image_list = page.get_images(full=True)
    for img_index, img in enumerate(image_list, start=1):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]

        image_filename = f"page{page_number}_image{img_index}.{image_ext}"
        image_path = os.path.join(IMAGES_DIR, image_filename)

        with open(image_path, "wb") as f:
            f.write(image_bytes)

        page_data["images"].append(image_path)

    output_data.append(page_data)

# Save JSON
with open(JSON_OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=4)

print("✅ Done! Check the 'extracted_content' folder.")
