from flask import Flask, request, Response, make_response
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'HEAD'])
def home():
    print("=== ENVIANDO RESPOSTA DE TEXTO PURA ===", file=sys.stderr)
    
    # Captura a chave de segurança que o celular enviou
    x_request_start = request.headers.get('X-Request-Start', '')
    
    # Formato de texto misto (Variáveis diretas + Chaves internas)
    # É o padrão definitivo que os injetores de pacotes da Unity leem sem quebrar o JSON
    raw_text = (
        "code=0\n"
        "status=1\n"
        "msg=success\n"
        "version=1.0.795\n"
        "server_status=1\n"
        "force_update=false\n"
        "download_url=\n"
        "update_url=\n"
    )
    
    # Força o Flask a responder como TEXTO PURO (mimetype='text/plain')
    response = make_response(Response(raw_text, mimetype='text/plain'))
    
    # Devolve a chave de segurança obrigatória nos cabeçalhos
    if x_request_start:
        response.headers['X-Request-Start'] = x_request_start
        response.headers['X-Request-Sign'] = x_request_start
        response.headers['X-Sign'] = x_request_start
        
    return response

@app.route('/sdk_service', methods=['GET', 'POST'])
@app.route('/sdk_service/', methods=['GET', 'POST'])
def sdk_service():
    return home()

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
