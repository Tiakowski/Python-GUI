from glob import glob
from tkinter import *

janela = Tk()
janela.title("Calculadora")
janela.resizable(False, False)

historico = Text(janela, height = 1, width =25, font=("Helvetica",10))
historico.grid(column=0,columnspan=10, row=0, sticky="e", padx=11)
historico.tag_config('justified', justify="right")
historico['state'] = 'disabled'

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

def inserir_historico(item):
    historico['state'] = 'normal'
    historico.insert(END,item,"justified")
    historico['state'] = 'disabled'

def limpar_historico():
    global numero_digitado
    global numeros_totais

    historico['state'] = 'normal'
    if numero_digitado == [] and numeros_totais == []:
        historico.delete('1.0', END)
    historico['state'] = 'disabled'

def limpar_tela():
    global numero_digitado
    global numeros_totais

    if numero_digitado == [] and numeros_totais == []:
        deletar_conta()
    
    if numero_digitado == []:
        deletar_conta()


def deletar_conta():
    conta['state'] = 'normal'
    conta.delete('1.0', END)
    conta['state'] = 'disabled'

def num1 ():
    limpar_historico()
    limpar_tela()
    digitar("1") 

def num2 ():
    limpar_historico()
    limpar_tela()
    digitar("2")

def num3 ():
    limpar_historico()
    limpar_tela()
    digitar("3")
    
def num4 ():
    limpar_historico()
    limpar_tela()
    digitar("4")
  
def num5 ():
    limpar_historico()
    limpar_tela()
    digitar("5")

def num6 ():
    limpar_historico()
    limpar_tela()
    digitar("6")

def num7 ():
    limpar_historico()
    limpar_tela()
    digitar("7")

def num8 ():
    limpar_historico()
    limpar_tela()
    digitar("8")

def num9 ():
    limpar_historico()
    limpar_tela()
    digitar("9")

def num0 ():
    limpar_historico()
    limpar_tela()
    digitar("0")

def limpar():
    global numero_digitado
    global numeros_totais

    deletar_conta()
    historico['state'] = 'normal'
    historico.delete('1.0', END)
    historico['state'] = 'disabled'
    numero_digitado = []
    numeros_totais = []

def soma():
    global numero_digitado
    global numeros_totais

    if  len(numero_digitado) > 0 and numero_digitado[-1] not in simbolos_matematicos :
        numero_formatado = ''.join(numero_digitado)
        numeros_totais.append(numero_formatado)
        numeros_totais.append("+")
        inserir_historico(numero_formatado)
        inserir_historico("+")
        numero_digitado = []

def multi():
    global numero_digitado
    global numeros_totais

    if  len(numero_digitado) > 0 and numero_digitado[-1] not in simbolos_matematicos :
        numero_formatado = ''.join(numero_digitado)
        numeros_totais.append(numero_formatado)
        numeros_totais.append("*")
        inserir_historico(numero_formatado)
        inserir_historico("×")
        numero_digitado = []

def divisao():
    global numero_digitado
    global numeros_totais

    if  len(numero_digitado) > 0 and numero_digitado[-1] not in simbolos_matematicos :
        numero_formatado = ''.join(numero_digitado)
        numeros_totais.append(numero_formatado)
        numeros_totais.append("/")
        inserir_historico(numero_formatado)
        inserir_historico("÷")
        numero_digitado = []

def sub():
    global numero_digitado
    global numeros_totais

    if  len(numero_digitado) > 0 and numero_digitado[-1] not in simbolos_matematicos :
        numero_formatado = ''.join(numero_digitado)
        numeros_totais.append(numero_formatado)
        numeros_totais.append("-")
        inserir_historico(numero_formatado)
        inserir_historico("-")
        numero_digitado = []

def igual():
    global numero_digitado
    global numeros_totais

    try:
        if numero_digitado != []:
            numero_formatado = ''.join(numero_digitado)
            numeros_totais.append(numero_formatado)
            inserir_historico(numero_formatado)
            inserir_historico("=")

        if numeros_totais[-1] in simbolos_matematicos:
            numeros_totais.pop()
            print(f'após o POP: {numeros_totais}')
        

        conta_final = ''.join(numeros_totais)
        
        try:
            conta['state'] = 'normal'
            conta.delete('1.0', END)
            inserir_tela(eval(conta_final))
            conta['state'] = 'disabled'

            numero_digitado = []
            numeros_totais = []
        except ZeroDivisionError:
            limpar()
            conta['state'] = 'normal'
            inserir_tela("Resultado indefinido")
            conta['state'] = 'disabled'

            pass


    except IndexError:
        pass
    
    

    
    

def teste():
    pass
    


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

botaovir = Button(text=",",command=limpar,height=2, width=5,font=("Helvetica",12,"bold"))
botaovir.grid(column=1,row=5,padx=10,pady=10)

botao0 = Button(text=0,height=2,command=num0, width=5,font=("Helvetica",12,"bold"))
botao0.grid(column=0,row=5,padx=10,pady=10)

botaodiv = Button(text="÷",command=divisao,height=2, width=5,font=("Helvetica",12,"bold"))
botaodiv.grid(column=3,row=2,padx=10,pady=10)

botaoigual = Button(text="=",height=2,command=igual, width=5,font=("Helvetica",12,"bold"))
botaoigual.grid(column=2,row=5,padx=10,pady=10)

botaomult = Button(text="X",height=2,command=multi, width=5,font=("Helvetica",12,"bold"))
botaomult.grid(column=3,row=3,padx=10,pady=10)

botaosub = Button(text="-",height=2,command=sub, width=5,font=("Helvetica",12,"bold"))
botaosub.grid(column=3,row=4,padx=10,pady=10)

botaosom = Button(text="+",command=soma,height=2, width=5,font=("Helvetica",12,"bold"))
botaosom.grid(column=3,row=5,padx=10,pady=10)






janela.mainloop()