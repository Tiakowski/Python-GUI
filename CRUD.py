import re
from tkinter import *
from tkinter import messagebox
import psycopg2

#banco de dados

# conn = psycopg2.connect (
#             database = "CRUD",
#             user = "postgres",
#             password = "123",
#             host = "localhost",
#             port = "5432")

# cur = conn.cursor()
# comando = '''create table cadastros xxxxxxxxxxxxxxxxxxx'''

# cur.execute(comando)
# conn.commit()
# conn.close()



dados = {"nome":"","telefone":"","email":""}

def verificar_nome(nome):
    nome = nome.split(' ')
    if len(nome) > 1:
        lnome_erro["text"] = ""
        return True
    else:
        lnome_erro["text"] = "Digite nome e sobrenome."
        
def verificar_telefone(telefone):
    padrao_telefone = re.compile(r'\(?[0-9]{2}?\)?9?[0-9]{4}-?[0-9]{4}')
    if re.fullmatch(padrao_telefone, telefone):
      ltelefone_erro["text"] = ""
      return True
    else:
      ltelefone_erro["text"] = "Telefone inválido"


def verificar_email(email):
    padrao_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    if re.fullmatch(padrao_email, email):
      lemail_erro["text"] = ""
      return True
    else:
      lemail_erro["text"] = "E-mail inválido"




def imprimir():
    if verificar_nome(enome.get()) and verificar_telefone(etelefone.get()) and verificar_email(eemail.get()):
        dados["nome"] = enome.get()
        enome.delete(0,END)
        dados["telefone"] = etelefone.get()
        etelefone.delete(0,END)
        dados["email"] = eemail.get()
        eemail.delete(0,END)
        messagebox.showinfo("Sucesso","Cadastro realizado com sucesso!")
        




janela = Tk()
#janela.configure(bg="#000000")
janela.geometry("280x300")

janela.title("CRUD")

lnome = Label(janela,text="Nome:")
lnome.place(x=3,y=26)
lnome_erro = Label(janela,text="")
lnome_erro.place(x=130,y=50)
enome = Entry(janela)
enome.place(x=3,y=50)

#x = horizontal
#y = vertical


ltelefone = Label(janela,text="Telefone:")
ltelefone.place(x=3,y=80)
ltelefone_erro = Label(janela,text="")
ltelefone_erro.place(x=130,y=104)
etelefone = Entry(janela)
etelefone.place(x=3,y=104)

lemail = Label(janela,text="E-Mail:")
lemail.place(x=3,y=134)
lemail_erro = Label(janela,text="")
lemail_erro.place(x=130,y=158)
eemail = Entry(janela)
eemail.place(x=3,y=158)


botao = Button(janela, command=imprimir , text="Cadastrar", width=20, height=1)
botao.place(x=50,y=200)



janela.mainloop()

print(dados)
