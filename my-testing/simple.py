from pydantic import BaseModel

from outlines import models, generate


class User(BaseModel):
    name: str
    last_name: str
    id: int


model = models.transformers("mistralai/Mistral-7B-Instruct-v0.3")
generator = generate.json(model, User)
result = generator(
    "Create a user profile with the fields name, last_name and id"
)
print(result)
# User(name="John", last_name="Doe", id=11)