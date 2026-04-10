
import sqlite3
import json
from datetime import datetime

DB_PATH = "interviews.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS interviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            difficulty TEXT,
            score TEXT,
            date TEXT,
            conversation TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_interview(topic, difficulty, score, conversation):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT INTO interviews (topic, difficulty, score, date, conversation)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        topic,
        difficulty,
        score,
        datetime.now().strftime("%Y-%m-%d %H:%M"),
        json.dumps(conversation)
    ))
    conn.commit()
    conn.close()

def get_all_interviews():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT id, topic, difficulty, score, date FROM interviews ORDER BY date DESC')
    rows = c.fetchall()
    conn.close()
    return rows

def get_interview_by_id(interview_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM interviews WHERE id = ?', (interview_id,))
    row = c.fetchone()
    conn.close()
    return row
