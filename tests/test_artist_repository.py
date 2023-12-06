from lib.artist_repository import ArtistRepository
from lib.artist import Artist

def test_artist_all(db_connection):
    repository = ArtistRepository(db_connection)
    assert repository.all() == [
        Artist (1, 'Pixies', 'Rock'),
        Artist (2, 'ABBA', 'Pop'),
        Artist (3, 'Taylor Swift', 'Pop'),
        Artist (4, 'Nina Simone', 'Jazz')
    ]

def test_artist_create(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)
    artist = Artist(None, 'Name Test', 'Genre Test')
    repository.create(artist)
    assert repository.all() == [
        Artist (1, 'Pixies', 'Rock'),
        Artist (2, 'ABBA', 'Pop'),
        Artist (3, 'Taylor Swift', 'Pop'),
        Artist (4, 'Nina Simone', 'Jazz'),
        Artist (5, 'Name Test', 'Genre Test')

    ]

def test_get_single_record(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)
    artist = repository.find(3)
    assert artist == Artist(3, "Taylor Swift", "Pop")
