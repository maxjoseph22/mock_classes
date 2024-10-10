from lib.track import *

def test_track_inits_with_title_and_artist():
    track = Track("Into You", "Tamia")
    assert track.title == "Into You"
    assert track.artist == "Tamia"

def test_keyword_match():
    track = Track("Into You", "Tamia")
    assert track.matches("Tamia") == True

def test_keyword_mismatch():
    track = Track("Into You", "Tamia")
    assert track.matches("Into yo") == False
