from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Bay
from .serializers import BaySerializer
from django.db.migrations import serializer
from .consumers import ChatConsumer

from channels.layers import get_channel_layer
import asyncio

# Create your views here.


class First(APIView):
    def get(self,request):
        post=[{
            "name":"myname"
        }]
        
        bay = Bay.objects.all()
        serializer= BaySerializer(bay,many=True)
        
        return Response(serializer.data)
        # return Response(post)
        
        
from asgiref.sync import async_to_sync
class MakeBusy(APIView):
    def get(self,request,id):
        print("makebusy")
        sam = Bay.objects.filter(id=id).update(status="Busy")
        self.bay=Bay.objects.all()
        
        serialize = BaySerializer(self.bay,many=True)
        print(serialize.data)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "test",
            {
                'type':'chat_message',
                'message':serialize.data
            }
        )
        
        
        return Response(200)
    
from asgiref.sync import async_to_sync
class MakeFree(APIView):
    def get(self,request,id):
        print("Makefree")
        sam = Bay.objects.filter(id=id).update(status="Free")
        self.bay=Bay.objects.all()
        
        serialize = BaySerializer(self.bay,many=True)
        print(serialize.data)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "test",
            {
                'type':'chat_message',
                'message':serialize.data
            }
        )
        return Response(200)