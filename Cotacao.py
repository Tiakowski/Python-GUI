import requests
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto




janela = Tk()
janela.title("Cotação")
janela.geometry("300x200")


texto_inicial = Label(janela, text="Dolar/Euro/BTC:")
texto_inicial.place(x=100,y=0)

botão = Button(janela, text='Buscar Cotações', command= pegar_cotacoes)
botão.place(x=100,y=50, width=100, height=50)

texto_cotacoes = Label(janela,text="")
texto_cotacoes.place(x=100,y=100)


janela.mainloop()