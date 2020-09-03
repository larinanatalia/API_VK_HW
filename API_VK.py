from pprint import pprint
class Users:
    token = '++++++++++++++++++++++++++++++++++++++++++++++++++++'

    def __init__(self, file_path):
        self.file_path = file_path

        import requests
        import json
        import time
        screen_name_spl = self.file_path.split('/')
        screen_name = screen_name_spl[-1]
        params = {'screen_name': screen_name,
                  'access_token': self.token,
                  'v': 5.122
                  }
        resp = requests.get('https://api.vk.com/method/utils.resolveScreenName', params=params)
        resp_get = resp.json()
        self.user_id = resp_get['response']['object_id']

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

        n = list()
        for id in friends_id_list:
            params_friends_names = {
                'user_ids': str(id),
                'name_case': 'Nom',
                'access_token': self.token,
                'v': 5.122
            }
            resp_fr_names = requests.get('https://api.vk.com/method/users.get', params=params_friends_names)
            time.sleep(0.25)
            resp_fr_names_get = resp_fr_names.json()
            fr_names_list_name = resp_fr_names_get["response"][0]["first_name"]
            fr_names_list_last_name = resp_fr_names_get["response"][0]["last_name"]
            n.append(fr_names_list_name + ' ' + fr_names_list_last_name)
        fr_names_set = set()
        fr_names_set = fr_names_set.union(n)
        self.friends = fr_names_set




nata = Users('https://vk.com/lanabanana1')
dima = Users('https://vk.com/kolechenkov')
set_fr = nata.friends & dima.friends
pprint(set_fr)
pprint(nata.file_path)
