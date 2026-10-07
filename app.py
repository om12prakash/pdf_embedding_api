from fastapi import FastAPI, UploadFile, File

from pdf_processor import extract_text_from_pdf
from chunking import chunk_text
from embedding import generate_embeddings

#file path operation
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok = True)

#Health check

@app.get("/")
def home():
    return{
        "message":'PDF Embedding API is running'
    }

#Main API for PDF processing

@app.post("/process_pdf")

async def process_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    #saving to disk
    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(file_path)

    chunks = chunk_text(text)

    print("Text extracted")
    print(f"Chunks created: {len(chunks)}")

    embeddings = generate_embeddings(chunks)

    print("Embeddings generated")

    return {
    "file_name": file.filename,
    "text_length": len(text),
    "total_chunks": len(chunks),
    "embedding_dimension": len(embeddings[0]) if embeddings else 0,
    "chunks": chunks
    }
