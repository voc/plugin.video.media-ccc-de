# coding: utf-8
from __future__ import print_function, division, absolute_import

from .helpers import maybe_json
from .kodi import log


class Relives(object):
    def __init__(self, json):
        self.recordings = [ReliveItem(elem) for elem in json]


class ReliveItem(object):
    def __init__(self, json):
        self.index_url = json['index_url']
        # self.media_conference_id = json['media_conference_id']
        self.project = json['project']
        self.updated_at = json['updated_at']


class ReliveRecording(object):
    def __init__(self, json):
        self.duration = json['duration']
        self.guid = json['guid']
        self.id = json['id']
        self.mtime = json['mtime']
        self.playlist = json['playlist']
        self.release_url = maybe_json(json, 'release_url', '')
        self.mp4 = maybe_json(json, 'mp4', '')
        self.room = json['room']
        self.start = json['start']
        self.status = json['status']
        self.thumbnail = json['thumbnail']
        self.title = json['title']
