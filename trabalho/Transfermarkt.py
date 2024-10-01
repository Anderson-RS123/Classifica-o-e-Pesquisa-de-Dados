from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tabulate import tabulate   # biblioteca para imrimir em uma tabela os valores de um arquivo

# Variável global que será usada para armazenar os nomes dos arquivos temporários
nomeArqCriados = []

# Inicializa o navegador
pagina = webdriver.Chrome()

# Abre a página da web
pagina.get("https://www.transfermarkt.com.br/statistik/weisseweste")
wait = WebDriverWait(pagina, 10)

# Função para buscar os dados na web
def geral():
    for a in range(1, 3):  # Usado para percorer 3 páginas da web
        for x in range(1, 26):    # Usado para pegar as informações de cada jogador. Cada página possui 26 jogadores
            # Lista para armazenar os dados de um jogador
            jogador = []

            # Pega o nome de cada jogador
            nome = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"/html/body/div/main/div[1]/div[1]/div/div[3]/div/table/tbody/tr[{x}]/td[2]/table/tbody/tr[1]/td[2]/a")))
            jogador.append(nome.text)

            # Pega a idade de cada jogador
            idadeJogador = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"/html/body/div/main/div[1]/div[1]/div/div[3]/div/table/tbody/tr[{x}]/td[3]")))
            jogador.append(idadeJogador.text)

            # Pega a quantidade de partidas jogadas de cada jogador
            jogosJogados = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"/html/body/div/main/div[1]/div[1]/div/div[3]/div/table/tbody/tr[{x}]/td[6]/a")))
            jogador.append(jogosJogados.text)
            
            # Pega a quantidade de partidas sem sofrer gols de cada jogador
            semSofrer = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"/html/body/div/main/div[1]/div[1]/div/div[3]/div/table/tbody/tr[{x}]/td[7]/a")))
            jogador.append(semSofrer.text)

            # Pega a quantidade de gols sofridos de cada jogador
            golLevado = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"/html/body/div/main/div[1]/div[1]/div/div[3]/div/table/tbody/tr[{x}]/td[8]")))
            jogador.append(golLevado.text)

            # Pega o valor de mercado de cada jogador
            valorJogador = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"/html/body/div/main/div[1]/div[1]/div/div[3]/div/table/tbody/tr[{x}]/td[9]/a")))
            jogador.append(valorJogador.text)
            
            # Adiciona o jogador na lista
            escreveJogadoresNoArquivo('jogadores.txt', jogador)

        # Serve para passar para a próxima página da web    
        avancar = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[1]/div[1]/div/div[3]/div/div[2]/ul/li[11]/a")))
        avancar.click()

# Função para escrever os dados no arquivo temporário
def escreveJogadoresNoArquivo(arquivo, jogadores):
    with open(arquivo, 'a') as file:
        linha = ', '.join(jogadores) + '\n'
        file.write(linha)

# Merge Sort Externo
def mergeSortExterno(arqOriginal):
    memoria = 5  # quantidade de elementos suportada na memória
    criaArquivos(arqOriginal, memoria)  # cria os arquivos criados

    for x in nomeArqCriados:  # ordena os valores dos arquivos criados
        ordenaValores(x)

    arquivoFinal(nomeArqCriados)  #Coloca os arquivos ordenados em um arquivo final

# Funcao para separar os dados em varios arquivos
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
                with open(arqOriginal, 'r') as file:
                    linhas = file.readlines()
                    for i in range(inicioLeitura, lerAteALinha):  # insere os dados
                        arquivoNovo.write(linhas[i])
            else:
                for i in range(inicioLeitura, numeroLinhas):  # insere as linhas restantes
                    arquivoNovo.write(linhas[i])
            nomeArqCriados.append(f'arquivo{cont}.txt')
        cont += 1
        aux -= memoria  # Atualiza o número de linhas restantes

# Funcao para ordenar os valores dos arquivos
def ordenaValores(arquivo):
    vetorTemp = []  # Cria um vetor local para armazenar os valores
    # Passa os valores do arquivo para o vetor
    with open(arquivo, 'r') as file:
        vetorTemp = file.readlines()  # Lê todas as linhas para o vetor
    # Converte os valores para uma lista de listas e extrai a quantidade de gols sofridos
    vetorTemp = [linha.strip().split(', ') for linha in vetorTemp]
    # Ordena o vetor com base na quantidade de gols sofridos (usando Merge Sort)
    mergesort(vetorTemp)    
    # Escreve os jogadores ordenados de volta no arquivo
    with open(arquivo, 'w') as arqOrdenado:  # Passa os valores do vetor para o arquivo
        for jogador in vetorTemp:
            arqOrdenado.write(', '.join(jogador) + '\n')  # Escreve cada jogador em uma nova linha

# Função de Merge Sort
def mergesort(lista):
    if len(lista) > 1:   # Verifica se ainda tem mais de um elemento no arquivo
        meio = len(lista) // 2
        left_half = lista[:meio]
        right_half = lista[meio:]

        # Ficar dividindo os arquivos
        mergesort(left_half)
        mergesort(right_half)

        i = j = k = 0
        # Vai ordenar os valores dos arquivos na posição 4, que é a quantidade de gols sofridos
        while i < len(left_half) and j < len(right_half):
            if int(left_half[i][4].replace('.', '')) < int(right_half[j][4].replace('.', '')):
                lista[k] = left_half[i]
                i += 1
            else:
                lista[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lista[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lista[k] = right_half[j]
            j += 1
            k += 1

# Insere em um arquivo os valores ordenados, pegando sempre o primeiro elemento de cada arquivo e fazendo a comparação
def arquivoFinal(arquivos):
    with open('resultado.txt', 'w') as resultado:  # Abre o arquivo
        while arquivos:
            menorValor = None
            nomeArquivo = None
            for x in arquivos:
                with open(x, 'r') as file:  # Abrir cada arquivo criado
                    primeiraLinha = file.readline()  # Ler a primeira linha
                    if primeiraLinha:  # Verifica se o arquivo não está vazio
                        jogador = primeiraLinha.strip().split(', ')   # Retira os espaços
                        valor = int(jogador[4].replace('.', ''))  # Pega o valor dessa posição
                        if menorValor is None or valor < menorValor:
                            menorValor = valor    # Guarda os valores das linhas de acordo com o menor valor de gols sofrido
                            nomeArquivo = x     # Guarda o nome do arquivo que tem esse menor valor
                    else:  # Remove o arquivo da lista, para não precisar abrir ele novamente
                        arquivos.remove(x)
                        break

            if nomeArquivo:   
                with open(nomeArquivo, 'r') as file:   # Lê o primeiro valor desse arquivo
                    linhas = file.readlines()
                with open(nomeArquivo, 'w') as file:
                    file.writelines(linhas[1:])  # Remove a primeira linha do arquivo

                resultado.write(linhas[0])  # Escreve os valores no arquivo resultado.txt

geral()  
mergeSortExterno('jogadores.txt')  # Ordenar os dados



# imprime os valores do arquivo em uma tabela
from tabulate import tabulate

# Função para ler dados do arquivo
def ler_dados(arquivo):
    with open(arquivo, 'r') as file:
        linhas = file.readlines()
    
    dados = []
    for linha in linhas:
        # Remover espaços em branco e caracteres especiais
        linha = linha.strip()
        if linha:  # Verifica se a linha não está vazia
            dados.append(linha.split(', '))  # Divide os dados por vírgula
    return dados

# Caminho para o arquivo resultado.txt
arquivo_resultado = 'resultado.txt'

# Ler os dados do arquivo
dados_jogadores = ler_dados(arquivo_resultado)

# Exibir os dados em uma tabela estilizada
print(tabulate(dados_jogadores, headers=[
    "Nome", "Idade", "Jogos Jogados", "Sem sofrer gols", "Gols Sofridos", "Valor Jogador"], 
    tablefmt="fancy_grid"))
