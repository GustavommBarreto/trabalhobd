from db import get_connection
import mysql.connector

# Classe repositório para o avaliacao
class AvaliacaoRepository:
    
    # Método para criação de avaliacao
    @staticmethod
    def create(data, tipo, descricao, nota, id_aluno, id_disciplina, id_turma):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """INSERT INTO avaliacao (data, tipo, descricao, nota, id_aluno, id_disciplina, id_turma)
                     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (data, tipo, descricao, nota, id_aluno, id_disciplina, id_turma))
            conn.commit()
            return cursor.lastrowid
        except Exception as exc:
            print(f"Erro ao criar avaliacao: {exc}")
            return None
        finally:
            cursor.close(); conn.close()
    
    # Método para leitura de todos os dados de avaliacao em JSON
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True) 
        try:
            sql = "SELECT id_avaliacao, data, tipo, descricao, nota, id_aluno, id_disciplina, id_turma FROM avaliacao"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cursor.close(); conn.close()

    # Método para leitura de dados de uma avaliacao em JSON
    @staticmethod
    def get_by_id(id_avaliacao):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            sql = "SELECT id_avaliacao, data, tipo, nota FROM avaliacao WHERE id_avaliacao = %s"
            cursor.execute(sql, (id_avaliacao,))
            return cursor.fetchone()
        finally:
            cursor.close(); conn.close()

    # Método para atualizar dados de avaliacao
    @staticmethod
    def update(id_avaliacao, data, tipo, descricao, nota, id_aluno, id_disciplina, id_turma):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """UPDATE avaliacao SET data=%s, tipo=%s, descricao=%s, nota=%s, id_aluno=%s, id_disciplina=%s, id_turma=%s 
                     WHERE id_avaliacao=%s"""
            params = (data, tipo, descricao, nota, id_aluno, id_disciplina, id_turma, id_avaliacao)            
            cursor.execute(sql, params)
            conn.commit()
            return cursor.rowcount > 0 # Retorna True se alterou algo
        except Exception as exc:
            print(f"Erro na atualização dos dados: {exc}")
            return False
        finally:
            cursor.close(); conn.close()

    # Método para deletar dados de avaliacao
    @staticmethod
    def delete(id_avaliacao):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = "DELETE FROM avaliacao WHERE id_avaliacao = %s"
            cursor.execute(sql, (id_avaliacao,))
            conn.commit()
            return True
        except mysql.connector.Error as exc:
            print(f"Erro ao deletar: {exc}")
            return False
        finally:
            cursor.close(); conn.close()

    @staticmethod
    def criar_avaliacao_via_procedure(data, tipo, desc, nota, id_aluno, id_disc, id_turma):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            args = (data, tipo, desc, nota, id_aluno, id_disc, id_turma)
            # Chama a procedure criada no passo SQL
            cursor.callproc('sp_inserir_avaliacao', args)
            conn.commit()
            return True
        except Exception as e:
            print(f"Erro na procedure: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
