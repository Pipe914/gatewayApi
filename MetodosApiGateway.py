from flask import Flask, jsonify, request
import requests
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

# Metodos ToDo

@app.route('/todo', methods=['GET'])
def getTodosTodo():
    resp = requests.get('http://127.0.0.1:5000/api/todo')
    if resp.status_code == 200:
        return resp.json(), 200

@app.route('/todo/<id>', methods=['GET'])
def getTodo(id):
    resp = requests.get(f'http://127.0.0.1:5000/api/todo/{id}')
    if resp.status_code == 200:
        return resp.json(), 200

@app.route('/todo', methods=['POST'])
def crearTodo():
    dataPost = request.get_json(force=True)
    resp = requests.post('http://127.0.0.1:5000/api/todo', json = dataPost)
    if resp.status_code == 201:
        return  resp.json(), 201

@app.route('/todo/<id>', methods=['PATCH'])
def actualizarTodo(id):
    dataPost = request.get_json(force=True)
    resp = requests.patch(f'http://127.0.0.1:5000/api/todo/{id}', json=dataPost)
    if resp.status_code == 204:
        return jsonify(), 204

@app.route('/todo/<id>', methods=['DELETE'])
def eliminarTodo(id):
    resp = requests.delete(f'http://127.0.0.1:5000/api/todo/{id}')
    if resp.status_code == 204:
        return jsonify(), 204


# Metodos Agenda Contactos

@app.route('/contacts', methods=['GET'])
def getTodosContact():
    resp = requests.get('http://127.0.0.1:8000/api/contacts')
    if resp.status_code == 200:
        return resp.json(), 200

@app.route('/contacts/<id>', methods=['GET'])
def getContact(id):
    resp = requests.get(f'http://127.0.0.1:8000/api/contacts/{id}')
    if resp.status_code == 200:
        return resp.json(), 200

@app.route('/contacts', methods=['POST'])
def crearContact():
    dataPost = request.get_json(force=True)
    resp = requests.post('http://127.0.0.1:8000/api/contacts', json = dataPost)
    if resp.status_code == 201:
        return  resp.json(), 201

@app.route('/contacts/<id>', methods=['PUT'])
def actualizarContact(id):
    dataPost = request.get_json(force=True)
    resp = requests.put(f'http://127.0.0.1:8000/api/contacts/{id}', json=dataPost)
    if resp.status_code == 204:
        return jsonify(), 204

@app.route('/contacts/<id>', methods=['DELETE'])
def eliminarContact(id):
    resp = requests.delete(f'http://127.0.0.1:8000/api/contacts/{id}')
    if resp.status_code == 204:
        return jsonify(), 204



def runApi():
    app.run(host="0.0.0.0", port="10000", debug=True)
