from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

# Rota para aceitar a checagem inicial do jogo (HEAD)
@app.route('/', methods=['HEAD', 'GET'])
def index():
    response = make_response()
    # Adiciona cabeçalhos que jogos mobile exigem para aceitar conexões
    response.headers['Content-Type'] = 'application/json'
    response.headers['Server'] = 'community-server'
    if request.method == 'GET':
        response.data = '{"status": "success", "message": "Omega Legends Community Server Online"}'
    return response

# Rota curinga para capturar qualquer pedido secreto que o jogo fizer depois
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT'])
def catch_all(path):
    print(f"\n[ALERTA] O jogo tentou acessar uma rota secreta: /{path}")
    print(f"Método: {request.method}")
    if request.data:
        print(f"Dados enviados pelo jogo: {request.data.decode('utf-8', errors='ignore')}")
    
    # Responde um JSON padrão simulando sucesso para tentar destravar a tela do jogo
    return jsonify({
        "code": 0,
        "msg": "success",
        "data": {}
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
