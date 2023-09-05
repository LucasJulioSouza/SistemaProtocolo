from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    protocolo = ""
    name = ""
    phoneNumber = ""
    PROVEDOR = ""

    if request.method == "POST":
        protocolo = request.form.get("protocolo")
        url = f"http://192.168.210.26:5678/webhook/buscar-atendimento-protocolo?protocolo={protocolo}"
        response = requests.get(url)

        try:
            data = json.loads(response.text)
            name = data.get("name", "N/A")
            phoneNumber = data.get("phoneNumber", "N/A")
            PROVEDOR = data.get("PROVEDOR", "N/A")
        except json.JSONDecodeError:
            return "Erro ao analisar a resposta JSON"

    return render_template("index.html", protocolo=protocolo, name=name, phoneNumber=phoneNumber, PROVEDOR=PROVEDOR)

if __name__ == "__main__":
    app.run(debug=True)
