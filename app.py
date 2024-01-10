from flask import Flask, send_from_directory, request, jsonify
import requests
import os

app = Flask(__name__, static_folder='chat-interface/dist')

OPENAI_API_KEY = 'SECRETKEY_OPENAI'

# Rota para servir os arquivos estáticos
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

# Rota para interagir com a API da OpenAI
@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data['user_input']

    response = requests.post(
        'https://api.openai.com/v1/engines/davinci-codex/completions',
        headers={
            'Authorization': f'Bearer {OPENAI_API_KEY}',
            'Content-Type': 'application/json'
        },
        json={
            'prompt': user_input,
            'max_tokens': 150
        }
    )

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Erro ao acessar a API da OpenAI.'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
