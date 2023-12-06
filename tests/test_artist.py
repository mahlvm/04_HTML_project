from lib.artist import Artist

def test_artist_construction():
    artist  = Artist (1, 'Artists Test', 'Genre test')
    assert artist.id == 1
    assert artist.name == 'Artists Test'
    assert artist.genre == 'Genre test'

def test_artist_compare():
    artist_1 = Artist (1, 'Test Name', 'Test Genre')
    artist_2 = Artist (1, 'Test Name', 'Test Genre')
    assert artist_1 == artist_2

def test_artist_stringfying():
    artist = Artist(1, 'Test Name', 'Test Genre')
    assert str(artist) == 'Artist(1, Test Name, Test Genre)'

    