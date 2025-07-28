# PDF Outline Extractor

## How to Build

```bash
docker build --platform linux/amd64 -t mysolution:latest .
```

## How to Run

```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none mysolution:latest
```

## Project Structure

- `main.py`: Entry point
- `utils/extractor.py`: Heading extraction logic
- `input/`: PDF input folder
- `output/`: Output JSON folder
