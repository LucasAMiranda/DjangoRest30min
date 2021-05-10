from rest_framework import serializers
from .models import Cliente

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'endereco', 'idade']