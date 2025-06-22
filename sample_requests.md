Example 1

POST /recommend

Request Body:
```json
{
  "query": "show me black sneakers",
  "top_k": 3
}

Response:

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

Example 2

Requested Body:

{
  "query": "white running shoes",
  "top_k": 2
}

Response:

{
  "query": "white running shoes",
  "results": [
    {
      "id": 2,
      "name": "Adidas Ultraboost",
      "category": "running shoes",
      "score": 0.651,
      "description": "Lightweight white running shoes with boost cushioning"
    },
    {
      "id": 9,
      "name": "Nike Revolution 6",
      "category": "running shoes",
      "score": 0.589,
      "description": "Everyday running shoes with responsive cushioning"
    }
  ]
}

Exampe 3

Requested Body:

{
  "query": "casual sandals",
  "top_k": 2
}

Response:

{
  "query": "casual sandals",
  "results": [
    {
      "id": 8,
      "name": "Crocs Classic Clogs",
      "category": "sandals",
      "score": 0.623,
      "description": "Lightweight green Crocs for casual indoor/outdoor wear"
    },
    {
      "id": 7,
      "name": "Bata Casual Loafers",
      "category": "loafers",
      "score": 0.554,
      "description": "Comfortable tan loafers for semi-formal occasions"
    }
  ]
}
