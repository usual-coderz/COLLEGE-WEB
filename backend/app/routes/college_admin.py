from fastapi import APIRouter, HTTPException
from app.core.database import db

router = APIRouter(
    prefix="/college-admin",
    tags=["College Admin"]
)

@router.post("/login")
async def login(data: dict):
    user = await db.users.find_one(
        {
            "email": data.get("email"),
            "password": data.get("password"),
            "role": "college_admin"
        }
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    user["_id"] = str(user["_id"])

    return {
        "success": True,
        "user": user
    }