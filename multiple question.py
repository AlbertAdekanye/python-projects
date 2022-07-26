from Question import Question
question_prompt = [
    "what color are apples\n?(a) Green/Red\n(b) purple\n(c) orange\n\n",
    "what color are banana\n?(a) Teal\n(b) magenta\n(c) yellow\n\n",
    "what color are strawberries\n?(a) yellow\n(b) blue\n(c) red\n\n",
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            print("you got: " + str(score) + "/" + str(len(questions)) + " correct: ")

run_test(questions)
