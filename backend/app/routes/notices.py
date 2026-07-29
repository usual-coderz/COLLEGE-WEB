from fastapi import APIRouter
from bson import ObjectId

from app.core.database import db
from app.models.notice import NoticeCreate

router = APIRouter(
    prefix="/notices",
    tags=["Notices"]
)

@router.post("/create")
async def create_notice(notice: NoticeCreate):
    data = notice.model_dump()

    result = await db.notices.insert_one(data)

    return {
        "success": True,
        "notice_id": str(result.inserted_id)
    }


@router.get("/{college_id}")
async def get_notices(college_id: str):
    notices = []

    async for notice in db.notices.find(
        {"college_id": college_id}
    ):
        notice["_id"] = str(notice["_id"])
        notices.append(notice)

    return notices


@router.delete("/{notice_id}")
async def delete_notice(notice_id: str):
    await db.notices.delete_one(
        {"_id": ObjectId(notice_id)}
    )

    return {
        "success": True,
        "message": "Notice deleted"
    }