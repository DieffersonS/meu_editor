from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para salvar (já com suporte a nome de arquivo)
@app.route('/salvar', methods=['POST'])
def salvar():
    dados = request.get_json()
    conteudo = dados.get('conteudo')
    nome = dados.get('nome', 'nota_sem_nome')

    if not nome.endswith(".html"):
        nome += ".html"

    try:
        with open(nome, "w", encoding="utf-8") as f:
            f.write(conteudo)
        return jsonify({"status": "sucesso"})
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": str(e)}), 500

# Rota para listar os arquivos
@app.route('/listar', methods=['GET'])
def listar():
    arquivos = [f for f in os.listdir('.') if f.endswith('.html')]
    return jsonify(arquivos)

if __name__ == '__main__':
    # O Render define a porta automaticamente na variável de ambiente PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)