from pydantic import BaseModel

class CourseSchema(BaseModel):
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str


