from lib.music_library import *
from lib.track import *
from unittest.mock import Mock


def test_add_a_single_track():
    music_library = MusicLibrary()
    track_1 = Track("Song 2", "Blur")
    music_library.add(track_1)

def test_search_for_a_track_that_is_present():
    music_library = MusicLibrary()
    track_1 = Track("Song 2", "Blur")
    music_library.add(track_1)
    assert music_library.search("Song 2") == [track_1]

def test_search_for_a_mock_track():
    music_library = MusicLibrary()
    fake_track = Mock()
    music_library.add(fake_track)
    fake_track.matches.return_value = True
    assert music_library.search("Song 2") == [fake_track]

    #  diary = Diary()

    # fake_two_word_diary_entry = Mock()
    # fake_two_word_diary_entry.count_words.return_value = 2

    # fake_three_word_diary_entry = Mock()
    # fake_three_word_diary_entry.count_words.return_value = 3

    # diary.add(fake_two_word_diary_entry)
    # # diary.add(fake_three_word_diary_entry)

    # assert diary.count_words() == 5

def test_search_for_a_track_that_is_present_multiple_times():
    music_library = MusicLibrary()
    track_1 = Track("Song 2", "Blur")
    music_library.add(track_1)
    track_2 = Track("Song 2", "Bon Iver")
    music_library.add(track_2)
    assert music_library.search("Song 2") == [track_1, track_2]
    
