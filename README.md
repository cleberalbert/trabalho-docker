
```markdown
# Projeto Guess Game com Docker Compose

Este projeto é uma implementação de uma aplicação de adivinhação de números, usando Docker Compose para orquestrar seus componentes. A aplicação é composta por um backend em Python com Flask, um frontend em React, um banco de dados Postgres e um servidor NGINX como proxy reverso e balanceador de carga.

## Estrutura do Projeto

O projeto é organizado nos seguintes componentes principais:

1. **Backend (Python + Flask):**
   - Implementa a lógica do jogo de adivinhação.
   - Se conecta ao banco de dados Postgres para salvar os dados do jogo.
   - *Dockerfile do Backend Python:* configura o ambiente necessário.

2. **Frontend (React):**
   - Fornece a interface gráfica para interação do usuário.
   - *Dockerfile do Frontend React:* configura o ambiente do frontend via NGINX.

3. **Banco de Dados (Postgres):**
   - Armazena as informações do jogo de forma persistente.
   - Utiliza volumes Docker para manter a persistência dos dados.

4. **NGINX:**
   - Atua como proxy reverso, servindo o frontend React.
   - Realiza balanceamento de carga entre múltiplas instâncias do backend Flask.
   - *Configuração do NGINX:* define as regras de proxy e balanceamento.

## Requisitos

- Docker 20.10.0 ou superior
- Docker Compose 1.27.0 ou superior

## Instalação e Execução

### Passo 1: Clonar o Repositório

Clone o repositório do jogo de adivinhação no GitHub:

```bash
git clone https://github.com/fams/guess_game.git
cd guess_game
```

### Passo 2: Construir e Iniciar os Serviços

Use Docker Compose para construir e iniciar todos os serviços:

```bash
docker-compose up --build
```

### Passo 3: Acessar a Aplicação

Acesse a aplicação através do navegador no endereço `http://localhost`.

## Decisões de Design

- **Uso de Docker Compose:** Facilita a orquestração de múltiplos serviços, permitindo fácil atualização e escalabilidade.
- **Flask para Backend:** Escolhido pela simplicidade e eficiência na construção de APIs RESTful.
- **React para Frontend:** Oferece uma interface moderna e reativa para a interação do usuário.
- **Postgres para Banco de Dados:** Um banco de dados relacional robusto, que oferece suporte a transações e persistência de dados.
- **NGINX como Proxy Reverso:** Proporciona uma configuração de proxy simples e eficiente, além de balancear a carga entre instâncias do backend, garantindo resiliência e escalabilidade.

## Atualização dos Serviços

Cada componente pode ser facilmente atualizado trocando a versão da imagem Docker associada no arquivo `docker-compose.yml`.

```

