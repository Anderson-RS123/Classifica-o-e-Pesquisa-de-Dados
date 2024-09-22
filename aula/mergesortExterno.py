# nome do arquivo criado para ser ordenado
lista = 'C:/Users/Usuario/Desktop/AMF 24.2/classPesqDados2/aulaa0909/teste.txt'
nomeArqCriados = []

def mergeSortExterno(arqOriginal):
    memoria = 10  # quantidade de elementos suportada na memória
    criaArquivos(arqOriginal, memoria)  # criar os arquivos

    for x in nomeArqCriados:  # ordena os valores dos arquivos
        ordenaValores(x)

    arquivoFinal(nomeArqCriados)   # ordena os valores em um arquivo apenas

def criaArquivos(arqOriginal, memoria):
    with open(arqOriginal, 'r') as file:
        linhas = file.readlines()
        numeroLinhas = len(linhas)  # número total de linhas

    cont = 1
    aux = numeroLinhas
    while aux > 0:  # criar os arquivos
        lerAteALinha = cont * memoria
        inicioLeitura = (cont - 1) * memoria

        with open(f'arquivo{cont}.txt', 'w') as arquivoNovo:  # cria o arquivo para inserir os dados
            if lerAteALinha <= numeroLinhas:
                for i in range(inicioLeitura, lerAteALinha):  # insere os dados
                    arquivoNovo.write(linhas[i])
            else:
                for i in range(inicioLeitura, numeroLinhas):  # insere as linhas restantes
                    arquivoNovo.write(linhas[i])
            nomeArqCriados.append(f'arquivo{cont}.txt')
        cont += 1
        aux -= memoria  # Atualiza o número de linhas restantes

def ordenaValores(arquivo):
    vetorTemp = []  # Cria um vetor local para armazenar os valores

    # Passa os valores do arquivo para o vetor
    with open(arquivo, 'r') as file:
        vetorTemp = file.readlines()  # Lê todas as linhas para o vetor

    # Converte os valores para inteiros antes de ordenar
    vetorTemp = [int(linha.strip()) for linha in vetorTemp]

    quickSort(vetorTemp, 0, len(vetorTemp) - 1)  # Ordena o vetor

    # Converte os inteiros de volta para strings para escrever no arquivo
    with open(arquivo, 'w') as arqOrdenado:  # Passa os valores do vetor para o arquivo
        for numero in vetorTemp:
            arqOrdenado.write(f"{numero}\n")  # Escreve cada número em uma nova linha

# insere em um arquivo os valores ordenados, pegando sempre o primeiro elemento da cada arquivo e fazendo a comparacao
def arquivoFinal(arquivos):
    while arquivos:  # enquanto houver arquivos na lista
        menorValor = None
        nomeArquivo = None
        for x in arquivos:   
            with open(x, 'r') as file:
                primeiraLinha = file.readline()  # Lê a primeira linha
                if primeiraLinha:    # verifica se tem valores no arquivo
                    primeiro_numero = int(primeiraLinha.strip())
                else:  # se não tiver elementos no arquivo, o arquivo é marcado para remoção
                    arquivos.remove(x)  # Remove diretamente da lista
                    break  # Sai do loop, pois a lista mudou

            # Verifica qual é o menor valor
            if menorValor is None or primeiro_numero < menorValor:
                menorValor = primeiro_numero
                nomeArquivo = x

        # Adiciona o menor valor no arquivo final, se encontrado
        if menorValor is not None:
            with open('resultado.txt', 'a') as resultado:  # Usar 'a' para adicionar ao arquivo
                resultado.write(str(menorValor) + '\n')

        # Remove o primeiro elemento do arquivo com o menor valor
        if nomeArquivo:
            with open(nomeArquivo, 'r') as remover:
                linhas_restantes = remover.readlines()[1:]  # Remove a primeira linha
            # Reescreve o arquivo com as linhas restantes
            with open(nomeArquivo, 'w') as reescrever:
                reescrever.writelines(linhas_restantes)

# quick sort
def quickSort(lista, inicio, fim):
    if inicio < fim:
        pivo = particionam(lista, inicio, fim)
        quickSort(lista, inicio, pivo - 1)
        quickSort(lista, pivo + 1, fim)

def particionam(lista, inicio, fim):
    esq, dir = inicio, fim
    pivo = lista[inicio]
    
    while esq < dir:
        while esq < len(lista) and lista[esq] <= pivo:
            esq += 1

        while dir >= 0 and lista[dir] > pivo:
            dir -= 1

        if esq < dir:
            lista[esq], lista[dir] = lista[dir], lista[esq]

    lista[inicio], lista[dir] = lista[dir], lista[inicio]
    return dir

mergeSortExterno(lista)