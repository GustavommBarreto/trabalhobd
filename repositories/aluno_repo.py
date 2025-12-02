from db import get_connection


class AlunoRepository:

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = """
            SELECT id_aluno, nome, data_nascimento, matricula,
                   id_turma, id_endereco, id_responsavel
            FROM aluno
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    @staticmethod
    def get_by_id(id_aluno: int):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = """
            SELECT id_aluno, nome, data_nascimento, matricula,
                   id_turma, id_endereco, id_responsavel, foto
            FROM aluno
            WHERE id_aluno = %s
        """
        cursor.execute(sql, (id_aluno,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row

    @staticmethod
    def create(
        nome,
        data_nascimento,
        matricula,
        id_turma,
        id_endereco=None,
        id_responsavel=None,
        foto=None,
    ):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO aluno (
                nome,
                data_nascimento,
                matricula,
                id_turma,
                id_endereco,
                id_responsavel,
                foto
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(
            sql,
            (
                nome,
                data_nascimento,
                matricula,
                id_turma,
                id_endereco,
                id_responsavel,
                foto,
            ),
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def update(
        id_aluno,
        nome,
        data_nascimento,
        matricula,
        id_turma,
        id_endereco=None,
        id_responsavel=None,
        foto=None,
    ):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            UPDATE aluno
            SET nome = %s,
                data_nascimento = %s,
                matricula = %s,
                id_turma = %s,
                id_endereco = %s,
                id_responsavel = %s,
                foto = %s
            WHERE id_aluno = %s
        """
        cursor.execute(
            sql,
            (
                nome,
                data_nascimento,
                matricula,
                id_turma,
                id_endereco,
                id_responsavel,
                foto,
                id_aluno,
            ),
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete(id_aluno: int):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM aluno WHERE id_aluno = %s"
        cursor.execute(sql, (id_aluno,))
        conn.commit()
        cursor.close()
        conn.close()
