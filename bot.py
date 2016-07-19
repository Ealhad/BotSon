import requests


def init():
    """ récupère le cookie de session et le nombre de vidéos dans la file
    aucune idée pour l'instant pour le nombre
    """
    r = requests.get('https://togethertube.com/rooms/salle-de-ballmer')
    return r.cookies['PLAY_SESSION'], 42  # TODO


def vote(video):
    """ vote pour une vidéo
    https://www.youtube.com/watch?v=<video>
    """
    post = requests.post('https://togethertube.com/api/v1/rooms/salle-de-ballmer/playlist/votes',
                         json={'mediaId': video, 'mediaServiceId': 'youtube'},
                         cookies={'PLAY_SESSION': cookie})
    return post.ok


def get_video():
    """ récupère une vidéo au pif dans videos.list
    (TODO)
    """
    lines = open('videos.list').read().splitlines()


cookie, number_of_videos = init()

if vote('dQw4w9WgXcQ'):
    print("Vidéo ajoutée !")
else:
    print("Snif, snif...")
