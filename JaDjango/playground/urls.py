from django.urls import path
from . import views
#URLCONF
urlpatterns = [
    
    path('/',views.hello)
]