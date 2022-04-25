"""A Flask application that serves as a simple web calculator"""

from flask import Flask
app = Flask(__name__)


@app.route('/square/<num>')
def square(num):
    """
    This function takes a number and returns the square of it
    """

    num = int(num)
    return str(num**2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
