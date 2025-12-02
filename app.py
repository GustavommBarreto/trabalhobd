# Projeto Banco de Dados
# Arquivo principal orquestrador

from flask import Flask, request, jsonify, send_file
from repositories.aluno_repo import AlunoRepository
from repositories.avaliacao_repo import AvaliacaoRepository
from repositories.curso_repo import CursoRepository
from repositories.disciplina_repo import DisciplinaRepository
from repositories.endereco_repo import EnderecoRepository
from repositories.escola_repo import EscolaRepository
from repositories.funcionario_repo import FuncionarioRepository
from repositories.professor_repo import ProfessorRepository
from repositories.responsavel_repo import ResponsavelRepository
from repositories.turma_repo import TurmaRepository
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# --- Rotas de ALUNO ---
# Método CREATE
@app.route('/alunos', methods=['POST'])
def criar_aluno():
    data = request.form 
    foto_bytes = None
    if 'foto' in request.files:
        foto_bytes = request.files['foto'].read()
    try:
        novo_id = AlunoRepository.create(
            data.get('nome'), 
            data.get('data_nascimento'), 
            data.get('matricula'), 
            data.get('id_turma'),
            data.get('id_endereco'),
            data.get('id_responsavel'),
            foto_bytes
        )
        return jsonify({'id': novo_id}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método READALL
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    return jsonify(AlunoRepository.get_all()), 200

# Método READ por id
@app.route('/alunos/<int:id>', methods=['GET'])
def buscar_aluno(id):
    res = AlunoRepository.get_by_id(id)
    return jsonify(res) if res else (jsonify({'erro': 'Não encontrado'}), 404)

# Método UPDATE
@app.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    data = request.form

    foto_bytes = None
    if 'foto' in request.files:
        foto_bytes = request.files['foto'].read()
    try:
        sucesso = AlunoRepository.update(
            id, # O ID vem da URL
            data.get('nome'), 
            data.get('data_nascimento'), 
            data.get('matricula'), 
            data.get('id_turma'),
            data.get('id_endereco'),
            data.get('id_responsavel'),
            foto_bytes
            )
        return jsonify({'sucesso': sucesso}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método DELETE
@app.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    if AlunoRepository.delete(id):
        return jsonify({'msg': 'Deletado com sucesso'}), 200
    return jsonify({'erro': 'Erro ao deletar (verifique vínculos)'}), 400

# --- Rotas de AVALIACAO ---
# Método CREATE
@app.route('/avaliacoes', methods=['POST'])
def criar_avaliacao():
    data = request.form 
    try:
        novo_id = AvaliacaoRepository.create(
            data.get('data'), 
            data.get('tipo'), 
            data.get('descricao'), 
            data.get('nota'),
            data.get('id_aluno'),
            data.get('id_disciplina'),
            data.get('id_turma')
        )
        return jsonify({'id': novo_id}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método READALL
@app.route('/avaliacoes', methods=['GET'])
def listar_avaliacoes():
    return jsonify(AvaliacaoRepository.get_all()), 200

# Método READ por id
@app.route('/avaliacoes/<int:id>', methods=['GET'])
def buscar_avaliacao(id):
    res = AvaliacaoRepository.get_by_id(id)
    return jsonify(res) if res else (jsonify({'erro': 'Não encontrado'}), 404)

# Método UPDATE
@app.route('/avaliacoes/<int:id>', methods=['PUT'])
def atualizar_avaliacao(id):
    data = request.form
    try:
        sucesso = AvaliacaoRepository.update(
            id, # O ID vem da URL
            data.get('data'), 
            data.get('tipo'), 
            data.get('descricao'), 
            data.get('nota'),
            data.get('id_aluno'),
            data.get('id_disciplina'),
            data.get('id_turma')
            )
        return jsonify({'sucesso': sucesso}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método DELETE
@app.route('/avaliacoes/<int:id>', methods=['DELETE'])
def deletar_avaliacao(id):
    if AvaliacaoRepository.delete(id):
        return jsonify({'msg': 'Deletado com sucesso'}), 200
    return jsonify({'erro': 'Erro ao deletar (verifique vínculos)'}), 400

# --- Rotas para CURSO ---
# Método CREATE
@app.route('/cursos', methods=['POST'])
def criar_curso():
    data = request.form 
    try:
        novo_id = CursoRepository.create(
            data.get('nome'), 
            data.get('nivel'), 
            data.get('carga_horaria_total'), 
            data.get('id_escola') 
        )
        return jsonify({'id': novo_id}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método READALL
@app.route('/cursos', methods=['GET'])
def listar_cursos():
    return jsonify(CursoRepository.get_all()), 200

# Método READ por id
@app.route('/cursos/<int:id>', methods=['GET'])
def buscar_curso(id):
    res = CursoRepository.get_by_id(id)
    return jsonify(res) if res else (jsonify({'erro': 'Não encontrado'}), 404)

# Método UPDATE
@app.route('/cursos/<int:id>', methods=['PUT'])
def atualizar_curso(id):
    data = request.form
    try:
        sucesso = CursoRepository.update(
            id, # O ID vem da URL
            data.get('nome'), 
            data.get('nivel'), 
            data.get('carga_horaria_total'), 
            data.get('id_escola')
            )
        return jsonify({'sucesso': sucesso}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método DELETE
@app.route('/cursos/<int:id>', methods=['DELETE'])
def deletar_curso(id):
    if CursoRepository.delete(id):
        return jsonify({'msg': 'Deletado com sucesso'}), 200
    return jsonify({'erro': 'Erro ao deletar (verifique vínculos)'}), 400

# --- Rotas para DISCIPLINA ---
# Método CREATE
@app.route('/disciplinas', methods=['POST'])
def criar_disciplina():
    data = request.form 
    try:
        novo_id = DisciplinaRepository.create(
            data.get('nome'), 
            data.get('carga_horaria'), 
            data.get('id_curso') 
        )
        return jsonify({'id': novo_id}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método READALL
@app.route('/disciplinas', methods=['GET'])
def listar_disciplinas():
    return jsonify(DisciplinaRepository.get_all()), 200

# Método READ por id
@app.route('/disciplinas/<int:id>', methods=['GET'])
def buscar_disciplina(id):
    res = DisciplinaRepository.get_by_id(id)
    return jsonify(res) if res else (jsonify({'erro': 'Não encontrado'}), 404)

# Método UPDATE
@app.route('/disciplinas/<int:id>', methods=['PUT'])
def atualizar_disciplina(id):
    data = request.form
    try:
        sucesso = DisciplinaRepository.update(
            id, # O ID vem da URL
            data.get('nome'), 
            data.get('carga_horaria'), 
            data.get('id_curso')
            )
        return jsonify({'sucesso': sucesso}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método DELETE
@app.route('/disciplinas/<int:id>', methods=['DELETE'])
def deletar_disciplina(id):
    if DisciplinaRepository.delete(id):
        return jsonify({'msg': 'Deletado com sucesso'}), 200
    return jsonify({'erro': 'Erro ao deletar (verifique vínculos)'}), 400

# --- Rotas para ENDERECO ---
# Método CREATE
@app.route('/enderecos', methods=['POST'])
def criar_endereco():
    data = request.form 
    try:
        novo_id = EnderecoRepository.create(
            data.get('logradouro'), 
            data.get('numero'),
            data.get('complemento'),
            data.get('bairro'),
            data.get('cidade'),
            data.get('uf'),
            data.get('cep')
        )
        return jsonify({'id': novo_id}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método READALL
@app.route('/enderecos', methods=['GET'])
def listar_enderecos():
    return jsonify(EnderecoRepository.get_all()), 200

# Método READ por id
@app.route('/enderecos/<int:id>', methods=['GET'])
def buscar_endereco(id):
    res = EnderecoRepository.get_by_id(id)
    return jsonify(res) if res else (jsonify({'erro': 'Não encontrado'}), 404)

# Método UPDATE
@app.route('/enderecos/<int:id>', methods=['PUT'])
def atualizar_endereco(id):
    data = request.form
    try:
        sucesso = EnderecoRepository.update(
            id, # O ID vem da URL
            data.get('logradouro'), 
            data.get('numero'),
            data.get('complemento'),
            data.get('bairro'),
            data.get('cidade'),
            data.get('uf'),
            data.get('cep')
            )
        return jsonify({'sucesso': sucesso}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método DELETE
@app.route('/enderecos/<int:id>', methods=['DELETE'])
def deletar_endereco(id):
    if EnderecoRepository.delete(id):
        return jsonify({'msg': 'Deletado com sucesso'}), 200
    return jsonify({'erro': 'Erro ao deletar (verifique vínculos)'}), 400

# ---- Rotas para ESCOLA ---
# Método CREATE
@app.route('/escolas', methods=['POST'])
def criar_escola():
    data = request.form 
    try:
        novo_id = EscolaRepository.create(
            data.get('nome'), 
            data.get('tipo'), 
            data.get('telefone'), 
            data.get('email'), 
            data.get('id_endereco')
        )
        return jsonify({'id': novo_id}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método READALL
@app.route('/escolas', methods=['GET'])
def listar_escolas():
    return jsonify(EscolaRepository.get_all()), 200

# Método READ por id
@app.route('/escolas/<int:id>', methods=['GET'])
def buscar_escola(id):
    res = EscolaRepository.get_by_id(id)
    return jsonify(res) if res else (jsonify({'erro': 'Não encontrado'}), 404)


# Método UPDATE
@app.route('/escolas/<int:id>', methods=['PUT'])
def atualizar_escola(id):
    data = request.form
    try:
        sucesso = EscolaRepository.update(
            id, # O ID vem da URL
            data.get('nome'), 
            data.get('tipo'), 
            data.get('telefone'), 
            data.get('email')
        )
        return jsonify({'sucesso': sucesso}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método DELETE
@app.route('/escolas/<int:id>', methods=['DELETE'])
def deletar_escola(id):
    if EscolaRepository.delete(id):
        return jsonify({'msg': 'Deletado com sucesso'}), 200
    return jsonify({'erro': 'Erro ao deletar (verifique vínculos)'}), 400

# --- Rotas para FUNCIONARIO ---
# Método CREATE
@app.route('/funcionarios', methods=['POST'])
def criar_funcionario():
    data = request.form 
    try:
        novo_id = FuncionarioRepository.create(
            data.get('nome'), 
            data.get('cpf'), 
            data.get('cargo'),
            data.get('telefone'),
            data.get('email'),
            data.get('id_escola'),
            data.get('id_endereco') 
        )
        return jsonify({'id': novo_id}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método READALL
@app.route('/funcionarios', methods=['GET'])
def listar_funcionarios():
    return jsonify(FuncionarioRepository.get_all()), 200

# Método READ por id
@app.route('/funcionarios/<int:id>', methods=['GET'])
def buscar_funcionario(id):
    res = FuncionarioRepository.get_by_id(id)
    return jsonify(res) if res else (jsonify({'erro': 'Não encontrado'}), 404)

# Método UPDATE
@app.route('/funcionarios/<int:id>', methods=['PUT'])
def atualizar_funcionario(id):
    data = request.form
    try:
        sucesso = FuncionarioRepository.update(
            id, # O ID vem da URL
            data.get('nome'), 
            data.get('cpf'), 
            data.get('cargo'),
            data.get('telefone'),
            data.get('email'),
            data.get('id_escola'),
            data.get('id_endereco')
            )
        return jsonify({'sucesso': sucesso}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método DELETE
@app.route('/funcionarios/<int:id>', methods=['DELETE'])
def deletar_funcionario(id):
    if FuncionarioRepository.delete(id):
        return jsonify({'msg': 'Deletado com sucesso'}), 200
    return jsonify({'erro': 'Erro ao deletar (verifique vínculos)'}), 400


# ---- Rotas para PROFESSOR ---
# Método CREATE
@app.route('/professores', methods=['POST'])
def criar_professor():
    data = request.form 
    try:
        novo_id = ProfessorRepository.create(
            data.get('nome'), 
            data.get('cpf'), 
            data.get('data_nascimento'), 
            data.get('email'), 
            data.get('telefone'),
            data.get('id_escola'),
            data.get('id_endereco')
        )
        return jsonify({'id': novo_id}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método READALL
@app.route('/professores', methods=['GET'])
def listar_professores():
    return jsonify(ProfessorRepository.get_all()), 200

# Método READ por id
@app.route('/professores/<int:id>', methods=['GET'])
def buscar_professor(id):
    res = ProfessorRepository.get_by_id(id)
    return jsonify(res) if res else (jsonify({'erro': 'Não encontrado'}), 404)


# Método UPDATE
@app.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    data = request.form
    try:
        sucesso = ProfessorRepository.update(
            id, # O ID vem da URL
            data.get('nome'), 
            data.get('cpf'), 
            data.get('data_nascimento'), 
            data.get('email'), 
            data.get('telefone'),
            data.get('id_escola'),
            data.get('id_endereco')
        )
        return jsonify({'sucesso': sucesso}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método DELETE
@app.route('/professores/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    if ProfessorRepository.delete(id):
        return jsonify({'msg': 'Deletado com sucesso'}), 200
    return jsonify({'erro': 'Erro ao deletar (verifique vínculos)'}), 400

# ---- Rotas para RESPONSAVEL ---
# Método CREATE
@app.route('/responsaveis', methods=['POST'])
def criar_responsavel():
    data = request.form 
    try:
        novo_id = ResponsavelRepository.create(
            data.get('nome'), 
            data.get('parentesco'), 
            data.get('telefone'), 
            data.get('email'),
            data.get('id_endereco')
        )
        return jsonify({'id': novo_id}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método READALL
@app.route('/responsaveis', methods=['GET'])
def listar_responsaveis():
    return jsonify(ResponsavelRepository.get_all()), 200

# Método READ por id
@app.route('/responsaveis/<int:id>', methods=['GET'])
def buscar_responsavel(id):
    res = ResponsavelRepository.get_by_id(id)
    return jsonify(res) if res else (jsonify({'erro': 'Não encontrado'}), 404)


# Método UPDATE
@app.route('/responsaveis/<int:id>', methods=['PUT'])
def atualizar_responsavel(id):
    data = request.form
    try:
        sucesso = ResponsavelRepository.update(
            id, # O ID vem da URL
            data.get('nome'), 
            data.get('parentesco'), 
            data.get('telefone'), 
            data.get('email'),
            data.get('id_endereco')
        )
        return jsonify({'sucesso': sucesso}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método DELETE
@app.route('/responsaveis/<int:id>', methods=['DELETE'])
def deletar_responsavel(id):
    if ResponsavelRepository.delete(id):
        return jsonify({'msg': 'Deletado com sucesso'}), 200
    return jsonify({'erro': 'Erro ao deletar (verifique vínculos)'}), 400

# ---- Rotas para TURMA ---
# Método CREATE
@app.route('/turmas', methods=['POST'])
def criar_turma():
    data = request.form 
    try:
        novo_id = TurmaRepository.create(
            data.get('nome'), 
            data.get('ano_letivo'), 
            data.get('turno'), 
            data.get('id_curso'),
            data.get('id_escola'),
            data.get('id_professor_regente')
        )
        return jsonify({'id': novo_id}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método READALL
@app.route('/turmas', methods=['GET'])
def listar_turmas():
    return jsonify(TurmaRepository.get_all()), 200

# Método READ por id
@app.route('/turmas/<int:id>', methods=['GET'])
def buscar_turma(id):
    res = TurmaRepository.get_by_id(id)
    return jsonify(res) if res else (jsonify({'erro': 'Não encontrado'}), 404)


# Método UPDATE
@app.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    data = request.form
    try:
        sucesso = TurmaRepository.update(
            id, # O ID vem da URL
            data.get('nome'), 
            data.get('ano_letivo'), 
            data.get('turno'), 
            data.get('id_curso'),
            data.get('id_escola'),
            data.get('id_professor_regente')
        )
        return jsonify({'sucesso': sucesso}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Método DELETE
@app.route('/turmas/<int:id>', methods=['DELETE'])
def deletar_turma(id):
    if TurmaRepository.delete(id):
        return jsonify({'msg': 'Deletado com sucesso'}), 200
    return jsonify({'erro': 'Erro ao deletar (verifique vínculos)'}), 400

# --- ROTAS para View, Procedure e Trigger ---

# Rota para VIEW de relatório de notas
@app.route('/relatorios/notas', methods=['GET'])
def relatorio_notas():
    dados = AvaliacaoRepository.get_relatorio_view()
    return jsonify(dados), 200

# Rota para a PROCEDURE de cálculo de média
@app.route('/alunos/<int:id_aluno>/media/<int:id_disciplina>', methods=['GET'])
def calcular_media_aluno(id_aluno, id_disciplina):
    media = AvaliacaoRepository.get_media_procedure(id_aluno, id_disciplina)
    
    if media is not None:
        return jsonify({
            "id_aluno": id_aluno,
            "id_disciplina": id_disciplina,
            "media_calculada": media
        }), 200
    return jsonify({"erro": "Erro ao calcular média"}), 500

# Rota de teste para o TRIGGER
@app.route('/testes/trigger', methods=['POST'])
def teste_trigger():
    # Tenta inserir uma nota inválida menor que 0 ou maior que 10
    data = request.form
    try:
        novo_id = AvaliacaoRepository.create(
            data.get('data'), 
            data.get('tipo'), 
            "Teste de Trigger - Nota Extrema", 
            data.get('nota'),
            data.get('id_aluno'),
            data.get('id_disciplina'),
            data.get('id_turma')
        )
        
        # Busca o registro criado para ver qual nota o banco salvou
        avaliacao_salva = AvaliacaoRepository.get_by_id(novo_id)
        
        return jsonify({
            "mensagem": "Tentativa de inserção realizada",
            "nota_enviada": data.get('nota'),
            "nota_final_no_banco": avaliacao_salva['nota'],
            "status_trigger": "FUNCIONOU" if float(avaliacao_salva['nota']) <= 10 else "FALHOU"
        }), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
