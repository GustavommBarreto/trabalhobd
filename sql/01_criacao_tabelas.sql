-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS gestao_escolar_municipal
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE gestao_escolar_municipal;

-- Tabela de endereços
CREATE TABLE endereco (
    id_endereco INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    logradouro  VARCHAR(120) NOT NULL,
    numero      VARCHAR(10),
    complemento VARCHAR(60),
    bairro      VARCHAR(60),
    cidade      VARCHAR(60) DEFAULT 'Brasília',
    uf          CHAR(2)     DEFAULT 'DF',
    cep         VARCHAR(9)
) ENGINE=InnoDB;

-- Escolas
CREATE TABLE escola (
    id_escola   INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome        VARCHAR(100) NOT NULL,
    tipo        VARCHAR(30),
    telefone    VARCHAR(20),
    email       VARCHAR(100),
    id_endereco INT UNSIGNED NOT NULL,
    CONSTRAINT fk_escola_endereco
        FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco)
        ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Cursos
CREATE TABLE curso (
    id_curso            INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome                VARCHAR(100) NOT NULL,
    nivel               VARCHAR(30),
    carga_horaria_total INT,
    id_escola           INT UNSIGNED NOT NULL,
    CONSTRAINT fk_curso_escola
        FOREIGN KEY (id_escola) REFERENCES escola(id_escola)
        ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Professores
CREATE TABLE professor (
    id_professor    INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome            VARCHAR(100) NOT NULL,
    cpf             CHAR(11) UNIQUE,
    data_nascimento DATE,
    email           VARCHAR(100),
    telefone        VARCHAR(20),
    id_escola       INT UNSIGNED NOT NULL,
    id_endereco     INT UNSIGNED,
    CONSTRAINT fk_professor_escola
        FOREIGN KEY (id_escola) REFERENCES escola(id_escola)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_professor_endereco
        FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco)
        ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB;

-- Responsáveis
CREATE TABLE responsavel (
    id_responsavel INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome           VARCHAR(100) NOT NULL,
    parentesco     VARCHAR(50),
    telefone       VARCHAR(20),
    email          VARCHAR(100),
    id_endereco    INT UNSIGNED,
    CONSTRAINT fk_responsavel_endereco
        FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco)
        ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB;

-- Turmas
CREATE TABLE turma (
    id_turma             INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome                 VARCHAR(50) NOT NULL,
    ano_letivo           INT NOT NULL,
    turno                VARCHAR(20),
    id_curso             INT UNSIGNED NOT NULL,
    id_escola            INT UNSIGNED NOT NULL,
    id_professor_regente INT UNSIGNED,
    CONSTRAINT fk_turma_curso
        FOREIGN KEY (id_curso) REFERENCES curso(id_curso)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_turma_escola
        FOREIGN KEY (id_escola) REFERENCES escola(id_escola)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_turma_professor
        FOREIGN KEY (id_professor_regente) REFERENCES professor(id_professor)
        ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB;

-- Alunos
CREATE TABLE aluno (
    id_aluno       INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome           VARCHAR(100) NOT NULL,
    data_nascimento DATE,
    matricula      VARCHAR(20) NOT NULL UNIQUE,
    id_turma       INT UNSIGNED NOT NULL,
    id_endereco    INT UNSIGNED,
    id_responsavel INT UNSIGNED,
    foto            LONGBLOB,
    CONSTRAINT fk_aluno_turma
        FOREIGN KEY (id_turma) REFERENCES turma(id_turma)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_aluno_endereco
        FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco)
        ON UPDATE CASCADE ON DELETE SET NULL,
    CONSTRAINT fk_aluno_responsavel
        FOREIGN KEY (id_responsavel) REFERENCES responsavel(id_responsavel)
        ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB;

-- Disciplinas
CREATE TABLE disciplina (
    id_disciplina INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome          VARCHAR(100) NOT NULL,
    carga_horaria INT,
    id_curso      INT UNSIGNED NOT NULL,
    CONSTRAINT fk_disciplina_curso
        FOREIGN KEY (id_curso) REFERENCES curso(id_curso)
        ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Funcionários
CREATE TABLE funcionario (
    id_funcionario INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome           VARCHAR(100) NOT NULL,
    cpf            CHAR(11) UNIQUE,
    cargo          VARCHAR(50),
    telefone       VARCHAR(20),
    email          VARCHAR(100),
    id_escola      INT UNSIGNED NOT NULL,
    id_endereco    INT UNSIGNED,
    CONSTRAINT fk_funcionario_escola
        FOREIGN KEY (id_escola) REFERENCES escola(id_escola)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_funcionario_endereco
        FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco)
        ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB;

-- Avaliações
CREATE TABLE avaliacao (
    id_avaliacao  INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    data          DATE NOT NULL,
    tipo          VARCHAR(50),
    descricao     VARCHAR(200),
    nota          DECIMAL(5,2) NOT NULL,
    id_aluno      INT UNSIGNED NOT NULL,
    id_disciplina INT UNSIGNED NOT NULL,
    id_turma      INT UNSIGNED NOT NULL,
    CONSTRAINT fk_avaliacao_aluno
        FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_avaliacao_disciplina
        FOREIGN KEY (id_disciplina) REFERENCES disciplina(id_disciplina)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_avaliacao_turma
        FOREIGN KEY (id_turma) REFERENCES turma(id_turma)
        ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;
