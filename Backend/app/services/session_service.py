from app.repository.interview_repository import InterviewRepository
# from services.llm_service import generate_questions_llm

class InterviewService:

    def start_interview(self, db, user_id, topic, tag):
        
        # 1. Create DB session
        session = InterviewRepository.create_session(
            db=db,
            user_id=user_id,
            topic=topic,
            tag=tag
        )

        # # 2. Generate questions (LLM or RAG)
        # questions = generate_questions_llm(topic, tag)

        # 3. Save questions in DB
        InterviewRepository.save_questions(
            db=db,
            session_id=session.id,
            questions="what is python?"
        )

        return {
            "session_id": session.id,
            "first_question": "what is python?"
        }

interview_service = InterviewService()