from pydantic import BaseModel

class User(BaseModel):
    college_id: str
    name: str
    email: str
    password: str
    role: str
    status: str