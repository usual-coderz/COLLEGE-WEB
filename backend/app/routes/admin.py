from fastapi import APIRouter, HTTPException
from bson import ObjectId

from app.core.database import db

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

SUPER_ADMIN_EMAIL = "admin@collegeweb.com"
SUPER_ADMIN_PASSWORD = "Admin@123"


@router.post("/login")
async def admin_login(data: dict):
    email = data.get("email")
    password = data.get("password")

    if (
        email == SUPER_ADMIN_EMAIL
        and password == SUPER_ADMIN_PASSWORD
    ):
        return {
            "success": True,
            "message": "Login successful"
        }

    raise HTTPException(
        status_code=401,
        detail="Invalid credentials"
    )


@router.get("/pending-colleges")
async def pending_colleges():
    colleges = []

    async for college in db.colleges.find(
        {"status": "pending"}
    ):
        college["_id"] = str(college["_id"])
        colleges.append(college)

    return colleges


@router.post("/approve/{college_id}")
async def approve_college(college_id: str):
    result = await db.colleges.update_one(
        {"_id": ObjectId(college_id)},
        {"$set": {"status": "approved"}}
    )

    if result.modified_count == 0:
        raise HTTPException(
            status_code=404,
            detail="College not found"
        )

    return {
        "success": True,
        "message": "College approved"
    }


@router.post("/reject/{college_id}")
async def reject_college(college_id: str):
    result = await db.colleges.update_one(
        {"_id": ObjectId(college_id)},
        {"$set": {"status": "rejected"}}
    )

    if result.modified_count == 0:
        raise HTTPException(
            status_code=404,
            detail="College not found"
        )

    return {
        "success": True,
        "message": "College rejected"
    }