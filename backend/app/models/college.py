from pydantic import BaseModel, EmailStr


class CollegeCreate(BaseModel):
    college_name: str
    email: EmailStr
    phone: str
    address: str


class CollegeResponse(BaseModel):
    success: bool
    message: str