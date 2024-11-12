FROM python:3.9

WORKDIR /app

# Copia todos os arquivos para o container
COPY . /app/

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 5000
EXPOSE 5000

# Define variáveis de ambiente para o Flask 
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Comando para iniciar a aplicação
CMD ["flask", "run"]
