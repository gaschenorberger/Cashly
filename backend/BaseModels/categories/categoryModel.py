from pydantic import BaseModel

class NewCategory(BaseModel):
    userId: int
    category: str