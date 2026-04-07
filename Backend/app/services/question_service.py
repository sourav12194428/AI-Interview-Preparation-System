# app/services/question_service.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repository.questions_repository import QuestionRepository
from app.db.models import Interview_Session


class QuestionService:

    @staticmethod
    def get_next_question(session_id: int, db: Session):
        
        # 1. Validate session
        session = db.query(Interview_Session).filter(
            Interview_Session.id == session_id
        ).first()

        if not session:
            raise HTTPException(status_code=404, detail="Session not found")

        # 2. Get used questions
        used_ids = QuestionRepository.get_used_question_ids(session_id, db)


        # 3. Fetch next question
        question = QuestionRepository.get_next_question(
            topic=session.topic,
            tag=session.tag,
            used_ids=used_ids,
            db=db
        )

        if not question:
            raise HTTPException(
                status_code=404,
                detail="No more questions available"
            )

        # 4. Save in session_questions
        session_question = QuestionRepository.add_session_question(
            session_id=session_id,
            question_id=question.id,
            db=db
        )

        return {
            "session_question_id": session_question.id,
            "question_id": question.id,
            "question_text": question.question_text,
            "topic": question.topic,
            "tag": question.tag
        }





















questions_db = {}


# def generate_question(topic: str):
#     question = f"Explain the concept of {topic} in detail."

#     question_id = len(questions_db) + 1

#     questions_db[question_id] = {
#         "id": question_id,
#         "topic": topic,
#         "question": question
#     }

#     return questions_db[question_id]


# def get_question(question_id: int):
#     return questions_db.get(question_id)