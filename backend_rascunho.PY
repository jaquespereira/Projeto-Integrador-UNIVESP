import requests
import json

# URL da API do Banco Central para a taxa Selic
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"

# Função para obter a taxa Selic atual
def obter_taxa_selic_atual():
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        if dados:
            # A API retorna os dados em ordem cronológica reversa, então o primeiro registro é o mais recente.
            taxa_atual = float(dados[0]['valor'])
            return taxa_atual
    return None

# Chama a função para obter a taxa Selic atual
taxa_atual = obter_taxa_selic_atual()

if taxa_atual is not None:
    print(f"A taxa Selic atual é de: {taxa_atual:.2f}%")
else:
    print("Não foi possível obter a taxa Selic atual. Verifique a URL da API ou a conexão com a internet.")


jupyter --> documentacao; API NAVEGADOR DE DADOS; (endpoints par pegar requicoas )
codgio, metodo e parametro 

sandbox --> voce pode ir testando e consumindo 



importa o requests]]


URL = 

requisca = request.get(URL =)
informacoe = requisica.json ()

voCE NAO PRCISA FAZER AUTENTICACAO 


PARAMENTO JSON QUE ARMAZENA (requisciao) ==> kk
informacoe te traz uma lista, dicionario 

parametros da data

panda numby editor ==> jupiter
