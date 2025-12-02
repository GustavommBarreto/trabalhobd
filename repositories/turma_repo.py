from db import get_connection


class TurmaRepository:

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = """
            SELECT id_turma,
                   nome,
                   ano_letivo,
                   id_escola,
                   id_curso
            FROM turma
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    @staticmethod
    def get_by_id(id_turma: int):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = """
            SELECT id_turma,
                   nome,
                   ano_letivo,
                   id_escola,
                   id_curso
            FROM turma
            WHERE id_turma = %s
        """
        cursor.execute(sql, (id_turma,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row

    @staticmethod
    def create(nome, ano_letivo=None, id_escola=None, id_curso=None):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO turma (
                nome,
                ano_letivo,
                id_escola,
                id_curso
            )
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (nome, ano_letivo, id_escola, id_curso))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def update(id_turma, nome, ano_letivo=None, id_escola=None, id_curso=None):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            UPDATE turma
            SET nome = %s,
                ano_letivo = %s,
                id_escola = %s,
                id_curso = %s
            WHERE id_turma = %s
        """
        cursor.execute(sql, (nome, ano_letivo, id_escola, id_curso, id_turma))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete(id_turma: int):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM turma WHERE id_turma = %s"
        cursor.execute(sql, (id_turma,))
        conn.commit()
        cursor.close()
        conn.close()
