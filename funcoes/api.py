import requests

# define a função 'checar_api' que recebe a URL da API como parâmetro
def checar_api(url):  

 # Bloco que tenta executar o código; se houver erro de rede, será capturado no except   
    try:
        response = requests.get(url)  # faz uma requisição HTTP GET para a URL passada e guarda a resposta
        if response.status_code == 200:  # verifica se o status HTTP retornado é 200 (OK)
            return {"ok": True}  # retorna um dicionário indicando que a API está funcionando corretamente
        else:  # se o status não for 200
            return {"ok": False, "mensagem": f"Erro na API: {response.status_code}"}  
            # retorna um dicionário indicando que houve erro, com a informação do código HTTP
    except requests.exceptions.RequestException as e:  # captura qualquer exceção gerada pela requisição
        return {"ok": False, "mensagem": f"Erro ao acessar API: {e}"}  
        # retorna um dicionário indicando que houve erro de conexão, mostrando a mensagem do erro
