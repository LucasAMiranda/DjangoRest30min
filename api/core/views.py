from django.shortcuts import render
from rest_framework import viewsets 
from .models import Cliente
from .serializers import ClienteSerializer

# Create your views here.
# Pega do models e mostra todos na lista Cliente


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
