albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

# for album, artist, year, song in albums:
#     print(f"Album: {album}\t Arist: {artist}\t year: {year}\t songs: {song}")
# #
# song = albums[1][3][5][1]
# print(song)
#
# year = albums[2][2]
# print("Year of NightFlight release: ", year)
#
# track_no = albums[len(albums)-1][3][3][0]
# print(f"Track no of Kentish Town Waltz: {track_no}")
#
# for album in albums:
#     album_name, arist, year, songs = album
#     for song in songs:
#         if "Keeping a Rendezvous" in song:
#             print(f"Found in album: {album_name}")
