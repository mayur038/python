
from django.contrib import admin
from django.urls import path
from features import views 
from django.conf import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [


   
    path('',views.PDF_view.as_view(),name='pdf_view' ),
    path('excel_export',views.ImportExportExcel.as_view(),name='excelexport' ),
    path('email',views.Email.as_view(),name='email' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()