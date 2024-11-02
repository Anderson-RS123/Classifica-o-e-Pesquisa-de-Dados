lista = []

for x in range(1,10001):
    lista.append(x)


def jump(lista, valor):
    size = len(lista)
    pular = 8
    while pular > 0:
        for x in range(0, size):
            if size > (pular + x):
                if lista[x] == valor:
                    return print(f"O valor {valor} está na lista.")
        pular = pular // 2 
    passouTodos = False
    while passouTodos == False:
        passouTodos = True
        for x in range(0, size):
            if lista[x] == valor:
                return print(f"O valor {valor} está na lista.")
    return print(f"O valor {valor} não está na lista.")

jump(lista, 10000)