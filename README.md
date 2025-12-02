# EduSys – Gestão Escolar Municipal

Trabalho da disciplina de Banco de Dados (UnB) desenvolvido em grupo, usando **MySQL** e **Flask** para implementar um sistema simples de gestão escolar municipal.

O sistema permite gerenciar informações de **alunos**, **professores**, **turmas** e outros cadastros relacionados, com interface web e integração total com o banco de dados.

---

## Tecnologias utilizadas

- **Banco de dados:** MySQL
- **Linguagem back-end:** Python 3
- **Framework web:** Flask
- **Front-end:** HTML + CSS (templates Jinja2)
- **Gerenciamento de dependências:** `venv` + `pip`

---

## Estrutura geral do projeto

- `app.py` – aplicação Flask (rotas de API e interface web)
- `db.py` – configuração de conexão com o MySQL
- `repositories/` – camada de acesso a dados (um repositório por tabela)
  - `aluno_repo.py`
  - `professor_repo.py`
  - `turma_repo.py`
  - `avaliacao_repo.py`
  - `curso_repo.py`
  - `escola_repo.py`
  - `endereco_repo.py`
  - `responsavel_repo.py`
  - etc.
- `templates/` – templates HTML (Jinja2)
  - `base.html` – layout principal
  - `index.html` – página inicial
  - `alunos/` – telas de CRUD de aluno (lista, formulário)
  - `professores/` – telas de CRUD de professor
  - `turmas/` – telas de CRUD de turma
  - `relatorio/` – tela de relatório de notas
- `sql/`
  - `01_criacao_tabelas.sql` – DDL com criação de todas as tabelas
  - `02_views_procedures_triggers.sql` – criação de **views**, **procedures** e **triggers**
  - `03_inserts_exemplo.sql` – dados de exemplo para popular o banco
- `requirements.txt` – dependências Python do projeto

---

## Configuração do banco de dados

1. Criar o banco no MySQL (pode ser via Workbench):

   ```sql
   CREATE DATABASE gestao_escolar_municipal;
   USE gestao_escolar_municipal;
