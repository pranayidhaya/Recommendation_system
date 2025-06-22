INMIN AI Developer Trial Submission
 Submitted by: Pranay Idhaya
 Date: June 22, 2025
 Objective

As part of the INMIN AI Developer Trial, this project demonstrates a mini recommendation engine for natural language
queries like:
"show me black sneakers"
The system returns relevant product matches using semantic similarity, sentence embeddings, and a FastAPI-powered
API.

 Key Features

    Semantic Query Understanding - Understands user intent using ML, not just keyword matching
    Cosine Similarity Matching - Uses vector-based similarity for accuracy
    FastAPI Endpoint - Clean REST API with Swagger UI for testing
    Easily Extendable - Supports new product data, categories, models
    Fully Offline - Works locally with no cloud dependencies
    ML Logic & NLP Pipeline

- Model: all-MiniLM-L6-v2 from sentence-transformers
- Technique: No training; pre-trained embeddings
- Inputs: Query and product descriptions are embedded to vectors
- Similarity: Cosine similarity between query and product vectors
- Top-K: Returns top N products ranked by semantic similarity

 Tech Stack
Programming | Python 3.10+
ML Model | Sentence Transformers
Matching | scikit-learn (cosine)
API | FastAPI
Server | Uvicorn
Testing | Swagger UI (auto docs)

Project Structure
    inmin_ai_recommendation/
        app.py FastAPI API server
        recommend.py ML recommendation logic
        product_data.json Mock product list (10 items)
        requirements.txt Python dependencies
        README.md This file
        sample_requests.md Sample inputs/outputs

How to Run the Project

Step 1: Clone the Repo / Extract Folder
cd inmin_ai_recommendation
Step 2: (Optional) Create Virtual Environment
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
Step 3: Install Required Packages
pip install -r requirements.txt
Step 4: Launch the API
uvicorn app:app --reload
Visit Swagger UI at:
http://127.0.0.1:8000/docs

 Example API Request
POST /recommend
{
 "query": "show me black sneakers",
   "top_k": 3
}

 Example API Response
{
 "query": "show me black sneakers",
 "results": [
 {
 "id": 3,
 "name": "Puma Street Rider",
 "category": "sneakers",
 "score": 0.682,
 "description": "Casual black sneakers for everyday use"
 },
 {
 "id": 1,
 "name": "Nike Air Max 90",
 "category": "sneakers",
 "score": 0.618,
 "description": "Stylish black Nike sneakers with air-cushion sole"
 },
 {
 "id": 10,
 "name": "Red Tape Oxford Shoes",
 "category": "formal shoes",
 "score": 0.538,
 "description": "Elegant black leather shoes for formal events"
 }
 ]
}

 Author Info
Name: Pranay Idhaya
Position Applied: AI Developer
Company: INMIN
Trial Submission Date: June 22, 2025
 Final Files for Submission
app.py - FastAPI API
recommend.py - Core recommendation logic
product_data.json - Mock product catalog
requirements.txt - Dependency list
README.md - Complete documentation (this)
sample_requests.md - Optional extra test cases (if needed)