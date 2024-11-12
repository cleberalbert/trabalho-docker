# Fase de construção
FROM node:14 AS build

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . ./
RUN npm run build

# Servindo o build com NGINX
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
RUN chown -R nginx:nginx /usr/share/nginx/html  # Ajusta as permissões para o NGINX
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
