from nested_tuple import albums

while True:
    print("Select the album to play song: ")
    for index, (album, artist, year, songs) in enumerate(albums):
        print(f"{index+1}, {album}")
    choice = int(input())
    if 1 <= choice <= len(albums):
        print(f"selected ablbum {albums[choice][0]}")
        print("Select songs to play: ")
    else:
        break
    for track_index, (track_no, song) in enumerate(albums[choice+1][3]):
        print(f"{track_index + 1}, {song}")
    song_choice = int(input())
    if 1 <= song_choice <= len(songs):
        print(f"your now playing song: {songs[song_choice]}\n sit back and enjoy the music")
    else:
        break
