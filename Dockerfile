# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho na imagem
WORKDIR /app

# Copia o arquivo de requisitos para a imagem e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação para o diretório de trabalho
COPY . .

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Expõe a porta do Django
EXPOSE 8000

# Comando para iniciar o servidor de desenvolvimento do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
