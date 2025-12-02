import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'host': '127.0.0.1',
    'database': 'gestao_escolar_municipal',
    'user': 'root',
    'password': 'admin'
}   


def get_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
        else:
            print("Conexão criada mas is_connected() == False")
            return None
    
    except Error as exc:
        print(f"Erro de conexão: {exc}")
        return None
