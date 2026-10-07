from sentence_transformers import SentenceTransformer

print("Loading model...")

model = SentenceTransformer(
"paraphrase-MiniLM-L3-v2"
)

print("Model loaded!")

embedding = model.encode(
["Hello World"]
)

print(embedding.shape)