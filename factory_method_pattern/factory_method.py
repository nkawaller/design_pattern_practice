# Studying the factory method pattern using this article:
# https://realpython.com/factory-method-python/

# How you'd handle different situations without the factory method

import json
import xml.etree.ElementTree as et

class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist