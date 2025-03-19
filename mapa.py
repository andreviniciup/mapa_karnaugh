import csv

# estrutura fixa do mapa (linhas CD, colunas AB)
MAPEAMENTO = [
    [0,  4, 12, 8],   
    [1,  5, 13, 9],   
    [3,  6, 14, 11], 
    [2,  7, 15, 10]   
]

def ler_csv(arquivo_csv):
    """lê o arquivo csv e retorna um dicionario com os valores de x"""
    valores = {}
    with open(arquivo_csv, 'r') as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            # converte a,b,c,d para o numero decimal 
            a = linha['a']
            b = linha['b']
            c = linha['c']
            d = linha['d']
            binario = c + d + a + b  # CDAB (formato do mapeamento)
            decimal = int(binario, 2)
            valores[decimal] = int(linha['x'])
    return valores

def criar_mapa(valores):
    """preenche o mapa seguindo a estrutura fixa"""
    mapa = []
    for linha in MAPEAMENTO:
        nova_linha = []
        for num in linha:
            nova_linha.append(valores.get(num, 0))  
        mapa.append(nova_linha)
    return mapa

def imprimir_mapa(mapa):
    """imprime o mapa no formato tradicional"""
    print("\nMapa de Karnaugh:")
    print("      AB")
    print("CD   00  01  11  10")
    print("    +---------------")
    for i, linha in enumerate(mapa):
        print(f"{['00','01','11','10'][i]} |", end=' ')
        for valor in linha:
            print(f"{valor:2}", end=' ')
        print()


valores = ler_csv('tabela.csv')
mapa = criar_mapa(valores)
imprimir_mapa(mapa)