import random

quiz = [
      {
            'question': '1 + 1 = ?',
            'options' : ['A. 1', 'B. 2', 'C. 3', 'D. 4'],
            'answer'  : 'B'
      },
      {
            'question': '2 + 2 = ?',
            'options': ['A. 1', 'B. 2', 'C. 3', 'D. 4'],
            'answer': 'D'
      },
      {
            'question': '2 - 1 = ?',
            'options': ['A. 1', 'B. 2', 'C. 3', 'D. 4'],
            'answer': 'A'
      }
]

random.shuffle(quiz)
score = 0

for index, item in enumerate(quiz):
      print(f'Question {index + 1}: {item['question']}')
      for option in item['options']:
            print(option)

      user_answer = input('Your answer: ').upper().strip()

      if user_answer == item['answer']:
            print('\033[32mCorrect\033[0m')
            score += 1
      else:
            print(f'\033[31mWrong\033[0m! The correct answer is {item['answer']}')

print(f'Quiz over! Your score is {score} out of {len(quiz)} ' )