from django.urls import path
from .views import RegisterViewAPI, LoginViewApi
from rest_framework_simplejwt.views import TokenRefreshView 


urlpatterns = [
    path('register/', RegisterViewAPI.as_view(), name='register'),
    path('login/', LoginViewApi.as_view(), name="login"),
    path('login/refresh', TokenRefreshView.as_view(), name="refresh")
]
