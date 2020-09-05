from pprint import pprint
import requests
import json
class Users:

    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token

        params_friends = {
            'user_id': self.user_id,
            'order': 'hints',
            'access_token': self.token,
            'v': 5.122
        }
        resp_fr = requests.get('https://api.vk.com/method/friends.get', params=params_friends)
        resp_fr_get = resp_fr.json()
        friends_id_list = resp_fr_get['response']['items']
        self.friends_id = friends_id_list

    def __str__(self):
        return f'https://vk.com/id{self.user_id}'


    def __and__(self, other):
        mutal_user_lust = list()
        for i in self.friends_id:
            if i in other.friends_id:
                mutal_user_lust.append(i)
        return mutal_user_lust

