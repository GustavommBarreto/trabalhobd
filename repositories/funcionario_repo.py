from db import get_connection
import mysql.connector

# Classe repositório para o funcionario
class FuncionarioRepository:
    
    # Método para criação de funcionario
    @staticmethod
    def create(nome, cpf, cargo, telefone, email, id_escola, id_endereco):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """INSERT INTO funcionario (nome, cpf, cargo, telefone, email, id_escola, id_endereco)
                     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (nome, cpf, cargo, telefone, email, id_escola, id_endereco))
            conn.commit()
            return cursor.lastrowid
        except Exception as exc:
            print(f"Erro ao criar funcionario: {exc}")
            return None
        finally:
            cursor.close(); conn.close()
    
    # Método para leitura de todos os dados de funcionario em JSON
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True) 
        try:
            sql = "SELECT id_funcionario, nome, cpf, cargo, telefone, email, id_escola, id_endereco FROM funcionario"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cursor.close(); conn.close()

    # Método para leitura de dados de um funcionario em JSON
    @staticmethod
    def get_by_id(id_funcionario):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            sql = "SELECT id_funcionario, nome, cargo, telefone FROM funcionario WHERE id_funcionario = %s"
            cursor.execute(sql, (id_funcionario,))
            return cursor.fetchone()
        finally:
            cursor.close(); conn.close()

    # Método para atualizar dados de funcionario
    @staticmethod
    def update(id_funcionario, nome, cpf, cargo, telefone, email, id_escola, id_endereco):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """UPDATE funcionario SET nome=%s, cpf=%s, cargo=%s, telefone=%s, email=%s, id_escola=%s, id_endereco=%s 
                     WHERE id_funcionario=%s"""
            params = (nome, cpf, cargo, telefone, email, id_escola, id_endereco, id_funcionario)            
            cursor.execute(sql, params)
            conn.commit()
            return cursor.rowcount > 0 # Retorna True se alterou algo
        except Exception as exc:
            print(f"Erro na atualização dos dados: {exc}")
            return False
        finally:
            cursor.close(); conn.close()

    # Método para deletar dados de funcionario
    @staticmethod
    def delete(id_funcionario):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = "DELETE FROM funcionario WHERE id_funcionario = %s"
            cursor.execute(sql, (id_funcionario,))
            conn.commit()
            return True
        except mysql.connector.Error as exc:
            print(f"Erro ao deletar: {exc}")
            return False
        finally:
            cursor.close(); conn.close()
