import jwt
from rest_framework import authentication,exceptions
from django.conf import settings

from .models import Account


class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        prefix,token= auth_data.decode('utf-8').split(' ')

        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY)

            account = Account.objects.get(email=payload['email'])

            return (account, token)
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed("Your Token is invalid, login")
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("Your Token is expired, login")

        return super(JWTAuthentication, self).authenticate(request)
