questions_db = {}


def generate_question(topic: str):
    question = f"Explain the concept of {topic} in detail."

    question_id = len(questions_db) + 1

    questions_db[question_id] = {
        "id": question_id,
        "topic": topic,
        "question": question
    }

    return questions_db[question_id]


def get_question(question_id: int):
    return questions_db.get(question_id)