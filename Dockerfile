# Use a imagem base oficial do Python
FROM python:3.12-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para o diretório de trabalho
COPY . .

# Exponha a porta que a aplicação vai rodar (ajuste conforme necessário)
ENV HOST 0.0.0.0
ENV PORT 8000

EXPOSE ${PORT}

# Comando para rodar a aplicação
CMD ["gunicorn", "app:app", "--host", "${HOST}}", "--port", "${PORT}}"]
