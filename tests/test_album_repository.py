from lib.album_repository import AlbumRepository
from lib.album import Album

def test_all(db_connection):
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album (1, 'Doolittle', 1989, 1),
        Album (2, 'Surfer Rosa', 1988, 1)
    ]

def test_create(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, 'Title Test', 2000, 1)
    repository.create(album)
    assert repository.all() == [
        Album (1, 'Doolittle', 1989, 1),
        Album (2, 'Surfer Rosa', 1988, 1),
        Album (3, 'Title Test', 2000, 1)
    ]

def test_find(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    result = repository.find(2)
    assert result == Album (2, 'Surfer Rosa', 1988, 1)