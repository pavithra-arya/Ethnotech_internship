import random

songs = [
    "Perfect - Ed Sheeran",
    "All of Me - John Legend",
    "Tum Hi Ho - Arijit Singh",
    "Just the Way You Are - Bruno Mars",
    "Raataan Lambiyan - Jubin Nautiyal"
]

def get_songs():
    return random.sample(songs, 3)
