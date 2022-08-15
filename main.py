#Eduarda Dallagrana Batista
#Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  apresentar  os  resultados  de operações que serão realizadas entre dois conjuntos de dados.


def ler(arquivo):
    with open(arquivo, 'r') as f:
        arquivo = f.readlines()
        linhas = []
        for linha in arquivo:
            linhas.append(linha.replace(" ", ""))
        return linhas


def define_operacoes(linhas):

    n_operacoes = int(linhas[0])
    operacoes = []
    l = 1

    for operacao in range(n_operacoes):
        op = linhas[l].rstrip('\n')
        l += 1
        conjunto_1 = linhas[l].rstrip('\n').split(',')
        l += 1
        conjunto_2 = linhas[l].rstrip('\n').split(',')
        l += 1
        operacoes.append((op, conjunto_1, conjunto_2))

    return operacoes


def uniao(conjunto_1, conjunto_2):
    conjunto_3 = []
    for i in conjunto_1:
        conjunto_3.append(i)
    for i in conjunto_2:
        if i not in conjunto_3:
            conjunto_3.append(i)
    return conjunto_3


def intersecao(conjunto_1, conjunto_2):
    conjunto_3 = []
    for i in conjunto_1:
        if i in conjunto_2:
            conjunto_3.append(i)
    return conjunto_3


def diferenca(conjunto_1, conjunto_2):
    conjunto_3 = []
    for i in conjunto_1:
        if i not in conjunto_2:
            conjunto_3.append(i)
    return conjunto_3


def produto_cartesiano(conjunto_1, conjunto_2):
    conjunto_3 = []
    for i in conjunto_1:
        for j in conjunto_2:
            conjunto_3.append(i + ',' + j)
    return conjunto_3


def print_resultado(operacao, conjunto_1, conjunto_2, conjunto_3):
    conjunto_1 = list_to_string(conjunto_1)
    conjunto_2 = list_to_string(conjunto_2)
    conjunto_3 = list_to_string(conjunto_3)
    str = operacao + ': conjunto 1 {' + conjunto_1 + '}, conjunto 2 {' + conjunto_2 + '}. Resultado: {' + conjunto_3 + '}'
    print(str)


def print_resultado_pc(operacao, conjunto_1, conjunto_2, conjunto_3):
    conjunto_1 = list_to_string(conjunto_1)
    conjunto_2 = list_to_string(conjunto_2)
    #conjunto_3 = list_to_string(conjunto_3)
    conjunto_pc = ""
    #print(conjunto_3)
    for i in conjunto_3:
        conjunto_pc += "(" + i + "),"

    str = operacao + ': conjunto 1 {' + conjunto_1 + '}, conjunto 2 {' + conjunto_2 + '}. Resultado: {' + conjunto_pc[:
                                                                                                                      -1] + '}'
    print(str)


def list_to_string(lista):
    string = ''
    for i in lista:
        string += i + ','
    return string[:-1]


def main():

    arquivo = input('arquivo >')
    linhas = ler(arquivo)
    operacoes = define_operacoes(linhas)

    for operacao in operacoes:

        op = operacao[0]
        conjunto_1 = operacao[1]
        conjunto_2 = operacao[2]

        if op == 'U':
            conjunto_3 = uniao(conjunto_1, conjunto_2)
            print_resultado('União', conjunto_1, conjunto_2, conjunto_3)
        elif op == 'I':
            conjunto_3 = intersecao(conjunto_1, conjunto_2)
            print_resultado('Interseção', conjunto_1, conjunto_2, conjunto_3)
        elif op == 'D':
            conjunto_3 = diferenca(conjunto_1, conjunto_2)
            print_resultado('Diferença', conjunto_1, conjunto_2, conjunto_3)
        elif op == 'C':
            conjunto_3 = produto_cartesiano(conjunto_1, conjunto_2)
            print_resultado_pc('Produto Cartesiano', conjunto_1, conjunto_2,
                               conjunto_3)


main()
