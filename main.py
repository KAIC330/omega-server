from flask import Flask, jsonify, request

app = Flask(__name__)

# O jogo está batendo aqui na raiz ('/') buscando as versões!
@app.route('/', methods=['GET', 'POST', 'HEAD'])
def home():
    # Entregando os dados de versão direto na rota principal
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

# Mantemos esta rota por segurança caso o jogo chame ela depois
@app.route('/sdk_service', methods=['GET', 'POST'])
@app.route('/sdk_service/', methods=['GET', 'POST'])
def sdk_service():
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
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
