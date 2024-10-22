# Usar uma imagem base oficial do Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos de código para o container
COPY . .

# Instalar as dependências necessárias
RUN pip install -r requirements.txt

# Expor a porta que a aplicação Flask usará
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["python", "app.py"]