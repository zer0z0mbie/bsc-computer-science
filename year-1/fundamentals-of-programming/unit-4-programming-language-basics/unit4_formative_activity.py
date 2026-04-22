score = 0

question1 = "What is 8 + 9? "
question2 = "What is 100 / 25? "
question3 = "What is 7 * 12? "

answer1 = input(f"{question1}")
if answer1 == "17":
    score += 1
    print("Correct answer!")
else:
    print("Incorrect answer. The correct answer is 17.")

answer2 = input(f"{question2}")
if answer2 == "4":
    score += 1
    print("Correct answer!")
else:
    print("Incorrect answer. The correct answer is 4.")

answer3 = input(f"{question3}")
if answer3 == "84":
    score += 1
    print("Correct answer!")
else:
    print("Incorrect answer. The correct answer is 84.")

if score == 1:
    print(f"You got {score} point out of 3.")
else:
    print(f"You got {score} points out of 3.")