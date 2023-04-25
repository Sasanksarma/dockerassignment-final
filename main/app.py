from flask import Flask, request, render_template
from flask_mysqldb import MySQL
import requests
import time,os
import mysql.connector

app = Flask(__name__)

# Replace these values with your MySQL server credentials
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'root')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'flaskapp')

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    number = request.form['number']
    operation = request.form['operation']
    if operation == 'Square':
        metric_start = time.time()
        response = requests.post('http://localhost:5001/square', data={'number': number})
        metric_end = time.time()
        metric = metric_end-metric_start
        store_metric('sqaure', metric)
    elif operation == 'Cube':
        response = requests.post('http://localhost:5002/cube', data={'number': number})
    elif operation == 'Fibonacci':
        response = requests.post('http://localhost:5003/fibonacci', data={'number': number})
    result = response.text
    return render_template('index.html', result=result)

def store_metric(table_name, metric):
    conn = mysql.connect()
    cursor = mysql.connection.cursor()
    cursor.execute('Use database flaskapp')
    cursor.execute(f'create table {table_name}(metric float)')
    query = f'INSERT INTO {table_name} (metric) VALUES (%s)'
    cursor.execute(query, (metric,))
    cursor.close()
    conn.close()

if __name__ == '__main__':
    app.run(port=8000)