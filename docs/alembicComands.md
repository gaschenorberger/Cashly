# Comandos do Alembic

## Preparar o terminal local

Com o PostgreSQL do Docker rodando:

```powershell
docker compose up -d postgres
$env:DATABASE_URL="postgresql://cashly_user:123@localhost:5433/cashly_db"
```

## Criar uma migration nova

```powershell
alembic revision -m "adicionar categorias padrao"
```

O arquivo será criado em `migrations/versions/`. Depois, escreva manualmente as operações nas funções `upgrade()` e `downgrade()`.

> Não utilize `--autogenerate` neste projeto atualmente, pois não há `target_metadata` configurado.

## Aplicar todas as migrations pendentes

```powershell
alembic upgrade head
```

## Aplicar apenas a próxima migration

```powershell
alembic upgrade +1
```

## Ver a migration aplicada no banco

```powershell
alembic current
```

## Ver o histórico de migrations

```powershell
alembic history
```

Para exibir mais detalhes:

```powershell
alembic history --verbose
```

## Ver a migration mais recente do projeto

```powershell
alembic heads
```

## Ver detalhes de uma migration

Para visualizar a migration mais recente:

```powershell
alembic show head
```

Para visualizar uma migration pelo ID:

```powershell
alembic show e6dc63a9aa30
```

## Desfazer a última migration

```powershell
alembic downgrade -1
```

## Voltar até uma migration específica

```powershell
alembic downgrade e6dc63a9aa30
```

## Voltar todas as migrations

```powershell
alembic downgrade base
```

> **Cuidado:** esse comando pode excluir todas as tabelas criadas pelas migrations.

## Aplicar uma migration específica

```powershell
alembic upgrade ID_DA_MIGRATION
```

Exemplo:

```powershell
alembic upgrade e6dc63a9aa30
```

## Gerar o SQL sem executar

```powershell
alembic upgrade head --sql
```

## Aplicar migrations em outro computador

As migrations fazem parte do código e são obtidas pelo Git. Depois, devem ser aplicadas no banco de dados.

```powershell
git pull
docker compose up -d postgres
pip install -r requirements.txt
$env:DATABASE_URL="postgresql://cashly_user:123@localhost:5433/cashly_db"
alembic upgrade head
```

Também é possível construir e iniciar todos os serviços de uma vez:

```powershell
git pull
docker compose up --build
```

Nesse caso, o serviço `migrate` executará automaticamente:

```powershell
alembic upgrade head
```

## Criar a migration das categorias padrão

Se a migration `e6dc63a9aa30` já foi aplicada ou compartilhada, não altere o arquivo antigo. Crie uma migration nova:

```powershell
alembic revision -m "adicionar categorias padrao"
```

Depois, adicione manualmente os comandos de inserção no `upgrade()` e a operação inversa no `downgrade()`.