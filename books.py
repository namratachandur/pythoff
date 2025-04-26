def play_books_quiz():
    print("Welcome to the Books Quiz!")
    print("Let's play!") 
    score = 0

    print("\nQuestion 1: Who wrote 'To Kill a Mockingbird'?")
    answer = input("Your answer: ").strip().lower()
    if answer == "harper lee":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Harper Lee.")

    print("\nQuestion 2: What is the title of the final Harry Potter book?")
    answer = input("Your answer: ").strip().lower()
    if answer == "Harry Potter and the Deathly Hallows":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Harry Potter and the Deathly Hallows.")

    print("\nQuestion 3: Who is the author of '1984'?")
    answer = input("Your answer: ").strip().lower()
    if answer == "george orwell":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is George Orwell.")
    
    print("\nQuestion 4: What is the name of the main character in 'The Book Thief'?")
    answer = input("Your answer: ").strip().lower()
    if answer == "liesel meminger":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Liesel Meminger.")

    print("\nQuestion 5: Who wrote 'Pride and Prejudice'?")
    answer = input("Your answer: ").strip().lower()
    if answer == "jane austen":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Jane Austen.")

    print("\nQuestion 6: Who wrote 'Jane Eyre'?")
    answer = input("Your answer: ").strip().lower()
    if answer == "charlotte brontë" or answer == "charlotte bronte":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Charlotte Brontë.")

    print("\nQuestion 7: What book is the quote 'It was the best of times, it was the worst of times' from?")
    answer = input("Your answer: ").strip().lower()
    if answer == "a tale of two cities":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is A Tale of Two Cities.")

    print("\nQuestion 8: Who wrote 'Great Expectations'?")
    answer = input("Your answer: ").strip().lower()
    if answer == "charles dickens":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Charles Dickens.")

    print("\nQuestion 9: What series of books features a character named Katniss Everdeen?")
    answer = input("Your answer: ").strip().lower()
    if answer == "the hunger games":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is The Hunger Games.")

    print("\nQuestion 10: Who wrote 'The Catcher in the Rye'?")
    answer = input("Your answer: ").strip().lower()
    if answer == "j.d. salinger":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is J.D. Salinger.")


    print(f"\nYour score is {score} out of 10 (i.e., {score * 10}%).")
    if score >= 7:
        print("Great job! You're a reader!")
    else:
        print("Better luck next time!")
    
    print("Thanks for playing the Books Quiz!")