from fastapi import APIRouter
from app.models.college import CollegeCreate
from app.core.database import db

router = APIRouter(
    prefix="/colleges",
    tags=["Colleges"]
)


@router.post("/register")
async def register_college(college: CollegeCreate):
    data = college.model_dump()

    data["status"] = "pending"

    await db.colleges.insert_one(data)

    return {
        "success": True,
        "message": "College registration submitted"
    }


@router.get("/")
async def get_colleges():
    colleges = []

    async for college in db.colleges.find():
        college["_id"] = str(college["_id"])
        colleges.append(college)

    return colleges