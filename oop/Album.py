class Song:
    """
    This class to represent song
    """

    def __init__(self, title, artist, duration=0):
        """
        Album init method
        title: title of the song display
        artist: song creator
        duration: length of the song in minutes
        """
        self.album = title
        self.artist = artist
        self.duration = duration


class Album:
    """
    This class to represent album
    name(str): name of the album
    year(int): song was made in year
    artist(str): if artist name is not present print as "various artist"
    position(int): position of the song in the list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artist")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)
