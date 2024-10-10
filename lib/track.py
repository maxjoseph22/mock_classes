# File: lib/track.py

class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        
    def matches(self, keyword):
        if keyword == self.artist or keyword == self.title:
            return True
        return False
        
