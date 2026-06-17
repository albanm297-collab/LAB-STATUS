import sqlite3

def init_db():
    conn = sqlite3.connect('laboratorio.db')
    cursor = conn.cursor()
    # Aquí puedes dejar que cree las tablas de tu laboratorio
    conn.commit()
    conn.close()
