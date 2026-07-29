from fastapi import FastAPI
from app.routes.colleges import router as colleges_router

app = FastAPI(
    title="College Web API",
    version="1.0.0"
)

app.include_router(colleges_router)


@app.get("/")
async def root():
    return {
        "status": "online",
        "message": "College Web Backend Running"
    }