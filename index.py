# index.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

marks_data = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40
}

@app.get("/api")
async def get_marks(name: List[str] = []):
    return {"marks": [marks_data.get(n, 0) for n in name]}
