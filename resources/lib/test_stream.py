# -*- coding: utf-8 -*-

from __future__ import print_function

from .stream import Streams
from .testdata import getfile


def test_conferences():
    s = Streams(SampleJson)
    assert len(s.conferences) == 1
    assert s.conferences[0].slug == "eh17"
    assert s.conferences[0].name == "Easterhegg 2017"


def test_rooms():
    s = Streams(SampleJson)
    c = s.conferences[0]
    assert len(c.rooms) == 3
    assert c.rooms[0].slug == "vortragssaal"
    assert c.rooms[0].display == u"Für die Glupscher: Vortragssaal"


def test_streams():
    s = Streams(SampleJson)
    c = s.conferences[0]
    r = c.rooms[0]
    assert len(r.streams) == 6
    streams = r.streams_sorted("hd", "mp4")
    assert len(streams) == 4
    preferred = streams[0]
    assert preferred.hd is True
    assert preferred.format == 'mp4'
    assert preferred.translated is False


SampleJson = getfile('stream_v2.json')
