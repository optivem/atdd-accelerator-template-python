from pydantic import BaseModel


class Todo(BaseModel):
    """Todo model representing a todo item."""
    
    userId: int
    id: int
    title: str
    completed: bool

    def __init__(self, userId: int = 0, id: int = 0, title: str = "", completed: bool = False, **kwargs):
        super().__init__(userId=userId, id=id, title=title, completed=completed, **kwargs)

    class Config:
        """Pydantic configuration."""
        json_encoders = {
            # Custom encoders if needed
        }
        schema_extra = {
            "example": {
                "userId": 1,
                "id": 1,
                "title": "Sample todo item",
                "completed": False
            }
        }