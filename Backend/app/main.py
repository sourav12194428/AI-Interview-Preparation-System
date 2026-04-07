from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.db.models import Interview_Session, Session_Questions
from app.api import interview

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(interview.router)

@app.get("/")
def home():
    return {"message": "Backend is running successfully"}