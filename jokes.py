import requests
import random
import json
res = requests.get('https://v2.jokeapi.dev/joke/Programming,Pun?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single&amount=10')
jokes = json.loads(res.text)['jokes']

joke = jokes[random.randint(0, len(jokes))]['joke']
print(joke)
