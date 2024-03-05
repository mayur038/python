from django.urls import path
from . import views as ss
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
#URLCONF
urlpatterns = [
    # path('', ss.TestView.as_view(), name='index'),
    # # path('api-token-auth/', views.obtain_auth_token),
    # # path('authview/', ss.StudentS, name='auth'),
    # path('register/', ss.Register.as_view(), name='register'),
    # path('Redirect/', ss.TestRegister.as_view(), name='redirect'),

    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 


#   generic clas
    path('generic-student/',ss.Generics_class_Demo.as_view(),name='generic'),
    path('generic-student/<id>',ss.Generics_class_update.as_view(),name='generic'),
]