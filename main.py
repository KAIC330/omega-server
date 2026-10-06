from flask import Flask, jsonify, request
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'HEAD'])
def home():
    # Isso vai forçar o Render a mostrar no log tudo o que o celular enviou
    print("=== NOVA REQUISIÇÃO DO JOGO ===", file=sys.stderr)
    print(f"Método: {request.method}", file=sys.stderr)
    print(f"Args (URL): {request.args}", file=sys.stderr)
    print(f"Headers: {dict(request.headers)}", file=sys.stderr)
    print(f"Dados brutos: {request.data}", file=sys.stderr)
    print("===============================", file=sys.stderr)
    
    # Vamos tentar responder um JSON de inicialização limpo e completo de servidores Unity
    return jsonify({
        "status": 0,
        "code": 0,
        "msg": "success",
        "data": {
            "version": "1.0.795",
            "server_status": 1,
            "force_update": False
        }
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
