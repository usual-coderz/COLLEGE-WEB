from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.core.database import db

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.post("/approve/{college_id}")
async def approve_college(college_id: str):
    college = await db.colleges.find_one(
        {"_id": ObjectId(college_id)}
    )

    if not college:
        raise HTTPException(
            status_code=404,
            detail="College not found"
        )

    await db.colleges.update_one(
        {"_id": ObjectId(college_id)},
        {"$set": {"status": "approved"}}
    )

    existing_admin = await db.users.find_one(
        {
            "college_id": college_id,
            "role": "college_admin"
        }
    )

    if not existing_admin:
        await db.users.insert_one(
            {
                "college_id": college_id,
                "name": f"{college['college_name']} Admin",
                "email": college["email"],
                "password": "Admin@123",
                "role": "college_admin",
                "status": "active"
            }
        )

    return {
        "success": True,
        "message": "College approved and admin account created"
    }