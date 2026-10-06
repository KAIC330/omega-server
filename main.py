from flask import Flask, jsonify, request

app = Flask(__name__)

# Rota principal (onde o jogo bate na inicialização)
@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "Servidor Fire Squad Ativo"
    })

# Rota sem a barra no final (evita erro 404 caso o jogo peça sem barra)
@app.route('/sdk_service', methods=['GET', 'POST'])
# Rota com a barra no final (a que você alterou no MT Manager)
@app.route('/sdk_service/', methods=['GET', 'POST'])
def sdk_service():
    # Resposta estruturada padrão para checagem de versão de pacotes Unity
    return jsonify({
        "code": 200,
        "msg": "success",
        "data": {
            "version": "1.0.795", 
            "force_update": False,
            "download_url": "",
            "server_status": 1
        }
    })

if __name__ == '__main__':
    # O Render exige que o servidor rode na porta fornecida pelo sistema deles
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
