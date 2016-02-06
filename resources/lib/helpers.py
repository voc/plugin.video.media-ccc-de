from __future__ import print_function


def user_preference_sorter(prefer_quality, prefer_format):
    def do_sort(obj):
        prio = 0

        if obj.format == prefer_format:
            prio += 20

        # Bonus & penalty for exact matches, no score for "obj.hd == None"
        if obj.hd == True and prefer_quality == "hd":
            prio += 20
        elif obj.hd == False and prefer_quality == "sd":
            prio += 20
        elif obj.hd == True and prefer_quality == "sd":
            prio -= 10
        elif obj.hd == False and prefer_quality == "hd":
            prio -= 10

        # Prefer versions with "more" audio tracks
        try:
            translations = len(obj.languages) - 1
            prio += translations
        except AttributeError:
            pass

        # Prefer "native" over "translated" for now (streaming)...
        try:
            if obj.translated:
                prio += 5
        except AttributeError:
            pass

        return -prio
    return do_sort
