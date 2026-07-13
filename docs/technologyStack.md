# Stack Tecnológica — Cashly

## ST01 — Backend

O backend do Cashly será desenvolvido utilizando:

- Python
- FastAPI

O Python será utilizado como linguagem principal do backend.

O FastAPI será utilizado para desenvolver a API responsável pelas regras de negócio, autenticação, validação dos dados e comunicação com o banco de dados.

## ST02 — Frontend

O frontend do Cashly será desenvolvido utilizando:

- React
- TypeScript
- Vite

O React será utilizado para construir a interface web por meio de componentes reutilizáveis.

O TypeScript será utilizado para adicionar tipagem ao código do frontend, facilitando a manutenção e reduzindo erros durante o desenvolvimento.

O Vite será utilizado para criar, executar e gerar a versão de produção do projeto frontend.

## ST03 — Banco de dados

O banco de dados utilizado será:

- PostgreSQL

O PostgreSQL será responsável pelo armazenamento dos usuários, categorias, transações e demais informações financeiras do sistema.

Os valores financeiros serão armazenados utilizando tipos decimais apropriados, evitando o uso de tipos imprecisos.

## ST04 — ORM

A comunicação entre o backend e o banco de dados será realizada utilizando:

- SQLAlchemy

O SQLAlchemy será utilizado para representar as tabelas do banco por meio de models Python, realizar consultas e controlar as operações de persistência.

## ST05 — Migrations

O controle de alterações na estrutura do banco de dados será realizado utilizando:

- Alembic

O Alembic será utilizado para criar e executar migrations, permitindo que mudanças nas tabelas sejam registradas e aplicadas de forma controlada.

## ST06 — Validação de dados

A validação dos dados recebidos e retornados pela API será realizada utilizando:

- Pydantic

O Pydantic será utilizado para definir schemas, validar os dados das requisições e controlar os dados retornados pelas rotas da API.

## ST07 — Autenticação

A autenticação será implementada utilizando:

- OAuth2 com Bearer Token
- JWT
- PyJWT

Após realizar o login, o usuário receberá um token JWT que deverá ser enviado nas requisições para acessar rotas protegidas.

O PyJWT será utilizado para criar, validar e decodificar os tokens.

## ST08 — Segurança das senhas

As senhas serão protegidas utilizando:

- pwdlib
- Argon2

As senhas não serão armazenadas em texto puro.

Antes de serem salvas no banco de dados, serão transformadas em hashes utilizando Argon2.

## ST09 — Comunicação entre frontend e backend

A comunicação do frontend com a API será realizada utilizando:

- Axios

O Axios será utilizado para enviar requisições HTTP, configurar a URL base da API e adicionar o token de autenticação nas requisições protegidas.

## ST10 — Estilização da interface

A estilização inicial do Cashly será desenvolvida utilizando:

- CSS Modules

Os estilos serão organizados por componente, reduzindo conflitos de nomes entre classes e mantendo a interface separada em módulos.

A adoção de outra biblioteca visual poderá ser avaliada posteriormente caso o projeto necessite de componentes mais complexos.

## ST11 — Gráficos

Os gráficos do dashboard serão desenvolvidos utilizando:

- Recharts

O Recharts será utilizado para representar visualmente informações como gastos por categoria, entradas, saídas e evolução financeira mensal.

## ST12 — Testes do backend

Os testes automatizados do backend serão desenvolvidos utilizando:

- pytest

O pytest será utilizado para criar testes unitários e testes de integração das regras de negócio, services, repositories e endpoints da API.

## ST13 — Documentação da API

A documentação dos endpoints será gerada automaticamente pelo FastAPI utilizando:

- OpenAPI
- Swagger UI

A documentação permitirá visualizar, testar e entender as rotas disponibilizadas pelo backend.

## ST14 — Controle de versão

O controle de versão do projeto será realizado utilizando:

- Git
- GitHub

O Git será utilizado para registrar as alterações realizadas no código.

O GitHub será utilizado para armazenar o repositório remoto e organizar a evolução do projeto.

## ST15 — Gerenciamento do projeto

O planejamento e acompanhamento do desenvolvimento serão realizados utilizando:

- Trello

O Trello será utilizado para organizar o backlog geral, as sprints, as tarefas em desenvolvimento e os cartões concluídos.

## ST16 — Ambiente de desenvolvimento

As principais ferramentas utilizadas durante o desenvolvimento serão:

- Visual Studio Code
- pgAdmin
- Swagger UI
- Git

O Visual Studio Code será utilizado como editor principal.

O pgAdmin será utilizado para visualizar e administrar o banco de dados PostgreSQL.

## ST17 — Containerização e deploy

A containerização será realizada futuramente utilizando:

- Docker
- Docker Compose

O Docker não será obrigatório nas primeiras sprints do projeto.

Ele será adicionado posteriormente para padronizar a execução do frontend, backend e banco de dados.

As plataformas de deploy serão definidas em uma etapa futura, após a conclusão das principais funcionalidades do MVP.

## Resumo da stack

Backend: Python e FastAPI

Frontend: React, TypeScript e Vite

Banco de dados: PostgreSQL

ORM: SQLAlchemy

Migrations: Alembic

Validação: Pydantic

Autenticação: OAuth2, JWT e PyJWT

Hash de senhas: pwdlib com Argon2

Comunicação HTTP: Axios

Estilização: CSS Modules

Gráficos: Recharts

Testes: pytest

Documentação da API: OpenAPI e Swagger UI

Controle de versão: Git e GitHub

Gerenciamento: Trello

Containerização futura: Docker e Docker Compose