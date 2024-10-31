from django.shortcuts import render
from billing.forms import ArquivoForm, ContaForm, FornecedorForm, LancamentoForm


def home(request):
    return render(request, 'billing/home.html')


def billing_view(request):
    return render(request, 'billing/billing.html')


def dashboard_view(request):
    context = {
        'indicadores': {
            'total_fornecedores': 10,  # exemplo
            'total_contas': 5,         # exemplo
            'total_lancamentos': 20,    # exemplo
        },
    }
    return render(request, 'billing/dashboard.html', context)

def fornecedor_create(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redireciona para o dashboard após salvar
    else:
        form = FornecedorForm()
    return render(request, 'billing/fornecedor_form.html', {'form': form})

# View para cadastrar conta
def conta_create(request):
    if request.method == 'POST':
        form = ContaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ContaForm()
    return render(request, 'billing/conta_form.html', {'form': form})

# View para cadastrar lançamento
def lancamento_create(request):
    if request.method == 'POST':
        form = LancamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = LancamentoForm()
    return render(request, 'billing/lancamento_form.html', {'form': form})

# View para cadastrar arquivo
def arquivo_create(request):
    if request.method == 'POST':
        form = ArquivoForm(request.POST, request.FILES)  # Inclui arquivos
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ArquivoForm()
    return render(request, 'billing/arquivo_form.html', {'form': form})