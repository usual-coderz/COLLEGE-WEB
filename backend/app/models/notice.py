from pydantic import BaseModel

class NoticeCreate(BaseModel):
    college_id: str
    title: str
    description: str
    created_by: str