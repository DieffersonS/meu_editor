# importa as bibliotecas que vamos utilizar

from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/salvar', methods=['POST'])
def salvar():
    # Recebe os dados em formato JSON vindos do navegador
    dados = request.get_json()
    conteudo_html = dados.get('conteudo')

    try:
        # Salva o conteúdo em um arquivo chamado 'nota.html'
        with open("minha_nota.html", "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo_html)
        
        return jsonify({"status": "sucesso", "mensagem": "Arquivo salvo com sucesso!"})
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)