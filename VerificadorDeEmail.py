import win32com.client as win32
import string
import random
import re
from tkinter import *
from tkinter import messagebox


def gerar_codigo():
    codigo = []
    alfabeto = list(string.ascii_uppercase)

    while len(codigo) < 6:
        lon = random.randrange(0,2)
        if lon == 0:
            indice = random.randrange(0,26)
            codigo.append(alfabeto[indice])
        else:
            indice = random.randrange(0,10)
            codigo.append(str(indice))
    return ' '.join(codigo)
   
codigo = gerar_codigo()

def enviar_email():

    padrao_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(padrao_email, eemail.get()):

        outlook = win32.Dispatch('outlook.application')

        email = outlook.CreateItem(0)

        email.To = f"{eemail.get()}"
        email.Subject = "Email Automático"
        email.HTMLBody = f""" 
        <p>Olá, aqui é a revolução dos robôs!. </p>
        <p>Iremos dominar o mundo em 2022.</p>
        <p> </p>
        <p>Álias, seu código de acceso é:<h1> <strong> {codigo} </strong> </h1> </p>
        <p> </p>

        <p>Abs,</p>
        <p>Máquinas.</p>

        """
        anexo = "https://i.gifer.com/3jaE.gif"
        email.Attachments.Add(anexo)

        email.Send()
    else:
        messagebox.showerror("Erro","Digite um email valido")

def verificar():
    if entrycodigo.get().upper().replace(" ","") == codigo.replace(" ",""):
        status.configure(text="Verificado", fg="green")
    else:
        messagebox.showerror("Código inválido","O Código que você digitou está errado.")

janela = Tk()
janela.title("Verificar email")
#janela.resizable(False, False)
instrucao = Label(janela,text="Insira seu email",font=("Helvetica",15,"bold"))
instrucao.grid(column=3,columnspan=6,row=1)

eemail = Entry(janela, width=40,font=("Helvetica", 15))
eemail.grid(column=1,columnspan=10,row=2,padx=30)

enviar = Button(janela,height=2,command=enviar_email,text="Enviar código")
enviar.grid(column=5, row=3, pady= 10)

reenviar = Button(janela,height=2,text="Reenviar código")
reenviar.grid(column=7, row=3, pady= 10)

labelcodigo = Label(janela,text="Digite o código recebido por email:",font=("Helvetica",15))
labelcodigo.grid(column=3,columnspan=6,row=4,pady=5)

entrycodigo = Entry(janela, width=10,font=("Helvetica", 15), justify="center")
entrycodigo.grid(column=1,columnspan=10,row=5,padx=30)

btnverificar = Button(janela,command=verificar,height=2,text="Verificar")
btnverificar.grid(column=6, row=6, pady= 10)

status = Label(janela,text="Não verificado.",fg="#6f0000",font=("Helvetica",15))
status.grid(column=3,columnspan=7,row=7,pady=25,padx=50)




janela.mainloop()