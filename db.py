import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'host': 'localhost',
    'database': 'gestao_escolar_municipal',
    'user': 'root',
    'password': ''
}


def get_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    
    except Error as exc:
        print(f"Erro de conexão: {exc}")
        return None
