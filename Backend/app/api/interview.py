from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.interview_schema import StartInterviewRequest
# from app.services.session_service import interview_service
# from app.services.question_service import get_next_question
# from app.services.evaluation_service import submit_answer, get_final_feedback
from app.services.session_service import interview_service
from app.services.question_service import QuestionService


router = APIRouter(prefix="/interviews")


@router.post("/api/questions/generate")
def generate_questions(
    request: StartInterviewRequest,
    db: Session = Depends(get_db)
):
    session_data = interview_service.start_interview(
        db=db,
        user_id=request.user_id,
        topic=request.topic,
        tag=request.tag
    )

    return {
        "session_id": session_data["session_id"],
        "first_question": session_data["first_question"]
    }


# app/api/question.py

router = APIRouter(prefix="/api/questions")


@router.get("/next/{session_id}")
def get_next_question(session_id: int, db: Session = Depends(get_db)):
    return QuestionService.get_next_question(session_id, db)















































# @router.post("/start/next_question")

# @router.post("/interview/answer")
# def answer_question(request: AnswerRequest):
#     result = submit_answer(
#         request.session_id,
#         request.answer
#     )

#     if not result:
#         raise HTTPException(status_code=404, detail="Session not found")

#     return result


# @router.get("/{question_id}", response_model=QuestionResponse)
# def get_question(question_id: int, db: Session = Depends(get_db)):
    
#     question = db.query(Question_Bank).filter(
#         Question_Bank.id == question_id
#     ).first()

#     if not question:
#         raise HTTPException(status_code=404, detail="Question not found")

#     return question

# # @router.get("/interview/{session_id}/feedback")
# # def feedback(session_id: int):
# #     result = get_final_feedback(session_id)

# #     if not result:
# #         raise HTTPException(status_code=404, detail="Session not found")

# #     return result