from django.db import models

class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    admin = models.BooleanField(default=False)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"

class Pedidos(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True, blank=True)
    entregado = models.BooleanField(default=False)
    detalle = models.CharField(max_length=100)
    medida = models.CharField(max_length=15)
    abono = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    por_pagar = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido de {self.usuario.nombre if self.usuario else 'Usuario no registrado'} - {self.fecha_pedido}"

    @classmethod
    def crear_pedido(cls, nombre, direccion, otros_campos_pedido=None):
        usuario = None

        if nombre:
            try:
                usuario = Usuarios.objects.get(nombre=nombre)
            except Usuarios.DoesNotExist:
                pass

        pedido = cls(usuario=usuario, direccion=direccion, **otros_campos_pedido)
        pedido.save()
        return pedido