# coding: utf-8
from __future__ import print_function, division, absolute_import

from .relive import Relives, ReliveRecordings
from .testdata import getfile


def test_index():
    r = Relives(sample_index)
    assert len(r.recordings) == 15
    assert r.recordings[0].project == "wevsclimatecrisis"
    assert r.recordings[0].index_url == "//cdn.c3voc.de/relive/wevsclimatecrisis/index.json"
    assert r.recordings[1].project == "rc3"
    assert r.recordings[1].index_url == "//cdn.c3voc.de/relive/rc3/index.json"
    assert r.recordings[1].get_url() == "https://cdn.c3voc.de/relive/rc3/index.json"


def test_index_by_conf():
    r = Relives(sample_index).by_conference('rc3')
    assert r is not None

    r = Relives(sample_index).by_conference('foo')
    assert r is None


def test_recordings():
    all = ReliveRecordings(sample_recording)
    assert len(all.recordings) == 7

    unreleased = ReliveRecordings(sample_recording).unreleased()
    assert len(unreleased) == 5

    assert unreleased[0].mp4 == "//cdn.c3voc.de/relive/rc3/11575/muxed.mp4"
    assert unreleased[0].get_video_url() == "https://cdn.c3voc.de/relive/rc3/11575/muxed.mp4"
    assert unreleased[0].thumbnail == "//cdn.c3voc.de/relive/rc3/11575/thumb.jpg"
    assert unreleased[0].get_thumb_url() == "https://cdn.c3voc.de/relive/rc3/11575/thumb.jpg"


sample_index = getfile('relive_index.json')
sample_recording = getfile('relive_recordings.json')
