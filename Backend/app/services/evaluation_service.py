from app.services.rag_service import retrieve_context
from app.services.llm_service import evaluate_with_llm

feedback_db = {}


def evaluate_answer(session_id: int, question_id: int, question: str, answer: str):
    # Step 1: retrieve ideal knowledge
    context = retrieve_context(question)

    # Step 2: evaluate using LLM
    result = evaluate_with_llm(
        question=question,
        answer=answer,
        context=context
    )

    # Expected result format:
    # {"score": 8, "feedback": "Strong explanation of event loop"}

    feedback_db[session_id] = {
        "session_id": session_id,
        "question_id": question_id,
        "score": result["score"],
        "feedback": result["feedback"]
    }

    return feedback_db[session_id]


def get_feedback(session_id: int):
    return feedback_db.get(session_id)