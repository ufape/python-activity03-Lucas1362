# -*- coding: utf-8 -*-

# Jamerson Lucas Tenorio
# UAG00098
# Problem Set 3 - Problem 3
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
A primeira linha de entrada contém um valor inteiro N que indica os
vários casos de teste que vem a seguir. Cada caso de teste contém um
inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de
amostras utilizadas e um caractere Tipo ('S', 'R' ou 'C'),
indicando o tipo de amostra (S:Salmão, R:Rabanete e C:Cenoura).
Exemplo:
Quantas amostras: 10
Tipo: C
Quantidade: 10
Tipo: R
Quantidade: 6
Tipo: S
Quantidade: 15
Tipo: C
Quantidade: 5
Tipo: R
Quantidade: 14
Tipo: C
Quantidade: 9
Tipo: R
Quantidade: 6
Tipo: S
Quantidade: 8
Tipo: C
Quantidade: 5
Tipo: R
Quantidade: 14

Processes:
Maria acabou de iniciar seu curso de Engenharia de Alimentos e precisa
de sua ajuda para organizar os experimentos de um laboratório o qual
ela é responsável. Ela quer saber no final do ano, quantas amostras
foram utilizadas no laboratório e o percentual de cada tipo de amostra
utilizada.

Este laboratório em especial utiliza três tipos de amostras: salmão,
rabanete e cenoura. Para obter estas informações, ela sabe exatamente
o número de experimentos que foram realizados, o tipo de amostra
utilizada e a quantidade de amostras utilizadas em cada experimento.

Output(s):
Apresente o total de amostras utilizadas, o total de cada tipo de
amostra utilizada e o percentual de cada uma em relação ao total
de amostras utilizadas, sendo que o percentual deve ser apresentado
com dois dígitos após o ponto.
Exemplo:
Total: 92 amostras
Total de cenoura: 29
Total de rabanete: 40
Total de salmão: 23
Percentual de cenoura: 31.52%
Percentual de rabanete: 43.48%
Percentual de salmão: 25.00%
"""


def main():
    
    n = int(input("Quantas amostras: "))
    total = 0
    cenoura = 0
    rabanete = 0
    salmão = 0

    for i in range(n):
        tipo = input("Tipo: ")
        quantidade = int(input("Quantidade: "))
        total += quantidade
    
        if tipo == 'S':
            salmão += quantidade
        elif tipo == 'R': 
            rabanete += quantidade
        elif tipo == 'C':
            cenoura += quantidade

    print("Total: {} amostras.".format(total))
    print("Total de cenouras: {}.".format(cenoura))
    print("Total de rabanetes: {}.".format(rabanete))
    print("Total de salmões: {}.".format(salmão))

    porcento_cenoura = (cenoura / total) * 100
    porcento_rabanete = (rabanete / total) * 100
    porcento_salmão = (salmão / total) * 100
    
    print("Percentual de cenouras: {:.2f}%".format(porcento_cenoura))
    print("Percentual de rabanetes: {:.2f}%".format(porcento_rabanete))
    print("Percentual de salmões: {:.2f}%".format(porcento_salmão))
if __name__ == '__main__':
    main()
