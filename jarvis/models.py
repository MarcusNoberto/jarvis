from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=200)
    ativo = models.BooleanField(default=True)
    data_de_saida = models.DateField(blank=True, null=True)
    cpf = models.CharField(primary_key=True, max_length=11, unique=True)
    telefone = models.CharField(max_length=30)
    email_lsd = models.EmailField(max_length=100, blank=True, null=True, )
    email_pessoal = models.EmailField(max_length=100, blank=True, null=True)
    lattes = models.CharField(max_length=500, blank=True, null=True)
    sala = models.CharField(max_length=100)
    chave = models.BooleanField(default=False)