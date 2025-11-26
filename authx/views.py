from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer
from config import global_parameter as gp
import base64

# Create your views here.

# This is for Register Logic
class RegisterViewAPI(APIView):

    def get(self, request):
        users = User.objects.filter(is_active=True)
        serializer = RegisterSerializer(users, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                msg = {
                    gp.RESPONSE_CODE_KEY : gp.SUCCESS_CODE,
                    gp.RESPONSE_KEY : gp.RESPONSE_SUCCESS_MSG,
                    gp.DATA : serializer.data
                }
                return Response(msg, status=201)
            else:
                msg={
                    gp.RESPONSE_CODE_KEY : gp.UNSUCCESS_CODE,
                    gp.DATA : serializer.error
                }
                return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exe:
            msg={
                gp.RESPONSE_ERROR : gp.INTERNAL_SERVER_ERROR
            }
            return Response(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# This class is for Login logic
class LoginViewApi(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        try:
            auth_header = request.META["HTTP_AUTHORIZATION"]
            enconded_data = auth_header.split(" ")[1]
            decoded_data = base64.b64decode(enconded_data).decode('utf-8')
            data = decoded_data.split(":")
            username = data[0]
            password = data[1]

            user = authenticate(username=username, password=password)
            # JWT TOKEN ADD
            if user:
                refresh = RefreshToken.for_user(user)
                refresh_token = str(refresh)
                return Response({
                    'refresh' : refresh_token
                })
            msg={
                gp.RESPONSE_ERROR : "Invalid username and password"
            }
            return Response(msg, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as exe:
            msg = {
                "response": "Internal server Error"
            }
            return Response(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
