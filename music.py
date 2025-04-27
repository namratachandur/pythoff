def play_music_quiz():
    print("Welcome to the Music Quiz!")
    print("Choose a decade:")
    print("1. 1970s")
    print("2. 1980s")
    print("3. 1990s")
    print("4. 2000s")
    print("5. 2010s")
    print("6. 2020s")
    decade_choice = input()

    if decade_choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid choice. Please select a number between 1 and 6.")
        return
    
    print(f"\nYou chose the {decade_choice}!")

    if decade_choice == '1':
        print("\nQuestion 1: Who sang 'Hotel California'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "eagles":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is Eagles.")

        print("\nQuestion 2: What is the title of the famous disco song by the Bee Gees?")
        answer = input("Your answer: ").strip().lower()
        if answer == "stayin' alive":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is Stayin' Alive.")

        print("\nQuestion 3: Who sang 'Ain't No Sunshine'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "bill withers":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is Bill Withers.")

        print("\nQuestion 4: What is the song that features the lyrics 'Do you remember the 21st night of September'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "september":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is September.")

        print("\nQuestion 5: Who is known as the 'Queen of Disco'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "donna summer":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is Donna Summer.")

        print("\nQuestion 6: Highway to Hell is a song by which band?")
        answer = input("Your answer: ").strip().lower()
        if answer == "ac/dc":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is AC/DC.")

        print("\nQuestion 7: Gladys Knight & the Pips most famous song 'Midnight Train to Georgia' was released in which year?")
        answer = input("Your answer: ").strip().lower()
        if answer == "1973":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is 1973.")

        print("\nQuestion 8: What song by Queen is an operatic rock anthem?")
        answer = input("Your answer: ").strip().lower()
        if answer == "bohemian rhapsody":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is Bohemian Rhapsody.")

        print("\nQuestion 9: Stevie Wonder's 'You Are the Sunshine of My Life' was released in which year?")
        answer = input("Your answer: ").strip().lower()
        if answer == "1972":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is 1972.")

        print("\nQuestion 10: 'Just the Way You Are' is a song by which artist?")
        answer = input("Your answer: ").strip().lower()
        if answer == "billy joel":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is Billy Joel.")

    elif decade_choice == '2':
        print("\nQuestion 1: What is the title of Whitney Houston's famous song released in 1987?")
        answer = input("Your answer: ").strip().lower()
        if answer == "i wanna dance with somebody":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is I Wanna Dance with Somebody.")

        print("What is the title of Journey's famous song released in 1981?")
        answer = input("Your answer: ").strip().lower()
        if answer == "don't stop believin'":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is Don't Stop Believin'.")

        print("\nQuestion 3: Who sang the famous meme song 'Never Gonna Give You Up'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "rick astley":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is Rick Astley.")

        print("\nQuestion 4: 'Livin' on a Prayer' is a song by which band?")
        answer = input("Your answer: ").strip().lower()
        if answer == "bon jovi":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is Bon Jovi.")

        print("\nQuestion 5: The Police's 'Every Breath You Take' was released in which year?")
        answer = input("Your answer: ").strip().lower()
        if answer == "1983":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is 1983.")
        
        print("\nQuestion 6: What is the title of Michael Jackson's album featuring songs like 'Billie Jean' and 'Beat It'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "thriller":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is Thriller.")

        print("\nQuestion 7: Madonna's 'Material Girl' was released in which year?")
        answer = input("Your answer: ").strip().lower()
        if answer == "1984":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is 1984.")

        print("\nQuestion 8: Who sang 'Hungry Like the Wolf'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "duran duran":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is Duran Duran.")

        print("\nQuestion 9: What is the title of Earth, Wind & Fire's famous song released in 1981??")
        answer = input("Your answer: ").strip().lower()
        if answer == "let's groove":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is Let's Groove.")

        print("\nQuestion 10: 'Wake me up before you go-go' is a song by which band?")
        answer = input("Your answer: ").strip().lower()
        if answer == "wham!":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is Wham!.")