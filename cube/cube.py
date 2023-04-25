from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="/cube" method="post">
            <input type="text" name="number">
            <input type="submit" value="Cube">
        </form>
    '''

@app.route('/cube', methods=['POST'])
def cube():
    number = int(request.form['number'])
    cube = number ** 3
    return f'The cube of {number} is {cube}.'

if __name__ == '__main__':
    app.run(port=5002)
