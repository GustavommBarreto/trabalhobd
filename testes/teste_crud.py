import requests

BASE_URL = "http://127.0.0.1:5000"

def teste_create_aluno():
    print("--- TESTANDO CRIAÇÃO VIA POST ---")
    url = f"{BASE_URL}/alunos"
    
    # Dados do formulário
    dados = {
        "nome": "Aluno Teste",
        "data_nascimento": "2005-01-01",
        "matricula": "TESTE001",
        "id_turma": "1",
        "id_endereco": "1",
        "id_responsavel": "1"
    }
    
    # Arquivo Binário
    arquivos = {
        'foto': ('foto_teste.txt', b'Conteudo binario da foto aqui', 'text/plain')
    }

    try:
        response = requests.post(url, data=dados, files=arquivos)
        if response.status_code == 201:
            id_novo = response.json()['id']
            print(f"SUCESSO! Aluno criado com ID: {id_novo}")
            return id_novo
        else:
            print(f"ERRO NO POST: {response.text}")
            return None
    except Exception as exc:
        print(f"Erro de conexão: {exc}")
        return None

def teste_update_aluno(id_aluno):
    print(f"\n--- TESTANDO ATUALIZAÇÃO VIA PUT para ID {id_aluno} ---")
    url = f"{BASE_URL}/alunos/{id_aluno}"
    
    dados = {
        "nome": "Novo Nome",
        "data_nascimento": "2001-10-01",
        "matricula": "MAT003",
        "id_turma": "1",
        "id_endereco": "2",
        "id_responsavel": "2"
    }

    response = requests.put(url, data=dados)
    
    if response.status_code == 200:
        print("SUCESSO! Dados atualizados.")
    else:
        print(f"ERRO NO PUT: {response.text}")

def teste_delete_aluno(id_aluno):
    print(f"\n--- TESTANDO REMOÇÃO VIA DELETE para ID {id_aluno} ---")
    url = f"{BASE_URL}/alunos/{id_aluno}"
    
    response = requests.delete(url)
    
    if response.status_code == 200:
        print("SUCESSO! Aluno deletado.")
    else:
        print(f"ERRO NO DELETE: {response.text}")

if __name__ == "__main__":
    id_criado = teste_create_aluno()
    if id_criado:
        teste_update_aluno(id_criado)
        teste_delete_aluno(id_criado)
