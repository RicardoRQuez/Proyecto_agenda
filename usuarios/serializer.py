from rest_framework import serializers
from .models import Usuarios, Pedidos


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

class PedidosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pedidos
        fields = '__all__'

    def create(self, validated_data):
        # Extrae los datos del usuario de los datos validados
        usuario_data = validated_data.pop('usuario', None)

        # Crea el pedido sin el campo usuario
        pedido = Pedidos.objects.create(**validated_data)

        # Asigna el usuario al pedido si se proporciona
        if usuario_data:
            usuario = Usuarios.objects.create(**usuario_data)
            pedido.usuario = usuario
            pedido.save()

        return pedido