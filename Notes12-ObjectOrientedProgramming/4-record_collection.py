# A docstring is a "documentation string". It is a type of comment used to describe what a class/function does, not how.
# Aim to be concise in your documentation—don't compromise on information, but avoid taking unnecessary space.

# Docstrings are used by the help() function and the .__doc__ attribute, among other things, as documentation which
# can be pulled directly from your class or function


class Song:
    """
    Class to represent a song.

    Attributes:
        title (str): title of the song
        artist (Artist): An artist object representing the song's creator
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        """Song init method"""

        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """
    Class to represent an album, using its track list.

    Attributes:
        album_name (str): The name of the album
        year (int): The year the album was released
        artist (Artist): The artist responsible for the album.
            If not specified, the artist will default to an artist with the name "Various Artists".
        tracks (List[Song]): A list of songs on the album.

    Methods:
        add_song: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=Artist("Various Artists")):
        """Album init method"""
        self.name = name
        self.year = year
        self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """
        Adds a song to the track list.

        Args:
            song (Song): The song being added.
            position (Optional[int]): If specified, the song will be added at that index of the track list;
                inserting between other songs if necessary.
                Otherwise, the song will be added to the end of the list.
        """

