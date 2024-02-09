from django.urls import path, include
from rest_framework import routers
from usuarios import views

#api versioning
router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuariosView, 'usuarios')

router_pedidos = routers.DefaultRouter()
router_pedidos.register(r'pedidos', views.PedidosView, 'pedidos')


urlpatterns = [
    path("usuarios/", include(router.urls)),
    path("pedidos/", include(router_pedidos.urls))
]