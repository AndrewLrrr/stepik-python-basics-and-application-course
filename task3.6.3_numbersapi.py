import requests

with open('task3.6.3/dataset_24476_3.txt', 'r') as f:
    for number in f:
        url = 'http://numbersapi.com/{0}/math'.format(number.strip())
        r = requests.get(url, {'json': 'true'})
        res = r.json()
        if res['found']:
            print('Interesting')
        else:
            print('Boring')
