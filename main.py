from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uvicorn

# Dummy data to simulate the marks
marks_data = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40
}

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def get_marks(name: List[str] = []):
    result = [marks_data.get(n, 0) for n in name]
    return {"marks": result}
