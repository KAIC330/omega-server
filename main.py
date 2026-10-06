from flask import Flask, jsonify, request

app = Flask(__name__)

# Nova tentativa na raiz com a estrutura JSON completa de SDKs mobile
@app.route('/', methods=['GET', 'POST', 'HEAD'])
def home():
    return jsonify({
        "code": 0,          # Muitas vezes 0 significa 'Sucesso' em APIs asiáticas
        "message": "success",
        "msg": "success",
        "data": {
            "version": "1.0.795",
            "force_update": 0,
            "force": False,
            "status": 1,
            "server_status": 1,
            "download_url": "",
            "update_url": ""
        }
    })

# Mantendo as rotas alternativas por precaução
@app.route('/sdk_service', methods=['GET', 'POST'])
@app.route('/sdk_service/', methods=['GET', 'POST'])
def sdk_service():
    return jsonify({
        "code": 0,
        "msg": "success",
        "data": {
            "version": "1.0.795",
            "force_update": 0,
            "server_status": 1
        }
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
