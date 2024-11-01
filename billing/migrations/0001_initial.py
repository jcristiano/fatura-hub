# Generated by Django 5.1.2 on 2024-10-30 23:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=14, unique=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('contato', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=50)),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contas', to='billing.fornecedor')),
            ],
        ),
        migrations.CreateModel(
            name='Lancamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status_pagamento', models.BooleanField(default=False)),
                ('vencimento', models.DateField()),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lancamentos', to='billing.conta')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('quantidade', models.IntegerField()),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lancamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='billing.lancamento')),
            ],
        ),
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50)),
                ('arquivo', models.FileField(upload_to='uploads/')),
                ('data_upload', models.DateTimeField(auto_now_add=True)),
                ('lancamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arquivos', to='billing.lancamento')),
            ],
        ),
    ]
