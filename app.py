# app.py

from fastapi import FastAPI
from pydantic import BaseModel
from recommend import recommend_products

# Initialize FastAPI app
app = FastAPI(
    title="INMIN Product Recommendation API",
    description="An ML-powered recommendation engine for product search.",
    version="1.0"
)

# Input model for request body
class QueryInput(BaseModel):
    query: str
    top_k: int = 5  # Optional, defaults to 5

# API Endpoint
@app.post("/recommend")
def get_recommendations(input: QueryInput):
    """
    Recommends top_k products based on user query
    """
    results = recommend_products(input.query, input.top_k)
    return {
        "query": input.query,
        "results": results
    }
