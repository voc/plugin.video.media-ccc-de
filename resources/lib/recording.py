from __future__ import print_function

from .helpers import user_preference_sorter


class Recordings(object):
    def __init__(self, json):
        self.recordings = [Recording(elem) for elem in json['recordings']]

    def recordings_sorted(self, quality, format, video=True):
        print("Requested quality %s and format %s" % (quality, format))
        typematch = "video" if video else "audio"
        want = sorted(filter(lambda rec: rec.type == typematch,
                             self.recordings),
                      key=user_preference_sorter(quality, format))
        print(want)
        return want


class Recording(object):
    def __init__(self, json):
        self.mime = json['mime_type']
        self.type, self.format = self.mime.split('/')
        self.hd = json['high_quality']
        self.url = json['recording_url']
        self.length = json['length']
        self.size = json['size']
        lang = json['language']
        if lang:
            self.languages = lang.split('-')
        else:
            self.languages = ('unk',)

    def __repr__(self):
        return "Recording<M:%s,HD:%s,LANG:%s>" % (self.mime, self.hd,
                                                  self.languages)

    def is_video(self):
        return self.type == 'video'

    def is_audio(self):
        return self.type == 'audio'
