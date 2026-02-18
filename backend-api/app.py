from fastapi import FastAPI, HTTPException
import psycopg2
import os

app = FastAPI()

def get_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASS"]
    )

@app.get("/tasks")
def get_tasks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tasks (id SERIAL PRIMARY KEY, name TEXT);")
    cur.execute("SELECT * FROM tasks;")
    rows = cur.fetchall()
    conn.close()
    return {"tasks": rows}

@app.post("/tasks/{task_name}")
def add_task(task_name: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (name) VALUES (%s);", (task_name,))
    conn.commit()
    conn.close()
    return {"message": "Task added"}
