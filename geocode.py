import requests
import os
from dotenv import load_dotenv

load_dotenv()

SERVER = 'http://geocode-maps.yandex.ru/1.x/'


def get_coord(address):
    params = {'apikey': os.getenv('API_KEY_GEOCODE'),
              'geocode': address,
              'format': 'json'}
    resp = requests.get(SERVER, params=params)
    if resp:
        resp = resp.json()
    else:
        raise RuntimeError('Ошибка выполнения запроса')
    return ','.join(resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split())


def geocode(coord):
    params = {'apikey': os.getenv('API_KEY_GEOCODE'),
              'geocode': coord,
              'format': 'json',
              'kind': 'district'}
    resp = requests.get(SERVER, params=params)
    if resp:
        resp = resp.json()
    else:
        raise RuntimeError('Ошибка выполнения запроса')
    return resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['name']
