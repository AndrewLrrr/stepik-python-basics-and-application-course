import requests

client_id = '5f833d23634f6c963d8a'
client_secret = 'b3de90159a0d8a6d5f425b7b2219f369'

token_url = 'https://api.artsy.net/api/tokens/xapp_token'

r = requests.post(token_url, data={'client_id': client_id, 'client_secret': client_secret})

res = r.json()

headers = {'X-Xapp-Token': res['token']}

artists = {}

with open('task3.6.6/dataset_24476_4.txt', 'r') as f:
    for artist_id in f:
        url = 'https://api.artsy.net:443/api/artists/{0}'.format(artist_id.strip())
        r = requests.get(url, headers=headers)
        res = r.json()
        if 'sortable_name' in res:
            artists[res['birthday']] = res['sortable_name']

with open('task3.6.6/result.txt', 'w') as f:
    for birth_date, name in sorted(artists.items()):
        f.write(name + '\n')
