import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer import model_observer




from channels.db import database_sync_to_async
from .models import Bay
from .serializers import BaySerializer

# class ChatConsumer(ListModelMixin,GenericAsyncAPIConsumer):
#     queryset: Bay.objects.all()
#     serializer_class: BaySerializer
#     async def connect(self, **kwargs):
#         await self.model_change.subscribe()
#         await super().connect()
    
#     @model_observer(Bay)
#     async def model_change(self,message,observer=None,**kwrgs):
#         await self.send_json(message)

#     @model_change.serializer
#     def model_serialize(self,instance, action, **kwrgs):
#         return dict(data=BaySerializer(instance=instance).data, action=action.value)






class ChatConsumer(AsyncWebsocketConsumer):
    
    def get_data(self):
        self.bay=Bay.objects.all()
        
        serialize = BaySerializer(self.bay,many=True)
        
        return serialize.data
    
    
    async def connect(self):
        self.room_group_name = 'test'
        await(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        print("connect")
        msg= await database_sync_to_async(self.get_data)()
        print(msg)
        await(self.channel_layer.group_send)(
            self.room_group_name,{
                'type':'chat_message',
                'message':msg
            }
        )
        

    async def receive(self,text_data):
        text_data_json = json.loads(text_data)
        message= text_data_json['message']
        await(self.channel_layer.group_send)(
            self.room_group_name,{
                'type':'chat_message',
                'message':message
            }
        )
    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
            
        }))
        