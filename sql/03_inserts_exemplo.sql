USE gestao_escolar_municipal;

-- ENDEREÇO
INSERT INTO endereco (logradouro, numero, bairro, cidade, uf, cep)
VALUES
('Rua A', '100', 'Centro', 'Cidade X', 'DF', '70000-000'),
('Rua B', '200', 'Bairro B', 'Cidade X', 'DF', '70000-001');

-- ESCOLA
INSERT INTO escola (nome, tipo, telefone, email, id_endereco)
VALUES
('Escola Municipal Centro', 'Municipal', '1111-1111', 'centro@escola.com', 1),
('Escola Municipal Bairro', 'Municipal', '2222-2222', 'bairro@escola.com', 2);

-- CURSO
INSERT INTO curso (nome, nivel, carga_horaria_total, id_escola)
VALUES
('Ensino Fundamental I', 'Fundamental', 4000, 1),
('Ensino Fundamental II', 'Fundamental', 4000, 1);

-- RESPONSÁVEL
INSERT INTO responsavel (nome, parentesco, telefone, email, id_endereco)
VALUES
('João Responsável', 'Pai', '9999-1111', 'joao@exemplo.com', 1),
('Maria Responsável', 'Mãe', '9999-2222', 'maria@exemplo.com', 2);

-- TURMA
INSERT INTO turma (nome, ano_letivo, turno, id_curso, id_escola)
VALUES
('6º A', 2025, 'Matutino', 1, 1),
('7º B', 2025, 'Vespertino', 2, 1);

-- ALUNO
INSERT INTO aluno (nome, data_nascimento, matricula, id_turma, id_endereco, id_responsavel)
VALUES
('Ana Aluna', '2013-05-10', 'MAT001', 1, 1, 1),
('Bruno Aluno', '2012-09-20', 'MAT002', 1, 2, 2);

-- DISCIPLINA
INSERT INTO disciplina (nome, carga_horaria, id_curso)
VALUES
('Matemática', 200, 1),
('Português', 200, 1);

-- AVALIAÇÃO
INSERT INTO avaliacao (data, tipo, descricao, nota, id_aluno, id_disciplina, id_turma)
VALUES
('2025-03-10', 'Prova', 'Prova 1 de Matemática', 8.5, 1, 1, 1),
('2025-04-15', 'Trabalho', 'Trabalho 1 de Matemática', 11.0, 1, 1, 1); -- aqui a trigger deve ajustar para 10
