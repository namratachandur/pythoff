def play_movies_quiz():
    print("\nWelcome to the Movies Quiz!")

    genre = input("Choose a genre (Action, Comedy, Drama, Horror): ").strip().lower()
    
    if genre not in ["action", "comedy", "drama", "horror"]:
        print("Invalid genre. Please choose from Action, Comedy, Drama, or Horror.")
        return
    
    print(f"\nYou chose {genre.capitalize()}!")
    print("Let's start!")
    score = 0

    if genre == "action":
        print("\nQuestion 1. Which actor is famous for playing Ethan Hunt in the Mission: Impossible series?")
        answer = input("Your answer: ").strip().lower()
        if answer == "tom cruise":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Tom Cruise.")
        
        print("\nQuestion 2. In which movie does a bus have to stay over 50 mph to avoid exploding?")
        answer = input("Your answer: ").strip().lower()
        if answer == "speed":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Speed.")
        
        print("\nQuestion 3. In which movie does Bruce Willis play a cop in a Los Angeles skyscraper?")
        answer = input("Your answer: ").strip().lower()
        if answer == "die hard":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Die Hard.")

        print("\nQuestion 4. Who plays John Wick - the unstoppable assassin?")
        answer = input("Your answer: ").strip().lower()
        if answer == "keanu reeves":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Keanu Reeves.")

        print("\nTime for some superhero questions!")
        print("\nQuestion 5. What superhero is also known as the 'Caped Crusader'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "batman":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Batman.")

        print("\nQuestion 6. Who is the Norse god of thunder?")
        answer = input("Your answer: ").strip().lower()
        if answer == "thor":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Thor.")

        print("\nQuestion 7. What planet is Superman from?")
        answer = input("Your answer: ").strip().lower()
        if answer == "krypton":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Krypton.")

        print("\nQuestion 8. How does Peter Parker become Spider-Man?")
        answer = input("Your answer: ").strip().lower()
        if "bitten" and "radioactive" and "spider" in answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is He was bitten by a radioactive spider.")
        
        print("\nQuestion 9. What is the name of the fictional African country in Black Panther?")
        answer = input("Your answer: ").strip().lower()
        if answer == "wakanda":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Wakanda.")

        print("\nQuestion 10. Who plays Joker in Christopher Nolan's The Dark Knight?")
        answer = input("Your answer: ").strip().lower()
        if answer == "heath ledger":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Heath Ledger.")

    elif genre == "comedy":
        print("\nQuestion 1. What's the kid's name in Home Alone?")
        answer = input("Your answer: ").strip().lower()
        if answer == "kevin":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Kevin.")

        print("\nQuestion 2. Which actor plays the character of Ace Ventura?")
        answer = input("Your answer: ").strip().lower()
        if answer == "jim carrey":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Jim Carrey.")

        print("\nQuestion 3. Whose job does Bruce take in Bruce Almighty?")
        answer = input("Your answer: ").strip().lower()
        if answer == "god's":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is God's.")
        
        print("\nQuestion 4. What is the name of the ghost-hunting group in the 1984 comedy?")
        answer = input("Your answer: ").strip().lower()
        if answer == "ghostbusters":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Ghostbusters.")

        print("\nQuestion 5. Which movie features three guys who lose their friend at a wild bachelor party?")
        answer = input("Your answer: ").strip().lower()
        if answer == "the hangover":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is The Hangover.")
        
        print("\nQuestion 6. Who is the grumpy green creature who tries to steal Christmas?")
        answer = input("Your answer: ").strip().lower()
        if answer == "grinch":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Grinch.")

        print("\nQuestion 7. In Despicable Me, what are the little yellow creatures called?")
        answer = input("Your answer: ").strip().lower()
        if answer == "minions":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Minions.")

        print("\nQuestion 8. What kind of animal is Sid from Ice Age?")
        answer = input("Your answer: ").strip().lower()
        if answer == "sloth":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Sloth.")

        print("\nQuestion 9. What's the name of the group of kung fu fighters who help Po in Kung Fu Panda?")
        answer = input("Your answer: ").strip().lower()
        if answer == "furious five":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Furious Five.")

        print("\nQuestion 10. Who is Andy's favorite toy in Toy Story?")
        answer = input("Your answer: ").strip().lower()
        if answer == "woody":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Woody.")