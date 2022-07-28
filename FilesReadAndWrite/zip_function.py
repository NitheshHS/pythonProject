albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

keys = ['album', 'artist', 'year']
album_dict = {}
for album in albums:
    for value in zip(keys, album):
        album_dict['str'] = album


for key, value in album_dict.items():
    print(key, value)

