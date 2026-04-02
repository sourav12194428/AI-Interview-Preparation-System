from fastapi import APIRouter, HTTPException
from app.schemas.interview_schema import (
    StartInterviewRequest,
    AnswerRequest
)
from app.services.session_service import create_session
from app.services.question_service import get_next_question
from app.services.evaluation_service import (
    submit_answer,
    get_final_feedback
)

router = APIRouter()


@router.post("/interview/start")
def start_interview(request: StartInterviewRequest):
    session = create_session(request.topic)

    return {
        "session_id": session["session_id"],
        "first_question": session["questions"][0]
    }


@router.post("/interview/answer")
def answer_question(request: AnswerRequest):
    result = submit_answer(
        request.session_id,
        request.answer
    )

    if not result:
        raise HTTPException(status_code=404, detail="Session not found")

    return result


@router.get("/interview/{session_id}/next-question")
def next_question(session_id: int):
    question = get_next_question(session_id)

    if not question:
        raise HTTPException(status_code=404, detail="Session not found")

    return question

@router.get("/interview/{session_id}/feedback")
def feedback(session_id: int):
    result = get_final_feedback(session_id)

    if not result:
        raise HTTPException(status_code=404, detail="Session not found")

    return result