def play_shows_quiz():
    print("Welcome to the Shows Quiz!")
    genre = input("Choose a genre (Action, Comedy, Drama): ").strip().lower()
    
    if genre not in ["action", "comedy", "drama"]:
        print("Invalid genre. Please choose from Action, Comedy, or Drama.")
        return
    
    print(f"\nYou chose {genre.capitalize()}!")
    print("Let's start!")
    score = 0

    if genre == "action":
        print("\nQuestion 1: Which show features a chemistry teacher who turns to cooking meth?")
        answer = input("Your answer: ").strip().lower()
        if answer == "breaking bad":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Breaking Bad.")
        
        print("\nQuestion 2: What is the name of The Mandalorian's little green companion?")
        answer = input("Your answer: ").strip().lower()
        if answer == "grogu":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Grogu.")
        
        print("\nQuestion 3: What is the name of the tv show about Oliver Queen, the DC character?")
        answer = input("Your answer: ").strip().lower()
        if answer == "arrow":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Arrow.")

        print("\nQuestion 4: What is the name of the 'superhero' girl in Stranger Things?")
        answer = input("Your answer: ").strip().lower()
        if answer == "el" or answer == "eleven":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Eleven.")

        print("\nQuestion 5:Who hunts supernatural creatures with his brother Sam?")
        answer = input("Your answer: ").strip().lower()
        if answer == "dean winchester" or answer == "dean":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Dean Winchester.")

        print("\nQuestion 6: Which TV show features a blind superhero named Matt Murdock?")
        answer = input("Your answer: ").strip().lower()
        if answer == "daredevil":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Daredevil.")

        print("\nQuestion 7: Which Netflix series has a female assassin named Villanelle?")
        answer = input("Your answer: ").strip().lower()
        if answer == "killing eve":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Killing Eve.")

        print("\nQuestion 8: Who plays Jack Ryan working as a CIA analyst-turned-field agent?")
        answer = input("Your answer: ").strip().lower()
        if answer == "john krasinski":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is John Krasinski.")
        
        print("\nQuestion 9: What is the name of the mutated fungus in the tv show 'The Last of Us'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "cordyceps":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Cordyceps.")

        print("\nQuestion 10: Who is the main characted in the Netflix show 'The Sandman'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "dream":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Dream.")

    elif genre == "comedy":
        print("\nQuestion 1: What's the name of the boss in 'The Office'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "michael scott":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Michael Scott.")

        print("\nQuestion 2: Which actor plays the character of Barney in 'How I Met Your Mother'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "neil patrick harris" or answer == "nph":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Neil Patrick Harris.")

        print("\nQuestion 3: Which show features a comedy duo named Oscar and Felix?")
        answer = input("Your answer: ").strip().lower()
        if answer == "the odd couple":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is The Odd Couple.")
        
        print("\nQuestion 4: What is the name of the animated show featuring a talking dog named Brian?")
        answer = input("Your answer: ").strip().lower()
        if answer == "family guy":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Family Guy.")

        print("\nQuestion 5: Which dark comedy show feautes a despressed horse?")
        answer = input("Your answer: ").strip().lower()
        if answer == "bojack horseman":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Bojack Horseman.")
        
        print("\nQuestion 6: What is the name of the character played by Jennifer Aniston in 'Friends'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "rachel green" or answer == "rachel":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Rachel Green.")

        print("\nQuestion 7: In The Simpsons, what is the name of the bartender who owns Moe's Tavern?")
        answer = input("Your answer: ").strip().lower()
        if answer == "moe szyslak":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Moe Szyslak.")

        print("\nQuestion 8: What kind of animal is Ross's pet 'Friends'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "monkey":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Monkey.")

        print("\nQuestion 9: What's the name of the dark comedy written by Ricky Gervais about a man who loses his wife to cancer?")
        answer = input("Your answer: ").strip().lower()
        if answer == "after life":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is After Life.")

        print("\nQuestion 10: What is the name of Mitchell and Cam's daughter in 'Modern Family'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "lily":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Lily.")

    elif genre == "drama":
        print("\nQuestion 1: What show features an autistic surgeon?")
        answer = input("Your answer: ").strip().lower()
        if answer == "the good doctor":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is The Good Doctor.")

        print("\nQuestion 2: Who plays Harvey Specter in 'Suits'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "gabriel macht":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Gabriel Macht.")
        
        print("\nQuestion 3: Who is House's best friend in 'House MD'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "james wilson":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is James Wilson.")

        print("\nQuestion 4: Who is Rory's boyfriend in season 7 of 'Gilmore Girls'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "logan" or answer == "logan huntzberger":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Logan Huntzberger.")

        print("\nQuestion 5: In 'Stranger Things', what is the name of the parallel universe?")
        answer = input("Your answer: ").strip().lower()
        if answer == "the upside down":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is The Upside Down.")

        print("\nQuestion 6: In 'Euphoria', what is the name of the main character played by Zendaya?")
        answer = input("Your answer: ").strip().lower()
        if answer == "Rue" or answer == "rue bennett":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Rue.")

        print("\nQuestion 7: Which show follows the Roy family, owners of a media conglomerate?")
        answer = input("Your answer: ").strip().lower()
        if answer == "succession":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Succession.")

        print("\nQuestion 8: Who is Lucifer Morningstar's brother in 'Lucifer'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "amenadiel":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Amenadiel.")

        print("\nQuestion 9: Which high school drama revolves around a suicide and cassette tapes?")
        answer = input("Your answer: ").strip().lower()
        if answer == "13 reasons why":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 13 Reasons Why")

        print("\nQuestion 10: Who plays Javier Peña in 'Narcos'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "pedro pascal":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Pedro Pascal")

    print(f"\nYour score is {score} out of 10 (i.e., {score * 10}%).")
    if score >= 7:
        print("Great job! You're a shows whiz!")
    else:
        print("Better luck next time!")
    
    print("Thanks for playing the Shows Quiz!")
    
