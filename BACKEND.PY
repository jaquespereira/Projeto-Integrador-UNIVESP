https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries

https://dadosabertos.bcb.gov.br/dataset/11-taxa-de-juros---selic/resource/b73edc07-bbac-430c-a2cb-b1639e605fa8



import requests
import json

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"

def taxaselic_atual():
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        if dados:
            taxa_atual = float(dados[0]['resultado'])
            return taxa_atual
    return None

taxa_atual = taxaselic_atual()

if taxa_atual is not None:
    print(f"A taxa Selic atual é de: {taxa_atual:.2f}%")
else:
    print("Não foi possível obter a taxa Selic atual. Verifique a URL da API ou a conexão com a internet.")