from tkinter import *
import collections
from Palavra import palavra_aleatoria

janela = Tk()
janela.title("Wordle")

palavra = palavra_aleatoria()



def caps(event):
    numero = repr(event.keycode)
    print(type((event.keycode)))
    foco = janela.focus_get()
    print(numero)
    naopode = [13,8,37]
    
    #Códigos keycode:
    #13 = Enter / 8 = Delete / 39 = Seta pra direita / 37 = Seta pra esquerda

    #Enter
    if int(numero) == 13:
        verificar()

    #Inserir a letra maiuscula e foco no próximo entry
    if int(numero) not in naopode:
        if foco == letra1:
            if int(numero) != 39:
                a.set(chr(int(numero)))
            letra2.focus_set()

        elif foco == letra2:
            if int(numero) != 39:
                b.set(chr(int(numero)))
            letra3.focus_set()

        elif foco == letra3:
            if int(numero) != 39:
                c.set(chr(int(numero)))
            letra4.focus_set()

        elif foco == letra4:
            if int(numero) != 39:
                d.set(chr(int(numero)))
            letra5.focus_set()

        elif foco == letra5:
            if int(numero) != 39:
                e.set(chr(int(numero)))

    #Delete e entry anterior
    elif int(numero) == 8 or int(numero) == 37:
        if foco == letra1:
            if int(numero) == 8:
                letra1.delete(0,'end')

        elif foco == letra2:
            if int(numero) == 8:
                letra2.delete(0,'end')
            letra1.focus_set()

        elif foco == letra3:
            if int(numero) == 8:
                letra3.delete(0,'end')
            letra2.focus_set()

        elif foco == letra4:
            if int(numero) == 8:
                letra4.delete(0,'end')
            letra3.focus_set()

        elif foco == letra5:
            if int(numero) == 8:
                letra5.delete(0,'end')
            letra4.focus_set()
        


def verificar():
    global palavra
    palavra_contada =dict(collections.Counter(palavra))
    contador_branco = 0
    a = letra1.get()
    b = letra2.get()
    c = letra3.get()
    d = letra4.get()
    e = letra5.get()

    if a != "" and b != "" and c != "" and d != "" and e != "":
        chute = [a,b,c,d,e]
        entradas = [letra1,letra2,letra3,letra4,letra5]
        print(chute)

        for letra in chute:
            if letra in palavra_contada:
                for i in palavra_contada:
                    if letra == i:
                        if palavra_contada[letra] != 0:
                            if letra == palavra[contador_branco]:
                                quantidade = palavra_contada[letra]
                                palavra_contada={**palavra_contada, letra:quantidade-1}
                                entradas[contador_branco].config({"background": "Green"})
            contador_branco += 1                    

        print(f"Contador: {palavra_contada}")

        contador_branco = 0 
        for letra in chute:
            if letra in palavra:
                for i in palavra_contada:
                    if letra == i:
                        if palavra_contada[letra] != 0:
                            quantidade = palavra_contada[letra]
                            palavra_contada={**palavra_contada, letra:quantidade-1}
                            entradas[contador_branco].config({"background": "Orange"})
                    
            contador_branco += 1 


             

botao = Button(janela,text="Verificar",width=20,font=("Helvetica",12,"bold"),command=verificar)
botao.grid(column=1,columnspan=3,row=10) 

a = StringVar()
letra1 = Entry(janela, width=3,font=("Helvetica", 32), justify="center",textvariable=a)
letra1.grid(column=0,row=0)
letra1.bind('<KeyRelease>',caps)

b = StringVar()
letra2 = Entry(janela, width=3,font=("Helvetica", 32), justify="center",textvariable=b)
letra2.grid(column=1,row=0)
letra2.bind('<KeyRelease>', caps)

c = StringVar()
letra3 = Entry(janela, width=3,font=("Helvetica", 32), justify="center",textvariable=c)
letra3.grid(column=2,row=0)
letra3.bind('<KeyRelease>', caps)

d = StringVar()
letra4 = Entry(janela, width=3,font=("Helvetica", 32), justify="center",textvariable=d)
letra4.grid(column=3,row=0)
letra4.bind('<KeyRelease>', caps)

e = StringVar()
letra5 = Entry(janela, width=3,font=("Helvetica", 32), justify="center",textvariable=e)
letra5.grid(column=4,row=0)
letra5.bind('<KeyRelease>', caps)

letra1.focus_set()

janela.mainloop()
