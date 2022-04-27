import re
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import sqlite3

#banco de dados #####################

conn = sqlite3.connect('cadastros.db')
cur = conn.cursor()

try:
    criar_tabela = ('''CREATE TABLE cadastros (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome varchar (50) NOT NULL,
                    telefone varchar(16) NOT NULL,
                    email varchar(250) NOT NULL)''' )
    cur.execute(criar_tabela)
    conn.commit()
    cur.close()
except sqlite3.OperationalError:
    pass


def inserir():
  cur = conn.cursor()
  comando = f'''INSERT INTO cadastros (nome, telefone, email) VALUES ("{dados["nome"].title()}", "{dados["telefone"]}", "{dados["email"]}") ''' 
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

def excluir(id_selecionado):
  cur = conn.cursor()
  comando = f'''delete from cadastros where id="{id_selecionado}" ''' 
  cur.execute(comando)
  conn.commit()
  cur.close()

def pesquisar():
  resultado = ""
  cur = conn.cursor()

  if item_combobox.get() == "Nome":
    comando = f'''select * from cadastros where nome like "%{epesquisa.get().title()}%" ''' 
    cur.execute(comando)
    resultado = cur.fetchall()
  if item_combobox.get() == "Telefone":
    comando = f'''select * from cadastros where telefone like "%{epesquisa.get()}%" ''' 
    cur.execute(comando)
    resultado = cur.fetchall()
  if item_combobox.get() == "Email":
    comando = f'''select * from cadastros where email like "%{epesquisa.get()}%" ''' 
    cur.execute(comando)
    resultado = cur.fetchall()

    cur.close()
  return resultado

def editar():
  try:
    dados = editar_tabela()
    cur = conn.cursor()
    if enome.get() != "":
      if verificar_nome(enome.get()):
        comando = f'''UPDATE cadastros SET nome = "{enome.get()}" WHERE id = "{dados[0]}" ''' 
        cur.execute(comando)
      else:
        lerro["text"] = "Digite nome e sobrenome."

    if etelefone.get() != "":
      if verificar_telefone(etelefone.get):
        comando = f'''UPDATE cadastros SET telefone = "{etelefone.get()}" WHERE id = "{dados[0]}" ''' 
        cur.execute(comando)
      else:
        lerro["text"] = "Telefone inválido"

    if eemail.get() != "":
      if verificar_email(eemail.get()):
        comando = f'''UPDATE cadastros SET email = "{eemail.get()}" WHERE id = "{dados[0]}" ''' 
        cur.execute(comando)
      else:
        lerro["text"] = "Email Inválido."

    conn.commit()
    cur.close()
  except IndexError:
    messagebox.showerror("Erro","Selecione um item para editar")


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
        atualizar()
        messagebox.showinfo("Sucesso","Cadastro realizado com sucesso!")
  


janela = Tk()
#janela.configure(bg="#000000")
janela.geometry("1000x300")
janela.title("CRUD")

lnome = Label(janela,text="Nome:")
lnome.place(x=3,y=26)
enome = Entry(janela)
enome.place(x=3,y=50)

ltelefone = Label(janela,text="Telefone:")
ltelefone.place(x=3,y=80)
etelefone = Entry(janela)
etelefone.place(x=3,y=104)

lemail = Label(janela,text="E-Mail:")
lemail.place(x=3,y=134)
eemail = Entry(janela)
eemail.place(x=3,y=158)

lpesquisa = Label(janela,text="Pesquisa:")
lpesquisa.place(x=3,y=210)
epesquisa = Entry(janela)
epesquisa.place(x=3,y=234)

lerro = Label(janela,text="")
lerro.place(x=130,y=255)

colunas = ("ID","Nome","Telefone","Email")
leitura = Treeview(janela, columns=colunas, show="headings",height=5,)
leitura.heading("ID",text="ID")
leitura.heading('Nome',text="Nome")
leitura.heading("Telefone",text="Telefone")
leitura.heading("Email", text="Email")
leitura.place(x=150,y=50)

def deletar_tudo():
    for item in leitura.get_children():
      leitura.delete(item)

def pesquisar_termo():
  cadastros = pesquisar()
  deletar_tudo()
  for conta in cadastros:
    leitura.insert('',END, values=conta)



def atualizar():
  cadastros = ler()
  deletar_tudo()
  for conta in cadastros:
    leitura.insert('',END, values=conta)


atualizar()

#Selecionar ID do item selecionado na TreeView


def deletar_tabela():
  try:
    ItemSelecionado = leitura.focus()
    temp = leitura.item(ItemSelecionado,'values')
    leitura.delete(ItemSelecionado)
    excluir(temp[0])
  except TclError:
    messagebox.showerror("Erro","Selecione um item para deletar")
  

def editar_tabela():
  ItemSelecionado = leitura.focus()
  temp = leitura.item(ItemSelecionado,'values')
  return temp  

#COMBO BOX
item_combobox = StringVar()
box = Combobox(janela, textvariable=item_combobox)
box['values'] = ('Nome', 
                 'Telefone',
                  'Email')
box.place(x=130,y=234)
box.set("Nome")
box['state'] = 'readonly'




botao_cadastro = Button(janela, command=imprimir , text="Cadastrar", width=52, height=2)
botao_cadastro.place(x=350,y=250)

botao_editar = Button(janela,width=25,text="Editar",command=editar, height=1)
botao_editar.place(x=540,y=220)

botao_deletar = Button(janela,width=24,command=deletar_tabela,text="Deletar", height=1)
botao_deletar.place(x=350,y=220)

botao_pesquisar = Button(janela,text="Pesquisar",command=pesquisar_termo)
botao_pesquisar.place(x=35,y=259)

janela.mainloop()


