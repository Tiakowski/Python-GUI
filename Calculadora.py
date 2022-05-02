from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title("Calculadora")
janela.configure(bg="#464646")
janela.resizable(False, False)

historico = Text(janela, height = 1, width =45, font=("Helvetica",10))
historico.grid(column=0,columnspan=10, row=0, sticky="e", padx=11,pady=5)
historico.tag_config('justified', justify="right")
historico['state'] = 'disabled'

conta = Text(janela, height = 1,width = 25,font=("Helvetica",20),)
conta.grid(column= 0,columnspan=10,row=1,padx=10,pady=3, sticky="e")
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
    if "." in item:
        item = item.replace(".",",")

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

def numvirgula ():
    if numero_digitado[-1] not in [0-9]:
        numero_digitado.append(".")
        inserir_tela(",")
    

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
            historico['state'] = 'normal'
            historico.delete("end-2c")
            historico['state'] = 'disabled'
            inserir_historico("=")
            print(f'após o POP: {numeros_totais}')

        conta_final = ''.join(numeros_totais)
        
        try:
            conta_final = eval(conta_final)
            conta['state'] = 'normal'
            conta.delete('1.0', END)
            inserir_tela(conta_final)
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
    
    
def backspace():
    global numero_digitado

    if numero_digitado != []:
        try:
        
            conta['state'] = 'normal'
            conta.delete("end-2c")
            conta['state'] = 'disabled'
            numero_digitado.pop()
        except IndexError:
            pass
    
def C():
    global numero_digitado
    global numeros_totais
    deletar_conta()
    historico['state'] = 'normal'
    historico.delete('1.0', END)
    historico['state'] = 'disabled'

    numero_digitado = []
    numeros_totais = []
   
botao7 = Button(text=7,bg="#090909", command=num7, height=2, width=5,fg="#ffffff", font=("Helvetica",12,"bold"))
botao7.grid(column=0,row=2,padx=10,pady=10)

botao8 = Button(text=8,height=2,bg="#090909", command=num8, width=5,fg="#ffffff",font=("Helvetica",12,"bold"))
botao8.grid(column=1,row=2, padx=10,pady=10)

botao9 = Button(text=9,height=2,bg="#090909",command=num9, width=5,fg="#ffffff",font=("Helvetica",12,"bold"))
botao9.grid(column=2,row=2,padx=10,pady=10)

botao4 = Button(text=4,height=2,bg="#090909",command=num4,width=5,fg="#ffffff",font=("Helvetica",12,"bold"))
botao4.grid(column=0,row=3,padx=10,pady=10)

botao5 = Button(text=5,height=2,bg="#090909",command=num5,fg="#ffffff", width=5,font=("Helvetica",12,"bold"))
botao5.grid(column=1,row=3,padx=10,pady=10)

botao6 = Button(text=6,height=2,bg="#090909",command=num6,fg="#ffffff", width=5,font=("Helvetica",12,"bold"))
botao6.grid(column=2,row=3,padx=10,pady=10)

botao1 = Button(text=1,height=2,bg="#090909",command=num1,fg="#ffffff",width=5,font=("Helvetica",12,"bold"))
botao1.grid(column=0,row=4,padx=10,pady=10)

botao2 = Button(text=2,height=2,bg="#090909", command=num2,fg="#ffffff",width=5,font=("Helvetica",12,"bold"))
botao2.grid(column=1,row=4,padx=10,pady=10)

botao3 = Button(text=3,height=2,bg="#090909",command=num3,fg="#ffffff", width=5,font= ("Helvetica",12,"bold"))
botao3.grid(column=2,row=4,padx=10,pady=10)

botaovir = Button(text=",",bg="#090909",fg="#ffffff",command=numvirgula,height=2, width=5,font=("Helvetica",12,"bold"))
botaovir.grid(column=1,row=5,padx=10,pady=10)

botao0 = Button(text=0,height=2,bg="#090909",command=num0,fg="#ffffff", width=5,font=("Helvetica",12,"bold"))
botao0.grid(column=0,row=5,padx=10,pady=10)

botaodiv = Button(text="÷",bg="#333333",fg="#d7d7d7",command=divisao,height=2, width=5,font=("Helvetica",12,"bold"))
botaodiv.grid(column=4,row=3,padx=10,pady=10)

botaoigual = Button(text="=",bg="#15456b",fg="#d7d7d7",height=2,command=igual, width=13,font=("Helvetica",12,"bold"))
botaoigual.grid(column=2,columnspan=2,row=5,padx=10,pady=10)

botaomult = Button(text="X",bg="#333333",fg="#d7d7d7",height=2,command=multi, width=5,font=("Helvetica",12,"bold"))
botaomult.grid(column=3,row=3,padx=10,pady=10)

botaosub = Button(text="-",bg="#333333",fg="#d7d7d7",height=2,command=sub, width=5,font=("Helvetica",12,"bold"))
botaosub.grid(column=3,row=4,padx=10,pady=10)

botaosom = Button(text="+",bg="#333333",fg="#d7d7d7",command=soma,height=2, width=5,font=("Helvetica",12,"bold"))
botaosom.grid(column=4,row=4,padx=10,pady=10)

botaopor = Button(text="%",bg="#333333",fg="#d7d7d7",height=2, width=5,font=("Helvetica",12,"bold"))
botaopor.grid(column=4,row=5,padx=10,pady=10)

botaobackspace = Button(text="<--",bg="#333333",fg="#d7d7d7", command=backspace, height=2, width=5,font=("Helvetica",12,"bold"))
botaobackspace.grid(column=4,row=2,padx=10,pady=10)

botaolimpar = Button(text="C",bg="#333333",fg="#d7d7d7",command=C, height=2, width=5,font=("Helvetica",12,"bold"))
botaolimpar.grid(column=3,row=2,padx=10,pady=10)

# TECLADO #

def numerodigitado(event):
    numero = repr(event.char)
    if numero == "'1'":
        num1()
    elif numero == "'2'":
        num2()
    elif numero == "'3'":
        num3()
    elif numero == "'4'":
        num4()
    elif numero == "'5'":
        num5()
    elif numero == "'6'":
        num6()
    elif numero == "'7'":
        num7()
    elif numero == "'8'":
        num8()
    elif numero == "'9'":
        num9()
    elif numero == "'0'":
        num0()
    elif numero == "'/'":
        divisao()
    elif numero == "'*'":
        multi()
    elif numero == "'-'":
        sub()
    elif numero == "'+'":
        soma()
    elif numero == "'\\r'":
        igual()
    elif numero == "'\\x08'":
        backspace()
    elif numero == "','":
        numvirgula()

janela.bind(sequence="<Key>", func=numerodigitado)

janela.mainloop()