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

Example 4

Requested Body:

{
  "query": "best noise cancelling headphones",
  "top_k": 3
}

Response:

{
  "query": "best noise cancelling headphones",
  "results": [
    {
      "id": 12,
      "name": "Sony WH-1000XM5",
      "category": "headphones",
      "score": 0.71,
      "description": "Premium over-ear headphones with industry-leading noise cancellation"
    },
    {
      "id": 11,
      "name": "Samsung Galaxy Buds 2",
      "category": "earphones",
      "score": 0.598,
      "description": "Wireless noise-cancelling earbuds with clear sound"
    },
    {
      "id": 17,
      "name": "Amazon Echo Dot (5th Gen)",
      "category": "smart home",
      "score": 0.254,
      "description": "Smart speaker with Alexa voice assistant and improved sound"
    }
  ]
}

Example 5

Requested Body:

{
  "query": "beginner dslr camera",
  "top_k": 3
}

Response:

{
  "query": "beginner dslr camera",
  "results": [
    {
      "id": 22,
      "name": "Canon EOS 1500D DSLR Camera",
      "category": "cameras",
      "score": 0.59,
      "description": "Beginner-friendly DSLR camera with 24.1 MP sensor"
    },
    {
      "id": 21,
      "name": "Adidas Duffel Gym Bag",
      "category": "bags",
      "score": 0.139,
      "description": "Durable and spacious gym bag with adjustable strap"
    },
    {
      "id": 20,
      "name": "HP DeskJet 2331 Printer",
      "category": "printers",
      "score": 0.121,
      "description": "All-in-one color printer for home and student use"
    }
  ]
}

