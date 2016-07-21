# coding=utf-8
from typing import List

from requests import get, post

from playlist import get_video, ultimate_shuffle

Url = str


def init() -> (dict, int):
    """ récupère les cookies de session et le nombre de vidéos dans la file
    aucune idée pour l'instant pour le nombre
    """
    r = get('https://togethertube.com/rooms/salle-de-ballmer')
    return r.cookies, 42  # TODO


def vote(video: Url, cookies: dict) -> bool:
    """ vote pour une vidéo """
    r = post('https://togethertube.com/api/v1/rooms/salle-de-ballmer/playlist/votes',
             json={'mediaId': video[video.index('=') + 1:], 'mediaServiceId': 'youtube'},
             cookies=cookies)
    return r.ok


def vote_all(videos: List[Url], cookie: dict) -> None:
    """ vote pour plusieurs vidéos """
    for video in videos:
        vote(video, cookie)


def main() -> None:
    cookies, _ = init()
    video, name = get_video()
    ok = vote(video, cookies)
    if ok:
        print('Vidéo ajoutée : {} ({})'.format(name, video))
    else:
        print('Erreur !')


if __name__ == "__main__":
    cookies, _ = init()
    vote_all(ultimate_shuffle(), cookies)
