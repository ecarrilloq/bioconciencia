from django.shortcuts import render
from bio.models import Perfil, Denuncia, Usuario
from rest_framework import generics
from bio.serializers import PerfilSerializer, DenunciaSerializer, UsuarioSerializer
# Create your views here.

class PerfilList(generics.ListCreateAPIView):
    serializer_class = PerfilSerializer 
    queryset = Perfil.objects.all()

class PerfilDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PerfilSerializer 
    queryset = Perfil.objects.all()

class DenunciaList(generics.ListCreateAPIView):
    serializer_class = DenunciaSerializer 
    queryset = Denuncia.objects.all()

class DenunciaDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DenunciaSerializer 
    queryset = Denuncia.objects.all()

class UsuarioList(generics.ListCreateAPIView):
    serializer_class = UsuarioSerializer 
    queryset = Usuario.objects.all()

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioSerializer 
    queryset = Usuario.objects.all()