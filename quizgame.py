questions = [
    {
        "prompt": "What is the capital of France? ",
        "answer": "Paris"
    },
    {
        "prompt": "Who painted the Mona Lisa? ",
        "answer": "Leonardo da Vinci"
    },
    {
        "prompt": "What is the largest planet in our solar system? ",
        "answer": "Jupiter"
    }
]

score = 0

for question in questions:
    user_answer = input(question["prompt"])
    if user_answer.lower() == question["answer"].lower():
        score += 1

print("Quiz completed!")
print("Your score is:", score, "/", len(questions))
