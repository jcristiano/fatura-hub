from django.contrib import admin
from .models import Fornecedor, Conta, Lancamento, Arquivo

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj')  # Campos a serem exibidos na lista
    search_fields = ('nome', 'cnpj')  # Campos que podem ser pesquisados

class ContaAdmin(admin.ModelAdmin):
    list_display = ('fornecedor', 'numero', 'tipo')  # Campos a serem exibidos na lista
    search_fields = ('fornecedor__nome', 'numero')  # Pesquisa pelo nome do fornecedor

class LancamentoAdmin(admin.ModelAdmin):
    list_display = ('conta', 'data', 'valor_total', 'status_pagamento')  # Campos a serem exibidos na lista
    list_filter = ('status_pagamento',)  # Filtro por status de pagamento

class ArquivoAdmin(admin.ModelAdmin):
    list_display = ('lancamento', 'categoria', 'data_upload')  # Campos a serem exibidos na lista
    search_fields = ('categoria',)

# Registro dos modelos no Django Admin com classes personalizadas
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Conta, ContaAdmin)
admin.site.register(Lancamento, LancamentoAdmin)
admin.site.register(Arquivo, ArquivoAdmin)