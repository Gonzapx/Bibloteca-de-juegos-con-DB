import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="gonza",  # Cambia por tu usuario
        password="Gonza.123",  # Cambia por tu contraseña
        database="prueba1"  # Nombre de la base de datos
    )

