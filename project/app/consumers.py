import json
from channels.generic.websocket import AsyncWebsocketConsumer 
from asgiref.sync import async_to_sync
from time import sleep
class ChatConsumer(AsyncWebsocketConsumer):
    count = 0
    patti = 1
    async def connect(self):
        print("==================")
        await self.accept()
        # ChatConsumer.count = ChatConsumer.count +1
        await self.channel_layer.group_add("chat", self.channel_name)
         
         
    async def disconnect(self, close_code):
        ChatConsumer.count =  ChatConsumer.count-1
        await self.channel_layer.group_send(
            'chat',
            {
                "type": "chat.message", 
                "message": ChatConsumer.count,
            }
        )
    # Receive message from WebSocket
    async def receive(self, text_data):
        print(text_data)
        a =0
        while a<10:
            await self.channel_layer.group_send(
            'chat',
            {
                'type':'send.msg',
                'msg':str(a)
            }
            )
            sleep(3)
            a =a+1

    async def send_msg(self,event):
        print(event['msg'])
        await  self.send(event['msg'])
    async def chat_message(self, event):
        print(event['message'])
        await self.send(json.dumps("Total Online :- "+str(event['message'])))
         


