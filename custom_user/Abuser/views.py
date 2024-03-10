from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import Registerserializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .views import *
from rest_framework.decorators import api_view

from .serializer import *

from rest_framework import generics
# Create your views here.
class RegisterView(APIView):
    def post(self,request):
        
        try:
            serializer = Registerserializer(data=request.data)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':404,
                    'message':"hel",
                    'message':serializer.errors
                })
            serializer.save()
            return Response({'status':200,'message':'an otp has been sent on your mail'})
        except Exception as e:
            # print(e)
            return Response({'status':44,'message':str(e)})