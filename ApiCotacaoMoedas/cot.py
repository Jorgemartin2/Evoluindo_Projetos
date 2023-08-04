import json, requests
from tkinter import *

def pegar_cotacao():
    requisicao=requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacao=requisicao.json()
    cotacao_dolar=cotacao["USDBRL"]["bid"]
    cotacao_euro=cotacao["EURBRL"]["bid"]
    cotacao_btc=cotacao["BTCBRL"]["bid"]

    texto=f'''
    Dólar= {cotacao_dolar}
    Euro= {cotacao_euro}
    Bitcoin= {cotacao_btc}'''

    texto_cotacao["text"]=texto

janela=Tk()
janela.title("Cotação atual das moedas")
janela.geometry("300x300")

texto=Label(janela, text="Clique aqui para visualizar a cotação")
texto.grid(column=0, row=0, padx=50, pady=50)

botao=Button(janela, text="Buscar cotações Dólar/Euro/Bitcoin", command=pegar_cotacao)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_cotacao=Label(janela, text="")
texto_cotacao.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()