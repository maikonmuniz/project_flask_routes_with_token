from flask import Flask, request, jsonify
import requests as r
import uuid

app = Flask('app')

def get_address(zipcode):
    res = r.get(f'https://viacep.com.br/ws/{zipcode}/json/')
    return res.json()

@app.route('/message', methods=["POST"])
def create_message():
    data = request.json
    message = data['message']
    zipcode = data['zipcode']

    address = get_address(zipcode)
    confirmation_message = {}
    confirmation_message['address'] = address
    confirmation_message['message'] = message
    confirmation_message['token'] = uuid.uuid4()

    return jsonify(confirmation_message)

@app.route('/message/send/<string:token>', methods=["PUT"])
def send_message(token):
    data = request.json
    message = data.get('message', 'mensagem original')
    print(f'token de confirmação {token}')
    print(f'texto corrigido {message}')

    return jsonify({'response': 'Mensagem enviada com sucesso!'})

app.run(host='localhost', port=5000, debug=True)
