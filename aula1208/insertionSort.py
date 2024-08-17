vetor = [3,2,1,4,5,9,6]
vetor2 = [1,4,6,7,8]
vetor3 = [8,6,4,3,2,1]
vetor4 = [4,5,5,2,5,3,3,7]
def insertion(vetor):
    for j in range(1,len(vetor)):
        i = j - 1                          
        temp = vetor[j]                    
        while i >= 0 and temp < vetor[i]:
            vetor[i+1] = vetor[i]        
            i = i-1                        
        vetor[i+1] = temp
    print(vetor)

print("Vetor aleatorio")
insertion(vetor)
print("Vetor ja ordenado")
insertion(vetor2)
print("Vetor inverso")
insertion(vetor3)
print("Vetor duplicado")
insertion(vetor4)

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

def lista_ordena(lista, qtdNos):
    for i in range(qtdNos - 1):
        atual = lista
        while atual.prox is not None:
            if atual.info > atual.prox.info:
                atual.info, atual.prox.info = atual.prox.info, atual.info
            atual = atual.prox

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
lista_ordena(lst, qtdNos)
lista_imprime(lst)

print("Lista ordenada")
qtdNos = list_comprimento(lst2)
lista_ordena(lst2, qtdNos)
lista_imprime(lst2)

print("Lista inversa")
qtdNos = list_comprimento(lst3)
lista_ordena(lst3, qtdNos)
lista_imprime(lst3)

print("Lista duplicada")
qtdNos = list_comprimento(lst4)
lista_ordena(lst4, qtdNos)
lista_imprime(lst4)