from db import get_connection
import mysql.connector

# Classe repositório para a endereco
class EnderecoRepository:
    
    # Método para criação de endereco
    @staticmethod
    def create(logradouro, numero, complemento, bairro, cidade, uf, cep):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """INSERT INTO endereco (logradouro, numero, complemento, bairro, cidade, uf, cep)
                     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (logradouro, numero, complemento, bairro, cidade, uf, cep))
            conn.commit()
            return cursor.lastrowid
        except Exception as exc:
            print(f"Erro ao criar endereco: {exc}")
            return None
        finally:
            cursor.close(); conn.close()
    
    # Método para leitura de todos os dados de endereco em JSON
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True) 
        try:
            sql = "SELECT id_endereco, logradouro, numero, complemento, bairro, cidade, uf, cep FROM endereco"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cursor.close(); conn.close()

    # Método para leitura de dados de um endereco em JSON
    @staticmethod
    def get_by_id(id_endereco):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            sql = """SELECT id_endereco, cidade, uf, cep
                    FROM endereco WHERE id_endereco = %s"""
            cursor.execute(sql, (id_endereco,))
            return cursor.fetchone()
        finally:
            cursor.close(); conn.close()

    # Método para atualizar dados de endereco
    @staticmethod
    def update(id_endereco, logradouro, numero, complemento, bairro, cidade, uf, cep):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """UPDATE endereco SET logradouro=%s, numero=%s, complemento=%s, bairro=%s, cidade=%s, uf=%s, cep=%s 
                     WHERE id_endereco=%s"""
            params = (logradouro, numero, complemento, bairro, cidade, uf, cep, id_endereco)            
            cursor.execute(sql, params)
            conn.commit()
            return cursor.rowcount > 0 # Retorna True se alterou algo
        except Exception as exc:
            print(f"Erro na atualização dos dados: {exc}")
            return False
        finally:
            cursor.close(); conn.close()

    # Método para deletar dados de endereco
    @staticmethod
    def delete(id_endereco):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = "DELETE FROM endereco WHERE id_endereco = %s"
            cursor.execute(sql, (id_endereco,))
            conn.commit()
            return True
        except mysql.connector.Error as exc:
            print(f"Erro ao deletar: {exc}")
            return False
        finally:
            cursor.close(); conn.close()
