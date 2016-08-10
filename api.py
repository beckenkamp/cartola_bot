# coding: utf-8
import os
import requests


def get_league():
    url = 'https://api.cartolafc.globo.com/auth/liga/liga-da-tia'
    headers = {
        'X-GLB-Token': os.environ['GLB_API_TOKEN']
    }

    r = requests.get(url, headers=headers)
    teams = r.json()['times']
    result = "".join([u"{}: {}\n".format(team['nome'],
                                         "{0:.2f}".format(team['pontos']['campeonato'])) for team in teams])
    return result


def get_partials():
    url = "https://api.cartolafc.globo.com/atletas/pontuados"

    r = requests.get(url)
    data = r.json()

    if "mensagem" in data:
        return data['mensagem']

    return data
