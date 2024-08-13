vetor = [3,2,1,4,5,9,6]

for j in range(1,len(vetor)):
    i = j - 1                          
    temp = vetor[j]                    
    while i >= 0 and temp < vetor[i]:
        vetor[i+1] = vetor[i]        
        i = i-1                        
    vetor[i+1] = temp
print(vetor)

# lista encadeada
# não funciona ainda
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

def lista_ordena(lista):
    ant = None
    while lista.prox != None:
        print("info",lista.info)
        print("prox",lista.prox.info)
        if lista.info > lista.prox.info:
            print("teste")
            ant = lista.prox
            lista.info = lista.prox.prox
            lista.prox = lista.info
        
            print(temp)
        ant = lista.info
        lista = lista.prox



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


#qtdNos = list_comprimento(lst)
#lista_ordena(lst)
#print("byx")
#lista_imprime(lst)