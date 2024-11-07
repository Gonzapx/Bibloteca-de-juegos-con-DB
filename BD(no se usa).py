import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="gonza",  # Cambia por tu usuario
        password="Gonza.123",  # Cambia por tu contraseña
        database="prueba1"  # Nombre de la base de datos
    )

def insert_user(db, cursor):
    """Inserta un nuevo usuario en la base de datos."""
    email = input("Ingrese el email del usuario: ")
    username = input("Ingrese el nombre de usuario: ")
    sql_query = "INSERT INTO Usuario (email, username) VALUES (%s, %s)"
    values = (email, username)
    cursor.execute(sql_query, values)
    db.commit()  # Usar el objeto db para commit
    print("Registro insertado correctamente.")

def delete_user(db, cursor):
    """Elimina un usuario de la base de datos."""
    user_id = input("Ingrese el ID del usuario a eliminar: ")
    sql_query = "DELETE FROM Usuario WHERE id = %s"
    cursor.execute(sql_query, (user_id,))
    db.commit()  # Usar el objeto db para commit
    print("Registro eliminado correctamente.")

def update_user(db, cursor):
    """Actualiza el email de un usuario en la base de datos."""
    user_id = input("Ingrese el ID del usuario a actualizar: ")
    new_email = input("Ingrese el nuevo email: ")
    sql_query = "UPDATE Usuario SET email = %s WHERE id = %s"
    cursor.execute(sql_query, (new_email, user_id))
    db.commit()  # Usar el objeto db para commit
    print("Registro actualizado correctamente.")

def view_users(cursor):
    """Muestra todos los usuarios en la base de datos."""
    cursor.execute("SELECT * FROM Usuario")
    resultados = cursor.fetchall()
    for row in resultados:
        print(row)

def main():
    """Función principal que maneja el menú."""
    db = create_connection()
    cursor = db.cursor()

    while True:
        print("\nMenu:")
        print("1. Insertar usuario")
        print("2. Eliminar usuario")
        print("3. Actualizar usuario")
        print("4. Ver usuarios")
        print("5. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            insert_user(db, cursor)  # Pasa el objeto db
        elif choice == '2':
            delete_user(db, cursor)  # Pasa el objeto db
        elif choice == '3':
            update_user(db, cursor)  # Pasa el objeto db
        elif choice == '4':
            view_users(cursor)
        elif choice == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
