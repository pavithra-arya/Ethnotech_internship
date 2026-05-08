from music import happy, sad, romantic, energetic
from utils.helper import display_songs


def suggest_songs(mood):
    mood = mood.lower()

    if mood == "happy":
        return happy.get_songs()
    elif mood == "sad":
        return sad.get_songs()
    elif mood == "romantic":
        return romantic.get_songs()
    elif mood == "energetic":
        return energetic.get_songs()
    else:
        return None


def main():
    print("🎶 Welcome to Mood-Based Song Recommender 🎶")
    print("Available Moods: Happy | Sad | Romantic | Energetic\n")

    mood = input("Enter your mood: ")

    songs = suggest_songs(mood)

    if songs:
        display_songs(songs)
    else:
        print("❌ Invalid mood entered.")


if __name__ == "__main__":
    main()
