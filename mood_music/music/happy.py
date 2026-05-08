import random

songs = [
    "Happy - Pharrell Williams",
    "Uptown Funk - Bruno Mars",
    "Can't Stop The Feeling - Justin Timberlake",
    "On Top of the World - Imagine Dragons",
    "Best Day of My Life - American Authors"
]

def get_songs():
    return random.sample(songs, 3)
