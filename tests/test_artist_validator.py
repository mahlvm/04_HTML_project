from lib.artist_validator import ArtistValidator
import pytest

def test_is_valid():
    validator = ArtistValidator("Artist Test", "Genre Test")
    assert validator.is_valid() == True

#######

def test_is_not_valid_with_bad_name():
    validator_1 = ArtistValidator("", "Genre Test")
    assert validator_1.is_valid() == False
    validator_2 = ArtistValidator(None, "Genre Test")
    assert validator_2.is_valid() == False

#######

def test_is_not_valid_with_bad_genre():
    validator_1 = ArtistValidator("Artist Test", "")
    assert validator_1.is_valid() == False
    validator_2 = ArtistValidator("Artist Test", None)
    assert validator_2.is_valid() == False

#######

def test_generate_errors():
    validator_1 = ArtistValidator("", "")
    assert validator_1.generate_errors() == [
        "Name must not be blank",
        "Genre must not be blank"
    ]
    validator_2 = ArtistValidator("Artist Test", "")
    assert validator_2.generate_errors() == [
        "Genre must not be blank"
    ]
    validator_3 = ArtistValidator("", "Genre Test")
    assert validator_3.generate_errors() == [
        "Name must not be blank"
    ]

#######

def test_get_valid_name_if_name_valid():
    validator = ArtistValidator("Artist Test", "Genre Test")
    assert validator.get_valid_name() == "Artist Test"

#######

def test_get_valid_name_refuses_if_invalid():
    validator = ArtistValidator("", "Genre Test")
    with pytest.raises(ValueError) as err:
        validator.get_valid_name()
    assert str(err.value) == "Cannot get valid name"

######


def test_get_valid_genre_if_genre():
    validator = ArtistValidator("Artist Test", "Genre Test")
    assert validator.get_valid_genre() == "Genre Test"

######

def test_get_valid_genre_refuses_if_invalid():
    validator = ArtistValidator("Artist Test", "")
    with pytest.raises(ValueError) as err:
        validator.get_valid_genre()
    assert str(err.value) == "Cannot get valid genre"