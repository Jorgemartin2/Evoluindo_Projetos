import json, requests

moedas_disponiveis=['USD','EUR','BRL','JPY']
print('MOEDAS DISPONIVEIS')
for moedas in moedas_disponiveis:
    print(f'-{moedas}')

origem=input(str('Moeda de origem: ')).strip().upper()
destino=input(str('Moeda de destino: ')).strip().upper()

if origem in moedas_disponiveis and destino in moedas_disponiveis:
    requisicao=requests.get(f"https://economia.awesomeapi.com.br/{origem}-{destino}")
    cotacao=requisicao.json()
    print(f'1 {origem} equivale á {float(cotacao[0]["bid"]):.2f} {destino}')
else:
    print('Moedas inválidas.')