from flask import Flask, request, Response

app = Flask(__name__)

# Mudando para responder texto puro na raiz ('/'), imitando um arquivo de configuração (.txt)
@app.route('/', methods=['GET', 'POST', 'HEAD'])
def home():
    # Estrutura padrão de arquivo VersionList para checagem da Unity
    text_data = (
        "version=1.0.795\n"
        "force_update=false\n"
        "server_status=1\n"
        "download_url=\n"
    )
    # Enviamos como 'text/plain' para o jogo ler as linhas diretamente
    return Response(text_data, mimetype='text/plain')

# Deixamos essa rota caso ele busque em formato JSON em outro momento
@app.route('/sdk_service', methods=['GET', 'POST'])
@app.route('/sdk_service/', methods=['GET', 'POST'])
def sdk_service():
    from flask import jsonify
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
