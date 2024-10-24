from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from forms import ResumeForm
from database import init_db, add_article, add_resume  # Импортируем функции из database.py

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

def get_db_connection():
    conn = sqlite3.connect('freelance.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/articles')
def articles():
    conn = get_db_connection()
    articles = conn.execute('SELECT * FROM articles').fetchall()
    conn.close()
    return render_template('articles.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    conn = get_db_connection()
    article = conn.execute('SELECT * FROM articles WHERE id = ?', (article_id,)).fetchone()
    conn.close()
    return render_template('article.html', article=article)

@app.route('/marketplace')
def marketplace():
    conn = get_db_connection()
    resumes = conn.execute('SELECT * FROM resumes').fetchall()
    conn.close()
    return render_template('marketplace.html', resumes=resumes)

@app.route('/resume/<int:resume_id>')
def resume(resume_id):
    conn = get_db_connection()
    resume = conn.execute('SELECT * FROM resumes WHERE id = ?', (resume_id,)).fetchone()
    conn.close()
    return render_template('resume.html', resume=resume)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/developers')
def developers():
    return render_template('developers.html')

if __name__ == '__main__':
    init_db()  # Инициализируем базу данных при запуске приложения
    app.run(debug=True)