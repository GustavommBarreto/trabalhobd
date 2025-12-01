from flask import Flask, render_template, request

app = Flask(__name__)

# --- Página inicial ---
@app.route("/")
def index():
    return render_template("index.html")


# ====== ENTIDADES ======

# --- Alunos ---
@app.route("/alunos")
def alunos():
    return render_template("alunos/list.html", alunos=[])

@app.route("/alunos/novo")
def alunos_novo():
    return render_template("alunos/form.html", aluno=None, titulo="Novo Aluno",
                           turmas=[], enderecos=[], responsaveis=[])

@app.route("/alunos/editar/<int:id>")
def alunos_editar(id):
    return render_template("alunos/form.html", aluno={}, titulo="Editar Aluno",
                           turmas=[], enderecos=[], responsaveis=[])

@app.route("/alunos/deletar/<int:id>")
def alunos_deletar(id):
    return render_template("alunos/delete.html", aluno={"nome": "Aluno Exemplo"})


# --- Professores ---
@app.route("/professores")
def professores():
    return render_template("professores/list.html", professores=[])

@app.route("/professores/novo")
def professores_novo():
    return render_template("professores/form.html", professor=None,
                           escolas=[], enderecos=[], titulo="Novo Professor")

@app.route("/professores/editar/<int:id>")
def professores_editar(id):
    return render_template("professores/form.html", professor={}, 
                           escolas=[], enderecos=[], titulo="Editar Professor")

@app.route("/professores/deletar/<int:id>")
def professores_deletar(id):
    return render_template("professores/delete.html", professor={"nome": "Professor Exemplo"})


# --- Turmas ---
@app.route("/turmas")
def turmas():
    return render_template("turmas/list.html", turmas=[])

@app.route("/turmas/novo")
def turmas_novo():
    return render_template("turmas/form.html", turma=None,
                           cursos=[], escolas=[], professores=[], titulo="Nova Turma")

@app.route("/turmas/editar/<int:id>")
def turmas_editar(id):
    return render_template("turmas/form.html", turma={}, 
                           cursos=[], escolas=[], professores=[], titulo="Editar Turma")

@app.route("/turmas/deletar/<int:id>")
def turmas_deletar(id):
    return render_template("turmas/delete.html", turma={"nome": "Turma Exemplo"})


# --- Disciplinas ---
@app.route("/disciplinas")
def disciplinas():
    return render_template("disciplinas/list.html", disciplinas=[])

@app.route("/disciplinas/novo")
def disciplinas_novo():
    return render_template("disciplinas/form.html", disciplina=None, cursos=[], titulo="Nova Disciplina")

@app.route("/disciplinas/editar/<int:id>")
def disciplinas_editar(id):
    return render_template("disciplinas/form.html", disciplina={}, cursos=[], titulo="Editar Disciplina")

@app.route("/disciplinas/deletar/<int:id>")
def disciplinas_deletar(id):
    return render_template("disciplinas/delete.html", disciplina={"nome": "Disciplina Exemplo"})


# --- Funcionários ---
@app.route("/funcionarios")
def funcionarios():
    return render_template("funcionarios/list.html", funcionarios=[])

@app.route("/funcionarios/novo")
def funcionarios_novo():
    return render_template("funcionarios/form.html", funcionario=None, escolas=[], enderecos=[], titulo="Novo Funcionário")

@app.route("/funcionarios/editar/<int:id>")
def funcionarios_editar(id):
    return render_template("funcionarios/form.html", funcionario={}, escolas=[], enderecos=[], titulo="Editar Funcionário")

@app.route("/funcionarios/deletar/<int:id>")
def funcionarios_deletar(id):
    return render_template("funcionarios/delete.html", funcionario={"nome": "Funcionário Exemplo"})


# --- Escolas ---
@app.route("/escolas")
def escolas():
    return render_template("escolas/list.html", escolas=[])

@app.route("/escolas/novo")
def escolas_novo():
    return render_template("escolas/form.html", escola=None, enderecos=[], titulo="Nova Escola")

@app.route("/escolas/editar/<int:id>")
def escolas_editar(id):
    return render_template("escolas/form.html", escola={}, enderecos=[], titulo="Editar Escola")

@app.route("/escolas/deletar/<int:id>")
def escolas_deletar(id):
    return render_template("escolas/delete.html", escola={"nome": "Escola Exemplo"})


# --- Cursos ---
@app.route("/cursos")
def cursos():
    return render_template("cursos/list.html", cursos=[])

@app.route("/cursos/novo")
def cursos_novo():
    return render_template("cursos/form.html", curso=None, escolas=[], titulo="Novo Curso")

@app.route("/cursos/editar/<int:id>")
def cursos_editar(id):
    return render_template("cursos/form.html", curso={}, escolas=[], titulo="Editar Curso")

@app.route("/cursos/deletar/<int:id>")
def cursos_deletar(id):
    return render_template("cursos/delete.html", curso={"nome": "Curso Exemplo"})


# --- Responsáveis ---
@app.route("/responsaveis")
def responsaveis():
    return render_template("responsaveis/list.html", responsaveis=[])

@app.route("/responsaveis/novo")
def responsaveis_novo():
    return render_template("responsaveis/form.html", responsavel=None, enderecos=[], titulo="Novo Responsável")

@app.route("/responsaveis/editar/<int:id>")
def responsaveis_editar(id):
    return render_template("responsaveis/form.html", responsavel={}, enderecos=[], titulo="Editar Responsável")

@app.route("/responsaveis/deletar/<int:id>")
def responsaveis_deletar(id):
    return render_template("responsaveis/delete.html", responsavel={"nome": "Responsável Exemplo"})


# --- Endereços ---
@app.route("/enderecos")
def enderecos():
    return render_template("enderecos/list.html", enderecos=[])

@app.route("/enderecos/novo")
def enderecos_novo():
    return render_template("enderecos/form.html", endereco=None, titulo="Novo Endereço")

@app.route("/enderecos/editar/<int:id>")
def enderecos_editar(id):
    return render_template("enderecos/form.html", endereco={}, titulo="Editar Endereço")

@app.route("/enderecos/deletar/<int:id>")
def enderecos_deletar(id):
    return render_template("enderecos/delete.html", endereco={"logradouro": "Rua Exemplo"})


# --- Avaliações ---
@app.route("/avaliacoes")
def avaliacoes():
    return render_template("avaliacoes/list.html", avaliacoes=[])

@app.route("/avaliacoes/novo")
def avaliacoes_novo():
    return render_template("avaliacoes/form.html", avaliacao=None,
                           alunos=[], disciplinas=[], turmas=[], titulo="Nova Avaliação")

@app.route("/avaliacoes/editar/<int:id>")
def avaliacoes_editar(id):
    return render_template("avaliacoes/form.html", avaliacao={},
                           alunos=[], disciplinas=[], turmas=[], titulo="Editar Avaliação")

@app.route("/avaliacoes/deletar/<int:id>")
def avaliacoes_deletar(id):
    return render_template("avaliacoes/delete.html", avaliacao={"descricao": "Prova Exemplo"})


if __name__ == "__main__":
    app.run(debug=True)
