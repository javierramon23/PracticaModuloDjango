from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):

    name = models.CharField(max_length=50)

    description = models.TextField(blank=True, null=True, default="")

    class Meta:

        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=150)

    summary = models.CharField(max_length=250)

    body = models.TextField()

    url = models.URLField(blank=True, null=True)

    publish_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    category = models.ManyToManyField(Category)

    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    # Campo de control para tareas de administracion.
    # Guarda la fecha de creación de un registro dentro de la BD.

    # 'auto_now': Automatically set the field to now every time the object is saved.
    # 'auto_now_add': Automatically set the field to now when the object is first created.
    # Este campo 'por defecto' no se puede EDITAR y NO se mostrará en el Panel de Administración
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
