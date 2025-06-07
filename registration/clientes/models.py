# clientes/models.py (do projeto Costumer_registration)

from django.db import models
from django.core.exceptions import ValidationError
import re

def validate_telefone(value):
    """
    Validador customizado para o formato do Telefone.
    Permite apenas números e os caracteres +, -, (, ).
    """
    # Remove os caracteres permitidos para verificar se sobram apenas números
    cleaned_value = value.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
    if not cleaned_value.isdigit():
        raise ValidationError('Telefone inválido. Utilize apenas números e os caracteres +, -, (, ).')

class Cliente(models.Model):
    """
    Modelo para representar um cliente.
    """
    nome = models.CharField(max_length=100, help_text="Nome completo do cliente")
    email = models.EmailField(unique=True, help_text="Endereço de e-mail do cliente")
    telefone = models.CharField(
        max_length=20, 
        blank=True, 
        null=True, 
        help_text="Número de telefone do cliente (opcional)",
        validators=[validate_telefone] # Validador adicionado aqui
    )
    data_cadastro = models.DateTimeField(auto_now_add=True, help_text="Data de cadastro do cliente")

    def __str__(self):
        """
        Retorna uma representação em string do objeto Cliente.
        """
        return self.nome

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nome']
