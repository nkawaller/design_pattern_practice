# Studying the factory method pattern using this article:
# https://realpython.com/factory-method-python/

# How you'd handle different situations without the factory method pattern

import json
import xml.etree.ElementTree as et
"""
class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist

class SongSerializer:
    def serialize(self, song, format):
        if format == 'JSON':
            song_info = {
                'id': song.song_id,
                'title': song.title,
                'artist': song.artist
            }
            return json.dumps(song_info)
        elif format == 'XML':
            song_info = et.Element('song', attrib={'id': song.song_id})
            title = et.SubElement(song_info, 'title')
            title.text = song.title
            artist = et.SubElement(song_info, 'artist')
            artist.text = song.artist
            return et.tostring(song_info, encoding='unicode')
        else:
            raise ValueError(format)

"""
# Refactoring the code into the desired interface

class SongSerializer:
    def serialize(self, song, format):
        if format == 'JSON':
            return self._serialize_to_json(song)

    def _serialize_to_json(self, song):
        payload = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(payload)

"""
import factory_method as sd
song = sd.Song('1', 'Water of Love', 'Dire Straits')
serializer = sd.SongSerializer()
"""