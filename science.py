def play_science_quiz():
    print("Welcome to the Science Quiz!")
    
    choice = input("Choose a category: (1) Physics, (2) Chemistry, (3) Biology: ").strip().lower()
    if choice == '1':
        category = "Physics"
    
    elif choice == '2':
        category = "Chemistry"
    
    elif choice == '3':
        category = "Biology"

    else:
        print("Invalid choice. Please select a valid category.")
        return
    
    print(f"You have selected {category}!")
    print("Let's start!")
    score = 0

    if category == "Physics":
        print("\nQuestion 1: What famous equation did Albert Einstein develop?")
        answer = input("Your answer: ").strip().lower()
        if answer == "e=mc^2":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is E=mc^2.")
        
        print("\nQuestion 2: What is the force that keeps us on the ground?")
        answer = input("Your answer: ").strip().lower()
        if answer == "gravity":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is gravity.")

        print("\nQuestion 3: What is Newton's third law of motion?")
        answer = input("Your answer: ").strip().lower()
        if answer == "for every action, there is an equal and opposite reaction":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 'For every action, there is an equal and opposite reaction.'")

        print("\nQuestion 4: Why do astronauts float in space?")
        answer = input("Your answer: ").strip().lower()
        if answer == "there is no gravity" or answer == "vacuum":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 'There is no gravity.' or 'Vacuum.'")

        print("\nQuestion 5: What force does a body have when it is moving?")
        answer = input("Your answer: ").strip().lower()
        if answer == "kinetic energy":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 'Kinetic energy.'")

        print("\nQuestion 6: What force does a body have when it is at rest?")
        answer = input("Your answer: ").strip().lower()
        if answer == "potential energy":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 'Potential energy.'")

        print("\nQuestion 7: What colour is formed when all the colours of the rainbow are combined?")
        answer = input("Your answer: ").strip().lower()
        if answer == "white":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 'White.'")

        print("\nQuestion 8: What travels faster in vacuum: light or sound?")
        answer = input("Your answer: ").strip().lower()
        if answer == "light":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 'Light.'")

        print("\nQuestion 9: What is heavier: a ton of feathers or a ton of bricks?")
        answer = input("Your answer: ").strip().lower()
        if answer == "They're the same!":
            print("Correct!")
            score += 1
        else:
            print("Haha gotcha! They're the same!")
        
        print("\nQuestion 10: What is the process called when a solid turns into a liquid?")
        answer = input("Your answer: ").strip().lower()
        if answer == "melting":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 'Melting.'")

    elif category == "Chemistry":
        print("\nQuestion 1: What is the chemical formula for water?")
        answer = input("Your answer: ").strip().lower()
        if answer == "h2o":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is H2O.")
        
        print("\nQuestion 2: What is the pH level of pure water?")
        answer = input("Your answer: ").strip().lower()
        if answer == "7":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 7.")

        print("\nQuestion 3: What gas protects us from the sun's harmful rays?")
        answer = input("Your answer: ").strip().lower()
        if answer == "ozone":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Ozone.")
        
        print("\nQuestion 4: What is the chemical formula for table salt?")
        answer = input("Your answer: ").strip().lower()
        if answer == "nacl":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is NaCl.")
        
        print("\nQuestion 5: What happens when you put mentos in soda?")
        answer = input("Your answer: ").strip().lower()
        if answer == "it fizzes" or answer == "it explodes":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 'It fizzes.' or 'It explodes.'")

        print("\nQuestion 6: What is the table of elements called?")
        answer = input("Your answer: ").strip().lower()
        if answer == "periodic table":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 'Periodic table.'")

        print("\nQuestion 7: What is the most abundant gas in the Earth's atmosphere?")
        answer = input("Your answer: ").strip().lower()
        if answer == "nitrogen":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 'Nitrogen.'")

        print("\nQuestion 8: What is the chemical formula for carbon dioxide?")
        answer = input("Your answer: ").strip().lower()
        if answer == "co2":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is CO2.")

        print("\nQuestion 9: What is the name of the element with the symbol 'Fe'?")
        answer = input("Your answer: ").strip().lower()
        if answer == "iron" or answer == "ferrum":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 'Iron' or 'Ferrum' if you want to be fancy.")

        print("\nQuestion 10: What are the three states of matter?")
        answer = input("Your answer: ").strip().lower()
        if "solid" and "liquid" and "gas" in answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is 'Solid, Liquid, and Gas.'")

    elif category == "Biology":
        print("\nQuestion 1: What is the powerhouse of the cell?")
        answer = input("Your answer: ").strip().lower()
        if answer == "mitochondria":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Mitochondria.")
        
        print("\nQuestion 2: What organ is responsible for pumping blood?")
        answer = input("Your answer: ").strip().lower()
        if answer == "heart":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Heart.")
        
        print("\nQuestion 3: What is the basic unit of life?")
        answer = input("Your answer: ").strip().lower()
        if answer == "cell":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Cell.")
        
        print("\nQuestion 4: What is the process by which plants make their own food?")
        answer = input("Your answer: ").strip().lower()
        if answer == "photosynthesis":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Photosynthesis.")

        print("\nQuestion 5: What gives leaves their green color?")
        answer = input("Your answer: ").strip().lower()
        if answer == "chlorophyll":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Chlorophyll.")

        print("\nQuestion 6: What is the largest organ in the human body?")
        answer = input("Your answer: ").strip().lower()
        if answer == "skin":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Skin.")

        print("\nQuestion 7: What organ system is responsible for sending and receiving messages in the body?")
        answer = input("Your answer: ").strip().lower()
        if answer == "nervous system":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Nervous System.")

        print("\nQuestion 8: What organ system is responsible for digesting food?")
        answer = input("Your answer: ").strip().lower()
        if answer == "digestive system":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Digestive System.")

        print("\nQuestion 9: The three types of blood cells are red blood cells, white blood cells, and ______?")
        answer = input("Your answer: ").strip().lower()
        if answer == "platelets":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Platelets.")

        print("\nQuestion 10: What is the skeleton made of?")
        answer = input("Your answer: ").strip().lower()
        if answer == "bones":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is Bones.")

    print(f"\nYour score is {score} out of 10 (i.e., {score * 10}%).")
    if score >= 7:
        print("Great job! You're a science whiz!")
    else:
        print("Better luck next time!")
    
    print("Thanks for playing the Science Quiz!")