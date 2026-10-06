from flask import Flask, jsonify, request, make_response
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'HEAD'])
def home():
    # Print de diagnóstico para acompanhar no painel do Render
    print("=== REQUISIÇÃO RECEBIDA DE VERSÃO ===", file=sys.stderr)
    
    # Captura os códigos de segurança enviados pelo cabeçalho do celular
    x_request_start = request.headers.get('X-Request-Start', '')
    
    # Essa é a estrutura exata e completa exigida por SDKs de jogos Unity
    json_data = jsonify({
        "code": 200,             # Código de sucesso interno da API
        "status": "success",     # Algumas versões checam por status
        "msg": "success",
        "message": "success",
        "version": "1.0.795",    # A versão exata que aparece no canto do seu jogo
        "data": {
            "version": "1.0.795",
            "server_status": 1,   # 1 = Servidor Online
            "status": 1,
            "force_update": False,
            "force": False,
            "download_url": "",
            "update_url": ""
        }
    })
    
    response = make_response(json_data)
    
    # Injeta de volta todas as chaves de segurança que o jogo enviou para validar a conexão
    if x_request_start:
        response.headers['X-Request-Start'] = x_request_start
        response.headers['X-Request-Sign'] = x_request_start
        response.headers['X-Sign'] = x_request_start
        
    return response

# Rota alternativa caso o jogo tente buscar por pastas após a validação inicial
@app.route('/sdk_service', methods=['GET', 'POST'])
@app.route('/sdk_service/', methods=['GET', 'POST'])
def sdk_service():
    return home()

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
