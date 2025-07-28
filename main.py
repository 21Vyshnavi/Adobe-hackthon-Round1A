import os
import json
import time
from utils.extractor import extract_outline_from_pdf

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def main():
    start = time.time()
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            input_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".json"))

            title, outline = extract_outline_from_pdf(input_path)
            result = {
                "title": title,
                "outline": outline
            }

            with open(output_path, "w") as f:
                json.dump(result, f, indent=2)

    print(f"✅ Done in {time.time() - start:.2f}s")

if __name__ == "__main__":
    main()
