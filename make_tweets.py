import twitter
import requests
#import json
import time 

base_site = requests.get('https://www.probytes.net').text

keys = ['yk',
        'oe',
        'uy',
        'rz']

api = twitter.Api(
                  consumer_key=keys[0],
                  consumer_secret=keys[1],
                  access_token_key=keys[2],
                  access_token_secret=keys[3])


def twatt(message, m):
    global api
    api.PostUpdate(message, media=m)
    print('The twatt has been tweeted.')

def exists(url):
    req = requests.get(url).text
    return req != base_site

def create_twatt(n): 
    while True: 
        url = f'https://www.probytes.net/wp-content/uploads/2018/01/{n}.jpg'

        if not exists(url):
            url = f'https://www.probytes.net/wp-content/uploads/2018/01/{n}-1.jpg'

        yield (f'I guess this is an ok #programming meme in place of anything else...\n', url)
        n += 1

creator = create_twatt(1)

twatts = [next(creator) for _ in range(10)]

for i in twatts:
    print('Sending...')
    twatt(i[0], i[1])
    time.sleep(600)
