questions = ("How many elements are in the periodic table?: ",
             "Witch animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: " ,
             "Witch planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")

guesses = []
score = 0
i = 0

for question in questions:
    print("************")
    print(question)

    for option in options[i]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[i]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT!")
        print(f"{answers[i]} is the correct answer.")
    
    i += 1

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
    
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

score = (int(score) / len(questions)  * 100)

print(f"Your score is: {score}%")