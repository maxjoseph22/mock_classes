# File: lib/music_library.py
from lib.track import *

class MusicLibrary:

    def __init__(self):
        self.track_library = []

    def add(self, track):
        self.track_library.append(track)

    def search(self, keyword):
        matches_list = []
        for track in self.track_library:
            if track.matches(keyword):
                matches_list.append(track)
        return matches_list
        


        # keyword is a string
        # Returns a list of instances of track that match the keyword
        pass
