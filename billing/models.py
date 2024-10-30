from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, unique=True)
    descricao = models.TextField(blank=True, null=True)
    contato = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Conta(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name='contas')
    numero = models.CharField(max_length=50)
    endereco = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50)  # residencial, comercial, etc.

    def __str__(self):
        return f"{self.numero} - {self.fornecedor.nome}"

class Lancamento(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='lancamentos')
    data = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    status_pagamento = models.BooleanField(default=False)
    vencimento = models.DateField()

    def __str__(self):
        return f"Lançamento de {self.data} - R${self.valor_total}"

class Arquivo(models.Model):
    lancamento = models.ForeignKey(Lancamento, on_delete=models.CASCADE, related_name='arquivos')
    categoria = models.CharField(max_length=50)  # boleto, comprovante, outros
    arquivo = models.FileField(upload_to='uploads/')
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.categoria} - {self.lancamento}"

class Item(models.Model):
    lancamento = models.ForeignKey(Lancamento, on_delete=models.CASCADE, related_name='itens')
    descricao = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def valor_total(self):
        return self.quantidade * self.valor_unitario
