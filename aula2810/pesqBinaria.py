lista = []

for x in range(1,10000):
    lista.append(x)


## recursiva
def pesquisaBinaria(lista, valor):
    if len(lista) == 0:
        return  print(f"O valor {valor} não está na lista.")
    
    meio = len(lista)//2

    if lista[meio] == valor:
        return print(f"O valor {lista[meio]} está na lista.")
    elif valor < lista[meio]:
        return pesquisaBinaria(lista[:meio], valor)
    else:
        return pesquisaBinaria(lista[meio + 1:], valor)

pesquisaBinaria(lista, 13)





##    iterativa

def pesquisaBinaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == valor:
            return print(f"O valor {valor} está na lista.")
        elif valor < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return print(f"O valor {valor} não está na lista.")

pesquisaBinaria(lista, 55555)
