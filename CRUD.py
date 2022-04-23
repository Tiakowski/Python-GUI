import re
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import psycopg2

#banco de dados #####################
conn = psycopg2.connect (
            database = "CRUD",
            user = "postgres",
            password = "123",
            host = "localhost",
            port = "5432")

def inserir():
  cur = conn.cursor()
  comando = f'''INSERT INTO cadastros (nome, telefone, email) VALUES ('{dados["nome"]}', '{dados["telefone"]}', '{dados["email"]}') ''' 
  cur.execute(comando)
  conn.commit()
  cur.close()

def ler():
  cur = conn.cursor()
  comando = f'''SELECT * FROM cadastros''' 
  cur.execute(comando)
  resultado = cur.fetchall()
  cur.close()
  return resultado


####################################



dados = {"nome":"","telefone":"","email":""}

def verificar_nome(nome):
    nome = nome.split(' ')
    if len(nome) > 1:
        lerro["text"] = ""
        return True
    else:
        lerro["text"] = "Digite nome e sobrenome."
        
def verificar_telefone(telefone):
    padrao_telefone = re.compile(r'\(?[0-9]{2}?\)?9?[0-9]{4}-?[0-9]{4}')
    if re.fullmatch(padrao_telefone, telefone):
      lerro["text"] = ""
      return True
    else:
      lerro["text"] = "Telefone inválido"


def verificar_email(email):
    padrao_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    if re.fullmatch(padrao_email, email):
      lerro["text"] = ""
      return True
    else:
      lerro["text"] = "E-mail inválido"




def imprimir():
    if verificar_nome(enome.get()) and verificar_telefone(etelefone.get()) and verificar_email(eemail.get()):
        dados["nome"] = enome.get()
        enome.delete(0,END)
        dados["telefone"] = etelefone.get()
        etelefone.delete(0,END)
        dados["email"] = eemail.get()
        eemail.delete(0,END)
        inserir()
        messagebox.showinfo("Sucesso","Cadastro realizado com sucesso!")

def closeconn():
  conn.close      




janela = Tk()
#janela.configure(bg="#000000")
janela.geometry("1000x300")

janela.title("CRUD")

lnome = Label(janela,text="Nome:")
lnome.place(x=3,y=26)
enome = Entry(janela)
enome.place(x=3,y=50)

#x = horizontal
#y = vertical


ltelefone = Label(janela,text="Telefone:")
ltelefone.place(x=3,y=80)
etelefone = Entry(janela)
etelefone.place(x=3,y=104)

lemail = Label(janela,text="E-Mail:")
lemail.place(x=3,y=134)
eemail = Entry(janela)
eemail.place(x=3,y=158)

lerro = Label(janela,text="")
lerro.place(x=70,y=270)


botao_cadastro = Button(janela, command=imprimir , text="Cadastrar", width=15, height=1)
botao_cadastro.place(x=10,y=200)



botao_editar = Button(janela,width=15,text="Editar", height=1)
botao_editar.place(x=130,y=230)

botao_deletar = Button(janela,width=15,command=closeconn,text="Deletar", height=1)
botao_deletar.place(x=130,y=200)

def atualizar_tabela():
  colunas = ("ID","Nome","Telefone","Email")
  leitura = Treeview(janela, columns=colunas, show="headings",height=5,)
  leitura.heading("ID",text="ID")
  leitura.heading('Nome',text="Nome")
  leitura.heading("Telefone",text="Telefone")
  leitura.heading("Email", text="Email")

  leitura.place(x=150,y=50)

  contatos = ler()
  
  for contato in contatos:
    leitura.insert('',END, values=contato)

atualizar_tabela()

botao_ler = Button(janela, text="Atualizar", command=atualizar_tabela, width=15, height=1)
botao_ler.place(x=10,y=230)

janela.mainloop()


