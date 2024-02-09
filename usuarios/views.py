from rest_framework import viewsets
from .serializer import UsuariosSerializer, PedidosSerializer
from .models import Usuarios, Pedidos

# Create your views here.
class UsuariosView(viewsets.ModelViewSet):
    serializer_class = UsuariosSerializer
    queryset = Usuarios.objects.all()

class PedidosView(viewsets.ModelViewSet):
    serializer_class = PedidosSerializer
    queryset = Pedidos.objects.all()