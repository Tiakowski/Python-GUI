from tkinter import *
import collections
from tkinter import messagebox
from PalavraFUT import palavra_aleatoria

class entradas:
    def __init__ (self,linha, palavra):
        self.palavra = palavra
        focado = False
        self.focado = focado
        acertos = 0
        completo = False
        self.acertos = acertos
        self.completo = completo
        status = True
        self.status = status

        self.a = a = StringVar()
        self.linha = linha
        self.letra1 = letra1 = Entry(janela, width=3,font=("Helvetica", 32), justify="center",textvariable=a)
        self.letra1grid = letra1.grid(column=0,row=self.linha,pady=2,padx=1)

        self.b = b = StringVar()
        self.letra2 = letra2 = Entry(janela, width=3,font=("Helvetica", 32), justify="center",textvariable=b)
        self.letra2grid = letra2.grid(column=1,row=self.linha,pady=2,padx=1)

        self.c = c = StringVar()
        self.letra3 = letra3 = Entry(janela, width=3,font=("Helvetica", 32), justify="center",textvariable=c)
        self.letra3grid =letra3.grid(column=2,row=self.linha,pady=2,padx=1)


        self.d = d = StringVar()
        self.letra4 = letra4 = Entry(janela, width=3,font=("Helvetica", 32), justify="center",textvariable=d)
        self.letra4grid = letra4.grid(column=3,row=self.linha,pady=2,padx=1)

        self.e = e = StringVar()
        self.letra5 = letra5 = Entry(janela, width=3,font=("Helvetica", 32), justify="center",textvariable=e)
        self.letra5grid = letra5.grid(column=4,row=self.linha,pady=2,padx=1)

    def caps(self, numero, foco):
        naopode = [13,8,37]
        
        #Códigos keycode:
        #13 = Enter / 8 = Delete / 39 = Seta pra direita / 37 = Seta pra esquerda

        #Enter
        if int(numero) == 13:
            self.verificar()

        #Inserir a letra maiuscula e foco no próximo entry
        if int(numero) not in naopode:
            if foco == self.letra1:
                if int(numero) != 39:
                    self.a.set(chr(int(numero)))
                self.letra2.focus_set()

            elif foco == self.letra2:
                if int(numero) != 39:
                    self.b.set(chr(int(numero)))
                self.letra3.focus_set()

            elif foco == self.letra3:
                if int(numero) != 39:
                    self.c.set(chr(int(numero)))
                self.letra4.focus_set()

            elif foco == self.letra4:
                if int(numero) != 39:
                    self.d.set(chr(int(numero)))
                self.letra5.focus_set()

            elif foco == self.letra5:
                if int(numero) != 39:
                    self.e.set(chr(int(numero)))

        #Delete e entry anterior
        elif int(numero) == 8 or int(numero) == 37:
            if foco == self.letra1:
                if int(numero) == 8:
                    self.letra1.delete(0,'end')

            elif foco == self.letra2:
                if int(numero) == 8:
                    self.letra2.delete(0,'end')
                self.letra1.focus_set()

            elif foco == self.letra3:
                if int(numero) == 8:
                    self.letra3.delete(0,'end')
                self.letra2.focus_set()

            elif foco == self.letra4:
                if int(numero) == 8:
                    self.letra4.delete(0,'end')
                self.letra3.focus_set()

            elif foco == self.letra5:
                if int(numero) == 8:
                    self.letra5.delete(0,'end')
                self.letra4.focus_set()

    def verificar(self):
        palavra_contada =dict(collections.Counter(self.palavra))
        contador_branco = 0
        a = self.letra1.get()
        b = self.letra2.get()
        c = self.letra3.get()
        d = self.letra4.get()
        e = self.letra5.get()

        if a != "" and b != "" and c != "" and d != "" and e != "":

            self.completo = True
            chute = [a,b,c,d,e]
            entradas = [self.letra1,self.letra2,self.letra3,self.letra4,self.letra5]

            for letra in chute:
                if letra in palavra_contada:
                    for i in palavra_contada:
                        if letra == i:
                            if palavra_contada[letra] != 0:
                                if letra == self.palavra[contador_branco]:
                                    quantidade = palavra_contada[letra]
                                    palavra_contada={**palavra_contada, letra:quantidade-1}
                                    entradas[contador_branco].config({"background": "Green"})
                                    entradas[contador_branco].configure({"disabledbackground": "Green"})
                                    entradas[contador_branco].configure({"disabledforeground":"Black"})
                                    self.acertos += 1
    
                else:
                    entradas[contador_branco].configure({"disabledforeground":"Black"})
                contador_branco += 1                    

            contador_branco = 0 
            for letra in chute:
                if letra in self.palavra:
                    for i in palavra_contada:
                        if letra == i:
                            if palavra_contada[letra] != 0:
                                quantidade = palavra_contada[letra]
                                palavra_contada={**palavra_contada, letra:quantidade-1}
                                entradas[contador_branco].config({"background": "Orange"})
                                entradas[contador_branco].configure({"disabledbackground": "Orange"})
                                entradas[contador_branco].configure({"disabledforeground":"Black"})               
                contador_branco += 1 
    
    def acertados(self):
        if self.acertos == 5:
            return True
        else:
            return False

    def completos(self):
        return self.completo

    def desativar (self):
        entradas = [self.letra1,self.letra2,self.letra3,self.letra4,self.letra5]
        for i in entradas:
            i['state'] = 'disabled'
        self.status = False

    def ativar(self):
        entradas = [self.letra1,self.letra2,self.letra3,self.letra4,self.letra5]
        for i in entradas:
            i['state'] = 'normal'
        self.status = True
        
    def focus(self):
        if not self.focado:
            self.letra1.focus_set()
            self.focado = True

    def comota(self):
        return self.status

palavra = palavra_aleatoria()
janela = Tk()
janela.title("Worlde")
janela.config(background="#fffafa")
Primeiro = entradas(0,palavra)
Segundo = entradas(1,palavra)
Terceiro = entradas(2,palavra)
Quarto = entradas(3,palavra)
Quinto = entradas(4,palavra)

# botao_verificar = Button(text="Verificar",height=2,bg="#5ab1c8",fg="black",width=20,font=("Helvetica",12,"bold"))
# botao_verificar.grid(column=1,columnspan=3, row=5,pady=20)

Segundo.desativar()
Terceiro.desativar()
Quarto.desativar()
Quinto.desativar()
Primeiro.focus()
print(palavra)
endereço = Primeiro

def digitar (event):
    letra = repr(event.keycode)
    teste = janela.focus_get()
    if Primeiro.comota():
        Primeiro.caps(numero=letra, foco=teste)
    if Segundo.comota():
        Segundo.caps(numero=letra, foco=teste)
    if Terceiro.comota():
        Terceiro.caps(numero=letra, foco=teste)
    if Quarto.comota():
        Quarto.caps(numero=letra, foco=teste)
    if Quinto.comota():
        Quinto.caps(numero=letra, foco=teste)

        
    if Primeiro.completos():
        Primeiro.desativar()
        if not Primeiro.acertados():
            Segundo.ativar()
            Segundo.focus()

    if Segundo.completos():
         Segundo.desativar()
         if not Segundo.acertados():
            Terceiro.ativar()
            Terceiro.focus()

    if Terceiro.completos():
        Terceiro.desativar()
        if not Terceiro.acertados():
            Quarto.ativar()
            Quarto.focus()
    
    if Quarto.completos():
        Quarto.desativar()
        if not Quarto.acertados():
            Quinto.ativar()
            Quinto.focus()

    if Quinto.completos():
        Quinto.desativar()
        if not Quinto.acertados():
            messagebox.showinfo("Errou!",f"Tu errou meu parceiro, a resposta era {''.join(palavra)}")
        

    

janela.bind('<KeyRelease>', digitar)
janela.mainloop()
