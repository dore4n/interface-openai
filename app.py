from flask import Flask, send_from_directory, request, jsonify
import requests
import os

app = Flask(__name__, static_folder='chat-interface/dist')

OPENAI_API_KEY = 'sua_chave_api_aqui'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data['user_input']
    model = data.get('model', 'text-davinci-003')

    response = requests.post(
        f'https://api.openai.com/v1/engines/{model}/completions',
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
        return jsonify({'error': 'Erro ao acessar a API da OpenAI.', 'status_code': response.status_code})

@app.route('/models', methods=['GET'])
def get_models():
    response = requests.get(
        'https://api.openai.com/v1/engines',
        headers={
            'Authorization': f'Bearer {OPENAI_API_KEY}'
        }
    )
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Erro ao buscar modelos da OpenAI.'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
