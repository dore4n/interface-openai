# 🚀 Flask OpenAI Chat Interface

Este projeto é uma aplicação Flask que serve uma interface web para interagir com a API da OpenAI. Ele permite que os usuários enviem perguntas, recebam respostas baseadas nos modelos da OpenAI, e listem os modelos disponíveis.

---

## 🛠️ Funcionalidades

- **Servir uma interface web estática**: A interface está localizada na pasta `chat-interface/dist` e é servida na raiz do aplicativo.
- **Interagir com a API da OpenAI**: Rota para enviar perguntas e receber respostas.
- **Listar modelos da OpenAI**: Endpoint para consultar os modelos disponíveis na API da OpenAI.

---

## 📂 Estrutura do Projeto

```plaintext
.
├── app.py                  # Código principal do servidor Flask
├── chat-interface/
│   └── dist/               # Interface web estática
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto
```

---

## 🚀 Como executar o projeto

### 1️⃣ Pré-requisitos

- Python 3.10+ instalado
- Conta na OpenAI para obter a API Key
- Gerenciador de pacotes `pip`

### 2️⃣ Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Substitua `sua_chave_api` no código pela sua chave de API da OpenAI.

### 3️⃣ Executando o projeto

Execute o servidor Flask:

```bash
python app.py
```

Acesse a aplicação no navegador em: [http://localhost:5000](http://localhost:5000).

---

## 🌐 Endpoints da API

### `/`
Serve os arquivos da interface web.

### `/ask` (POST)
Envia perguntas para a API da OpenAI.

- **Corpo da requisição (JSON):**
  ```json
  {
    "user_input": "Sua pergunta aqui",
    "model": "text-davinci-003" // Opcional, modelo padrão
  }
  ```
- **Resposta (JSON):**
  Retorna a resposta gerada pela OpenAI.

### `/models` (GET)
Lista os modelos disponíveis na OpenAI.

- **Resposta (JSON):**
  Retorna uma lista de modelos.

---

## 📜 Dependências

- Flask
- Requests

Instale as dependências com:
```bash
pip install -r requirements.txt
```

---

## 🛡️ Observações

- **Chave de API:** Certifique-se de não expor sua chave de API publicamente.
- **Uso Responsável:** Este projeto utiliza recursos da OpenAI que podem gerar custos dependendo do uso.

---

## 📧 Contato

Criado por **Lucas Emanuel Barboza Santos**.  
[LinkedIn](https://linkedin.com/in/lucasebsantos) | [GitHub](https://github.com/dore4n)
```

### Ajustes necessários:
1. **Repositório GitHub:** Atualize o link de clonagem e outras referências ao repositório.
2. **Interface Web:** Descreva melhor a interface caso ela tenha funcionalidades específicas.

Se precisar de mais algo, é só avisar! 🚀
