from fastapi import FastAPI

app = FastAPI(
    title="College Web API",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "status": "online",
        "message": "College Web Backend Running"
    }