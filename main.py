from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    # Esse bloco serve para monitorar o que o jogo está pedindo
    print(f"O jogo tentou acessar a rota: /{path}")
    print(f"Método usado: {request.method}")
    if request.data:
        print(f"Dados enviados pelo jogo: {request.data.decode('utf-8', errors='ignore')}")
        
    # Resposta básica temporária para o jogo não travar
    return jsonify({
        "status": "success",
        "message": "Conectado ao servidor da comunidade!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

