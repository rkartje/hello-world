import requests
from pprint import pprint as pp

r = requests.get('https://api.github.com/events')
pp(r.content)