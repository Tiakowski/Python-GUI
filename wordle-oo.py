from tkinter import *

class entradas:
    def __init__ (self,linha):
        self.a = a = StringVar()
        self.linha = linha
        letra1 = Entry(janela, width=3,font=("Helvetica", 32), justify="center",textvariable=a)
        letra1.grid(column=0,row=self.linha)

    def mudar(self,letra):
        self.a.set(letra)



janela = Tk()
Primeiro = entradas(0)
Primeiro.mudar("A")
Segundo = entradas(1)
Segundo.mudar("B")
janela.mainloop()
