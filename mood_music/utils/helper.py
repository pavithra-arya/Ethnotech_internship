def display_songs(song_list):
    print("\n🎵 Suggested Songs:\n")
    for index, song in enumerate(song_list, start=1):
        print(f"{index}. {song}")
