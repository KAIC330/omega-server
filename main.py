from flask import Flask, request

app = Flask(__name__)

# Respondendo apenas 'success' em texto puro na raiz, comum para pings de validação
@app.route('/', methods=['GET', 'POST', 'HEAD'])
def home():
    # Se o jogo aceitar apenas a confirmação de que o link está ativo
    return "success"

# Se ele ignorar a raiz e passar a pedir o arquivo de versão em JSON depois
@app.route('/sdk_service', methods=['GET', 'POST'])
@app.route('/sdk_service/', methods=['GET', 'POST'])
def sdk_service():
    from flask import jsonify
    return jsonify({
        "code": 0,
        "msg": "success",
        "data": {
            "version": "1.0.795",
            "server_status": 1
        }
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
