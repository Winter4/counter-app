from flask import Flask
import os
import psycopg2
from psycopg2.extras import DictCursor

app = Flask(__name__)

# Database configuration
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", 5432)
DB_USER = os.getenv("POSTGRES_USER", "user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
DB_NAME = os.getenv("POSTGRES_DB", "counterdb")

# Initialize database connection
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME
    )
    return conn

# Ensure the database and table are set up
def init_db():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS counter (
                id SERIAL PRIMARY KEY,
                count INT NOT NULL DEFAULT 0,
                stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            INSERT INTO counter (id, count) VALUES (1, 0) ON CONFLICT (id) DO NOTHING;
            """
        )
        conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        cursor.execute("SELECT count FROM counter WHERE id = 1;")
        row = cursor.fetchone()

        if row:
            count = row['count'] + 1
            cursor.execute("UPDATE counter SET count = %s WHERE id = 1;", (count,))
        else:
            count = 1
            cursor.execute("INSERT INTO counter (id, count) VALUES (1, %s);", (count,))
        
        conn.commit()

    conn.close()
    return f"Hello World! This page has been viewed {count} times"

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
