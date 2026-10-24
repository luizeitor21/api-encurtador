import random
import string
from django.db import models

# Create your models here.
def gerar_codigo():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(6))

class Link(models.Model):
    url_original = models.URLField(max_length=500)
    codigo = models.CharField(max_length=6, unique=True, default=gerar_codigo)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.codigo} -> {self.url_original}"