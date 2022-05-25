import json

with open('cenz.txt', encoding='utf-8') as r:
    for i in r:
        n = i.split(', ')

with open('cenz.json', 'w', encoding='utf-8') as e:
    json.dump(n,e)