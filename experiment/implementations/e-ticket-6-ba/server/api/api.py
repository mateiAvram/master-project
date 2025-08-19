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

import sqlite3
def delete_ticket(ticket_id):
    """
    Deletes the ticket with the given id from the SQLite database.
    """
    print("test", flush = True)
    conn = sqlite3.connect(PROJECT_ROOT + '/database.db')
    try:
        conn.execute('DELETE FROM tickets WHERE id = ?', (ticket_id,))
        conn.commit()
    finally:
        conn.close()

@app.route('/api/tickets/<int:ticket_id>', methods=['DELETE'])
def api_delete_ticket(ticket_id):
    """
    DELETE /api/tickets/123
    Deletes the ticket with id=123.
    Returns {"success": True} on success, or {"success": False, "error": "..."} on failure.
    """
    try:
        print("test", flush=True)
        delete_ticket(ticket_id)
        return jsonify(success=True), 200
    except Exception as e:
        # Optionally log the error here
        return jsonify(success=False, error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
