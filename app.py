from flask import Flask
import datetime
app = Flask(__name__)

@app.route('/')
def hello():
    return f"Hello from Dr. ViKi DevOps Pipeline! Time: {datetime.datetime.now()}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

