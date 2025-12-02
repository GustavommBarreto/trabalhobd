from db import get_connection
import mysql.connector

# Classe repositório para a disciplina
class DisciplinaRepository:
    
    # Método para criação de disciplina
    @staticmethod
    def create(nome, carga_horaria, id_curso):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """INSERT INTO disciplina (nome, carga_horaria, id_curso)
                     VALUES (%s, %s, %s)"""
            cursor.execute(sql, (nome, carga_horaria, id_curso))
            conn.commit()
            return cursor.lastrowid
        except Exception as exc:
            print(f"Erro ao criar disciplina: {exc}")
            return None
        finally:
            cursor.close(); conn.close()
    
    # Método para leitura de todos os dados de disciplina em JSON
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True) 
        try:
            sql = "SELECT id_disciplina, nome, id_curso FROM disciplina"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cursor.close(); conn.close()

    # Método para leitura de dados de uma disciplina em JSON
    @staticmethod
    def get_by_id(id_disciplina):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            sql = "SELECT id_disciplina, nome, carga_horaria, id_curso FROM disciplina WHERE id_disciplina = %s"
            cursor.execute(sql, (id_disciplina,))
            return cursor.fetchone()
        finally:
            cursor.close(); conn.close()

    # Método para atualizar dados de disciplina
    @staticmethod
    def update(id_disciplina, nome, carga_horaria, id_curso):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """UPDATE disciplina SET nome=%s, carga_horaria=%s, id_curso=%s 
                     WHERE id_disciplina=%s"""
            params = (nome, carga_horaria, id_curso, id_disciplina)            
            cursor.execute(sql, params)
            conn.commit()
            return cursor.rowcount > 0 # Retorna True se alterou algo
        except Exception as exc:
            print(f"Erro na atualização dos dados: {exc}")
            return False
        finally:
            cursor.close(); conn.close()

    # Método para deletar dados de disciplina
    @staticmethod
    def delete(id_disciplina):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = "DELETE FROM disciplina WHERE id_disciplina = %s"
            cursor.execute(sql, (id_disciplina,))
            conn.commit()
            return True
        except mysql.connector.Error as exc:
            print(f"Erro ao deletar: {exc}")
            return False
        finally:
            cursor.close(); conn.close()
