import random

songs = [
    "Someone Like You - Adele",
    "Let Her Go - Passenger",
    "Fix You - Coldplay",
    "All I Want - Kodaline",
    "Stay With Me - Sam Smith"
]

def get_songs():
    return random.sample(songs, 3)
