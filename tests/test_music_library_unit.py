from lib.music_library import *

def test_music_library_inits_with_blank_list_of_tracks():
    music_library = MusicLibrary()
    assert music_library.track_library == []