from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():
    operation = None
    return '''
        <form action="/square" method="post">
            <input type="text" name="number">
            <input type="submit" value="Square">
        </form>
    '''

@app.route('/square', methods=['POST'])
def square():
    number = int(request.form['number'])
    square = number ** 2
    operation = 'square'
    return f'The {operation} of {number} is {square}.'

if __name__ == '__main__':
    app.run(port=5001)