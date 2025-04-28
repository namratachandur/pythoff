def play_music_quiz():
    print("Welcome to the Music Quiz!")
    print("Choose a decade:")
    print("1970s")
    print("1980s")
    print("1990s")
    print("2000s")
    print("2010s")
    print("2020s")
    decade_choice = input()

    if decade_choice not in ['1970s', '1980s', '1990s', '2000s', '2010s', '2020s']:
        print("Invalid choice. Please select a decade from the list.")
        return
    
    print(f"\nYou chose the {decade_choice}!")
    print("Let's play!")
    score = 0

    if decade_choice == '1970s':
        print("\nQuestion 1: Who sang 'Hotel California'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "eagles":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Eagles.")

        print("\nQuestion 2: What is the title of the famous disco song by the Bee Gees?")
        answer = input("Your answer: ").strip().lower()
        if answer == "stayin' alive":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Stayin' Alive.")

        print("\nQuestion 3: Who sang 'Ain't No Sunshine'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "bill withers":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Bill Withers.")

        print("\nQuestion 4: What is the song that features the lyrics 'Do you remember the 21st night of September'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "september":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is September.")

        print("\nQuestion 5: Who is known as the 'Queen of Disco'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "donna summer":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Donna Summer.")

        print("\nQuestion 6: Highway to Hell is a song by which band?")
        answer = input("Your answer: ").strip().lower()
        if answer == "ac/dc":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is AC/DC.")

        print("\nQuestion 7: Gladys Knight & the Pips most famous song 'Midnight Train to Georgia' was released in which year?")
        answer = input("Your answer: ").strip().lower()
        if answer == "1973":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 1973.")

        print("\nQuestion 8: What song by Queen is an operatic rock anthem?")
        answer = input("Your answer: ").strip().lower()
        if answer == "bohemian rhapsody":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Bohemian Rhapsody.")

        print("\nQuestion 9: Stevie Wonder's 'You Are the Sunshine of My Life' was released in which year?")
        answer = input("Your answer: ").strip().lower()
        if answer == "1972":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 1972.")

        print("\nQuestion 10: 'Just the Way You Are' is a song by which artist?")
        answer = input("Your answer: ").strip().lower()
        if answer == "billy joel":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Billy Joel.")

    elif decade_choice == '1980s':
        print("\nQuestion 1: What is the title of Whitney Houston's famous song released in 1987?")
        answer = input("Your answer: ").strip().lower()
        if answer == "i wanna dance with somebody":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is I Wanna Dance with Somebody.")

        print("What is the title of Journey's famous song released in 1981?")
        answer = input("Your answer: ").strip().lower()
        if answer == "don't stop believin'":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Don't Stop Believin'.")

        print("\nQuestion 3: Who sang the famous meme song 'Never Gonna Give You Up'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "rick astley":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Rick Astley.")

        print("\nQuestion 4: 'Livin' on a Prayer' is a song by which band?")
        answer = input("Your answer: ").strip().lower()
        if answer == "bon jovi":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Bon Jovi.")

        print("\nQuestion 5: The Police's 'Every Breath You Take' was released in which year?")
        answer = input("Your answer: ").strip().lower()
        if answer == "1983":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 1983.")
        
        print("\nQuestion 6: What is the title of Michael Jackson's album featuring songs like 'Billie Jean' and 'Beat It'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "thriller":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Thriller.")

        print("\nQuestion 7: Madonna's 'Material Girl' was released in which year?")
        answer = input("Your answer: ").strip().lower()
        if answer == "1984":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 1984.")

        print("\nQuestion 8: Who sang 'Hungry Like the Wolf'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "duran duran":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Duran Duran.")

        print("\nQuestion 9: What is the title of Earth, Wind & Fire's famous song released in 1981??")
        answer = input("Your answer: ").strip().lower()
        if answer == "let's groove":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Let's Groove.")

        print("\nQuestion 10: 'Wake me up before you go-go' is a song by which band?")
        answer = input("Your answer: ").strip().lower()
        if answer == "wham!":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Wham!.")

    elif decade_choice == '1990s':
        print("\nQuestion 1: Who sang 'Damn I Wish I Was Your Lover', the 1992 hit?")
        answer = input("Your answer: ").strip().lower()
        if answer == "sophie b. hawkins" or answer == "sophie hawkins":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Sophie B. Hawkins.")

        print("\nQuestion 2: What is the title of the famous song by New Radicals released in 1998?")
        answer = input("Your answer: ").strip().lower()
        if answer == "you get what you give":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is You Get What You Give.")

        print("\nQuestion 3: The 1992 single 'Baby Got Back' was released by which rapper/songwriter?")
        answer = input("Your answer: ").strip().lower()
        if answer == "sir mix-a-lot" or answer == "sir mix a lot":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Sir Mix-A-Lot.")

        print("\nQuestion 4: What is the title of the 1993 'anthem for the neighborhood girl' song by Bikini Kill?")
        answer = input("Your answer: ").strip().lower()
        if answer == "rebel girl":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Rebel Girl.")
        
        print("\nQuestion 5: 'No Diggity' is a song by which R&B group?")
        answer = input("Your answer: ").strip().lower()
        if answer == "blackstreet":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Blackstreet.")

        print("\nQuestion 6: What is the title of the 1991 hit by Nirvana?")
        answer = input("Your answer: ").strip().lower()
        if answer == "smells like teen spirit":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Smells Like Teen Spirit.")

        print("\nQuestion 7: Who sang 'I Will Always Love You' in 1992?")
        answer = input("Your answer: ").strip().lower()
        if answer == "whitney houston":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Whitney Houston.")

        print("\nQuestion 8: The Goo Goo Dolls' 'Iris' was released in which year?")
        answer = input("Your answer: ").strip().lower()
        if answer == "1998":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 1998.")

        print("\nQuestion 9: 'Always Be My Baby' is a song by which artist?")
        answer = input("Your answer: ").strip().lower()
        if answer == "mariah carey":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Mariah Carey.")

        print("\nQuestion 10: 'Enter Sandman' is a song by which band?")
        answer = input("Your answer: ").strip().lower()
        if answer == "metallica":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Metallica.")

    elif decade_choice == '2000s':
        print("\nQuestion 1: Who released 'Family Affair' in 2001?")
        answer = input("Your answer: ").strip().lower()
        if answer == "mary j. blige" or answer == "mary j blige":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Mary J. Blige.")

        print("\nQuestion 2: What is the title of the 2000 hit by Britney Spears?")
        answer = input("Your answer: ").strip().lower()
        if answer == "oops!... i did it again":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Oops!... I Did It Again.")

        print("\nQuestion 3: What is the title of Backsteet Boys' 2000 hit?")
        answer = input("Your answer: ").strip().lower()
        if answer == "shape of my heart":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Shape of My Heart.")

        print("\nQuestion 4: 'Seven Nation Army' is a song by which rock duo?")
        answer = input("Your answer: ").strip().lower()
        if answer == "the white stripes":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is The White Stripes.")

        print("\nQuestion 5: Lady Gaga's 'Poker Face' was released in which year?")
        answer = input("Your answer: ").strip().lower()
        if answer == "2008":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 2008.")

        print("\nQuestion 6: 'Umbrella' by Rihanna is featuring which other major artist?")
        answer = input("Your answer: ").strip().lower()
        if answer == "jay-z":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Jay-Z.")

        print("\nQuestion 7: Coldplay's 'Viva La Vida' was released in which year?")
        answer = input("Your answer: ").strip().lower()
        if answer == "2008":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 2008.")

        print("\nQuestion 8: What is the title of the famous song by Green Day released in 2004?")
        answer = input("Your answer: ").strip().lower()
        if answer == "boulevard of broken dreams" or answer == "american idiot":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Boulevard of Broken Dreams or American Idiot.")

        print("\nQuestion 9: The Shins's 'New Slang' was released in which year?")
        answer = input("Your answer: ").strip().lower()
        if answer == "2001":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 2001.")

        print("\nQuestion 10: 'All the Single Ladies' is a song by which artist?")
        answer = input("Your answer: ").strip().lower()
        if answer == "beyoncé":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Beyoncé.")

    elif decade_choice == '2010s':
        print("\nQuestion 1: Who sang 'Rolling in the Deep' in 2010?")
        answer = input("Your answer: ").strip().lower()
        if answer == "adele":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Adele.")

        print("\nQuestion 2: What is the title of the famous song by Pharrell Williams released in 2013?")
        answer = input("Your answer: ").strip().lower()
        if answer == "happy":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Happy.")

        print("\nQuestion 3: 'Uptown Funk' is a song by which artist?")
        answer = input("Your answer: ").strip().lower()
        if answer == "bruno mars":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Bruno Mars.")

        print("\nQuestion 4: What is the title of Linkin Park's album released in 2010?")
        answer = input("Your answer: ").strip().lower()
        if answer == "a thousand suns":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is A Thousand Suns.")

        print("\nQuestion 5: Ed Sheeran's 'Shape of You' was released in which year?")
        answer = input("Your answer: ").strip().lower()
        if answer == "2017":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 2017.")

        print("\nQuestion 6: 'Tik Tok' is a song by which artist?")
        answer = input("Your answer: ").strip().lower()
        if answer == "kesha":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Kesha.")

        print("\nQuestion 7: 'Love the Way You Lie' features which two artists?")
        answer = input("Your answer: ").strip().lower()
        if "eminem" and "rihanna" in answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Eminem and Rihanna.")

        print("\nQuestion 8: 'Counting Stars' is a song by which band?")
        answer = input("Your answer: ").strip().lower()
        if answer == "one republic":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is One Republic.")

        print("\nQuestion 9: Which artist made a comeback by collaborating with Lil Nas X to release 'Old Town Road' in 2019?")
        answer = input("Your answer: ").strip().lower()
        if answer == "billy ray cyrus":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Billy Ray Cyrus.")

        print("\nQuestion 10: 'Closer' is a song by which duo?")
        answer = input("Your answer: ").strip().lower()
        if answer == "the chainsmokers":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is The Chainsmokers.")

    elif decade_choice == '2020s':
        print("\nQuestion 1: Who sang 'Blinding Lights' in 2020?")
        answer = input("Your answer: ").strip().lower()
        if answer == "the weeknd":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is The Weeknd.")

        print("\nQuestion 2: What is the title of Olivia Rodrigo's debut single released in 2021?")
        answer = input("Your answer: ").strip().lower()
        if answer == "drivers license":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Drivers License.")

        print("\nQuestion 3: 'Watermelon Sugar' is a song by which artist?")
        answer = input("Your answer: ").strip().lower()
        if answer == "harry styles":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Harry Styles.")

        print("\nQuestion 4: What is the title of BTS's hit song released in 2020?")
        answer = input("Your answer: ").strip().lower()
        if answer == "dynamite":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Dynamite.")

        print("\nQuestion 5: 'Stay' is a collaboration between which two artists?")
        answer = input("Your answer: ").strip().lower()
        if "the kid laroi" and "justin bieber" in answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is The Kid Laroi and Justin Bieber.")

        print("\nQuestion 6: 'Good 4 U' is a song by which artist?")
        answer = input("Your answer: ").strip().lower()
        if answer == "olivia rodrigo":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Olivia Rodrigo.")

        print("\nQuestion 7: 'abcdefu' is a song by which artist?")
        answer = input("Your answer: ").strip().lower()
        if answer == "gayeon":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Gayeon.")

        print("\nQuestion 8: Chappell Roan's 'Red Wine' was released in which year?")
        answer = input("Your answer: ").strip().lower()
        if answer == "2023":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 2023.")

        print("\nQuestion 9: 'As It Was' is a song by which artist?")
        answer = input("Your answer: ").strip().lower()
        if answer == "harry styles":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Harry Styles.")

        print("\nQuestion 10: 'Bad Habits' is a song by which artist?")
        answer = input("Your answer: ").strip().lower()
        if answer == "ed sheeran":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Ed Sheeran.")

    print(f"\nYour score is {score} out of 10 (i.e., {score * 10}%).")
    if score >= 7:
        print("Great job! You're a music wizz!")
    else:
        print("Better luck next time!")
    
    print("Thanks for playing the Music Quiz!")
