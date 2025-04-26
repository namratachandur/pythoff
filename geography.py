def play_geography_quiz():
    print("Welcome to the Geography Quiz!")
    print("Let's play!") 
    score = 0

    print("\nQuestion 1: What is the capital of France?")
    answer = input("Your answer: ").strip().lower()
    if answer == "paris":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Paris.")

    print("\nQuestion 2: What is the largest continent?")
    answer = input("Your answer: ").strip().lower()
    if answer == "asia":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Asia.")
    
    print("\nQuestion 3: What is the longest river in the world?")
    answer = input("Your answer: ").strip().lower()
    if answer == "nile":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Nile.")

    print("\nQuestion 4: What is the smallest country in the world? (Hint: It is a city-state)")
    answer = input("Your answer: ").strip().lower()
    if answer == "vatican city":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Vatican City.")

    print("\nQuestion 5: What continent is Egypt in?")
    answer = input("Your answer: ").strip().lower()
    if answer == "africa":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Africa.")

    print("\nQuestion 6: What is the largest ocean on Earth?")
    answer = input("Your answer: ").strip().lower()
    if answer == "pacific":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Pacific.")

    print("\nQuestion 7: What is the capital of Japan?")
    answer = input("Your answer: ").strip().lower()
    if answer == "tokyo":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Tokyo.")

    print("\nQuestion 8: What is the capital of Israel?")
    answer = input("Your answer: ").strip().lower()
    if answer == "jerusalem":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Jerusalem.")

    print("\nQuestion 9: What is the capital of India?")
    answer = input("Your answer: ").strip().lower()
    if answer == "new delhi" or answer == "delhi":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is New Delhi.")
    
    print("\nQuestion 10: What continent is Brazil in?")
    answer = input("Your answer: ").strip().lower()
    if answer == "south america":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is South America.")

    print(f"\nYour score is {score} out of 10 (i.e., {score * 10}%).")
    if score >= 7:
        print("Great job! You're a geography whiz!")
    else:
        print("Better luck next time!")
    
    print("Thanks for playing the Geography Quiz!")