from flask import Flask
app = Flask(__name__)

@app.route('/square/<num>')
def square(num):
    num = int(num)
    return str(num**2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


