from database.connection import create_connection

def get_games():
    db = create_connection()
    cursor = db.cursor()
    cursor.execute("SELECT id, title, genre, release_year FROM Juego")
    results = cursor.fetchall()
    cursor.close()
    db.close()
    return [{'id': row[0], 'title': row[1], 'genre': row[2], 'release_year': row[3]} for row in results]

def add_game_to_db(title, genre, release_year):
    db = create_connection()
    cursor = db.cursor()
    sql_query = "INSERT INTO Juego (title, genre, release_year) VALUES (%s, %s, %s)"
    cursor.execute(sql_query, (title, genre, release_year))
    db.commit()
    cursor.close()
    db.close()

def get_game_by_id(game_id):
    db = create_connection()
    cursor = db.cursor()
    cursor.execute("SELECT id, title, genre, release_year FROM Juego WHERE id = %s", (game_id,))
    game = cursor.fetchone()
    cursor.close()
    db.close()
    return game

def update_game_in_db(game_id, title, genre, release_year):
    db = create_connection()
    cursor = db.cursor()
    sql_query = "UPDATE Juego SET title = %s, genre = %s, release_year = %s WHERE id = %s"
    cursor.execute(sql_query, (title, genre, release_year, game_id))
    db.commit()
    cursor.close()
    db.close()

def delete_game_from_db(game_id):
    db = create_connection()
    cursor = db.cursor()
    sql_query = "DELETE FROM Juego WHERE id = %s"
    cursor.execute(sql_query, (game_id,))
    db.commit()
    cursor.close()
    db.close()

