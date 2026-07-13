# Regras de Negócio — Cashly

## RN01 — Propriedade dos dados

Cada usuário deve acessar apenas suas próprias transações, categorias e informações financeiras.

## RN02 — Tipos de transação

Toda transação deve possuir um dos seguintes tipos:

- Entrada
- Saída

Uma transação não pode possuir os dois tipos simultaneamente.

## RN03 — Cálculo do saldo

O saldo do usuário será calculado pela fórmula:

Saldo = total de entradas - total de saídas

O saldo será calculado com base nas transações registradas.

## RN04 — Campos obrigatórios da transação

Toda transação deve possuir:

- Descrição
- Valor
- Tipo
- Categoria
- Data da transação
- Usuário responsável

## RN05 — Valores financeiros

O valor de uma transação deve ser maior que zero.

Valores financeiros devem utilizar precisão decimal de duas casas.

Exemplo:

R$ 150,90

Não deve ser utilizado tipo float para armazenar dinheiro.

## RN06 — Categorias

Toda transação deve estar vinculada a uma categoria.

As categorias podem ser:

- Padrão do sistema
- Personalizadas pelo usuário

Uma categoria de entrada não deve ser utilizada em uma transação de saída, salvo quando a categoria for definida para ambos os tipos.

## RN07 — Exclusão de categorias

Uma categoria que já estiver vinculada a transações não deve ser excluída diretamente.

O sistema poderá:

- Impedir a exclusão
- Solicitar que as transações sejam movidas para outra categoria
- Permitir apenas a desativação da categoria

A decisão inicial recomendada para o MVP é impedir a exclusão.

## RN08 — Datas

Toda transação deve possuir uma data de referência.

A data da transação representa quando a movimentação financeira ocorreu.

O sistema deve armazenar também:

- Data de criação do registro
- Data da última atualização

A data da transação pode ser diferente da data em que o registro foi criado.

## RN09 — Segurança

Senhas nunca devem ser armazenadas em texto puro.

Cada usuário deve estar autenticado para acessar seus dados financeiros.