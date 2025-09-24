import requests

def enviar_slack(mensagem):
    # URL do Webhook (você pega no Slack, siga os passos no arquivo url_slack)
    webhook_url = "URL WEBHOOK"  

    payload = {"text": mensagem}  # O Slack espera JSON com a chave "text"

    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            print("Mensagem enviada para o Slack com sucesso!")
        else:
            print(f"Erro ao enviar para o Slack: {response.status_code}, {response.text}")
    except Exception as e:
        print("Erro ao conectar com Slack:", e)
