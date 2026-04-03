from pydantic import BaseModel, Field


class StartInterviewRequest(BaseModel):
    topic: str = Field(..., min_length=2, max_length=100)


class StartInterviewResponse(BaseModel):
    session_id: int
    question_id: int
    question: str


class EvaluationRequest(BaseModel):
    session_id: int
    question_id: int
    answer: str = Field(..., min_length=1)


class EvaluationResponse(BaseModel):
    score: int
    feedback: str
    next_question_id: int | None = None
    next_question: str | None = None
    completed: bool = False