# coding=utf-8
from random import choice, shuffle
from typing import List

from requests import get


def get_video() -> (str, str):
    """ récupère une vidéo au pif dans videos.list """
    lines = open('videos.list').read().splitlines()
    line = choice(lines)
    pos = line.index(';')
    video_id, video_name = line[:pos].strip(), line[pos + 1:].strip()
    return video_id, video_name


def ultimate_shuffle() -> List[str]:
    """ récupère la liste contenue dans videos.list, mélangée """
    lines = open('videos.list').read().splitlines()
    lines = [line[:line.index(';')] for line in lines]
    shuffle(lines)
    return lines


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
