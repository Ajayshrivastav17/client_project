from pydantic import BaseModel

class Response(BaseModel):
    reply: str
    sentiment: str
    confidence: float

data = {
    "reply": "Hello!",
    "sentiment": "positive",
    "confidence": 0.98
}

validated = Response.model_validate(data)

print(validated)