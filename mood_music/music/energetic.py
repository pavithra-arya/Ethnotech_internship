import random

songs = [
    "Believer - Imagine Dragons",
    "Stronger - Kanye West",
    "Eye of the Tiger - Survivor",
    "Thunder - Imagine Dragons",
    "Power - Kanye West"
]

def get_songs():
    return random.sample(songs, 3)
