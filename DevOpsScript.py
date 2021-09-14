import requests
import json


def get_data():

    url = ""    #твой url

    req = requests.get(url, auth=('user', 'pass'))
    req_json = req.json()

    # Переводишь в словарь
    data_in_dict = json.load(req_json)

    # Вычленяешь нужную инфу
    pending = "pending: " + data_in_dict["pending"]

