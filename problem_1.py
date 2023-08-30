# -*- coding: utf-8 -*-

# Jamerson Lucas Tenorio Valentim
# UAG00098
# Problem Set 3 - Problem 1
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
A entrada contém dois valores inteiros.
Exemplo:
Digite um valor inteiro para X: 15
Digite um valor inteiro para Y: 12

Processes:
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos
números impares entre eles.

Output(s):
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores
ímpares que estão entre os valores fornecidos na entrada que deverá caber
em um inteiro.
Exemplo:
A soma dos números ímpares entre 15 e 12 é: 13

"""


def main():
    while True:
        n = int(input("Digite um valor para X (ou 0 para sair): "))
        if n == 0:
            break
        sequencia = ' '.join(str(i) for i in range(1, n + 1))
        print(f"A sequência até {n} é {sequencia}")


if __name__ == '__main__':
    main()
