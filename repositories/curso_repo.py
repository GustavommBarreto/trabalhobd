from db import get_connection
import mysql.connector

# Classe repositório para o curso
class CursoRepository:
    
    # Método para criação de curso
    @staticmethod
    def create(nome, nivel, carga_horaria_total, id_escola):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """INSERT INTO curso (nome, nivel, carga_horaria_total, id_escola)
                     VALUES (%s, %s, %s, %s)"""
            cursor.execute(sql, (nome, nivel, carga_horaria_total, id_escola))
            conn.commit()
            return cursor.lastrowid
        except Exception as exc:
            print(f"Erro ao criar curso: {exc}")
            return None
        finally:
            cursor.close(); conn.close()
    
    # Método para leitura de todos os dados de curso em JSON
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True) 
        try:
            sql = "SELECT id_curso, nome, nivel, carga_horaria_total, id_escola FROM curso"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cursor.close(); conn.close()

    # Método para leitura de dados de um curso em JSON
    @staticmethod
    def get_by_id(id_curso):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            sql = "SELECT id_curso, nome, carga_horaria_total FROM curso WHERE id_curso = %s"
            cursor.execute(sql, (id_curso,))
            return cursor.fetchone()
        finally:
            cursor.close(); conn.close()

    # Método para atualizar dados de curso
    @staticmethod
    def update(id_curso, nome, nivel, carga_horaria_total, id_escola):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """UPDATE curso SET nome=%s, nivel=%s, carga_horaria_total=%s, id_escola=%s 
                     WHERE id_curso=%s"""
            params = (nome, nivel, carga_horaria_total, id_escola, id_curso)            
            cursor.execute(sql, params)
            conn.commit()
            return cursor.rowcount > 0 # Retorna True se alterou algo
        except Exception as exc:
            print(f"Erro na atualização dos dados: {exc}")
            return False
        finally:
            cursor.close(); conn.close()

    # Método para deletar dados de curso
    @staticmethod
    def delete(id_curso):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = "DELETE FROM curso WHERE id_curso = %s"
            cursor.execute(sql, (id_curso,))
            conn.commit()
            return True
        except mysql.connector.Error as exc:
            print(f"Erro ao deletar: {exc}")
            return False
        finally:
            cursor.close(); conn.close()
