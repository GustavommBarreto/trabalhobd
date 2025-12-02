from db import get_connection
import mysql.connector

# Classe repositório para o turma
class TurmaRepository:
    
    # Método para criação de turma
    @staticmethod
    def create(nome, ano_letivo, turno, id_curso, id_escola, id_professor_regente):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """INSERT INTO turma (nome, ano_letivo, turno, id_curso, id_escola, id_professor_regente)
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (nome, ano_letivo, turno, id_curso, id_escola, id_professor_regente))
            conn.commit()
            return cursor.lastrowid
        except Exception as exc:
            print(f"Erro ao criar turma: {exc}")
            return None
        finally:
            cursor.close(); conn.close()
    
    # Método para leitura de todos os dados de turma em JSON
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True) 
        try:
            sql = "SELECT id_turma, nome, ano_letivo, turno, id_curso, id_escola, id_professor_regente FROM turma"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cursor.close(); conn.close()

    # Método para leitura de dados de uma turma em JSON
    @staticmethod
    def get_by_id(id_turma):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            sql = "SELECT id_turma, nome, ano_letivo, turno FROM turma WHERE id_turma = %s"
            cursor.execute(sql, (id_turma,))
            return cursor.fetchone()
        finally:
            cursor.close(); conn.close()

    # Método para atualizar dados de turma
    @staticmethod
    def update(id_turma, nome, ano_letivo, turno, id_curso, id_escola, id_professor_regente):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """UPDATE turma SET nome=%s, ano_letivo=%s, turno=%s, id_curso=%s, id_escola=%s, id_professor_regente=%s 
                     WHERE id_turma=%s"""
            params = (nome, ano_letivo, turno, id_curso, id_escola, id_professor_regente, id_turma)            
            cursor.execute(sql, params)
            conn.commit()
            return cursor.rowcount > 0 # Retorna True se alterou algo
        except Exception as exc:
            print(f"Erro na atualização dos dados: {exc}")
            return False
        finally:
            cursor.close(); conn.close()

    # Método para deletar dados de turma
    @staticmethod
    def delete(id_turma):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = "DELETE FROM turma WHERE id_turma = %s"
            cursor.execute(sql, (id_turma,))
            conn.commit()
            return True
        except mysql.connector.Error as exc:
            print(f"Erro ao deletar: {exc}")
            return False
        finally:
            cursor.close(); conn.close()
