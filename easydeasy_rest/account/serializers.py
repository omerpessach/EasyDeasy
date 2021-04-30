from rest_framework.serializers import ModelSerializer,EmailField, CharField

from .models import Account


class AccountSerializer(ModelSerializer):
    password = CharField(write_only=True)
    email = EmailField()

    class Meta:
        model = Account
        fields = '__all__'
