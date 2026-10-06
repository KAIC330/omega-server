from flask import Flask, jsonify, request

app = Flask(__name__)

# Rota principal (onde o jogo bateu no seu log)
@app.route('/')
def home():
    # Geralmente os jogos esperam uma lista de servidores ou status aqui
    return jsonify({
        "status": "success",
        "message": "Servidor Fire Squad Ativo"
    })

# Rota crucial que você alterou no MT Manager (sdk_service)
@app.route('/sdk_service/', methods=['GET', 'POST'])
def sdk_service():
    # Aqui o jogo pede verificação de versão, login e termos
    # Você precisa estruturar a resposta conforme o jogo pede. 
    # Um exemplo genérico de resposta de versão aceita por jogos Unity:
    return jsonify({
        "code": 200,
        "msg": "success",
        "data": {
            "version": "1.0.795", # A versão exata que aparece no canto do seu jogo
            "force_update": False,
            "download_url": "",
            "server_status": 1 # 1 normalmente significa servidor online nos SDKs
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
