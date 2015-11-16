from __future__ import print_function

import operator

from xbmcswift2 import Plugin

from resources.lib.helpers import recording_list
import resources.lib.http as http

plugin = Plugin()

QUALITY = ["sd", "hd"]
FORMATS = ["mp4", "webm"]

@plugin.route('/', name='index')
@plugin.route('/dir/<subdir>')
def show_dir(subdir = ''):
    try:
        data = get_index_data()
    except http.FetchError:
        return

    items = []
    subdirs = set()
    if subdir == '':
        depth = 0
    else:
        depth = len(subdir.split('/'))


    for event in data:
        top, down, children = split_pathname(event['webgen_location'], depth)

        if top != subdir or down in subdirs:
            continue
        if children:
            items.append({
                'label': down.title(),
                'path': plugin.url_for('show_dir', subdir = build_path(top, down))
            })
            subdirs.add(down)
        else:
            items.append({
                'label': event['title'],
                'label2': event['acronym'],
                'thumbnail': event['logo_url'],
                'path': plugin.url_for('show_conference', conf = event['url'].rsplit('/', 1)[1])
            })

    items.sort(key=operator.itemgetter('label'))

    if depth == 0:
        items.insert(0, {
            'label': 'Live Streaming',
            'path': plugin.url_for('show_live')
        })

    return items

@plugin.route('/conference/<conf>')
def show_conference(conf):
    data = None
    try:
        data = http.fetch_data('conferences/' + conf)['events']
    except http.FetchError:
        return

    items = []
    for event in data:
        items.append({
            'label': event['title'],
            'thumbnail': event['thumb_url'],
            'info': {
                'cast': event['persons'],
                'plot': event['description'],
                'tagline': event['subtitle']
            },
            'stream_info': {
                'video': {
                    'duration': event['length']
                },
            },
            'path': plugin.url_for('resolve_event_default', event = event['url'].rsplit('/', 1)[1]),
            'is_playable': True
            })
    return sorted(items, key=operator.itemgetter('label'))

@plugin.route('/event/<event>', name = 'resolve_event_default')
@plugin.route('/event/<event>/<quality>/<format>')
def resolve_event(event, quality = None, format = None):
    if quality not in QUALITY:
        quality = QUALITY[plugin.get_setting('quality', int)]
    if format not in FORMATS:
        format = FORMATS[plugin.get_setting('format', int)]

    data = None
    try:
        data = http.fetch_data('events/' + event)['recordings']
    except http.FetchError:
        return
    want = recording_list(data, quality, format)

    if len(want) > 0:
        http.count_view(event, want[0].url)
        plugin.set_resolved_url(want[0].url)

@plugin.route('/live')
def show_live():
    quality = QUALITY[plugin.get_setting('quality', int)]
    format = FORMATS[plugin.get_setting('format', int)]

    data = None
    try:
        data = http.fetch_live()
    except http.FetchError:
        return

    if len(data.rooms) == 0:
        return [{
            'label': 'No live event currently, go watch some recordings!',
            'path': plugin.url_for('index')
        }]

    items = []
    for room in data.rooms:
        want = room.streams_sorted(quality, format)

        try:
            item = next(x for x in want if x.translated == False)
            items.append({
                'label': room.display,
                'is_playable': True,
                'path': item.url
            })
        except StopIteration:
            pass

        try:
            item = next(x for x in want if x.translated == True)
            items.append({
                'label': room.display + ' (Translated)',
                'is_playable': True,
                'path': item.url
            })
        except StopIteration:
            pass

    return items


@plugin.cached()
def get_index_data():
    return http.fetch_data('conferences')['conferences']

def split_pathname(name, depth):
    path = name.split('/')
    top = '/'.join(path[0:depth])
    if depth < len(path):
        down = path[depth]
    else:
        down = None
    children = len(path)-1 > depth
    return (top, down, children)

def build_path(top, down):
    if top == '':
        return down
    else:
        return '/'.join((top, down))

if __name__ == '__main__':
    plugin.run()
