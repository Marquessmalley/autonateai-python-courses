
def ask_question(question, answer):
    """Ask a question and check if the answer is correct"""
    guess = input(question + " ")

    if(guess.lower() == answer.lower()):

        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False
    


score = 0;

questions = [("What is the capital of France?", "Paris"), ("What is 7 x 8?", "56"), ("What color is the sky", "Blue"), ]

for i, (question, answer) in enumerate(questions):
  if(ask_question(question, answer)):
    score += 1

print(f"🎉 Final Score:  {score /len(questions) * 100}%")
