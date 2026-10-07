
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

def generate_embeddings(chunks):
    if not chunks:
        return []

    embeddings = vectorizer.fit_transform(chunks)
    #convert matrix to list
    return embeddings.toarray().tolist()