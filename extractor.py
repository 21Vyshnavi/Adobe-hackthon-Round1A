def extract_outline_from_pdf(pdf_path):
    # TODO: Implement heading extraction logic
    title = "Sample Title"
    outline = [
        { "level": "H1", "text": "Introduction", "page": 1 },
        { "level": "H2", "text": "What is AI?", "page": 2 },
        { "level": "H3", "text": "History of AI", "page": 3 }
    ]
    return title, outline
