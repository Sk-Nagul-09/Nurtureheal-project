from flask import Flask, jsonify
from datetime import datetime
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUESTS = Counter('drviki_requests_total', 'Total HTTP requests')

@app.route('/')
def hello():
    REQUESTS.inc()
    return f"Hello from Dr. ViKi DevOps Pipeline! — {datetime.utcnow().isoformat()}Z"

@app.route('/health')
def health():
    return jsonify(status='ok')

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
