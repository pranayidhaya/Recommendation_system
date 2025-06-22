# recommend.py

import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Load pre-trained model (this downloads once)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load product data
with open("product_data.json", "r", encoding="utf-8") as f:
    products = json.load(f)

# Create a list of descriptions for embedding
product_texts = [
    f"{p['name']} {p['category']} {p['color']} {p['description']}"
    for p in products
]

# Embed product descriptions
product_embeddings = model.encode(product_texts)

def recommend_products(user_query, top_k=5):
    """
    Given a text query, return top_k matching products using cosine similarity
    """
    query_embedding = model.encode([user_query])
    similarities = cosine_similarity(query_embedding, product_embeddings)[0]
    
    # Get top K indices
    top_indices = np.argsort(similarities)[::-1][:top_k]
    
    results = []
    for idx in top_indices:
        product = products[idx]
        score = float(similarities[idx])
        results.append({
            "id": product["id"],
            "name": product["name"],
            "category": product["category"],
            "score": round(score, 3),
            "description": product["description"]
        })
    
    return results
