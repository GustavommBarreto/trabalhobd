from db import get_connection


class ProfessorRepository:

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = """
            SELECT id_professor,
                   nome,
                   cpf,
                   data_nascimento,
                   email,
                   telefone,
                   id_escola,
                   id_endereco
            FROM professor
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    @staticmethod
    def get_by_id(id_professor: int):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = """
            SELECT id_professor,
                   nome,
                   cpf,
                   data_nascimento,
                   email,
                   telefone,
                   id_escola,
                   id_endereco
            FROM professor
            WHERE id_professor = %s
        """
        cursor.execute(sql, (id_professor,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row

    @staticmethod
    def create(
        nome,
        cpf=None,
        data_nascimento=None,
        email=None,
        telefone=None,
        id_escola=None,
        id_endereco=None,
    ):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO professor (
                nome,
                cpf,
                data_nascimento,
                email,
                telefone,
                id_escola,
                id_endereco
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(
            sql,
            (
                nome,
                cpf,
                data_nascimento,
                email,
                telefone,
                id_escola,
                id_endereco,
            ),
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def update(
        id_professor,
        nome,
        cpf=None,
        data_nascimento=None,
        email=None,
        telefone=None,
        id_escola=None,
        id_endereco=None,
    ):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            UPDATE professor
            SET nome = %s,
                cpf = %s,
                data_nascimento = %s,
                email = %s,
                telefone = %s,
                id_escola = %s,
                id_endereco = %s
            WHERE id_professor = %s
        """
        cursor.execute(
            sql,
            (
                nome,
                cpf,
                data_nascimento,
                email,
                telefone,
                id_escola,
                id_endereco,
                id_professor,
            ),
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete(id_professor: int):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM professor WHERE id_professor = %s"
        cursor.execute(sql, (id_professor,))
        conn.commit()
        cursor.close()
        conn.close()
