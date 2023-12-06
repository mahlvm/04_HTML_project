from lib.album import Album

def test_construction():
    album  = Album (1, 'Title Test', 2000, 2)
    assert album.id == 1
    assert album.title == 'Title Test'
    assert album.release_year == 2000
    assert album.artist_id == 2

def test_compare():
    album_1 = Album(1, 'Tes Title', 1000, 2)
    album_2 = Album(1, 'Tes Title', 1000, 2)
    assert album_1 == album_2

def test_stringfying():
    album = Album(1, 'Teste Title', 1000, 2)
    assert str(album) == 'Album(1, Teste Title, 1000, 2)'