import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question):
        print(question['question'])
        for i, option in enumerate(question['options'], 1):
            print(f"{i}. {option}")

        user_answer = input("Your answer (enter the number): ")
        return int(user_answer) == question['correct_answer']

    def run_quiz(self):
        for question in self.questions:
            if self.ask_question(question):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is: {question['options'][question['correct_answer'] - 1]}\n")

        print(f"Quiz completed! Your final score is: {self.score}/{len(self.questions)}")

def main():
    # Customize your quiz by modifying the questions, options, and correct answers.
    questions = [
        {
            'question': 'Which is the capital of India ?',
            'options': ['Chennai', 'Delhi', 'Banglore', 'Mumbai'],
            'correct_answer': 2
        },
        {
            'question': 'In which Planet we Live?',
            'options': ['Earth', 'Venus', 'Jupiter', 'Saturn'],
            'correct_answer': 1
        },
        {
            'question': 'Which programming language is known for its use in creating dynamic web pages ?',
            'options': ['Java', 'Javascript', 'Python', 'c'],
            'correct_answer': 2
        }
    ]

    # Shuffle the questions to make the quiz more dynamic
    random.shuffle(questions)

    # Create a Quiz instance and run the quiz
    quiz = Quiz(questions)
    quiz.run_quiz()

if __name__ == "__main__":
    main()
