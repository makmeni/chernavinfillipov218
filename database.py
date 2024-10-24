import sqlite3

def init_db():
    conn = sqlite3.connect('freelance.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS articles
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  content TEXT NOT NULL,
                  image_url TEXT NOT NULL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS resumes
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  description TEXT NOT NULL,
                  image_url TEXT NOT NULL,
                  category TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_article(title, content, image_url):
    conn = sqlite3.connect('freelance.db')
    c = conn.cursor()
    c.execute("INSERT INTO articles (title, content, image_url) VALUES (?, ?, ?)", (title, content, image_url))
    conn.commit()
    conn.close()

def add_resume(title, description, image_url, category):
    conn = sqlite3.connect('freelance.db')
    c = conn.cursor()
    c.execute("INSERT INTO resumes (title, description, image_url, category) VALUES (?, ?, ?, ?)", (title, description, image_url, category))
    conn.commit()
    conn.close()

# Пример добавления статей и резюме
init_db()
