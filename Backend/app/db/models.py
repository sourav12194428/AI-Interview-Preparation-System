from sqlalchemy import create_engine, Column, Enum, Integer, String, Text, text, ForeignKey, DateTime, Float, TIMESTAMP, func
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base   # your declarative base


# ---------------------------
# 1. Interview Session
# ---------------------------
class Interview_Session(Base):
    __tablename__ = "interview_session"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    topic = Column(String, nullable=False)
    # tag = Column(Enum("easy", "medium", "hard", name="tag_enum"), nullable=False )
    tag = Column(Enum("easy", "medium", "hard", name="tag_enum", create_type=False))
    started_at = Column(TIMESTAMP,nullable=False, default=func.now())
    completed_at = Column(TIMESTAMP,nullable=False, default=text("NOW() + INTERVAL '30 minutes'"))
    status = Column(Enum("in_progress", "completed", name="status_enum"), default="in_progress")  # pending / in_progress / completed
    overall_score = Column(Float, nullable=True)
    final_feedback = Column(Text, nullable=True)

    session_question=relationship("Session_Questions", back_populates="session")
    answers=relationship("Session_Answers", back_populates="session")
    
# ---------------------------
# 2. Session_Questions
# ---------------------------
class Session_Questions(Base):
    __tablename__ = "session_questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(Integer, ForeignKey("interview_session.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("question_bank.id"), nullable=False)

    # Relationships
    session = relationship("Interview_Session", back_populates="session_question")
    question = relationship("Question_Bank", back_populates="session_question")
    answers = relationship("Session_Answers", back_populates="session_question")

#---------------------------
# 3. Session_Answers
#---------------------------
class Session_Answers(Base):
    __tablename__ = "session_answers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(Integer, ForeignKey("interview_session.id"), nullable=False)
    session_question_id = Column(Integer, ForeignKey("session_questions.id"), nullable=False)
    user_answer = Column(Text, nullable=True)
    ai_feedback = Column(Text, nullable=True)
    score = Column(Float, nullable=True)

    # Relationships
    session = relationship("Interview_Session",  back_populates="answers")
    session_question = relationship("Session_Questions", back_populates="answers")


#---------------------------
# 4. Question_Bank
#---------------------------
class Question_Bank(Base):
    __tablename__ = "question_bank"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_text = Column(Text, nullable=False)
    topic = Column(String, nullable=False)
    # tag = Column(Enum("easy", "medium", "hard", name="tag_enum"), nullable=True)
    tag = Column(Enum("easy", "medium", "hard", name="tag_enum", create_type=False))
    expected_answer = Column(Text, nullable=True)

    session_question = relationship("Session_Questions", back_populates="question")