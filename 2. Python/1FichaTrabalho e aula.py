import math
import random


def main():
    print(n_triangularQ(25))


def pot2(base, expoente):
    # 8. Implemente uma função, de forma recursiva, o cálculo de x^y.
    if expoente == 0:
        return 1
    else:
        return base * pot2(base, expoente - 1)


def fact2(n):
    # 7. Implemente uma função para cálculo do fatorial de forma recursiva.
    if n == 0:
        return 1
    else:
        return n * fact2(n - 1)


def n_triangularQ(n):
    # exercício 6 da folha de exercícios
    # Escreva uma função que dado um número n, verifique se este é triangular.
    # Um nº n diz-se triangular se existir um outro número, m, tal que n = 1 + 2 + 3+ ... + m.
    # A função deverá devolver True se n é triangular e False se n for 0.
    soma = 0

    for x in range(1, n):
        soma = soma + x
        if soma == n:
            return True
    return False


def primoQ(n):
    # exercício 5 da folha de exercícios
    # Recorrendo a funções, determine se um dado número n é primo ou não.
    # Se o número for inferior a 2 deve devolver “Número inválido para verificação. Insira valor superior ou igual a 2”.
    # Para testar: print(list(map(primoQ, [2, 3, 4, 5, 6, 7, 8])))
    if n < 2:
        print("Número inválido para verificação. Insira valor superior ou igual a 2")
        exit()

    result = False
    n_divisores = 2  # 1 e n são sempre divisores
    i = 2

    for x in range(2, n):
        if n % x == 0:
            n_divisores = n_divisores + 1

    if n_divisores == 2:
        result = True

    return result


def soma_divisores(n):
    # exercício 4 da folha de exercícios
    # Escreva uma função que dado um valor n, determine a soma dos seus divisores.
    # Se o valor inserido for 0 deve devolver 0.
    soma = 0 + n  # n é sempre divisor de si próprio
    divisor = 1

    while divisor < n:
        if n % divisor == 0:
            soma = soma + divisor
        divisor = divisor + 1

    return soma


def mdc(m, n):
    # exercício 3 da folha de exercícios
    # Dados 2 valores inteiros m e n, diferentes de zero, implemente uma função que determine
    # o máximo divisor comum entre eles.
    # Ex: mdc(24, 16) = 8, ou seja, 8 é o maior inteiro possível que divide ambos.

    menor = min(m, n)
    divisor = menor

    while divisor > 0:
        if m % divisor == 0 and n % divisor == 0:
            return divisor
        divisor = divisor - 1


def fact1(n):
    # exercício 2 da folha de exercícios
    # Dado um valor inteiro positivo, determine a função fatorial.
    resultado = 1
    while n != 0:
        resultado = resultado * n
        n = n - 1
    return resultado


def pot(base, expoente):
    # exercício 1 da folha de exercícios
    # Implemente a função pot que recebe 2 argumentos dados pelo utilizador e devolve a potência entre ambos.
    # Ex: pot(2,3) = 2^3 = 8
    return base ** expoente


def exer3():
    dado = float(input("Introduza um número decimal: "))
    potencia = float(input("Introduza a potência: "))
    print("A raiz quadrada de {} é: {}".format(dado, math.sqrt(dado)))
    print("A potência de {} com expoente {} é: {}".format(dado, potencia, math.pow(dado, potencia)))
    print("O valor truncado de {} é: {}".format(dado, math.trunc(dado)))
    print("O valor arredondado de {} com duas casas decimais é: {}".format(dado, round(dado, 2)))


def exer4():
    print(random.random())
    print(random.random())
    print(random.randint(1, 10))
    print(random.randint(1, 10))


def divide_2int():
    x = int(input("Insira o 1º número: "))
    y = int(input("Insira o 2º número: "))
    s = x / y
    print("O valor da divisão de {} por {} é de {:.3f}".format(x, y, s))


def soma_2int():
    x = int(input("Insira o 1º número: "))
    y = int(input("Insira o 2º número: "))
    s = x + y
    print("A soma de {} com {} é de {}".format(x, y, s))


def exer2():
    dados = input("Introduza algo:      ")
    print("Tipo de dado:       ", type(dados))
    print("É um número?        ", dados.isnumeric())
    print("É alfanumérico?     ", dados.isalnum())
    print("É alfabético?       ", dados.isalpha())
    print("Está em maiúsculas? ", dados.isupper())
    print("Está em minúsculas? ", dados.islower())
    print("Está capitalizada?  ", dados.istitle())


def bool_pt(entrada):
    if entrada == True:
        return 'Verdadeiro'
    else:
        return 'Falso'


def exer1():
    var1 = str(input("Introduza um string: "))
    var2 = bool(input("Introduza um bool: "))
    var3 = int(input("Introduza um inteiro: "))
    var4 = float(input("Introduza um float: "))

    print("Tipo de", var1, "é ", type(var1))
    print("Tipo de", var2, "é ", type(var2))
    print("Tipo de", var3, "é ", type(var3))
    print("Tipo de", var4, "é ", type(var4))


if __name__ == '__main__':
    main()
