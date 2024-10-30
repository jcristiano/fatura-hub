# FaturaHub

FaturaHub é um sistema de gestão de fornecedores, contas e lançamentos de faturas. Com o FaturaHub, você pode organizar e monitorar suas faturas e comprovantes de serviços, como energia elétrica, telefonia, internet e muito mais.

## Funcionalidades

- **Cadastro de Fornecedores:** Registre informações sobre fornecedores de serviços, como nome, CNPJ e contatos.
- **Gestão de Contas/Instalações:** Associe diferentes contas ou instalações a fornecedores (por exemplo, várias propriedades associadas a uma mesma empresa de energia).
- **Lançamentos de Faturas:** Realize lançamentos mensais de contas com valor total, vencimento e status de pagamento.
- **Anexos e Comprovantes:** Anexe arquivos (boletos, comprovantes, etc.) a cada lançamento, categorizando-os para facilitar o acesso.
- **Itens de Compra:** Detalhe itens incluídos nas faturas, como quantidades e valores individuais.

## Tecnologias

- **Backend:** Django (Arquitetura MVT)
- **Frontend:** Django Templates, com Bootstrap ou Tailwind CSS (escolha sua preferência)
- **Banco de Dados:** PostgreSQL (ou SQLite para desenvolvimento)
- **Upload de Arquivos:** Sistema de Arquivos Local (ou AWS S3 para produção)

## Estrutura de Modelos

- `Fornecedor`: Representa os fornecedores de serviço.
- `Conta`: Representa contas associadas a fornecedores.
- `Lancamento`: Representa lançamentos de contas ou faturas de serviços.
- `Arquivo`: Representa arquivos anexados aos lançamentos (boletos, comprovantes, etc.).
- `Item`: Representa itens detalhados dentro de um lançamento.

## Instalação

Siga estas etapas para configurar o projeto localmente.

### Pré-requisitos

- Python 3.x
- Django 4.x
- PostgreSQL (ou SQLite para testes locais)

### Passo a Passo

1. **Clone este repositório:**

   ```bash
   git clone https://github.com/seuusuario/faturahub.git
   cd faturahub

