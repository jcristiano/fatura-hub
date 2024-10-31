from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('billing/', views.billing_view, name='billing'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('fornecedor/create/', views.fornecedor_create, name='fornecedor_create'),
    path('conta/create/', views.conta_create, name='conta_create'),
    path('lancamento/create/', views.lancamento_create, name='lancamento_create'),
    path('arquivo/create/', views.arquivo_create, name='arquivo_create'),
]
