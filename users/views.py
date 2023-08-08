from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.serializers import MyTokenObtainPairSerializer


class TokenObtain(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
