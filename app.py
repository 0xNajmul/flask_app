from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)

# index page
@app.route('/')
def index():
    return render_template('home.html')

# about page
@app.route('/about')
def about():
    return render_template('about.html')

# articles page
@app.route('/articles')
def articles():    
    return render_template('articles.html')

# dashboard page 
@app.route('/dashboard')
def dashboard():    
    return render_template('dashboard.html')

# contact page 
@app.route('/contact')
def contact():    
    return render_template('contact.html')

# login page
@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)