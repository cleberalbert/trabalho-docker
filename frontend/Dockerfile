# Usar uma imagem oficial do Node.js para construir o frontend
FROM node:14

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto
COPY . .

# Instalar as dependências do React
RUN npm install

# Construir o frontend
RUN npm run build

# Usar o NGINX para servir o frontend
FROM nginx:alpine
COPY --from=0 /app/build /usr/share/nginx/html