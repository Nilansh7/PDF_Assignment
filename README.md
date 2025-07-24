#  PDF Assignment to MCQ Generator using AI

This project automates the process of generating multiple-choice questions (MCQs) from a scanned assignment or handwritten notes in PDF format using AI.

##  Features

-  Extracts text and images from PDF assignments
-  Identifies questions with associated images using layout detection
-  Generates MCQs using a powerful language model
-  Outputs MCQs in a structured JSON format

##  Technologies Used

- Python
- PyMuPDF (`fitz`)
- `transformers` by Hugging Face
- LayoutLMv3 (for image-text mapping)
- OpenAI / LLM API (for MCQ generation)

##  Folder Structure

PDF_Assignment/

├── sample.pdf                  # Input PDF file

├── extract_pdf.py              # Extracts text and images from PDF

├── identify_questions.py       # Maps images to relevant questions

├── generate_mcqs.py            # Generates MCQs using AI

├── extracted_content/          # Extracted text + images

   └── ai_ready_questions.json # Preprocessed content for MCQ generation

├── generated_mcqs.json         # Final MCQs with options and answers



##  How to Run

1. **Place your PDF assignment** in the root folder as `sample.pdf`.

2. Run the following scripts step-by-step:
   ```bash
   python extract_pdf.py
   python identify_questions.py
   python generate_mcqs.py
The final MCQs will be saved in:
  generated_mcqs.json

  
Output Format (JSON)

[
  {
    "question": "What is the capital of France?",
    "options": ["Berlin", "Madrid", "Paris", "Rome"],
    "answer": "Paris"
  },
  ...
]

Author

Nilansh Kumar Singh
GitHub: Nilansh7



