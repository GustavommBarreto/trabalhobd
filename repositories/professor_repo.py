from db import get_connection
import mysql.connector

# Classe repositório para o professor
class ProfessorRepository:
    
    # Método para criação de professor
    @staticmethod
    def create(nome, cpf, data_nascimento, email, telefone, id_escola, id_endereco):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """INSERT INTO professor (nome, cpf, data_nascimento, email, telefone, id_escola, id_endereco)
                     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (nome, cpf, data_nascimento, email, telefone, id_escola, id_endereco))
            conn.commit()
            return cursor.lastrowid
        except Exception as exc:
            print(f"Erro ao criar professor: {exc}")
            return None
        finally:
            cursor.close(); conn.close()
    
    # Método para leitura de todos os dados do professor em JSON
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True) 
        try:
            sql = "SELECT id_professor, nome, cpf, data_nascimento, email, telefone, id_escola, id_endereco FROM professor"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cursor.close(); conn.close()

    # Método para leitura de dados de um professor em JSON
    @staticmethod
    def get_by_id(id_professor):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            sql = "SELECT id_professor, nome, email, telefone FROM professor WHERE id_professor = %s"
            cursor.execute(sql, (id_professor,))
            return cursor.fetchone()
        finally:
            cursor.close(); conn.close()

    # Método para atualizar dados de professor
    @staticmethod
    def update(id_professor, nome, cpf, data_nascimento, email, telefone, id_escola, id_endereco):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """UPDATE professor SET nome=%s, cpf=%s, data_nascimento=%s, email=%s, telefone=%s, id_escola=%s, id_endereco=%s 
                     WHERE id_professor=%s"""
            params = (nome, cpf, data_nascimento, email, telefone, id_escola, id_endereco, id_professor)            
            cursor.execute(sql, params)
            conn.commit()
            return cursor.rowcount > 0 # Retorna True se alterou algo
        except Exception as exc:
            print(f"Erro na atualização dos dados: {exc}")
            return False
        finally:
            cursor.close(); conn.close()

    # Método para deletar dados de professor
    @staticmethod
    def delete(id_professor):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = "DELETE FROM professor WHERE id_professor = %s"
            cursor.execute(sql, (id_professor,))
            conn.commit()
            return True
        except mysql.connector.Error as exc:
            print(f"Erro ao deletar: {exc}")
            return False
        finally:
            cursor.close(); conn.close()
