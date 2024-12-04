from django.db import models
from pathlib import Path
import uuid

class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    nome = models.CharField(max_length=100, verbose_name="Nome")
    descricao = models.TextField(max_length=2000, verbose_name="Descrição")
    quantidade = models.IntegerField(verbose_name="Quantidade")
    data = models.DateField(verbose_name="Data")
    foto = models.ImageField(upload_to="estoque/fotos/", blank=True, null=True, verbose_name="Foto")
    criado_em = models.DateField(auto_now_add=True, verbose_name="Data de Criação")
    editado_em = models.DateField(auto_now=True, verbose_name="Data de Edição")

    def __str__(self):
        return self.nome
    
    def delete(self, *args, **kwargs):
        foto = self.foto
        super().delete(*args, **kwargs)
        if foto:
            Path(foto.path).unlink(missing_ok=True)