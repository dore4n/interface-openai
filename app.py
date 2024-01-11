from flask import Flask, send_from_directory, request, jsonify
import requests
import os

app = Flask(__name__, static_folder='chat-interface/dist')

OPENAI_API_KEY = 'sua_chave_api'  # Substitua com sua chave de API real
headers = {
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}

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

    try:
        response = requests.post(
            'https://api.openai.com/v1/completions',
            headers=headers,
            json={
                'model': model,
                'prompt': user_input,
                'max_tokens': 150
            }
        )
        print("Resposta da API OpenAI:", response.json())  # Log para depuração
        return jsonify(response.json())
    except Exception as e:
        print("Erro ao acessar a API da OpenAI:", e)  # Log para depuração
        return jsonify({'error': str(e)})

@app.route('/models', methods=['GET'])
def get_models():
    try:
        response = requests.get('https://api.openai.com/v1/models', headers=headers)
        print("Modelos disponíveis:", response.json())  # Log para depuração
        return jsonify(response.json())
    except Exception as e:
        print("Erro ao buscar modelos:", e)  # Log para depuração
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
