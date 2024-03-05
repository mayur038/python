from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .views import *
from rest_framework.decorators import api_view
from .models import Student,subjects
from .serializer import *
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics

# Create your views here.

# Token authentication
class Register(APIView):
    def post(self,request):
        serializer = Registerserializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status':403,'error':serializer.errors,'message':'error occured'})
        
        serializer.save()
        user = User.objects.get(phone = serializer.data['phone'])

        Token_obj ,_ = Token.objects.get_or_create(user=user)
        return Response({'status':100,'data':serializer.data,'token':str(Token_obj),'message':'token'})

class TestView(APIView):
    authentication_classes = [ JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,*arg,**kwargs):
        data = {
            'phone':'admin',
            'years_active':10
        }
        return Response(data)

@api_view(['GET'])
def testt(request):
    data ={
        "status":300,
        "data":data,
        "message":'sended'
    }
    return Response(data)

@api_view(['GET'])
def StudentS(request):
 
    student = Student.objects.all()
    serializers = StudentSerializer(student,many=True)
    serializers.validate
    return Response({'status':202,'data':serializers.data,'message':'hello fucking shit'})

# class TestRegister(APIView):
#     def post(self,request):
#         serialize = Registerserializer(data=request.data)

#         if not serialize.is_valid():
#             return Response({'status': 403 ,'error':serialize.errors})
        
#         serialize.save()
#         user = User.objects.get(phone=serialize.data['phone'])
#         refresh = RefreshToken.for_user(user)
#         # token = Token.objects.get_or_create(user)
#         return Response({'status':232,'refresh': str(refresh),
#         'access': str(refresh.access_token),'data':serialize.data})
    

class Generics_class_Demo(generics.ListAPIView , generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Generics_class_update(generics.UpdateAPIView , generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'