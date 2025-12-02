import requests

url = "http://localhost:5000/testes/trigger"

print("--- TESTE DE INTEGRIDADE (TRIGGER) ---")

# Dados para o teste com a nota fora do padrão
payload = {
    "nota": "-1",
    "id_aluno": "1",
    "id_disciplina": "1",
    "id_turma": "1",
    "data": "2024-12-02",
    "tipo": "Prova Final"
}

try:
    response = requests.post(url, data=payload)
    
    if response.status_code == 201:
        resultado = response.json()
        print(f"Nota enviada: {resultado['nota_enviada']}")
        print(f"Nota salva no banco: {resultado['nota_final_no_banco']}")
        print(f"Status do Trigger: {resultado['status_trigger']}")
    else:
        print(f"\n Erro na requisição: {response.status_code}")
        print(response.text)

except Exception as exc:
    print(f"Erro de conexão: {exc}")
