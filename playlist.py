# coding=utf-8
from random import shuffle
from typing import List

from requests import get

Url = str


def get_video() -> Url:
    """ récupère une vidéo au pif dans videos.list """
    return get_videos(1)[0]


def get_videos(n: int = 0) -> List[str]:
    """ récupère une liste mélangée de vidéos tirées de videos.list """
    lines = open('videos.list').read().splitlines()
    lines = [line[:line.index(';')] for line in lines]
    shuffle(lines)
    return lines if n == 0 else lines[:n]


def add_video(video: str, name: str = '') -> None:
    """ ajoute une vidéo (par URL) à videos.list """
    r = get(video)
    if not r.ok:
        print('Vidéo introuvable')
        return
    if name == '':
        name = r.text[r.text.find('<title>') + 7:r.text.find('</title>') - 10]

    video = video[video.find('=') + 1:]

    with open('videos.list', 'a') as playlist:
        playlist.write('{0}; {1}\n'.format(video, name))


def main() -> None:
    from sys import argv

    if len(argv) > 1:
        video = argv[1]
        name = argv[2] if len(argv) > 2 else ''
        add_video(video, name)
    else:
        print("Pas assez d'arguments !\nArguments : url [nom]")


if __name__ == "__main__":
    main()
