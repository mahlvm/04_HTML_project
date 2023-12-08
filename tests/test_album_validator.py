from lib.album_validator import AlbumValidator
import pytest

def test_is_valid():
    validator = AlbumValidator("My title", "1990")
    assert validator.is_valid() == True

def test_is_not_valid_with_bad_title():
    validator_1 = AlbumValidator("", 1990)
    assert validator_1.is_valid() == False
    validator_2 = AlbumValidator(None, 1990)
    assert validator_2.is_valid() == False


def test_is_not_valid_with_bad_release_year():
    validator_1 = AlbumValidator("Title", "")
    assert validator_1.is_valid() == False
    validator_2 = AlbumValidator("Title", None)
    assert validator_2.is_valid() == False
    validator_3 = AlbumValidator("Title", "no int")
    assert validator_3.is_valid() == False


def test_generate_errors():
    validator_1 = AlbumValidator("", "")
    assert validator_1.generate_errors() == [
        "Title must not be blank",
        "Release year must be a number"
    ]
    validator_2 = AlbumValidator("Title", "")
    assert validator_2.generate_errors() == [
        "Release year must be a number"
    ]
    validator_3 = AlbumValidator("", "1234")
    assert validator_3.generate_errors() == [
        "Title must not be blank"
    ]

def test_get_valid_title_if_title_valid():
    validator = AlbumValidator("My title", "1990")
    assert validator.get_valid_title() == "My title"

def test_get_valid_title_refuses_if_invalid():
    validator = AlbumValidator("", "1990")
    with pytest.raises(ValueError) as err:
        validator.get_valid_title()
    assert str(err.value) == "Cannot get valid title"


def test_get_valid_release_year_if_release_year_valid():
    validator = AlbumValidator("My title", "1990")
    assert validator.get_valid_release_year() == 1990

def test_get_valid_release_year_refuses_if_invalid():
    validator = AlbumValidator("My title", "")
    with pytest.raises(ValueError) as err:
        validator.get_valid_release_year()
    assert str(err.value) == "Cannot get valid release year"