from app.db.models import Interview_Session, Session_Questions

class InterviewRepository:

    @staticmethod
    def create_session(db, topic, user_id, tag):
        session = Interview_Session(
            user_id=user_id,
            topic=topic,
            tag=tag
        )
        db.add(session)
        db.commit()
        db.refresh(session)
        return session

    @staticmethod
    def save_questions(db, session_id, questions):
        question_objs = [
            Session_Questions(
                session_id=session_id
                # question=q
            )
            # for q in questions
        ]

        db.add_all(question_objs)
        db.commit()