vetor = [3,6,2,8,4,7,4]
vetor2 = [1,3,5,6,7,8,9]
vetor3 = [9,7,6,4,2,1]
vetor4 = [3,5,2,5,3,3,3,4,5]
def ordena(vetor):
    for j in range(0,len(vetor)):
        menor = vetor[j]
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
ordenado3 = ordena(vetor3)
ordenado4 = ordena(vetor4)
print("Vetor aleatorio",ordenado)
print("Vetor ordenado",ordenado2)
print("Vetor inverso",ordenado3)
print("Vetor duplicado",ordenado4)

print("Lista encadeada")
# lista encadeada
class Lista:
    def __init__(self, valor=None):
        self.info = valor
        self.prox = None

def cria_lista():   
    return None

def insere_lista(lista, valor):
    novo = Lista(valor)
    novo.prox = lista
    return novo

def lista_imprime(lst):
    atual = lst
    while atual is not None:
        print(atual.info)
        atual = atual.prox


def listaOrdena(lista, qtdNos):
    for i in range(0, qtdNos - 1):
        menor = lista.info
        menorValor = lista
        proxValor = lista.prox
        while proxValor is not None:
            if proxValor.info < menor:
                menor = proxValor.info
                menorValor = proxValor
            proxValor = proxValor.prox
        if menorValor != lista:
            lista.info, menorValor.info = menorValor.info, lista.info
        lista = lista.prox
    return lista

def list_comprimento(lst):
    atual = lst
    contador = 0
    while atual is not None:
        contador = contador + 1
        atual = atual.prox
    return contador



lst = insere_lista(None, 5)
lst = insere_lista(lst, 6)
lst = insere_lista(lst, 7)
lst = insere_lista(lst, 3)
lst = insere_lista(lst, 4)
lst = insere_lista(lst, 2)

lst2 = insere_lista(None, 1)
lst2 = insere_lista(lst2, 2)
lst2 = insere_lista(lst2, 3)
lst2 = insere_lista(lst2, 4)
lst2 = insere_lista(lst2, 5)
lst2 = insere_lista(lst2, 6)

lst3 = insere_lista(None, 7)
lst3 = insere_lista(lst3, 6)
lst3 = insere_lista(lst3, 5)
lst3 = insere_lista(lst3, 3)
lst3 = insere_lista(lst3, 2)
lst3 = insere_lista(lst3, 1)

lst4 = insere_lista(None, 5)
lst4 = insere_lista(lst4, 5)
lst4 = insere_lista(lst4, 7)
lst4 = insere_lista(lst4, 3)
lst4 = insere_lista(lst4, 3)
lst4 = insere_lista(lst4, 2)

print("Lista aleatoria")
qtdNos = list_comprimento(lst)
listaOrdena(lst, qtdNos)
lista_imprime(lst)

print("Lista ordenada")
qtdNos = list_comprimento(lst2)
listaOrdena(lst2, qtdNos)
lista_imprime(lst2)

print("Lista inversa")
qtdNos = list_comprimento(lst3)
listaOrdena(lst3, qtdNos)
lista_imprime(lst3)

print("Lista duplicada")
qtdNos = list_comprimento(lst4)
listaOrdena(lst4, qtdNos)
lista_imprime(lst4)