class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment
    
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        else:
            print("Genre is already in list")
        
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
        else:
            print("Artist is already in list")

    @classmethod
    def add_to_genre_count(cls,genre,increment = 1):
        cls.genre_count[f"{genre}"] += increment

    @classmethod
    def add_to_artist_count(cls,artist,increment = 1):
        cls.artist_count[f"{artist}"] += increment


        
