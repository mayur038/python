from django.urls import path
from . import views
#URLCONF
urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register,name='register'),
    path('shello/',views.say_hello,name='shello'),
    path('login/',views.login,name='login'),
    path('post/<int:pk>',views.post,name='post')
]