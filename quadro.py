
import psycopg2

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


chave = ["nome","telefone","email"]
resultado = ler()


    