from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Enable CORS so the API can be accessed from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Hardcoded marks for imaginary students
student_marks = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40,
    "E": 50
}

@app.get("/api")
async def get_marks(name: List[str] = []):
    result = [student_marks.get(n, 0) for n in name]
    return {"marks": result}
