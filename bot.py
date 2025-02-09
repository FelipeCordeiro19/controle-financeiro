from flask import Flask, request
import pandas as pd
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)
FILE_NAME = "gastos.xlsx"

# Criar ou carregar o arquivo Excel
if os.path.exists(FILE_NAME):
    df = pd.read_excel(FILE_NAME)
else:
    df = pd.DataFrame(columns=["Data", "Descrição", "Valor"])

@app.route("/bot", methods=["POST"])
def bot():
    msg = request.form.get("Body")  # Mensagem recebida no WhatsApp
    response = registrar_gasto(msg)  # Processar mensagem

    twilio_resp = MessagingResponse()
    twilio_resp.message(response)  # Responder ao usuário
    return str(twilio_resp)

def registrar_gasto(mensagem):
    try:
        partes = mensagem.split(",")  # Exemplo: "Almoço, 25.50"
        descricao = partes[0].strip()
        valor = float(partes[1].strip())

        global df
        df = df.append({"Data": pd.Timestamp.now(), "Descrição": descricao, "Valor": valor}, ignore_index=True)
        df.to_excel(FILE_NAME, index=False)

        return f"Gasto registrado: {descricao} - R$ {valor:.2f}"
    except Exception as e:
        return f"Erro ao registrar gasto: {e}"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
