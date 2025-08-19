import os

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from business.ticket_manager import TicketManager

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', '..'))
CLIENT_DIR = os.path.join(PROJECT_ROOT, 'client')

app = Flask(__name__, static_folder=os.path.join(CLIENT_DIR, 'web'))

@app.route('/')
def serve_index():
    return send_from_directory(os.path.join(CLIENT_DIR, 'web'), 'index.html')

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory(os.path.join(CLIENT_DIR, 'assets'), filename)

@app.route('/style/<path:filename>')
def serve_style(filename):
    return send_from_directory(os.path.join(CLIENT_DIR, 'style'), filename)

@app.route('/scripts/<path:filename>')
def serve_scripts(filename):
    return send_from_directory(os.path.join(CLIENT_DIR, 'scripts'), filename)

# API Route example
@app.route('/hello_world', methods=['GET'])
def hello_world():
    data = {'message': 'hello world'}
    resp = jsonify(data)
    return resp

@app.route('/get_tickets', methods=['GET'])
def get_tickets():
    tm = TicketManager()
    try:
        data = tm.retrieve_tickets()
        resp = jsonify(data)
        return resp
    
    except Exception as e:
        data = {'message': e.args[0]}
        resp = jsonify(data)
        return resp

@app.route('/add_ticket', methods=['POST'])
def add_ticket():
    data = request.json
    tm = TicketManager()
    try:
        tm.insert_ticket(data)
        data = {'message': 'OK'}
        resp = jsonify(data)
        return resp
    
    except Exception as e:
        data = {'message': e.args[0]}
        resp = jsonify(data)
        return resp

@app.route('/delete_ticket', methods=['DELETE'])
def delete_ticket():
    payload = request.get_json()
    print(payload)
    try:
        success = TicketManager.delete_ticket(payload)
        return jsonify({'status': 'success', 'deleted_id': payload.get('id')}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
