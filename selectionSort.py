vetor = [3,6,2,8,4]
vetor2 = [3,7,57,35,24,7,88,5]

def ordena(vetor):
    for j in range(0,len(vetor)):
        menor = vetor[j]
        print("aqui")
        for x in range(j+1,len(vetor)):
            if menor > vetor[x]:
                menor = vetor[x]
                pos = x 
        if menor != vetor[j]:
            temp = vetor[j]
            vetor[j] = vetor[pos]
            vetor[pos] = temp
    return vetor

ordenado = ordena(vetor)
ordenado2 = ordena(vetor2)
print(ordenado)
print(ordenado2)