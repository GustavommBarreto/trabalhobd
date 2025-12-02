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

    # Método para utilizar a view das notas de um aluno
    @staticmethod
    def get_relatorio_view():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            # Select na view
            sql = "SELECT * FROM vw_notas_aluno_disciplina"
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as exc:
            print(f"Erro ao ler View: {exc}")
            return None
        finally:
            cursor.close(); conn.close()

    # Método para utilizar a procedure de cálculo da média de um aluno
    @staticmethod
    def get_media_procedure(id_aluno, id_disciplina):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            # 0 ou None como placeholder para o valor de saída
            args = [id_aluno, id_disciplina, 0]
            
            # callproc executa a procedure e retorna a lista 'args' com os resultados
            result_args = cursor.callproc('sp_calcular_media_aluno_disciplina', args)
            
            # O valor de saída é o terceiro elemento
            media_calculada = result_args[2]
            
            if media_calculada:
                return float(media_calculada)
            else:
                return 0.0
    
        except Exception as exc:
            print(f"Erro na Procedure: {exc}")
            return None
        finally:
            cursor.close(); conn.close()