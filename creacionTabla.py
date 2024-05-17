import sqlite3

try:
    mi_conexion= sqlite3.connect("task.db")
    mi_cursor= mi_conexion.cursor()
    mi_cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN NOT NULL DEFAULT FALSE
            )
                      ''')
    mi_conexion.commit()
except Exception as ex: 
    print(ex)