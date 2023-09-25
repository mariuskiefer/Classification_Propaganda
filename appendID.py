import json
import os
from itertools import islice

file = open('tweet_ids.json')

data = json.load(file)

url = 'https://twitter.com/anyuser/status/'

urllist = []
idlist = []

for item in data:

    item = str(item)
    urllist.append(item)

urllist_new = []

with open('ids.txt', 'w') as f:
    for link in urllist:
        f.write(link + str('\n'))

