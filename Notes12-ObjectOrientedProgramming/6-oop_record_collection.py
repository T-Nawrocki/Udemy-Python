# The previous examples we've seen in files 4 and 5 *use* objects, but they are not *object oriented*.
# In other words, there's nothing particularly different about the way we coded them compared to how we coded
# things in previous sections of this course—we just defined our classes ourselves, but if they'd been part
# of the Python standard library, we wouldn't have needed to do anything different.

# OOP is more than just using objects, there are other key concepts involved as well:
#   ENCAPSULATION:  The principle that data and the methods that work on that data be wrapped in a single unit, and only
#                   the interfaces to that unit be exposed.
#   COMPOSITION:    One object has another object to which it delegates behaviour, in the same way that your body has
#                   arms and legs which perform certain tasks and are components of the whole that is the body.
#                   Composition can be thought of as aggregating objects so that one is an attribute of the other.
#   INHERITANCE:    One object extends another object; which is to say it *is* an object of the parent type, and
#                   inherits all the attributes and methods of that object, adding more of its own. Inheritance can
#                   be thought of as creating subtypes/subsets of existing objects.
#   DELEGATION:     A technique where certain methods of one object are automatically applied to another object. So
#                   for example, if you have a class A, you could create another class B which has certain methods which
#                   differ from A, but for all other methods you use the implementations already written in A. In this
#                   situation, B delegates those methods to A. In other words, delegation is when an object passes off
#                   a function to another object that's better suited to handle it.

# So an object oriented version of the record collection program would at least make more use of encapsulation
# and delegation (we'll deal with composition and inheritance more later in the course).
# For example, while we've encapsulated data pretty well, we've not encapsulated methods much at all.
# The load_data function was doing way too much outside of the objects for this to be properly object-oriented.
# Really, we should encapsulate the methods to parse and handle albums in the Artist class (which is best equipped to
# handle them, given it contains the album list for each artist), and similarly songs should be handled by the Album
# class (which contains the track list for each album).

# So in this version of the program, we've delegated most of the work required for the load_data function to the Artist
# and Album classes and their new methods.

# This version also removes the circular references from album to artist and artist to album,
# which is possible due to the new find_object function


class Song:
    """
    Class to represent a song.

    Attributes:
        name (str): title of the song
        artist (str): name of the song's creator
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, name, artist, duration=0):
        self.name = name
        self.artist = artist
        self.duration = duration


class Album:
    """
    Class to represent an album, using its track list.

    Attributes:
        name (str): The name of the album
        year (int): The year the album was released
        artist (str): Name of the artist responsible for the album.
            If not specified, the artist will default to "Various Artists".
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
            self.artist = "Various Artists"
        self.tracks = []

    def add_song(self, song, position=None):
        """
        Adds a song to the track list.

        Args:
            song (str): The title of the song being added.
            position (Optional[int]): If specified, the song will be added at that index of the track list;
                inserting between other songs if necessary.
                Otherwise, the song will be added to the end of the list.
        """
        song_found = find_object(song, self.tracks)
        if not song_found:
            song_found = Song(song, self.artist)
            if not position:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


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
        """
        self.albums.append(album)

    def add_song(self, album, year, title):
        """
        Add a new song to the collection of albums.

        This method will add the song to an album in the collection.
        A new album will be created in the collection if it doesn't already exist.

        Args:
            album (str): The name of the album.
            year (int): The year the album was produced.
            title (str): the title of the song.
        """

        album_found = find_object(album, self.albums)
        if not album_found:
            print(f"{album} not found.")
            album_found = Album(album, year, self.name)
            self.add_album(album_found)
        else:
            print(f"Found album {album}")

        album_found.add_song(title)


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

    artist_list = []

    print("Loading music data...")

    with open("albums.txt", "r") as albums:
        for line in albums:
            # bind variables to the fields of each line (stripping new line char and splitting on tabs)
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)  # convert string value to int
            print(f"\t{artist_field}:{album_field}:{year_field}:{song_field}")

            current_artist = find_object(artist_field, artist_list)
            if not current_artist:
                current_artist = Artist(artist_field)
                artist_list.append(current_artist)

            current_artist.add_song(album_field, year_field, song_field)

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
                    print(f"{artist.name}\t{album.name}\t{album.year}\t{song.name}", file=checkfile)

    print("Checkfile created.")
    print()
    print("=" * 40)
    print()


if __name__ == '__main__':

    # loads data from albums.txt
    artists = load_data()
    create_checkfile(artists)



