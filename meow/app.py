import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

# get_db_connection
def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='meowculator',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'],
                            port=6969)

    return conn

# index
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()

    meats = {} # pass to render_template

    # build render object with data pulled from db
    cur.execute('SELECT * FROM chicken')
    meats["chicken"] = cur.fetchall()
    cur.execute('SELECT * FROM duck')
    meats["duck"] = cur.fetchall()
    cur.execute('SELECT * FROM lamb')
    meats["lamb"] = cur.fetchall()
    cur.execute('SELECT * FROM pork')
    meats["pork"] = cur.fetchall()
    cur.execute('SELECT * FROM rabbit')
    meats["rabbit"] = cur.fetchall()
    cur.execute('SELECT * FROM turkey')
    meats["turkey"] = cur.fetchall()
    cur.execute('SELECT * FROM others')
    meats["others"] = cur.fetchall()

    # Close everyting
    cur.close()
    conn.close()

    return render_template('index.html', meats=meats)