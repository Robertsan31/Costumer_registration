# Generated by Django 5.2.1 on 2025-06-07 13:16

import clientes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['nome'], 'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='data_cadastro',
            field=models.DateTimeField(auto_now_add=True, help_text='Data de cadastro do cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(help_text='Endereço de e-mail do cliente', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(help_text='Nome completo do cliente', max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, help_text='Número de telefone do cliente (opcional)', max_length=20, null=True, validators=[clientes.models.validate_telefone]),
        ),
    ]
