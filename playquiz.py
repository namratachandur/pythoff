from science import play_science_quiz
from movies import play_movies_quiz
from geography import play_geography_quiz
from books import play_books_quiz
from music import play_music_quiz
from shows import play_shows_quiz

def play_quiz(topic):
    score = 0
    if topic == "Science":
        play_science_quiz()

    elif topic == "Movies":
        play_movies_quiz()
    
    elif topic == "Geography":
        play_geography_quiz()
    
    elif topic == "Books":
        play_books_quiz()
    
    elif topic == "Music":
        play_music_quiz()

    elif topic == "Shows":
        play_shows_quiz()