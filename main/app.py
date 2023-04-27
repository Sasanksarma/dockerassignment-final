from flask import Flask, request, render_template
import requests
import time
import mysql.connector

app = Flask(__name__)

# Replace these values with your MySQL server credentials
mysql_config = {
    'user': 'root',
    'password': '1234',
    'host': 'mysql',
    'database': 'flaskapp'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    number = request.form['number']
    operation = request.form['operation']
    if operation == 'Square':
        metric_start = time.time()
        response = requests.post(url='http://localhost:5001/square', data={'number': number})
        metric_end = time.time()
        metric = metric_end-metric_start
        store_metric('sqaure', metric)
    elif operation == 'Cube':
        response = requests.post(url='http://localhost:5002/cube', data={'number': number})
    elif operation == 'Fibonacci':
        response = requests.post(url='http://localhost:5003/fibonacci', data={'number': number})
    result = response.text
    return render_template('index.html', result=result)

def store_metric(table_name, metric):
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()
    query = f'INSERT INTO {table_name} (metric) VALUES (%s)'
    cursor.execute(query, (metric,))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    app.run(port=8000,host='0.0.0.0')
