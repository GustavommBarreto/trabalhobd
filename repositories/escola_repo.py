from db import get_connection
import mysql.connector

# Classe repositório para a escola
class EscolaRepository:
    
    # Método para criação de escola
    @staticmethod
    def create(nome, tipo, telefone, email, id_endereco):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """INSERT INTO escola (nome, tipo, telefone, email, id_endereco)
                     VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (nome, tipo, telefone, email, id_endereco))
            conn.commit()
            return cursor.lastrowid
        except Exception as exc:
            print(f"Erro ao criar escola: {exc}")
            return None
        finally:
            cursor.close(); conn.close()
    
    # Método para leitura de todos os dados de escola em JSON
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True) 
        try:
            sql = "SELECT id_escola, nome, tipo, telefone, email, id_endereco FROM escola"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cursor.close(); conn.close()

    # Método para leitura de dados de uma escola em JSON
    @staticmethod
    def get_by_id(id_escola):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            sql = "SELECT id_escola, nome, telefone FROM escola WHERE id_escola = %s"
            cursor.execute(sql, (id_escola,))
            return cursor.fetchone()
        finally:
            cursor.close(); conn.close()

    # Método para atualizar dados de escola
    @staticmethod
    def update(id_escola, nome, tipo, telefone, email, id_endereco):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """UPDATE escola SET nome=%s, tipo=%s, telefone=%s, email=%s, id_endereco=%s
                     WHERE id_escola=%s"""
            params = (nome, tipo, telefone, email, id_endereco, id_escola)            
            cursor.execute(sql, params)
            conn.commit()
            return cursor.rowcount > 0 # Retorna True se alterou algo
        except Exception as exc:
            print(f"Erro na atualização dos dados: {exc}")
            return False
        finally:
            cursor.close(); conn.close()

    # Método para deletar dados de escola
    @staticmethod
    def delete(id_escola):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = "DELETE FROM escola WHERE id_escola = %s"
            cursor.execute(sql, (id_escola,))
            conn.commit()
            return True
        except mysql.connector.Error as exc:
            print(f"Erro ao deletar: {exc}")
            return False
        finally:
            cursor.close(); conn.close()
