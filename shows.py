def play_shows_quiz():
    print("Welcome to the Shows Quiz!")
    genre = input("Choose a genre (Action, Comedy, Drama, Horror): ").strip().lower()
    
    if genre not in ["action", "comedy", "drama", "horror"]:
        print("Invalid genre. Please choose from Action, Comedy, Drama, or Horror.")
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
        print("\nQuestion 1: What's the kid's name in Home Alone?")
        answer = input("Your answer: ").strip().lower()
        if answer == "kevin":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Kevin.")

        print("\nQuestion 2: Which actor plays the character of Ace Ventura?")
        answer = input("Your answer: ").strip().lower()
        if answer == "jim carrey":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Jim Carrey.")

        print("\nQuestion 3: Whose job does Bruce take in Bruce Almighty?")
        answer = input("Your answer: ").strip().lower()
        if answer == "god's":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is God's.")
        
        print("\nQuestion 4: What is the name of the ghost-hunting group in the 1984 comedy?")
        answer = input("Your answer: ").strip().lower()
        if answer == "ghostbusters":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Ghostbusters.")

        print("\nQuestion 5: Which movie features three guys who lose their friend at a wild bachelor party?")
        answer = input("Your answer: ").strip().lower()
        if answer == "the hangover":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is The Hangover.")
        
        print("\nQuestion 6: Who is the grumpy green creature who tries to steal Christmas?")
        answer = input("Your answer: ").strip().lower()
        if answer == "grinch":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Grinch.")

        print("\nQuestion 7: In Despicable Me, what are the little yellow creatures called?")
        answer = input("Your answer: ").strip().lower()
        if answer == "minions":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Minions.")

        print("\nQuestion 8: What kind of animal is Sid from Ice Age?")
        answer = input("Your answer: ").strip().lower()
        if answer == "sloth":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Sloth.")

        print("\nQuestion 9: What's the name of the group of kung fu fighters who help Po in Kung Fu Panda?")
        answer = input("Your answer: ").strip().lower()
        if answer == "furious five":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Furious Five.")

        print("\nQuestion 10: Who is Andy's favorite toy in Toy Story?")
        answer = input("Your answer: ").strip().lower()
        if answer == "woody":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Woody.")

    elif genre == "drama":
        print("\nQuestion 1: Who does Leonardo DiCaprio play in 'Once Upon a Time in Hollywood'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "rick dalton":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Rick Dalton.")

        print("\nQuestion 2: In which movie does Meryl Streep play a chef?")
        answer = input("Your answer: ").strip().lower()
        if answer == "julie and julia":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Julie and Julia.")
        
        print("\nQuestion 3: What is the name of the 2024 movie starring Andrew Garfield and Florence Pugh?")
        answer = input("Your answer: ").strip().lower()
        if answer == "we live in time":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is We Live in Time.")

        print("\nQuestion 4: What movie is the quote 'I'm the king of the world!' from?")
        answer = input("Your answer: ").strip().lower()
        if answer == "titanic":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Titanic.")

        print("\nQuestion 5: What movie is the quote 'I'm gonna make him an offer he can't refuse' from?")
        answer = input("Your answer: ").strip().lower()
        if answer == "the godfather":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is The Godfather.")

        print("\nQuestion 6: Who plays the lead role in 'The Pursuit of Happyness'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "will smith":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Will Smith.")

        print("\nQuestion 7: Who plays the lead role in 'Fight Club'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "brad pitt":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Brad Pitt.")

        print("\nQuestion 8: What movie is the quote 'Oh, Captain! My Captain!' from?")
        answer = input("Your answer: ").strip().lower()
        if answer == "dead poets society":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Dead Poets Society.")

        print("\nQuestion 9: What movie features a character named Andy Dufresne?")
        answer = input("Your answer: ").strip().lower()
        if answer == "the shawshank redemption":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is The Shawshank Redemption.")

        print("\nQuestion 10: In which movie do Steve Carell and Timothée Chalamet play father and son?")
        answer = input("Your answer: ").strip().lower()
        if answer == "beautiful boy":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Beautiful Boy.")

    elif genre == "horror":
        print("\nQuestion 1: What is the name of paranormal investigators in 'The Conjuring'?")
        answer = input("Your answer: ").strip().lower()
        if "ed warren" and "lorraine warren" in answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Ed and Lorraine Warren.")
        
        print("\nQuestion 2: What is the name of the haunted doll in 'The Conjuring'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "annabelle":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Annabelle.")

        print("\nQuestion 3: What is the name of the hotel in 'The Shining'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "overlook hotel":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Overlook Hotel.")

        print("\nQuestion 4: What is the name of the serial killer in 'Silence of the Lambs'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "Hannibal Lecter":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Hannibal Lecter.")
        
        print("\nQuestion 5: How many people die in 'The Babadook'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "zero" or answer == "0":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Zero.")
        
        print("\nQuestion 6: In which horror movie does the villian attack through dreams?")
        answer = input("Your answer: ").strip().lower()
        if answer == "a nightmare on elm street":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is A Nightmare on Elm Street.")
        
        print("\nQuestion 7: How often does the Purge happen in 'The Purge'?")
        answer = input("Your answer: ").strip().lower()
        if "yearly" in answer or "once a year" in answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is once a year.")
        
        print("\nQuestion 8: What horror movie features a William Shatner mask?")
        answer = input("Your answer: ").strip().lower()
        if answer == "halloween":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Halloween.")
        
        print("\nQuestion 9: What is the name of the demon in 'The Exorcist'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "pazuzu":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Pazuzu.")
        
        print("\nQuestion 10: What horror movie features a creepy doll named Chucky?")
        answer = input("Your answer: ").strip().lower()
        if answer == "child's play":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Child's Play.")

    print(f"\nYour score is {score} out of 10 (i.e., {score * 10}%).")
    if score >= 7:
        print("Great job! You're a movies whiz!")
    else:
        print("Better luck next time!")
    
    print("Thanks for playing the Movie Quiz!")
    