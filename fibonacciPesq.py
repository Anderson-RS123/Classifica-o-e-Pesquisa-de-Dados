lista = []

for x in range(1, 10000):
    lista.append(x)



def fibonacci(lista, valorEncontrar):
    valor2 = 0
    valor3 = 1

    while valor3 < len(lista):
        valor2 = valor3
        valor3 = valor2 + valor3

    while valor3 >= 1:
        menor = min(len(lista) - 1, valor3)

        if lista[valor2] == valorEncontrar:
            return print(f"O valor {valorEncontrar} está na lista.")
        
        elif lista[valor2] < valorEncontrar:
            for x in range(valor2 + 1, menor + 1):
                if lista[x] == valorEncontrar:
                    return print(f"O valor {valorEncontrar} está na lista.")
            valor3 = valor3 - valor2
            valor2 = valor2
        else:
            valor3 = valor2
            valor2 = valor3 - valor2

    return print(f"O valor {valorEncontrar} não está na lista.")

fibonacci(lista, 613)
