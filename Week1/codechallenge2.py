# Simple Quiz Game 🎮
# Create a multiple-choice quiz with questions about Python, movies, or any fun topic! Display scores at the end and allow the user to play again.
#Multiple choice questions with answers
# Simple Quiz Game 🎮
# Create a multiple-choice quiz with questions about Python, movies, or any fun topic! Display scores at the end and allow the user to play again.
# Multiple choice questions with answers

# Question 1
question1 = "What is the keyword used to define a function in Python?"
options1 = ["1. def", "2. function", "3. func", "4. define"]
correct_answer1 = 1

# Question 2
question2 = "Which of the following is not a Python data type?"
options2 = ["1. list", "2. tuple", "3. dictionary", "4. array"]
correct_answer2 = 4

# Question 3
question3 = "Which operator is used for exponentiation in Python?"
options3 = ["1. ^", "2. **", "3. //", "4. %"]
correct_answer3 = 2

# Question 4
question4 = "How do you create a list in Python?"
options4 = ["1. list = ()", "2. list = []", "3. list = {}", "4. list = <>"]
correct_answer4 = 2

# Keep track of the score
score = 0

# Question 1
print("Question 1: ", question1)
for option in options1:
    print(option)
answer1 = int(input("Choose the correct option (1-4): "))
if answer1 == correct_answer1:
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 2
print("\nQuestion 2: ", question2)
for option in options2:
    print(option)
answer2 = int(input("Choose the correct option (1-4): "))
if answer2 == correct_answer2:
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 3
print("\nQuestion 3: ", question3)
for option in options3:
    print(option)
answer3 = int(input("Choose the correct option (1-4): "))
if answer3 == correct_answer3:
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 4
print("\nQuestion 4: ", question4)
for option in options4:
    print(option)
answer4 = int(input("Choose the correct option (1-4): "))
if answer4 == correct_answer4:
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Display the final score
print(f"\nYour final score is: {score}/4 🏆")
