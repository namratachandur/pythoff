from playquiz import play_quiz

topics = ["Science", "Movies", "Geography", "Books", "Music", "Shows"]

print("\nWelcome to my quiz game!")
print("\nDo you want to play?")
choice = input()

if choice.lower() != "yes":
    print("\nOkay, bye!")
    exit()

else:
    print("Okay! Let's play!")
    print("\nChoose a topic to get quizzed on!")
    for i in range(len(topics)):
        print(f"{i + 1}. {topics[i]}")
    chosen_topic = input()

    for i in range(len(topics)):
        if chosen_topic.lower() == topics[i].lower():
            chosen_topic = topics[i]
            break

    print(f"\nYou chose {chosen_topic.capitalize()}!")

if chosen_topic not in topics:
    print("\nPick one from the list pleasee :(")

play_quiz(chosen_topic)