from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from djrestfm.models  import *
from features.helper import *
import  datetime as d
from djrestfm.serializer import *

import uuid 
import pandas as pd

from django.conf import settings

from features.models import ExportCSV

# Create your views here.
class PDF_view(APIView):
    def get(self,request):
        st = Student.objects.all()
        params = {
            'date': d.date.today(),
            'data': st,
            'message':'student data'
        }

        file_name , status = save_pdf(params)

        if not status:
            return Response({'status':404,'message':'failed'})


        return Response({'status':200,'filename':f'/media/{file_name}.pdf'})


class ImportExportExcel(APIView):
    def get(self,request):

        data = Student.objects.all()
        serializer = StudentSerializer(data,many=True)
        df = pd.DataFrame(serializer.data)
     
        print(df)
        df.to_csv(f"public/static/{uuid.uuid4()}.csv",encoding='UTF-8',index=False)
        return Response({'status':200})

    def post(self,request):
        excel_obj     = ExportCSV.objects.create(ExportFile=request.FILES['files'])
        


        df = pd.read_csv(f"{settings.BASE_DIR}/public/static/{excel_obj.ExportFile}")

        for x in df.values:

            print(x)
        return Response({'status':200})
class Email(APIView):
    def post(self,request):
        return Response({'status': 200,'text':'hello'})
