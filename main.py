from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

# Resposta para a checagem inicial que o jogo já está fazendo
@app.route('/', methods=['HEAD', 'GET'])
def index():
    response = make_response('{"status": "success", "message": "Omega Server Online"}')
    response.headers['Content-Type'] = 'application/json'
    return response

# Rota simulando o sistema de Atualização (Patch) da IGG
@app.route('/all_patch', methods=['GET', 'POST'])
@app.route('/patch', methods=['GET', 'POST'])
def patch_check():
    print("[LOG] Jogo checou atualizações de patch!")
    return jsonify({
        "code": 0,
        "msg": "success",
        "data": {
            "version": "1.0.77",
            "download_url": "",
            "force_update": False
        }
    })

# Rota simulando o sistema de Login da IGG
@app.route('/login', methods=['GET', 'POST'])
@app.route('/account', methods=['GET', 'POST'])
def login_sim():
    print(f"[LOG] Tentativa de login recebida! Dados: {request.data}")
    return jsonify({
        "code": 0,
        "msg": "success",
        "data": {
            "user_id": "123456",
            "token": "comunidade_omega_token",
            "nickname": "JogadorOmega"
        }
    })

# Captura qualquer outra rota que o jogo inventar
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT'])
def catch_all(path):
    print(f"[ALERTA MESTRE] Rota desconhecida acessada: /{path}")
    return jsonify({"code": 0, "msg": "success", "data": {}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
