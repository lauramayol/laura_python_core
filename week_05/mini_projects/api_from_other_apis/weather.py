from pprint import pprint
import requests


class My_app:

    def get_weather(self):
        r = requests.get("http://api.openweathermap.org/data/2.5/weather?id=6356055&units=imperial&APPID=e821aa02dca02c009dbc45400a3ceacd", json=True)

        data = r.json()

        # pprint(r.headers)
        pprint(data)
        # print(type(data))

        print(data['visibility'])


curl - F 'client_id=0a6d65b210a1428c876bd417de259968' \
    - F 'client_secret=dec191328e6f4912b2881f5fdf06cd05' \
    - F 'grant_type=authorization_code' \
    - F 'redirect_uri=https://codingnomads.co/' \
    - F 'code=820a4c5fd9444f44b2c51cbd979dce4d' \
    https: // api.instagram.com / oauth / access_token
