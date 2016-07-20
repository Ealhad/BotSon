# coding=utf-8
from random import choice
from requests import get, post


def init():
    # type: () -> dict, int
    """ récupère les cookies de session et le nombre de vidéos dans la file
    aucune idée pour l'instant pour le nombre
    :return: cookies, nombre de vidéos
    """
    r = get('https://togethertube.com/rooms/salle-de-ballmer')
    return {'PLAY_SESSION': r.cookies['PLAY_SESSION']}, 42  # TODO


def vote(video, cookies):
    # type: (str, dict) -> bool
    """ vote pour une vidéo
    :return: succès du vote
    :param cookies: cookies à ajouter à la requête
    :param video: id de la vidéo - https://www.youtube.com/watch?v=<vidéo>
    """
    r = post('https://togethertube.com/api/v1/rooms/salle-de-ballmer/playlist/votes',
             json={'mediaId': video, 'mediaServiceId': 'youtube'},
             cookies=cookies)
    return r.ok


def get_video():
    # type: () -> str, str
    """ récupère une vidéo au pif dans videos.list
    (TODO)
    :return: id, nom de la vidéo
    """
    lines = open('videos.list').read().splitlines()
    line = choice(lines)
    pos = line.index(';')
    return line[:pos].strip(), line[pos + 1:].strip()


def main():
    cookies, _ = init()
    video, name = get_video()
    status = vote(video, cookies)
    if status:
        print('Vidéo ajoutée : {0} (https://youtube.com/watch?v={1})'.format(name, video))
    else:
        print('Erreur !')


main()
