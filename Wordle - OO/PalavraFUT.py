def palavra_aleatoria():
    import random
    palavras = open("times.txt", "r")
    aleatorio = random.randrange(1,quantidade_de_palavras())
    contador = 1
    for linha in palavras:
        if aleatorio == contador:
            palavra_escolhida = linha
            palavra_escolhida = list(palavra_escolhida.upper().strip())
            return palavra_escolhida
        else:
            contador += 1
    palavras.close()

def quantidade_de_palavras():
    palavras = open("times.txt")
    lista = list(palavras)
    tamanho = len(lista)
    return tamanho

palavra = palavra_aleatoria()