from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="/fibonacci" method="post">
            <input type="text" name="number">
            <input type="submit" value="Fibonacci">
        </form>
    '''

@app.route('/fibonacci', methods=['POST'])
def fibonacci():
    number = int(request.form['number'])
    a, b = 0, 1
    sequence = []
    for _ in range(number):
        sequence.append(a)
        a, b = b, a + b
    return f'The first {number} numbers of the Fibonacci sequence are: {sequence}.'

if __name__ == '__main__':
    app.run(port=5003)