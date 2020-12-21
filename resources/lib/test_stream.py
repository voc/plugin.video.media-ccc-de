# coding: utf-8
from __future__ import print_function, division, absolute_import

import pytest

from .stream import Streams
from .testdata import getfile


DATA = list((quality, format, quality == 'hd', dash)
    for quality in ('hd', 'sd')
    for format in ('mp4', 'webm')
    for dash in (True, False))


def test_conferences():
    s = Streams(SampleJson)
    assert len(s.conferences) == 2
    assert s.conferences[0].slug == "eh17"
    assert s.conferences[0].name == "Easterhegg 2017"


def test_rooms():
    s = Streams(SampleJson)
    c = s.conferences[0]
    assert len(c.rooms) == 3
    assert c.rooms[0].slug == "vortragssaal"
    assert c.rooms[0].display == u"Für die Glupscher: Vortragssaal"


@pytest.mark.parametrize('quality,format,hd,dash', DATA)
def test_streams(quality, format, hd, dash):
    s = Streams(SampleJson)
    c = s.conferences[0]
    r = c.rooms[0]
    assert len(r.streams) == 6
    streams = r.streams_sorted(quality, format, dash)
    assert len(streams) == 4
    preferred = streams[0]
    assert preferred.type == 'video'
    assert preferred.hd is hd
    assert preferred.format == format
    assert preferred.translated is False


@pytest.mark.parametrize('quality,format,hd,prefer_dash', DATA)
def test_streams_multiple_translations(quality, format, hd, prefer_dash):
    s = Streams(SampleJson)
    c = s.conferences[1]
    r = c.rooms[0]
    assert len(r.streams) == 25
    streams = r.streams_sorted(quality, format, prefer_dash)
    assert len(streams) == 13

    if prefer_dash:
        dash = streams[0]
        native = streams[1]
        trans1 = streams[2]
        trans2 = streams[3]
    else:
        native = streams[0]
        trans1 = streams[1]
        trans2 = streams[2]
        dash = streams[-1]

    assert native.hd is hd
    assert native.format == format
    assert native.translated is False

    assert trans1.hd is hd
    assert trans1.format == format
    assert trans1.translated is True

    assert trans2.hd is hd
    assert trans2.format == format
    assert trans2.translated is True

    assert dash.type == 'dash'
    assert dash.hd is None
    assert dash.format == 'dash'
    assert dash.translated is False


SampleJson = getfile('stream_v2.json')
