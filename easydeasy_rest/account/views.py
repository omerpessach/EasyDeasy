from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from django.conf import settings
from django.contrib import auth
import jwt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import AccountSerializer
from .models import Account


class LoginView(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        email = data.get('email', '')
        password = data.get('password', '')

        user = auth.authenticate(username=username,password=password,email=email)

        if user:
            auth_token = jwt.encode({'email': user.email},settings.JWT_SECRET_KEY)
            serializer=AccountSerializer(user)

            data={
                'user': serializer.data,
                'token': auth_token
            }
            return Response(data, status=status.HTTP_200_OK)
            #SEND RES
        return Response({'detail': 'Invalid Credentials'}, status= status.HTTP_401_UNAUTHORIZED)