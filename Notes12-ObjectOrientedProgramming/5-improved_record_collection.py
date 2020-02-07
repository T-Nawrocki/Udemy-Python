# A version of the record_collection program from the previous file, but with an improved load_data algorithm
# which accounts for datasets which aren't accurately ordered by artist.
# This is achieved by comparing the artist name read to the existing artist objects, and creating artist objects
# as they're read, rather than at artist boundaries.

class Song:
    """
    Class to represent a song.

    Attributes:
        title (str): title of the song
        artist (Artist): An artist object representing the song's creator
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """
    Class to represent an album, using its track list.

    Attributes:
        name (str): The name of the album
        year (int): The year the album was released
        artist (Artist): The artist responsible for the album.
            If not specified, the artist will default to an artist with the name "Various Artists".
        tracks (List[Song]): A list of songs on the album.

    Methods:
        add_song: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist:
            self.artist = artist
        else:
            self.artist = Artist("Various Artists")
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
        if position:
            self.tracks.insert(position, song)
        else:
            self.tracks.append(song)


class Artist:
    """
    Class to represent an Artist and store artist details

    Attributes:
        name (str): Name of the Artist.
        albums (List[Album]): List of the albums by this artist.
            List only includes albums in this collection—not exhaustive.

    Methods:
        add_album: Adds a new album to the albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """
        Adds a new album to the albums list.

        Args:
            album (Album): Album object to add to the list
                If the album is already present, it will not be added again. (TODO)
        """
        self.albums.append(album)


def find_object(field, object_list):
    """Check "object_list" to see if an object with "name" attribute equal to "field" exists, and return it if so."""
    for item in object_list:
        if item.name == field:
            return item
    return None  # returns None if there is no matching item


def load_data():
    """
    Loads data from albums.txt, parsing it into artist, album and song objects. Returns artist list.

    Data in albums.txt is formatted as (artist, album, year, song), tab separated.
    """

    current_artist = None
    current_album = None
    artist_list = []

    print("Loading music data...")

    with open("albums.txt", "r") as albums:
        for line in albums:
            # bind variables to the fields of each line (stripping new line char and splitting on tabs)
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)  # convert string value to int
            print(f"\t{artist_field}:{album_field}:{year_field}:{song_field}")

            # Creates an Artist object for the artists read from artist_field using the current_artist tracker.
            # If there is no current artist, create one.
            if current_artist is None:
                current_artist = Artist(artist_field)
                artist_list.append(current_artist)
            elif current_artist.name != artist_field:
                # If there is a current artist, retrieve artist object if there is one,
                # otherwise create a new artist object and add it to the artist list
                current_artist = find_object(artist_field, artist_list)
                if current_artist is None:
                    current_artist = Artist(artist_field)
                    artist_list.append(current_artist)
                current_album = None

            # Creates an Album object for the albums read from album_field using the current_album tracker.
            # Follows a very similar process to the current_artist assignment above.
            if current_album is None:
                current_album = Album(album_field, year_field, current_artist)
                current_artist.add_album(current_album)
            elif current_album.name != album_field:
                current_album = find_object(album_field, current_artist.albums)
                if current_album is None:
                    current_album = Album(album_field, year_field, current_artist)
                    current_artist.add_album(current_album)

            # Creates a new Song object, and adds it to current_album object
            current_song = Song(song_field, current_artist)
            current_album.add_song(current_song)

    print(f"A total of {len(artist_list)} artists were loaded.")
    print()
    print("=" * 40)
    print()
    return artist_list


def create_checkfile(artist_list):
    """Create a check file from the object data for comparison with the original file"""

    print("Creating checkfile...")

    with open("checkfile.txt", "w") as checkfile:

        for artist in artist_list:
            for album in artist.albums:
                for song in album.tracks:
                    print(f"{artist.name}\t{album.name}\t{album.year}\t{song.title}", file=checkfile)

    print("Checkfile created.")
    print()
    print("=" * 40)
    print()


if __name__ == '__main__':

    # loads data from albums.txt
    artists = load_data()
    create_checkfile(artists)



