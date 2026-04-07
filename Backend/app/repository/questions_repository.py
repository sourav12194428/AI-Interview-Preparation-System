# app/repositories/question_repo.py

from sqlalchemy.orm import Session
from app.db.models import Question_Bank, Session_Questions


class QuestionRepository:

    @staticmethod
    def get_used_question_ids(session_id: int, db: Session):
        result = db.query(Session_Questions.question_id).filter(
            Session_Questions.session_id == session_id
        ).all()
        
        return [r[0] for r in result]

    @staticmethod
    def get_next_question(topic: str, tag: str, used_ids: list, db: Session): #topic: str, tag: str
        query = db.query(Question_Bank).filter(
            Question_Bank.topic == topic
        )

        if tag:
            query = query.filter(Question_Bank.tag == tag)

        if used_ids:
            query = query.filter(~Question_Bank.id.in_(used_ids))
        
        return query.first()

    @staticmethod
    def add_session_question(session_id: int, question_id: int, db: Session):
        session_question = Session_Questions(
            session_id=session_id,
            question_id=question_id
        )
        db.add(session_question)
        db.commit()
        db.refresh(session_question)

        return session_question