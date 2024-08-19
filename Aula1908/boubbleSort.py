vetor = [3,1,2,5]
vetor1 = [1,4,6,7,9]
vetor2 = [8,7,5,3,2]
vetor3 = [3,4,6,2,2,6,4]

def bouble(vetor):
    for m in range(0,len(vetor)):
        jaOrdenou = False
        for c in range(0,len(vetor)-1):
            if vetor[c] > vetor[c+1]:
                aux = vetor[c]
                vetor[c] = vetor[c+1] 
                vetor[c+1] = aux
                jaOrdenou = True
    if jaOrdenou == False:
        return vetor

a = bouble(vetor)
print("Vetor Aleatorio", a)

b = bouble(vetor1)
print("Vetor Ja ordendo", b)

c = bouble(vetor2)
print("Vetor Inverso", c)

d = bouble(vetor3)
print("Vetor duplicado", d)
