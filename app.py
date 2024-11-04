from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="gonza",  # Cambia por tu usuario
        password="Gonza.123",  # Cambia por tu contraseña
        database="prueba1"  # Nombre de la base de datos
    )

@app.route('/')
def index():
    db = create_connection()
    cursor = db.cursor()
    cursor.execute("SELECT id, title, genre, release_year FROM Juego")
    results = cursor.fetchall()
    games = [{'id': row[0], 'title': row[1], 'genre': row[2], 'release_year': row[3]} for row in results]
    cursor.close()
    db.close()
    return render_template('index.html', games=games)

@app.route('/add', methods=['GET', 'POST'])
def add_game():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        release_year = request.form['release_year']
        
        db = create_connection()
        cursor = db.cursor()
        sql_query = "INSERT INTO Juego (title, genre, release_year) VALUES (%s, %s, %s)"
        cursor.execute(sql_query, (title, genre, release_year))
        db.commit()
        cursor.close()
        db.close()
        
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_game(id):
    db = create_connection()
    cursor = db.cursor()
    cursor.execute("SELECT id, title, genre, release_year FROM Juego WHERE id = %s", (id,))
    game = cursor.fetchone()
    cursor.close()
    
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        release_year = request.form['release_year']
        
        cursor = db.cursor()
        sql_query = "UPDATE Juego SET title = %s, genre = %s, release_year = %s WHERE id = %s"
        cursor.execute(sql_query, (title, genre, release_year, id))
        db.commit()
        cursor.close()
        db.close()
        
        return redirect(url_for('index'))
    
    db.close()
    return render_template('edit.html', game={'id': game[0], 'title': game[1], 'genre': game[2], 'release_year': game[3]})

@app.route('/delete/<int:id>')
def delete_game(id):
    db = create_connection()
    cursor = db.cursor()
    sql_query = "DELETE FROM Juego WHERE id = %s"
    cursor.execute(sql_query, (id,))
    db.commit()
    cursor.close()
    db.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
