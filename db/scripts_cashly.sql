CREATE TABLE usuarios (
    id BIGSERIAL PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    criado_em TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    atualizado_em TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE categorias (
    id BIGSERIAL PRIMARY KEY,
    usuario_id_fk BIGINT,
    nome_categoria VARCHAR(100) NOT NULL,
    criado_em TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    atualizado_em TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT fk_categorias_usuario
        FOREIGN KEY (usuario_id_fk)
        REFERENCES usuarios(id)
        ON DELETE CASCADE
);

CREATE TABLE transacoes (
    id BIGSERIAL PRIMARY KEY,
    usuario_id_fk BIGINT NOT NULL,
    categoria_id_fk BIGINT NOT NULL,
    nome_transacao VARCHAR(255) NOT NULL,
    valor NUMERIC(12, 2) NOT NULL,
    tipo_transacao VARCHAR(10) NOT NULL,
    data_transacao DATE NOT NULL,
    observacao TEXT,
    criado_em TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    atualizado_em TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_transacoes_usuario
        FOREIGN KEY (usuario_id_fk)
        REFERENCES usuarios(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_transacoes_categoria
        FOREIGN KEY (categoria_id_fk)
        REFERENCES categorias(id)
        ON DELETE RESTRICT,
    CONSTRAINT chk_transacoes_valor_positivo
        CHECK (valor > 0),
    CONSTRAINT chk_transacoes_tipo
        CHECK (tipo_transacao IN ('entrada', 'saida'))
);

INSERT INTO usuarios (nome, email, cpf, senha_hash)
VALUES ()