from rest_framework import serializers

from bio.models import Perfil, Denuncia, Usuario

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ('id','Nombre', 'IdEstado')

class DenunciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denuncia
        fields = ('id','Descripcion', 'Observacion', 'Imagen', 'EstadoDenuncia', 'Georeferencia')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','UserName', 'Nombre', 'Apellido', 'FechaNacimiento', 'EstadoId')