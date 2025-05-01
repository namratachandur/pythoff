from playquiz import play_quiz

topics = ["Science", "Movies", "Geography", "Books", "Music", "Shows"]

def get_topic_choice():
    print("\nChoose a topic to get quizzed on!")
    for i, topic in enumerate(topics, start=1):
        print(f"{i}. {topic}")
    
    while True:
        choice = input("\nEnter the number or name of your chosen topic: ").strip()
        
        # Check if input is a valid number
        if choice.isdigit():
            choice_num = int(choice)
            if 1 <= choice_num <= len(topics):
                return topics[choice_num - 1]
        
        # Check if input matches a topic name (case-insensitive)
        for topic in topics:
            if choice.lower() == topic.lower():
                return topic
        
        print(f"Please choose a number between 1-{len(topics)} or one of the topic names.")

def main():
    print("\nWelcome to my quiz game!")
    print("\nDo you want to play? (yes/no)")
    
    while True:
        choice = input().strip().lower()
        if choice in ['yes', 'no']:
            break
        print("Please answer with 'yes' or 'no'")
    
    if choice != "yes":
        print("\nOkay, bye!")
        return
    
    print("\nOkay! Let's play!")
    chosen_topic = get_topic_choice()
    print(f"\nYou chose {chosen_topic}!")
    play_quiz(chosen_topic)

if __name__ == "__main__":
    main()
