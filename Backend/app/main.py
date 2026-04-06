from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.db.models import Interview_Session, Question_Bank, Session_Questions, Session_Answers

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Backend is running successfully"}