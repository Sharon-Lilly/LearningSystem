from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Minimal FastAPI skeleton (no logic)
app = FastAPI(title="LearningSystem")


@app.get("/")
async def read_root():
    return {"message": "Backend running"}


# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Add routes and application logic in later iterations.
