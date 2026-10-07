# PDF Embedding API

## Overview

This project accepts a PDF file as input, extracts text from the PDF, splits the text into chunks, generates vector embeddings for each chunk, and exposes the functionality through FastAPI APIs.

The application is designed to be containerized using Docker and deployed on Azure.

---

## Features

- Upload PDF files
- Extract text using PyPDF
- Split text into chunks
- Generate vector embeddings
- FastAPI REST APIs
- Swagger API documentation
- Docker-ready configuration

---

## Project Structure

```text
pdf_embedding_api/
│
├── app.py
├── pdf_processor.py
├── chunking.py
├── embedding.py
├── requirements.txt
├── Dockerfile
├── uploads/
└── README.md

