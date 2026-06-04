# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/voc/plugin.video.media-ccc-de/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                             |    Stmts |     Miss |   Branch |   BrPart |   Cover |   Missing |
|--------------------------------- | -------: | -------: | -------: | -------: | ------: | --------: |
| addon.py                         |      170 |      170 |       52 |        0 |      0% |     2-265 |
| resources/\_\_init\_\_.py        |        0 |        0 |        0 |        0 |    100% |           |
| resources/lib/\_\_init\_\_.py    |        0 |        0 |        0 |        0 |    100% |           |
| resources/lib/gui.py             |       21 |        0 |        2 |        1 |     96% |   21-\>25 |
| resources/lib/helpers.py         |       51 |       16 |       18 |        0 |     71% |51-61, 65-70 |
| resources/lib/http.py            |       48 |       48 |        0 |        0 |      0% |      2-69 |
| resources/lib/kodi.py            |       16 |        6 |        4 |        1 |     55% | 13-17, 22 |
| resources/lib/recording.py       |       31 |        3 |        2 |        1 |     88% |36, 43, 46 |
| resources/lib/relive.py          |       34 |        2 |        0 |        0 |     94% |       6-7 |
| resources/lib/settings.py        |       16 |       16 |        2 |        0 |      0% |      2-28 |
| resources/lib/stream.py          |       45 |        1 |       16 |        2 |     95% |30-\>29, 35-\>38, 62 |
| resources/lib/test\_gui.py       |       14 |        0 |        0 |        0 |    100% |           |
| resources/lib/test\_recording.py |       24 |        0 |        0 |        0 |    100% |           |
| resources/lib/test\_relive.py    |       28 |        0 |        0 |        0 |    100% |           |
| resources/lib/test\_stream.py    |       75 |        0 |        2 |        0 |    100% |           |
| resources/lib/testdata.py        |        7 |        0 |        0 |        0 |    100% |           |
| **TOTAL**                        |  **580** |  **262** |   **98** |    **5** | **52%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/voc/plugin.video.media-ccc-de/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/voc/plugin.video.media-ccc-de/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/voc/plugin.video.media-ccc-de/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/voc/plugin.video.media-ccc-de/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fvoc%2Fplugin.video.media-ccc-de%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/voc/plugin.video.media-ccc-de/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.