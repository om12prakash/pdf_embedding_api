# PDF Embedding API

A FastAPI-based backend service that accepts PDF files, extracts text, splits the text into chunks, generates embeddings, and returns processing information through REST APIs.

---

## Project Overview

This application demonstrates a document processing pipeline commonly used in AI-powered and Retrieval-Augmented Generation (RAG) solutions.

### Workflow

```text
PDF Upload
    ↓
Text Extraction
    ↓
Text Chunking
    ↓
Embedding Generation
    ↓
API Response
```

---

## Features

- Upload PDF files through REST API
- Extract text using PyPDF
- Split large text into chunks
- Generate embeddings using TF-IDF
- FastAPI-based API endpoints
- Interactive API testing using Swagger UI
- Docker-ready for deployment
- Azure deployment ready

---

## Technology Stack

### Backend Framework

- FastAPI

### PDF Processing

- PyPDF

### Text Chunking

- Custom Python Logic

### Embeddings

- Scikit-Learn TF-IDF Vectorizer

### API Documentation

- Swagger UI

### Containerization

- Docker

### Cloud Deployment

- Azure Container Apps
- Azure App Service

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
├── .dockerignore
└── uploads/
```

---

# Installation

## 1. Clone the Repository

```bash
git clone <repository-url>
cd pdf_embedding_api
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Health Check Endpoint

### Request

```http
GET /
```

### Response

```json
{
  "message": "PDF Embedding API is running"
}
```

---

## Process PDF Endpoint

### Request

```http
POST /process_pdf
```

### Input

Form Data

| Field | Type |
|---------|---------|
| file | PDF File |

### Sample Response

```json
{
  "file_name": "sample.pdf",
  "text_length": 1250,
  "total_chunks": 3,
  "embedding_dimension": 45
}
```

---

# Module Details

## app.py

Main FastAPI application.

Responsibilities:

- Accept PDF uploads
- Save uploaded files
- Trigger processing workflow
- Return API responses

Workflow:

```text
Upload PDF
      ↓
Extract Text
      ↓
Chunk Text
      ↓
Generate Embeddings
      ↓
Return Response
```

---

## pdf_processor.py

Responsible for extracting text from PDF documents.

Uses:

```python
from pypdf import PdfReader
```

Input:

```text
PDF File
```

Output:

```text
Extracted Text
```

---

## chunking.py

Responsible for splitting large text into smaller chunks.

Example:

Input:

```text
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

Chunk Size:

```text
5
```

Output:

```text
ABCDE
FGHIJ
KLMNO
PQRST
UVWXY
Z
```

Purpose:

- Improve processing efficiency
- Handle large documents
- Support future RAG implementations

---

## embedding.py

Responsible for converting text chunks into vectors.

Uses:

```python
from sklearn.feature_extraction.text import TfidfVectorizer
```

Input:

```text
Text Chunks
```

Output:

```text
Numerical Vector Embeddings
```

Example:

```text
Azure is a cloud platform
```

↓

```text
[0.12, 0.43, 0.89, ...]
```

---

# API Processing Flow

## Step 1

User uploads a PDF.

```text
sample.pdf
```

---

## Step 2

FastAPI receives the file.

```text
POST /process_pdf
```

---

## Step 3

PyPDF extracts text content.

```python
PdfReader()
```

---

## Step 4

Extracted text is divided into chunks.

```python
chunk_text()
```

---

## Step 5

TF-IDF generates embeddings for each chunk.

```python
generate_embeddings()
```

---

## Step 6

API returns processing details.

```json
{
  "file_name": "sample.pdf",
  "text_length": 1250,
  "total_chunks": 3,
  "embedding_dimension": 45
}
```

---

# Local Testing

## Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

Steps:

1. Open Swagger UI
2. Expand `/process_pdf`
3. Click "Try it Out"
4. Upload PDF
5. Click "Execute"
6. View response

---

# Docker Support

## Build Docker Image

```bash
docker build -t pdf-embedding-api .
```

---

## Run Docker Container

```bash
docker run -p 8000:8000 pdf-embedding-api
```

---

## Access Swagger

```text
http://localhost:8000/docs
```

---

# Azure Deployment Architecture

## Option 1: Azure Container Apps

```text
FastAPI Application
         ↓
Docker Image
         ↓
Azure Container Registry (ACR)
         ↓
Azure Container Apps
```

---

## Option 2: Azure App Service

```text
FastAPI Application
         ↓
Docker Image
         ↓
Azure App Service
```

---

# Challenges Encountered

## Challenge 1

Python 3.14 compatibility issues with AI libraries.

### Resolution

Migrated project to Python 3.11.

---

## Challenge 2

SSL certificate restrictions prevented downloading Hugging Face embedding models.

### Resolution

Implemented local TF-IDF-based embeddings using Scikit-Learn to keep the solution fully functional.

---

# Future Enhancements

- Replace TF-IDF with Sentence Transformers
- Use Azure OpenAI Embeddings
- Store embeddings in a vector database
- Integrate Azure AI Search
- Implement semantic search
- Build a complete RAG solution
- Add authentication and authorization
- Add database persistence

---

# Key Learning Outcomes

- FastAPI API Development
- REST API Design
- PDF Processing
- Text Chunking
- Embedding Generation
- Swagger Documentation
- Containerization with Docker
- Azure Deployment Architecture
- Backend Service Development for AI Applications

---

# Author

**Om Prakash Yadav**

Backend Python API Assignment

Technologies Used:

- FastAPI
- Python
- PyPDF
- Scikit-Learn
- Docker
- Azure