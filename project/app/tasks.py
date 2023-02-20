from celery import shared_task
import requests
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import random
import json
channel_layer = get_channel_layer()
jokes = [
     "Why do programmers always mix up Halloween and Christmas? Because Oct 31 equals Dec 25",
     "There are only 10 kinds of people in this world: those who know binary and those who don’t",
     "A programmer walks to the butcher shop and buys a kilo of meat.  An hour later he comes back upset that the butcher shortchanged him by 24 grams.",
     "Programming is 10% science, 20% ingenuity, and 70% getting the ingenuity to work with the science",
     "Programming is like sex:One mistake and you have to support it for the rest of your life."
]
@shared_task
def add():
    # url = 'http://api.icdb.com/jokes/random/'
    # res = requests.get(url).json()
    # joke = res['value']['joke']
    # print(joke)
    print(jokes[random.randint(0, 4)])
    async_to_sync(channel_layer.group_send)('chat',{
        'type':'send.msg',
        'msg': jokes[random.randint(0, 4)]
    }) 

