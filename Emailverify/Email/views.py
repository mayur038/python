from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from serializer import *
from rest_framework.response import Response
# Create your views here.
def fun(request):
    return HttpResponse("Hell Wold")

class RegisterView(APIView):
    def post(self,request):
        try:
            serializer = Registerserializer(data=request.data)

            if not serializer.is_valid():
                return Response(
                    {
                        'status':404,
                        'erro':'something went wrong',
                    }
                )
            serializer.save()
            return Response({'status':200,'message':'otp has been sent'})
        except Exception as e:
            print(e)