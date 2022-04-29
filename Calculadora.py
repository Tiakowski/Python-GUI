from tkinter import *

janela = Tk()
janela.title("Calculadora")
janela.resizable(False, False)

historico = Text(janela, height = 1, width =25, font=("Helvetica",10))
historico.grid(column=0,columnspan=10, row=0, sticky="e", padx=11)
historico.tag_config('justified', justify="right")

conta = Text(janela, height = 1,width = 20,font=("Helvetica",20),)
conta.grid(column= 0,columnspan=10,row=1,padx=10,pady=3)
conta.tag_config('justified', justify="right")
conta['state'] = 'disabled'

numeros_totais = []
numero_digitado = []
simbolos_matematicos = ["+","-","/","*"]

def digitar(numero):
    global numero_digitado
    numero_digitado.append(numero)
    print(numero_digitado)

    inserir_tela(numero)
    

def inserir_tela(item):
    conta['state'] = 'normal'
    conta.insert(END,item,"justified")
    conta['state'] = 'disabled'



def num1 ():
    digitar("1")

def num2 ():
    digitar("2")

def num3 ():
    digitar("3")
    
def num4 ():
    digitar("4")

def num5 ():
    digitar("5")

def num6 ():
    digitar("6")

def num7 ():
    digitar("7")

def num8 ():
    digitar("8")

def num9 ():
    digitar("9")

def num0 ():
    digitar("0")

def soma():
    global numero_digitado
    global numeros_totais


    if  len(numero_digitado) > 0 and numero_digitado[-1] not in simbolos_matematicos :
        inserir_tela("+")
        numero_formatado = ''.join(numero_digitado)
        numeros_totais.append(numero_formatado)
        numeros_totais.append("+")
        numero_digitado = []


def teste():
    print(numero_digitado)
    print(numeros_totais)


botao7 = Button(text=7, command=num7, height=2, width=5,font=("Helvetica",12,"bold"))
botao7.grid(column=0,row=2,padx=10,pady=10)

botao8 = Button(text=8,height=2, command=num8, width=5,font=("Helvetica",12,"bold"))
botao8.grid(column=1,row=2, padx=10,pady=10)

botao9 = Button(text=9,height=2,command=num9, width=5,font=("Helvetica",12,"bold"))
botao9.grid(column=2,row=2,padx=10,pady=10)

botao4 = Button(text=4,height=2,command=num4,width=5,font=("Helvetica",12,"bold"))
botao4.grid(column=0,row=3,padx=10,pady=10)

botao5 = Button(text=5,height=2,command=num5, width=5,font=("Helvetica",12,"bold"))
botao5.grid(column=1,row=3,padx=10,pady=10)

botao6 = Button(text=6,height=2,command=num6, width=5,font=("Helvetica",12,"bold"))
botao6.grid(column=2,row=3,padx=10,pady=10)

botao1 = Button(text=1,height=2,command=num1, width=5,font=("Helvetica",12,"bold"))
botao1.grid(column=0,row=4,padx=10,pady=10)

botao2 = Button(text=2,height=2, command=num2,width=5,font=("Helvetica",12,"bold"))
botao2.grid(column=1,row=4,padx=10,pady=10)

botao3 = Button(text=3,height=2,command=num3, width=5,font= ("Helvetica",12,"bold"))
botao3.grid(column=2,row=4,padx=10,pady=10)

botaovir = Button(text=",",command=teste,height=2, width=5,font=("Helvetica",12,"bold"))
botaovir.grid(column=1,row=5,padx=10,pady=10)

botao0 = Button(text=0,height=2,command=num0, width=5,font=("Helvetica",12,"bold"))
botao0.grid(column=0,row=5,padx=10,pady=10)

botaodiv = Button(text="÷",height=2, width=5,font=("Helvetica",12,"bold"))
botaodiv.grid(column=3,row=2,padx=10,pady=10)

botaoigual = Button(text="=",height=2, width=5,font=("Helvetica",12,"bold"))
botaoigual.grid(column=2,row=5,padx=10,pady=10)

botaomult = Button(text="X",height=2, width=5,font=("Helvetica",12,"bold"))
botaomult.grid(column=3,row=3,padx=10,pady=10)

botaosub = Button(text="-",height=2, width=5,font=("Helvetica",12,"bold"))
botaosub.grid(column=3,row=4,padx=10,pady=10)

botaosom = Button(text="+",command=soma,height=2, width=5,font=("Helvetica",12,"bold"))
botaosom.grid(column=3,row=5,padx=10,pady=10)






janela.mainloop()