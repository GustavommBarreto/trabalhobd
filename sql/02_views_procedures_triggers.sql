USE gestao_escolar_municipal;

CREATE OR REPLACE VIEW vw_notas_aluno_disciplina AS
SELECT
    a.id_aluno,
    a.nome              AS nome_aluno,
    e.nome              AS nome_escola,
    c.nome              AS nome_curso,
    t.nome              AS nome_turma,
    t.ano_letivo,
    d.nome              AS nome_disciplina,
    av.data,
    av.tipo,
    av.descricao,
    av.nota
FROM avaliacao av
JOIN aluno      a ON a.id_aluno       = av.id_aluno
JOIN turma      t ON t.id_turma       = av.id_turma
JOIN disciplina d ON d.id_disciplina  = av.id_disciplina
JOIN curso      c ON c.id_curso       = t.id_curso
JOIN escola     e ON e.id_escola      = c.id_escola;

DELIMITER $$

CREATE PROCEDURE sp_calcular_media_aluno_disciplina(
    IN  p_id_aluno      INT UNSIGNED,
    IN  p_id_disciplina INT UNSIGNED,
    OUT p_media         DECIMAL(5,2)
)
BEGIN
    SELECT AVG(nota)
    INTO p_media
    FROM avaliacao
    WHERE id_aluno = p_id_aluno
      AND id_disciplina = p_id_disciplina;
END$$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER trg_validar_nota
BEFORE INSERT ON avaliacao
FOR EACH ROW
BEGIN
    IF NEW.nota < 0 THEN
        SET NEW.nota = 0;
    ELSEIF NEW.nota > 10 THEN
        SET NEW.nota = 10;
    END IF;
END$$

DELIMITER ;

