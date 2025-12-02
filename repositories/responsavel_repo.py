from db import get_connection
import mysql.connector

# Classe repositório para o responsavel
class ResponsavelRepository:
    
    # Método para criação de responsavel
    @staticmethod
    def create(nome, parentesco, telefone, email, id_endereco):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """INSERT INTO responsavel (nome, parentesco, telefone, email, id_endereco)
                     VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (nome, parentesco, telefone, email, id_endereco))
            conn.commit()
            return cursor.lastrowid
        except Exception as exc:
            print(f"Erro ao criar responsavel: {exc}")
            return None
        finally:
            cursor.close(); conn.close()
    
    # Método para leitura de todos os dados de responsavel em JSON
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True) 
        try:
            sql = "SELECT id_professor, nome, parentesco, telefone, email, id_endereco FROM responsavel"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cursor.close(); conn.close()

    # Método para leitura de dados de um responsavel em JSON
    @staticmethod
    def get_by_id(id_responsavel):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            sql = "SELECT id_responsavel, nome, parentesco FROM responsavel WHERE id_responsavel = %s"
            cursor.execute(sql, (id_responsavel,))
            return cursor.fetchone()
        finally:
            cursor.close(); conn.close()

    # Método para atualizar dados de responsavel
    @staticmethod
    def update(id_responsavel, nome, parentesco, telefone, email, id_endereco):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """UPDATE responsavel SET nome=%s, parentesco=%s, telefone=%s, email=%s, id_endereco=%s 
                     WHERE id_responsavel=%s"""
            params = (nome, parentesco, telefone, email, id_endereco, id_responsavel)            
            cursor.execute(sql, params)
            conn.commit()
            return cursor.rowcount > 0 # Retorna True se alterou algo
        except Exception as exc:
            print(f"Erro na atualização dos dados: {exc}")
            return False
        finally:
            cursor.close(); conn.close()

    # Método para deletar dados de responsavel
    @staticmethod
    def delete(id_responsavel):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = "DELETE FROM responsavel WHERE id_responsavel = %s"
            cursor.execute(sql, (id_responsavel,))
            conn.commit()
            return True
        except mysql.connector.Error as exc:
            print(f"Erro ao deletar: {exc}")
            return False
        finally:
            cursor.close(); conn.close()
