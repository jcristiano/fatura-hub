from django import forms
from .models import Fornecedor, Conta, Lancamento, Arquivo

from django.core.exceptions import ValidationError

import re


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'cnpj', 'descricao', 'contato']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'contato': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')

        # Remove caracteres não numéricos
        cnpj = re.sub(r'\D', '', cnpj)

        # Verifica se o CNPJ resultante tem 14 dígitos
        if len(cnpj) != 14:
            raise ValidationError("CNPJ deve ter 14 dígitos.")

        # Validação do CNPJ
        if not self.is_valid_cnpj(cnpj):
            raise ValidationError("CNPJ inválido.")

        return cnpj


    def is_valid_cnpj(self, cnpj):
        # Aqui você pode implementar a lógica de validação do CNPJ.
        # Esta é uma implementação básica.
        
        if cnpj in ["00000000000000", "11111111111111", "22222222222222", "33333333333333",
                    "44444444444444", "55555555555555", "66666666666666", "77777777777777",
                    "88888888888888", "99999999999999"]:
            return False

        def calculate_check_digit(cnpj, length):
            digits = [int(d) for d in cnpj[:length]]
            weight = 2
            total = 0
            for i in range(length - 1, -1, -1):
                total += digits[i] * weight
                weight += 1
                if weight > 9:
                    weight = 2
            remainder = total % 11
            return 0 if remainder < 2 else 11 - remainder

        first_check_digit = calculate_check_digit(cnpj, 12)
        second_check_digit = calculate_check_digit(cnpj + str(first_check_digit), 13)

        return cnpj == cnpj[:12] + str(first_check_digit) + str(second_check_digit)


class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = ['fornecedor', 'numero', 'endereco', 'tipo']
        widgets = {
            'fornecedor': forms.Select(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
        }


class LancamentoForm(forms.ModelForm):
    class Meta:
        model = Lancamento
        fields = ['conta', 'data', 'valor_total',
                  'status_pagamento', 'vencimento']
        widgets = {
            'conta': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'valor_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'status_pagamento': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'vencimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class ArquivoForm(forms.ModelForm):
    class Meta:
        model = Arquivo
        fields = ['lancamento', 'categoria', 'arquivo']
        widgets = {
            'lancamento': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'arquivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
