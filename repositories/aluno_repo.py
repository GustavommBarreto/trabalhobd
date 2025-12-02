from db import get_connection
import mysql.connector

# Classe repositório para o aluno
class AlunoRepository:
    
    # Método para criação de aluno
    @staticmethod
    def create(nome, data_nascimento, matricula, id_turma, id_endereco, id_responsavel, foto_bytes):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """INSERT INTO aluno (nome, data_nascimento, matricula, id_turma, id_endereco, id_responsavel, foto)
                     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (nome, data_nascimento, matricula, id_turma, id_endereco, id_responsavel, foto_bytes))
            conn.commit()
            return cursor.lastrowid
        except Exception as exc:
            print(f"Erro ao criar aluno: {exc}")
            return None
        finally:
            cursor.close(); conn.close()
    
    # Método para leitura de todos os dados de aluno em JSON
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True) 
        try:
            sql = "SELECT id_aluno, nome, data_nascimento, matricula, id_turma, id_endereco, id_responsavel FROM aluno"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cursor.close(); conn.close()

    # Método para leitura de dados de um aluno em JSON
    @staticmethod
    def get_by_id(id_aluno):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            # Aqui pegamos tudo, exceto a foto
            sql = "SELECT id_aluno, nome, data_nascimento, matricula FROM aluno WHERE id_aluno = %s"
            cursor.execute(sql, (id_aluno,))
            return cursor.fetchone()
        finally:
            cursor.close(); conn.close()

    # Método para atualizar dados de aluno
    @staticmethod
    def update(id_aluno, nome, data_nascimento, matricula, id_turma, id_endereco, id_responsavel, foto_bytes=None):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if foto_bytes:
                # Se receber uma foto nova, atualiza tudo inclusive a foto
                sql = """UPDATE aluno SET nome=%s, data_nascimento=%s, matricula=%s, id_turma=%s, id_endereco=%s, id_responsavel=%s, foto=%s 
                         WHERE id_aluno=%s"""
                params = (nome, data_nascimento, matricula, id_turma, id_endereco, id_responsavel, foto_bytes, id_aluno)
            else:
                sql = """UPDATE aluno SET nome=%s, data_nascimento=%s, matricula=%s, id_turma=%s, id_endereco=%s, id_responsavel=%s
                         WHERE id_aluno=%s"""
                params = (nome, data_nascimento, matricula, id_turma, id_endereco, id_responsavel, id_aluno)
            
            cursor.execute(sql, params)
            conn.commit()
            return cursor.rowcount > 0 # Retorna True se alterou algo
        except Exception as exc:
            print(f"Erro na atualização dos dados: {exc}")
            return False
        finally:
            cursor.close(); conn.close()

    # Método para deletar dados de aluno
    @staticmethod
    def delete(id_aluno):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = "DELETE FROM aluno WHERE id_aluno = %s"
            cursor.execute(sql, (id_aluno,))
            conn.commit()
            return True
        except mysql.connector.Error as exc:
            print(f"Erro ao deletar: {exc}")
            return False
        finally:
            cursor.close(); conn.close()

    @staticmethod
    def insert_aluno(nome, data_nasc, matricula, id_turma, id_endereco, id_responsavel, foto_bytes):
        """
        Insere aluno com foto (BLOB).
        Retorna o ID do novo aluno ou None em caso de erro.
        """
        conn = get_connection()
        if not conn: 
            return None

        cursor = conn.cursor()
        try:
            sql = """
                INSERT INTO aluno 
                (nome, data_nascimento, matricula, id_turma, id_endereco, id_responsavel, foto)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            params = (nome, data_nasc, matricula, id_turma, id_endereco, id_responsavel, foto_bytes)
            
            cursor.execute(sql, params)
            conn.commit()
            return cursor.lastrowid
        except mysql.connector.Error as exc:
            print(f"Erro ao inserir aluno: {exc}")
            return None
        finally:
            cursor.close(); conn.close()

    @staticmethod
    def get_alunos_view():
        """
        Busca dados usando a VIEW criada (Requisito acadêmico).
        """
        conn = get_connection()
        if not conn: return []
        
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM vw_detalhes_aluno")
            return cursor.fetchall()
        except mysql.connector.Error as exc:
            print(f"Erro ao ler view: {exc}")
            return []
        finally:
            cursor.close(); conn.close()

    @staticmethod
    def get_foto(id_aluno):
        """Recupera apenas o binário da foto para download/visualização."""
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT foto FROM aluno WHERE id_aluno = %s", (id_aluno,))
            result = cursor.fetchone()
            if result and result[0]:
                return result[0] # Retorna os bytes puros
            return None
        finally:
            cursor.close(); conn.close()
