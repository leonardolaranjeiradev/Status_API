from funcoes.api import checar_api
from funcoes.slack import enviar_slack   # 👈 corrigido

def tarefa():
    url_api = "https://pokeapi.co/api/v2/pokemon/erro"
    resultado = checar_api(url_api)
    if not resultado["ok"]:
        enviar_slack(resultado["mensagem"])  # 👈 corrigido
    else:
        print("API funcionando corretamente!")

# testar diretamente
tarefa()
