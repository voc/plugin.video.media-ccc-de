import requests

from .stream import Streams
from .recording import Recordings
from . import gui

BASE_URL = 'api.media.ccc.de/public/'
LIVE_URL = 'streaming.media.ccc.de/streams/v1.json'

# BASE_URL = '127.0.0.1:3000/public/'
# LIVE_URL = '127.0.0.1:3000/v1.json'


class FetchError(Exception):
    pass


def fetch_data(what, insecure=False):
    try:
        req = requests.get(build_url(BASE_URL + what, insecure))
        return req.json()
    except requests.RequestException as e:
        gui.err('Can\'t fetch %s: %s' % (what, e))
        raise FetchError(e)


def count_view(event, src, insecure=False):
    try:
        data = {'event_id': event, 'src': src}
        requests.post(build_url(BASE_URL + 'recordings/count', insecure), data=data)
    except requests.RequestException as e:
        gui.info('Can\'t count view: %s' % e)


def fetch_recordings(event, insecure=False):
    req = fetch_data('events/' + event, insecure)
    return Recordings(req)


def fetch_live(insecure=False):
    try:
        req = requests.get(build_url(LIVE_URL, insecure))
        return Streams(req.json())
    except requests.exceptions.RequestException as e:
        gui.err('Can\'t fetch streams: %s' % e)
        raise FetchError(e)


def build_url(url, insecure=False):
    return "http%s://%s" % ("" if insecure else "s", url)
