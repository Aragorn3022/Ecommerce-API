from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import status, permissions


class  MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)

class MyTokenRefreshView(TokenRefreshView):
    permission_classes = (permissions.AllowAny,)